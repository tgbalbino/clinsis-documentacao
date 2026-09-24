# Contas Recorrentes

_Contas que se repetem todo mês (ou a cada período) geradas automaticamente_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Contas-Recorrentes/Documentacao_Contas_Recorrentes_Simplificado.pdf)

## Vídeo narrado

- [▶️ Assistir o vídeo no YouTube](https://youtu.be/1qx_Mgp4T_Q)

## Conteúdo completo do manual

*As capturas de tela deste trecho estão no PDF acima — aqui fica só o texto.*

---


_Contas que se repetem todo mês (ou a cada período) geradas automaticamente_

Versão 1.0 — 17/09/2026

Contas Recorrentes serve para cadastrar UMA VEZ uma despesa ou receita que se repete sempre (ex.: aluguel, mensalidade de software, salário de um profissional fixo) e deixar o próprio sistema gerar automaticamente o lançamento em Contas a Pagar (ou Contas a Receber) a cada novo período — sem precisar cadastrar tudo de novo todo mês. Esta rotina exige Plano de Conta, Centro de Custo e um Favorecido (Pessoa) já cadastrados antes de usar.

Assista ao vídeo narrado desta rotina: [https://youtu.be/1qx_Mgp4T_Q](https://youtu.be/1qx_Mgp4T_Q)
---

## Tela inicial

Lista todas as contas recorrentes já cadastradas, com Favorecido, Plano de Contas, Centro de Custo, Descrição, Frequência, Dia de Vencimento, período de vigência (Início/Fim) e Valor.


## Cadastrando uma nova conta recorrente (exemplo)

Clique em Novo. No exemplo abaixo, cadastramos um aluguel de R$ 1.500,00, mensal, vencendo todo dia 10, começando hoje.


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Favorecido | Pessoa (fornecedor, profissional, cliente) para quem o pagamento é feito ou de quem o recebimento vem. *(obrigatório)* |
| Plano de Contas | Categoria do lançamento (ex.: Aluguel). Precisa estar cadastrado antes, na tela de Plano de Contas. *(obrigatório)* |
| Centro de Custo | Setor da clínica responsável pelo lançamento. Precisa estar cadastrado antes, na tela de Centro de Custo. *(obrigatório)* |
| Descrição | Texto livre identificando o lançamento nas contas geradas. *(obrigatório)* |
| Valor | Valor de cada parcela gerada automaticamente. *(obrigatório)* |
| Dia Vencimento | Dia do mês (1 a 31) em que a conta gerada deve vencer. *(obrigatório)* |
| Frequência | De quanto em quanto tempo o sistema gera uma nova conta: Mensal, Bimestral, Trimestral, Semestral ou Anual. *(obrigatório)* |
| Data Início / Data Fim | Período em que a recorrência vale. Data Fim vazia = sem previsão de encerramento. |
| Gerar Antecedência | Quantos dias antes do vencimento o sistema já pode gerar a conta (para dar tempo de conferir/pagar antes do prazo). |


## Como a geração automática acontece

Todos os dias, um job (rotina automática) do sistema roda de madrugada e verifica quais contas recorrentes precisam gerar um novo lançamento naquele dia (considerando a frequência, o dia de vencimento e a antecedência configurada). Quando isso acontece, o sistema cria automaticamente uma nova Conta a Pagar (ou Conta a Receber, dependendo do tipo do Plano de Conta) — sem nenhuma ação manual do usuário.

Para conferir isso sem esperar até a madrugada, esta tela tem o botão Log do Job, que mostra o histórico de execuções e também permite forçar a execução agora — útil para testar ou para gerar uma conta que ficou pendente.



## Onde a conta gerada aparece

A conta criada automaticamente pelo job aparece normalmente na tela de Contas a Pagar (ou Contas a Receber, se o Plano de Conta for do tipo Receita), como qualquer outro lançamento — só que já vem com Favorecido, Plano de Conta, Centro de Custo, Descrição e Valor preenchidos automaticamente, prontos para conferência e pagamento.


> ⚠️ Esta é uma das rotinas que geram Conta a Pagar/Receber automaticamente: o usuário cadastra a recorrência uma única vez, e o sistema cuida de criar os lançamentos a cada período, sem precisar repetir o cadastro manualmente todo mês.
