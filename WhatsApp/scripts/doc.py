# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.2'
DATA = '01/10/2026'
TITULO = 'WhatsApp - lembretes e confirmações'
SUBTITULO = 'Envio manual e envio automático pela API oficial da Meta: requisitos, configuração, templates, consentimento e acompanhamento'
VIDEO_NOME = "https://youtu.be/2lvKkYApZFE"
INTRO = ('O ClinSis avisa os pacientes de seus agendamentos por <b>WhatsApp</b> de duas formas: o <b>envio manual</b>, '
         'em que a recepção abre o WhatsApp com a mensagem pronta e envia com um clique, e o <b>envio automático pela '
         'API oficial da Meta</b> (WhatsApp Business Platform), em que o sistema envia sozinho o lembrete do dia seguinte '
         'e o paciente confirma ou avisa que não poderá ir por um link. Este documento explica as duas formas, o que a '
         'clínica precisa ter na Meta, como configurar, como acompanhar e os erros mais comuns.')
RODAPE = ('Documento gerado por teste manual guiado em ambiente local de homologação, clínica de testes "Homologação" '
          '(Clínica 1), usuário administrador de teste. Números de telefone e identificadores da conta Meta foram '
          'ocultados nas imagens. Nenhuma mensagem foi enviada durante a captura.')

blocks = [
    ('h2', 'Visão geral: dois modos de envio'),
    ('tabelagen', ['Modo', 'Como funciona', 'Quando usar'], [
        ['Manual', 'A recepção abre <b>Enviar lembretes</b>, vê os pacientes agendados de hoje ou de amanhã, clica em <b>Enviar</b> e o WhatsApp do próprio computador ou celular abre com a mensagem pronta. Quem envia é a pessoa.', 'Clínica sem conta na Meta, ou para casos pontuais.'],
        ['Automático (Meta)', 'O sistema envia sozinho, no horário configurado, um lembrete com os agendamentos do dia seguinte usando a API oficial da Meta. O paciente confirma pelo botão da mensagem.', 'Clínica com conta e número comerciais na Meta. Envio em escala e com acompanhamento.'],
    ], [3, 9.5, 5]),
    ('aviso', 'Só o perfil <b>Administrador</b> configura. O envio automático exige que o paciente tenha <b>autorizado o recebimento</b> '
              'por WhatsApp no cadastro (veja o capítulo de consentimento).'),

    ('h2', 'Onde fica no sistema'),
    ('tabela', [
        ('Tabelas Aux. → WhatsApp', 'Painel com o resumo de mensagens, a definição da mensagem, o envio manual de lembretes e o telefone/chave da integração antiga (WhatsGW).', 'Administrador'),
        ('Agenda → Enviar lembretes', 'Atalho para a tela de envio manual dos lembretes de hoje e de amanhã.', 'Recepção / Administrador'),
        ('Tabelas Aux. → WhatsApp Meta', 'Configuração do envio automático: conta da Meta, lembrete, filtros, templates, disparos e mensagens.', 'Administrador'),
        ('Cadastros → Paciente → Dados principais', 'Campo Celular para WhatsApp e a autorização de recebimento, logo abaixo dos telefones.', 'Recepção / Administrador'),
        ('Agenda → Respostas WhatsApp (no celular: Mais → Respostas WhatsApp)', 'Respostas dos pacientes de ontem, hoje e amanhã, com o botão Reenviar para as mensagens que falharam.', 'Recepção / Administrador'),
    ]),
    ('img', '00-painel-whatsapp.png', 'Painel WhatsApp: cartões de resumo, mensagem de aviso, lembretes do dia (envio manual) e integração antiga.'),

    ('h2', '1. Envio manual'),
    ('h2', 'Enviar lembretes'),
    ('p', 'No painel, em <b>Lembretes do dia (envio manual)</b>, clique em <b>Acessar</b> (ou use o botão <b>Enviar lembretes</b> da Agenda). Escolha a data (as setas mudam o dia; '
          '<b>Hoje</b> volta para hoje), se quiser filtre pelo paciente e clique na lupa. A lista mostra cada paciente com o celular '
          'e todos os horários e profissionais do dia. O botão verde <b>Enviar</b> abre o WhatsApp no navegador com a mensagem pronta; '
          'o envio é feito por você. <b>O envio só é liberado para hoje e para amanhã</b>: nas demais datas a tela serve apenas para consulta e '
          'mostra um aviso em amarelo.'),
    ('img', '01-manual-lembretes-do-dia.png', 'Enviar lembretes: um paciente por linha, com os horários do dia. Em datas que não são hoje nem amanhã, aparece o aviso de que a tela é só para consulta.'),
    ('h2', 'Definir a mensagem'),
    ('p', 'Em <b>Definir mensagem</b> escreva o texto que será usado nos avisos manuais. Os campos entre chaves são trocados '
          'automaticamente pelos dados do paciente e do agendamento.'),
    ('img', '02-manual-definir-mensagem.png', 'Definir mensagem: texto padrão do aviso de agendamento.'),

    ('h2', '2. Envio automático pela Meta: o que a clínica precisa ter'),
    ('p', 'O envio automático usa a <b>WhatsApp Business Platform (Cloud API)</b>, o serviço oficial da Meta para empresas. '
          'A clínica precisa criar e manter esta estrutura <b>na Meta</b>; o ClinSis apenas usa os dados dela. Você precisa de:'),
    ('tabelagen', ['Item', 'O que é', 'Onde criar'], [
        ['Conta Meta e Portfólio Empresarial', 'Conta de um responsável da clínica (Facebook) e o portfólio empresarial (Business Portfolio) que representa a clínica. É a "dona" de tudo o mais.', 'business.facebook.com'],
        ['Aplicativo Meta', 'Aplicativo do tipo Empresa, com o produto WhatsApp adicionado. É o que gera o acesso à API.', 'developers.facebook.com/apps'],
        ['Conta do WhatsApp Business (WABA)', 'Conta que reúne os números e os templates da clínica. Gera o <b>WABA ID</b>.', 'Painel do aplicativo → WhatsApp → Configuração da API'],
        ['Número de telefone comercial', 'Número da clínica que será o remetente. Gera o <b>Phone Number ID</b>.', 'Mesmo painel: "Adicionar número de telefone"'],
        ['Forma de pagamento', 'Cartão para pagar as mensagens enviadas (a Meta cobra por mensagem de template entregue).', 'Meta Business Suite → Configurações → Cobrança e pagamentos'],
        ['Token de acesso permanente', 'Chave que autoriza o ClinSis a enviar mensagens pela conta. Criada por um <b>Usuário do sistema</b>.', 'Configurações do negócio → Usuários → Usuários do sistema'],
        ['Template aprovado', 'Modelo de mensagem aprovado pela Meta. Só mensagens de template aprovado podem ser iniciadas pela clínica.', 'WhatsApp Manager → Modelos de mensagem (ou pelo ClinSis, aba Templates)'],
    ], [4.2, 8.3, 5]),
    ('aviso', 'As telas da Meta mudam com frequência e os nomes dos menus podem variar. Em caso de dúvida, siga a documentação '
              'oficial em <b>developers.facebook.com/docs/whatsapp</b>. Este manual não traz imagens do site da Meta porque o acesso exige o login da clínica.'),

    ('h2', 'Sobre o número comercial'),
    ('tabelagen', ['Regra', 'Detalhe'], [
        ['Número da empresa', 'Use um número que pertença à clínica, com código do país e DDD (por exemplo, +55 32 ...). Pode ser celular ou linha fixa.'],
        ['Precisa receber o código de verificação', 'A Meta confirma o número por <b>SMS</b> ou por <b>ligação de voz</b>. Linha fixa só funciona pela ligação.'],
        ['Não pode estar em uso no aplicativo WhatsApp', 'Um número ativo no WhatsApp comum precisa ter a conta excluída antes de ser cadastrado na API. Para o WhatsApp Business (aplicativo) existe a opção de coexistência; confirme as condições com a Meta antes de decidir.'],
        ['Nome de exibição', 'É o nome que o paciente vê. Precisa ser aprovado e representar a clínica.'],
        ['Limites', 'Um portfólio novo pode ter poucos números e um limite inicial de conversas por dia. Com a <b>verificação da empresa</b> concluída, os limites aumentam.'],
    ], [5.5, 12]),
    ('aviso', 'Use, de preferência, um número exclusivo para o envio automático. Pacientes podem <b>responder</b> a mensagem; '
              'quem atende essas respostas deve ser definido pela clínica.'),

    ('h2', 'Passo a passo resumido na Meta'),
    ('tabelagen', ['Passo', 'O que fazer'], [
        ['1', 'Crie ou acesse o <b>Portfólio Empresarial</b> da clínica em business.facebook.com e, se pedido, faça a verificação da empresa.'],
        ['2', 'Em developers.facebook.com/apps crie um aplicativo do tipo <b>Empresa</b>, vinculado a esse portfólio, e adicione o produto <b>WhatsApp</b>.'],
        ['3', 'Em WhatsApp → Configuração da API, adicione o <b>número de telefone</b>, informe o nome de exibição e confirme o código recebido por SMS ou ligação.'],
        ['4', 'Anote o <b>WABA ID</b> e o <b>Phone Number ID</b> mostrados nessa tela.'],
        ['5', 'Cadastre a <b>forma de pagamento</b> na conta do WhatsApp Business.'],
        ['6', 'Nas Configurações do negócio, crie um <b>Usuário do sistema</b> administrador, atribua a ele o aplicativo e a conta do WhatsApp e gere o <b>token</b> sem expiração com as permissões whatsapp_business_messaging, whatsapp_business_management e business_management. Guarde o token em local seguro; ele é mostrado uma única vez.'],
        ['7', 'Informe à equipe do ClinSis o endereço de retorno (webhook) e a chave de verificação que ela fornecer, e cadastre-os no aplicativo em WhatsApp → Configuração → Webhook, assinando o campo <b>messages</b>. É por ele que o sistema recebe entregas, leituras e falhas.'],
    ], [1.6, 15.9]),

    ('h2', '3. Configuração no ClinSis'),
    ('p', 'Em <b>Tabelas Aux. → WhatsApp Meta</b>, aba <b>Configuração</b>. No alto, um quadro de <b>ativação</b> mostra o que ainda falta: '
          'WABA ID e Phone Number ID, token salvo, link público de confirmação, template aprovado vinculado ao lembrete, integração ativa e '
          'lembrete de agendamento ativo. As etiquetas <b>API</b> e <b>Envio automático</b> indicam se o servidor está pronto e se o envio está ligado.'),
    ('img', '03-meta-configuracao.png', 'Configuração: lista de verificação da ativação, dados da conta da Meta e ajustes do lembrete.'),
    ('tabelagen', ['Campo', 'O que informar'], [
        ['Integração ativa', 'Liga ou desliga a integração para a clínica.'],
        ['WABA ID / Phone Number ID / Número de exibição', 'Dados anotados na Meta (passo 4). O número de exibição é o telefone que o paciente vê.'],
        ['Access token', 'Token do usuário do sistema (passo 6). Depois de salvo, o campo fica em branco e aparece "Token salvo"; deixe em branco para mantê-lo. Se o ClinSis já fornece um token próprio para a clínica, o campo é opcional e a tela mostra "Usando o token do Clinsis"; para usar o token da própria clínica, cole-o e salve.'],
        ['Lembrete de agendamento (chave)', 'Liga o lembrete automático. Sem ela nada é enviado.'],
        ['Gerar lembretes às', 'Horário em que o sistema prepara os lembretes dos agendamentos do <b>dia seguinte</b> (por exemplo, 08:00).'],
        ['Template do lembrete', 'Template aprovado que será usado. Pelo botão <b>Ver texto</b> vê-se como o paciente o recebe.'],
    ], [5.5, 12]),
    ('p', 'Depois de preencher, clique em <b>Testar conexão</b> para conferir se a Meta aceita os dados e em <b>Salvar configuração</b>.'),
    ('aviso', 'O endereço público da página de confirmação, a chave do webhook e o segredo do aplicativo ficam no servidor e são '
              'configurados pela equipe técnica do ClinSis. Se o quadro de ativação indicar "API: pendente", solicite essa configuração.'),
    ('img', '04-meta-ver-texto.png', 'Ver texto: o corpo do template, as variáveis e como a mensagem aparece para o paciente.'),

    ('h2', 'Filtros: quando não enviar o lembrete'),
    ('p', 'Em <b>Não enviar lembrete quando</b> marque os valores do agendamento que devem ser ignorados: atendimento particular, forma de atendimento, '
          'plano, cooparticipativo, especialidades, tipos de marcação, método e programa. Um agendamento que combine com qualquer valor marcado não gera lembrete.'),
    ('img', '05-meta-filtros.png', 'Filtros do lembrete: cada quadro abre a lista de valores que devem ser ignorados.'),

    ('h2', 'Quem recebe o lembrete'),
    ('p', 'O lembrete automático é gerado uma vez por dia para os agendamentos do <b>dia seguinte</b>, por paciente: uma única mensagem reúne todos os horários do paciente. '
          'Só entram pacientes com WhatsApp autorizado e que não sejam barrados pelos filtros acima. Para o agendamento <b>fixo</b> (semanal), o lembrete só é gerado '
          'se existir a agenda do <b>mês da consulta</b>; sem a agenda daquele mês, o horário não gera lembrete. No link de confirmação, cada agendamento aparece como um item próprio.'),

    ('h2', 'Simular próximos envios'),
    ('p', 'O botão <b>Simular próximos envios</b> mostra, antes de salvar, quem receberia o lembrete na próxima geração, considerando os filtros marcados. '
          'Dá para trocar a data e pesquisar por nome ou telefone. O aviso em amarelo informa quantos pacientes têm agendamento mas <b>não receberão</b> por '
          'não terem a autorização de WhatsApp. A simulação não envia nada.'),
    ('img', '06-meta-simulacao.png', 'Simulação: pacientes que receberiam o lembrete e quantos não receberão por falta de autorização.'),

    ('h2', '4. Templates'),
    ('p', 'Na Meta, a clínica só pode iniciar uma conversa com um <b>template aprovado</b>. Na aba <b>Templates</b> aparecem os modelos da conta com idioma, '
          'categoria e status. Use <b>Sincronizar</b> para trazer da Meta os modelos e a situação atual, e <b>Novo template</b> para criar um modelo e enviá-lo '
          'para análise. A coluna <b>Usar na rotina</b> vincula um template aprovado ao lembrete de agendamento.'),
    ('img', '07-meta-templates.png', 'Templates: status de cada modelo e vínculo com a rotina de lembrete.'),
    ('tabelagen', ['Item', 'Explicação'], [
        ['Categoria', '<b>Utilidade</b> (avisos sobre algo já contratado, como um agendamento), <b>Marketing</b> (promoções) ou <b>Autenticação</b>. O lembrete deve ser de <b>Utilidade</b>.'],
        ['Status', 'Em análise (a Meta responde em até cerca de 24 horas), <b>Aprovado</b> ou <b>Rejeitado</b>. Só template aprovado envia.'],
        ['Variáveis', 'O lembrete usa quatro: 1 nome do paciente, 2 nome da clínica, 3 data dos agendamentos, 4 horários e profissionais.'],
        ['Botão', 'O template de confirmação tem o botão <b>Confirmar meus horários</b>, que abre a página pública de confirmação.'],
        ['Texto fixo', 'O texto aprovado não pode ser alterado. Para mudar, crie um novo template e vincule-o.'],
        ['Testar', 'Envia o template escolhido para um número de teste informado. Use com cuidado: é um envio real e pode ser cobrado.'],
    ], [3.2, 14.3]),

    ('h2', '5. Consentimento do paciente'),
    ('p', 'O sistema só envia a quem <b>autorizou</b>. No cadastro do paciente, em <b>Dados principais</b>, no campo <b>Celular para WhatsApp</b>, informe o celular e marque '
          '"Autorizo receber lembretes e confirmações por WhatsApp". Sem a marca, o selo fica <b>Autorização pendente</b> e nenhuma mensagem é enviada.'),
    ('img', '11-paciente-aba-whatsapp.png', 'Cadastro do paciente, Dados principais: Celular para WhatsApp, autorização e situação (Autorização pendente).'),
    ('p', 'Na lista de pacientes, a coluna com o ícone do WhatsApp mostra com um visto verde quem já autorizou e com um X vermelho quem não autorizou. '
          'O filtro da lista permite ver só os que autorizaram ou só os que não autorizaram.'),
    ('img', '10-pacientes-lista.png', 'Lista de pacientes: coluna WhatsApp indica quem autorizou o recebimento.'),
    ('aviso', 'Registre a autorização somente quando o paciente ou responsável consentir de fato (por exemplo, no termo de atendimento). '
              'É uma exigência da LGPD e das regras do WhatsApp.'),

    ('h2', '6. Confirmação feita pelo paciente'),
    ('p', 'A mensagem enviada traz o botão <b>Confirmar meus horários</b>. Ele abre uma página pública, sem senha, em que o paciente vê seus agendamentos '
          'do dia e marca, em cada horário, <b>Vou comparecer</b> ou <b>Não poderei ir</b>. O link é individual e <b>expira</b> após alguns dias (por padrão, 2). '
          'Depois de expirar, o paciente precisa entrar em contato com a clínica. A confirmação fica registrada e aparece para a recepção na Agenda.'),
    ('aviso', 'A página de confirmação só funciona para clínicas com o módulo de WhatsApp Meta habilitado no contrato.'),

    ('h2', '7. Como acompanhar'),
    ('h2', 'Disparos'),
    ('p', 'Mostra um disparo por dia com início, término, total de pacientes, enviadas, falhas, respostas e a situação. '
          'Use o filtro de período (por exemplo, últimos 30 dias) e o botão de atualizar.'),
    ('img', '08-meta-disparos.png', 'Disparos: resumo diário do envio automático.'),
    ('h2', 'Mensagens'),
    ('p', 'Lista as mensagens recentes com data, paciente, destino, template, status, tentativas, eventos (envio, entrega e leitura) e a resposta ou erro devolvido pela Meta. '
          'Os botões acima filtram por situação.'),
    ('img', '09-meta-mensagens.png', 'Mensagens: status de cada envio e, em caso de falha, o código e o motivo do erro.'),
    ('tabelagen', ['Status', 'Significado'], [
        ['Pendente / Processando', 'Na fila para ser enviada ou sendo enviada agora.'],
        ['Enviada', 'A Meta aceitou a mensagem.'],
        ['Entregue', 'Chegou ao aparelho do paciente.'],
        ['Lida', 'O paciente abriu a mensagem.'],
        ['Falha', 'A mensagem não foi enviada. O motivo aparece na coluna Resposta/erro.'],
    ], [4.5, 13]),
    ('h2', 'Respostas dos pacientes na Agenda'),
    ('p', 'Na Agenda, o botão <b>Respostas WhatsApp</b> (no celular, em <b>Mais</b>; também na tela de Pacientes do dia do profissional) abre a janela '
          '<b>Respostas dos pacientes - WhatsApp Meta</b>, com as abas <b>Ontem</b>, <b>Hoje</b> e <b>Amanhã</b>. Ela traz os contadores de agendamentos, '
          'enviadas, falhas, <b>confirmados</b>, <b>não vão</b> e <b>sem resposta</b>, e um filtro para listar só um desses grupos, inclusive <b>Falha no envio</b>. '
          'A recepção usa para ligar aos que não responderam e liberar horários dos que avisaram que não vêm.'),
    ('img', '12-agenda-respostas-whatsapp.png', 'Respostas dos pacientes: abas Ontem, Hoje e Amanhã, contadores e lista por horário (aqui sem mensagens no dia).'),
    ('h2', 'Reenviar mensagens com falha'),
    ('p', 'Quando uma mensagem falha, a linha mostra o <b>motivo em português</b> (por exemplo, número sem WhatsApp ou problema de pagamento na conta da Meta) '
          'e o botão <b>Reenviar</b>. Acima da lista, <b>Reenviar falhas (n)</b> reenvia de uma vez todas as mensagens com falha do dia. Antes de reenviar, o sistema pede confirmação.'),
    ('tabelagen', ['Regra do reenvio', 'Detalhe'], [
        ['Quando vale', 'Só para consultas de <b>hoje</b> e de <b>amanhã</b>.'],
        ['Link novo', 'Cada reenvio gera um link de confirmação novo; o link enviado antes <b>deixa de valer</b>.'],
        ['Limite', 'Cada mensagem pode ser reenviada manualmente até <b>3 vezes</b>; depois disso o botão não aparece mais.'],
        ['Uma mensagem por paciente', 'Uma mensagem cobre todos os agendamentos do paciente no dia; o botão aparece só na primeira linha dela.'],
        ['Quem pode', 'Administrador e atendente, com o módulo WhatsApp Meta habilitado na clínica.'],
    ], [4.6, 12.9]),
    ('aviso', 'Se a falha continuar, o motivo indica o que corrigir: celular do paciente, pagamento da conta na Meta, template aprovado ou limite de envios. Corrija e use Reenviar novamente.'),

    ('h2', 'Erros comuns'),
    ('tabelagen', ['Sintoma', 'Causa provável', 'O que fazer'], [
        ['131042 - Business eligibility payment issue', 'A conta do WhatsApp Business não tem forma de pagamento válida, ou há pendência de moeda, fuso ou dados fiscais.', 'Na Meta, cadastre ou regularize o pagamento da conta e tente novamente.'],
        ['131058 - Hello World só de números de teste', 'O template de exemplo hello_world só pode ser enviado pelo número de teste público da Meta.', 'Use o template do lembrete aprovado, não o hello_world.'],
        ['Template não aparece ou não é aprovado', 'Ainda em análise, rejeitado ou não sincronizado.', 'Clique em Sincronizar; se rejeitado, crie um novo template ajustando o texto.'],
        ['Ninguém recebe o lembrete', 'Lembrete desligado, sem template vinculado, pacientes sem autorização, filtros excluindo tudo ou envio automático desabilitado no servidor.', 'Confira o quadro de ativação, use Simular próximos envios e peça à equipe técnica para verificar o servidor.'],
        ['Falha só em alguns pacientes', 'Número inválido ou sem WhatsApp.', 'Corrija o celular no cadastro do paciente e use Reenviar na janela de respostas da Agenda.'],
        ['O botão Enviar está desabilitado no envio manual', 'A data escolhida não é hoje nem amanhã, ou o paciente está sem celular válido.', 'Escolha hoje ou amanhã; corrija o celular no cadastro.'],
        ['Paciente com horário fixo não recebeu o lembrete', 'Não existe a agenda do mês da consulta para esse horário fixo.', 'Crie a agenda do mês e confira novamente em Simular próximos envios.'],
        ['Entrega e leitura não atualizam', 'Webhook não configurado na Meta.', 'Refaça o passo 7 e confirme a chave de verificação.'],
    ], [4.6, 6.8, 6.1]),

    ('h2', 'Boas práticas'),
    ('tabelagen', ['Recomendação', 'Por quê'], [
        ['Faça uma homologação controlada antes de ligar para todos', 'Autorize poucos pacientes, use Simular próximos envios e confira Mensagens no dia seguinte.'],
        ['Guarde o token com segurança', 'Quem tem o token envia mensagens em nome da clínica. Se vazar, gere um novo e atualize no sistema.'],
        ['Monitore Disparos e Mensagens', 'Falhas de pagamento ou de template interrompem os envios.'],
        ['Mantenha o texto sem dados sensíveis', 'O lembrete traz só nome, data e horários; não inclua diagnóstico ou valores.'],
        ['Respeite a autorização do paciente', 'Quem pedir para não receber deve ter a marca removida do cadastro.'],
        ['Confira os custos na Meta', 'A cobrança é por mensagem; mensagens de utilidade dentro de uma conversa aberta podem não ser cobradas. Consulte a tabela de preços atual da Meta.'],
    ], [6.5, 11]),
    ('aviso', 'O envio manual continua disponível a qualquer momento e não depende da Meta, o que o torna uma alternativa caso o envio automático esteja indisponível.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_WhatsApp.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_WhatsApp_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_WhatsApp.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
