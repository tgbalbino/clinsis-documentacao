# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.0'
DATA = '16/10/2026'
NOME = 'Totem_de_Checkin'
TITULO = "Totem de Check-in"
SUBTITULO = "O paciente (ou o responsável) registra a chegada sozinho na portaria, com CPF e data de nascimento"
VIDEO_NOME = "video-totem-de-checkin-com-legenda.mp4"
INTRO = ('O <b>Totem de check-in</b> é a tela da portaria onde o paciente, ou o responsável por ele, registra a chegada '
         'sem usuário e senha: basta informar o <b>CPF</b> e a <b>data de nascimento</b>. A recepção vê um selo verde '
         'com o <b>horário da chegada</b> ao lado do nome do paciente na <b>Agenda</b> do dia. O totem apenas avisa a chegada: '
         'o <b>Check-in</b> da recepção (pagamento, Plano Próprio) continua sendo feito normalmente. O recurso vem '
         '<b>desligado</b> e é ativado pelo administrador da clínica.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado. O horário do paciente do exemplo foi ajustado só para este manual.')

blocks = [
    ('h2', 'Onde fica cada coisa'),
    ('tabelagen', ['O que', 'Onde', 'Quem acessa'],
     [['Ativar e configurar o totem', 'Menu <b>Tabelas Aux. → Totem de check-in</b> (<b>/totem/configuracao</b>)', 'Somente <b>Administrador</b>'],
      ['Tela do totem (a que o paciente usa)', '<b>/totem</b>, aberta no equipamento da portaria', 'Sem login (precisa ser autorizada uma vez)'],
      ['Autorizar um totem', '<b>/totem/autorizar</b>, aberta pelo QR code lido no celular do administrador', 'Somente <b>Administrador</b> logado'],
      ['Ver quem chegou', 'Selo verde com o horário, antes do nome do paciente, na <b>Agenda</b> do dia', 'Recepção e demais usuários da agenda']],
     [5, 8, 5]),

    ('h2', 'Antes de começar'),
    ('tabelagen', ['Requisito', 'Detalhe'],
     [['Paciente com CPF e data de nascimento', 'É com esses dois dados que o paciente se identifica no totem.'],
      ['Responsável (opcional)', 'Cadastrado no paciente, com <b>CPF</b>, <b>data de nascimento</b> e vínculo <b>ativo</b>. Com o totem ativo, a data de nascimento do responsável passa a ser obrigatória. Para achar quem está sem ela: <b>Cadastros → Pessoa → Filtros</b>, marque <i>Responsável</i> e <i>Sem data de nascimento</i>.'],
      ['Atendimento marcado para hoje', 'O totem só mostra o que está agendado no dia. Atendimentos desmarcados, com falta, justificados ou remarcados não aparecem.'],
      ['Scripts do banco (suporte)', 'Antes de publicar a API: 206_Totem_Auto_Checkin.sql, 207_Responsaveis_Paciente.sql e 209_Totem_Responsavel.sql.']],
     [6, 12]),

    ('h2', 'Passo 1: ativar e configurar (administrador)'),
    ('p', 'Entre com um usuário <b>Administrador</b>, abra <b>Tabelas Aux. → Totem de check-in</b>, marque <b>Ativar o totem nesta clínica</b>, '
          'ajuste os valores se precisar e clique em <b>Salvar</b>.'),
    ('img', '01-configuracao.png', 'Configuração do totem: ativar, janela de horário, inatividade, validade, bloqueio e mensagem de Plano Próprio.'),
    ('tabelagen', ['Campo', 'Para que serve', 'Padrão'],
     [['Liberar quantos minutos antes', 'Até quanto tempo antes do horário o paciente pode registrar a chegada (máx. 240)', '60'],
      ['Aceitar até quantos minutos depois', 'Até quanto tempo depois do horário ainda aceita (máx. 240)', '30'],
      ['Inatividade para voltar ao início', 'A tela volta ao início sozinha se ninguém tocar (segundos)', '30'],
      ['Validade da autorização', 'Depois desse prazo o totem pede nova autorização (horas)', '720 (30 dias)'],
      ['Tentativas erradas antes de bloquear', 'Erros de CPF/nascimento antes de bloquear aquele CPF', '5'],
      ['Bloqueio (minutos)', 'Tempo do bloqueio', '10'],
      ['Mensagem para Plano Próprio', 'Texto mostrado ao paciente de Plano Próprio', 'Chegada registrada. Dirija-se à recepção.']],
     [5.5, 9, 3.5]),

    ('h2', 'Passo 2: abrir o totem na portaria'),
    ('p', 'No computador ou tablet da portaria, abra o navegador no endereço do sistema acrescido de <b>/totem</b>. '
          'A tela mostra <b>Autorize este totem</b>, com um <b>QR code</b> e um <b>código de 6 dígitos</b>.'),
    ('img', '02-totem-qr.png', 'Totem ainda não autorizado: QR code e código de 6 dígitos.'),

    ('h2', 'Passo 3: autorizar o totem (administrador)'),
    ('p', 'Com o <b>Administrador logado</b>, leia o QR code com o celular. Dê um nome ao totem (por exemplo, "Totem da recepção") '
          'e clique em <b>Autorizar totem</b>. O QR code vale por 5 minutos; se expirar, a própria tela gera outro.'),
    ('img', '03-autorizar.png', 'Página de autorização aberta pelo QR code: nome do totem e botão Autorizar totem.'),
    ('img', '03b-autorizado.png', 'Totem autorizado: a página já pode ser fechada.'),
    ('p', 'Em poucos segundos o equipamento troca para <b>Bem-vindo(a)</b>, pronto para uso.'),
    ('img', '04-totem-inicio.png', 'Tela inicial do totem, pronta para o paciente.'),

    ('h2', 'Como o paciente usa'),
    ('p', 'Quem chega toca em <b>Registrar chegada</b>, digita o <b>CPF</b> e depois a <b>data de nascimento</b> (somente números). '
          '<b>Os dois são da mesma pessoa, a que está diante do totem</b>: o paciente usa os próprios dados; o responsável usa os <b>dele</b>, '
          'não os do paciente.'),
    ('img', '05-totem-cpf.png', 'Teclado numérico: o CPF aparece formatado conforme é digitado.'),
    ('img', '06-totem-nascimento.png', 'Data de nascimento: dia, mês e ano (8 números), da mesma pessoa do CPF.'),
    ('p', 'Identificada a pessoa, o totem mostra os atendimentos de hoje. Marque o que está chegando e toque em <b>Confirmar chegada</b>.'),
    ('img', '07-totem-itens.png', 'Atendimentos de hoje: o paciente marca o horário e confirma.'),
    ('img', '08-totem-resultado.png', 'Chegada registrada. A tela volta ao início sozinha.'),
    ('tabelagen', ['Quem está no totem', 'CPF e nascimento digitados', 'O que aparece'],
     [['Paciente', 'Os do próprio paciente', 'Os atendimentos dele'],
      ['Responsável (pai, mãe, avó, babá…)', 'Os do <b>responsável</b>', 'Os atendimentos dos pacientes ligados a ele; com mais de um dependente, o nome de cada paciente']],
     [5, 6, 7]),
    ('aviso', 'Criança cadastrada com o CPF do pai ou da mãe: com o CPF do responsável e o nascimento <b>do responsável</b>, ele entra como responsável; '
              'com o CPF do responsável e o nascimento <b>da criança</b>, entra como o próprio paciente. Os dois caminhos funcionam.'),
    ('aviso', 'Sugestão de aviso para colar ao lado do totem: "Digite o CPF e a data de nascimento de quem está aqui agora. Se você é o responsável '
              'pelo paciente, use os SEUS dados, não os do paciente. Em caso de dúvida, procure a recepção."'),

    ('h2', 'O que o totem responde'),
    ('tabelagen', ['Situação', 'O que o totem mostra'],
     [['Dentro da janela de horário', 'Chegada registrada, "Aguarde ser chamado"'],
      ['Plano Próprio', 'Chegada registrada e a mensagem para seguir à recepção'],
      ['Chegou cedo demais', '"Ainda é cedo para o seu horário"'],
      ['Passou da janela', '"O horário do seu atendimento já passou. Procure a recepção"'],
      ['Já registrado, ou já fez check-in', '"Sua chegada já foi registrada"'],
      ['Sem atendimento hoje', '"Não encontramos agendamento para hoje. Procure a recepção"'],
      ['CPF/nascimento não conferem, ou bloqueado', 'Mensagem genérica "Procure a recepção" (não revela se o CPF existe)']],
     [7, 11]),

    ('h2', 'O que a recepção vê'),
    ('p', 'Na <b>Agenda</b> do dia, antes do nome do paciente aparece um selo verde com um <b>✔</b> e o horário da chegada. '
          'Ao passar o mouse, o selo diz "Chegada registrada no totem às HH:mm". A tela consulta a cada 30 segundos. '
          'O totem <b>não</b> faz check-in financeiro nem baixa pagamento: o Check-in da recepção continua normal.'),
    ('img', '09-agenda-chegou.png', 'Agenda do dia: selo verde com o horário da chegada antes do nome do paciente que usou o totem.'),

    ('h2', 'Gerenciar os totens'),
    ('p', 'Na mesma tela <b>Totem de check-in</b>, a lista <b>Totens autorizados</b> mostra nome, quando foi autorizado, validade e último acesso. '
          'O botão <b>Revogar</b> desliga aquele equipamento na hora (ele volta ao QR code). Para parar de usar o totem em toda a clínica, '
          'desmarque <b>Ativar o totem nesta clínica</b> e salve.'),
    ('img', '10-configuracao-totens.png', 'Totens autorizados, com a opção Revogar.'),

    ('h2', 'Segurança e privacidade'),
    ('p', 'O totem usa uma credencial própria, guardada só como hash, com validade e possibilidade de revogação, que só funciona nas rotas do totem '
          'e só para a clínica que o autorizou. A tela nunca mostra o CPF (só o primeiro nome e o horário) e apaga os dados digitados depois da identificação. '
          'Há bloqueio por CPF e por totem após erros, com registro de cada tentativa (o CPF é guardado só como código irreversível). '
          'Qualquer toque reinicia a contagem de inatividade.'),
    ('p', '<b>Equipamento recomendado:</b> computador com Chrome ou Edge em modo quiosque (<b>--kiosk --app=https://seu-sistema/totem</b>) ou tablet Android com Fully Kiosk. '
          'A credencial fica no navegador do equipamento: limpar os dados do navegador exige autorizar o totem de novo.'),

    ('h2', 'Problemas comuns'),
    ('tabelagen', ['Sintoma', 'Causa provável', 'O que fazer'],
     [['"Totem desativado. Procure a recepção"', 'Opção desmarcada na configuração', 'Marcar <b>Ativar o totem nesta clínica</b> e salvar'],
      ['Volta ao QR de autorização sozinho', 'Autorização expirada ou revogada', 'Autorizar de novo (passo 3)'],
      ['Responsável não é reconhecido', 'Sem data de nascimento, sem CPF, vínculo inativo ou paciente inativo', 'Completar o cadastro do responsável no paciente'],
      ['Paciente "não encontrado" com dados certos', 'CPF/nascimento diferentes do cadastro, ou bloqueio temporário', 'Conferir o cadastro; aguardar o tempo de bloqueio'],
      ['Atendimento não aparece', 'Fora do dia, desmarcado, ou fora da janela', 'Conferir a agenda e a janela configurada'],
      ['"Sem conexão" no totem', 'API indisponível ou rede da portaria', 'Verificar a rede; a tela tenta de novo sozinha'],
      ['Item "Totem de check-in" não aparece no menu', 'Usuário não é Administrador', 'Entrar com perfil Administrador']],
     [5.5, 6, 6.5]),
]

render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
print('ok')
