# Tabela de Valores para Pagamento

_Cadastro, valores por Especialidade/Profissional e reajuste de preço em massa_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Tabela-de-Precos-Pagamento/Documentacao_Tabela_Preco_Pagamento_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/tupHNaRxSrY?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/tupHNaRxSrY)

## Conteúdo completo do manual

---


_Cadastro, valores por Especialidade/Profissional e reajuste de preço em massa_

Versão 1.1 — 30/09/2026

A Tabela de Valores para Pagamento (Tabelas Aux. → Tab. Pagamento) define quanto a clínica paga a cada profissional por sessão atendida. É essa tabela que o relatório de Pagamento de Profissionais usa para calcular o valor a pagar todo mês. Este manual cobre o cadastro completo e a ferramenta de reajuste de preço em massa, que aplica um percentual a vários valores de uma vez, sem precisar editar linha por linha.


---

## O conceito de "Tabela de Valores"

Cada linha da lista principal é uma Tabela de Valores, com uma Descrição e um status Ativo/Inativo. O botão de engrenagem ("Valores") abre a tabela para cadastrar os valores propriamente ditos.


> ⚠️ O cálculo do Pagamento de Profissionais sempre usa a tabela marcada como Ativo = Sim — e o sistema não garante que exista só uma. Nunca deixe duas tabelas ativas ao mesmo tempo: como não há uma ordem confiável entre elas, o resultado do cálculo fica imprevisível.

## Dentro de "Valores": três abas

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Agenda | Vincula quais meses/anos de agenda usam esta tabela de valores (não define preço, só habilita o mês para entrar no cálculo). |
| Especialidades | Valor padrão por Especialidade × Tipo de Marcação, aplicado a todo profissional que não tiver um valor específico. |
| Profissionais | Valor específico por Profissional × Especialidade × Tipo de Marcação, que sobrepõe o valor padrão da aba Especialidades só para aquele profissional. |



## Reajuste de preço em massa

O card "Manutenção rápida de preços" aparece tanto na aba Especialidades (reajusta toda a tabela) quanto dentro do modal de valores de um profissional (reajusta só aquele profissional). O funcionamento é o mesmo nos dois casos.


Passo a passo:

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| 1. Percentual de reajuste | Número positivo (aumento) ou negativo (desconto). Limite: maior que -100% e até 1000%. |
| 2. Campos a reajustar | Marque "Valor", "Valor convênio", ou os dois. |
| 3. Calcular prévia | Mostra uma tabela comparando o valor atual com o valor novo, linha por linha — sem gravar nada ainda. |
| 4. Confirmar reajuste | Só depois de conferir a prévia, grava de fato. Pede uma confirmação extra ("Confirma o reajuste de X valor(es) em Y registro(s)?"). |





> ⚠️ A simulação (prévia) não grava nada — só depois de clicar em "Confirmar reajuste" os valores mudam de fato. Se algum valor for alterado por outra pessoa entre a prévia e a confirmação, o sistema recusa e pede para gerar uma nova prévia (evita reajustar em cima de dados já desatualizados). Linhas com Valor Convênio vazio não são alteradas, mesmo com o campo marcado. Toda confirmação de reajuste fica registrada no log do sistema.

## Valores, limites e uso no celular

| Assunto | O que saber |
|---|---|
| Valores com milhar | Os valores aparecem com separador de milhar (por exemplo, 1.250,00) na lista e nos campos. |
| Valor máximo | Cada valor aceita até R$ 99.999.999,99 (8 dígitos antes da vírgula). O campo não deixa digitar mais que isso, e o reajuste em massa também respeita esse teto. |
| Falha ao salvar | Se o salvamento falhar (por exemplo, por um valor inválido), o sistema mostra o erro e recarrega a lista, para você ver o que realmente está gravado. |
| No celular | As abas Especialidades e Profissionais mostram os valores em cartões, com menu de ações e busca, em vez de tabela. |
