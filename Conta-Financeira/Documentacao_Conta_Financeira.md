# Cadastro de Conta Financeira

_O que é, onde é usada e a validação Conta Financeira x Forma de Pagamento_

Versão 1.0 — 18/09/2026

A Conta Financeira é o "cofre" onde o dinheiro da clínica realmente entra e sai: uma conta bancária (Banco do Brasil, Sicoob, etc.) ou o próprio caixa em dinheiro. Toda baixa (recebimento ou pagamento) informa em qual conta o valor caiu ou de qual conta ele saiu — é isso que permite conferir o extrato do banco, saber o saldo de cada conta e montar o Fluxo de Caixa. Este manual explica o cadastro, onde ele é usado e, principalmente, a regra que amarra cada Conta Financeira às Formas de Pagamento permitidas nela.

Assista ao vídeo narrado desta rotina: [https://youtu.be/er1uv0qlUjk](https://youtu.be/er1uv0qlUjk)
---

## O que é e para que serve

Cada Conta Financeira representa um lugar onde existe saldo. Exemplos: "BANCO BRASIL" (conta corrente da clínica), "SICOOB CONTA CORRENTE" ou "CAIXA" (o dinheiro em espécie na recepção). Sem Conta Financeira o sistema não sabe onde o dinheiro foi parar, e por isso ela é obrigatória em toda baixa de Conta a Pagar e de Conta a Receber, e também na baixa automática do Checkin.

O cadastro fica em Financeiro → Cadastros → Contas Financeiras (acesso do administrador).

![Lista de Contas Financeiras. A coluna "Tipo" mostra "Banco" quando a conta tem dados bancários e "Caixa" quando é uma conta sem banco (dinheiro em espécie).](00-lista-contas-financeiras.png)

_Lista de Contas Financeiras. A coluna "Tipo" mostra "Banco" quando a conta tem dados bancários e "Caixa" quando é uma conta sem banco (dinheiro em espécie)._

## Cadastrando uma conta nova

Clique em Novo e preencha. Só a Descrição é obrigatória; os demais campos são opcionais e servem para identificar a conta bancária.

![Modal "Nova Conta Financeira" preenchido como conta bancária (Banco do Brasil, agência 0001, conta 12345-6 e chave PIX).](10-novo-cadastro-completo.png)

_Modal "Nova Conta Financeira" preenchido como conta bancária (Banco do Brasil, agência 0001, conta 12345-6 e chave PIX)._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Descrição * | Nome que aparece em todas as telas de baixa, movimentos e fluxo de caixa. Sempre gravado em maiúsculas. | ContaFinanceira.Descricao |
| Banco | Banco da conta (lista de bancos cadastrados). Deixe em branco para uma conta do tipo Caixa. | ContaFinanceira.IdBanco |
| Agência | Agência bancária (até 20 caracteres). | ContaFinanceira.Agencia |
| Conta | Número da conta (até 30 caracteres). | ContaFinanceira.Conta |
| Chave PIX | Chave PIX da conta, só para consulta/identificação. | ContaFinanceira.ChavePix |
| Ativo (só ao editar) | Conta inativa deixa de ser oferecida nas telas de baixa (só contas ativas aparecem na lista), mas o histórico é mantido. | ContaFinanceira.Ativo |
| Tipo (badge Banco/Caixa) | Não é um campo: aparece como "Banco" se Banco/Agência/Conta estiverem preenchidos e como "Caixa" caso contrário. | Calculado na tela (conta-financeira-painel) |

![Conta "SICOOB CONTA CORRENTE" salva e já listada, com o tipo "Banco".](11-lista-com-conta-nova.png)

_Conta "SICOOB CONTA CORRENTE" salva e já listada, com o tipo "Banco"._

![Ao editar, aparece também o campo "Ativo" (Ativo/Inativo).](13-editar-conta.png)

_Ao editar, aparece também o campo "Ativo" (Ativo/Inativo)._

> ⚠️ Uma conta Inativa é a forma correta de "aposentar" uma conta que já teve movimento: ela some das telas de baixa, mas o histórico de movimentos continua íntegro.

## Onde a Conta Financeira é usada

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Contas a Pagar — baixa | Campo Conta Financeira (obrigatório): de qual conta o dinheiro saiu. Gera um movimento de Saída na conta. | ContaPagarBaixaRepository.cs |
| Contas a Receber — baixa | Campo Conta Financeira (obrigatório na tela: "Informe a conta financeira"): em qual conta o dinheiro entrou. Gera um movimento de Entrada na conta. | ContaReceberBaixaRepository.cs |
| Checkin de Paciente | A baixa automática do pagamento feito no Checkin usa a conta definida no parâmetro IdContaFinanceiraCheckin. | CheckinRepository.cs / Parametro |
| Movimentos Financeiros | Extrato de todas as entradas/saídas, com filtro por conta. Também permite Nova Transferência entre duas contas. | MovimentoFinanceiro |
| Fluxo de Caixa e Dashboard | Saldo, entradas e saídas por conta (quadro "Por Conta Financeira"). | MovimentoFinanceiro |

![Movimentos Financeiros filtrado pela conta "CAIXA": só aparecem os lançamentos que passaram por ela (uma entrada de Conta a Receber e uma saída de Conta a Pagar).](22-movimentos-filtrado-caixa.png)

_Movimentos Financeiros filtrado pela conta "CAIXA": só aparecem os lançamentos que passaram por ela (uma entrada de Conta a Receber e uma saída de Conta a Pagar)._

![Fluxo de Caixa: o quadro "Por Conta Financeira" (no rodapé) mostra entradas, saídas e resultado de cada conta cadastrada.](21-fluxo-caixa.png)

_Fluxo de Caixa: o quadro "Por Conta Financeira" (no rodapé) mostra entradas, saídas e resultado de cada conta cadastrada._

## Validação Conta Financeira x Forma de Pagamento

Nem toda forma de pagamento faz sentido em toda conta. Uma máquina de cartão, por exemplo, deposita na conta bancária — não existe "Cartão de Crédito" dentro da gaveta de dinheiro do caixa. Por isso cada Conta Financeira tem a sua própria lista de Formas de Pagamento permitidas, e o sistema recusa qualquer baixa que combine uma forma com uma conta em que ela não foi habilitada.

Essa regra vale em três lugares: baixa de Conta a Receber, baixa de Conta a Pagar e pagamento do Checkin.

## Como configurar (passo a passo)

Passo 1 — Formas de pagamento da clínica. Em Tabelas Aux. → Formas de Pagamento ficam as formas com as quais a clínica trabalha (Cartão de Crédito, Débito, Cheque, Dinheiro, Pix). Só as formas ativas aqui são oferecidas nas telas de baixa e servem de sugestão inicial para as contas novas.

![Formas de Pagamento da clínica: neste exemplo Cartão de Crédito, Dinheiro e Pix estão ativos; Cartão de Débito e Cheque estão desativados.](23-formas-pagamento-clinica.png)

_Formas de Pagamento da clínica: neste exemplo Cartão de Crédito, Dinheiro e Pix estão ativos; Cartão de Débito e Cheque estão desativados._

Passo 2 — Formas permitidas em cada conta. Na lista de Contas Financeiras, clique no botão azul "Formas de pagamento desta conta" (ícone de cheque) da linha desejada. Cada forma tem um botão: Desabilitar (vermelho) quando está permitida e Habilitar (verde) quando não está.

![Formas de pagamento da conta nova "SICOOB": ao criar uma conta, o sistema já habilita todas as formas que estão ativas na clínica (Crédito, Dinheiro e Pix). Basta desabilitar as que não se aplicam.](12-formas-conta-nova.png)

_Formas de pagamento da conta nova "SICOOB": ao criar uma conta, o sistema já habilita todas as formas que estão ativas na clínica (Crédito, Dinheiro e Pix). Basta desabilitar as que não se aplicam._

![Conta "CAIXA" com Cartão de Crédito, Dinheiro e Pix habilitados.](02-formas-pagamento-antes.png)

_Conta "CAIXA" com Cartão de Crédito, Dinheiro e Pix habilitados._

![Depois de clicar em "Desabilitar" no Cartão de Crédito: a conta CAIXA passa a aceitar só Dinheiro e Pix.](03-formas-pagamento-depois.png)

_Depois de clicar em "Desabilitar" no Cartão de Crédito: a conta CAIXA passa a aceitar só Dinheiro e Pix._

> ⚠️ Ao criar uma conta, o sistema já a deixa com todas as formas ativas da clínica habilitadas — é uma sugestão inicial. Confira sempre a lista e desabilite o que não se aplica àquela conta (ex.: cartão em uma conta "Caixa").

## Exemplo prático: o que acontece na tela

Exemplo 1 — Combinação não permitida (Conta a Receber). Com a conta CAIXA aceitando apenas Dinheiro e Pix, tentamos receber R$ 1,00 escolhendo Método Pagto = Cartão de Crédito e Conta Financeira = CAIXA. O sistema recusa e mostra a orientação de como resolver.

![Baixa recusada: "Esta forma de pagamento não está habilitada para a conta financeira selecionada. Configure essa relação na tela de Conta Financeira."](05-erro-forma-nao-habilitada.png)

_Baixa recusada: "Esta forma de pagamento não está habilitada para a conta financeira selecionada. Configure essa relação na tela de Conta Financeira."_

Exemplo 2 — Combinação permitida. Trocando o método para Dinheiro (que a conta CAIXA aceita), a baixa é gravada normalmente e passa a aparecer no extrato da conta.

![Baixa de R$ 1,00 em Dinheiro na conta CAIXA gravada com sucesso (aviso "Salvo" e a nova linha na lista de acertos).](07-baixa-com-sucesso.png)

_Baixa de R$ 1,00 em Dinheiro na conta CAIXA gravada com sucesso (aviso "Salvo" e a nova linha na lista de acertos)._

Exemplo 3 — Mesma regra em Contas a Pagar. A baixa de uma Conta a Pagar com Cartão de Crédito saindo do CAIXA é recusada com a mesma mensagem. Aqui a Conta Financeira é obrigatória (asterisco vermelho no campo). Em Contas a Receber a tela também exige a conta, mesmo sem o asterisco.

![Conta a Pagar: Cartão de Crédito na conta CAIXA recusado com a mensagem de forma não habilitada.](26-contapagar-erro-forma-nao-habilitada.png)

_Conta a Pagar: Cartão de Crédito na conta CAIXA recusado com a mensagem de forma não habilitada._

> ⚠️ Se aparecer essa mensagem no dia a dia, há duas saídas: escolher outra Conta Financeira que aceite aquela forma (ex.: a conta bancária, para cartão) ou habilitar a forma na conta desejada pelo botão "Formas de pagamento desta conta".

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Regra de validação | Ao gravar a baixa, o sistema consulta se existe o par (Conta Financeira, Forma de Pagamento) habilitado. Se não existir, recusa e não grava nada. | ContaFinanceiraPagamentoForma |
| Onde é conferida | Baixa de Conta a Receber, baixa de Conta a Pagar e pagamento do Checkin (que usa a conta do parâmetro IdContaFinanceiraCheckin). | ContaReceberBaixaRepository.cs / ContaPagarBaixaRepository.cs / CheckinRepository.cs |

## Conta Financeira do Checkin

O pagamento feito no Checkin do paciente gera uma Conta a Receber e sua baixa automática. Como não existe um campo para o recepcionista escolher a conta, o sistema usa a definida no parâmetro IdContaFinanceiraCheckin (Tabelas Aux. → Parâmetros). A forma de pagamento escolhida no Checkin também é validada contra essa conta.

![Tela de Parâmetros: a linha "Conta financeira usada na baixa automática do ContaReceber gerado pelo Checkin" aponta para "BANCO BRASIL".](24-parametro-conta-financeira-checkin.png)

_Tela de Parâmetros: a linha "Conta financeira usada na baixa automática do ContaReceber gerado pelo Checkin" aponta para "BANCO BRASIL"._

> ⚠️ Se a conta configurada nesse parâmetro não aceitar a forma de pagamento escolhida no Checkin (por exemplo, o parâmetro apontando para o CAIXA e o paciente pagando no cartão), o Checkin é recusado com uma mensagem indicando o parâmetro e a tela de Conta Financeira para ajuste. Por isso, aponte o parâmetro para uma conta que aceite todas as formas usadas na recepção.

## Excluir uma conta financeira

O botão vermelho (lixeira) exclui a conta — desde que ela nunca tenha sido usada. Uma conta com movimentos financeiros não pode ser excluída, para não perder o histórico. O sistema explica o motivo e sugere o caminho correto: alterar o cadastro para Inativo.

![Tentativa de excluir a conta CAIXA (que já tem movimentos): o sistema recusa e orienta a usar o status Inativo.](15-resultado-exclusao-caixa.png)

_Tentativa de excluir a conta CAIXA (que já tem movimentos): o sistema recusa e orienta a usar o status Inativo._

![Conta "SICOOB" (criada agora, sem nenhum movimento) excluída com sucesso ("Removido!").](17-exclusao-conta-sem-movimentos-ok.png)

_Conta "SICOOB" (criada agora, sem nenhum movimento) excluída com sucesso ("Removido!")._

> ⚠️ Também não é possível excluir a conta que estiver configurada no parâmetro IdContaFinanceiraCheckin: primeiro troque o parâmetro para outra conta.

## Atenção: usuários com "Controla Caixa"

Se o usuário logado tem a opção Controla Caixa marcada no cadastro de acesso, qualquer baixa de Conta a Receber/Pagar exige que ele tenha o caixa aberto (Caixa → Meu caixa). Sem o caixa aberto, a baixa é recusada com mensagem específica — independentemente da Conta Financeira escolhida. Veja o manual do Módulo de Caixa.

![Baixa recusada porque o usuário controla caixa e não há caixa aberto: "Nenhum caixa aberto para o usuário. Abra o caixa antes de registrar o recebimento."](09-erro-caixa-fechado.png)

_Baixa recusada porque o usuário controla caixa e não há caixa aberto: "Nenhum caixa aberto para o usuário. Abra o caixa antes de registrar o recebimento."_
