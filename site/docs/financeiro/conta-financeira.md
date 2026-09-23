# Cadastro de Conta Financeira

_O que é, onde é usada e a validação Conta Financeira x Forma de Pagamento_

## Documentação em PDF

- [📄 Manual completo (com origem técnica no banco)](../assets/Conta-Financeira/Documentacao_Conta_Financeira.pdf)
- [📄 Manual simplificado](../assets/Conta-Financeira/Documentacao_Conta_Financeira_Simplificado.pdf)

## Vídeo narrado

*Vídeo em processo de publicação — o link será adicionado aqui assim que estiver disponível no YouTube.*

## Conteúdo completo do manual

*As capturas de tela deste trecho estão no PDF acima — aqui fica só o texto.*

---


_O que é, onde é usada e a validação Conta Financeira x Forma de Pagamento_

Versão 1.0 — 18/09/2026

A Conta Financeira é o "cofre" onde o dinheiro da clínica realmente entra e sai: uma conta bancária (Banco do Brasil, Sicoob, etc.) ou o próprio caixa em dinheiro. Toda baixa (recebimento ou pagamento) informa em qual conta o valor caiu ou de qual conta ele saiu — é isso que permite conferir o extrato do banco, saber o saldo de cada conta e montar o Fluxo de Caixa. Este manual explica o cadastro, onde ele é usado e, principalmente, a regra que amarra cada Conta Financeira às Formas de Pagamento permitidas nela.

Vídeo narrado desta rotina: `video-conta-financeira-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

## O que é e para que serve

Cada Conta Financeira representa um lugar onde existe saldo. Exemplos: "BANCO BRASIL" (conta corrente da clínica), "SICOOB CONTA CORRENTE" ou "CAIXA" (o dinheiro em espécie na recepção). Sem Conta Financeira o sistema não sabe onde o dinheiro foi parar, e por isso ela é obrigatória em toda baixa de Conta a Pagar e de Conta a Receber, e também na baixa automática do Checkin.

O cadastro fica em Financeiro → Cadastros → Contas Financeiras (acesso do administrador).


## Cadastrando uma conta nova

Clique em Novo e preencha. Só a Descrição é obrigatória; os demais campos são opcionais e servem para identificar a conta bancária.


| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Descrição * | Nome que aparece em todas as telas de baixa, movimentos e fluxo de caixa. Sempre gravado em maiúsculas. | ContaFinanceira.Descricao |
| Banco | Banco da conta (lista de bancos cadastrados). Deixe em branco para uma conta do tipo Caixa. | ContaFinanceira.IdBanco |
| Agência | Agência bancária (até 20 caracteres). | ContaFinanceira.Agencia |
| Conta | Número da conta (até 30 caracteres). | ContaFinanceira.Conta |
| Chave PIX | Chave PIX da conta, só para consulta/identificação. | ContaFinanceira.ChavePix |
| Ativo (só ao editar) | Conta inativa deixa de ser oferecida nas telas de baixa (só contas ativas aparecem na lista), mas o histórico é mantido. | ContaFinanceira.Ativo |
| Tipo (badge Banco/Caixa) | Não é um campo: aparece como "Banco" se Banco/Agência/Conta estiverem preenchidos e como "Caixa" caso contrário. | Calculado na tela (conta-financeira-painel) |



> ⚠️ Uma conta Inativa é a forma correta de "aposentar" uma conta que já teve movimento: ela some das telas de baixa, mas o histórico de movimentos continua íntegro.

## Onde a Conta Financeira é usada

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Contas a Pagar — baixa | Campo Conta Financeira (obrigatório): de qual conta o dinheiro saiu. Gera um movimento de Saída na conta. | ContaPagarBaixaRepository.cs |
| Contas a Receber — baixa | Campo Conta Financeira (obrigatório na tela: "Informe a conta financeira"): em qual conta o dinheiro entrou. Gera um movimento de Entrada na conta. | ContaReceberBaixaRepository.cs |
| Checkin de Paciente | A baixa automática do pagamento feito no Checkin usa a conta definida no parâmetro IdContaFinanceiraCheckin. | CheckinRepository.cs / Parametro |
| Movimentos Financeiros | Extrato de todas as entradas/saídas, com filtro por conta. Também permite Nova Transferência entre duas contas. | MovimentoFinanceiro |
| Fluxo de Caixa e Dashboard | Saldo, entradas e saídas por conta (quadro "Por Conta Financeira"). | MovimentoFinanceiro |



## Validação Conta Financeira x Forma de Pagamento

Nem toda forma de pagamento faz sentido em toda conta. Uma máquina de cartão, por exemplo, deposita na conta bancária — não existe "Cartão de Crédito" dentro da gaveta de dinheiro do caixa. Por isso cada Conta Financeira tem a sua própria lista de Formas de Pagamento permitidas, e o sistema recusa qualquer baixa que combine uma forma com uma conta em que ela não foi habilitada.

Essa regra vale em três lugares: baixa de Conta a Receber, baixa de Conta a Pagar e pagamento do Checkin.

## Como configurar (passo a passo)

Passo 1 — Formas de pagamento da clínica. Em Tabelas Aux. → Formas de Pagamento ficam as formas com as quais a clínica trabalha (Cartão de Crédito, Débito, Cheque, Dinheiro, Pix). Só as formas ativas aqui são oferecidas nas telas de baixa e servem de sugestão inicial para as contas novas.


Passo 2 — Formas permitidas em cada conta. Na lista de Contas Financeiras, clique no botão azul "Formas de pagamento desta conta" (ícone de cheque) da linha desejada. Cada forma tem um botão: Desabilitar (vermelho) quando está permitida e Habilitar (verde) quando não está.




> ⚠️ Ao criar uma conta, o sistema já a deixa com todas as formas ativas da clínica habilitadas — é uma sugestão inicial. Confira sempre a lista e desabilite o que não se aplica àquela conta (ex.: cartão em uma conta "Caixa").

## Exemplo prático: o que acontece na tela

Exemplo 1 — Combinação não permitida (Conta a Receber). Com a conta CAIXA aceitando apenas Dinheiro e Pix, tentamos receber R$ 1,00 escolhendo Método Pagto = Cartão de Crédito e Conta Financeira = CAIXA. O sistema recusa e mostra a orientação de como resolver.


Exemplo 2 — Combinação permitida. Trocando o método para Dinheiro (que a conta CAIXA aceita), a baixa é gravada normalmente e passa a aparecer no extrato da conta.


Exemplo 3 — Mesma regra em Contas a Pagar. A baixa de uma Conta a Pagar com Cartão de Crédito saindo do CAIXA é recusada com a mesma mensagem. Aqui a Conta Financeira é obrigatória (asterisco vermelho no campo). Em Contas a Receber a tela também exige a conta, mesmo sem o asterisco.


> ⚠️ Se aparecer essa mensagem no dia a dia, há duas saídas: escolher outra Conta Financeira que aceite aquela forma (ex.: a conta bancária, para cartão) ou habilitar a forma na conta desejada pelo botão "Formas de pagamento desta conta".

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Regra de validação | Ao gravar a baixa, o sistema consulta se existe o par (Conta Financeira, Forma de Pagamento) habilitado. Se não existir, recusa e não grava nada. | ContaFinanceiraPagamentoForma |
| Onde é conferida | Baixa de Conta a Receber, baixa de Conta a Pagar e pagamento do Checkin (que usa a conta do parâmetro IdContaFinanceiraCheckin). | ContaReceberBaixaRepository.cs / ContaPagarBaixaRepository.cs / CheckinRepository.cs |

## Conta Financeira do Checkin

O pagamento feito no Checkin do paciente gera uma Conta a Receber e sua baixa automática. Como não existe um campo para o recepcionista escolher a conta, o sistema usa a definida no parâmetro IdContaFinanceiraCheckin (Tabelas Aux. → Parâmetros). A forma de pagamento escolhida no Checkin também é validada contra essa conta.


> ⚠️ Se a conta configurada nesse parâmetro não aceitar a forma de pagamento escolhida no Checkin (por exemplo, o parâmetro apontando para o CAIXA e o paciente pagando no cartão), o Checkin é recusado com uma mensagem indicando o parâmetro e a tela de Conta Financeira para ajuste. Por isso, aponte o parâmetro para uma conta que aceite todas as formas usadas na recepção.

## Excluir uma conta financeira

O botão vermelho (lixeira) exclui a conta — desde que ela nunca tenha sido usada. Uma conta com movimentos financeiros não pode ser excluída, para não perder o histórico. O sistema explica o motivo e sugere o caminho correto: alterar o cadastro para Inativo.



> ⚠️ Também não é possível excluir a conta que estiver configurada no parâmetro IdContaFinanceiraCheckin: primeiro troque o parâmetro para outra conta.

## Atenção: usuários com "Controla Caixa"

Se o usuário logado tem a opção Controla Caixa marcada no cadastro de acesso, qualquer baixa de Conta a Receber/Pagar exige que ele tenha o caixa aberto (Caixa → Meu caixa). Sem o caixa aberto, a baixa é recusada com mensagem específica — independentemente da Conta Financeira escolhida. Veja o manual do Módulo de Caixa.

