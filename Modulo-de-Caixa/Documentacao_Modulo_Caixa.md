# Módulo de Caixa

_Abertura, lançamentos, fechamento, solicitações de cancelamento e histórico_

Versão 1.0 — 18/09/2026

O módulo Caixa controla o dinheiro/valores que passam pela mão de cada atendente durante o dia: abertura com um fundo de troco, recebimentos e pagamentos feitos enquanto ele está aberto, sangrias/suprimentos manuais, e o fechamento no fim do expediente. Cada usuário tem o seu próprio caixa — não é um caixa único da clínica nem por consultório —, e mais de um atendente pode estar com o caixa aberto ao mesmo tempo.

Assista ao vídeo narrado desta rotina: [https://youtu.be/n7F19sn_uXs](https://youtu.be/n7F19sn_uXs)
---

## Abrindo o caixa

Em Caixa → Meu caixa, se você ainda não tem um caixa aberto, aparece o botão "Abrir Caixa". É informado apenas o valor inicial (fundo de troco) em dinheiro — não há mais nenhum outro dado a preencher na abertura.

![Tela "Meu caixa" com o caixa fechado: badge "CAIXA FECHADO" e botão "Abrir Caixa".](00-meu-caixa-inicial.png)

_Tela "Meu caixa" com o caixa fechado: badge "CAIXA FECHADO" e botão "Abrir Caixa"._

![Modal de Abertura de Caixa com o valor inicial preenchido (R$ 100,00).](02-abrir-caixa-preenchido.png)

_Modal de Abertura de Caixa com o valor inicial preenchido (R$ 100,00)._

![Caixa aberto: badge fica verde ("CAIXA ABERTO"), com a aba "Extrato" e o botão "Novo Lançamento".](03-caixa-aberto-extrato-vazio.png)

_Caixa aberto: badge fica verde ("CAIXA ABERTO"), com a aba "Extrato" e o botão "Novo Lançamento"._

> ⚠️ Só é possível ter um caixa aberto por usuário de cada vez — o sistema bloqueia abrir um segundo caixa enquanto o anterior não for fechado (ou reaberto por um administrador).

## Lançamentos manuais: Suprimento e Sangria

Com o caixa aberto, clique em "Novo Lançamento" para registrar uma entrada extra de dinheiro (Suprimento) ou uma retirada (Sangria) — por exemplo, reforçar o troco ou retirar dinheiro para um depósito. Escolha o tipo, a forma de pagamento, uma observação e o valor.

![Lançamento de Suprimento: forma de pagamento Dinheiro, valor R$ 50,00, com observação.](05-lancamento-suprimento-preenchido.png)

_Lançamento de Suprimento: forma de pagamento Dinheiro, valor R$ 50,00, com observação._

![Lançamento salvo e refletido no Extrato do caixa, com o ícone verde de entrada.](07-extrato-com-suprimento.png)

_Lançamento salvo e refletido no Extrato do caixa, com o ícone verde de entrada._

> ⚠️ Suprimento só pode ser feito em Dinheiro — o sistema bloqueia qualquer outra forma de pagamento para esse tipo de lançamento (testado ao vivo: tentar suprimento em Cartão de Crédito é recusado com a mensagem "Suprimento só pode ser feito em dinheiro"). Já a Sangria também é sempre validada contra o saldo em espécie disponível no caixa — não é possível retirar mais dinheiro do que existe.

## Recebimentos e pagamentos aparecem automaticamente

A grande vantagem do caixa é que ele não precisa de lançamento manual para registrar dinheiro que já entrou ou saiu pelo sistema: toda baixa de Conta a Receber ou Conta a Pagar feita enquanto seu caixa está aberto entra automaticamente no extrato dele — não existe um passo extra de "lançar no caixa" depois de dar baixa numa conta.

![Dando baixa numa Conta a Receber (tela normal de Contas a Receber) com o caixa aberto.](08b-modal-baixa-preenchida.png)

_Dando baixa numa Conta a Receber (tela normal de Contas a Receber) com o caixa aberto._

![De volta em "Meu caixa": a baixa aparece automaticamente no Extrato, como uma entrada em nome do paciente — sem nenhum lançamento manual adicional.](10-extrato-com-entrada-refletida.png)

_De volta em "Meu caixa": a baixa aparece automaticamente no Extrato, como uma entrada em nome do paciente — sem nenhum lançamento manual adicional._

> ⚠️ Isso só acontece para usuários com a opção "Controla Caixa" marcada no cadastro de acesso dele (Admin → Acessos). Se essa opção estiver desmarcada, o usuário consegue dar baixa em Contas a Receber/Pagar normalmente mesmo sem caixa aberto, e essas baixas não aparecem em nenhum caixa. Já um usuário com "Controla Caixa" marcado é obrigado a ter um caixa aberto para registrar qualquer recebimento — sem isso, o sistema recusa com a mensagem "Nenhum caixa aberto para o usuário".

## Fechando o caixa

Clique em "Fechar Caixa". O sistema mostra um resumo com todas as Entradas (valor de abertura + suprimentos + recebimentos, agrupados por forma de pagamento) e Saídas (sangrias + pagamentos), e calcula o saldo final em espécie, em cheque e o saldo geral.

![Resumo do fechamento: Entradas, Saídas e o Saldo do caixa calculado (em espécie, em cheque e geral).](17-bloqueio-fechar-com-solicitacao-pendente.png)

_Resumo do fechamento: Entradas, Saídas e o Saldo do caixa calculado (em espécie, em cheque e geral)._

![Confirmação "Caixa Fechado!" — badge volta a ficar cinza/fechado e o botão "Abrir Caixa" reaparece.](15-apos-fechar-caixa.png)

_Confirmação "Caixa Fechado!" — badge volta a ficar cinza/fechado e o botão "Abrir Caixa" reaparece._

> ⚠️ O fechamento do ClinSis é totalmente calculado pelo sistema — não existe uma etapa de "contar o dinheiro físico" e digitar um valor diferente para comparar com o esperado (não há registro de sobra/quebra de caixa). O valor de fechamento gravado é sempre exatamente igual ao saldo calculado pelas entradas e saídas do próprio caixa.

## Solicitação de cancelamento de lançamento

Um lançamento manual (Suprimento/Sangria) pode ser cancelado, mas não diretamente — quem lançou clica em "Cancelar" na linha do Extrato para solicitar o cancelamento; só um administrador, na tela Caixa → Solicitações, efetiva o cancelamento de fato.

![Solicitando o cancelamento de um lançamento de Suprimento a partir do Extrato.](12-confirmar-solicitar-cancelamento.png)

_Solicitando o cancelamento de um lançamento de Suprimento a partir do Extrato._

![Tela "Solicitações de cancelamento" (acesso só do administrador): lista as solicitações pendentes de todos os usuários.](18-solicitacoes-pendentes.png)

_Tela "Solicitações de cancelamento" (acesso só do administrador): lista as solicitações pendentes de todos os usuários._

![Depois de aprovado pelo administrador, o lançamento some da lista de pendentes.](20-solicitacoes-apos-aprovar.png)

_Depois de aprovado pelo administrador, o lançamento some da lista de pendentes._

> ⚠️ Enquanto existir uma solicitação de cancelamento pendente naquele caixa, o fechamento fica bloqueado — o sistema recusa com a mensagem "Não é possível fechar. Existe solicitação pendente de cancelamento". É preciso que um administrador aprove (ou o próprio usuário desfaça a solicitação, botão "Desfazer Cancelar") antes de conseguir fechar o caixa.

## Histórico de caixas

Em Caixa → Listar, é possível consultar caixas já abertos/fechados, filtrando por usuário e por período (é preciso informar usuário ou um intervalo de datas). Atendentes só veem os próprios caixas; administradores podem consultar de qualquer usuário.

![Histórico de caixas do usuário, com valor de fechamento e valor em espécie de cada um.](23-listar-historico-caixas.png)

_Histórico de caixas do usuário, com valor de fechamento e valor em espécie de cada um._

![Extrato de um caixa já fechado, acessado pelo botão "Extrato" — mesmo layout do extrato do caixa aberto.](22-extrato-caixa-fechado.png)

_Extrato de um caixa já fechado, acessado pelo botão "Extrato" — mesmo layout do extrato do caixa aberto._

> ⚠️ Reabrir um caixa já fechado só pode ser feito por um administrador, e exige informar um motivo (mínimo 5 caracteres) — é a única forma de corrigir um caixa fechado por engano ou com dados incompletos.
