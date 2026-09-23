# Dashboard de Agenda

_O que significa cada informação e como conferir cada uma no sistema_

Versão 2.1 — 23/09/2026

O Dashboard de Agenda reúne, num só lugar, números sobre os atendimentos de um período: sessões, pacientes, presença/falta, ocupação da agenda e faturamento por convênio. Este manual explica o que cada card, gráfico e tabela representa, como o número é calculado e, principalmente, como conferir cada valor dentro do sistema — com um exemplo real passo a passo (Setembro/2026).

Vídeo narrado desta rotina: `video-dashboard-agenda-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

## Onde encontrar e o filtro de período

Acesso em Agenda → Dashboard Agenda (perfil administrador). Os filtros são Período - Início e Período - Fim; ao abrir, vêm com o mês corrente, e o botão de borracha volta a esse padrão. O filtro de Profissional existe no sistema, mas não aparece na tela: o Dashboard sempre mostra todos os profissionais juntos.

![Dashboard filtrado para Setembro/2026 (01/09 a 30/09) — os números deste exemplo serão conferidos abaixo.](40-dashboard-setembro-cards.png)

_Dashboard filtrado para Setembro/2026 (01/09 a 30/09) — os números deste exemplo serão conferidos abaixo._

## Atenção: o que o Dashboard conta como "sessão"

> ⚠️ O Dashboard só enxerga sessões que já têm uma data registrada. O sistema só grava essa data quando a sessão é marcada como PRESENTE, AUSENTE, AUSENTE - JUSTIFICATIVA ou REMARCAÇÃO. Por isso: (1) sessões ainda pendentes ("****", sem marcação) não aparecem; (2) PAC. DESMARCOU e PRO. DESMARCOU não aparecem (por isso o gráfico não tem fatias de desmarcação). Em outras palavras, o Dashboard mostra sessões registradas, e não todas as sessões agendadas — a própria tela traz esse aviso e os cards foram renomeados para deixar isso claro.

Exemplo real (Agenda de Setembro/2026): a agenda tem 165 sessões previstas — 150 ainda pendentes, 10 marcadas como Presente e 5 como Ausente. O Dashboard mostra 15 (10 + 5). Os relatórios de Agenda (que contam as sessões previstas) mostram 165.

## Exemplo passo a passo: conferindo Sessões Registradas, Presença e Absenteísmo

Estes números do Dashboard de Setembro: Sessões Registradas = 15, Taxa de Presença = 66,7%, Taxa de Absenteísmo = 33,3%. Para conferir dentro da Agenda:

| Passo | O que fazer |
|---|---|
| 1 | Menu Agenda → na linha do mês (2026 / SETEMBRO) clique em Ver Agenda. |
| 2 | Clique em Filtros. No campo Sessão 1, escolha PRESENTE e clique em Filtrar. Veja no rodapé: "Total de registros: 8". |
| 3 | Repita trocando para Sessão 2 (resultado: 1), Sessão 3 (1), Sessão 4 (0) e Sessão 5 (0). Some: 8 + 1 + 1 = 10 presentes. |
| 4 | Repita tudo com AUSENTE: Sessão 1 = 3, Sessão 2 = 2, demais 0. Soma = 5 ausentes. |
| 5 | Sessões Registradas = 10 + 5 = 15. Taxa de Presença = 10 ÷ 15 = 66,7%. Taxa de Absenteísmo = 5 ÷ 15 = 33,3%. Bate com o Dashboard. |

![Tela Agenda de Setembro/2026 (Ver Agenda): sem filtros mostra 150 linhas de agendamento (cada linha pode ter até 5 sessões).](22-agendamento-grade-mes.png)

_Tela Agenda de Setembro/2026 (Ver Agenda): sem filtros mostra 150 linhas de agendamento (cada linha pode ter até 5 sessões)._

![Filtros → Sessão 1 = PRESENTE.](23a-modal-filtro-sessao1-presente.png)

_Filtros → Sessão 1 = PRESENTE._

![Resultado: "Total de registros: 8" — as linhas cuja Sessão 1 é PRESENTE.](23-agendamento-filtro-sessao1-presente.png)

_Resultado: "Total de registros: 8" — as linhas cuja Sessão 1 é PRESENTE._

> ⚠️ Por que somar as 5 colunas? A grade tem uma linha por agendamento, com até 5 sessões (Sessão 1 a 5). O Dashboard conta cada sessão, então é preciso somar o resultado de cada coluna. Se o período passar de um mês, repita para cada mês (a Agenda é mensal) e some — o Dashboard usa a data da sessão, não o mês da agenda.

## Taxa de Absenteísmo: o que é e como conferir

Absenteísmo é a taxa de faltas: Ausentes ÷ (Presentes + Ausentes) × 100. É o complemento exato da Taxa de Presença (as duas somam 100%). Só entram na conta as sessões marcadas PRESENTE e AUSENTE; AUSENTE - JUSTIFICATIVA, remarcações e desmarcações ficam fora da fórmula.

Como conferir na Agenda: use o passo a passo acima (Filtros → Sessão 1 a 5 = AUSENTE e PRESENTE) e faça a divisão. Exemplo de Setembro: 5 ÷ (10 + 5) = 33,3%.

![Alternativa mais rápida: Relatórios → Agenda - Qtd Marcação (escolha a Agenda 2026/SETEMBRO) traz Presentes e Ausentes por profissional.](24-relatorio-qtd-marcacao.png)

_Alternativa mais rápida: Relatórios → Agenda - Qtd Marcação (escolha a Agenda 2026/SETEMBRO) traz Presentes e Ausentes por profissional._

> ⚠️ Sobre o relatório "Agenda - Qtd Marcação" (atualizado): a linha TOTAL agora soma o mês inteiro, em todas as páginas (Setembro: 165 sessões, 10 presentes, 5 ausentes, 0 ausência justificada), e a coluna Ausência Justificada é separada de Ausente, como no Dashboard. Atenção: "Qtde. Sessões" continua sendo o número de sessões previstas (165), não as registradas (15).

## Os 8 cards do topo — o que são e como conferir

| Card | O que é / como é calculado | Como conferir no sistema |
|---|---|---|
| Sessões Registradas (antes "Total de Sessões") | Quantidade de sessões registradas (com data) no período: Presente, Ausente, Ausente-Justificativa e Remarcação. | Agenda → Ver Agenda → Filtros → somar as colunas Sessão 1 a 5 por status (exemplo acima). |
| Pacientes com Sessão Registrada (antes "Pacientes Atendidos") | Pacientes distintos com ao menos uma sessão registrada no período (inclui quem faltou). | Na Agenda filtrada (Sessão = PRESENTE/AUSENTE), contar os nomes diferentes da coluna Paciente. |
| Taxa de Presença | Presentes ÷ (Presentes + Ausentes) × 100. | Contagens de PRESENTE e AUSENTE na Agenda (exemplo acima). |
| Taxa de Absenteísmo | Ausentes ÷ (Presentes + Ausentes) × 100. | Idem — ver seção anterior. |
| Pacientes Novos | Pacientes cuja primeira sessão registrada de toda a história cai dentro do período. | Relatórios → Histórico do Paciente (aba Agenda). A lista vem do mais recente para o mais antigo: vá até a última página para ver a primeira sessão. |
| Pacientes Recorrentes | Pacientes do período que já tinham sessão registrada antes do início do período. | Mesma consulta acima (primeira sessão anterior ao início do período). |
| Dias de Antecedência (média) | Média de dias entre a data de inclusão do agendamento e a data da sessão. | Não há tela que mostre a data de inclusão do agendamento — hoje só é possível conferir por consulta ao banco. Ver "Relatórios previstos". |
| Taxa de Ocupação | Total de Sessões ÷ Capacidade Total × 100 (o card mostra "15 de 629"). Capacidade = horários configurados para os profissionais no período, descontados os feriados. | Agenda → Prof. horários (escolha o profissional) lista os horários semanais/avulsos configurados. A capacidade é a soma desses horários ao longo dos dias do período. Não há tela que já traga o total. |

![Agenda → Prof. horários (Profissional 01, Setembro/2026): cada linha da tabela é um horário disponível; a capacidade do card soma esses horários pelos dias do período.](42-prof-horarios.png)

_Agenda → Prof. horários (Profissional 01, Setembro/2026): cada linha da tabela é um horário disponível; a capacidade do card soma esses horários pelos dias do período._

> ⚠️ Taxa de Ocupação: como só as sessões registradas entram no numerador, a taxa fica baixa em meses em andamento (2,4% em Setembro, com muitas sessões ainda pendentes). Férias ou bloqueios de um profissional específico não são descontados da capacidade — só feriados cadastrados em Tabelas Aux. → Feriados (isso já aparece no tooltip do card).

## Gráficos

| Gráfico | O que mostra | Como conferir |
|---|---|---|
| Sessões Registradas por Status (pizza) | Presentes, Ausentes, Ausência Justificada e Remarcações. As fatias de Desmarcação foram retiradas: esses status não gravam data e nunca apareciam. | Mesmas contagens da Agenda por status (Filtros → Sessão n). |
| Evolução Diária | Presentes e Ausentes de cada dia do período. | Agenda → Filtros → campo Data (um dia) + Sessão n = PRESENTE/AUSENTE; ou Relatório "Marcação sessão dia" (Agenda → Relatórios). |
| Sessões por Faixa Etária | Sessões por idade do paciente na data da sessão (0–10, 11–20, 21–30, 31–40, 41+). | Sem tela de conferência; usa a data de nascimento do cadastro do paciente. |

![Gráficos de pizza (status) e de linha (evolução diária).](11-graficos.png)

_Gráficos de pizza (status) e de linha (evolução diária)._

## Tabelas do Dashboard

| Tabela | O que mostra | Como conferir |
|---|---|---|
| Por Profissional | Sessões, Presentes e Ausentes de cada profissional. | Agenda → Filtros → Profissionais (marque um) + Sessão n; ou relatório Agenda - Qtd Marcação (uma linha por profissional). |
| Por Especialidade | Sessões registradas por especialidade. | Agenda: a coluna Espec. tem filtro no cabeçalho; combine com Sessão n. |
| Particular x Convênio | Sessões particulares × demais (sem marcação de Particular conta como Convênio). | Agenda → Filtros → Particular (Sim/Não) + Sessão n. |
| Por Operadora | Sessões por convênio/operadora. | Agenda: coluna Plano (filtro no cabeçalho) + Sessão n. |
| Por Método / Por Programa | Só aparecem se a clínica usa Método/Programa; contam sessões que têm essa informação. | Agenda → Filtros → Método (e coluna de programa, se habilitada). |
| Dias e Horários Mais Concorridos | Top 10 de dia da semana + horário com mais sessões registradas. | Agenda: filtros de cabeçalho Dia e Hora (ou Filtros → Dias) + Sessão n. Lembre: o Dashboard conta sessões; a grade conta linhas. |

![Tabelas Por Profissional, Por Especialidade, Particular x Convênio e Por Operadora.](12-tabelas-profissional-especialidade.png)

_Tabelas Por Profissional, Por Especialidade, Particular x Convênio e Por Operadora._

## Faturamento por Convênio: de onde vem e como conferir

> ⚠️ Este é o único quadro que não usa a data da sessão. O período filtra a data do pagamento (baixa) registrado no Financeiro. Uma sessão de um mês pode ser paga em outro.

De onde vem: só entram guias de faturamento (Doc. Faturamento) que já tiveram baixa em Contas a Receber dentro do período. Valor Faturado = valor da guia faturada; Valor Recebido = soma das baixas (valor pago) dessa conta. Guias faturadas sem nenhuma baixa no período não aparecem.

![Quadro Faturamento por Convênio (01/01 a 30/09/2026): Operadora PROPRIO — Faturado R$ 1.223,00 / Recebido R$ 1.373,00.](43-faturamento-corrigido.png)

_Quadro Faturamento por Convênio (01/01 a 30/09/2026): Operadora PROPRIO — Faturado R$ 1.223,00 / Recebido R$ 1.373,00._

Como conferir hoje: (1) Doc. Faturamento → Listar (botão "Listar Últimos" ou "Filtros") mostra as guias: número, paciente, emissão, sessões, status, localização e a coluna Faturamento; (2) Relatórios → Financeiro - Recebimentos (Contas a Receber), com Filtros → Data inicial/final = o período do Dashboard, lista as baixas (data, forma, valor original, valor pago) com o total no rodapé.

No exemplo: aparecem 4 baixas com o nome "PROPRIO" na coluna Paciente. Três delas têm valor original de R$ 1.223,00 (a conta da guia): R$ 1.023,00 + R$ 200,00 + R$ 150,00 = R$ 1.373,00 recebidos, que é o valor do quadro. A quarta (R$ 180,00, valor original R$ 200,00) é de outra conta a receber, que não é de guia, e por isso não entra no quadro.

![Financeiro - Recebimentos com período 01/01 a 30/09/2026: as baixas de "PROPRIO" somam o Valor Recebido do quadro.](32-relatorio-recebimentos-periodo.png)

_Financeiro - Recebimentos com período 01/01 a 30/09/2026: as baixas de "PROPRIO" somam o Valor Recebido do quadro._

> ⚠️ Correção realizada nesta revisão: o quadro estava somando o valor faturado da guia uma vez para cada baixa (uma guia de R$ 1.223,00 com 3 baixas aparecia como R$ 3.669,00). Já corrigido: agora cada guia é contada uma única vez. Conferência por operadora: o relatório Financeiro - Recebimentos agora tem a coluna e o filtro Operadora (pela guia faturada), e o Relatório Guia Faturamento tem a opção Agrupar por Operadora.

## Como ver quais sessões compõem cada número (novo)

Cada número do Dashboard pode ser aberto para mostrar as sessões que o formam. Clique em um dos cards (Sessões Registradas, Pacientes, Taxa de Presença, Taxa de Absenteísmo), em uma linha das tabelas Por Profissional, Por Especialidade ou Por Operadora, ou em Particular / Convênio. Para ver todas as sessões do período, use o botão Ver sessões ao lado de Buscar. A lista usa exatamente o mesmo critério do painel, então o total da lista é sempre igual ao número clicado.

![Ao clicar em Taxa de Presença (Setembro/2026): as 10 sessões presentes, com paciente, profissional, especialidade, operadora, data de inclusão e dias de antecedência.](44-dashboard-drilldown.png)

_Ao clicar em Taxa de Presença (Setembro/2026): as 10 sessões presentes, com paciente, profissional, especialidade, operadora, data de inclusão e dias de antecedência._

## Listas de conferência dos demais cards

Os cards que não são sessões também abrem uma lista, com o mesmo critério do painel: Pacientes Novos e Pacientes Recorrentes (paciente, data da primeira sessão de toda a história e sessões no período), Taxa de Ocupação (cada horário de profissional que compõe a capacidade, com data, dia da semana, profissional, horário e se é fixo ou avulso) e as linhas do quadro Faturamento por Convênio (uma linha por conta a receber, com quantidade de guias, valor faturado e valor recebido no período).

![Pacientes Novos (Setembro/2026): 2 pacientes, cuja primeira sessão de toda a história cai dentro do período.](45-drilldown-novos.png)

_Pacientes Novos (Setembro/2026): 2 pacientes, cuja primeira sessão de toda a história cai dentro do período._

![Taxa de Ocupação: a lista tem 629 linhas, uma para cada horário disponível; esse é o denominador da taxa (15 de 629).](46-drilldown-capacidade.png)

_Taxa de Ocupação: a lista tem 629 linhas, uma para cada horário disponível; esse é o denominador da taxa (15 de 629)._

![Faturamento por Convênio, linha PROPRIO (01/01 a 30/09/2026): conta a receber 61, 1 guia, R$ 1.223,00 faturado e R$ 1.373,00 recebido; confere com o quadro.](47-drilldown-faturamento.png)

_Faturamento por Convênio, linha PROPRIO (01/01 a 30/09/2026): conta a receber 61, 1 guia, R$ 1.223,00 faturado e R$ 1.373,00 recebido; confere com o quadro._

> ⚠️ Como conferir: o número de linhas de cada lista (mostrado no título) deve ser igual ao número do card. Se algum horário da capacidade não deveria contar (por exemplo, um profissional em férias), ele aparece na lista e pode ser identificado ali.

Use o botão Exportar CSV para levar a lista ao Excel. Colunas: Data, Sessão, Paciente, Idade, Profissional, Especialidade, Operadora, Particular, Método, Programa, Status, Data de inclusão e Dias de antecedência. A coluna Dias de antecedência é a que permite conferir o card "Dias de Antecedência (média)".

## Quadro resumo: onde conferir cada informação

| Informação do Dashboard | Onde conferir | Observação |
|---|---|---|
| Sessões Registradas, Presentes, Ausentes, Taxas | Agenda → Ver Agenda → Filtros (Sessão 1 a 5) | Somar as 5 colunas; repetir por mês. |
| Por profissional / status | Relatórios → Agenda - Qtd Marcação | TOTAL do mês inteiro; "Ausência Justificada" em coluna própria. |
| Cards/contagens de um mês | Relatórios → Relatório Agenda (Agenda → botão Relatório) | Mostra Presentes/Ausentes/desmarcações do mês da agenda. |
| Presença de um dia | Relatórios → Presença Diária (por data de marcação) | A data é a do registro da marcação, não a da sessão. |
| Pacientes Novos/Recorrentes | Relatórios → Histórico do Paciente → aba Agenda | Ir à última página para ver a 1ª sessão. |
| Taxa de Ocupação (capacidade) | Agenda → Prof. horários | Somar horários × dias; descontar feriados. |
| Faturamento por Convênio | Doc. Faturamento → Listar + Relatórios → Financeiro - Recebimentos | Sem agrupamento por operadora. |
| Dias de Antecedência | — (sem tela) | Só por consulta ao banco. |
| Faixa etária | — (sem tela) | Idade calculada na data da sessão. |

## Diferenças entre o Dashboard e as telas da Agenda

| Ponto | Dashboard | Telas da Agenda / relatórios |
|---|---|---|
| Período | Intervalo livre de datas (data da sessão). | Um mês de Agenda por vez. |
| O que conta | Sessões com data registrada (Presente, Ausente, Justificada, Remarcação). | Agenda mostra todas as linhas; "Qtd Marcação" conta sessões previstas. |
| Ausente | Só status AUSENTE. | Qtd Marcação separa AUSENTE e Ausência Justificada. |
| Totais | Do período inteiro. | Qtd Marcação: TOTAL do período inteiro. |

> ⚠️ Previsão de melhorias: foi elaborado um plano para criar relatórios que permitam conferir todos os números do Dashboard diretamente (sessões por período, pacientes novos, capacidade e faturamento por convênio), além de decidir se o Dashboard deve passar a contar também as sessões agendadas e desmarcadas. Enquanto isso, use os caminhos acima.
