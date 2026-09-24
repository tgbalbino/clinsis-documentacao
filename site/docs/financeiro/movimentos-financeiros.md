# Movimentos Financeiros

_O que é, de onde vem e para que serve o extrato de cada Conta Financeira_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Movimentos-Financeiros/Documentacao_Movimentos_Financeiros_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/YEE6RAVUX8I?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/YEE6RAVUX8I)

## Conteúdo completo do manual

---


_O que é, de onde vem e para que serve o extrato de cada Conta Financeira_

Versão 1.0 — 22/09/2026

Movimentos Financeiros é o extrato interno do sistema: cada linha é uma entrada ou saída de dinheiro em uma Conta Financeira específica (um banco ou o caixa), com data, valor e origem. A tela serve para conferir esse extrato contra o extrato real do banco (conciliação), fazer transferências entre contas do sistema e, se necessário, excluir um lançamento incorreto.

---

## O que é e de onde vem cada linha

Acesso em Financeiro → Movimentos → Movimentos Financeiros (rota financeiro/movimentos). Cada linha da lista representa um lançamento numa Conta Financeira, gerado automaticamente pelo sistema — nesta tela não existe um botão de "lançamento manual avulso"; as únicas formas de gerar uma linha nova aqui são as baixas do financeiro e a Transferência entre Contas (explicada mais abaixo).


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Baixa de Conta a Pagar | Toda vez que um pagamento é registrado com uma Conta Financeira informada, gera uma linha de Saída. |
| Baixa de Conta a Receber | Todo recebimento registrado com uma Conta Financeira informada gera uma linha de Entrada. |
| Transferência entre Contas | O botão "Nova Transferência" desta própria tela gera duas linhas ao mesmo tempo: uma Saída na conta de origem e uma Entrada na conta de destino. |

> ⚠️ Se uma baixa de Conta a Pagar/Receber for cancelada ou excluída, o sistema remove automaticamente (some da lista) o Movimento Financeiro que ela tinha gerado — não é preciso fazer nada manualmente nesta tela nesse caso.

## Para que serve

É a base para três outras telas do módulo Financeiro: o saldo de cada Conta Financeira, o Fluxo de Caixa e o Dashboard Financeiro são todos calculados a partir dessas mesmas linhas. Na prática, esta tela funciona como o "extrato bancário" de cada conta dentro do sistema, usado para conciliar com o extrato real do banco.

## Filtros

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Período - Início/Fim | Obrigatório; vem com o mês corrente por padrão. |
| Conta Financeira | Filtra só os lançamentos de uma conta. |
| Tipo | Entrada ou Saída. |
| Origem | Conta a Pagar, Conta a Receber ou Transferência. |
| Conciliado | Sim, Não ou Todos. |

## Card "Conciliação"

Mostra três números — Total, Conciliado (verde) e Não Conciliado (vermelho) — e uma barra de progresso, somando o valor de todos os lançamentos do período (e da conta, se filtrada). É recalculado toda vez que "Buscar" é clicado.

## Conciliar / Desconciliar

O botão verde (✓) marca o lançamento como conciliado — ou seja, confirma que aquele valor bate com o extrato real do banco naquele dia. É uma ação de um clique, sem pedir motivo. Um lançamento conciliado ganha o botão amarelo "Desconciliar" (desfazer), caso a conciliação tenha sido feita por engano.


> ⚠️ Um lançamento conciliado não pode ser excluído diretamente — é preciso desconciliar primeiro (o botão vermelho de excluir some da linha assim que ela é conciliada).

## Excluir um lançamento

O botão vermelho (lixeira), disponível só em linhas não conciliadas, pede o Motivo da exclusão antes de confirmar.


> ⚠️ Excluir um lançamento aqui é uma ação isolada: não desfaz a baixa de Conta a Pagar/Receber que o gerou — só remove esta linha específica do extrato. Se o lançamento excluído era referente a uma baixa, o ideal é cancelar a baixa na tela de origem, não excluir por aqui.

## Nova Transferência entre Contas

Usada para registrar uma movimentação interna, como um saque do banco para reforçar o caixa físico, ou um depósito do dinheiro do caixa na conta bancária. Pede Data, Conta de Origem, Conta de Destino (diferentes entre si), Valor, Plano de Contas, Centro de Custo e um Histórico opcional.



> ⚠️ Assim como qualquer outro lançamento financeiro do sistema, a transferência exige um Plano de Contas e um Centro de Custo — são usados para que ela também apareça corretamente classificada nos relatórios de Fluxo de Caixa "Por Plano de Conta" e "Por Centro de Custo".
