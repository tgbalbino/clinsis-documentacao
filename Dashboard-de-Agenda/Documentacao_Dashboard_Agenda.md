# Dashboard de Agenda

_O que significa cada informação da tela e como conferir cada uma no sistema_

Versão 1.0 — 22/09/2026

O Dashboard de Agenda reúne, num só lugar, os principais números sobre os atendimentos agendados num período: quantas sessões aconteceram, quantos pacientes foram atendidos, taxas de presença/falta, ocupação da agenda e outros recortes (por profissional, especialidade, convênio, faixa etária, etc.). Este manual explica o que cada card, gráfico e tabela representa e, principalmente, como o número é calculado — para que qualquer valor exibido possa ser conferido manualmente se necessário.

Vídeo narrado desta rotina: `video-dashboard-agenda-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

## Onde encontrar e o filtro de período

Acesso em Agenda → Dashboard Agenda (restrito ao perfil administrador). Os únicos filtros da tela são Período - Início e Período - Fim; ao abrir a tela, eles já vêm preenchidos com o mês corrente (do dia 1 ao último dia do mês), e o botão "Limpar" (ícone de borracha) volta a esse padrão.

![Filtros de período e os 8 cards de resumo no topo da tela.](10-topo-cards.png)

_Filtros de período e os 8 cards de resumo no topo da tela._

> ⚠️ Existe um filtro de Profissional já implementado no backend, mas ele não aparece na tela hoje — na prática, o Dashboard sempre mostra todos os profissionais juntos, sem opção de filtrar por um profissional específico.

Praticamente todos os blocos da tela contam sessões dentro do período — e "sessão" aqui é cada data de atendimento agendada (um agendamento recorrente de segunda e quarta, por exemplo, gera uma sessão para cada dia). A única exceção é o quadro "Faturamento por Convênio", explicado ao final, que usa outra data.

## Os 8 cards do topo

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Total de Sessões | Quantidade de sessões agendadas no período, com qualquer status (inclui as que ainda nem aconteceram, faltas e desmarcações). | Contagem de sessões no período |
| Pacientes Atendidos | Quantidade de pacientes distintos que têm ao menos uma sessão no período. O nome pode sugerir "que compareceram", mas conta qualquer status, inclusive falta e desmarcação. | Pacientes distintos com sessão no período |
| Taxa de Presença | Presentes ÷ (Presentes + Ausentes) × 100. Só compara quem esteve presente com quem faltou puro — não entra no cálculo quem desmarcou, teve ausência justificada ou está sem status. | Presentes / (Presentes + Ausentes) |
| Taxa de Absenteísmo | Ausentes ÷ (Presentes + Ausentes) × 100 — é o espelho exato da Taxa de Presença (as duas somam 100%). Mesma ressalva: ignora desmarcações e ausência justificada. | Ausentes / (Presentes + Ausentes) |
| Pacientes Novos | Entre os pacientes atendidos no período, quantos tiveram a primeira sessão de toda a história deles na clínica dentro desse período. | Primeira sessão do paciente cai dentro do período |
| Pacientes Recorrentes | O restante dos pacientes atendidos: já tinham ao menos uma sessão antes do início do período filtrado. | Primeira sessão do paciente é anterior ao período |
| Dias de Antecedência (média) | Média de quantos dias antes da sessão o agendamento foi cadastrado no sistema (data do agendamento menos data de inclusão do registro). | Média de (Data da Sessão − Data de Cadastro) |
| Taxa de Ocupação | Total de Sessões ÷ Capacidade Total da agenda × 100. O número entre parênteses no card mostra as duas partes da conta (ex.: "70 de 2319"). | Total de Sessões / Capacidade Total |

> ⚠️ Taxa de Ocupação tem um ícone de informação (ⓘ) com a explicação completa direto na tela: a "capacidade" soma todos os horários fixos e avulsos configurados na Agenda de cada profissional no período, já descontando os feriados cadastrados em Tabelas Aux. → Feriados. Férias ou bloqueios individuais de um profissional específico ainda não são descontados dessa capacidade — então, se algum profissional tirou férias no período, a taxa de ocupação real fica um pouco menor do que a exibida (o denominador conta uma capacidade maior do que a disponível de fato).

## Gráfico "Presença x Ausência x Desmarcações"

Pizza com todas as sessões do período divididas pelo status: Presentes, Ausentes, Ausência Justificada, Desmarcado Paciente, Desmarcado Profissional e Remarcações.

![Gráfico de pizza (status das sessões) e gráfico de linha (evolução diária) lado a lado.](11-graficos.png)

_Gráfico de pizza (status das sessões) e gráfico de linha (evolução diária) lado a lado._

> ⚠️ Sessões sem nenhum status definido ("em aberto", ainda não marcadas como presente/falta) não aparecem em nenhuma fatia desse gráfico nem em nenhum outro card — elas só entram no card "Total de Sessões". Se o total de sessões for maior que a soma de todas as fatias, é porque existem sessões sem status no período.

## Gráfico "Evolução Diária"

Duas linhas — Presentes e Ausentes — mostrando, dia a dia dentro do período, quantas sessões tiveram cada um desses dois status. As demais categorias (desmarcação, ausência justificada) não entram nesse gráfico, só no de pizza acima.

## Tabelas "Por Profissional", "Por Especialidade" e "Particular x Convênio"

![Tabelas "Por Profissional" (sessões/presentes/ausentes), "Por Especialidade" e "Particular x Convênio"/"Por Operadora".](12-tabelas-profissional-especialidade.png)

_Tabelas "Por Profissional" (sessões/presentes/ausentes), "Por Especialidade" e "Particular x Convênio"/"Por Operadora"._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Por Profissional | Sessões, Presentes e Ausentes de cada profissional no período, ordenado do maior para o menor número de sessões. | Agrupado por profissional |
| Por Especialidade | Total de sessões de cada especialidade no período. | Agrupado por especialidade da agenda |
| Particular x Convênio | Quantas sessões foram marcadas como Particular e quantas como Convênio. | Campo "Particular" da agenda |
| Por Operadora | Total de sessões de cada operadora/convênio. | Agrupado por operadora da agenda |

> ⚠️ A coluna "Desmarcações" que aparece em outras telas do sistema, quando existir aqui, soma Desmarcado Paciente + Desmarcado Profissional num único número (não separa quem desmarcou). Já no card "Particular x Convênio": uma sessão sem essa marcação preenchida é contabilizada como Convênio, não fica de fora da conta.

## "Por Método" e "Por Programa"

![Tabelas "Por Método" e "Por Programa" — só aparecem se a clínica tiver essas opções habilitadas.](13-metodo-programa.png)

_Tabelas "Por Método" e "Por Programa" — só aparecem se a clínica tiver essas opções habilitadas._

Esses dois quadros só aparecem se a clínica tiver, no cadastro dela, a exibição de Método e/ou de Programa da Agenda habilitada. Contam sessões que têm um Método/Programa definido — sessões sem essa informação preenchida não entram na lista, mesmo que o quadro esteja visível.

## Gráfico "Sessões por Faixa Etária"

Sessões agrupadas pela idade do paciente na data de cada sessão (não a idade atual dele), em faixas de 0–10, 11–20, 21–30, 31–40 e 41 anos ou mais. Por isso, um mesmo paciente pode contribuir para faixas diferentes se tiver sessões espalhadas por datas distantes (ex.: fazendo aniversário de faixa no meio do período analisado).

![Gráfico de barras por faixa etária e tabela "Dias e Horários Mais Concorridos".](14-faixa-etaria-dias-horarios.png)

_Gráfico de barras por faixa etária e tabela "Dias e Horários Mais Concorridos"._

## Tabela "Dias e Horários Mais Concorridos"

Mostra as combinações de dia da semana + horário com mais sessões marcadas no período — útil para identificar os horários de pico da agenda. A tela exibe apenas o Top 10; existem mais combinações calculadas por trás, mas só as 10 primeiras (por quantidade de sessões) são mostradas.

## Tabela "Faturamento por Convênio"

![Faturamento por Convênio: valor faturado e valor recebido, por operadora.](15-faturamento-convenio.png)

_Faturamento por Convênio: valor faturado e valor recebido, por operadora._

> ⚠️ Esta é a única tabela da tela que NÃO usa a data da sessão. O próprio título traz o aviso "(por data de recebimento, não por data da sessão)": o período do filtro aqui passa a valer sobre a data em que a baixa do pagamento da guia foi registrada no Financeiro. Uma sessão atendida em um mês pode ter sua guia recebida (e portanto contabilizada aqui) só em outro mês.

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Valor Faturado | Soma do valor das guias de faturamento cujo recebimento caiu dentro do período filtrado. | Guias com baixa no período |
| Valor Recebido | Soma do valor efetivamente pago (baixado) dessas guias no período. | Baixas de Conta a Receber no período |

> ⚠️ Guias já faturadas mas que ainda não tiveram nenhuma baixa de recebimento não aparecem nessa lista — o quadro mostra só o que já foi efetivamente recebido no período.
