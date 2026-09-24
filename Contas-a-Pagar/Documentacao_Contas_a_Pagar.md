# Contas a Pagar

_Cadastrar e pagar as contas da clínica, com indicadores de vencimento_

Versão 1.0 — 17/09/2026

Contas a Pagar é onde ficam todas as despesas da clínica: as lançadas manualmente aqui e também as que chegam automaticamente de outras rotinas, como Contas Recorrentes e Pagamento de Profissionais. A partir dela dá pra acompanhar o que está em aberto, vencido, vencendo hoje ou a vencer, e lançar os pagamentos (baixas) de cada conta. Assim como as demais telas financeiras, exige Plano de Conta e Centro de Custo já cadastrados.

Assista ao vídeo narrado desta rotina: [https://youtu.be/dlllj9on1gQ](https://youtu.be/dlllj9on1gQ)
---

## Indicadores do topo

Cinco caixas resumem a situação das contas: Em Aberto (soma de tudo que ainda não foi pago), Vencido (em aberto com vencimento no passado), Vence Hoje, A Vencer (em aberto com vencimento futuro) e Pago no Mês (soma do que já foi baixado no mês atual).

![Tela inicial de Contas a Pagar, com indicadores e a lista de contas.](00-lista-inicial.png)

_Tela inicial de Contas a Pagar, com indicadores e a lista de contas._

## Cadastrando uma conta a pagar (exemplo)

Clique em Novo. No exemplo abaixo, lançamos uma compra de material de escritório de R$ 350,00, tipo documento Boleto, vencendo hoje.

![Cadastro de exemplo: Favorecido, Plano de Contas, Centro de Custo, Descrição, Valor e datas preenchidos.](01-novo-modal-preenchido.png)

_Cadastro de exemplo: Favorecido, Plano de Contas, Centro de Custo, Descrição, Valor e datas preenchidos._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Favorecido (Pessoa) | Para quem a clínica está pagando (fornecedor, prestador, profissional). | Obrigatório |
| Plano de Contas | Categoria da despesa (ex.: Material de Consumo). Precisa estar cadastrado antes. | Obrigatório |
| Centro de Custo | Setor da clínica responsável pela despesa. Precisa estar cadastrado antes. | Obrigatório |
| Valor Original | Valor total da conta antes de qualquer pagamento parcial. | Obrigatório |
| Tipo Documento | Boleto, Nota Fiscal, Contrato ou Pag. Profissional — este último é o tipo usado quando a conta vem da rotina de Pagamento de Profissionais. | Obrigatório |
| Competência (MM/AAAA) | Mês/ano de referência da despesa (pode ser diferente do mês do vencimento). | Obrigatório |
| Data Vencimento | Data limite para pagamento sem juros/atraso. | Obrigatório |

![Depois de salvar, a nova conta aparece na lista, com Situação "1 - Aberto".](02-apos-salvar.png)

_Depois de salvar, a nova conta aparece na lista, com Situação "1 - Aberto"._

## Pagando (baixando) uma conta

O botão verde com o cifrão ($), na linha da conta, abre a tela de Pagamento / Acerto. É possível lançar mais de um pagamento para a mesma conta (pagamentos parciais) até o saldo chegar a zero.

![Pagamento preenchido: Valor Pago, Forma de Pagamento (Cartão de Crédito) e Conta Financeira (Banco Brasil).](03-pagamento-preenchido.png)

_Pagamento preenchido: Valor Pago, Forma de Pagamento (Cartão de Crédito) e Conta Financeira (Banco Brasil)._

![Depois de clicar em Lançar: o pagamento aparece na tabela "Acertos / Pagamentos da Conta", com opção de ver Detalhes ou Cancelar o acerto.](04-apos-lancar-pagamento.png)

_Depois de clicar em Lançar: o pagamento aparece na tabela "Acertos / Pagamentos da Conta", com opção de ver Detalhes ou Cancelar o acerto._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Valor Pago | Quanto está sendo pago nesse acerto. | ContaPagarBaixaController.cs |
| Juros Pago | Juros cobrados por atraso, se houver, somados ao valor pago. | ContaPagarBaixaController.cs |
| Desconto | Só é aceito quando o pagamento quita a conta inteira. | ContaPagarBaixaController.cs |
| Forma Pagamento | Dinheiro, Cartão, PIX, etc. | Obrigatório |
| Conta Financeira | De qual conta bancária/caixa o dinheiro realmente saiu — usada para conferir o extrato e alimentar o Fluxo de Caixa. | Obrigatório |

> ⚠️ Contas a Pagar é o destino de lançamentos automáticos vindos de outras rotinas: Contas Recorrentes (despesas que se repetem) e Pagamento de Profissionais (repasse calculado a partir dos atendimentos do mês) — ambas criam a conta aqui sozinhas, sem o usuário precisar cadastrar manualmente.
