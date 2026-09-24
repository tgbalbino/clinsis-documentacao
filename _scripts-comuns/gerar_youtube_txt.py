# -*- coding: utf-8 -*-
import glob
import os
import re
import sys

RAIZ = r"C:\Projetos\W_Clinica\Documentacao-Entrega"
SITE = "https://tgbalbino.github.io/clinsis-documentacao/"
IGNORAR = {"Marca-ClinSis", "_scripts-comuns", "site", "youtube_upload", "Area-do-Profissional"}


def limpar(t):
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*([^*]*)\*\*", r"\1", t)
    return t.strip()


def ler_md(caminho):
    linhas = open(caminho, encoding="utf-8").read().splitlines()
    titulo = subtitulo = ""
    intro = []
    topicos = []
    estado = "cab"
    for l in linhas:
        if l.startswith("# ") and not titulo:
            titulo = limpar(l[2:])
            continue
        if not subtitulo and l.startswith("_") and l.endswith("_"):
            subtitulo = limpar(l.strip("_"))
            continue
        if l.startswith("## "):
            estado = "topicos"
            t = limpar(l[3:])
            if t and t not in topicos:
                topicos.append(t)
            continue
        if estado == "cab" and l.strip() and not l.startswith(("Versão", "Vídeo narrado", "---")):
            intro.append(limpar(l))
    return titulo, subtitulo, " ".join(intro), topicos


def ler_pdf(caminho):
    import pymupdf
    d = pymupdf.open(caminho)
    texto = " ".join(d[i].get_text() for i in range(min(3, len(d))))
    texto = re.sub(r"\s+", " ", texto)
    return texto[:700]


def encurtar(t, n):
    if len(t) <= n:
        return t
    corte = t[:n].rsplit(" ", 1)[0]
    return corte.rstrip(",;:") + "..."


for pasta in sorted(os.listdir(RAIZ)):
    caminho = os.path.join(RAIZ, pasta)
    if not os.path.isdir(caminho) or pasta in IGNORAR:
        continue
    videos = sorted(glob.glob(os.path.join(caminho, "*.mp4")))
    if not videos:
        continue
    mds = glob.glob(os.path.join(caminho, "*.md"))
    if mds:
        titulo, subtitulo, intro, topicos = ler_md(mds[0])
    else:
        titulo = pasta.replace("-", " ")
        subtitulo = ""
        pdfs = [p for p in glob.glob(os.path.join(caminho, "*.pdf")) if "Simplificado" not in p]
        intro = ler_pdf(pdfs[0]) if pdfs else ""
        topicos = []
    if pasta == "Dashboard-Financeiro-e-Fluxo-Caixa":
        titulo = "Dashboard Financeiro e Fluxo de Caixa"
        subtitulo = "O que é cada informação exibida na tela e de onde ela vem no sistema"
        intro = ("Explicação das duas telas financeiras do ClinSis: o Dashboard Financeiro e o Fluxo de Caixa. "
                 "Mostra o que significa cada card, gráfico e tabela e de onde vem cada número, com exemplos reais.")
        topicos = ["Dashboard Financeiro: cards, gráficos e tabelas", "Fluxo de Caixa: entradas, saídas e saldo"]
    if not titulo:
        titulo = pasta.replace("-", " ")

    saida = []
    saida.append(f"TÍTULOS E DESCRIÇÕES PARA O YOUTUBE — {titulo}")
    saida.append("=" * 70)
    saida.append("Sugestão: publique os dois vídeos da pasta (com e sem legenda) ou só o com legenda,")
    saida.append("como preferir. Cada bloco abaixo pode ser copiado direto para o YouTube.")
    saida.append("")
    for v in videos:
        nome = os.path.basename(v)
        if nome.startswith("video-com-legenda-conteudo") or nome == "video-narrado.mp4":
            continue
        legenda = "com-legenda" in nome
        sufixo = " (com legendas)" if legenda else " (sem legendas)"
        titulo_yt = encurtar(f"ClinSis | {titulo}{sufixo}", 100)
        desc = []
        if subtitulo:
            desc.append(subtitulo + ".")
        if intro:
            desc.append(encurtar(intro, 600))
        if topicos:
            desc.append("Neste vídeo:\n" + "\n".join("• " + t for t in topicos[:10]))
        desc.append("Manual em PDF (completo e simplificado) e as demais rotinas do ClinSis:\n" + SITE)
        desc.append("#ClinSis #GestãoDeClínicas #Tutorial")
        saida.append(f"ARQUIVO DO VÍDEO: {nome}")
        saida.append("")
        saida.append("TÍTULO:")
        saida.append(titulo_yt)
        saida.append("")
        saida.append("DESCRIÇÃO:")
        saida.append("\n\n".join(desc))
        saida.append("")
        saida.append("-" * 70)
        saida.append("")
    destino = os.path.join(caminho, "YouTube_Titulo_e_Descricao.txt")
    with open(destino, "w", encoding="utf-8-sig", newline="\r\n") as f:
        f.write("\n".join(saida))
    print("ok", pasta, len(videos))
