# Estorno de Baixas

Como desfazer uma baixa de Contas a Receber ou a Pagar, com motivo e histórico, e como conferir o efeito no dashboard financeiro, nos relatórios e nos movimentos financeiros.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Estorno-de-Baixas/Documentacao_Estorno_de_Baixas_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/Bb6zZYqqztg?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/Bb6zZYqqztg)

## Conteúdo completo do manual

---


_Contas a Receber e Contas a Pagar: como estornar e como conferir no Dashboard e nos relatórios_

Versão 1.0 — 07/10/2026

Estornar uma baixa é cancelar um recebimento ou um pagamento que foi lançado errado (conta errada, valor ou data incorretos, duplicidade, ou pagamento que não aconteceu). O ClinSis não apaga o lançamento: ele fica no histórico, marcado como estornado, com quem estornou, quando e por quê, e o título volta a ficar em aberto com o saldo integral. Este manual mostra o passo a passo nas Contas a Receber e nas Contas a Pagar e como conferir o efeito no Dashboard Financeiro, nos relatórios e nos Movimentos Financeiros.


---

## O exemplo deste manual

Para mostrar o antes e o depois, foram lançadas quatro baixas em dinheiro no mesmo dia, na conta financeira Caixa: dois recebimentos (R$ 400,00 e R$ 250,00) e dois pagamentos (R$ 350,00 e R$ 120,00). Depois foram estornados o recebimento de R$ 400,00 e o pagamento de R$ 350,00; os outros dois ficaram ativos para servir de comparação.

| Baixa | Valor | O que foi feito |
|---|---|---|
| Recebimento — Paciente 0002 | R$ 400,00 | Estornado |
| Recebimento — Paciente 0003 | R$ 250,00 | Mantido |
| Pagamento — Energia elétrica | R$ 350,00 | Estornado |
| Pagamento — Material de limpeza | R$ 120,00 | Mantido |

## Antes do estorno: o que os totais mostram

Com as quatro baixas ativas, o Dashboard Financeiro do mês (Financeiro → Dashboard) mostra Entradas R$ 650,00, Saídas R$ 470,00 e Resultado do Período R$ 180,00. O saldo da conta Caixa é de R$ 180,00.


Os relatórios Recebimentos e Pagamentos (menu Relatórios) listam as mesmas baixas, e Financeiro → Movimentos → Mov. Financeiros mostra um lançamento na conta Caixa para cada baixa.




## Como estornar um recebimento (Contas a Receber)

Acesso em Financeiro → Movimentos → Contas a Receber. Localize o título (situação Baixada) e clique no botão verde de pagamento ($).


Na janela Acertos / Recebimentos, abra a aba Histórico / Estornos. Ela lista todas as baixas do título, ativas e estornadas. Para estornar, clique na lixeira vermelha da linha.


O sistema pede o motivo do cancelamento, que é obrigatório. Os motivos são cadastrados em Tabelas Aux. → Motivo Estorno; no exemplo: Recebimento lançado em conta errada, Valor ou data do recebimento incorretos, Recebimento registrado em duplicidade e Recebimento não realizado.


Depois de confirmar, aparece a mensagem Estornado. A baixa continua no histórico, em vermelho, com a data, o usuário e o motivo do estorno. O Valor Restante do título volta ao valor original, e a lixeira some: uma baixa estornada não pode ser estornada de novo.


Na lista de Contas a Receber o título volta para Aberto, com o saldo integral. Se o lançamento estava errado, basta lançar a baixa correta.


## Como estornar um pagamento (Contas a Pagar)

Acesso em Financeiro → Movimentos → Contas a Pagar. Clique no botão verde de pagamento ($) da conta quitada.


Na janela Pagamento / Acerto da Conta a Pagar, abra a aba Histórico / Estornos. Para estornar, clique no botão vermelho de cancelar (círculo cortado). O botão azul i mostra os detalhes do pagamento.


Escolha o motivo do cancelamento (obrigatório) e clique em Confirmar Cancelamento.


O pagamento passa a aparecer como Cancelado e a janela informa o Total Cancelado.



## Conferência no Dashboard Financeiro

Com o mesmo período, o Dashboard passa a refletir apenas as baixas ativas:

| Indicador | Antes | Depois | Diferença |
|---|---|---|---|
| Entradas | R$ 650,00 | R$ 250,00 | − R$ 400,00 (recebimento estornado) |
| Saídas | R$ 470,00 | R$ 120,00 | − R$ 350,00 (pagamento cancelado) |
| Resultado do Período | R$ 180,00 | R$ 130,00 | Entradas − Saídas |
| Saldo da conta Caixa | R$ 180,00 | R$ 130,00 | Saiu a entrada e voltou a saída |


As tabelas Entradas e Saídas por Plano de Conta e Maiores Pagamentos / Recebimentos por Pessoa também deixam de contar o que foi estornado. O card Recebido em atraso desconta as baixas estornadas.

## Conferência nos relatórios

Os relatórios Recebimentos e Pagamentos têm o filtro Situação:

| Situação | O que lista |
|---|---|
| Todas | Baixas ativas e estornadas. As estornadas ficam com o selo vermelho (Excluída no recebimento, Cancelado no pagamento). |
| Somente ativas | Só as baixas que continuam valendo. |
| Somente excluídas / canceladas | Só as estornadas, para auditoria. |




> ⚠️ Nos dois relatórios, os totais (rodapé e agrupamento Mensal por Forma de Pagamento) consideram somente as baixas ativas. Uma baixa estornada nunca soma, mesmo aparecendo na lista.

## Conferência nos Movimentos Financeiros

O lançamento gerado pela baixa não é apagado do banco de dados: ele é marcado como excluído, com o usuário, a data e o motivo do estorno. Por isso deixa de aparecer em Movimentos Financeiros e não entra mais nos saldos, no Dashboard, no extrato nem na conciliação bancária.


## O que o estorno altera no sistema

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Baixa do recebimento | Marcada como excluída, com usuário, data e motivo. Continua no Histórico / Estornos. |
| Título a receber | Volta para Aberto, com o saldo integral. |
| Baixa do pagamento | Marcada como cancelada, com usuário, data e motivo. Continua no Histórico / Estornos. |
| Conta a pagar | Volta para Aberto, com o saldo integral e o valor pago recalculado. |
| Movimento financeiro | Marcado como excluído, com usuário, data e motivo; sai de saldos, Dashboard e extrato. |
| Caixa | Se a baixa foi feita em um caixa, o estorno registra uma observação nele (quem, quando e o motivo). |

## Regras e bloqueios

| Situação | O que o sistema faz |
|---|---|
| Motivo não informado | Não estorna. O motivo é obrigatório e precisa estar cadastrado para a rotina (Contas a Receber ou Contas a Pagar). |
| Caixa da baixa já fechado | Bloqueia e orienta pedir a um administrador para reabrir o caixa antes de estornar. |
| Cheque já compensado ou cartão com parcela repassada | Bloqueia o estorno direto. Antes é preciso devolver a liquidação financeira (veja o manual de Cheques e Liquidação). |
| Baixa já estornada | Não oferece novo estorno (a lixeira some e o pagamento aparece como Cancelado). |
| Título com baixa ativa | Uma conta a pagar com baixa registrada não pode ser cancelada: estorne primeiro a baixa. |

> ⚠️ Estornar não é excluir: tudo fica registrado para auditoria. Se o lançamento estava errado, estorne e lance a baixa correta em seguida.
