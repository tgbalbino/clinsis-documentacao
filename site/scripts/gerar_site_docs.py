# -*- coding: utf-8 -*-
"""Gera o site MkDocs a partir das pastas de Documentacao-Entrega."""
import os
import re
import shutil

ENTREGA = r"C:\Projetos\W_Clinica\Documentacao-Entrega"
SITE = os.path.join(ENTREGA, "site")
DOCS = os.path.join(SITE, "docs")

# (pasta_origem, categoria, slug_categoria, titulo_curto_menu)
ROTINAS = [
    ("Manual-Base-ClinSis", "Base", "introducao", "Manual Base do ClinSis"),

    ("Cadastro-de-Especialidades", "Cadastros Gerais", "cadastros", "Cadastro de Especialidades"),
    ("Cadastro-de-Servicos", "Cadastros Gerais", "cadastros", "Cadastro de Serviços"),

    ("Checkin", "Agenda e Atendimento", "agenda", "Checkin de Paciente"),
    ("WhatsApp", "Agenda e Atendimento", "agenda", "WhatsApp - lembretes e confirmações"),
    ("Dashboard-de-Agenda", "Agenda e Atendimento", "agenda", "Dashboard de Agenda"),

    ("Layout-de-Contrato", "Contrato", "contrato", "Layout de Contrato"),
    ("Contrato", "Contrato", "contrato", "Contrato (sem assinatura digital)"),
    ("Contrato-D4Sign", "Contrato", "contrato", "Contrato com Assinatura Digital (D4Sign)"),

    ("Prontuario-Configuracao", "Prontuário", "prontuario", "Prontuário — Configuração (Tipos, Alíneas e Textos padrão)"),
    ("Prontuario-Uso", "Prontuário", "prontuario", "Prontuário — Uso pelo Profissional"),
    ("Prontuario-Auditoria", "Prontuário", "prontuario", "Prontuário — Auditoria e Relatórios"),

    ("Area-do-Profissional", "Área do Profissional", "area-do-profissional", "Manual da Área do Profissional"),

    ("Tabela-de-Precos-Cobranca", "Cobrança e Pagamento", "cobranca-pagamento", "Tabela de Valores para Cobrança"),
    ("Tabela-de-Precos-Pagamento", "Cobrança e Pagamento", "cobranca-pagamento", "Tabela de Valores para Pagamento"),
    ("Previsao-de-Faturamento", "Cobrança e Pagamento", "cobranca-pagamento", "Previsão de Faturamento da Agenda"),
    ("Cobranca-de-Paciente", "Cobrança e Pagamento", "cobranca-pagamento", "Cobrança de Paciente"),
    ("Pagamento-de-Profissionais", "Cobrança e Pagamento", "cobranca-pagamento", "Pagamento de Profissionais"),

    ("Cadastro-Plano-de-Contas", "Financeiro", "financeiro", "Cadastro de Plano de Contas"),
    ("Cadastro-Centro-de-Custo", "Financeiro", "financeiro", "Cadastro de Centro de Custo"),
    ("Conta-Financeira", "Financeiro", "financeiro", "Cadastro de Conta Financeira"),
    ("Contas-Recorrentes", "Financeiro", "financeiro", "Contas Recorrentes"),
    ("Contas-a-Pagar", "Financeiro", "financeiro", "Contas a Pagar"),
    ("Contas-a-Receber", "Financeiro", "financeiro", "Contas a Receber"),
    ("Movimentos-Financeiros", "Financeiro", "financeiro", "Movimentos Financeiros"),
    ("Modulo-de-Caixa", "Financeiro", "financeiro", "Módulo de Caixa"),
    ("Conciliacao-Bancaria-OFX", "Financeiro", "financeiro", "Conciliação Bancária (OFX)"),
    ("Dashboard-Financeiro-e-Fluxo-Caixa", "Financeiro", "financeiro", "Dashboard Financeiro e Fluxo de Caixa"),]

# Links do YouTube: preencha aqui quando os vídeos forem publicados.
# Chave = pasta de origem; valor = url do vídeo com legenda (str) ou (url_com_legenda, url_sem_legenda)
YOUTUBE_LINKS = {
    "Manual-Base-ClinSis": "https://youtu.be/bba5Ib4ly8Q",
    "Cadastro-Plano-de-Contas": "https://youtu.be/KJhezxjX10w",
    "Cadastro-Centro-de-Custo": "https://youtu.be/TGcyxaZc2QY",
    "Conta-Financeira": "https://youtu.be/m-j4pqukoHg",
    "Cadastro-de-Especialidades": "https://youtu.be/mtXmqvbPCkM",
    "Cadastro-de-Servicos": "https://youtu.be/Zk-GdESYkls",
    "Tabela-de-Precos-Cobranca": "https://youtu.be/DyyO49lac8I",
    "Tabela-de-Precos-Pagamento": "https://youtu.be/tupHNaRxSrY",
    "Prontuario-Configuracao": "https://youtu.be/tMs3WdzjMSg",
    "Layout-de-Contrato": "https://youtu.be/xh1Ja1kJ0Vo",
    "Modulo-de-Caixa": "https://youtu.be/yv9WdeiVlhI",
    "Contas-a-Receber": "https://youtu.be/PFpYbTqKvFM",
    "Contas-a-Pagar": "https://youtu.be/LIRC0NJ6Z3c",
    "Contas-Recorrentes": "https://youtu.be/74XN1Jb4f_c",
    "Movimentos-Financeiros": "https://youtu.be/md1GdiLY9Qw",
    "Checkin": "https://youtu.be/MKW8mdKnfTg",
    "Prontuario-Uso": "https://youtu.be/lCpFbKV5WrI",
    "Contrato": "https://youtu.be/szRnAwHrqI4",
    "Contrato-D4Sign": "https://youtu.be/eg7ABN_eNyo",
    "Cobranca-de-Paciente": "https://youtu.be/ViW55USFc6I",
    "Pagamento-de-Profissionais": "https://youtu.be/PkvsWwKU2nM",
    "Dashboard-de-Agenda": "https://youtu.be/yMswtbogABA",
    "Prontuario-Auditoria": "https://youtu.be/xdxI2t3df8w",
    "Dashboard-Financeiro-e-Fluxo-Caixa": "https://youtu.be/WCa8gVOdXKE",
    "Conciliacao-Bancaria-OFX": "https://youtu.be/17EE36VWZHM",
    "WhatsApp": "https://youtu.be/2lvKkYApZFE",
    "Area-do-Profissional": "https://youtu.be/TAq1nN4P4DM",
    "Previsao-de-Faturamento": "https://youtu.be/Aft3I2vvkLk",
}


# Texto de apresentação de cada página (aparece logo abaixo do título). Chave = pasta de origem.
# Explica o que é a rotina, para que serve e quando usar; substitui o subtítulo curto do manual.
INTRO_SITE = {
    "Manual-Base-ClinSis": "Ponto de partida para quem vai usar o ClinSis. Apresenta o sistema, o fluxo geral de trabalho e os cadastros essenciais (clínica, setores, especialidades, profissionais, pacientes e operadoras), além do cadastro de usuários e da criação da agenda. Leia primeiro: as demais rotinas dependem do que é configurado aqui.",
    "Cadastro-de-Especialidades": "As especialidades definem a área de atuação de cada profissional e influenciam outras rotinas: o Tipo de Cobrança determina como o profissional é pago (por sessão ou por paciente) e o Relatório Compartilhado controla quais prontuários podem ser vistos entre profissionais. Cadastre-as antes dos profissionais, das tabelas de valores e da agenda.",
    "Cadastro-de-Servicos": "Serviço é o item que a clínica vende ao paciente dentro de um Contrato (por exemplo, um pacote de sessões). Este manual mostra como cadastrar os serviços, reajustar preços em massa e onde cada serviço aparece no sistema. Cadastre os serviços antes de criar contratos.",
    "Checkin": "O Check-in registra a chegada do paciente à clínica. Quando o atendimento é cobrável, o pagamento já pode ser lançado na hora, evitando cobranças esquecidas e mantendo o caixa conferido no mesmo dia. Rotina diária da recepção.",
    "WhatsApp": "Envia lembretes e pedidos de confirmação aos pacientes pelo WhatsApp, reduzindo faltas e horários vagos. Existem dois modos: envio manual, feito pela recepção, e envio automático pela API oficial da Meta. O manual cobre requisitos, configuração, templates, consentimento e acompanhamento dos envios.",
    "Dashboard-de-Agenda": "O Dashboard é um painel que reúne, numa única tela e em forma de cards, gráficos e tabelas, os principais números de um período, para que o gestor acompanhe o desempenho sem montar relatórios manualmente. O Dashboard de Agenda mostra sessões realizadas, presença e faltas (absenteísmo), antecedência dos agendamentos, ocupação da agenda e faturamento por convênio. Serve para avaliar a produtividade da clínica, identificar problemas como excesso de faltas e apoiar decisões. O manual explica o que cada indicador significa e como conferir o número dentro do sistema.",
    "Layout-de-Contrato": "O layout é o modelo (template) usado para gerar o PDF de todos os contratos da clínica: texto, cabeçalho e dados que aparecem no documento. Aqui você aprende a editar o modelo, usar o modelo padrão, pré-visualizar e ativar o layout. Configure antes de emitir os primeiros contratos.",
    "Contrato": "Contrato formaliza a venda de serviços ao paciente, com as condições de pagamento acordadas. Este manual acompanha o ciclo completo sem assinatura digital: criação, adição de serviços, fechamento (que gera a Conta a Receber), aviso de vencimento e renovação.",
    "Contrato-D4Sign": "Complementa o Contrato com assinatura eletrônica pela D4Sign: o contrato é enviado ao paciente para assinar à distância, a assinatura é acompanhada no sistema e, quando concluída, o contrato é fechado automaticamente. Evita impressão e coleta de assinatura em papel.",
    "Prontuario-Configuracao": "Prepara o prontuário eletrônico antes do uso pelos profissionais: Tipos de prontuário (a estrutura de cada modelo), Alíneas (os campos de cada tipo) e Textos padrão (frases prontas para agilizar o preenchimento). Rotina feita pela administração, normalmente uma vez e depois ajustada conforme a necessidade.",
    "Prontuario-Uso": "Passo a passo do profissional no prontuário: encontrar, criar, preencher, finalizar, consultar e imprimir prontuários, além de tags e consulta a prontuários de outros profissionais. Mostra também o que não pode ser alterado depois de finalizado.",
    "Prontuario-Auditoria": "Relatórios para a administração conferir se cada atendimento realizado gerou o prontuário correspondente: Auditoria de Prontuários, Produção de Prontuários e Atendimentos Sequenciais. Ajuda a identificar atendimentos sem registro e inclui um roteiro de conferência mensal.",
    "Area-do-Profissional": "Visão do profissional de saúde no ClinSis: home com resumo do dia e pendências, agenda, lista de pacientes, prontuário e atendimento (receituário). Reúne em um só lugar o que o profissional precisa no dia a dia, inclusive pelo celular.",
    "Tabela-de-Precos-Cobranca": "Define quanto a clínica cobra por sessão, por Especialidade, Profissional e Operadora. É a base do cálculo da Cobrança de Paciente e da Previsão de Faturamento. O manual mostra o cadastro, o reajuste de preço em massa e a diferença para a Tabela de Pagamento.",
    "Tabela-de-Precos-Pagamento": "Define quanto a clínica paga a cada profissional, por Especialidade e Profissional, incluindo valores por tipo de marcação. É a base do cálculo do Pagamento de Profissionais. O manual mostra o conceito de Tabela de Valores, as abas de valores e o reajuste de preço em massa.",
    "Previsao-de-Faturamento": "Estima quanto a clínica deve faturar no mês com base na agenda, nos valores cadastrados e na probabilidade histórica de comparecimento. Serve para planejar o caixa, acompanhar a meta e conferir agenda e financeiro. O manual explica a configuração, como o valor é calculado e como conferir cada número.",
    "Cobranca-de-Paciente": "Calcula e gera, de uma só vez, a cobrança de todos os pacientes particulares do mês a partir das sessões realizadas, criando as Contas a Receber correspondentes. Possui relatórios sintético e analítico para conferência e proteção contra cobrança em duplicidade. Depende da Tabela de Valores para Cobrança.",
    "Pagamento-de-Profissionais": "Calcula e gera, de uma só vez, o repasse de todos os profissionais no mês a partir das sessões realizadas, criando as Contas a Pagar correspondentes. Possui relatórios sintético e analítico, exportação para planilha e depende da Tabela de Valores para Pagamento.",
    "Cadastro-Plano-de-Contas": "O Plano de Contas organiza as categorias de receitas e despesas da clínica (por exemplo, aluguel, salários, consultas). Cada lançamento financeiro é classificado nele, o que permite saber de onde vem e para onde vai o dinheiro. Cadastre-o antes de lançar contas a pagar e a receber.",
    "Cadastro-Centro-de-Custo": "O Centro de Custo divide a clínica em setores ou áreas (por exemplo, recepção, fisioterapia) para mostrar qual parte gera receita e qual gera despesa. Complementa o Plano de Contas, que diz o tipo do gasto, enquanto o Centro de Custo diz onde ele ocorreu.",
    "Conta-Financeira": "Conta Financeira é o local onde o dinheiro da clínica fica: conta bancária, caixa ou carteira. Todo recebimento e pagamento é lançado em uma delas. O manual explica o cadastro, onde ela é usada e a validação entre Conta Financeira e Forma de Pagamento.",
    "Contas-Recorrentes": "Cadastro de contas que se repetem todo mês, ou em outro período (aluguel, internet, mensalidades), geradas automaticamente como Contas a Pagar ou a Receber. Evita lançar a mesma conta a cada mês e reduz esquecimentos.",
    "Contas-a-Pagar": "Controle das despesas da clínica: cadastro das contas, acompanhamento de vencimentos por indicadores e baixa (pagamento) quando elas são quitadas. Os pagamentos baixados alimentam os Movimentos Financeiros e o fluxo de caixa.",
    "Contas-a-Receber": "Controle dos valores que pacientes e convênios devem à clínica: cadastro das parcelas, acompanhamento de vencimentos e baixa (recebimento). Os recebimentos baixados alimentam os Movimentos Financeiros e o fluxo de caixa.",
    "Movimentos-Financeiros": "Extrato de cada Conta Financeira: lista todas as entradas e saídas já realizadas, vindas de baixas de contas, caixa e transferências. Serve para conferir o saldo, conciliar com o banco e fazer transferências entre contas.",
    "Modulo-de-Caixa": "Controle diário do caixa da clínica: abertura, lançamentos manuais (suprimento e sangria), recebimentos e pagamentos automáticos, fechamento e histórico. Garante que o dinheiro em caixa confira ao fim de cada dia ou turno.",
    "Conciliacao-Bancaria-OFX": "Confere o extrato do banco com os Movimentos Financeiros do ClinSis a partir de um arquivo OFX exportado do banco. O sistema sugere os pares e aponta divergências, garantindo que o saldo do sistema reflita o saldo real da conta.",
    "Dashboard-Financeiro-e-Fluxo-Caixa": "O Dashboard é um painel que reúne, numa única tela, os principais números de um período em indicadores, tabelas e gráficos, para que o gestor entenda a situação sem montar relatórios manualmente. O Dashboard Financeiro resume o que entrou, o que saiu, o resultado e o saldo de cada conta, com rankings e comparativo mensal. O Fluxo de Caixa mostra a movimentação por dia, semana ou mês e projeta o saldo futuro com base nas contas a pagar e a receber em aberto. Servem para acompanhar a saúde financeira, antecipar faltas de caixa e apoiar decisões. O manual explica cada indicador e de onde ele vem no sistema.",
}

def slugify(nome):
    s = nome.lower()
    s = (s.replace("ç", "c").replace("ã", "a").replace("á", "a").replace("â", "a")
           .replace("é", "e").replace("ê", "e").replace("í", "i").replace("ó", "o")
           .replace("ô", "o").replace("õ", "o").replace("ú", "u"))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def limpar_para_usuario_final(md):
    """Remove do texto do manual o que é técnico (arquivos de código, banco de dados, notas de
    correção interna), já que o site é destinado ao usuário final."""
    saida = []
    pular_nivel = None
    tabela_tecnica = False
    for l in md.split("\n"):
        m = re.match(r"^(#+)\s+(.*)", l)
        if m:
            nivel = len(m.group(1))
            if pular_nivel is not None and nivel <= pular_nivel:
                pular_nivel = None
            if pular_nivel is None and re.search(r"anexo t[eé]cnico", m.group(2), re.I):
                pular_nivel = nivel
                continue
        if pular_nivel is not None:
            continue
        if re.match(r"^>\s*.{0,4}Corre[cç][aã]o (feita|realizada)", l):
            continue
        if re.match(r"^(Assista ao v[ií]deo narrado|V[ií]deo narrado desta rotina)", l):
            continue  # o site já traz o vídeo incorporado na seção "Vídeo narrado"
        if l.startswith("|"):
            cel = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cel) == 3 and cel[1].startswith("Origem no banco"):
                tabela_tecnica = True
                l = "| Campo / Label na tela | O que é / de onde vem |"
            elif tabela_tecnica and len(cel) >= 3:
                if set(l.strip()) <= set("|- :"):
                    l = "|---|---|"
                else:
                    extra = " *(obrigatório)*" if cel[2].lower().startswith("obrigat") else ""
                    l = f"| {cel[0]} | {cel[1]}{extra} |"
        else:
            tabela_tecnica = False
        saida.append(l)
    return "\n".join(saida).replace("preservado no banco", "preservado no sistema")


def extrair_intro(md_path):
    if not os.path.exists(md_path):
        return None, None
    with open(md_path, encoding="utf-8") as f:
        linhas = f.readlines()
    titulo = None
    intro = []
    i = 0
    while i < len(linhas):
        l = linhas[i].strip()
        if l.startswith("# ") and titulo is None:
            titulo = l[2:].strip()
            i += 1
            continue
        if titulo is not None:
            if l.startswith("#"):
                break
            if l.startswith(">") or l.startswith("!["):
                i += 1
                continue
            if l:
                intro.append(l)
                if len(" ".join(intro)) > 500:
                    break
            elif intro:
                break
        i += 1
    return titulo, " ".join(intro) if intro else None


def main():
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)
    assets_dir = os.path.join(DOCS, "assets")
    os.makedirs(assets_dir)

    categorias = {}  # slug -> (nome, [ (slug_pagina, titulo_menu) ])

    for pasta, categoria, cat_slug, titulo_menu in ROTINAS:
        origem = os.path.join(ENTREGA, pasta)
        if not os.path.isdir(origem):
            print("AVISO: pasta não encontrada:", origem)
            continue

        arquivos = os.listdir(origem)
        pdfs = sorted([a for a in arquivos if a.lower().endswith(".pdf")])
        pdf_completo = next((a for a in pdfs if "simplificado" not in a.lower()), None)
        pdf_simples = next((a for a in pdfs if "simplificado" in a.lower()), None)
        mds = [a for a in arquivos if a.lower().endswith(".md")]
        md_path = os.path.join(origem, mds[0]) if mds else None

        titulo, intro = extrair_intro(md_path) if md_path else (None, None)
        titulo = titulo or titulo_menu
        intro = INTRO_SITE.get(pasta, intro)

        # copia PDFs para docs/assets/<pasta>/
        dest_assets = os.path.join(assets_dir, pasta)
        os.makedirs(dest_assets, exist_ok=True)
        for pdf in pdfs:
            if pdf == pdf_completo and pdf_simples:
                continue  # o completo tem coluna técnica (banco/código): não é publicado para o usuário final
            shutil.copy2(os.path.join(origem, pdf), os.path.join(dest_assets, pdf))

        pagina_slug = slugify(pasta)
        pagina_dir = os.path.join(DOCS, cat_slug)
        os.makedirs(pagina_dir, exist_ok=True)
        pagina_path = os.path.join(pagina_dir, pagina_slug + ".md")

        linhas_md = [f"# {titulo}", ""]
        if intro:
            linhas_md += [intro, ""]

        linhas_md += ["## Documentação em PDF", ""]
        pdf_publico = pdf_simples or pdf_completo
        if pdf_publico:
            linhas_md.append(f"- [📄 Manual em PDF](../assets/{pasta}/{pdf_publico})")
        linhas_md.append("")

        linhas_md += ["## Vídeo narrado", ""]
        yt = YOUTUBE_LINKS.get(pasta)
        if yt:
            if isinstance(yt, str):
                vid = yt.rstrip("/").split("/")[-1]
                linhas_md.append(
                    '<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">'
                    f'<iframe src="https://www.youtube.com/embed/{vid}?rel=0" title="Vídeo narrado" '
                    'style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" '
                    'allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" '
                    'allowfullscreen></iframe></div>')
                linhas_md.append("")
                linhas_md.append(f"[Abrir no YouTube]({yt})")
            else:
                linhas_md.append(f"- [▶️ Assistir com legenda]({yt[0]})")
                linhas_md.append(f"- [▶️ Assistir sem legenda]({yt[1]})")
        else:
            linhas_md.append("*Vídeo em processo de publicação — o link será adicionado aqui assim que estiver disponível no YouTube.*")
        linhas_md.append("")

        if md_path:
            linhas_md += ["## Conteúdo completo do manual", "", "---", ""]
            with open(md_path, encoding="utf-8") as f:
                conteudo = f.read()
            # remove o H1 duplicado do topo do md original
            conteudo = re.sub(r"^#\s+.*\n", "", conteudo, count=1)
            # remove blocos de imagem (![legenda](arquivo.png) + linha em branco + _legenda_),
            # pois os screenshots originais não fazem parte da entrega final (só o PDF já renderizado os tem)
            conteudo = re.sub(r"!\[.*?\]\([^)\n]+\.png\)\n\n_.*?_\n", "", conteudo, flags=re.DOTALL)
            linhas_md.append(limpar_para_usuario_final(conteudo))

        with open(pagina_path, "w", encoding="utf-8") as f:
            f.write("\n".join(linhas_md))

        categorias.setdefault(cat_slug, [categoria, []])
        categorias[cat_slug][1].append((f"{cat_slug}/{pagina_slug}.md", titulo_menu))

    # index.md
    with open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8") as f:
        f.write("# Documentação de Rotinas do ClinSis\n\n")
        f.write("Central de manuais (PDF) e vídeos narrados de cada rotina do sistema, organizados por área.\n\n")
        for cat_slug, (nome, paginas) in categorias.items():
            f.write(f"## {nome}\n\n")
            for caminho, titulo_menu in paginas:
                f.write(f"- [{titulo_menu}]({caminho})\n")
            f.write("\n")

    # mkdocs.yml
    nav_lines = ["nav:", "  - Início: index.md"]
    for cat_slug, (nome, paginas) in categorias.items():
        nav_lines.append(f"  - {nome}:")
        for caminho, titulo_menu in paginas:
            nav_lines.append(f"      - {titulo_menu}: {caminho}")

    mkdocs_yml = f"""site_name: Documentação ClinSis
site_description: Manuais e vídeos das rotinas do sistema ClinSis
theme:
  name: material
  language: pt-BR
  palette:
    - scheme: default
      primary: indigo
      toggle:
        icon: material/brightness-7
        name: Modo escuro
    - scheme: slate
      primary: indigo
      toggle:
        icon: material/brightness-4
        name: Modo claro
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.suggest
    - content.action.edit
markdown_extensions:
  - admonition
  - tables
  - toc:
      permalink: true
site_dir: publicado
{chr(10).join(nav_lines)}
"""
    with open(os.path.join(SITE, "mkdocs.yml"), "w", encoding="utf-8") as f:
        f.write(mkdocs_yml)

    print("Site gerado em", SITE)
    print("Rotinas processadas:", sum(len(v[1]) for v in categorias.values()))


if __name__ == "__main__":
    main()
