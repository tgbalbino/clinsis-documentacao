# Contrato (sem assinatura digital)

_Ciclo de vida completo: criação, fechamento, geração de Conta a Receber, renovação e aviso de vencimento_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Contrato/Documentacao_Contrato_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/szRnAwHrqI4?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/szRnAwHrqI4)

## Conteúdo completo do manual

---


_Ciclo de vida completo: criação, fechamento, geração de Conta a Receber, renovação e aviso de vencimento_

Versão 1.1 — 29/09/2026

Contrato formaliza um pacote de sessões vendido ao paciente (ex.: "10 sessões de Fisioterapia"), com um valor total e uma ou mais condições de pagamento (à vista, parcelado no cartão, etc.). Diferente de um agendamento avulso, o Contrato tem um ciclo de vida com fases — criado, assinado, fechado — e, uma vez fechado, gera automaticamente as parcelas em Contas a Receber. Este manual cobre a versão sem assinatura digital (assinatura "no papel", marcada manualmente no sistema); a versão com assinatura eletrônica pela D4Sign é documentada à parte.


---

> ⚠️ Para o contrato poder ser fechado/impresso, a clínica precisa ter um Layout de Contrato ativo configurado (o modelo/template que vira o PDF) — veja o manual separado "Layout de Contrato" para essa configuração.

## As fases do Contrato

O Contrato não tem um único campo de "status" — a fase em que ele está é resultado da combinação de algumas informações: se está Ativo, se já foi Assinado, se já foi Fechado e, depois de fechado, se está pendente de renovação. Na prática, um contrato passa pelas seguintes fases:

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Criado | Contrato recém-cadastrado. Serviços e condição de pagamento podem ser editados livremente. |
| Assinado | Marcado manualmente como assinado "no papel" (sem D4Sign). A partir daqui, os dados do contrato não podem mais ser alterados. |
| Fechado | Botão "Fechar Contrato" acionado: gera as parcelas em Contas a Receber e trava o contrato definitivamente. |
| Cancelado | Pode acontecer a qualquer momento antes de Fechado, desmarcando "Ativo" na edição do contrato. É definitivo — não existe botão para reativar. |
| Vencendo / Renovado / Não vai renovar | Só depois de Fechado: controla se aquele contrato já venceu (ou está perto de vencer) e o que a clínica decidiu fazer a respeito. |

> ⚠️ Um contrato assinado não pode mais ser editado — nem os serviços, nem a condição de pagamento. Revise tudo com atenção antes de marcar como assinado.

## Criando um contrato

Em Contrato (menu lateral), clique em Novo, escolha o paciente pela lupa e preencha a Data de Emissão (obrigatória). Depois de salvar, o contrato passa a existir (fase Criado) e as seções de Serviços e Acertos/Pagamentos ficam disponíveis.


O botão Filtros permite localizar contratos pelo número do contrato, além de paciente, período e situação.




## Adicionando Serviços

Na aba "Dados do Contrato", a seção Serviços lista o que o paciente está contratando. Clique em Novo, pesquise o serviço, informe a quantidade de sessões e o valor por sessão — o Valor Total é calculado automaticamente.




## Condição de Pagamento (Acertos/Pagamentos)

Na aba "Acertos / Pagamentos", cadastre como o paciente vai pagar. Você pode combinar mais de um acerto no mesmo contrato (por exemplo, parte em Pix e o restante no Crediário). Os campos mudam conforme a Forma de Pagamento escolhida:

| Forma | O que informar | Título gerado em Contas a Receber |
|---|---|---|
| Crediário | Valor, número de parcelas, data da 1ª e da Última Parcela e, se houver, a Taxa de Juros Mensal. | Uma parcela por mês. |
| Cartão de Crédito | Valor, quantas vezes foi passado no cartão (até o máximo aceito pela clínica) e a Data do Pagamento. | Um único título com o valor total. |
| Dinheiro, Pix, Cartão de Débito e demais | Valor e Data do Pagamento (por padrão, hoje). | Um único título com o valor total. |

O Crediário é a única forma que parcela o pagamento do paciente. As demais são à vista. Para parcelar em Dinheiro ou Pix, use o Crediário.

A soma de todas as condições de pagamento precisa bater exatamente com o total dos Serviços para o contrato poder ser fechado — o card "Falta Acertar" mostra a diferença em tempo real.

> ℹ️ O acerto é a condição combinada com o paciente, não o recebimento. O dinheiro só entra no caixa ou na conta financeira quando a parcela é baixada em Contas a Receber, informando como o paciente realmente pagou. O Crediário não aparece nas telas de baixa, porque ele é uma condição do contrato e não um meio de pagamento.



## Assinatura eletrônica, dispensa ou assinatura em papel

Depois de salvar, o topo do contrato mostra a opção Assinatura eletrônica (D4Sign), com dois botões: "Assinar pela D4Sign" e "Não assinar". O valor inicial segue o padrão da clínica (parâmetro de assinatura). Se a clínica assina pela D4Sign, o contrato é enviado pelo botão "Enviar para assinatura" e o fluxo segue como no manual de Contrato com D4Sign. Se este contrato não vai ser assinado eletronicamente, clique em Não assinar.


Dispensar a assinatura exige liberação administrativa: quem é Administrador escolhe apenas o Motivo (lista de motivos cadastrada); os demais usuários precisam informar também o login e a senha de um Administrador. A dispensa fica registrada no contrato (quem dispensou, quem liberou, quando e o motivo).



Se a clínica prefere registrar a assinatura no papel, na listagem de Contratos clique no botão de caneta/download da linha e, no modal que abre, em "Marcar como assinado" (esse botão só aparece se o contrato ainda não estiver assinado). O mesmo modal permite baixar o PDF do contrato para impressão e assinatura física.


## Fechando o Contrato (gera a Conta a Receber)

Com o contrato assinado (ou mesmo sem assinar, se a clínica não exigir isso), abra-o de novo e clique em Fechar Contrato. O botão só fica habilitado se houver pelo menos um Serviço, pelo menos uma condição de Pagamento, e a diferença entre os dois totais for zero. Ao confirmar, o sistema gera, de uma só vez, os títulos em Contas a Receber — uma parcela por mês para cada acerto em Crediário e um único título para cada acerto à vista ou no cartão — e o contrato fica travado definitivamente (nunca mais pode ser editado).




> ⚠️ Só é possível fechar um contrato se dois parâmetros de sistema estiverem configurados para a clínica: Plano de Conta do Contrato e Centro de Custo do Contrato (tela de Parâmetros). São eles que definem em qual Plano de Conta/Centro de Custo as parcelas geradas vão cair em Contas a Receber.

## Aviso de vencimento (contratos "vencendo")

Uma vez por dia (de madrugada), o sistema verifica todos os contratos já fechados e ainda não renovados, e gera um aviso para a equipe administrativa quando a última parcela cadastrada estiver perto de vencer (por padrão, até 30 dias antes). Esse aviso aparece como uma notificação no sino no canto superior direito do sistema, com um balão mostrando o contrato e o paciente — clicar nele leva direto para a lista de contratos vencendo.


## Configurando quantos dias de antecedência do aviso

O prazo de antecedência do aviso é configurável por clínica, em Tabelas Aux. → Parâmetros, no parâmetro DiasAvisoVencContrato ("Quantos dias antes do vencimento do plano o sistema avisa o financeiro que o Contrato está vencendo") — se não for configurado, o sistema usa 30 dias como padrão. No exemplo abaixo, está configurado para 30 dias.



> ⚠️ Este é um aviso interno, para a equipe agir — ligar para o paciente, mandar mensagem por fora do sistema, negociar a renovação. Nesta versão sem D4Sign, o sistema não envia nenhuma notificação automática (e-mail/WhatsApp) diretamente ao paciente ou responsável sobre o contrato.

## Renovando um contrato

Com o contrato fechado e ainda não renovado, o botão Renovar fica disponível. Ao confirmar, o sistema cria um contrato novo, copiando os mesmos Serviços e a mesma condição de Pagamento do contrato original — mas com as datas deslocadas: os acertos em Crediário continuam no mês seguinte ao da última parcela do contrato antigo, e os acertos à vista ou no cartão passam a ter a data de hoje. O contrato antigo não é alterado (continua fechado, com suas parcelas já geradas intactas); ele só ganha a marca "Renovado" e some da lista de vencendo. O novo contrato nasce na fase "Criado" — revise os dados e feche-o normalmente quando estiver pronto.



## Quando o paciente não vai renovar

Se a equipe já sabe que o paciente não vai continuar, em vez de Renovar, clique em Não vai renovar. Isso não cria contrato nenhum — apenas marca o contrato atual com esse status e para de gerar o aviso de vencimento para ele.


