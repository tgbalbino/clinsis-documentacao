# -*- coding: utf-8 -*-
"""Monta a pasta C:\\Projetos\\W_Clinica\\Videos-YouTube com os vídeos (com legenda) de um lote, prontos para subir:
vídeo numerado + .json (título/descrição para o uploader) + miniatura + _Titulos_e_Descricoes_YouTube.txt. O conteúdo anterior da pasta vai para uma subpasta _anteriores-<data>.

Uso: python montar_pasta_youtube.py <AAAA-MM-DD>   (edite LOTE abaixo para o lote desejado)
Antes: gerar_youtube_txt.py (gera YouTube_Titulo_e_Descricao.txt em cada rotina).
"""
import glob
import os
import re
import shutil
import sys

RAIZ = r"C:\Projetos\W_Clinica\Documentacao-Entrega"
DEST = r"C:\Projetos\W_Clinica\Videos-YouTube"
DATA = sys.argv[1] if len(sys.argv) > 1 else "lote"

# (pasta da rotina, prefixo do arquivo de vídeo, título curto da miniatura, categoria)
LOTE = [
    ("Manual-Base-ClinSis", "video-manual-base-clinsis", "Manual Base do ClinSis", "PRIMEIROS PASSOS"),
    ("Cadastro-de-Servicos", "video-cadastro-servicos", "Serviços", "CADASTROS"),
    ("Tabela-de-Precos-Cobranca", "video-tabela-preco-cobranca", "Tabela de Valores: Cobrança", "CADASTROS"),
    ("Tabela-de-Precos-Pagamento", "video-tabela-preco-pagamento", "Tabela de Valores: Pagamento", "CADASTROS"),
    ("Movimentos-Financeiros", "video-movimentos-financeiros", "Movimentos Financeiros", "FINANCEIRO"),
    ("Conciliacao-Bancaria-OFX", "video-conciliacao-bancaria-ofx", "Conciliação Bancária (OFX)", "FINANCEIRO"),
    ("WhatsApp", "video-whatsapp", "WhatsApp: lembretes e confirmações", "AGENDA E ATENDIMENTO"),
    ("Dashboard-de-Agenda", "video-dashboard-agenda", "Dashboard de Agenda", "PAINÉIS"),
    ("Area-do-Profissional", "video-area-do-profissional", "Área do Profissional", "PRIMEIROS PASSOS"),
    ("Checkin", "video-checkin", "Checkin de Paciente", "ATENDIMENTO"),
]

# 1) guarda o que já estava na pasta
os.makedirs(DEST, exist_ok=True)
ant = os.path.join(DEST, f"_anteriores-{DATA}")
antigos = [f for f in os.listdir(DEST) if not f.startswith("_anteriores")] if not os.path.exists(ant) else []
if antigos:
    os.makedirs(ant, exist_ok=True)
    for f in antigos:
        shutil.move(os.path.join(DEST, f), os.path.join(ant, f))
    print("movidos para", ant, len(antigos))

# 2) miniaturas: reaproveita o desenho de gerar_miniaturas.py trocando a lista de itens
fonte = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gerar_miniaturas.py"), encoding="utf-8").read()
itens = [(i, v, p, t, c) for i, (p, v, t, c) in enumerate(LOTE, 1)]
fonte = re.sub(r"ITENS = \[.*?\n\]\n", "ITENS = " + repr(itens) + "\n", fonte, flags=re.S)
exec(compile(fonte, "gerar_miniaturas", "exec"), {"__name__": "__main__"})

# 3) vídeos numerados + títulos/descrições
blocos = ["TÍTULOS E DESCRIÇÕES — vídeos com legenda (lote de " + DATA + ")", "=" * 70, ""]
for n, (pasta, prefixo, _t, _c) in enumerate(LOTE, 1):
    origem = os.path.join(RAIZ, pasta, prefixo + "-com-legenda.mp4")
    nome = f"{n:02d}_{prefixo}-com-legenda.mp4"
    shutil.copy2(origem, os.path.join(DEST, nome))
    json_origem = os.path.join(RAIZ, pasta, prefixo + "-com-legenda.json")
    if os.path.exists(json_origem):
        shutil.copy2(json_origem, os.path.join(DEST, os.path.splitext(nome)[0] + ".json"))
    else:
        print("AVISO: sem JSON para", nome, "(rode gerar_youtube_txt.py antes)")
    txt = open(os.path.join(RAIZ, pasta, "YouTube_Titulo_e_Descricao.txt"), encoding="utf-8-sig").read()
    partes = re.split(r"\r?\n-{70}\r?\n", txt)
    bloco = next(p for p in partes if "com-legenda" in p)
    bloco = re.sub(r"ARQUIVO DO VÍDEO: .*", "ARQUIVO DO VÍDEO: " + nome, bloco)
    bloco = bloco[bloco.index("ARQUIVO DO VÍDEO"):]
    blocos += [bloco.strip(), "", "-" * 70, ""]
    print("ok", nome)
with open(os.path.join(DEST, "_Titulos_e_Descricoes_YouTube.txt"), "w", encoding="utf-8-sig", newline="\r\n") as f:
    f.write("\n".join(blocos))
