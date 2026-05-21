# Orixá IA 🌿

Plataforma de autoconhecimento baseada nos arquétipos dos Orixás do Candomblé e Umbanda. O usuário responde um questionário e descobre seu Orixá primário e secundário, com interpretação personalizada via IA.

## Funcionalidades

- Questionário com 25 perguntas e cálculo de afinidade com 10 Orixás
- Resultado com perfil primário e secundário, scores e percentuais
- Chat com IA (Claude Haiku) contextualizado ao arquétipo do usuário
- Autenticação por e-mail/senha e Google OAuth
- Recuperação de senha por token
- Mapa de terreiros por cidade
- Geração de PDF com relatório completo
- Plano premium com conteúdo exclusivo

---

## Requisitos

- Python 3.10+
- Conta na [Anthropic](https://console.anthropic.com) para a chave de API
- Projeto no [Google Cloud Console](https://console.cloud.google.com) para OAuth

---

## Instalação local

### 1. Clone o repositório

```bash
git clone https://github.com/AdrianoC3Peoh/orixa-ia.git
cd orixa-ia
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com seus dados:

| Variável | Onde obter |
|---|---|
| `SECRET_KEY` | Gere com `python3 -c "import secrets; print(secrets.token_hex(32))"` |
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com/settings/keys) |
| `GOOGLE_CLIENT_ID` | Google Cloud Console (veja abaixo) |
| `GOOGLE_CLIENT_SECRET` | Google Cloud Console (veja abaixo) |

### 5. Configure o Google OAuth

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Crie um projeto (ou use um existente)
3. Vá em **APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID**
4. Tipo: **Web application**
5. Em **Authorized redirect URIs**, adicione:
   - `http://localhost:8000/auth/google/callback`
6. Copie o **Client ID** e **Client Secret** para o `.env`

> Para uso remoto (ngrok, Railway etc.), adicione também a URL remota como redirect URI no Google Console e deixe `GOOGLE_REDIRECT_URI=` vazio no `.env` — a detecção é automática.

### 6. Inicie o servidor

```bash
uvicorn main:app --reload
```

Acesse em: [http://localhost:8000](http://localhost:8000)

---

## Deploy no Railway

1. Crie uma conta em [railway.app](https://railway.app)
2. Faça deploy direto do GitHub (selecione este repositório)
3. Configure as mesmas variáveis do `.env` em **Variables**
4. O `Procfile` já está configurado para iniciar o servidor

---

## Estrutura do projeto

```
orixa-ia/
├── main.py            # Rotas FastAPI, autenticação, OAuth, chat
├── database.py        # Modelos SQLAlchemy e dados iniciais
├── orixa_data.py      # Dados dos 10 arquétipos, perguntas e system prompt
├── auth.py            # Helpers JWT e hash de senha
├── gerar_pdf.py       # Gerador de PDF com todo o conteúdo do site
├── templates/         # Templates Jinja2 (HTML)
│   ├── base.html
│   ├── index.html
│   ├── cadastro.html
│   ├── login.html
│   ├── esqueci_senha.html
│   ├── resetar_senha.html
│   ├── onboarding.html
│   ├── questionario.html
│   ├── resultado.html
│   ├── dashboard.html
│   ├── chat.html
│   ├── terreiros.html
│   └── premium.html
├── static/            # CSS, JS e imagens
├── requirements.txt
├── Procfile           # Configuração Railway
├── railway.json
└── .env.example       # Template de variáveis de ambiente
```

---

## Variáveis de ambiente

Veja o arquivo [`.env.example`](.env.example) para a lista completa.

---

## Licença

Projeto privado — todos os direitos reservados.
