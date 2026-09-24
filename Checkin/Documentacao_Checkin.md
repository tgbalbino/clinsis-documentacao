# Checkin de Paciente

_Registrar a chegada do paciente e, se houver cobrança, já receber na hora_

Versão 1.0 — 17/09/2026

O Checkin registra a chegada do paciente na clínica no dia da consulta/sessão. Quando o paciente tem um horário AGENDADO PARA HOJE que é cobrado na hora (ex.: particular, pagamento no ato), o Checkin também mostra a cobrança e permite lançar o pagamento — nesse caso, o sistema gera automaticamente uma Conta a Receber já paga. Pré-requisito importante: para o Checkin com pagamento funcionar, a clínica precisa ter configurado, na tela de Parâmetros do sistema, qual Plano de Conta, Centro de Custo e Conta Financeira usar para os recebimentos do Checkin — sem isso configurado corretamente (apontando para cadastros que realmente existem), o sistema recusa o lançamento.

Assista ao vídeo narrado desta rotina: [https://youtu.be/6usoK6x4e3I](https://youtu.be/6usoK6x4e3I)
---

## Tela inicial

Mostra os check-ins já feitos no dia (ou no período filtrado), com Paciente, Data/Hora do check-in, Horário da Agenda e quem atendeu. O botão Realizar Check-In abre o lançamento de um novo.

![Tela inicial de Paciente Check-In.](00-lista-inicial.png)

_Tela inicial de Paciente Check-In._

## Antes de usar: configuração obrigatória em Parâmetros

O Checkin só consegue lançar pagamento se a clínica tiver configurado, com antecedência, para qual Plano de Conta, Centro de Custo e Conta Financeira o dinheiro recebido no Checkin deve ir. Essa configuração não fica em uma tela própria do Checkin — fica na tela geral de Parâmetros do sistema, em Tabelas Aux. → Parâmetros (rota /aux/parametro).

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| IdPlanoContaCheckin | Qual Plano de Conta é usado nos recebimentos lançados pelo Checkin (ex.: "Honorário Médico"). | Parâmetro configurável em Tabelas Aux. → Parâmetros |
| IdCentroCustoCheckin | Qual Centro de Custo é usado nos recebimentos lançados pelo Checkin. | Parâmetro configurável em Tabelas Aux. → Parâmetros |
| IdContaFinanceiraCheckin | Para qual Conta Financeira (banco/caixa) vai o valor recebido no Checkin. | Parâmetro configurável em Tabelas Aux. → Parâmetros |

Na tela de Parâmetros, procure por esses três nomes na lista: se ainda não estiverem configurados, clique em Configurar; se já estiverem, use o lápis para editar o valor. O valor de cada um deve apontar para um Plano de Conta / Centro de Custo / Conta Financeira que realmente exista e esteja ativo no sistema — se o cadastro apontado for excluído depois, o Checkin com pagamento passa a falhar até alguém corrigir o parâmetro de novo.

## Identificando o paciente

O Checkin foi pensado para ser rápido no balcão: o campo principal lê um código de barras (de uma carteirinha ou pulseira do paciente, por exemplo), confirmando o paciente automaticamente assim que o código é lido. Quando não há código de barras à mão, o botão Pesquisa Manual abre uma busca por nome/CPF para selecionar o paciente na mão.

![Tela de Check-In: campo para leitura de código de barras, ou os botões "Ler Código" / "Pesquisa Manual".](01-modal-codigo-barras.png)

_Tela de Check-In: campo para leitura de código de barras, ou os botões "Ler Código" / "Pesquisa Manual"._

![Resultado da Pesquisa Manual por nome.](02-pesquisa-resultado.png)

_Resultado da Pesquisa Manual por nome._

## Quando o paciente tem um horário cobrável hoje

Assim que o paciente é identificado, o sistema busca automaticamente os horários da agenda de hoje dele. Se houver um horário marcado para hoje com uma especialidade que cobra (configurada em Config → Cobrança), aparece a linha do horário já marcada, com o Valor e o Valor Social daquela sessão.

![Exemplo real: paciente "Paciente 000" com um horário de hoje (19:50, especialidade "TO" = Terapeuta Ocupacional) já selecionado, valor R$ 1,99.](03-paciente-com-agenda-hoje.png)

_Exemplo real: paciente "Paciente 000" com um horário de hoje (19:50, especialidade "TO" = Terapeuta Ocupacional) já selecionado, valor R$ 1,99._

![Com o horário marcado, aparecem o Tipo de Preço (Normal ou Social) e a área "Adicionar pagamento".](04-horarios-marcados-com-valor.png)

_Com o horário marcado, aparecem o Tipo de Preço (Normal ou Social) e a área "Adicionar pagamento"._

## Lançando o pagamento

Escolha a Forma de Pagamento (Dinheiro, Cartão, PIX, etc.), informe o valor — ou use o botão da calculadora para preencher automaticamente o "valor restante" — e clique em Adicionar. É possível combinar mais de uma forma de pagamento na mesma cobrança, até o "Restante" chegar a zero.

![Forma de pagamento "Dinheiro" com o valor da sessão preenchido, antes de clicar em Adicionar.](05-pagamento-preenchido.png)

_Forma de pagamento "Dinheiro" com o valor da sessão preenchido, antes de clicar em Adicionar._

![Depois de Adicionar: o pagamento aparece na lista, Total pago R$ 1,99 e Restante R$ 0,00 — com isso o botão Confirmar Check-In fica disponível.](06-pagamento-adicionado.png)

_Depois de Adicionar: o pagamento aparece na lista, Total pago R$ 1,99 e Restante R$ 0,00 — com isso o botão Confirmar Check-In fica disponível._

## Confirmando o Check-In

Ao clicar em Confirmar Check-In, o sistema registra a chegada do paciente e, como havia pagamento, já gera e baixa a Conta a Receber na hora.

![Check-in confirmado: aparece na lista com o horário da agenda (19:50:00) e o usuário responsável.](07-apos-confirmar-checkin.png)

_Check-in confirmado: aparece na lista com o horário da agenda (19:50:00) e o usuário responsável._

![Conferindo em Contas a Receber: a linha do "Paciente 000", R$ 1,99, Plano de Conta "Honorário Médico", Situação "Baixada" — gerada e já paga automaticamente pelo Checkin, sem nenhum lançamento manual.](08-conta-a-receber-gerada-pelo-checkin.png)

_Conferindo em Contas a Receber: a linha do "Paciente 000", R$ 1,99, Plano de Conta "Honorário Médico", Situação "Baixada" — gerada e já paga automaticamente pelo Checkin, sem nenhum lançamento manual._

## Quando não há agenda para hoje

Se o sistema não encontrar nenhum horário marcado para hoje para aquele paciente, aparece o aviso "Nenhuma marcação existente na agenda para o dia" e o check-in não é processado — o Checkin serve para confirmar presença em algo que já está na agenda do dia, não para criar um atendimento novo.

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Código de barras / Pesquisa Manual | Forma de identificar o paciente que está chegando. | CheckinComponent |
| Horários do dia (checkbox) | Quais atendimentos de hoje estão sendo confirmados nesse check-in. | PacienteAgendaDoDiaDto |
| Tipo de Preço | Normal ou Social — só aparece quando o atendimento tem cobrança configurada para a especialidade. | CheckinComponent |
| Adicionar pagamento (Forma + Valor) | Cada forma de pagamento usada e seu valor, até fechar o total a receber. | CheckinController.cs (inserir) |

> ⚠️ Esta é uma das rotinas que geram Conta a Receber automaticamente: quando o Checkin tem pagamento, o sistema já cria a Conta a Receber JÁ BAIXADA (já paga) no momento da confirmação — o usuário não precisa ir depois em Contas a Receber lançar nada manualmente.

Se o Checkin com pagamento for recusado, a mensagem exibida agora indica exatamente qual dos três parâmetros (Plano de Conta, Centro de Custo ou Conta Financeira) está sem configurar ou aponta para um cadastro que não existe mais — basta ir em Tabelas Aux. → Parâmetros e corrigir o valor indicado.
