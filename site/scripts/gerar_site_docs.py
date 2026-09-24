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
    ("Manual-Base-ClinSis", "Introdução", "introducao", "Manual Base do ClinSis"),

    ("Dashboard-Financeiro-e-Fluxo-Caixa", "Financeiro", "financeiro", "Dashboard Financeiro e Fluxo de Caixa"),
    ("Cadastro-Plano-de-Contas", "Financeiro", "financeiro", "Cadastro de Plano de Contas"),
    ("Cadastro-Centro-de-Custo", "Financeiro", "financeiro", "Cadastro de Centro de Custo"),
    ("Conta-Financeira", "Financeiro", "financeiro", "Cadastro de Conta Financeira"),
    ("Contas-Recorrentes", "Financeiro", "financeiro", "Contas Recorrentes"),
    ("Contas-a-Pagar", "Financeiro", "financeiro", "Contas a Pagar"),
    ("Contas-a-Receber", "Financeiro", "financeiro", "Contas a Receber"),
    ("Movimentos-Financeiros", "Financeiro", "financeiro", "Movimentos Financeiros"),
    ("Modulo-de-Caixa", "Financeiro", "financeiro", "Módulo de Caixa"),
    ("Tabela-de-Precos-Pagamento", "Financeiro", "financeiro", "Tabela de Valores para Pagamento"),
    ("Tabela-de-Precos-Cobranca", "Financeiro", "financeiro", "Tabela de Valores para Cobrança"),

    ("Checkin", "Agenda e Atendimento", "agenda", "Checkin de Paciente"),
    ("Dashboard-de-Agenda", "Agenda e Atendimento", "agenda", "Dashboard de Agenda"),

    ("Cobranca-de-Paciente", "Cobrança e Pagamento", "cobranca-pagamento", "Cobrança de Paciente"),
    ("Pagamento-de-Profissionais", "Cobrança e Pagamento", "cobranca-pagamento", "Pagamento de Profissionais"),

    ("Contrato", "Contrato", "contrato", "Contrato (sem assinatura digital)"),
    ("Contrato-D4Sign", "Contrato", "contrato", "Contrato com Assinatura Digital (D4Sign)"),
    ("Layout-de-Contrato", "Contrato", "contrato", "Layout de Contrato"),

    ("Cadastro-de-Especialidades", "Cadastros Gerais", "cadastros", "Cadastro de Especialidades"),
    ("Cadastro-de-Servicos", "Cadastros Gerais", "cadastros", "Cadastro de Serviços"),

    ("Prontuario-Configuracao", "Prontuário", "prontuario", "Prontuário — Configuração (Tipos, Alíneas e Textos padrão)"),

    ("Prontuario-Uso", "Prontuário", "prontuario", "Prontuário — Uso pelo Profissional"),
    ("Prontuario-Auditoria", "Prontuário", "prontuario", "Prontuário — Auditoria e Relatórios"),
    ("Area-do-Profissional", "Área do Profissional", "area-do-profissional", "Manual da Área do Profissional"),
]

# Links do YouTube: preencha aqui quando os vídeos forem publicados.
# Chave = pasta de origem; valor = url do vídeo com legenda (str) ou (url_com_legenda, url_sem_legenda)
YOUTUBE_LINKS = {
    "Manual-Base-ClinSis": "https://youtu.be/r7iJc03azkw",
    "Cadastro-Plano-de-Contas": "https://youtu.be/m4e2BMEsMZg",
    "Cadastro-Centro-de-Custo": "https://youtu.be/mUPp2HgJV6I",
    "Conta-Financeira": "https://youtu.be/er1uv0qlUjk",
    "Cadastro-de-Especialidades": "https://youtu.be/9pTvpUSwb_g",
    "Cadastro-de-Servicos": "https://youtu.be/uotROr-rj6s",
    "Tabela-de-Precos-Cobranca": "https://youtu.be/mFThg03z-RY",
    "Tabela-de-Precos-Pagamento": "https://youtu.be/B5Jlz0kweIM",
    "Prontuario-Configuracao": "https://youtu.be/X4ClyuUIsAE",
    "Layout-de-Contrato": "https://youtu.be/w-cCTVEKQng",
    "Modulo-de-Caixa": "https://youtu.be/n7F19sn_uXs",
    "Contas-a-Receber": "https://youtu.be/72i8FLOKhII",
    "Contas-a-Pagar": "https://youtu.be/dlllj9on1gQ",
    "Contas-Recorrentes": "https://youtu.be/1qx_Mgp4T_Q",
    "Movimentos-Financeiros": "https://youtu.be/YEE6RAVUX8I",
    "Checkin": "https://youtu.be/6usoK6x4e3I",
    "Prontuario-Uso": "https://youtu.be/XPTXN2u41Ps",
    "Contrato": "https://youtu.be/c1ki58j_khQ",
    "Contrato-D4Sign": "https://youtu.be/OY-A2nyWsuA",
    "Cobranca-de-Paciente": "https://youtu.be/AdzPSoJ7_4I",
    "Pagamento-de-Profissionais": "https://youtu.be/0dVv7ctVDPE",
    "Dashboard-de-Agenda": "https://youtu.be/QAra0-JTD5w",
    "Prontuario-Auditoria": "https://youtu.be/xRpzTXrGA3Y",
    "Dashboard-Financeiro-e-Fluxo-Caixa": "https://youtu.be/aO-85WdVPYY",
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
