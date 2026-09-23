# Tabela de Preços para Pagamento

_Cadastro, valores por Especialidade/Profissional e reajuste de preço em massa_

Versão 1.0 — 22/09/2026

A Tabela de Preços para Pagamento (Tabelas Aux. → Tab. Pagamento) define quanto a clínica paga a cada profissional por sessão atendida. É essa tabela que o relatório de Pagamento de Profissionais usa para calcular o valor a pagar todo mês. Este manual cobre o cadastro completo e a ferramenta de reajuste de preço em massa, que aplica um percentual a vários valores de uma vez, sem precisar editar linha por linha.

Vídeo narrado desta rotina: `video-tabela-preco-pagamento-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

## O conceito de "Tabela" (vigência)

Cada linha da lista principal é uma tabela de valores (o sistema chama de "vigência"), com uma Descrição e um status Ativo/Inativo. O botão de engrenagem ("Gerenciar") abre a tabela para cadastrar os valores propriamente ditos.

![Lista de tabelas de pagamento cadastradas, com o status Ativo de cada uma.](00-lista-vigencias.png)

_Lista de tabelas de pagamento cadastradas, com o status Ativo de cada uma._

> ⚠️ O cálculo do Pagamento de Profissionais sempre usa a tabela marcada como Ativo = Sim — e o sistema não garante que exista só uma. Nunca deixe duas tabelas ativas ao mesmo tempo: como não há uma ordem confiável entre elas, o resultado do cálculo fica imprevisível.

## Dentro de "Gerenciar": três abas

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Agenda | Vincula quais meses/anos de agenda usam esta tabela de vigência (não define preço, só habilita o mês para entrar no cálculo). | AgendaVigenciaProfPagto |
| Especialidades | Valor padrão por Especialidade × Tipo de Marcação, aplicado a todo profissional que não tiver um valor específico. | ConfigEspecPagto |
| Profissionais | Valor específico por Profissional × Especialidade × Tipo de Marcação, que sobrepõe o valor padrão da aba Especialidades só para aquele profissional. | ConfigProfissionalEspecialidadePagto |

![Aba "Especialidades": valor padrão (Valor e Valor Convênio) por Especialidade e Tipo de Marcação.](02-aba-especialidades.png)

_Aba "Especialidades": valor padrão (Valor e Valor Convênio) por Especialidade e Tipo de Marcação._

![Aba "Profissionais": ao clicar no ícone "$" de um profissional, abre a grade de valores específicos dele — sobrepõe o valor padrão só para esse profissional.](08-modal-valores-profissional.png)

_Aba "Profissionais": ao clicar no ícone "$" de um profissional, abre a grade de valores específicos dele — sobrepõe o valor padrão só para esse profissional._

## Reajuste de preço em massa

O card "Manutenção rápida de preços" aparece tanto na aba Especialidades (reajusta toda a tabela) quanto dentro do modal de valores de um profissional (reajusta só aquele profissional). O funcionamento é o mesmo nos dois casos.

![Botão "Reajustar preços" expande o formulário: percentual e quais campos reajustar (Valor e/ou Valor Convênio).](03-reajuste-formulario-aberto.png)

_Botão "Reajustar preços" expande o formulário: percentual e quais campos reajustar (Valor e/ou Valor Convênio)._

Passo a passo:

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| 1. Percentual de reajuste | Número positivo (aumento) ou negativo (desconto). Limite: maior que -100% e até 1000%. | ReajustePrecoController.cs |
| 2. Campos a reajustar | Marque "Valor", "Valor convênio", ou os dois. | reajuste-preco.component.html |
| 3. Calcular prévia | Mostra uma tabela comparando o valor atual com o valor novo, linha por linha — sem gravar nada ainda. | ReajustePreco/pagamento/simular |
| 4. Confirmar reajuste | Só depois de conferir a prévia, grava de fato. Pede uma confirmação extra ("Confirma o reajuste de X valor(es) em Y registro(s)?"). | ReajustePreco/pagamento/confirmar |

![Prévia de um reajuste de 10%: mostra valor atual e valor novo (em verde) de cada linha, sem alterar nada até a confirmação.](04-reajuste-previa.png)

_Prévia de um reajuste de 10%: mostra valor atual e valor novo (em verde) de cada linha, sem alterar nada até a confirmação._

![Confirmação final antes de gravar as alterações.](05-reajuste-modal-confirmar.png)

_Confirmação final antes de gravar as alterações._

!["9 valor(es) reajustado(s) com sucesso" — os valores já aparecem atualizados na grade.](06-reajuste-confirmado.png)

_"9 valor(es) reajustado(s) com sucesso" — os valores já aparecem atualizados na grade._

![O mesmo recurso, dentro do modal de um profissional específico: reajusta só os valores daquele profissional, sem afetar a tabela padrão.](09-reajuste-profissional-formulario.png)

_O mesmo recurso, dentro do modal de um profissional específico: reajusta só os valores daquele profissional, sem afetar a tabela padrão._

> ⚠️ A simulação (prévia) não grava nada — só depois de clicar em "Confirmar reajuste" os valores mudam de fato. Se algum valor for alterado por outra pessoa entre a prévia e a confirmação, o sistema recusa e pede para gerar uma nova prévia (evita reajustar em cima de dados já desatualizados). Linhas com Valor Convênio vazio não são alteradas, mesmo com o campo marcado. Toda confirmação de reajuste fica registrada no log do sistema.
