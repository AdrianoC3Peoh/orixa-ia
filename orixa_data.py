from typing import Dict, List

ORIXAS: Dict[str, dict] = {
    "ogum": {
        "nome": "Ogum",
        "subtitulo": "O Guerreiro dos Caminhos",
        "cor": "#4A90D9",
        "cor_secundaria": "#1a3a5c",
        "emoji": "⚔️",
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
    },
    "oxossi": {
        "nome": "Oxóssi",
        "subtitulo": "O Estrategista da Abundância",
        "cor": "#2ECC71",
        "cor_secundaria": "#1a4a2e",
        "emoji": "🏹",
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
    },
    "xango": {
        "nome": "Xangô",
        "subtitulo": "O Soberano da Justiça",
        "cor": "#E74C3C",
        "cor_secundaria": "#5c1a1a",
        "emoji": "⚡",
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
    },
    "iansa": {
        "nome": "Iansã",
        "subtitulo": "A Força dos Ventos e da Mudança",
        "cor": "#E67E22",
        "cor_secundaria": "#5c3a1a",
        "emoji": "🌪️",
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
    },
    "iemanja": {
        "nome": "Iemanjá",
        "subtitulo": "A Profundidade das Águas",
        "cor": "#3498DB",
        "cor_secundaria": "#1a2a5c",
        "emoji": "🌊",
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
    },
    "oxum": {
        "nome": "Oxum",
        "subtitulo": "O Poder do Amor e da Beleza",
        "cor": "#F1C40F",
        "cor_secundaria": "#5c4a00",
        "emoji": "✨",
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
    },
    "oxala": {
        "nome": "Oxalá",
        "subtitulo": "A Sabedoria do Equilíbrio",
        "cor": "#ECF0F1",
        "cor_secundaria": "#2c3e50",
        "emoji": "🕊️",
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
    },
    "omolu": {
        "nome": "Omolu",
        "subtitulo": "A Força da Transformação",
        "cor": "#8E44AD",
        "cor_secundaria": "#2c1a4a",
        "emoji": "🌑",
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
    },
    "oxumare": {
        "nome": "Oxumaré",
        "subtitulo": "O Arco-Íris da Dualidade",
        "cor": "#1ABC9C",
        "cor_secundaria": "#0a4a3a",
        "emoji": "🌈",
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
    },
    "nana": {
        "nome": "Nanã",
        "subtitulo": "A Memória Ancestral",
        "cor": "#9B59B6",
        "cor_secundaria": "#2c1a4a",
        "emoji": "🌸",
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


SYSTEM_PROMPT_TEMPLATE = """Você é o assistente de autoconhecimento e orientação comportamental do app Orixá IA.

O usuário teve o seguinte diagnóstico estatístico-comportamental:
- **Arquétipo Primário**: {primario} — {primario_subtitulo}
- **Arquétipo Secundário**: {secundario} — {secundario_subtitulo}

**Descrição do perfil primário**: {primario_descricao}

**Pontos fortes do perfil**:
{pontos_fortes}

**Pontos de atenção**:
{pontos_atencao}

**Padrão de tomada de decisão**:
{tomada_decisao}

**Padrão em relacionamentos**:
{relacionamentos}

---

INSTRUÇÕES IMPORTANTES:
1. Você orienta EXCLUSIVAMENTE com base nos padrões comportamentais e estatísticos dos arquétipos
2. NUNCA faça afirmações religiosas, espirituais ou litúrgicas
3. Use sempre linguagem como "seu perfil tende a", "estatisticamente, pessoas com esse arquétipo", "a tendência comportamental indica"
4. Quando o usuário perguntar sobre decisões, relacionamentos, carreira ou comportamento, responda com base no arquétipo dele
5. Seja empático, perspicaz e prático
6. Inclua o arquétipo secundário quando relevante para enriquecer a análise
7. Seja conciso e direto — respostas longas demais perdem o impacto
8. NÃO substitua orientação psicológica, médica ou espiritual profissional
9. Quando não souber, diga que precisa de mais informações sobre a situação específica do usuário

Você pode responder sobre: tomada de decisão, relacionamentos, carreira, comportamento em grupo, padrões emocionais, pontos cegos e forças do usuário — sempre conectando ao arquétipo.
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
