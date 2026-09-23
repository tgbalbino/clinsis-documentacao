# Plano: relatórios para conferir os números do Dashboard de Agenda

Data da análise: 23/09/2026. Base: revisão do Dashboard de Agenda com conferência real contra as
telas existentes (Agenda mensal, relatórios de Agenda, Financeiro) e contra o banco de teste.

## 1. O que a revisão encontrou

### 1.1 Bug corrigido (já commitado na `main` da ApiClinica)
**Faturamento por Convênio repetia o valor faturado a cada baixa.** Uma guia de R$ 1.223,00 com 3
baixas no período aparecia como R$ 3.669,00 (3 × 1.223). O JOIN entre guia e baixas multiplicava o
valor. Agora as baixas são somadas por conta a receber antes de juntar com a guia
(`DashboardAgenda_query.cs`). Resultado validado ao vivo: Faturado R$ 1.223,00 / Recebido R$ 1.373,00.

### 1.2 Divergência de definição — **precisa de decisão do produto**
O Dashboard só enxerga sessões que **têm data gravada** (`DataS1..DataS5`). O sistema só grava essa
data quando a sessão é marcada como **Presente, Ausente, Ausência Justificada ou Remarcação**
(`AgendaProfissionalDiaPacController.SessaoParaAgenda`). Consequências, todas verificadas no banco de teste:

| Situação | Aparece no Dashboard? |
|---|---|
| Sessão marcada Presente / Ausente / Ausência Justificada / Remarcação | Sim |
| Sessão pendente ("****", ainda sem marcação) | **Não** |
| PAC. DESMARCOU / PRO. DESMARCOU | **Não** (fatias "Desmarcado" do gráfico nunca enchem) |

Exemplo real (Agenda de Setembro/2026): 165 sessões previstas = 150 pendentes + 10 presentes + 5
ausentes. O Dashboard mostra **15** (só as 10+5). O relatório "Agenda - Qtd Marcação" mostra 165
(soma de páginas), porque conta as sessões **previstas** por agendamento.

Impactos: "Total de Sessões", "Pacientes Atendidos", "Taxa de Ocupação" (15 de 629 = 2,4%),
tabelas por profissional/especialidade/operadora, faixa etária e dias/horários refletem **sessões
registradas**, não sessões agendadas.

**Opções (escolher uma):**
- **A. Assumir "sessões registradas"** (mais rápido, sem risco): renomear os cards/tooltip
  ("Sessões registradas"), remover as fatias de Desmarcação do gráfico ou marcá-las como
  "não disponível", e documentar. Nenhuma mudança de dados.
- **B. Contar também as sessões previstas**: expandir a agenda semanal em datas (mês da Agenda +
  dia da semana + nº da sessão, respeitando feriados/remarcações) dentro do Dashboard. Correto
  semanticamente, mas é uma reescrita da consulta com risco de divergir da grade da Agenda.
- **C. Gravar a data também nas desmarcações** (mudar `SessaoParaAgenda`): faz as fatias de
  Desmarcação funcionarem, mas altera o dado gravado e pode afetar relatórios que assumem "data =
  sessão ocorrida" (ex.: Cobrança usa `DataS <= hoje` + status).

Recomendação: **A agora** (honestidade dos rótulos) e decidir B/C depois, com o relatório R1 abaixo
já permitindo comparar "previstas × registradas".

### 1.3 Inconsistências entre telas
- "Agenda - Qtd Marcação": a linha **TOTAL soma só a página exibida** (pág. 1 = 123/5/2/116, pág. 2 =
  42/5/3/34; total real 165/10/5/150). E a coluna **AUSENTE inclui Ausência Justificada** (status
  4 e 5), enquanto o Dashboard conta Ausente = só status 4.
- "Financeiro - Recebimentos": não tem coluna nem filtro de Operadora/Convênio.
- "Relatório Guia Faturamento": agrupa só por Situação da guia; sem Operadora.
- Nenhuma tela mostra a data de inclusão do agendamento (necessária p/ "Dias de Antecedência").
- Nenhuma tela lista a capacidade (horários disponíveis) que compõe a "Taxa de Ocupação".

## 2. Relatórios que faltam (proposta)

Princípio: **usar a mesma consulta do Dashboard** (`#Sessoes`, `#PacienteHistorico`, capacidade,
faturamento) como fonte única, para o relatório nunca divergir do card.

| # | Relatório novo | Confronta qual informação | Filtros | Colunas / saída |
|---|---|---|---|---|
| R1 | **Sessões por período** (Agenda → Relatórios) | Total de Sessões, Pacientes Atendidos, Presença/Absenteísmo, Por Profissional/Especialidade/Operadora/Método/Programa, Particular×Convênio, Evolução Diária, Dias/Horários, Faixa Etária, Dias de Antecedência | Período livre (início/fim), profissional, especialidade, operadora, particular, status | Linha a linha: data da sessão, nº da sessão, paciente, idade na data, profissional, especialidade, operadora, particular, método, programa, status, data de inclusão, dias de antecedência. Totais por status. Exportar CSV |
| R2 | **Pacientes novos × recorrentes** | Pacientes Novos / Recorrentes | Período | Paciente, data da 1ª sessão (toda a história), classificação (Novo/Recorrente) |
| R3 | **Capacidade da agenda** | Taxa de Ocupação (capacidade) | Período, profissional | Profissional, dia, horários fixos/avulsos, dias descontados (feriados/inatividade), capacidade total, sessões registradas, % |
| R4 | **Faturamento por Convênio** | Faturamento por Convênio | Período de recebimento, operadora | Operadora, guia, conta a receber, valor faturado, baixas (data/valor), recebido |

**Alternativa que cobre R1–R4 de uma vez (recomendada):** *drill-down nos cards* — clicar num
card/gráfico/tabela do Dashboard abre uma lista com as linhas que compõem aquele número e botão
"Exportar CSV". Garante critério idêntico e evita quatro telas novas. R1–R4 viram as "visões" desse
drill-down.

### Ajustes em relatórios existentes (baratos, fazer junto)
1. Qtd Marcação: TOTAL geral (não por página) e separar "Ausente" de "Ausência Justificada".
2. Recebimentos: coluna e filtro de Operadora (via guia faturada).
3. Guia Faturamento: opção de agrupar por Operadora.

## 3. Ordem sugerida
1. Decidir a opção A/B/C do item 1.2 (bloqueia o texto final dos cards).
2. Ajustes baratos (1–3 acima).
3. Drill-down com R1 (maior valor: cobre 80% das conferências).
4. R4, depois R3 e R2.
5. Atualizar o manual/vídeo do Dashboard de Agenda com as novas telas.

## 4. Estimativa (ordem de grandeza)
- Ajustes baratos: 0,5–1 dia. R1 + drill-down: 2–3 dias. R2/R3/R4: ~1 dia cada.
- Opção B (sessões previstas): 3–5 dias + validação contra a grade; Opção C: 1 dia + análise de impacto.
