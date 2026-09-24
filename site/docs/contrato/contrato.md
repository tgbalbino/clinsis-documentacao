# Contrato (sem assinatura digital)

_Ciclo de vida completo: criação, fechamento, geração de Conta a Receber, renovação e aviso de vencimento_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Contrato/Documentacao_Contrato_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/c1ki58j_khQ?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/c1ki58j_khQ)

## Conteúdo completo do manual

---


_Ciclo de vida completo: criação, fechamento, geração de Conta a Receber, renovação e aviso de vencimento_

Versão 1.0 — 18/09/2026

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




## Adicionando Serviços

Na aba "Dados do Contrato", a seção Serviços lista o que o paciente está contratando. Clique em Novo, pesquise o serviço, informe a quantidade de sessões e o valor por sessão — o Valor Total é calculado automaticamente.




## Condição de Pagamento (Acertos/Pagamentos)

Na aba "Acertos / Pagamentos", cadastre como o paciente vai pagar: Forma de Pagamento, Valor, número de Parcelas, data da 1ª e da Última Parcela (e, se for parcelado com juros, a Taxa de Juros Mensal). A soma de todas as condições de pagamento precisa bater exatamente com o total dos Serviços para o contrato poder ser fechado — o card "Falta Acertar" mostra a diferença em tempo real.



## Assinatura (sem D4Sign)

Nesta versão sem assinatura eletrônica, a assinatura é registrada manualmente: na listagem de Contratos, clique no botão de caneta/download da linha do contrato e, no modal que abre, clique em "Marcar como assinado" (esse botão só aparece se o contrato ainda não estiver assinado). O mesmo modal também permite baixar o PDF do contrato para impressão/assinatura física.



## Fechando o Contrato (gera a Conta a Receber)

Com o contrato assinado (ou mesmo sem assinar, se a clínica não exigir isso), abra-o de novo e clique em Fechar Contrato. O botão só fica habilitado se houver pelo menos um Serviço, pelo menos uma condição de Pagamento, e a diferença entre os dois totais for zero. Ao confirmar, o sistema gera, de uma só vez, todas as parcelas em Contas a Receber — uma parcela por mês a partir da 1ª Parcela informada — e o contrato fica travado definitivamente (nunca mais pode ser editado).





> ⚠️ Só é possível fechar um contrato se dois parâmetros de sistema estiverem configurados para a clínica: Plano de Conta do Contrato e Centro de Custo do Contrato (tela de Parâmetros). São eles que definem em qual Plano de Conta/Centro de Custo as parcelas geradas vão cair em Contas a Receber.

## Aviso de vencimento (contratos "vencendo")

Uma vez por dia (de madrugada), o sistema verifica todos os contratos já fechados e ainda não renovados, e gera um aviso para a equipe administrativa quando a última parcela cadastrada estiver perto de vencer (por padrão, até 30 dias antes). Esse aviso aparece como uma notificação no sino no canto superior direito do sistema, com um balão mostrando o contrato e o paciente — clicar nele leva direto para a lista de contratos vencendo.



## Configurando quantos dias de antecedência do aviso

O prazo de antecedência do aviso é configurável por clínica, em Tabelas Aux. → Parâmetros, no parâmetro DiasAvisoVencContrato ("Quantos dias antes do vencimento do plano o sistema avisa o financeiro que o Contrato está vencendo") — se não for configurado, o sistema usa 30 dias como padrão. No exemplo abaixo, está configurado para 30 dias.



> ⚠️ Este é um aviso interno, para a equipe agir — ligar para o paciente, mandar mensagem por fora do sistema, negociar a renovação. Nesta versão sem D4Sign, o sistema não envia nenhuma notificação automática (e-mail/WhatsApp) diretamente ao paciente ou responsável sobre o contrato.

## Renovando um contrato

Com o contrato fechado e ainda não renovado, o botão Renovar fica disponível. Ao confirmar, o sistema cria um contrato novo, copiando os mesmos Serviços e a mesma condição de Pagamento do contrato original — mas com as datas de parcela deslocadas para o mês seguinte ao da última parcela do contrato antigo. O contrato antigo não é alterado (continua fechado, com suas parcelas já geradas intactas); ele só ganha a marca "Renovado" e some da lista de vencendo. O novo contrato nasce na fase "Criado" — revise os dados e feche-o normalmente quando estiver pronto.



## Quando o paciente não vai renovar

Se a equipe já sabe que o paciente não vai continuar, em vez de Renovar, clique em Não vai renovar. Isso não cria contrato nenhum — apenas marca o contrato atual com esse status e para de gerar o aviso de vencimento para ele.


