# Checkin de Paciente

O Check-in registra a chegada do paciente à clínica. Quando o atendimento é cobrável, o pagamento já pode ser lançado na hora, evitando cobranças esquecidas e mantendo o caixa conferido no mesmo dia. Rotina diária da recepção.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Checkin/Documentacao_Checkin_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/MKW8mdKnfTg?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/MKW8mdKnfTg)

## Conteúdo completo do manual

---


_Registrar a chegada do paciente e, se houver cobrança, já receber na hora_

Versão 2.0 — 30/09/2026

O Checkin registra a chegada do paciente na clínica no dia da consulta ou sessão. Quando o paciente tem um horário agendado para hoje que é cobrado na hora (por exemplo, atendimento particular), o Checkin também mostra a cobrança e permite lançar o pagamento: nesse caso, o sistema gera automaticamente uma Conta a Receber já paga. Para o pagamento funcionar, a clínica precisa ter configurado, em Parâmetros, o Plano de Conta, o Centro de Custo e a Conta Financeira do Checkin, e o usuário precisa ter o caixa aberto.


---

## Tela inicial

Na Home, clique no cartão Check-in (perfil administrador; endereço /paciente/checkin). A tela mostra os check-ins já feitos na data escolhida, com Paciente, Data/Hora do check-in, Horário da Agenda e quem atendeu. O botão Realizar Check-In abre o lançamento de um novo.


## Antes de usar

| O que precisa existir | Onde configurar / como conferir |
|---|---|
| Parâmetros do Checkin | Em Tabelas Aux. → Parâmetros, configure IdPlanoContaCheckin (Plano de Conta), IdCentroCustoCheckin (Centro de Custo) e IdContaFinanceiraCheckin (Conta Financeira que recebe o valor). Cada um deve apontar para um cadastro que exista e esteja ativo; se o cadastro for excluído depois, o Checkin com pagamento passa a falhar até o parâmetro ser corrigido. A mensagem de erro diz qual dos três está errado. |
| Caixa aberto | Se o usuário controla caixa, é preciso abrir o caixa antes (menu Caixa). Sem isso, o sistema avisa: "Nenhum caixa aberto para o usuário. Abra o caixa antes de registrar o recebimento." |
| Plano Próprio | O Checkin trabalha com pacientes de Plano Próprio (por exemplo, operadora PROPRIO). Se nem o cadastro do paciente nem o agendamento forem de plano próprio, o sistema avisa e não confirma. Se só o agendamento for, ele pergunta se deseja atualizar o cadastro do paciente. |
| Horário de hoje e valor | O paciente precisa ter um horário marcado hoje, com uma especialidade que tenha valor em Config → Cobrança. |

## Identificando o paciente

O campo principal lê o código de barras da carteirinha ou pulseira do paciente e confirma o paciente assim que o código é lido. Sem o código à mão, use Pesquisa Manual: digite o nome ou CPF, pressione Enter e clique em selecionar na linha do paciente.



## Quando o paciente tem um horário cobrável hoje

Identificado o paciente, o sistema busca os horários de hoje dele e mostra, para cada um, o dia, a data, a hora, o profissional, a especialidade, o Valor e o Valor Social. Marque a caixa do horário que está sendo confirmado; pode marcar mais de um.


Depois de marcar, escolha o Tipo de preço (Valor normal ou Valor social). O campo Valor Receber mostra o total a cobrar.


> ⚠️ Se aparecer "* Verificar pendência de pagamento" em vermelho, o paciente tem valor em aberto em Contas a Receber. Confira antes de finalizar.

## Lançando o pagamento

Em Adicionar pagamento, escolha a forma (Dinheiro, Pix, Cheque, Car. Débito ou Car. Crédito), informe o valor, ou use o botão da calculadora para preencher o valor restante, e clique em Adicionar. É possível combinar mais de uma forma de pagamento até o Restante chegar a zero.



No Cartão de Crédito aparece o campo de Parcelas, limitado ao máximo de parcelas de recebimento configurado para a clínica; as parcelas seguem para a Conta a Receber.


## Confirmando o Check-In

Com o Restante em zero, clique em Confirmar Check-In. O sistema registra a chegada e, como houve pagamento, gera e baixa a Conta a Receber na hora, lançando o valor na Conta Financeira configurada e no caixa aberto do usuário.



> ⚠️ Esta rotina gera Conta a Receber automaticamente: não é preciso lançar nada à mão em Contas a Receber.

## Mensagens que você pode encontrar

| Mensagem | Causa | O que fazer |
|---|---|---|
| Nenhuma marcação existente na agenda para o dia | O paciente não tem horário marcado hoje. | Confira a data e a agenda. O Checkin confirma presença em algo já agendado; não cria atendimento novo. |
| Existe 1 marcação na agenda para o dia e 1 check-in realizado | Todos os horários de hoje já tiveram check-in. | Nada a fazer. |
| Selecione ao menos um horário e informe o valor | Nenhum horário marcado ou sem valor a receber. | Marque o horário e confira o Tipo de preço. |
| Nenhum caixa aberto para o usuário... | O usuário controla caixa e ainda não abriu. | Abra o caixa e confirme de novo. |
| Paciente não está vinculado a um Plano Próprio... | Nem o cadastro nem o agendamento são de plano próprio. | Ajuste a operadora do agendamento ou do cadastro do paciente. |
| Erro citando Plano de Conta, Centro de Custo ou Conta Financeira | Parâmetro do Checkin vazio ou apontando para cadastro excluído. | Corrija em Tabelas Aux. → Parâmetros. |
