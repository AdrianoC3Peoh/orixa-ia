import os
import json
import secrets
from dotenv import load_dotenv
load_dotenv(override=True)
from typing import Optional, List
from urllib.parse import urlencode
from fastapi import FastAPI, Request, Depends, HTTPException, Form, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
import httpx
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

import math
from database import get_db, init_db, User, Resultado, MensagemChat, Centro
from auth import (
    hash_senha, verificar_senha, criar_token,
    get_usuario_atual, require_usuario, require_premium,
    get_token_from_request, decodificar_token
)
from orixa_data import ORIXAS, PERGUNTAS, calcular_resultado, build_system_prompt

try:
    import anthropic
    ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    ai_client = anthropic.Anthropic(api_key=ANTHROPIC_KEY) if ANTHROPIC_KEY else None
except ImportError:
    ai_client = None

app = FastAPI(title="Orixá IA", docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory="templates")

try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass

init_db()


# ─── Pydantic models ─────────────────────────────────────────────────────────

CODIGO_CONVITE = os.getenv("CODIGO_CONVITE", "ORIXA2024")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback")
GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"

class RegisterRequest(BaseModel):
    nome: str
    email: str
    senha: str
    codigo_convite: str = ""

class LoginRequest(BaseModel):
    email: str
    senha: str

class QuestionarioRequest(BaseModel):
    respostas: dict  # {pergunta_id: opcao_index}
    disclaimer_aceito: bool = True

class ChatRequest(BaseModel):
    mensagem: str

class UpgradeRequest(BaseModel):
    codigo: str = ""  # código de desconto ou simulação de pagamento


# ─── Helpers ─────────────────────────────────────────────────────────────────

def get_resultado_usuario(user_id: int, db: Session) -> Optional[Resultado]:
    return (
        db.query(Resultado)
        .filter(Resultado.user_id == user_id)
        .order_by(Resultado.criado_em.desc())
        .first()
    )


def render(request: Request, template: str, ctx: dict = {}, status_code: int = 200):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    resultado = get_resultado_usuario(usuario.id, db) if usuario else None
    ctx["request"] = request
    ctx["usuario"] = usuario
    ctx["resultado"] = resultado
    ctx["orixas"] = ORIXAS
    return templates.TemplateResponse(template, ctx, status_code=status_code)


# ─── Páginas HTML ─────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return render(request, "index.html")


@app.get("/cadastro", response_class=HTMLResponse)
async def cadastro_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if usuario:
        return RedirectResponse("/onboarding" if not usuario.disclaimer_aceito else "/questionario")
    return render(request, "cadastro.html")


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if usuario:
        return RedirectResponse("/dashboard")
    return render(request, "login.html")


@app.get("/onboarding", response_class=HTMLResponse)
async def onboarding_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if not usuario:
        return RedirectResponse("/login")
    return render(request, "onboarding.html")


@app.get("/questionario", response_class=HTMLResponse)
async def questionario_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if not usuario:
        return RedirectResponse("/login")
    resultado = get_resultado_usuario(usuario.id, db)
    if resultado:
        return RedirectResponse("/resultado")
    return render(request, "questionario.html", {"perguntas": PERGUNTAS})


@app.get("/resultado", response_class=HTMLResponse)
async def resultado_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if not usuario:
        return RedirectResponse("/login")
    resultado = get_resultado_usuario(usuario.id, db)
    if not resultado:
        return RedirectResponse("/questionario")
    dados = calcular_resultado(resultado.respostas)
    return render(request, "resultado.html", {"dados": dados, "resultado": resultado})


@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if not usuario:
        return RedirectResponse("/login")
    resultado = get_resultado_usuario(usuario.id, db)
    if not resultado:
        return RedirectResponse("/questionario")
    if not usuario.is_premium:
        return render(request, "assinar.html", {})
    historico = (
        db.query(MensagemChat)
        .filter(MensagemChat.user_id == usuario.id)
        .order_by(MensagemChat.criado_em.asc())
        .limit(50)
        .all()
    )
    dados = calcular_resultado(resultado.respostas)
    return render(request, "chat.html", {"historico": historico, "dados": dados})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if not usuario:
        return RedirectResponse("/login")
    resultado = get_resultado_usuario(usuario.id, db)
    if not resultado:
        return RedirectResponse("/onboarding" if not usuario.disclaimer_aceito else "/questionario")
    dados = calcular_resultado(resultado.respostas)
    return render(request, "dashboard.html", {"dados": dados})


@app.get("/assinar", response_class=HTMLResponse)
async def assinar_page(request: Request):
    db = next(get_db())
    usuario = get_usuario_atual(request, db)
    if not usuario:
        return RedirectResponse("/login")
    if usuario.is_premium:
        return RedirectResponse("/chat")
    return render(request, "assinar.html", {})


@app.get("/terreiros", response_class=HTMLResponse)
async def terreiros_page(request: Request):
    db = next(get_db())
    centros = db.query(Centro).filter(Centro.ativo == True).order_by(Centro.cidade).all()
    return render(request, "terreiros.html", {"centros": centros})


@app.get("/api/terreiros/proximos")
async def api_terreiros_proximos(
    lat: float,
    lng: float,
    raio: float = 50,
    db: Session = Depends(get_db),
):
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        return R * 2 * math.asin(math.sqrt(a))

    centros = db.query(Centro).filter(Centro.ativo == True, Centro.latitude != None).all()
    resultado = []
    for c in centros:
        dist = haversine(lat, lng, c.latitude, c.longitude)
        if dist <= raio:
            resultado.append({
                "id": c.id,
                "nome": c.nome,
                "tradicao": c.tradicao,
                "endereco": c.endereco,
                "cidade": c.cidade,
                "estado": c.estado,
                "telefone": c.telefone,
                "site": c.site,
                "distancia_km": round(dist, 1),
            })
    resultado.sort(key=lambda x: x["distancia_km"])
    return {"terreiros": resultado[:10], "total": len(resultado)}


@app.get("/sair")
async def sair(response: Response):
    resp = RedirectResponse("/", status_code=302)
    resp.delete_cookie("token")
    return resp


# ─── Google OAuth ─────────────────────────────────────────────────────────────

@app.get("/auth/google")
async def google_login():
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(503, "Google OAuth não configurado. Adicione GOOGLE_CLIENT_ID no .env")
    state = secrets.token_urlsafe(16)
    params = urlencode({
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
        "access_type": "online",
        "prompt": "select_account",
    })
    resp = RedirectResponse(f"{GOOGLE_AUTH_URL}?{params}", status_code=302)
    resp.set_cookie("oauth_state", state, max_age=300, httponly=True, samesite="lax")
    return resp


@app.get("/auth/google/callback")
async def google_callback(
    request: Request,
    code: str = None,
    state: str = None,
    error: str = None,
    db: Session = Depends(get_db),
):
    if error:
        return RedirectResponse(f"/login?erro={error}", status_code=302)

    stored_state = request.cookies.get("oauth_state")
    if not state or state != stored_state:
        return RedirectResponse("/login?erro=state_invalido", status_code=302)

    if not code:
        return RedirectResponse("/login?erro=sem_codigo", status_code=302)

    async with httpx.AsyncClient() as client:
        token_resp = await client.post(
            GOOGLE_TOKEN_URL,
            data={
                "code": code,
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "redirect_uri": GOOGLE_REDIRECT_URI,
                "grant_type": "authorization_code",
            },
        )
        if token_resp.status_code != 200:
            return RedirectResponse("/login?erro=token_falhou", status_code=302)

        token_data = token_resp.json()
        access_token = token_data.get("access_token")

        userinfo_resp = await client.get(
            GOOGLE_USERINFO_URL,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        if userinfo_resp.status_code != 200:
            return RedirectResponse("/login?erro=userinfo_falhou", status_code=302)

        info = userinfo_resp.json()

    google_id = info.get("id")
    email = info.get("email", "").lower().strip()
    nome = info.get("name", email.split("@")[0])

    user = db.query(User).filter(User.google_id == google_id).first()
    if not user:
        user = db.query(User).filter(User.email == email).first()
        if user:
            user.google_id = google_id
        else:
            user = User(nome=nome, email=email, google_id=google_id, disclaimer_aceito=False)
            db.add(user)
        db.commit()
        db.refresh(user)

    token = criar_token({"sub": str(user.id)})
    resultado = get_resultado_usuario(user.id, db)
    if resultado:
        redirect = "/resultado"
    elif not user.disclaimer_aceito:
        redirect = "/onboarding"
    else:
        redirect = "/questionario"

    resp = RedirectResponse(redirect, status_code=302)
    resp.set_cookie("token", token, max_age=7 * 24 * 3600, httponly=False, samesite="lax")
    resp.delete_cookie("oauth_state")
    return resp


# ─── API Endpoints ────────────────────────────────────────────────────────────

@app.post("/api/auth/cadastro")
async def api_cadastro(data: RegisterRequest, db: Session = Depends(get_db)):
    if data.codigo_convite.upper() != CODIGO_CONVITE.upper():
        raise HTTPException(400, "Código de convite inválido. Solicite o código ao administrador.")
    if db.query(User).filter(User.email == data.email.lower()).first():
        raise HTTPException(400, "E-mail já cadastrado")
    if len(data.senha) < 6:
        raise HTTPException(400, "Senha deve ter ao menos 6 caracteres")
    user = User(
        nome=data.nome.strip(),
        email=data.email.lower().strip(),
        senha_hash=hash_senha(data.senha),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = criar_token({"sub": str(user.id)})
    return {"token": token, "nome": user.nome, "email": user.email}


@app.post("/api/auth/login")
async def api_login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email.lower().strip()).first()
    if not user or not verificar_senha(data.senha, user.senha_hash):
        raise HTTPException(401, "E-mail ou senha incorretos")
    token = criar_token({"sub": str(user.id)})
    resultado = get_resultado_usuario(user.id, db)
    redirect = "/resultado" if resultado else ("/questionario" if user.disclaimer_aceito else "/onboarding")
    return {"token": token, "nome": user.nome, "redirect": redirect}


@app.post("/api/onboarding/aceitar")
async def api_aceitar_disclaimer(
    request: Request,
    db: Session = Depends(get_db),
):
    usuario = require_usuario(request, db)
    usuario.disclaimer_aceito = True
    db.commit()
    return {"ok": True, "redirect": "/questionario"}


@app.post("/api/questionario/submeter")
async def api_submeter_questionario(
    data: QuestionarioRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    usuario = require_usuario(request, db)
    if len(data.respostas) < len(PERGUNTAS):
        raise HTTPException(400, f"Responda todas as {len(PERGUNTAS)} perguntas")

    dados = calcular_resultado(data.respostas)
    resultado = Resultado(
        user_id=usuario.id,
        primario=dados["primario"],
        secundario=dados["secundario"],
        scores=dados["scores"],
        percentuais=dados["percentuais"],
        respostas=data.respostas,
    )
    db.add(resultado)
    if data.disclaimer_aceito:
        usuario.disclaimer_aceito = True
    db.commit()
    return {"ok": True, "redirect": "/resultado"}


@app.get("/api/resultado")
async def api_resultado(request: Request, db: Session = Depends(get_db)):
    usuario = require_usuario(request, db)
    resultado = get_resultado_usuario(usuario.id, db)
    if not resultado:
        raise HTTPException(404, "Resultado não encontrado")
    dados = calcular_resultado(resultado.respostas)
    return {
        "primario": dados["primario"],
        "secundario": dados["secundario"],
        "primario_data": dados["primario_data"],
        "secundario_data": dados["secundario_data"],
        "percentuais": dados["percentuais"],
        "ranking": dados["ranking"],
        "is_premium": usuario.is_premium,
    }


@app.post("/api/chat")
async def api_chat(
    data: ChatRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    usuario = require_premium(request, db)
    resultado = get_resultado_usuario(usuario.id, db)
    if not resultado:
        raise HTTPException(400, "Complete o questionário primeiro")

    dados = calcular_resultado(resultado.respostas)
    system_prompt = build_system_prompt(dados)

    historico = (
        db.query(MensagemChat)
        .filter(MensagemChat.user_id == usuario.id)
        .order_by(MensagemChat.criado_em.asc())
        .limit(20)
        .all()
    )

    messages = [{"role": m.role, "content": m.conteudo} for m in historico]
    messages.append({"role": "user", "content": data.mensagem})

    if ai_client:
        try:
            response = ai_client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1024,
                system=system_prompt,
                messages=messages,
            )
            resposta = response.content[0].text
        except Exception as e:
            resposta = f"Erro ao conectar com a IA: {str(e)}"
    else:
        orixa = dados["primario_data"]
        resposta = (
            f"[Modo demo — configure ANTHROPIC_API_KEY para IA real]\n\n"
            f"Seu perfil {orixa['nome']} sugere que: {orixa['tomada_decisao']}"
        )

    db.add(MensagemChat(user_id=usuario.id, role="user", conteudo=data.mensagem))
    db.add(MensagemChat(user_id=usuario.id, role="assistant", conteudo=resposta))
    db.commit()

    return {"resposta": resposta}


@app.post("/api/premium/ativar")
async def api_ativar_premium(
    data: UpgradeRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    usuario = require_usuario(request, db)
    # Em produção: integrar Stripe/PagSeguro aqui
    # Por ora, qualquer código "DEMO2024" ativa
    codigos_validos = {"DEMO2024", "ORIXA2024", "BETA100"}
    if data.codigo.upper() not in codigos_validos and data.codigo != "":
        # Aceita string vazia para demo (simula pagamento)
        pass
    usuario.is_premium = True
    db.commit()
    return {"ok": True, "redirect": "/chat", "mensagem": "Premium ativado com sucesso!"}


@app.delete("/api/chat/limpar")
async def api_limpar_chat(request: Request, db: Session = Depends(get_db)):
    usuario = require_usuario(request, db)
    db.query(MensagemChat).filter(MensagemChat.user_id == usuario.id).delete()
    db.commit()
    return {"ok": True}


@app.delete("/api/resultado/resetar")
async def api_resetar_resultado(request: Request, db: Session = Depends(get_db)):
    usuario = require_usuario(request, db)
    db.query(Resultado).filter(Resultado.user_id == usuario.id).delete()
    db.query(MensagemChat).filter(MensagemChat.user_id == usuario.id).delete()
    db.commit()
    return {"ok": True, "redirect": "/questionario"}


@app.get("/api/me")
async def api_me(request: Request, db: Session = Depends(get_db)):
    usuario = require_usuario(request, db)
    resultado = get_resultado_usuario(usuario.id, db)
    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "is_premium": usuario.is_premium,
        "disclaimer_aceito": usuario.disclaimer_aceito,
        "tem_resultado": resultado is not None,
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("ENVIRONMENT", "production") == "development"
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=reload)
