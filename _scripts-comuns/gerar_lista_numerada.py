# -*- coding: utf-8 -*-
"""Gera a lista numerada (ordem sugerida de treinamento) dos vídeos de documentação, com o link do YouTube.
Saída: C:\\Projetos\\W_Clinica\\Videos-YouTube\\_Lista_Numerada_dos_Videos.txt
Os links vêm de site/scripts/gerar_site_docs.py (YOUTUBE_LINKS)."""
import re

RAIZ = r"C:\Projetos\W_Clinica\Documentacao-Entrega"
SAIDA = r"C:\Projetos\W_Clinica\Videos-YouTube\_Lista_Numerada_dos_Videos.txt"

fonte = open(RAIZ + r"\site\scripts\gerar_site_docs.py", encoding="utf-8").read()
bloco = fonte[fonte.index("YOUTUBE_LINKS = {"):]
bloco = bloco[:bloco.index("\n}\n")]
LINKS = dict(re.findall(r'"([^"]+)": "(https://youtu\.be/[^"]+)"', bloco))

# (pasta, título, situação)  situação: N = vídeo novo (subido em 01/10), A = link do vídeo anterior (novo de 29/09 ainda não subido), V = vigente
ORDEM = [
    ("Manual-Base-ClinSis", "Manual Base do ClinSis", "N"),
    ("Cadastro-Plano-de-Contas", "Cadastro de Plano de Contas", "A"),
    ("Cadastro-Centro-de-Custo", "Cadastro de Centro de Custo", "A"),
    ("Conta-Financeira", "Cadastro de Conta Financeira", "A"),
    ("Cadastro-de-Especialidades", "Cadastro de Especialidades", "A"),
    ("Cadastro-de-Servicos", "Cadastro de Serviços", "N"),
    ("Tabela-de-Precos-Cobranca", "Tabela de Valores para Cobrança", "N"),
    ("Tabela-de-Precos-Pagamento", "Tabela de Valores para Pagamento", "N"),
    ("Prontuario-Configuracao", "Prontuário - Configuração (Tipos, Alíneas e Textos padrão)", "V"),
    ("Layout-de-Contrato", "Layout de Contrato", "V"),
    ("Modulo-de-Caixa", "Módulo de Caixa", "A"),
    ("Contas-a-Receber", "Contas a Receber", "A"),
    ("Contas-a-Pagar", "Contas a Pagar", "A"),
    ("Contas-Recorrentes", "Contas Recorrentes", "A"),
    ("Movimentos-Financeiros", "Movimentos Financeiros", "N"),
    ("Conciliacao-Bancaria-OFX", "Conciliação Bancária (OFX)", "N"),
    ("Checkin", "Checkin de Paciente", "N"),
    ("WhatsApp", "WhatsApp - lembretes e confirmações", "N"),
    ("Prontuario-Uso", "Prontuário - Uso pelo Profissional", "V"),
    ("Contrato", "Contrato (sem assinatura digital)", "A"),
    ("Contrato-D4Sign", "Contrato com Assinatura Digital (D4Sign)", "A"),
    ("Cobranca-de-Paciente", "Cobrança de Paciente", "V"),
    ("Pagamento-de-Profissionais", "Pagamento de Profissionais", "A"),
    ("Previsao-de-Faturamento", "Previsão de Faturamento da Agenda", "S"),
    ("Dashboard-de-Agenda", "Dashboard de Agenda", "N"),
    ("Prontuario-Auditoria", "Prontuário - Auditoria e Relatórios", "V"),
    ("Dashboard-Financeiro-e-Fluxo-Caixa", "Dashboard Financeiro e Fluxo de Caixa", "A"),
    ("Area-do-Profissional", "Área do Profissional", "N"),
]
ROTULO = {
    "N": "vídeo novo, já no YouTube",
    "A": "link do vídeo ANTERIOR; o vídeo refeito em 29/09 ainda não foi subido",
    "V": "vídeo vigente (sem alterações)",
    "S": "ainda sem link do YouTube",
}

linhas = [
    "ClinSis | Vídeos de documentação - lista numerada na ordem sugerida de treinamento",
    "Atualizada em 01/10/2026. Do mais básico para os que dependem deles.",
    "=" * 78, "",
]
for n, (pasta, titulo, sit) in enumerate(ORDEM, 1):
    url = LINKS.get(pasta, "(sem link)")
    linhas.append(f"{n:02d}. {titulo}")
    linhas.append(f"    {url}")
    linhas.append(f"    [{ROTULO[sit]}]")
    linhas.append("")
linhas.append("-" * 78)
linhas.append("Resumo: %d vídeos novos já no YouTube; %d com vídeo refeito ainda por subir; %d vigentes; %d sem link."
              % tuple(sum(1 for o in ORDEM if o[2] == s) for s in "NAVS"))
with open(SAIDA, "w", encoding="utf-8-sig", newline="\r\n") as f:
    f.write("\n".join(linhas) + "\n")
print(SAIDA, len(ORDEM))
