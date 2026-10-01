# Dashboard Financeiro e Fluxo de Caixa

_O que é cada informação exibida na tela e de onde ela vem no sistema_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Dashboard-Financeiro-e-Fluxo-Caixa/Documentacao_Dashboard_Financeiro_e_Fluxo_de_Caixa_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/WCa8gVOdXKE?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/WCa8gVOdXKE)

## Conteúdo completo do manual

---


_O que é cada informação exibida na tela e de onde ela vem no sistema_

Versão 1.1 — 29/09/2026

O Dashboard Financeiro resume, num período escolhido, o que entrou, o que saiu, o saldo de cada conta e os maiores pagamentos e recebimentos. O Fluxo de Caixa mostra a movimentação dia a dia (ou por semana/mês) e ainda projeta o saldo futuro a partir das contas a pagar e a receber em aberto. Este documento explica cada campo das duas telas.


---

## 1. Dashboard Financeiro

Acesso em Financeiro → Dashboard. Mostra um resumo financeiro da clínica dentro do período escolhido, com opção de restringir por Conta Financeira, Centro de Custo e Plano de Conta.

## Filtros e botões do topo

Período - Início / Período - Fim definem o intervalo (com base na data do movimento financeiro). Conta Financeira, Centro de Custo e Plano de Conta são opcionais: "Todas"/"Todos" traz tudo. O botão azul Buscar carrega os dados e o botão só com o ícone de borracha Limpa os filtros. No celular, os filtros ficam recolhidos numa barra com o resumo do período e a quantidade de filtros aplicados; toque nela para abrir.


## Indicadores do topo (caixas coloridas)


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Entradas (caixa verde) | Soma de todos os lançamentos de entrada do período, dentro do filtro de conta, centro de custo e plano de conta escolhidos. |
| Saídas (caixa vermelha) | Igual ao anterior, somando os lançamentos de saída. |
| Resultado do Período (caixa azul) | Entradas − Saídas do período (cálculo simples, feito na própria tela). |
| Saldo das Contas (caixa amarela) | Soma do saldo atual de cada Conta Financeira ativa. É o saldo acumulado de toda a história da conta e não fica restrito ao período do filtro. |
| Juros Recebido | Soma dos juros registrados nas baixas de Contas a Receber cuja data de pagamento caiu no período. |
| Desconto Concedido | Soma do desconto dado ao paciente nas baixas de Contas a Receber no período. |
| Juros Pago | Soma dos juros pagos nas baixas de Contas a Pagar no período (por atraso). |
| Desconto Obtido | Soma do desconto conseguido nas baixas de Contas a Pagar no período. |

## Tabelas do meio da tela

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Saldo por Conta Financeira | Uma linha para cada Conta Financeira ativa, com o saldo acumulado desde o início (entradas menos saídas), sem depender do período. Fica em vermelho quando o saldo é negativo. |
| Entradas por Plano de Conta | Soma das entradas do período agrupadas pelo Plano de Conta de cada lançamento. Sem plano, aparece como "Sem plano de conta". |
| Saídas por Plano de Conta | Mesma lógica, somando as saídas do período por Plano de Conta. |

## Rankings e comparativo mensal

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Maiores Pagamentos por Pessoa | Para cada pessoa (fornecedor/prestador), soma o valor pago mais os juros pagos nas baixas de Contas a Pagar do período, do maior para o menor. |
| Maiores Recebimentos por Pessoa | Igual, para Contas a Receber: valor recebido mais juros, do maior para o menor. |
| Comparativo Mensal — Entradas/Saídas/Resultado | Compara o mês informado com o imediatamente anterior, com a mesma lógica de Entradas/Saídas do topo, sem os filtros de conta, centro de custo e plano. |
| Comparativo Mensal — Variação | (atual − anterior) ÷ anterior × 100. Verde quando positiva ou zero, vermelha quando negativa; fica "-" quando o mês anterior não teve valor. |

## 2. Fluxo de Caixa

Acesso em Financeiro → Fluxo de Caixa. Mostra a movimentação dia a dia (ou agrupada por semana/mês) dentro de um período, separando o que já aconteceu ("Realizado") do que está previsto ("Projetado", a partir das contas a pagar e a receber ainda em aberto).

## Filtros

Além do período, conta, centro de custo e plano de conta (iguais aos do Dashboard), a tela tem Mostrar (Realizado + Projetado, Somente Realizado ou Somente Projetado) e, com "Somente Realizado", o campo Agrupamento (Dia, Semana ou Mês). O botão Buscar carrega os dados e o botão de borracha limpa os filtros.

> ⚠️ O intervalo entre a data de início e a de fim não pode passar de 2 anos no Fluxo de Caixa; períodos maiores são recusados e a tela não atualiza. Escolha um período menor.



| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Saldo Inicial | Saldo acumulado de todos os movimentos registrados antes da data de início do filtro: quanto já existia em caixa na véspera do período. |
| Entradas / Saídas | Soma das entradas e saídas dentro do período filtrado (mesma lógica do Dashboard). |
| Resultado | Entradas − Saídas do período. |
| Saldo Final | Saldo Inicial + Resultado: o saldo em caixa no último dia do período. |

## Bloco "Fluxo de Caixa Projetado" (previsão)

Aparece quando "Mostrar" inclui "Projetado".

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Saldo Atual | Saldo de todos os movimentos financeiros já registrados até hoje (histórico completo): o ponto de partida da projeção. |
| Recebimentos Previstos | Soma do saldo em aberto das Contas a Receber com vencimento antes da data de fim do filtro. |
| Pagamentos Previstos | Soma do saldo em aberto das Contas a Pagar não canceladas com vencimento antes da data de fim do filtro. |
| Saldo Projetado | Saldo Atual + Recebimentos Previstos − Pagamentos Previstos: estimativa do que vai sobrar em caixa na data de fim, se tudo for recebido/pago como previsto. |

## Gráfico e tabela por período

O gráfico Saldo acumulado desenha a evolução da coluna "Saldo Acumulado" da tabela logo abaixo.

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Período | Cada linha é um dia (ou semana/mês, conforme o Agrupamento) dentro do intervalo filtrado. |
| Entradas / Saídas da linha | Soma das entradas e saídas daquele dia, semana ou mês. |
| Resultado da linha | Entradas − Saídas daquele período; vermelho quando negativo. |
| Saldo Acumulado | Saldo Inicial somado, linha a linha, ao Resultado de cada período; vermelho quando negativo. |

## Por Conta Financeira e Por Centro de Custo

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Por Conta Financeira | Para cada Conta Financeira ativa, soma as entradas e saídas do período e calcula o Resultado. A linha Total soma todas as contas. |
| Por Centro de Custo | Mesma lógica por Centro de Custo (sem centro aparece como "Sem centro de custo"), ordenado pelo resultado, do maior para o menor. |

## Exemplo com Agrupamento = Mês

Com "Somente Realizado" e Agrupamento "Mês", a tabela passa a ter uma linha por mês em vez de uma por dia, mais fácil de ler em períodos longos.


## Pontos de atenção

> ⚠️ Todos os valores em dinheiro aparecem no formato R$ 0.000,00 e saldos ou resultados negativos ficam em vermelho. Nos indicadores: verde = entradas, vermelho = saídas, azul = resultado, amarelo = saldo e cinza = informações auxiliares (juros, desconto e saldo inicial).

> ⚠️ O indicador "Saldo das Contas" e a tabela "Saldo por Conta Financeira" mostram sempre o saldo acumulado de toda a história da conta, independentemente do período escolhido; já Entradas, Saídas e Resultado respeitam o período.
