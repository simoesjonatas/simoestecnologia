from datetime import date
from urllib.parse import quote


WHATSAPP_NUMBER = "5521971347985"
WHATSAPP_MESSAGE = "Ola, quero conversar sobre uma solucao personalizada para minha organizacao."

SITE = {
    "name": "Simões Tecnologia",
    "domain": "https://simoesti.com.br",
    "title": "Simões Tecnologia | Sistemas personalizados para empresas",
    "description": (
        "Desenvolvimento de sistemas web e mobile, automação de processos, "
        "controle de produção, gestão de cobranças, escalas, condomínios e eventos."
    ),
    "email": "",
    "whatsapp_number": WHATSAPP_NUMBER,
    "whatsapp_url": f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(WHATSAPP_MESSAGE)}",
}

NAV_ITEMS = [
    {"label": "Início", "href": "/"},
    {"label": "Soluções", "href": "/#solucoes"},
    {"label": "Serviços", "href": "/#servicos"},
    {"label": "Sobre", "href": "/#sobre"},
    {"label": "Contato", "href": "/#contato"},
]

CONTACT_SOLUTION_CHOICES = [
    ("sistema-personalizado", "Desenvolvimento de sistema personalizado"),
    ("gestao-encomendas", "Gestão de encomendas"),
    ("gestao-cobrancas", "Gestão de cobranças"),
    ("fabriq", "Controle de fábrica - Fabriq"),
    ("gestao-escalas", "Gestão de escalas"),
    ("controle-entrada-saida", "Controle de entrada e saída"),
    ("integracao-automacao", "Integração ou automação"),
    ("consultoria-tecnica", "Consultoria técnica"),
    ("outro", "Outro"),
]

PILLARS = [
    {
        "label": "01",
        "title": "Entendimento do negócio",
        "text": "Analisamos o processo antes de definir a tecnologia.",
    },
    {
        "label": "02",
        "title": "Desenvolvimento personalizado",
        "text": "Criamos sistemas de acordo com as necessidades reais de cada operação.",
    },
    {
        "label": "03",
        "title": "Evolução contínua",
        "text": "As soluções podem crescer e receber novos recursos conforme o negócio evolui.",
    },
]

SOLUTIONS = [
    {
        "slug": "encomendas-condominio",
        "name": "CondoEntrega",
        "subtitle": "Gestão de encomendas para condomínios",
        "icon": "CE",
        "accent": "cyan",
        "short_description": (
            "Sistema para registrar, organizar e acompanhar o recebimento e a retirada "
            "de encomendas em condomínios."
        ),
        "problem": (
            "Portarias que dependem de livros, planilhas ou mensagens soltas perdem "
            "rastreabilidade e tornam a retirada de encomendas mais lenta."
        ),
        "solution": (
            "O CondoEntrega centraliza moradores, unidades, entradas, retiradas e histórico "
            "de movimentações em um fluxo digital preparado para a rotina da portaria."
        ),
        "highlight": "Rastreabilidade da portaria até a retirada.",
        "features": [
            "Cadastro de moradores e unidades",
            "Registro de encomendas na portaria",
            "Identificação de quem recebeu",
            "Notificação de encomenda disponível",
            "Confirmação de retirada",
            "Histórico de movimentações",
            "Redução de papéis e controles manuais",
            "Rastreabilidade das entregas",
        ],
        "audience": [
            "Condomínios residenciais",
            "Condomínios comerciais",
            "Administradoras",
            "Empresas de portaria",
        ],
        "benefits": [
            "Organização da rotina da portaria",
            "Consulta rápida por morador ou unidade",
            "Mais segurança no registro de retirada",
        ],
        "mockup": {
            "title": "Fila de encomendas",
            "primary": "Aguardando retirada",
            "rows": ["Unidade 1204", "Recebida na portaria", "Retirada confirmada"],
            "tags": ["Portaria", "Morador", "Histórico"],
        },
    },
    {
        "slug": "gestao-cobrancas",
        "name": "Gestão de Cobranças",
        "subtitle": "Controle financeiro centralizado",
        "icon": "R$",
        "accent": "blue",
        "short_description": (
            "Plataforma para centralizar cobranças, acompanhar boletos e facilitar o "
            "controle financeiro da organização."
        ),
        "problem": (
            "Cobranças acompanhadas manualmente exigem conferências constantes, dificultam "
            "a priorização e espalham informações financeiras por vários controles."
        ),
        "solution": (
            "A plataforma reúne cobranças, vencimentos, histórico por cliente e relatórios "
            "em um ambiente único, com integrações financeiras quando aplicável."
        ),
        "highlight": "Cobranças, boletos e histórico em um só fluxo.",
        "features": [
            "Geração e acompanhamento de cobranças",
            "Controle de boletos pendentes, pagos e vencidos",
            "Consulta por cliente",
            "Histórico financeiro",
            "Organização de vencimentos",
            "Relatórios",
            "Redução do acompanhamento manual",
            "Integração com serviços financeiros quando aplicável",
        ],
        "audience": [
            "Empresas",
            "Organizações",
            "Associações",
            "Times financeiros",
        ],
        "benefits": [
            "Visão organizada dos vencimentos",
            "Menos dependência de planilhas",
            "Acompanhamento financeiro mais claro",
        ],
        "mockup": {
            "title": "Painel de cobranças",
            "primary": "Vencimentos organizados",
            "rows": ["Cliente selecionado", "Boleto pendente", "Histórico financeiro"],
            "tags": ["Pendentes", "Pagos", "Relatórios"],
        },
    },
    {
        "slug": "fabriq",
        "name": "Fabriq",
        "subtitle": "Controle digital das etapas de produção",
        "icon": "FQ",
        "accent": "green",
        "short_description": (
            "Sistema desenvolvido para acompanhar processos de uma fábrica desde o "
            "recebimento da matéria-prima até a liberação do produto final."
        ),
        "problem": (
            "Operações industriais com registros descentralizados têm dificuldade para "
            "acompanhar lotes, evidências, qualidade, temperatura, limpeza e aprovações."
        ),
        "solution": (
            "O Fabriq centraliza as etapas produtivas, documentos e resultados laboratoriais, "
            "aumentando a rastreabilidade e a organização da operação."
        ),
        "highlight": "Informações produtivas centralizadas e rastreáveis.",
        "features": [
            "Controle de produção",
            "Rastreabilidade de lotes",
            "Registro de matérias-primas",
            "Controle de qualidade",
            "Liberação de produtos",
            "Armazenamento de resultados laboratoriais",
            "Controle de temperatura",
            "Registros de limpeza e manutenção",
            "Aprovações eletrônicas",
            "Histórico das etapas produtivas",
            "Organização de documentos e evidências",
        ],
        "audience": [
            "Fábricas",
            "Indústrias",
            "Laboratórios internos",
            "Equipes de qualidade",
        ],
        "benefits": [
            "Rastreabilidade entre etapas",
            "Menos controles paralelos",
            "Documentação mais organizada",
        ],
        "mockup": {
            "title": "Ordem de produção",
            "primary": "Etapa em validação",
            "rows": ["Matéria-prima registrada", "Temperatura anotada", "Qualidade em análise"],
            "tags": ["Lotes", "Evidências", "Aprovações"],
        },
    },
    {
        "slug": "connect-pibvp",
        "name": "Connect PIBVP",
        "subtitle": "Gerenciamento de equipes e escalas",
        "icon": "EV",
        "accent": "violet",
        "short_description": (
            "Sistema criado para organizar voluntários, equipes, eventos e escalas da PIBVP."
        ),
        "problem": (
            "Equipes, eventos e escalas organizados por mensagens soltas dificultam "
            "confirmações, comunicação e acompanhamento dos compromissos."
        ),
        "solution": (
            "O Connect PIBVP organiza usuários, equipes, eventos, escalas e confirmações "
            "em um fluxo claro para comunidades e organizações."
        ),
        "highlight": "Equipes, eventos e confirmações em um ambiente centralizado.",
        "features": [
            "Cadastro de usuários",
            "Organização de equipes",
            "Criação de eventos",
            "Montagem de escalas",
            "Visualização de compromissos",
            "Notificações",
            "Confirmação de participação",
            "Organização por função ou ministério",
            "Comunicação centralizada",
            "Acompanhamento das atividades",
        ],
        "audience": [
            "Organizações",
            "Comunidades",
            "Equipes de voluntários",
            "Coordenações de eventos",
        ],
        "benefits": [
            "Escalas mais claras",
            "Confirmação de participação",
            "Comunicação menos dispersa",
        ],
        "mockup": {
            "title": "Agenda de equipes",
            "primary": "Escala publicada",
            "rows": ["Equipe organizada", "Evento agendado", "Participação confirmada"],
            "tags": ["Equipes", "Eventos", "Notificações"],
        },
    },
    {
        "slug": "ebf-checkin",
        "name": "EBF Check-in",
        "subtitle": "Entrada e saída segura de crianças",
        "icon": "QR",
        "accent": "amber",
        "short_description": (
            "Sistema para controlar o cadastro, a entrada, a permanência e a saída de "
            "crianças durante eventos."
        ),
        "problem": (
            "Recepções com muitas crianças precisam registrar responsáveis, alergias, "
            "turmas, entrada e saída sem depender de papéis difíceis de consultar."
        ),
        "solution": (
            "O EBF Check-in estrutura o fluxo de cadastro, identificação, presença e "
            "checkout, registrando o responsável autorizado na saída."
        ),
        "highlight": "Check-in, identificação e checkout com rastreabilidade.",
        "features": [
            "Cadastro das crianças",
            "Cadastro de responsáveis",
            "Registro de alergias e informações importantes",
            "Separação por turma",
            "Check-in",
            "Geração de identificação",
            "Utilização de QR Code",
            "Impressão de etiquetas",
            "Controle de presença",
            "Checkout com registro do responsável",
            "Histórico de entrada e saída",
            "Relatórios por turma e por evento",
        ],
        "audience": [
            "Eventos infantis",
            "Organizações",
            "Equipes de recepção",
            "Coordenações de turma",
        ],
        "benefits": [
            "Mais organização",
            "Agilidade na recepção",
            "Rastreabilidade",
            "Segurança na entrega ao responsável autorizado",
        ],
        "mockup": {
            "title": "Check-in do evento",
            "primary": "Identificação gerada",
            "rows": ["Criança cadastrada", "Responsável autorizado", "Checkout registrado"],
            "tags": ["QR Code", "Turmas", "Etiquetas"],
        },
    },
]

SERVICES = [
    {
        "title": "Desenvolvimento de sistemas web",
        "text": "Sistemas administrativos, portais, dashboards, APIs e plataformas empresariais.",
    },
    {
        "title": "Aplicativos e soluções mobile",
        "text": "Aplicações adaptadas para celulares, tablets, totens e operações em campo.",
    },
    {
        "title": "Integrações e automações",
        "text": "Integração entre sistemas, APIs, notificações, webhooks e automação de tarefas.",
    },
    {
        "title": "Infraestrutura e implantação",
        "text": "Configuração de servidores, containers, ambientes, proxies, bancos de dados e publicação de aplicações.",
    },
    {
        "title": "Consultoria técnica",
        "text": "Análise de arquitetura, modernização de sistemas, segurança, desempenho e evolução tecnológica.",
    },
]

PROCESS_STEPS = [
    {
        "title": "Entendimento do processo",
        "text": "Conhecemos a rotina, as dificuldades e os objetivos antes de propor qualquer tecnologia.",
    },
    {
        "title": "Levantamento dos requisitos",
        "text": "Organizamos necessidades, regras, usuários e prioridades da solução.",
    },
    {
        "title": "Planejamento da solução",
        "text": "Definimos arquitetura, etapas, integrações e caminhos de implantação.",
    },
    {
        "title": "Desenvolvimento",
        "text": "Construímos telas, fluxos, integrações e estrutura técnica com ciclos de validação.",
    },
    {
        "title": "Validação com o cliente",
        "text": "Ajustamos a solução com base no uso real e nas regras da operação.",
    },
    {
        "title": "Implantação",
        "text": "Publicamos, configuramos ambientes e apoiamos a entrada em operação.",
    },
    {
        "title": "Suporte e evolução",
        "text": "Acompanhamos melhorias, correções e novos recursos conforme o negócio evolui.",
    },
]

DIFFERENTIALS = [
    "Solução adaptada ao processo do cliente",
    "Contato direto durante o desenvolvimento",
    "Experiência com diferentes segmentos",
    "Preocupação com segurança e rastreabilidade",
    "Sistemas preparados para evoluir",
    "Integração com tecnologias já utilizadas pelo cliente",
    "Suporte técnico próximo",
    "Domínio de desenvolvimento e infraestrutura",
]


def get_solution(slug):
    return next((solution for solution in SOLUTIONS if solution["slug"] == slug), None)


def get_site_context():
    return {
        "site": SITE,
        "nav_items": NAV_ITEMS,
        "solutions": SOLUTIONS,
        "services": SERVICES,
        "pillars": PILLARS,
        "process_steps": PROCESS_STEPS,
        "differentials": DIFFERENTIALS,
        "current_year": date.today().year,
    }
