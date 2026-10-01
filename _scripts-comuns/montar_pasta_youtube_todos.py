# -*- coding: utf-8 -*-
"""Monta C:\\Projetos\\W_Clinica\\Videos-YouTube com TODOS os vídeos (com legenda) na ordem da lista numerada:
NN_video-...-com-legenda.mp4 + NN_...-miniatura.jpg + _videos_youtube.json (título e descrição de cada um) + _Titulos_e_Descricoes_YouTube.txt.
O conteúdo anterior da pasta vai para _anteriores-<data> (para não misturar numerações).
Uso: python montar_pasta_youtube_todos.py <AAAA-MM-DD>
Antes: gerar_youtube_txt.py (YouTube_Titulo_e_Descricao.txt em cada rotina) e gerar_lista_numerada.py (ORDEM)."""
import glob
import json
import os
import re
import shutil
import sys

RAIZ = r"C:\Projetos\W_Clinica\Documentacao-Entrega"
DEST = r"C:\Projetos\W_Clinica\Videos-YouTube"
DATA = sys.argv[1] if len(sys.argv) > 1 else "lote"
AQUI = os.path.dirname(os.path.abspath(__file__))

# ordem e títulos vêm da lista numerada
src = open(os.path.join(AQUI, "gerar_lista_numerada.py"), encoding="utf-8").read()
ORDEM = eval(re.search(r"ORDEM = (\[.*?\n\])", src, re.S).group(1))

CATEGORIA = {
    "Manual-Base-ClinSis": "PRIMEIROS PASSOS", "Area-do-Profissional": "PRIMEIROS PASSOS",
    "Cadastro-Plano-de-Contas": "FINANCEIRO", "Cadastro-Centro-de-Custo": "FINANCEIRO", "Conta-Financeira": "FINANCEIRO",
    "Modulo-de-Caixa": "FINANCEIRO", "Contas-a-Receber": "FINANCEIRO", "Contas-a-Pagar": "FINANCEIRO",
    "Contas-Recorrentes": "FINANCEIRO", "Movimentos-Financeiros": "FINANCEIRO", "Conciliacao-Bancaria-OFX": "FINANCEIRO",
    "Cadastro-de-Especialidades": "CADASTROS", "Cadastro-de-Servicos": "CADASTROS",
    "Tabela-de-Precos-Cobranca": "CADASTROS", "Tabela-de-Precos-Pagamento": "CADASTROS",
    "Prontuario-Configuracao": "PRONTUÁRIO", "Prontuario-Uso": "PRONTUÁRIO", "Prontuario-Auditoria": "PRONTUÁRIO",
    "Layout-de-Contrato": "CONTRATOS", "Contrato": "CONTRATOS", "Contrato-D4Sign": "CONTRATOS",
    "Checkin": "ATENDIMENTO", "WhatsApp": "AGENDA E ATENDIMENTO",
    "Cobranca-de-Paciente": "COBRANÇA E PAGAMENTO", "Pagamento-de-Profissionais": "COBRANÇA E PAGAMENTO",
    "Previsao-de-Faturamento": "COBRANÇA E PAGAMENTO",
    "Dashboard-de-Agenda": "PAINÉIS", "Dashboard-Financeiro-e-Fluxo-Caixa": "PAINÉIS",
}
CURTO = {  # títulos curtos para a miniatura
    "Manual-Base-ClinSis": "Manual Base do ClinSis", "Cadastro-Plano-de-Contas": "Plano de Contas",
    "Cadastro-Centro-de-Custo": "Centro de Custo", "Conta-Financeira": "Conta Financeira",
    "Cadastro-de-Especialidades": "Especialidades", "Cadastro-de-Servicos": "Serviços",
    "Tabela-de-Precos-Cobranca": "Tabela de Valores: Cobrança", "Tabela-de-Precos-Pagamento": "Tabela de Valores: Pagamento",
    "Prontuario-Configuracao": "Prontuário: Configuração", "Layout-de-Contrato": "Layout de Contrato",
    "Modulo-de-Caixa": "Módulo de Caixa", "Contas-a-Receber": "Contas a Receber", "Contas-a-Pagar": "Contas a Pagar",
    "Contas-Recorrentes": "Contas Recorrentes", "Movimentos-Financeiros": "Movimentos Financeiros",
    "Conciliacao-Bancaria-OFX": "Conciliação Bancária (OFX)", "Checkin": "Checkin de Paciente",
    "WhatsApp": "WhatsApp: lembretes e confirmações", "Prontuario-Uso": "Prontuário: Uso pelo Profissional",
    "Contrato": "Contrato", "Contrato-D4Sign": "Contrato com Assinatura Digital", "Cobranca-de-Paciente": "Cobrança de Paciente",
    "Pagamento-de-Profissionais": "Pagamento de Profissionais", "Previsao-de-Faturamento": "Previsão de Faturamento",
    "Dashboard-de-Agenda": "Dashboard de Agenda", "Prontuario-Auditoria": "Prontuário: Auditoria",
    "Dashboard-Financeiro-e-Fluxo-Caixa": "Dashboard Financeiro e Fluxo de Caixa", "Area-do-Profissional": "Área do Profissional",
}


def video_com_legenda(pasta):
    c = [f for f in glob.glob(os.path.join(RAIZ, pasta, "video-*-com-legenda.mp4")) if "conteudo" not in f]
    assert len(c) == 1, (pasta, c)
    return c[0]


# 1) guarda o que havia
os.makedirs(DEST, exist_ok=True)
ant = os.path.join(DEST, f"_anteriores-{DATA}")
if not os.path.exists(ant):
    antigos = [f for f in os.listdir(DEST) if not f.startswith("_anteriores") and f not in ("enviados", "Backup")]  # enviados/Backup são do usuário
    if antigos:
        os.makedirs(ant)
        for f in antigos:
            shutil.move(os.path.join(DEST, f), os.path.join(ant, f))
        print("movidos para", ant, len(antigos))

# 2) miniaturas (reaproveita gerar_miniaturas.py com a nova lista)
itens = []
for n, (pasta, _titulo, _s) in enumerate(ORDEM, 1):
    prefixo = os.path.basename(video_com_legenda(pasta))[:-len("-com-legenda.mp4")]
    itens.append((n, prefixo, pasta, CURTO[pasta], CATEGORIA[pasta]))
fonte = open(os.path.join(AQUI, "gerar_miniaturas.py"), encoding="utf-8").read()
fonte = re.sub(r"ITENS = \[.*?\n\]\n", "ITENS = " + repr(itens) + "\n", fonte, flags=re.S)
exec(compile(fonte, "gerar_miniaturas", "exec"), {"__name__": "__main__"})

# 3) vídeos + json + txt
lista_json, blocos = [], ["TÍTULOS E DESCRIÇÕES — vídeos com legenda, ordem numerada (" + DATA + ")", "=" * 70, ""]
for n, prefixo, pasta, _c, _cat in itens:
    nome = f"{n:02d}_{prefixo}-com-legenda.mp4"
    shutil.copy2(video_com_legenda(pasta), os.path.join(DEST, nome))
    txt = open(os.path.join(RAIZ, pasta, "YouTube_Titulo_e_Descricao.txt"), encoding="utf-8-sig").read()
    partes = re.split(r"\r?\n-{70}\r?\n", txt)
    bloco = next(p for p in partes if "com-legenda" in p)
    titulo = re.search(r"TÍTULO:\s*\r?\n(.+)", bloco).group(1).strip()
    descricao = re.search(r"DESCRIÇÃO:\s*\r?\n(.*)", bloco, re.S).group(1).strip()
    descricao = re.sub(r"\s*Assista ao vídeo narrado desta rotina.*?(?=\n\n|$)", "", descricao, flags=re.S)
    descricao = re.sub(r"\s+#+\s[^\n]*?\.\.\.(?=\n)", "", descricao)  # tira restos de markdown ('# 1. Título ...') do resumo
    lista_json.append({
        "numero": n, "arquivo": nome, "miniatura": f"{n:02d}_{prefixo}-miniatura.jpg",
        "titulo": titulo, "descricao": descricao, "pasta_origem": pasta, "privacidade_sugerida": "nao_listado",
    })
    with open(os.path.join(DEST, nome[:-4] + ".json"), "w", encoding="utf-8") as fj:  # texto de upload ao lado do vídeo
        json.dump({"titulo": titulo, "descricao": descricao, "tags": ["ClinSis", "Gestão de Clínicas", "Tutorial"]}, fj, ensure_ascii=False, indent=2)
    blocos += [f"{n:02d}. ARQUIVO DO VÍDEO: {nome}", "", "TÍTULO:", titulo, "", "DESCRIÇÃO:", descricao, "", "-" * 70, ""]
    print("ok", nome)
with open(os.path.join(DEST, "_videos_youtube.json"), "w", encoding="utf-8") as f:
    json.dump(lista_json, f, ensure_ascii=False, indent=2)
with open(os.path.join(DEST, "_Titulos_e_Descricoes_YouTube.txt"), "w", encoding="utf-8-sig", newline="\r\n") as f:
    f.write("\n".join(blocos))
