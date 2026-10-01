# WhatsApp - lembretes e confirmações

Envia lembretes e pedidos de confirmação aos pacientes pelo WhatsApp, reduzindo faltas e horários vagos. Existem dois modos: envio manual, feito pela recepção, e envio automático pela API oficial da Meta. O manual cobre requisitos, configuração, templates, consentimento e acompanhamento dos envios.

## Documentação em PDF

- [📄 Manual em PDF](../assets/WhatsApp/Documentacao_WhatsApp_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/2lvKkYApZFE?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/2lvKkYApZFE)

## Conteúdo completo do manual

---


_Envio manual e envio automático pela API oficial da Meta: requisitos, configuração, templates, consentimento e acompanhamento_

Versão 1.2 — 01/10/2026

O ClinSis avisa os pacientes de seus agendamentos por WhatsApp de duas formas: o envio manual, em que a recepção abre o WhatsApp com a mensagem pronta e envia com um clique, e o envio automático pela API oficial da Meta (WhatsApp Business Platform), em que o sistema envia sozinho o lembrete do dia seguinte e o paciente confirma ou avisa que não poderá ir por um link. Este documento explica as duas formas, o que a clínica precisa ter na Meta, como configurar, como acompanhar e os erros mais comuns.


---

## Visão geral: dois modos de envio

| Modo | Como funciona | Quando usar |
|---|---|---|
| Manual | A recepção abre Enviar lembretes, vê os pacientes agendados de hoje ou de amanhã, clica em Enviar e o WhatsApp do próprio computador ou celular abre com a mensagem pronta. Quem envia é a pessoa. | Clínica sem conta na Meta, ou para casos pontuais. |
| Automático (Meta) | O sistema envia sozinho, no horário configurado, um lembrete com os agendamentos do dia seguinte usando a API oficial da Meta. O paciente confirma pelo botão da mensagem. | Clínica com conta e número comerciais na Meta. Envio em escala e com acompanhamento. |

> ⚠️ Só o perfil Administrador configura. O envio automático exige que o paciente tenha autorizado o recebimento por WhatsApp no cadastro (veja o capítulo de consentimento).

## Onde fica no sistema

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Tabelas Aux. → WhatsApp | Painel com o resumo de mensagens, a definição da mensagem, o envio manual de lembretes e o telefone/chave da integração antiga (WhatsGW). |
| Agenda → Enviar lembretes | Atalho para a tela de envio manual dos lembretes de hoje e de amanhã. |
| Tabelas Aux. → WhatsApp Meta | Configuração do envio automático: conta da Meta, lembrete, filtros, templates, disparos e mensagens. |
| Cadastros → Paciente → Dados principais | Campo Celular para WhatsApp e a autorização de recebimento, logo abaixo dos telefones. |
| Agenda → Respostas WhatsApp (no celular: Mais → Respostas WhatsApp) | Respostas dos pacientes de ontem, hoje e amanhã, com o botão Reenviar para as mensagens que falharam. |


## 1. Envio manual

## Enviar lembretes

No painel, em Lembretes do dia (envio manual), clique em Acessar (ou use o botão Enviar lembretes da Agenda). Escolha a data (as setas mudam o dia; Hoje volta para hoje), se quiser filtre pelo paciente e clique na lupa. A lista mostra cada paciente com o celular e todos os horários e profissionais do dia. O botão verde Enviar abre o WhatsApp no navegador com a mensagem pronta; o envio é feito por você. O envio só é liberado para hoje e para amanhã: nas demais datas a tela serve apenas para consulta e mostra um aviso em amarelo.


## Definir a mensagem

Em Definir mensagem escreva o texto que será usado nos avisos manuais. Os campos entre chaves são trocados automaticamente pelos dados do paciente e do agendamento.


## 2. Envio automático pela Meta: o que a clínica precisa ter

O envio automático usa a WhatsApp Business Platform (Cloud API), o serviço oficial da Meta para empresas. A clínica precisa criar e manter esta estrutura na Meta; o ClinSis apenas usa os dados dela. Você precisa de:

| Item | O que é | Onde criar |
|---|---|---|
| Conta Meta e Portfólio Empresarial | Conta de um responsável da clínica (Facebook) e o portfólio empresarial (Business Portfolio) que representa a clínica. É a "dona" de tudo o mais. | business.facebook.com |
| Aplicativo Meta | Aplicativo do tipo Empresa, com o produto WhatsApp adicionado. É o que gera o acesso à API. | developers.facebook.com/apps |
| Conta do WhatsApp Business (WABA) | Conta que reúne os números e os templates da clínica. Gera o WABA ID. | Painel do aplicativo → WhatsApp → Configuração da API |
| Número de telefone comercial | Número da clínica que será o remetente. Gera o Phone Number ID. | Mesmo painel: "Adicionar número de telefone" |
| Forma de pagamento | Cartão para pagar as mensagens enviadas (a Meta cobra por mensagem de template entregue). | Meta Business Suite → Configurações → Cobrança e pagamentos |
| Token de acesso permanente | Chave que autoriza o ClinSis a enviar mensagens pela conta. Criada por um Usuário do sistema. | Configurações do negócio → Usuários → Usuários do sistema |
| Template aprovado | Modelo de mensagem aprovado pela Meta. Só mensagens de template aprovado podem ser iniciadas pela clínica. | WhatsApp Manager → Modelos de mensagem (ou pelo ClinSis, aba Templates) |

> ⚠️ As telas da Meta mudam com frequência e os nomes dos menus podem variar. Em caso de dúvida, siga a documentação oficial em developers.facebook.com/docs/whatsapp. Este manual não traz imagens do site da Meta porque o acesso exige o login da clínica.

## Sobre o número comercial

| Regra | Detalhe |
|---|---|
| Número da empresa | Use um número que pertença à clínica, com código do país e DDD (por exemplo, +55 32 ...). Pode ser celular ou linha fixa. |
| Precisa receber o código de verificação | A Meta confirma o número por SMS ou por ligação de voz. Linha fixa só funciona pela ligação. |
| Não pode estar em uso no aplicativo WhatsApp | Um número ativo no WhatsApp comum precisa ter a conta excluída antes de ser cadastrado na API. Para o WhatsApp Business (aplicativo) existe a opção de coexistência; confirme as condições com a Meta antes de decidir. |
| Nome de exibição | É o nome que o paciente vê. Precisa ser aprovado e representar a clínica. |
| Limites | Um portfólio novo pode ter poucos números e um limite inicial de conversas por dia. Com a verificação da empresa concluída, os limites aumentam. |

> ⚠️ Use, de preferência, um número exclusivo para o envio automático. Pacientes podem responder a mensagem; quem atende essas respostas deve ser definido pela clínica.

## Passo a passo resumido na Meta

| Passo | O que fazer |
|---|---|
| 1 | Crie ou acesse o Portfólio Empresarial da clínica em business.facebook.com e, se pedido, faça a verificação da empresa. |
| 2 | Em developers.facebook.com/apps crie um aplicativo do tipo Empresa, vinculado a esse portfólio, e adicione o produto WhatsApp. |
| 3 | Em WhatsApp → Configuração da API, adicione o número de telefone, informe o nome de exibição e confirme o código recebido por SMS ou ligação. |
| 4 | Anote o WABA ID e o Phone Number ID mostrados nessa tela. |
| 5 | Cadastre a forma de pagamento na conta do WhatsApp Business. |
| 6 | Nas Configurações do negócio, crie um Usuário do sistema administrador, atribua a ele o aplicativo e a conta do WhatsApp e gere o token sem expiração com as permissões whatsapp_business_messaging, whatsapp_business_management e business_management. Guarde o token em local seguro; ele é mostrado uma única vez. |
| 7 | Informe à equipe do ClinSis o endereço de retorno (webhook) e a chave de verificação que ela fornecer, e cadastre-os no aplicativo em WhatsApp → Configuração → Webhook, assinando o campo messages. É por ele que o sistema recebe entregas, leituras e falhas. |

## 3. Configuração no ClinSis

Em Tabelas Aux. → WhatsApp Meta, aba Configuração. No alto, um quadro de ativação mostra o que ainda falta: WABA ID e Phone Number ID, token salvo, link público de confirmação, template aprovado vinculado ao lembrete, integração ativa e lembrete de agendamento ativo. As etiquetas API e Envio automático indicam se o servidor está pronto e se o envio está ligado.


| Campo | O que informar |
|---|---|
| Integração ativa | Liga ou desliga a integração para a clínica. |
| WABA ID / Phone Number ID / Número de exibição | Dados anotados na Meta (passo 4). O número de exibição é o telefone que o paciente vê. |
| Access token | Token do usuário do sistema (passo 6). Depois de salvo, o campo fica em branco e aparece "Token salvo"; deixe em branco para mantê-lo. Se o ClinSis já fornece um token próprio para a clínica, o campo é opcional e a tela mostra "Usando o token do Clinsis"; para usar o token da própria clínica, cole-o e salve. |
| Lembrete de agendamento (chave) | Liga o lembrete automático. Sem ela nada é enviado. |
| Gerar lembretes às | Horário em que o sistema prepara os lembretes dos agendamentos do dia seguinte (por exemplo, 08:00). |
| Template do lembrete | Template aprovado que será usado. Pelo botão Ver texto vê-se como o paciente o recebe. |

Depois de preencher, clique em Testar conexão para conferir se a Meta aceita os dados e em Salvar configuração.

> ⚠️ O endereço público da página de confirmação, a chave do webhook e o segredo do aplicativo ficam no servidor e são configurados pela equipe técnica do ClinSis. Se o quadro de ativação indicar "API: pendente", solicite essa configuração.


## Filtros: quando não enviar o lembrete

Em Não enviar lembrete quando marque os valores do agendamento que devem ser ignorados: atendimento particular, forma de atendimento, plano, cooparticipativo, especialidades, tipos de marcação, método e programa. Um agendamento que combine com qualquer valor marcado não gera lembrete.


## Quem recebe o lembrete

O lembrete automático é gerado uma vez por dia para os agendamentos do dia seguinte, por paciente: uma única mensagem reúne todos os horários do paciente. Só entram pacientes com WhatsApp autorizado e que não sejam barrados pelos filtros acima. Para o agendamento fixo (semanal), o lembrete só é gerado se existir a agenda do mês da consulta; sem a agenda daquele mês, o horário não gera lembrete. No link de confirmação, cada agendamento aparece como um item próprio.

## Simular próximos envios

O botão Simular próximos envios mostra, antes de salvar, quem receberia o lembrete na próxima geração, considerando os filtros marcados. Dá para trocar a data e pesquisar por nome ou telefone. O aviso em amarelo informa quantos pacientes têm agendamento mas não receberão por não terem a autorização de WhatsApp. A simulação não envia nada.


## 4. Templates

Na Meta, a clínica só pode iniciar uma conversa com um template aprovado. Na aba Templates aparecem os modelos da conta com idioma, categoria e status. Use Sincronizar para trazer da Meta os modelos e a situação atual, e Novo template para criar um modelo e enviá-lo para análise. A coluna Usar na rotina vincula um template aprovado ao lembrete de agendamento.


| Item | Explicação |
|---|---|
| Categoria | Utilidade (avisos sobre algo já contratado, como um agendamento), Marketing (promoções) ou Autenticação. O lembrete deve ser de Utilidade. |
| Status | Em análise (a Meta responde em até cerca de 24 horas), Aprovado ou Rejeitado. Só template aprovado envia. |
| Variáveis | O lembrete usa quatro: 1 nome do paciente, 2 nome da clínica, 3 data dos agendamentos, 4 horários e profissionais. |
| Botão | O template de confirmação tem o botão Confirmar meus horários, que abre a página pública de confirmação. |
| Texto fixo | O texto aprovado não pode ser alterado. Para mudar, crie um novo template e vincule-o. |
| Testar | Envia o template escolhido para um número de teste informado. Use com cuidado: é um envio real e pode ser cobrado. |

## 5. Consentimento do paciente

O sistema só envia a quem autorizou. No cadastro do paciente, em Dados principais, no campo Celular para WhatsApp, informe o celular e marque "Autorizo receber lembretes e confirmações por WhatsApp". Sem a marca, o selo fica Autorização pendente e nenhuma mensagem é enviada.


Na lista de pacientes, a coluna com o ícone do WhatsApp mostra com um visto verde quem já autorizou e com um X vermelho quem não autorizou. O filtro da lista permite ver só os que autorizaram ou só os que não autorizaram.


> ⚠️ Registre a autorização somente quando o paciente ou responsável consentir de fato (por exemplo, no termo de atendimento). É uma exigência da LGPD e das regras do WhatsApp.

## 6. Confirmação feita pelo paciente

A mensagem enviada traz o botão Confirmar meus horários. Ele abre uma página pública, sem senha, em que o paciente vê seus agendamentos do dia e marca, em cada horário, Vou comparecer ou Não poderei ir. O link é individual e expira após alguns dias (por padrão, 2). Depois de expirar, o paciente precisa entrar em contato com a clínica. A confirmação fica registrada e aparece para a recepção na Agenda.

> ⚠️ A página de confirmação só funciona para clínicas com o módulo de WhatsApp Meta habilitado no contrato.

## 7. Como acompanhar

## Disparos

Mostra um disparo por dia com início, término, total de pacientes, enviadas, falhas, respostas e a situação. Use o filtro de período (por exemplo, últimos 30 dias) e o botão de atualizar.


## Mensagens

Lista as mensagens recentes com data, paciente, destino, template, status, tentativas, eventos (envio, entrega e leitura) e a resposta ou erro devolvido pela Meta. Os botões acima filtram por situação.


| Status | Significado |
|---|---|
| Pendente / Processando | Na fila para ser enviada ou sendo enviada agora. |
| Enviada | A Meta aceitou a mensagem. |
| Entregue | Chegou ao aparelho do paciente. |
| Lida | O paciente abriu a mensagem. |
| Falha | A mensagem não foi enviada. O motivo aparece na coluna Resposta/erro. |

## Respostas dos pacientes na Agenda

Na Agenda, o botão Respostas WhatsApp (no celular, em Mais; também na tela de Pacientes do dia do profissional) abre a janela Respostas dos pacientes - WhatsApp Meta, com as abas Ontem, Hoje e Amanhã. Ela traz os contadores de agendamentos, enviadas, falhas, confirmados, não vão e sem resposta, e um filtro para listar só um desses grupos, inclusive Falha no envio. A recepção usa para ligar aos que não responderam e liberar horários dos que avisaram que não vêm.


## Reenviar mensagens com falha

Quando uma mensagem falha, a linha mostra o motivo em português (por exemplo, número sem WhatsApp ou problema de pagamento na conta da Meta) e o botão Reenviar. Acima da lista, Reenviar falhas (n) reenvia de uma vez todas as mensagens com falha do dia. Antes de reenviar, o sistema pede confirmação.

| Regra do reenvio | Detalhe |
|---|---|
| Quando vale | Só para consultas de hoje e de amanhã. |
| Link novo | Cada reenvio gera um link de confirmação novo; o link enviado antes deixa de valer. |
| Limite | Cada mensagem pode ser reenviada manualmente até 3 vezes; depois disso o botão não aparece mais. |
| Uma mensagem por paciente | Uma mensagem cobre todos os agendamentos do paciente no dia; o botão aparece só na primeira linha dela. |
| Quem pode | Administrador e atendente, com o módulo WhatsApp Meta habilitado na clínica. |

> ⚠️ Se a falha continuar, o motivo indica o que corrigir: celular do paciente, pagamento da conta na Meta, template aprovado ou limite de envios. Corrija e use Reenviar novamente.

## Erros comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| 131042 - Business eligibility payment issue | A conta do WhatsApp Business não tem forma de pagamento válida, ou há pendência de moeda, fuso ou dados fiscais. | Na Meta, cadastre ou regularize o pagamento da conta e tente novamente. |
| 131058 - Hello World só de números de teste | O template de exemplo hello_world só pode ser enviado pelo número de teste público da Meta. | Use o template do lembrete aprovado, não o hello_world. |
| Template não aparece ou não é aprovado | Ainda em análise, rejeitado ou não sincronizado. | Clique em Sincronizar; se rejeitado, crie um novo template ajustando o texto. |
| Ninguém recebe o lembrete | Lembrete desligado, sem template vinculado, pacientes sem autorização, filtros excluindo tudo ou envio automático desabilitado no servidor. | Confira o quadro de ativação, use Simular próximos envios e peça à equipe técnica para verificar o servidor. |
| Falha só em alguns pacientes | Número inválido ou sem WhatsApp. | Corrija o celular no cadastro do paciente e use Reenviar na janela de respostas da Agenda. |
| O botão Enviar está desabilitado no envio manual | A data escolhida não é hoje nem amanhã, ou o paciente está sem celular válido. | Escolha hoje ou amanhã; corrija o celular no cadastro. |
| Paciente com horário fixo não recebeu o lembrete | Não existe a agenda do mês da consulta para esse horário fixo. | Crie a agenda do mês e confira novamente em Simular próximos envios. |
| Entrega e leitura não atualizam | Webhook não configurado na Meta. | Refaça o passo 7 e confirme a chave de verificação. |

## Boas práticas

| Recomendação | Por quê |
|---|---|
| Faça uma homologação controlada antes de ligar para todos | Autorize poucos pacientes, use Simular próximos envios e confira Mensagens no dia seguinte. |
| Guarde o token com segurança | Quem tem o token envia mensagens em nome da clínica. Se vazar, gere um novo e atualize no sistema. |
| Monitore Disparos e Mensagens | Falhas de pagamento ou de template interrompem os envios. |
| Mantenha o texto sem dados sensíveis | O lembrete traz só nome, data e horários; não inclua diagnóstico ou valores. |
| Respeite a autorização do paciente | Quem pedir para não receber deve ter a marca removida do cadastro. |
| Confira os custos na Meta | A cobrança é por mensagem; mensagens de utilidade dentro de uma conversa aberta podem não ser cobradas. Consulte a tabela de preços atual da Meta. |

> ⚠️ O envio manual continua disponível a qualquer momento e não depende da Meta, o que o torna uma alternativa caso o envio automático esteja indisponível.
