from typing import Dict, List

ORIXAS: Dict[str, dict] = {
    "ogum": {
        "nome": "Ogum",
        "subtitulo": "O Guerreiro dos Caminhos",
        "cor": "#4A90D9",
        "cor_secundaria": "#1a3a5c",
        "emoji": "⚔️",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="2" x2="12" y2="18"/><line x1="8" y1="8" x2="16" y2="8"/><path d="M10 18 L12 22 L14 18"/></svg>',
        "gradiente": "from-blue-600 to-blue-900",
        "descricao_curta": "Arquétipo da ação, determinação e abertura de caminhos.",
        "descricao": (
            "O arquétipo Ogum representa o perfil de ação imediata, determinação e capacidade de "
            "abrir caminhos onde outros veem obstáculos. Perfis Ogum são naturalmente líderes na execução, "
            "possuem alta tolerância ao conflito e preferem a prática à teoria. São os primeiros a agir "
            "e os últimos a desistir."
        ),
        "tracos": ["Determinação", "Objetividade", "Resiliência", "Coragem", "Execução"],
        "pontos_fortes": [
            "Capacidade excepcional de execução",
            "Liderança direta e eficaz",
            "Resiliência diante de obstáculos",
            "Tomada de decisão rápida sob pressão",
            "Abertura de novos caminhos e possibilidades",
        ],
        "pontos_atencao": [
            "Tendência à impulsividade em decisões complexas",
            "Dificuldade com ambiguidade prolongada",
            "Comunicação pode ser percebida como agressiva",
            "Excesso de independência pode isolar",
            "Dificuldade em delegar ou pedir ajuda",
        ],
        "tomada_decisao": (
            "Perfis Ogum decidem melhor sob pressão e com informações concretas. "
            "Evite análise em excesso — seu instinto executivo é seu maior diferencial. "
            "Atenção: decisões tomadas na raiva tendem ao arrependimento."
        ),
        "relacionamentos": (
            "Em relações, Ogum é protetor e leal, mas pode parecer frio ou controlador. "
            "Demonstra afeto através de ações práticas. Precisa de parceiros que respeitem sua independência."
        ),
        "carreira": (
            "Perfis Ogum se destacam em ambientes de alta pressão: empreendedorismo, "
            "liderança executiva, forças militares, construção, tecnologia, esportes de competição."
        ),
        "simbolo_cultural": "Ferro, ferramentas, caminhos",
        "elementos": ["ferro", "trabalho", "caminhos", "guerreiro"],
        "cores": ["Azul marinho", "Verde", "Preto"],
        "datas": [
            {"data": "Terça-feira", "significado": "Dia semanal de Ogum — ideal para iniciar projetos e superar obstáculos"},
            {"data": "23 de abril", "significado": "Festa de São Jorge, sincretizado com Ogum — celebração da força e da abertura de caminhos"},
        ],
        "praticas": [
            "Comece o dia escrevendo um obstáculo que quer vencer. À noite, registre o que fez para avançar.",
            "Exercício físico pela manhã ativa sua energia natural de ação e clareza.",
            "Antes de uma decisão importante, pergunte a si mesmo: 'Isso abre ou fecha caminhos?'",
        ],
    },
    "oxossi": {
        "nome": "Oxóssi",
        "subtitulo": "O Estrategista da Abundância",
        "cor": "#2ECC71",
        "cor_secundaria": "#1a4a2e",
        "emoji": "🏹",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 18 Q2 12 6 6"/><line x1="6" y1="6" x2="6" y2="18"/><line x1="6" y1="12" x2="20" y2="12"/><polyline points="17,9 20,12 17,15"/></svg>',
        "gradiente": "from-green-600 to-green-900",
        "descricao_curta": "Arquétipo do foco, estratégia e conexão com o essencial.",
        "descricao": (
            "O arquétipo Oxóssi representa o perfil analítico-estratégico, capaz de focar com "
            "precisão cirúrgica no objetivo. Perfis Oxóssi observam antes de agir, planejam com "
            "paciência e raramente erram o alvo. São excelentes em ambientes que exigem concentração "
            "e pensamento estratégico de longo prazo."
        ),
        "tracos": ["Foco", "Estratégia", "Paciência", "Observação", "Precisão"],
        "pontos_fortes": [
            "Capacidade analítica e estratégica excepcional",
            "Paciência e foco prolongados",
            "Precisão na execução de planos",
            "Independência e autossuficiência",
            "Forte conexão com a natureza e o essencial",
        ],
        "pontos_atencao": [
            "Pode demorar demais para agir",
            "Isolamento excessivo",
            "Dificuldade em trabalho colaborativo intenso",
            "Perfeccionismo paralisante",
            "Comunicação introspectiva pode ser mal interpretada",
        ],
        "tomada_decisao": (
            "Perfis Oxóssi decidem melhor com tempo, informações completas e silêncio. "
            "Ambientes barulhentos ou com pressa prejudicam sua clareza. "
            "Confie em sua análise — quando Oxóssi mira, raramente erra."
        ),
        "relacionamentos": (
            "Em relações, Oxóssi é leal mas precisa de espaço. Demonstra afeto através de presença "
            "e experiências compartilhadas. Evita conflito direto, preferindo se afastar temporariamente."
        ),
        "carreira": (
            "Perfis Oxóssi se destacam em: pesquisa, ciência, tecnologia, programação, "
            "consultoria estratégica, medicina, natureza e ecologia."
        ),
        "simbolo_cultural": "Arco e flecha, floresta, caça",
        "elementos": ["floresta", "estratégia", "caça", "natureza"],
        "cores": ["Verde escuro", "Azul turquesa", "Marrom terra"],
        "datas": [
            {"data": "Quinta-feira", "significado": "Dia de Oxóssi — propício para planejamento, estudo e foco profundo"},
            {"data": "20 de janeiro", "significado": "Celebração do caçador em algumas casas — momento de renovar intenções e alinhar estratégia"},
        ],
        "praticas": [
            "Reserve 15 minutos de silêncio diário para planejar. Oxóssi não desperdiça flechas.",
            "Antes de qualquer decisão, escreva: 'Qual é exatamente o meu objetivo aqui?'",
            "Passe tempo na natureza semanalmente — árvores, parques, trilhas — para recarregar o foco.",
        ],
    },
    "xango": {
        "nome": "Xangô",
        "subtitulo": "O Soberano da Justiça",
        "cor": "#E74C3C",
        "cor_secundaria": "#5c1a1a",
        "emoji": "⚡",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="15,2 9,13 13,13 9,22 15,11 11,11"/></svg>',
        "gradiente": "from-red-600 to-red-900",
        "descricao_curta": "Arquétipo da justiça, autoridade e poder equilibrado.",
        "descricao": (
            "O arquétipo Xangô representa o perfil de liderança com autoridade e senso de justiça. "
            "Perfis Xangô são magnéticos, moralmente firmes e naturalmente respeitados. "
            "Possuem habilidade inata para arbitrar conflitos e impor ordem onde há caos. "
            "Sua força vem do equilíbrio entre poder e responsabilidade."
        ),
        "tracos": ["Justiça", "Autoridade", "Carisma", "Firmeza", "Equilíbrio"],
        "pontos_fortes": [
            "Liderança carismática e respeitada",
            "Forte senso de justiça e ética",
            "Capacidade de arbitrar e mediar conflitos",
            "Presença magnética e autoridade natural",
            "Tomada de decisão equilibrada e firme",
        ],
        "pontos_atencao": [
            "Tendência ao orgulho e dificuldade em reconhecer erros",
            "Intolerância com a injustiça pode gerar conflitos",
            "Pode ser excessivamente rígido",
            "Dificuldade em aceitar críticas",
            "Expectativas muito altas sobre os outros",
        ],
        "tomada_decisao": (
            "Perfis Xangô decidem melhor quando têm clareza sobre princípios e impactos. "
            "São excelentes em decisões que envolvem ética, poder e responsabilidade coletiva. "
            "Cuidado com o orgulho que pode bloquear revisões necessárias."
        ),
        "relacionamentos": (
            "Em relações, Xangô é protetor e leal, mas exige respeito mútuo. "
            "Pode ser dominante. Precisa de parceiros que tenham sua própria força."
        ),
        "carreira": (
            "Perfis Xangô se destacam em: direito, política, liderança executiva, judiciário, "
            "gestão de pessoas, mediação, diplomacia, academia."
        ),
        "simbolo_cultural": "Raio, pedra, balança",
        "elementos": ["trovão", "fogo", "justiça", "poder"],
        "cores": ["Vermelho", "Branco", "Marrom"],
        "datas": [
            {"data": "Quarta-feira", "significado": "Dia de Xangô — propício para questões de justiça, liderança e acordos importantes"},
            {"data": "29 de junho", "significado": "Festa de São Pedro, sincretizado com Xangô em algumas tradições — celebração da autoridade justa"},
        ],
        "praticas": [
            "Antes de julgar uma situação ou pessoa, pergunte: 'Tenho todos os fatos?'",
            "Quando sentir indignação com injustiça, canalize-a em ação concreta — não apenas em raiva.",
            "Honre seus compromissos como honraria uma lei: sua palavra é seu maior símbolo de autoridade.",
        ],
    },
    "iansa": {
        "nome": "Iansã",
        "subtitulo": "A Força dos Ventos e da Mudança",
        "cor": "#E67E22",
        "cor_secundaria": "#5c3a1a",
        "emoji": "🌪️",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="5" y1="19" x2="19" y2="5"/><line x1="5" y1="5" x2="19" y2="19"/><line x1="5" y1="5" x2="3" y2="3"/><line x1="19" y1="5" x2="21" y2="3"/></svg>',
        "gradiente": "from-orange-600 to-orange-900",
        "descricao_curta": "Arquétipo da paixão, liberdade e transformação contínua.",
        "descricao": (
            "O arquétipo Iansã representa o perfil de alta energia emocional, amor pela liberdade "
            "e capacidade de liderar através do carisma e da paixão. Perfis Iansã são tempestades "
            "que movem tudo ao redor — criativos, intensos, corajosos e absolutamente imprevisíveis. "
            "Sua força está na autenticidade radical."
        ),
        "tracos": ["Paixão", "Liberdade", "Intensidade", "Coragem", "Espontaneidade"],
        "pontos_fortes": [
            "Energia e carisma magnéticos",
            "Coragem para enfrentar o desconhecido",
            "Criatividade e pensamento fora do padrão",
            "Capacidade de inspirar e mobilizar pessoas",
            "Adaptação rápida a mudanças",
        ],
        "pontos_atencao": [
            "Impulsividade em decisões importantes",
            "Dificuldade com rotina e comprometimentos longos",
            "Explosões emocionais podem prejudicar relações",
            "Dificuldade em terminar o que começa",
            "Cansaço dos outros com a intensidade",
        ],
        "tomada_decisao": (
            "Perfis Iansã decidem melhor quando agem pela intuição e paixão. "
            "Análise excessiva paralisa Iansã. Mas atenção: decisões feitas no pico emocional "
            "frequentemente precisam de revisão quando a tempestade passa."
        ),
        "relacionamentos": (
            "Em relações, Iansã é apaixonado e totalmente presente — ou totalmente ausente. "
            "Precisa de parceiros que aguentem a intensidade e valorizem a liberdade."
        ),
        "carreira": (
            "Perfis Iansã se destacam em: empreendedorismo criativo, artes, entretenimento, "
            "marketing, jornalismo, ativismo, esportes, moda, comunicação."
        ),
        "simbolo_cultural": "Vento, raio, espadas",
        "elementos": ["vento", "fogo", "tempestade", "liberdade"],
        "cores": ["Marrom avermelhado", "Amarelo", "Coral"],
        "datas": [
            {"data": "Segunda-feira", "significado": "Dia de Iansã — ideal para iniciar mudanças e enfrentar o que está estagnado"},
            {"data": "4 de dezembro", "significado": "Festa de Santa Bárbara, sincretizada com Iansã — celebração da coragem e da força transformadora"},
        ],
        "praticas": [
            "Quando sentir que está preso em algo, pergunte: 'Que vento novo pode entrar aqui?'",
            "Antes de decisões impulsivas, faça 10 respirações lentas — a clareza virá sem apagar a coragem.",
            "Pratique uma mudança pequena por semana para manter seu fluxo natural de renovação.",
        ],
    },
    "iemanja": {
        "nome": "Iemanjá",
        "subtitulo": "A Profundidade das Águas",
        "cor": "#3498DB",
        "cor_secundaria": "#1a2a5c",
        "emoji": "🌊",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round"><path d="M12 3 C7 3 3 7 3 12 C3 17 7 21 12 21 C17 21 21 17 21 12 C21 7 17 3 12 3Z" stroke-width="2"/><line x1="12" y1="3" x2="12" y2="21" stroke-width="1.5"/><line x1="12" y1="3" x2="5" y2="18" stroke-width="1.5"/><line x1="12" y1="3" x2="19" y2="18" stroke-width="1.5"/><path d="M4 23 Q7 22 10 23 Q13 24 16 23 Q19 22 22 23" stroke-width="1.5"/></svg>',
        "gradiente": "from-blue-500 to-indigo-900",
        "descricao_curta": "Arquétipo da emoção profunda, proteção e conexão.",
        "descricao": (
            "O arquétipo Iemanjá representa o perfil de profundidade emocional, capacidade de cuidar "
            "e criar vínculos duradouros. Perfis Iemanjá sentem tudo com intensidade, têm memória "
            "emocional poderosa e um instinto protetor inato. São a base emocional de qualquer grupo."
        ),
        "tracos": ["Empatia", "Profundidade", "Proteção", "Memória", "Lealdade"],
        "pontos_fortes": [
            "Inteligência emocional elevada",
            "Capacidade de criar vínculos profundos e duradouros",
            "Instinto protetor e cuidado genuíno",
            "Memória afetiva e fidelidade",
            "Presença acolhedora que inspira confiança",
        ],
        "pontos_atencao": [
            "Dificuldade em separar emoção da razão em decisões",
            "Guarda mágoas por muito tempo",
            "Pode se perder cuidando dos outros e esquecer de si",
            "Sensibilidade excessiva a críticas",
            "Resistência a mudanças e ao desconhecido",
        ],
        "tomada_decisao": (
            "Perfis Iemanjá decidem melhor quando têm segurança emocional e tempo para processar. "
            "Evite decidir em momentos de instabilidade emocional. "
            "Seu instinto sobre pessoas raramente falha — confie nele."
        ),
        "relacionamentos": (
            "Em relações, Iemanjá é completamente dedicado e leal. "
            "Precisa de reciprocidade e segurança. Quando se sente traído, retira a proteção completamente."
        ),
        "carreira": (
            "Perfis Iemanjá se destacam em: saúde, psicologia, educação, serviço social, "
            "RH, coaching, artes, medicina, cuidado familiar."
        ),
        "simbolo_cultural": "Mar, lua, estrelas do mar",
        "elementos": ["água", "mar", "lua", "maternidade"],
        "cores": ["Azul claro", "Branco", "Prata"],
        "datas": [
            {"data": "Sábado", "significado": "Dia de Iemanjá — propício para cuidar de si e fortalecer vínculos afetivos"},
            {"data": "2 de fevereiro", "significado": "Festa de Iemanjá — celebração da mãe das águas, de proteção e dos vínculos profundos"},
        ],
        "praticas": [
            "Ao final do dia, identifique alguém que você cuidou — e alguém que cuidou de você.",
            "Quando as emoções estiverem intensas, beba um copo d'água conscientemente antes de reagir.",
            "Periodicamente, escreva quem está em sua rede de proteção afetiva. Cuide dessas pessoas.",
        ],
    },
    "oxum": {
        "nome": "Oxum",
        "subtitulo": "O Poder do Amor e da Beleza",
        "cor": "#F1C40F",
        "cor_secundaria": "#5c4a00",
        "emoji": "✨",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="10" r="7"/><line x1="12" y1="17" x2="12" y2="22"/><line x1="9" y1="22" x2="15" y2="22"/></svg>',
        "gradiente": "from-yellow-500 to-yellow-900",
        "descricao_curta": "Arquétipo do amor, criatividade, beleza e abundância.",
        "descricao": (
            "O arquétipo Oxum representa o perfil criativo-afetivo, que conquista através da beleza, "
            "charme e inteligência emocional. Perfis Oxum são sedutores, criativos e possuem habilidade "
            "única de atrair o que desejam. São os grandes conectores sociais e criadores de harmonia."
        ),
        "tracos": ["Criatividade", "Charme", "Sensibilidade", "Abundância", "Harmonia"],
        "pontos_fortes": [
            "Criatividade e senso estético excepcionais",
            "Habilidade de criar conexões e harmonia social",
            "Inteligência emocional e persuasão naturais",
            "Capacidade de atrair oportunidades e recursos",
            "Diplomacia e resolução de conflitos pelo afeto",
        ],
        "pontos_atencao": [
            "Vaidade e excesso de preocupação com aparência",
            "Dificuldade em lidar com rejeição",
            "Pode usar o charme para manipular",
            "Ciúme e possessividade em relações",
            "Dificuldade em tomar decisões duras",
        ],
        "tomada_decisao": (
            "Perfis Oxum decidem melhor em ambientes harmoniosos e com apoio emocional. "
            "Evite decisões quando se sentir desvalorizado. "
            "Seu senso de oportunidade e de pessoas é seu maior guia."
        ),
        "relacionamentos": (
            "Em relações, Oxum é intensamente afetivo, generoso e precisa de admiração. "
            "Quando não se sente valorizado, pode retirar todo o afeto de uma vez."
        ),
        "carreira": (
            "Perfis Oxum se destacam em: artes, moda, beleza, publicidade, comunicação, "
            "diplomacia, gastronomia, música, design, relações públicas."
        ),
        "simbolo_cultural": "Ouro, espelho, rios",
        "elementos": ["ouro", "água doce", "beleza", "amor"],
        "cores": ["Dourado", "Amarelo mel", "Coral suave"],
        "datas": [
            {"data": "Sábado", "significado": "Dia de Oxum — propício para cultivar beleza, afetos e abundância"},
            {"data": "8 de dezembro", "significado": "Festa de Nossa Senhora da Conceição, sincretizada com Oxum — celebração do amor, da fertilidade e da criação"},
        ],
        "praticas": [
            "Cuide de um espaço da sua casa ou trabalho com intenção de beleza — Oxum prospera em ambientes harmoniosos.",
            "Quando sentir que está desvalorizado, pergunte: 'Estou me valorizando primeiro?'",
            "Pratique gratidão diária por algo belo ou abundante que existe na sua vida agora.",
        ],
    },
    "oxala": {
        "nome": "Oxalá",
        "subtitulo": "A Sabedoria do Equilíbrio",
        "cor": "#ECF0F1",
        "cor_secundaria": "#2c3e50",
        "emoji": "🕊️",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="12" y1="2" x2="12" y2="22"/><line x1="5" y1="9" x2="19" y2="9"/></svg>',
        "gradiente": "from-gray-300 to-gray-700",
        "descricao_curta": "Arquétipo da sabedoria, paz e equilíbrio profundo.",
        "descricao": (
            "O arquétipo Oxalá representa o perfil de sabedoria calma e equilíbrio duradouro. "
            "Perfis Oxalá são os sábios do grupo — pacientes, tolerantes e capazes de ver o todo "
            "quando todos veem apenas partes. São mediadores naturais que constroem através da paz e da harmonia."
        ),
        "tracos": ["Sabedoria", "Paciência", "Tolerância", "Equilíbrio", "Profundidade"],
        "pontos_fortes": [
            "Sabedoria e visão de longo prazo",
            "Paciência excepcional",
            "Tolerância e capacidade de perdoar",
            "Mediação e resolução de conflitos",
            "Profundidade de pensamento e espiritualidade",
        ],
        "pontos_atencao": [
            "Passividade excessiva diante de situações que exigem ação",
            "Dificuldade em estabelecer limites claros",
            "Pode ser explorado pela generosidade",
            "Lentidão na tomada de decisões urgentes",
            "Pode ser visto como distante ou indiferente",
        ],
        "tomada_decisao": (
            "Perfis Oxalá decidem melhor com tempo, reflexão e clareza de valores. "
            "Pressão e urgência são seus maiores inimigos na decisão. "
            "Confie na sua visão de longo prazo — raramente está errada."
        ),
        "relacionamentos": (
            "Em relações, Oxalá é estável, profundo e confiável. "
            "Precisa de reciprocidade na paciência. Pode se tornar distante quando não respeitado."
        ),
        "carreira": (
            "Perfis Oxalá se destacam em: filosofia, educação, espiritualidade, medicina, "
            "psicologia, magistratura, pesquisa, trabalho social."
        ),
        "simbolo_cultural": "Branco, bastão, paz",
        "elementos": ["branco", "ar", "paz", "criação"],
        "cores": ["Branco", "Prata", "Cinza suave"],
        "datas": [
            {"data": "Sexta-feira", "significado": "Dia de Oxalá em muitas casas — propício para meditação, cura, perdão e recomeços"},
            {"data": "1º de janeiro", "significado": "Festa do Senhor do Bonfim e renovação — celebração da paz, da criação e dos recomeços"},
        ],
        "praticas": [
            "Pratique uma pausa consciente de 5 minutos antes de qualquer decisão importante.",
            "Quando alguém errar com você, pergunte internamente: 'O que precisaria entender para perdoar?'",
            "Reserve 15 minutos diários em silêncio — sem tela, sem barulho. Apenas presença.",
        ],
    },
    "omolu": {
        "nome": "Omolu",
        "subtitulo": "A Força da Transformação",
        "cor": "#8E44AD",
        "cor_secundaria": "#2c1a4a",
        "emoji": "🌑",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="12" y1="15" x2="12" y2="22" stroke-width="2.5"/><path d="M12 5 C8 5 5 7.5 5 10.5 C5 13.5 8 15 12 15 C16 15 19 13.5 19 10.5 C19 7.5 16 5 12 5Z"/><circle cx="12" cy="4.5" r="2.5" fill="currentColor" stroke="none"/></svg>',
        "gradiente": "from-purple-700 to-purple-950",
        "descricao_curta": "Arquétipo da resiliência, transformação e sabedoria pela dor.",
        "descricao": (
            "O arquétipo Omolu representa o perfil que transforma dor em sabedoria. "
            "Perfis Omolu passaram por desafios intensos e emergiram mais fortes. "
            "São extremamente resilientes, possuem visão única sobre a vida e uma profundidade "
            "que poucos atingem. Guardiões da sobrevivência e da superação."
        ),
        "tracos": ["Resiliência", "Transformação", "Profundidade", "Superação", "Cura"],
        "pontos_fortes": [
            "Resiliência extraordinária diante de adversidades",
            "Profundidade emocional e psicológica",
            "Capacidade única de transformar crises em crescimento",
            "Sabedoria prática adquirida pela experiência",
            "Empatia com quem sofre",
        ],
        "pontos_atencao": [
            "Tendência ao isolamento e ao sofrimento silencioso",
            "Dificuldade em pedir ajuda",
            "Pode carregar traumas que afetam decisões",
            "Visão pessimista ou excessivamente cautelosa",
            "Dificuldade em celebrar conquistas",
        ],
        "tomada_decisao": (
            "Perfis Omolu decidem melhor quando conectados à própria experiência de superação. "
            "Evite o isolamento na tomada de decisão — busque perspectivas externas. "
            "Sua capacidade de antecipar riscos é um diferencial poderoso."
        ),
        "relacionamentos": (
            "Em relações, Omolu é profundamente leal mas difícil de acessar emocionalmente. "
            "Precisa de parceiros pacientes e genuinamente confiáveis."
        ),
        "carreira": (
            "Perfis Omolu se destacam em: medicina, psicologia, pesquisa, serviço social, "
            "trabalho com populações vulneráveis, reabilitação, cuidados paliativos."
        ),
        "simbolo_cultural": "Terra, palha, doenças e cura",
        "elementos": ["terra", "cura", "morte", "renascimento"],
        "cores": ["Preto", "Vermelho", "Branco"],
        "datas": [
            {"data": "Segunda-feira", "significado": "Dia de Omolu — propício para processos de cura, transformação e superação de ciclos difíceis"},
            {"data": "13 de maio", "significado": "Data associada à transformação social e à cura coletiva em algumas tradições"},
        ],
        "praticas": [
            "Ao final de um ciclo difícil, escreva: 'O que essa experiência me ensinou?'",
            "Não carregue sofrimento em silêncio — a cura começa pelo reconhecimento honesto da dor.",
            "Celebre vitórias pequenas: quem supera muito precisa aprender a reconhecer suas conquistas.",
        ],
    },
    "oxumare": {
        "nome": "Oxumaré",
        "subtitulo": "O Arco-Íris da Dualidade",
        "cor": "#1ABC9C",
        "cor_secundaria": "#0a4a3a",
        "emoji": "🌈",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round"><path d="M3 19 Q12 3 21 19" stroke-width="2.5"/><path d="M6 19 Q12 7 18 19" stroke-width="2"/><circle cx="3" cy="19" r="1.5" fill="currentColor" stroke="none"/><circle cx="21" cy="19" r="1.5" fill="currentColor" stroke="none"/></svg>',
        "gradiente": "from-teal-500 to-teal-900",
        "descricao_curta": "Arquétipo da dualidade, adaptação e movimento contínuo.",
        "descricao": (
            "O arquétipo Oxumaré representa o perfil de alta adaptabilidade e visão dual. "
            "Perfis Oxumaré transitam naturalmente entre mundos diferentes, adaptam-se a qualquer "
            "ambiente e enxergam múltiplas perspectivas simultaneamente. São os grandes mediadores "
            "e transformadores de ciclos."
        ),
        "tracos": ["Adaptabilidade", "Dualidade", "Movimento", "Renovação", "Versatilidade"],
        "pontos_fortes": [
            "Adaptabilidade excepcional a contextos variados",
            "Capacidade de ver múltiplas perspectivas",
            "Renovação e ciclos de crescimento constantes",
            "Mediação entre opostos",
            "Versatilidade e multitalento",
        ],
        "pontos_atencao": [
            "Falta de consistência e inconstância",
            "Dificuldade em definir identidade clara",
            "Pode ser volátil emocionalmente",
            "Dificuldade em comprometimentos longos",
            "Pode se perder na adaptação excessiva",
        ],
        "tomada_decisao": (
            "Perfis Oxumaré decidem melhor quando reconhecem que ambas as opções têm valor. "
            "Sua tendência natural é ver o que outros não veem — use isso. "
            "Evite decisões que exijam rigidez absoluta de posição."
        ),
        "relacionamentos": (
            "Em relações, Oxumaré é fascinante, imprevisível e difícil de 'segurar'. "
            "Precisa de liberdade e de parceiros que se adaptem ao movimento."
        ),
        "carreira": (
            "Perfis Oxumaré se destacam em: consultoria, empreendedorismo serial, viagens, "
            "artes plásticas, tecnologia, inovação, mediação cultural."
        ),
        "simbolo_cultural": "Arco-íris, cobra, ciclos",
        "elementos": ["arco-íris", "cobra", "ciclos", "dualidade"],
        "cores": ["Verde", "Amarelo", "Todas as cores em movimento"],
        "datas": [
            {"data": "Terça-feira", "significado": "Dia de Oxumaré em algumas casas — propício para mudanças, adaptações e abertura de novos ciclos"},
            {"data": "Solstícios e equinócios", "significado": "Pontos de transição do ano — momentos naturais de renovação e de fechamento de ciclos para Oxumaré"},
        ],
        "praticas": [
            "Quando estiver entre duas opções opostas, pergunte: 'Existe uma terceira via que reúne o melhor das duas?'",
            "A cada mês, avalie: que ciclo está se encerrando e que novo está chegando?",
            "Celebre suas contradições — sua capacidade de ver dos dois lados é um diferencial raro.",
        ],
    },
    "nana": {
        "nome": "Nanã",
        "subtitulo": "A Memória Ancestral",
        "cor": "#9B59B6",
        "cor_secundaria": "#2c1a4a",
        "emoji": "🌸",
        "icone_svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="12" y1="14" x2="12" y2="22" stroke-width="2.5"/><path d="M8 4 Q7 7 8 11"/><path d="M10.5 3 Q10 6 10.5 10"/><path d="M13.5 3 Q14 6 13.5 10"/><path d="M16 4 Q17 7 16 11"/><path d="M8 11 Q10 14 12 14 Q14 14 16 11 Q14 10 12 10 Q10 10 8 11Z"/></svg>',
        "gradiente": "from-violet-600 to-violet-950",
        "descricao_curta": "Arquétipo da memória, tradição e sabedoria ancestral.",
        "descricao": (
            "O arquétipo Nanã representa o perfil de profunda conexão com a memória, a tradição e "
            "a sabedoria acumulada. Perfis Nanã são os guardiões da história — têm memória prodigiosa, "
            "aprendem com o passado e possuem sabedoria que vai além da experiência individual. "
            "São a âncora que estabiliza os grupos."
        ),
        "tracos": ["Memória", "Tradição", "Profundidade", "Estabilidade", "Ancestralidade"],
        "pontos_fortes": [
            "Memória excepcional e aprendizado com o passado",
            "Estabilidade emocional e presença constante",
            "Sabedoria transmitida através das gerações",
            "Profundidade e consistência",
            "Capacidade de manter tradições e valores essenciais",
        ],
        "pontos_atencao": [
            "Resistência a mudanças necessárias",
            "Peso do passado impedindo o presente",
            "Rigidez em padrões antigos",
            "Dificuldade em abrir mão do controle",
            "Pode ser excessivamente tradicional",
        ],
        "tomada_decisao": (
            "Perfis Nanã decidem melhor quando consultam a própria história e valores profundos. "
            "Evite decisões que rompam com o que você considera sagrado. "
            "Sua sabedoria histórica é um guia poderoso — mas equilibre com o presente."
        ),
        "relacionamentos": (
            "Em relações, Nanã é profundamente leal, protetora e exige reciprocidade total. "
            "Não perdoa traições facilmente e pode guardar ressentimentos profundos."
        ),
        "carreira": (
            "Perfis Nanã se destacam em: história, arqueologia, arquivística, educação, "
            "tradições culturais, cuidado com idosos, genealogia, restauração."
        ),
        "simbolo_cultural": "Lama, chuva, palha roxa",
        "elementos": ["lama", "chuva", "memória", "ancestralidade"],
        "cores": ["Lilás", "Azul lavanda", "Branco"],
        "datas": [
            {"data": "Segunda-feira", "significado": "Dia de Nanã — propício para conexão com a memória, a família e as raízes ancestrais"},
            {"data": "26 de julho", "significado": "Festa de Sant'Ana, sincretizada com Nanã — celebração da ancestralidade, da sabedoria das avós e da continuidade"},
        ],
        "praticas": [
            "Periodicamente, reconecte-se com sua história: fotos, memórias, histórias de família.",
            "Quando estiver preso no passado, pergunte: 'O que esse ensinamento me pede para fazer agora?'",
            "Crie rituais de continuidade: preserve o que é essencial, libere o que já cumpriu seu ciclo.",
        ],
    },
}

PERGUNTAS = [
    # Bloco 1: Ação vs Contemplação
    {
        "id": 1,
        "bloco": 1,
        "bloco_nome": "Ação e Decisão",
        "texto": "Quando precisa resolver um problema urgente, você:",
        "opcoes": [
            {"texto": "Age imediatamente, sem pensar muito", "pesos": {"ogum": 3, "iansa": 2}},
            {"texto": "Analisa cuidadosamente antes de qualquer movimento", "pesos": {"oxossi": 3, "oxala": 2}},
            {"texto": "Busca equilíbrio entre análise rápida e ação", "pesos": {"xango": 2, "oxumare": 2}},
            {"texto": "Consulta outras pessoas antes de decidir", "pesos": {"iemanja": 2, "oxum": 2}},
        ],
    },
    {
        "id": 2,
        "bloco": 1,
        "bloco_nome": "Ação e Decisão",
        "texto": "Diante de um conflito direto, você:",
        "opcoes": [
            {"texto": "Enfrenta de frente, sem rodeios", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Tenta mediar e encontrar uma solução pacífica", "pesos": {"oxala": 3, "iemanja": 2}},
            {"texto": "Evita o conflito ao máximo possível", "pesos": {"oxum": 2, "nana": 2}},
            {"texto": "Usa estratégia para vencer sem confronto direto", "pesos": {"oxossi": 3, "xango": 2}},
        ],
    },
    {
        "id": 3,
        "bloco": 1,
        "bloco_nome": "Ação e Decisão",
        "texto": "Como você toma decisões importantes na vida?",
        "opcoes": [
            {"texto": "Pela razão e lógica, pesando prós e contras", "pesos": {"xango": 3, "ogum": 2}},
            {"texto": "Pela emoção e intuição, sinto o que é certo", "pesos": {"iemanja": 3, "oxum": 2}},
            {"texto": "Por instinto imediato, sem muita reflexão", "pesos": {"iansa": 3, "ogum": 2}},
            {"texto": "Com muita reflexão e paciência, nada é urgente", "pesos": {"oxala": 3, "nana": 2}},
        ],
    },
    {
        "id": 4,
        "bloco": 1,
        "bloco_nome": "Ação e Decisão",
        "texto": "Seu ritmo natural de trabalho e produção é:",
        "opcoes": [
            {"texto": "Intenso e focado — não paro enquanto não termino", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Paciente e metódico — um passo de cada vez", "pesos": {"oxossi": 3, "oxala": 2}},
            {"texto": "Variável — com picos de energia seguidos de descanso", "pesos": {"iansa": 2, "oxumare": 3}},
            {"texto": "Tranquilo — prefiro qualidade e não me pressiono", "pesos": {"oxala": 3, "nana": 2}},
        ],
    },
    {
        "id": 5,
        "bloco": 1,
        "bloco_nome": "Ação e Decisão",
        "texto": "Para você, ser bem-sucedido significa principalmente:",
        "opcoes": [
            {"texto": "Conquistar, produzir e alcançar minhas metas", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Ter paz, harmonia e equilíbrio na vida", "pesos": {"oxala": 3, "iemanja": 2}},
            {"texto": "Ter abundância, prazer e aproveitar a vida", "pesos": {"oxum": 3, "oxossi": 2}},
            {"texto": "Fazer diferença, ser justo e deixar legado", "pesos": {"xango": 3, "omolu": 2}},
        ],
    },
    # Bloco 2: Emoções
    {
        "id": 6,
        "bloco": 2,
        "bloco_nome": "Vida Emocional",
        "texto": "Como você lida com mágoas profundas?",
        "opcoes": [
            {"texto": "Guardo por muito tempo — difícil esquecer", "pesos": {"iemanja": 3, "nana": 2}},
            {"texto": "Explodo rapidamente, mas perdoo com facilidade", "pesos": {"iansa": 3, "ogum": 2}},
            {"texto": "Perdoo facilmente — não guardo rancor", "pesos": {"oxala": 3, "oxum": 2}},
            {"texto": "Processo sozinho e sigo em frente sem ruído", "pesos": {"oxossi": 2, "omolu": 3}},
        ],
    },
    {
        "id": 7,
        "bloco": 2,
        "bloco_nome": "Vida Emocional",
        "texto": "Quando está com raiva, você tipicamente:",
        "opcoes": [
            {"texto": "Explode e coloca tudo para fora", "pesos": {"iansa": 3, "ogum": 2}},
            {"texto": "Se silencia e se afasta por um tempo", "pesos": {"oxala": 2, "oxossi": 3}},
            {"texto": "Usa palavras duras mas é direto e honesto", "pesos": {"xango": 3, "ogum": 2}},
            {"texto": "Chora ou demonstra emocionalmente", "pesos": {"iemanja": 3, "oxum": 2}},
        ],
    },
    {
        "id": 8,
        "bloco": 2,
        "bloco_nome": "Vida Emocional",
        "texto": "Sua relação com o passado é:",
        "opcoes": [
            {"texto": "Difícil de separar — o passado está sempre presente", "pesos": {"nana": 3, "iemanja": 2}},
            {"texto": "Aprendo com ele mas sigo em frente naturalmente", "pesos": {"omolu": 3, "oxumare": 2}},
            {"texto": "Prefiro focar no presente e no futuro", "pesos": {"ogum": 2, "iansa": 3}},
            {"texto": "O passado me define e me orgulha muito", "pesos": {"xango": 3, "nana": 2}},
        ],
    },
    {
        "id": 9,
        "bloco": 2,
        "bloco_nome": "Vida Emocional",
        "texto": "Em relação à espiritualidade e ao sagrado:",
        "opcoes": [
            {"texto": "Tenho crenças profundas e rituais próprios", "pesos": {"oxala": 3, "iemanja": 2}},
            {"texto": "Acredito em algo maior mas de forma pragmática", "pesos": {"xango": 2, "ogum": 2}},
            {"texto": "Sou muito conectado — sinto e percebo energias", "pesos": {"iemanja": 3, "oxum": 2}},
            {"texto": "Prefiro a razão, sou cético em relação ao espiritual", "pesos": {"ogum": 2, "oxossi": 2}},
        ],
    },
    {
        "id": 10,
        "bloco": 2,
        "bloco_nome": "Vida Emocional",
        "texto": "Quando alguém próximo precisa de ajuda, você:",
        "opcoes": [
            {"texto": "Oferece suporte emocional profundo e escuta", "pesos": {"iemanja": 3, "oxum": 2}},
            {"texto": "Age praticamente para resolver o problema", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Ensina e orienta como a pessoa pode se ajudar", "pesos": {"oxossi": 3, "oxala": 2}},
            {"texto": "Ouve com paciência total e acolhe sem julgamento", "pesos": {"oxala": 3, "nana": 2}},
        ],
    },
    # Bloco 3: Liderança
    {
        "id": 11,
        "bloco": 3,
        "bloco_nome": "Liderança e Poder",
        "texto": "Em grupo, você naturalmente:",
        "opcoes": [
            {"texto": "Lidera e toma a frente das iniciativas", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Organiza, estrutura e distribui tarefas", "pesos": {"xango": 3, "oxossi": 2}},
            {"texto": "Inspira e motiva as pessoas emocionalmente", "pesos": {"iansa": 3, "oxum": 2}},
            {"texto": "Acompanha, contribui e apoia quem lidera", "pesos": {"oxala": 2, "iemanja": 2}},
        ],
    },
    {
        "id": 12,
        "bloco": 3,
        "bloco_nome": "Liderança e Poder",
        "texto": "Você prefere trabalhar:",
        "opcoes": [
            {"texto": "Solo, no meu próprio ritmo e autonomia total", "pesos": {"oxossi": 3, "ogum": 2}},
            {"texto": "Liderando um time, sendo a referência", "pesos": {"xango": 3, "ogum": 2}},
            {"texto": "Dentro de uma comunidade, sentindo pertencimento", "pesos": {"iemanja": 3, "oxum": 2}},
            {"texto": "Em dupla ou parceria próxima e colaborativa", "pesos": {"oxum": 2, "oxumare": 2}},
        ],
    },
    {
        "id": 13,
        "bloco": 3,
        "bloco_nome": "Liderança e Poder",
        "texto": "Sua relação com figuras de autoridade é:",
        "opcoes": [
            {"texto": "Questiono e desafio quando não concordo", "pesos": {"ogum": 3, "iansa": 2}},
            {"texto": "Respeito mas avalio criticamente antes de seguir", "pesos": {"xango": 3, "oxossi": 2}},
            {"texto": "Aceito e sigo — confio em quem tem mais experiência", "pesos": {"oxala": 2, "nana": 2}},
            {"texto": "Prefiro ser a autoridade — não funciono bem sendo liderado", "pesos": {"xango": 3, "ogum": 2}},
        ],
    },
    {
        "id": 14,
        "bloco": 3,
        "bloco_nome": "Liderança e Poder",
        "texto": "Quando você lidera, seu estilo é:",
        "opcoes": [
            {"texto": "Direto, exigente e totalmente focado em resultados", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Justo, firme mas sempre aberto ao diálogo", "pesos": {"xango": 3, "oxala": 2}},
            {"texto": "Inspirador, carismático e que mobiliza pela paixão", "pesos": {"iansa": 3, "oxum": 2}},
            {"texto": "Cuidadoso, protetor e que desenvolve cada pessoa", "pesos": {"iemanja": 3, "oxum": 2}},
        ],
    },
    {
        "id": 15,
        "bloco": 3,
        "bloco_nome": "Liderança e Poder",
        "texto": "Como você assume responsabilidade por seus erros?",
        "opcoes": [
            {"texto": "Assumo imediatamente e ajo para corrigir", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Analiso o que errei antes de falar sobre", "pesos": {"oxossi": 3, "oxala": 2}},
            {"texto": "Sinto profundamente mas processo sozinho", "pesos": {"omolu": 3, "iemanja": 2}},
            {"texto": "Tenho dificuldade — aceitar erros não é fácil", "pesos": {"xango": 2, "iansa": 2}},
        ],
    },
    # Bloco 4: Ambiente e conexão
    {
        "id": 16,
        "bloco": 4,
        "bloco_nome": "Ambiente e Energia",
        "texto": "O ambiente que mais te conecta e revitaliza:",
        "opcoes": [
            {"texto": "Mar, rio, lago — qualquer água corrente ou profunda", "pesos": {"iemanja": 3, "oxum": 2}},
            {"texto": "Floresta, mata, natureza selvagem", "pesos": {"oxossi": 3, "omolu": 2}},
            {"texto": "Cidade, movimento, estradas, agitação urbana", "pesos": {"ogum": 3, "iansa": 2}},
            {"texto": "Espaços abertos, céu, horizonte, ar livre", "pesos": {"iansa": 3, "oxumare": 2}},
        ],
    },
    {
        "id": 17,
        "bloco": 4,
        "bloco_nome": "Ambiente e Energia",
        "texto": "O elemento que mais representa sua energia interior:",
        "opcoes": [
            {"texto": "Fogo — intenso, transformador, aquecedor", "pesos": {"iansa": 3, "ogum": 2, "xango": 2}},
            {"texto": "Água — profundo, fluido, nutritivo", "pesos": {"iemanja": 3, "oxum": 3}},
            {"texto": "Terra — sólido, estável, fértil", "pesos": {"omolu": 3, "nana": 3, "oxossi": 2}},
            {"texto": "Ar/Vento — livre, renovador, imprevisível", "pesos": {"iansa": 3, "oxumare": 2}},
        ],
    },
    {
        "id": 18,
        "bloco": 4,
        "bloco_nome": "Ambiente e Energia",
        "texto": "O que mais te energiza no dia a dia?",
        "opcoes": [
            {"texto": "Movimento, ação, desafios físicos ou mentais", "pesos": {"ogum": 3, "iansa": 2}},
            {"texto": "Silêncio, contemplação, leitura, estudo profundo", "pesos": {"oxossi": 3, "oxala": 2}},
            {"texto": "Conexão com pessoas, afeto, conversas significativas", "pesos": {"iemanja": 3, "oxum": 2}},
            {"texto": "Criar, expressar, realizar algo novo e belo", "pesos": {"oxum": 3, "iansa": 2, "xango": 2}},
        ],
    },
    {
        "id": 19,
        "bloco": 4,
        "bloco_nome": "Ambiente e Energia",
        "texto": "Sua relação com mudanças e transformações:",
        "opcoes": [
            {"texto": "Amo mudanças — elas me dão energia e renovação", "pesos": {"iansa": 3, "oxumare": 2}},
            {"texto": "Aceito quando necessário e me adapto bem", "pesos": {"omolu": 3, "oxumare": 2}},
            {"texto": "Prefiro estabilidade mas me adapto quando preciso", "pesos": {"oxala": 3, "iemanja": 2}},
            {"texto": "Resisto — prefiro o conhecido e o seguro", "pesos": {"nana": 3, "iemanja": 2}},
        ],
    },
    {
        "id": 20,
        "bloco": 4,
        "bloco_nome": "Ambiente e Energia",
        "texto": "O que você mais valoriza e não abre mão na vida?",
        "opcoes": [
            {"texto": "Liberdade e total independência", "pesos": {"ogum": 3, "oxossi": 2, "iansa": 2}},
            {"texto": "Segurança, proteção e estabilidade emocional", "pesos": {"iemanja": 3, "oxala": 2}},
            {"texto": "Amor, conexões afetivas profundas", "pesos": {"oxum": 3, "iemanja": 2}},
            {"texto": "Conhecimento, sabedoria e crescimento constante", "pesos": {"oxossi": 3, "xango": 2, "oxala": 2}},
        ],
    },
    # Bloco 5: Relações e comportamento social
    {
        "id": 21,
        "bloco": 5,
        "bloco_nome": "Relações e Sociedade",
        "texto": "Socialmente, você se define como:",
        "opcoes": [
            {"texto": "Expansivo, animado e facilmente extrovertido", "pesos": {"oxum": 3, "iansa": 2}},
            {"texto": "Reservado mas profundo quando cria vínculo", "pesos": {"oxossi": 3, "omolu": 2}},
            {"texto": "Acolhedor, protetor e que cuida dos que estão perto", "pesos": {"iemanja": 3, "oxala": 2}},
            {"texto": "Carismático, com presença marcante e autoridade", "pesos": {"xango": 3, "ogum": 2}},
        ],
    },
    {
        "id": 22,
        "bloco": 5,
        "bloco_nome": "Relações e Sociedade",
        "texto": "Em relacionamentos íntimos, você é:",
        "opcoes": [
            {"texto": "Intenso, passional e se entrega completamente", "pesos": {"iansa": 3, "oxum": 2}},
            {"texto": "Cuidadoso, protetor e profundamente leal", "pesos": {"iemanja": 3, "ogum": 2}},
            {"texto": "Equilibrado, racional e um parceiro confiável", "pesos": {"oxala": 3, "xango": 2}},
            {"texto": "Preserva bastante independência mesmo em relações", "pesos": {"ogum": 3, "oxossi": 2}},
        ],
    },
    {
        "id": 23,
        "bloco": 5,
        "bloco_nome": "Relações e Sociedade",
        "texto": "Como você demonstra afeto às pessoas que ama?",
        "opcoes": [
            {"texto": "Com atos práticos, presença física e proteção", "pesos": {"ogum": 3, "iemanja": 2}},
            {"texto": "Com palavras, emoção e demonstrações afetivas", "pesos": {"oxum": 3, "iansa": 2}},
            {"texto": "Com presença tranquila, constante e confiável", "pesos": {"oxala": 3, "nana": 2}},
            {"texto": "Com experiências compartilhadas e aventuras", "pesos": {"oxossi": 3, "oxumare": 2}},
        ],
    },
    {
        "id": 24,
        "bloco": 5,
        "bloco_nome": "Relações e Sociedade",
        "texto": "O que você absolutamente não tolera nas pessoas:",
        "opcoes": [
            {"texto": "Injustiça, covardia e desonestidade", "pesos": {"ogum": 3, "xango": 2}},
            {"texto": "Falsidade, traição e quebra de confiança", "pesos": {"iemanja": 3, "oxum": 2}},
            {"texto": "Arrogância, prepotência e falta de humildade", "pesos": {"oxala": 2, "omolu": 3}},
            {"texto": "Preguiça, falta de propósito e acomodação", "pesos": {"ogum": 2, "oxossi": 3}},
        ],
    },
    {
        "id": 25,
        "bloco": 5,
        "bloco_nome": "Relações e Sociedade",
        "texto": "Qual frase ressoa mais com sua forma de ver a vida?",
        "opcoes": [
            {"texto": '"Agir é o único caminho — o movimento cria a realidade"', "pesos": {"ogum": 3, "iansa": 2}},
            {"texto": '"A sabedoria real vem do silêncio e da observação"', "pesos": {"oxala": 3, "oxossi": 2}},
            {"texto": '"O amor e a conexão são a força que move tudo"', "pesos": {"oxum": 3, "iemanja": 2}},
            {"texto": '"A vida é transformação constante — resista ao estático"', "pesos": {"omolu": 3, "iansa": 2, "oxumare": 2}},
        ],
    },
]


def calcular_resultado(respostas: dict) -> dict:
    """
    respostas: {pergunta_id: opcao_index}
    Retorna o ranking dos orixás com pontuação.
    """
    scores = {orixa: 0 for orixa in ORIXAS}

    for pergunta_id_str, opcao_idx in respostas.items():
        pergunta_id = int(pergunta_id_str)
        pergunta = next((p for p in PERGUNTAS if p["id"] == pergunta_id), None)
        if not pergunta:
            continue
        opcao_idx = int(opcao_idx)
        if opcao_idx < 0 or opcao_idx >= len(pergunta["opcoes"]):
            continue
        opcao = pergunta["opcoes"][opcao_idx]
        for orixa, peso in opcao["pesos"].items():
            if orixa in scores:
                scores[orixa] += peso

    total = sum(scores.values()) or 1
    percentuais = {k: round((v / total) * 100, 1) for k, v in scores.items()}
    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    primario_key = ranking[0][0]
    secundario_key = ranking[1][0]

    return {
        "primario": primario_key,
        "secundario": secundario_key,
        "primario_data": ORIXAS[primario_key],
        "secundario_data": ORIXAS[secundario_key],
        "scores": scores,
        "percentuais": percentuais,
        "ranking": [(k, v, ORIXAS[k]["nome"]) for k, v in ranking],
    }


SYSTEM_PROMPT_TEMPLATE = """Você é um conselheiro de autoconhecimento do app Orixá IA, especializado nos padrões comportamentais dos arquétipos ancestrais afro-brasileiros.

O usuário tem o seguinte perfil comportamental:
- **Arquétipo Principal**: {primario} — {primario_subtitulo}
- **Arquétipo Auxiliar**: {secundario} — {secundario_subtitulo}

**Sobre o perfil primário**:
{primario_descricao}

**Forças identificadas**:
{pontos_fortes}

**Pontos de atenção**:
{pontos_atencao}

**Padrão de decisão**:
{tomada_decisao}

**Padrão em relacionamentos**:
{relacionamentos}

---

COMO VOCÊ DEVE RESPONDER:

1. **Voz de conselheiro sábio**: Fale como alguém que conhece profundamente o perfil do usuário. Use frases como "Com base no seu perfil...", "Percebo que você tende a...", "Quem carrega a energia de {primario} geralmente...", "Uma reflexão importante para você...". Seja como um conselheiro que orienta com cuidado e clareza — não como uma máquina.

2. **Você é um aplicativo, não um guia espiritual**: Deixe isso claro quando relevante. Você oferece reflexões baseadas em padrões comportamentais — não previsões, não certezas espirituais, não diagnósticos. Use sempre linguagem probabilística: "é provável que", "muitas pessoas com esse perfil", "uma tendência comum é".

3. **Respeito à tradição**: Os Orixás são entidades sagradas para milhões de pessoas. Trate seus arquétipos com seriedade e reverência. Nunca banalize, nunca faça piada, nunca reduza a tradição a um simples teste de personalidade.

4. **Orientação espiritual e religiosa — postura laica e respeitosa**: Quando o usuário perguntar sobre questões espirituais, destino, missão de vida ou temas sagrados, encaminhe com respeito à orientação de cada um. Use algo como: *"Para questões de natureza espiritual, o ideal é buscar orientação com quem representa sua tradição: se você é de religiões de matriz africana, um Pai ou Mãe de Santo de confiança pode te guiar com profundidade. Se segue outra tradição religiosa, um padre, pastor, rabino ou líder espiritual da sua comunidade são os caminhos mais indicados. O que nenhum aplicativo pode substituir é o olhar humano de quem conhece sua jornada."*

5. **Postura passiva — não prolongue a conversa**: Você é um conselheiro, não um interlocutor ativo. Responda com profundidade mas NÃO faça perguntas de acompanhamento, NÃO se coloque à disposição de forma proativa ("se precisar estou aqui", "pode me perguntar qualquer coisa", etc.). Cada resposta deve ser completa em si mesma — o usuário é quem decide continuar ou não.

6. **Não crie dependência**: Se o usuário demonstrar que está usando o chat como suporte emocional primário ou para questões que exigem ajuda profissional, acolha com cuidado e indique recursos adequados: terapia, aconselhamento, apoio médico, espiritual ou comunitário — conforme o tema. Nunca estimule que o usuário volte ao chat como substituto de ajuda real.

7. **Inclua o arquétipo auxiliar quando relevante**: Mencione como a influência de {secundario} complementa, tensiona ou enriquece o perfil primário.

8. **Tom**: Sério, cálido, respeitoso. Sem gírias, sem informalidade excessiva, mas também sem frieza técnica. Pense em como um conselheiro experiente falaria — com autoridade tranquila e cuidado genuíno.

9. **Tamanho**: Respostas de 3 a 5 parágrafos. Substanciais, mas sem prolixidade. Cada parágrafo deve trazer uma reflexão nova, não repetir o anterior.

10. **Limites claros**: Não faça diagnósticos médicos ou psicológicos. Se o usuário trouxer algo que exige atenção profissional de saúde mental, acolha com empatia e oriente claramente a buscar apoio especializado.

Você pode orientar sobre: decisões de vida, relacionamentos, carreira, padrões emocionais, pontos cegos, forças, propósito — sempre conectando ao arquétipo com respeito e profundidade, e sempre lembrando que você é uma ferramenta de reflexão, não um oráculo.
"""


def build_system_prompt(resultado: dict) -> str:
    p = resultado["primario_data"]
    s = resultado["secundario_data"]
    return SYSTEM_PROMPT_TEMPLATE.format(
        primario=p["nome"],
        primario_subtitulo=p["subtitulo"],
        secundario=s["nome"],
        secundario_subtitulo=s["subtitulo"],
        primario_descricao=p["descricao"],
        pontos_fortes="\n".join(f"- {x}" for x in p["pontos_fortes"]),
        pontos_atencao="\n".join(f"- {x}" for x in p["pontos_atencao"]),
        tomada_decisao=p["tomada_decisao"],
        relacionamentos=p["relacionamentos"],
    )
