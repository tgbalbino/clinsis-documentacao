# Módulo de Caixa

_Abertura, lançamentos, fechamento, solicitações de cancelamento e histórico_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Modulo-de-Caixa/Documentacao_Modulo_Caixa_Simplificado.pdf)

## Vídeo narrado

- [▶️ Assistir o vídeo no YouTube](https://youtu.be/n7F19sn_uXs)

## Conteúdo completo do manual

*As capturas de tela deste trecho estão no PDF acima — aqui fica só o texto.*

---


_Abertura, lançamentos, fechamento, solicitações de cancelamento e histórico_

Versão 1.0 — 18/09/2026

O módulo Caixa controla o dinheiro/valores que passam pela mão de cada atendente durante o dia: abertura com um fundo de troco, recebimentos e pagamentos feitos enquanto ele está aberto, sangrias/suprimentos manuais, e o fechamento no fim do expediente. Cada usuário tem o seu próprio caixa — não é um caixa único da clínica nem por consultório —, e mais de um atendente pode estar com o caixa aberto ao mesmo tempo.

Assista ao vídeo narrado desta rotina: [https://youtu.be/n7F19sn_uXs](https://youtu.be/n7F19sn_uXs)
---

## Abrindo o caixa

Em Caixa → Meu caixa, se você ainda não tem um caixa aberto, aparece o botão "Abrir Caixa". É informado apenas o valor inicial (fundo de troco) em dinheiro — não há mais nenhum outro dado a preencher na abertura.




> ⚠️ Só é possível ter um caixa aberto por usuário de cada vez — o sistema bloqueia abrir um segundo caixa enquanto o anterior não for fechado (ou reaberto por um administrador).

## Lançamentos manuais: Suprimento e Sangria

Com o caixa aberto, clique em "Novo Lançamento" para registrar uma entrada extra de dinheiro (Suprimento) ou uma retirada (Sangria) — por exemplo, reforçar o troco ou retirar dinheiro para um depósito. Escolha o tipo, a forma de pagamento, uma observação e o valor.



> ⚠️ Suprimento só pode ser feito em Dinheiro — o sistema bloqueia qualquer outra forma de pagamento para esse tipo de lançamento (testado ao vivo: tentar suprimento em Cartão de Crédito é recusado com a mensagem "Suprimento só pode ser feito em dinheiro"). Já a Sangria também é sempre validada contra o saldo em espécie disponível no caixa — não é possível retirar mais dinheiro do que existe.

## Recebimentos e pagamentos aparecem automaticamente

A grande vantagem do caixa é que ele não precisa de lançamento manual para registrar dinheiro que já entrou ou saiu pelo sistema: toda baixa de Conta a Receber ou Conta a Pagar feita enquanto seu caixa está aberto entra automaticamente no extrato dele — não existe um passo extra de "lançar no caixa" depois de dar baixa numa conta.



> ⚠️ Isso só acontece para usuários com a opção "Controla Caixa" marcada no cadastro de acesso dele (Admin → Acessos). Se essa opção estiver desmarcada, o usuário consegue dar baixa em Contas a Receber/Pagar normalmente mesmo sem caixa aberto, e essas baixas não aparecem em nenhum caixa. Já um usuário com "Controla Caixa" marcado é obrigado a ter um caixa aberto para registrar qualquer recebimento — sem isso, o sistema recusa com a mensagem "Nenhum caixa aberto para o usuário".

## Fechando o caixa

Clique em "Fechar Caixa". O sistema mostra um resumo com todas as Entradas (valor de abertura + suprimentos + recebimentos, agrupados por forma de pagamento) e Saídas (sangrias + pagamentos), e calcula o saldo final em espécie, em cheque e o saldo geral.



> ⚠️ O fechamento do ClinSis é totalmente calculado pelo sistema — não existe uma etapa de "contar o dinheiro físico" e digitar um valor diferente para comparar com o esperado (não há registro de sobra/quebra de caixa). O valor de fechamento gravado é sempre exatamente igual ao saldo calculado pelas entradas e saídas do próprio caixa.

## Solicitação de cancelamento de lançamento

Um lançamento manual (Suprimento/Sangria) pode ser cancelado, mas não diretamente — quem lançou clica em "Cancelar" na linha do Extrato para solicitar o cancelamento; só um administrador, na tela Caixa → Solicitações, efetiva o cancelamento de fato.




> ⚠️ Enquanto existir uma solicitação de cancelamento pendente naquele caixa, o fechamento fica bloqueado — o sistema recusa com a mensagem "Não é possível fechar. Existe solicitação pendente de cancelamento". É preciso que um administrador aprove (ou o próprio usuário desfaça a solicitação, botão "Desfazer Cancelar") antes de conseguir fechar o caixa.

## Histórico de caixas

Em Caixa → Listar, é possível consultar caixas já abertos/fechados, filtrando por usuário e por período (é preciso informar usuário ou um intervalo de datas). Atendentes só veem os próprios caixas; administradores podem consultar de qualquer usuário.



> ⚠️ Reabrir um caixa já fechado só pode ser feito por um administrador, e exige informar um motivo (mínimo 5 caracteres) — é a única forma de corrigir um caixa fechado por engano ou com dados incompletos.
