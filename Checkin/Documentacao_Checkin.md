# Checkin de Paciente

_Registrar a chegada do paciente e, se houver cobrança, já receber na hora_

Versão 2.1 — 16/10/2026

O Checkin registra a chegada do paciente na clínica no dia da consulta ou sessão. Quando o paciente tem um horário agendado para hoje que é cobrado na hora (por exemplo, atendimento particular), o Checkin também mostra a cobrança e permite lançar o pagamento: nesse caso, o sistema gera automaticamente uma Conta a Receber já paga. Para o pagamento funcionar, a clínica precisa ter configurado, em Parâmetros, o Plano de Conta, o Centro de Custo e a Conta Financeira do Checkin, e o usuário precisa ter o caixa aberto.

Assista ao vídeo narrado desta rotina: [https://youtu.be/ifvL23xnsPY](https://youtu.be/ifvL23xnsPY)

---

## Tela inicial

Na Home, clique no cartão Check-in (perfil administrador; endereço /paciente/checkin). A tela mostra os check-ins já feitos na data escolhida, com Paciente, Data/Hora do check-in, Horário da Agenda e quem atendeu. O botão Realizar Check-In abre o lançamento de um novo.

![Paciente Check-In: check-ins do dia e o botão Realizar Check-In.](00-lista-inicial.png)

_Paciente Check-In: check-ins do dia e o botão Realizar Check-In._

## Antes de usar

| O que precisa existir | Onde configurar / como conferir |
|---|---|
| Parâmetros do Checkin | Em Tabelas Aux. → Parâmetros, configure IdPlanoContaCheckin (Plano de Conta), IdCentroCustoCheckin (Centro de Custo) e IdContaFinanceiraCheckin (Conta Financeira que recebe o valor). Cada um deve apontar para um cadastro que exista e esteja ativo; se o cadastro for excluído depois, o Checkin com pagamento passa a falhar até o parâmetro ser corrigido. A mensagem de erro diz qual dos três está errado. |
| Caixa aberto | Se o usuário controla caixa, é preciso abrir o caixa antes (menu Caixa). Sem isso, o sistema avisa: "Nenhum caixa aberto para o usuário. Abra o caixa antes de registrar o recebimento." |
| Plano Próprio | O Checkin trabalha com pacientes de Plano Próprio (por exemplo, operadora PROPRIO). Se nem o cadastro do paciente nem o agendamento forem de plano próprio, o sistema avisa e não confirma. Se só o agendamento for, ele pergunta se deseja atualizar o cadastro do paciente. |
| Horário de hoje e valor | O paciente precisa ter um horário marcado hoje, com uma especialidade que tenha valor em Config → Cobrança. |

## Identificando o paciente

O campo principal lê o código de barras da carteirinha ou pulseira do paciente e confirma o paciente assim que o código é lido. Sem o código à mão, use Pesquisa Manual: digite o nome ou CPF, pressione Enter e clique em selecionar na linha do paciente.

![Check-In: campo para leitura do código de barras, ou os botões Ler Código e Pesquisa Manual.](01-modal-codigo-barras.png)

_Check-In: campo para leitura do código de barras, ou os botões Ler Código e Pesquisa Manual._

![Resultado da Pesquisa Manual por nome.](02-pesquisa-resultado.png)

_Resultado da Pesquisa Manual por nome._

## Quando o paciente tem um horário cobrável hoje

Identificado o paciente, o sistema busca os horários de hoje dele e mostra, para cada um, o dia, a data, a hora, o profissional, a especialidade, o Valor e o Valor Social. Marque a caixa do horário que está sendo confirmado; pode marcar mais de um.

![Horário de hoje do paciente (20:30, especialidade TO), com Valor e Valor Social.](03-paciente-com-agenda-hoje.png)

_Horário de hoje do paciente (20:30, especialidade TO), com Valor e Valor Social._

Depois de marcar, escolha o Tipo de preço (Valor normal ou Valor social). O campo Valor Receber mostra o total a cobrar.

![Horário marcado, Tipo de preço e Valor Receber (R$ 36,56) preenchidos, com a área Adicionar pagamento.](04-horarios-marcados-com-valor.png)

_Horário marcado, Tipo de preço e Valor Receber (R$ 36,56) preenchidos, com a área Adicionar pagamento._

> ⚠️ Se aparecer "* Verificar pendência de pagamento" em vermelho, o paciente tem valor em aberto em Contas a Receber. Confira antes de finalizar.

## Lançando o pagamento

Em Adicionar pagamento, escolha a forma (Dinheiro, Pix, Cheque, Car. Débito ou Car. Crédito), informe o valor, ou use o botão da calculadora para preencher o valor restante, e clique em Adicionar. É possível combinar mais de uma forma de pagamento até o Restante chegar a zero.

![Forma Dinheiro com o valor da sessão preenchido, antes de clicar em Adicionar.](05-pagamento-preenchido.png)

_Forma Dinheiro com o valor da sessão preenchido, antes de clicar em Adicionar._

![Depois de Adicionar: o pagamento aparece na lista, Total pago R$ 36,56 e Restante R$ 0,00.](06-pagamento-adicionado.png)

_Depois de Adicionar: o pagamento aparece na lista, Total pago R$ 36,56 e Restante R$ 0,00._

No Cartão de Crédito aparece o campo de Parcelas, limitado ao máximo de parcelas de recebimento configurado para a clínica; as parcelas seguem para a Conta a Receber.

![Car. Crédito: campo de parcelas ao lado da forma de pagamento.](06b-cartao-credito-parcelas.png)

_Car. Crédito: campo de parcelas ao lado da forma de pagamento._

## Confirmando o Check-In

Com o Restante em zero, clique em Confirmar Check-In. O sistema registra a chegada e, como houve pagamento, gera e baixa a Conta a Receber na hora, lançando o valor na Conta Financeira configurada e no caixa aberto do usuário.

![Check-in confirmado: aparece na lista com a data/hora, o horário da agenda (20:30:00) e o atendente.](07-apos-confirmar-checkin.png)

_Check-in confirmado: aparece na lista com a data/hora, o horário da agenda (20:30:00) e o atendente._

![Contas a Receber: a linha do paciente, R$ 36,56, Plano de Conta "Consulta Particular", Situação "Baixada", gerada e paga automaticamente pelo Checkin.](08-conta-a-receber-gerada-pelo-checkin.png)

_Contas a Receber: a linha do paciente, R$ 36,56, Plano de Conta "Consulta Particular", Situação "Baixada", gerada e paga automaticamente pelo Checkin._

> ⚠️ Esta rotina gera Conta a Receber automaticamente: não é preciso lançar nada à mão em Contas a Receber.

## Avisar o profissional (Painel de chegada)

Com o módulo Painel de chegada ligado na clínica, logo depois de confirmar o Check-In abre a janela Notificar profissional: "Deseja avisar o profissional que o paciente chegou?". Cada horário do paciente aparece com a hora e o profissional. Marque os que quiser e clique em Avisar agora (ou em Agora não). O sistema confirma com "N aviso(s) enviado(s) para o painel": a TV da clínica mostra Nova chegada e o profissional recebe o chamado no sistema. Se nenhuma TV estiver conectada, o aviso não é enviado. Todos os detalhes estão no manual Painel de Chegada (TV).

![TV da clínica mostrando a chegada avisada pelo Check-In.](09-painel-tv-nova-chegada.png)

_TV da clínica mostrando a chegada avisada pelo Check-In._

## Aviso de revisão cadastral

Com o módulo Revisão cadastral ligado, se o cadastro do paciente precisa de revisão (prazo vencido, endereço incompleto ou sem contato), aparece uma faixa amarela no Check-In com o motivo. O aviso não bloqueia o check-in; o link Abrir cadastro em outra aba permite conferir os dados sem perder o atendimento. Veja o manual Revisão Cadastral de Pacientes.

![Check-In: faixa de revisão cadastral com o motivo, acima dos agendamentos do dia.](10-aviso-revisao-cadastral.png)

_Check-In: faixa de revisão cadastral com o motivo, acima dos agendamentos do dia._

## Quando o paciente já se anunciou no totem

Se a clínica usa o Totem de check-in, o paciente (ou o responsável) pode registrar a chegada sozinho na portaria. Na Agenda, aparece um selo verde com o horário antes do nome do paciente. O totem apenas avisa a chegada: o Check-In da recepção, com pagamento e Plano Próprio, continua sendo feito normalmente, como descrito neste manual. Veja o manual Totem de Check-in.

![Agenda: selo verde com o horário da chegada registrada no totem.](11-agenda-chegada-totem.png)

_Agenda: selo verde com o horário da chegada registrada no totem._

## Mensagens que você pode encontrar

| Mensagem | Causa | O que fazer |
|---|---|---|
| Nenhuma marcação existente na agenda para o dia | O paciente não tem horário marcado hoje. | Confira a data e a agenda. O Checkin confirma presença em algo já agendado; não cria atendimento novo. |
| Existe 1 marcação na agenda para o dia e 1 check-in realizado | Todos os horários de hoje já tiveram check-in. | Nada a fazer. |
| Selecione ao menos um horário e informe o valor | Nenhum horário marcado ou sem valor a receber. | Marque o horário e confira o Tipo de preço. |
| Nenhum caixa aberto para o usuário... | O usuário controla caixa e ainda não abriu. | Abra o caixa e confirme de novo. |
| Paciente não está vinculado a um Plano Próprio... | Nem o cadastro nem o agendamento são de plano próprio. | Ajuste a operadora do agendamento ou do cadastro do paciente. |
| Erro citando Plano de Conta, Centro de Custo ou Conta Financeira | Parâmetro do Checkin vazio ou apontando para cadastro excluído. | Corrija em Tabelas Aux. → Parâmetros. |
