# Contas a Pagar

_Cadastrar e pagar as contas da clínica, com indicadores de vencimento_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Contas-a-Pagar/Documentacao_Contas_a_Pagar_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/dlllj9on1gQ?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/dlllj9on1gQ)

## Conteúdo completo do manual

---


_Cadastrar e pagar as contas da clínica, com indicadores de vencimento_

Versão 1.0 — 17/09/2026

Contas a Pagar é onde ficam todas as despesas da clínica: as lançadas manualmente aqui e também as que chegam automaticamente de outras rotinas, como Contas Recorrentes e Pagamento de Profissionais. A partir dela dá pra acompanhar o que está em aberto, vencido, vencendo hoje ou a vencer, e lançar os pagamentos (baixas) de cada conta. Assim como as demais telas financeiras, exige Plano de Conta e Centro de Custo já cadastrados.

---

## Indicadores do topo

Cinco caixas resumem a situação das contas: Em Aberto (soma de tudo que ainda não foi pago), Vencido (em aberto com vencimento no passado), Vence Hoje, A Vencer (em aberto com vencimento futuro) e Pago no Mês (soma do que já foi baixado no mês atual).


## Cadastrando uma conta a pagar (exemplo)

Clique em Novo. No exemplo abaixo, lançamos uma compra de material de escritório de R$ 350,00, tipo documento Boleto, vencendo hoje.


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Favorecido (Pessoa) | Para quem a clínica está pagando (fornecedor, prestador, profissional). *(obrigatório)* |
| Plano de Contas | Categoria da despesa (ex.: Material de Consumo). Precisa estar cadastrado antes. *(obrigatório)* |
| Centro de Custo | Setor da clínica responsável pela despesa. Precisa estar cadastrado antes. *(obrigatório)* |
| Valor Original | Valor total da conta antes de qualquer pagamento parcial. *(obrigatório)* |
| Tipo Documento | Boleto, Nota Fiscal, Contrato ou Pag. Profissional — este último é o tipo usado quando a conta vem da rotina de Pagamento de Profissionais. *(obrigatório)* |
| Competência (MM/AAAA) | Mês/ano de referência da despesa (pode ser diferente do mês do vencimento). *(obrigatório)* |
| Data Vencimento | Data limite para pagamento sem juros/atraso. *(obrigatório)* |


## Pagando (baixando) uma conta

O botão verde com o cifrão ($), na linha da conta, abre a tela de Pagamento / Acerto. É possível lançar mais de um pagamento para a mesma conta (pagamentos parciais) até o saldo chegar a zero.



| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Valor Pago | Quanto está sendo pago nesse acerto. |
| Juros Pago | Juros cobrados por atraso, se houver, somados ao valor pago. |
| Desconto | Só é aceito quando o pagamento quita a conta inteira. |
| Forma Pagamento | Dinheiro, Cartão, PIX, etc. *(obrigatório)* |
| Conta Financeira | De qual conta bancária/caixa o dinheiro realmente saiu — usada para conferir o extrato e alimentar o Fluxo de Caixa. *(obrigatório)* |

> ⚠️ Contas a Pagar é o destino de lançamentos automáticos vindos de outras rotinas: Contas Recorrentes (despesas que se repetem) e Pagamento de Profissionais (repasse calculado a partir dos atendimentos do mês) — ambas criam a conta aqui sozinhas, sem o usuário precisar cadastrar manualmente.
