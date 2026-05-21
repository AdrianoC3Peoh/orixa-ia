#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de PDF — Orixá IA
Conteúdo completo do site: todas as páginas e todos os textos.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fpdf import FPDF, XPos, YPos
from orixa_data import ORIXAS, PERGUNTAS, SYSTEM_PROMPT_TEMPLATE

OUTPUT = os.path.expanduser(
    "~/Documents/Claude_Peoh/output/orixa-ia-conteudo.pdf"
)
FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("AU", "", FONT_PATH)

    def _f(self, size=9):
        self.set_font("AU", size=size)

    def header(self):
        self._f(8)
        self.set_text_color(120, 80, 40)
        self.cell(0, 8, "ORIXA IA — Conteúdo Completo do Site", align="C")
        self.ln(2)
        self.set_draw_color(180, 130, 60)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-15)
        self._f(7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

    def chapter_title(self, title):
        self._f(14)
        self.set_fill_color(60, 40, 10)
        self.set_text_color(255, 220, 100)
        self.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def section_title(self, title):
        self._f(11)
        self.set_text_color(120, 60, 0)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(180, 130, 60)
        self.line(self.l_margin, self.get_y(), 200, self.get_y())
        self.set_text_color(0, 0, 0)
        self.ln(3)

    def subsection(self, title):
        self._f(10)
        self.set_text_color(80, 60, 30)
        self.cell(0, 7, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)

    def body(self, text):
        self._f(9)
        self.multi_cell(0, 5, str(text))
        self.set_x(self.l_margin)
        self.ln(2)

    def bullet(self, items, prefix="  • "):
        self._f(9)
        for item in items:
            self.multi_cell(0, 5, prefix + str(item))
            self.set_x(self.l_margin)
        self.ln(2)

    def label_val(self, label, value):
        self._f(9)
        self.set_text_color(80, 60, 30)
        lw = self.get_string_width(label + ": ") + 2
        self.cell(lw, 5, label + ": ", new_x=XPos.RIGHT, new_y=YPos.LAST)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, str(value))
        self.set_x(self.l_margin)

    def mono(self, text):
        self._f(7)
        self.set_fill_color(245, 240, 230)
        for line in str(text).split("\n"):
            if len(line) > 220:
                line = line[:220] + "..."
            self.multi_cell(0, 4, line, fill=True)
            self.set_x(self.l_margin)


def build_pdf():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(15, 20, 15)

    # CAPA
    pdf.add_page()
    pdf._f(28)
    pdf.set_text_color(120, 60, 0)
    pdf.ln(30)
    pdf.cell(0, 15, "ORIXÁ IA", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf._f(16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Conteúdo Completo do Site", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(6)
    pdf._f(11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Todas as páginas, textos e arquétipos", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Maio 2026", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(20)
    pdf.set_draw_color(180, 130, 60)
    pdf.set_line_width(1.5)
    pdf.line(40, pdf.get_y(), 170, pdf.get_y())
    pdf.set_line_width(0.2)
    pdf.ln(20)
    pdf._f(9)
    pdf.set_text_color(120, 120, 120)
    pdf.multi_cell(0, 6,
        "Documento de referência interno — arquitetura de conteúdo, "
        "arquétipos dos Orixás e fluxos do aplicativo Orixá IA.",
        align="C")
    pdf.set_text_color(0, 0, 0)

    # 01 PAGINA INICIAL
    pdf.add_page()
    pdf.chapter_title("01. PÁGINA INICIAL (index.html)")

    pdf.section_title("Hero Section")
    pdf.body(
        "Título: Descubra seu Arquétipo com os Orixás\n"
        "Subtítulo: Uma jornada de autoconhecimento baseada nos arquétipos ancestrais "
        "afro-brasileiros. Descubra seu Orixá de Frente, seus padrões comportamentais "
        "e seu potencial único."
    )
    pdf.body("Botão principal: Descobrir Meu Orixá  |  Botão secundário: Fazer Login")

    pdf.section_title("Como Funciona — 3 Etapas")
    pdf.bullet([
        "1. Questionário Comportamental — Responda 25 perguntas sobre seus padrões de decisão, emoções, relações e valores.",
        "2. Análise por Arquétipos — Nosso algoritmo identifica quais dos 10 arquétipos dos Orixás mais se alinham com seu perfil.",
        "3. Seu Resultado Personalizado — Receba seu Orixá de Frente e Orixá de Cabeça com análise detalhada.",
    ])

    pdf.section_title("Os 10 Arquétipos")
    for k, v in ORIXAS.items():
        pdf.body(f"  {v['nome']} — {v['subtitulo']}")

    pdf.section_title("Planos")
    pdf.subsection("GRATUITO — R$ 0")
    pdf.bullet([
        "Diagnóstico de Orixá de Frente e de Cabeça",
        "Análise comportamental completa",
        "Distribuição dos 10 arquétipos",
        "Localização de terreiros próximos",
    ])
    pdf.subsection("PREMIUM — R$ 29,90/mês")
    pdf.bullet([
        "Tudo do plano gratuito",
        "Chat com IA especializada no seu arquétipo",
        "Orientações personalizadas sobre decisões, carreira e relacionamentos",
        "Suporte contínuo de desenvolvimento pessoal",
    ])

    pdf.section_title("Rodapé — Aviso Legal")
    pdf.body(
        '"Orixá IA é uma ferramenta de autoconhecimento baseada em arquétipos culturais '
        'afro-brasileiros. Não substitui orientação espiritual, psicológica ou médica. '
        'Para questões espirituais genuínas, consulte um Pai ou Mãe de Santo de confiança."\n'
        '© 2024 Orixá IA. Todos os direitos reservados.'
    )

    # 02 CADASTRO / 03 LOGIN
    pdf.add_page()
    pdf.chapter_title("02. CADASTRO (cadastro.html)")
    pdf.section_title("Formulário de Cadastro")
    pdf.bullet([
        "Campo: Nome completo",
        "Campo: E-mail",
        "Campo: Senha (mínimo 6 caracteres)",
        "Campo: Código de convite (opcional — campo ORIXA2024)",
        "Botão: Criar minha conta",
    ])
    pdf.body("Link: Já tem conta? Fazer login")
    pdf.body("Nota: O código ORIXA2024 libera acesso durante a fase beta.")

    pdf.section_title("Login com Google")
    pdf.body(
        "Botão: Entrar com Google\n"
        "Fluxo: OAuth 2.0 — redireciona para Google, retorna com token, "
        "cria conta automaticamente se primeiro acesso."
    )

    pdf.ln(6)
    pdf.chapter_title("03. LOGIN (login.html)")
    pdf.section_title("Formulário de Login")
    pdf.bullet([
        "Campo: E-mail",
        "Campo: Senha",
        "Botão: Entrar",
        "Botão: Entrar com Google",
    ])
    pdf.body("Link: Não tem conta? Criar conta")

    # 04 ONBOARDING
    pdf.add_page()
    pdf.chapter_title("04. ONBOARDING (onboarding.html)")
    pdf.body("Tela de boas-vindas exibida após o primeiro login.")

    pdf.section_title("Passo 1 — O que você vai descobrir")
    pdf.bullet([
        "Seu Orixá de Frente — o arquétipo dominante do seu perfil comportamental",
        "Distribuição — como os 10 arquétipos se distribuem em você",
        "Foco — pontos fortes, atenção, carreira e relacionamentos",
    ])

    pdf.section_title("Passo 2 — Como funciona a análise")
    pdf.body(
        "Baseamos nossa análise em padrões comportamentais estudados a partir dos arquétipos dos Orixás. "
        "Não é um teste espiritual — é uma ferramenta de autoconhecimento que usa a riqueza simbólica "
        "da tradição afro-brasileira como linguagem.\n\n"
        "Não existem arquétipos melhores ou piores — cada um tem força, luz e sombra."
    )

    pdf.section_title("Passo 3 — Os 10 Arquétipos")
    pdf.body("Grade visual com os 10 Orixás e seus ícones.")
    for k, v in ORIXAS.items():
        pdf.body(f"  {v['nome']}: {v['descricao_curta']}")

    pdf.section_title("Passo 4 — Antes de começar")
    pdf.body(
        "Leia com atenção:\n"
        "• Não existe resposta certa ou errada\n"
        "• Responda como você É, não como gostaria de ser\n"
        "• Seja honesto — quanto mais honesto, mais preciso será o resultado\n"
        "• Leva cerca de 5 a 8 minutos\n\n"
        "Nota: Orixá IA é uma ferramenta de autoconhecimento, não de adivinhação. "
        "Para conhecer seu verdadeiro Orixá de cabeça, o caminho é o jogo de búzios com um Pai ou Mãe de Santo.\n\n"
        "Botão: Iniciar o Questionário"
    )

    # 05 QUESTIONÁRIO
    pdf.add_page()
    pdf.chapter_title("05. QUESTIONÁRIO (questionario.html) — 25 Perguntas")
    pdf.body("5 blocos temáticos, 5 perguntas por bloco. Seleção única por pergunta.")

    blocos = {}
    for p in PERGUNTAS:
        b = p["bloco_nome"]
        if b not in blocos:
            blocos[b] = []
        blocos[b].append(p)

    for bloco_nome, perguntas in blocos.items():
        pdf.section_title(f"Bloco: {bloco_nome}")
        for p in perguntas:
            pdf.subsection(f"P{p['id']}. {p['texto']}")
            for i, op in enumerate(p["opcoes"]):
                pdf.body(f"   ({chr(65+i)}) {op['texto']}")

    # 06 RESULTADO
    pdf.add_page()
    pdf.chapter_title("06. RESULTADO (resultado.html)")

    pdf.section_title("Cabeçalho do Resultado")
    pdf.body(
        "Exibe:\n"
        "  • Ícone + Nome do Orixá de Frente\n"
        "  • Subtítulo do arquétipo\n"
        "  • Porcentagem de afinidade\n"
        "  • Descrição curta\n"
        "  • Link: 'Ver terreiros próximos'"
    )

    pdf.section_title("Card — Orixá de Frente vs Orixá de Cabeça")
    pdf.body(
        "Orixá de Frente: arquétipo com maior pontuação no questionário.\n"
        "Orixá de Cabeça: segundo arquétipo com maior pontuação.\n\n"
        "Texto educativo:\n"
        "  Orixá de Frente: O arquétipo que mais se manifesta no seu comportamento cotidiano.\n"
        "  Orixá de Cabeça (Ori): Sua influência complementar.\n"
        "  Ori (Orixá Espiritual): Seu destino e essência espiritual única, "
        "que só pode ser revelado pelo jogo de búzios."
    )

    pdf.section_title("Seções de Análise")
    pdf.bullet([
        "Traços de Personalidade (badges com os 5 traços principais)",
        "Pontos Fortes",
        "Pontos de Atenção",
        "Tomada de Decisão",
        "Relacionamentos",
        "Carreira e Propósito",
        "Distribuição dos 10 Arquétipos (barra de progresso)",
    ])

    pdf.section_title("Indicações de Livros")
    pdf.bullet([
        "Lendas Africanas dos Orixás — Pierre Fatumbi Verger",
        "Orixá — Mãe Stella de Oxossi",
        "Candomblé da Bahia — Edison Carneiro",
        "Os Nagôs e a Morte — Juana Elbein dos Santos",
        "O Candomblé bem explicado — Pai Rodney de Oxossi",
        "Candomblé: A Religião do Axé — Reginaldo Prandi",
        "Mitologia dos Orixás — Reginaldo Prandi",
        "As Senhoras do Pajéu — Edimilson de Almeida Pereira",
    ])

    pdf.section_title("Botões de Ação")
    pdf.bullet([
        "Ver Terreiros Próximos",
        "Refazer Questionário",
        "Começar Chat (apenas usuários Premium)",
    ])

    # 07 DASHBOARD
    pdf.add_page()
    pdf.chapter_title("07. DASHBOARD (dashboard.html)")
    pdf.body("Painel do usuário após login. Exibe resumo do perfil e acesso rápido às funções.")

    pdf.section_title("Cards de Estatísticas Rápidas")
    pdf.bullet([
        "Orixá de Frente — nome e ícone do arquétipo primário",
        "Orixá de Cabeça — nome e ícone do arquétipo secundário",
        "Terreiros — link para busca de terreiros próximos",
        "Distribuição — link para a seção de distribuição no resultado",
    ])

    pdf.section_title("Ações do Dashboard")
    pdf.bullet([
        "Ver Análise Completa",
        "Iniciar/Refazer Questionário",
        "Acessar Chat IA (Premium)",
        "Buscar Terreiros",
    ])

    # 08 CHAT
    pdf.add_page()
    pdf.chapter_title("08. CHAT IA (chat.html)")
    pdf.body("Funcionalidade exclusiva para usuários Premium.")

    pdf.section_title("Interface do Chat")
    pdf.bullet([
        "Cabeçalho: ícone do Orixá de Frente + nome + botão 'Nova conversa'",
        "Área de mensagens com histórico persistente",
        "Campo de input de texto + botão Enviar",
        "Mensagem de boas-vindas automática ao abrir o chat",
    ])

    pdf.section_title("Mensagem de Boas-vindas")
    pdf.body(
        "Olá! Sou seu conselheiro baseado no arquétipo [Orixá de Frente] "
        "e Orixá de Cabeça [Orixá de Cabeça]. Estou aqui para ajudar você a entender "
        "seus padrões comportamentais, decisões e relacionamentos com base no seu perfil.\n\n"
        "Pode me fazer qualquer pergunta sobre sua vida, carreira, relacionamentos ou decisões."
    )

    pdf.section_title("Regras do System Prompt")
    pdf.bullet([
        "Voz de conselheiro — 'Com base no seu perfil...', 'Percebo que você tende a...'",
        "Respeito à tradição — tratar os Orixás com seriedade e reverência",
        "Clareza sobre probabilidades — 'é provável que', 'uma tendência comum é'",
        "Recomendação ao terreiro — para questões espirituais, sempre indicar visita a terreiro",
        "Incluir o secundário — mencionar como o Orixá de Cabeça complementa o primário",
        "Tom sério, caloroso, respeitoso — 3 a 5 parágrafos por resposta",
    ])

    # 09 TERREIROS
    pdf.add_page()
    pdf.chapter_title("09. TERREIROS (terreiros.html)")
    pdf.body("Página de busca de espaços religiosos próximos ao usuário.")

    pdf.section_title("Sistema de Busca")
    pdf.body(
        "Ao carregar a página, o sistema solicita geolocalização do dispositivo.\n"
        "Busca simultânea em duas fontes:\n"
        "  1. Banco de dados interno (centros cadastrados no app)\n"
        "  2. Overpass API (OpenStreetMap) — busca terreiros reais num raio de 10km\n\n"
        "Os resultados são mesclados, deduplicados por nome e ordenados por distância (km).\n"
        "Exibe no máximo 15 resultados."
    )

    pdf.section_title("Cards de Resultado")
    pdf.bullet([
        "Nome do terreiro/centro",
        "Distância em km",
        "Endereço (quando disponível)",
        "Telefone (quando disponível)",
        "Badge: 'Cadastrado' (verde) ou 'OpenStreetMap' (terra)",
        "Botão: Abrir no Google Maps",
    ])

    pdf.section_title("Sem Resultados")
    pdf.body(
        "Caso nenhum terreiro seja encontrado na região, exibe link para busca "
        "automática no Google Maps: 'Buscar terreiros de candomblé e umbanda próximos'."
    )

    pdf.section_title("Cadastro de Novo Terreiro (Admin)")
    pdf.body(
        "Formulário para administradores cadastrarem novos centros: "
        "nome, tradição, descrição, endereço, bairro, cidade, estado, telefone, e-mail, site."
    )

    # 10 PREMIUM
    pdf.add_page()
    pdf.chapter_title("10. ASSINAR PREMIUM (assinar.html)")

    pdf.section_title("Benefícios Premium")
    pdf.bullet([
        "Chat com IA personalizado no seu Orixá de Frente",
        "Orientações sobre decisões importantes de carreira e vida",
        "Análise de relacionamentos baseada no seu arquétipo",
        "Suporte contínuo de autoconhecimento",
    ])
    pdf.section_title("Preço")
    pdf.body("R$ 29,90 / mês — Simulação de pagamento (modo desenvolvimento)")

    pdf.section_title("Formulário de Assinatura")
    pdf.bullet([
        "Campo: Código de desconto (opcional)",
        "Botão: Assinar Premium",
        "Nota: Em modo de desenvolvimento, qualquer código ativa o Premium para teste",
    ])

    # 11 ARQUETIPOS
    pdf.add_page()
    pdf.chapter_title("11. ARQUÉTIPOS DOS ORIXÁS — CONTEÚTO COMPLETO")

    for key, o in ORIXAS.items():
        pdf.add_page()
        pdf.section_title(f"{o['nome'].upper()} — {o['subtitulo']}")

        pdf.label_val("Descrição curta", o["descricao_curta"])
        pdf.ln(2)
        pdf.subsection("Descrição Completa")
        pdf.body(o["descricao"])

        pdf.subsection("Traços de Personalidade")
        pdf.body(", ".join(o["tracos"]))

        pdf.subsection("Pontos Fortes")
        pdf.bullet(o["pontos_fortes"])

        pdf.subsection("Pontos de Atenção")
        pdf.bullet(o["pontos_atencao"])

        pdf.subsection("Tomada de Decisão")
        pdf.body(o["tomada_decisao"])

        pdf.subsection("Relacionamentos")
        pdf.body(o["relacionamentos"])

        pdf.subsection("Carreira e Propósito")
        pdf.body(o["carreira"])

        pdf.label_val("Símbolo Cultural", o["simbolo_cultural"])
        pdf.label_val("Elementos", ", ".join(o["elementos"]))

    # 12 PERGUNTAS COM PESOS
    pdf.add_page()
    pdf.chapter_title("12. QUESTIONÁRIO — PERGUNTAS E PESOS (REFERÊNCIA TÉCNICA)")
    pdf.body("Esta seção documenta o algoritmo de cálculo. Os pesos não são exibidos ao usuário.")

    for p in PERGUNTAS:
        pdf._f(9)
        pdf.set_text_color(80, 40, 0)
        pdf.multi_cell(0, 5, f"P{p['id']} [{p['bloco_nome']}] — {p['texto']}")
        pdf.set_x(pdf.l_margin)
        pdf.set_text_color(0, 0, 0)
        for i, op in enumerate(p["opcoes"]):
            pesos_str = ", ".join(f"{k}+{v}" for k, v in op["pesos"].items())
            pdf._f(8)
            pdf.multi_cell(0, 4, f"   ({chr(65+i)}) {op['texto']} [{pesos_str}]")
            pdf.set_x(pdf.l_margin)
        pdf.ln(2)

    # 13 SYSTEM PROMPT
    pdf.add_page()
    pdf.chapter_title("13. SYSTEM PROMPT DA IA (REFERÊNCIA)")
    pdf.body("Template usado para configurar o modelo Claude ao iniciar cada sessão de chat.")
    pdf.mono(SYSTEM_PROMPT_TEMPLATE)

    # SALVAR
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    pdf.output(OUTPUT)
    print(f"\nPDF gerado com sucesso!")
    print(f"Arquivo: {OUTPUT}")
    print(f"Total de páginas: {pdf.page}")


if __name__ == "__main__":
    build_pdf()
