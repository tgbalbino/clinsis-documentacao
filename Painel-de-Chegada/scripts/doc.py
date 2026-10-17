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
NOME = 'Painel_de_Chegada'
TITULO = "Painel de Chegada (TV)"
SUBTITULO = "Avisar o profissional, na TV e no celular, que o paciente chegou"
VIDEO_NOME = "https://youtu.be/CX3IduHG7Kg"
INTRO = ('O <b>Painel de chegada</b> mostra, numa <b>TV</b> da clínica, o nome do profissional e do paciente que acabou de chegar, '
         'com um aviso sonoro. Ao mesmo tempo, o <b>profissional</b> recebe o chamado no sistema (e no celular, se ativar as '
         'notificações). O aviso sai do <b>Check-in</b> ("Notificar profissional") ou do botão <b>Avisar chegada</b> da <b>Agenda</b>. '
         'Quando não há chegada, a TV mostra a data, a hora, o clima e os <b>aniversariantes do dia</b>. O módulo é liberado por clínica '
         'pela Área do Administrador e vem <b>desligado</b>.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado. Os nomes do exemplo são fictícios.')

blocks = [
    ('h2', 'Como funciona'),
    ('tabelagen', ['Peça', 'Para que serve'],
     [['TV (<b>/painel-chegada</b>)', 'Tela cheia que fica ligada na recepção ou no corredor. Mostra a chegada, o som e os aniversariantes. Não tem login: é autorizada uma vez por QR code.'],
      ['Configuração (<b>Tabelas Aux. → Painel de chegada</b>)', 'Ativa o painel e define duração do aviso, tempo de cada cartão, som, volume, forma de mostrar o nome do paciente e limite de TVs. Somente <b>Administrador</b>.'],
      ['Aviso de chegada', 'Criado pelo <b>Check-in</b> (modal "Notificar profissional") ou pelo botão <b>Avisar chegada</b> na Agenda.'],
      ['Chamado ao profissional', 'O profissional vê "<b>Fulano foi chamado</b>" na tela do sistema e, com as notificações ativas, recebe o aviso também no celular ou no computador.']],
     [6, 12]),

    ('h2', 'Passo 1: liberar e configurar'),
    ('p', 'Na <b>Área do Administrador</b> (<b>/area</b>), no cadastro da clínica, marque <b>Painel de chegada na TV</b>. Depois, com um usuário '
          '<b>Administrador</b>, abra <b>Tabelas Aux. → Painel de chegada</b>, marque <b>Ativar módulo de painel de chegada</b>, ajuste os campos e clique em <b>Salvar</b>. '
          'Quem já estava logado precisa sair e entrar de novo para o menu aparecer.'),
    ('img', '01-configuracao.png', 'Configuração do painel: ativação, tempos, som, volume, nome do paciente e TVs autorizadas. Embaixo, a presença da TV.'),
    ('tabelagen', ['Campo', 'Para que serve'],
     [['Duração do aviso (minutos)', 'Por quanto tempo a chegada continua na fila da TV (de 1 a 60).'],
      ['Tempo de cada cartão (segundos)', 'Quanto tempo cada chamada fica na tela antes de passar para a próxima (de 5 a 30).'],
      ['Som e Volume', 'Suave, Neutro, Acessível, Piano ambiente ou Sem som. O botão <b>Ouvir som</b> toca uma prévia.'],
      ['Nome do paciente', '<b>Primeiro nome + inicial</b> (mais discreto, recomendado para sala de espera) ou <b>Nome completo</b>.'],
      ['Máximo de TVs autorizadas', 'Quantas TVs podem estar conectadas ao mesmo tempo (de 1 a 20).'],
      ['Validade da autorização (horas)', 'Depois desse prazo a TV pede nova autorização (de 1 a 72).']],
     [6, 12]),
    ('p', 'A seção <b>Presença da TV</b> informa se há TV conectada ("TV conectada (1)" ou "Nenhuma TV conectada"). '
          'Na <b>Agenda</b>, se o painel estiver ligado e nenhuma TV conectada, aparece um aviso amarelo: '
          '<b>"Painel de chegada indisponível: nenhum dispositivo conectado. Os avisos não serão exibidos."</b>, com o link <b>Como conectar a TV</b>.'),
    ('img', '02-agenda-sem-tv.png', 'Agenda avisando que nenhuma TV está conectada ao painel.'),

    ('h2', 'Passo 2: abrir a TV'),
    ('p', 'No navegador da TV (ou do computador ligado a ela), abra o endereço do sistema acrescido de <b>/painel-chegada</b> e deixe em tela cheia. '
          'Aparece <b>Autorize esse dispositivo</b>, com um <b>QR code</b> e um <b>código de 6 dígitos</b>.'),
    ('img', '03-tv-qr.png', 'TV ainda não autorizada: QR code e código.'),

    ('h2', 'Passo 3: autorizar a TV'),
    ('p', 'Com o celular da recepção, <b>logado como administrador</b>, leia o QR code e clique em <b>Autorizar</b>. '
          'Em poucos segundos a TV passa para <b>Aguardando chegadas</b>.'),
    ('img', '04-autorizar.png', 'Página aberta pelo QR code: confirmar a autorização da TV.'),
    ('img', '04b-autorizado.png', 'TV autorizada; a página fecha sozinha.'),
    ('img', '05-tv-aguardando.png', 'TV aguardando chegadas. A primeira vez pede um clique na tela para liberar o som.'),
    ('aviso', 'O navegador só toca som depois de um clique na página. Por isso, ao ligar a TV, clique uma vez na tela: o rodapé deixa de mostrar '
              '"Clique na tela para ativar o som" e o ícone do alto-falante fica ativo.'),

    ('h2', 'Avisar a chegada do paciente'),
    ('p', '<b>Pelo Check-in.</b> Ao confirmar um Check-in (módulo e painel ligados), o sistema abre <b>Notificar profissional</b>: "Deseja avisar o profissional que o paciente chegou?". '
          'Cada horário do paciente aparece com o profissional. Marque os que quiser e clique em <b>Avisar agora</b>, ou em <b>Agora não</b> para seguir sem avisar. '
          'O resultado é <b>"N aviso(s) enviado(s) para o painel"</b>.'),
    ('p', '<b>Pela Agenda.</b> Na linha do paciente, abra o menu de ações (os três pontinhos) e clique em <b>Avisar chegada</b>. O botão só aparece para atendimentos de <b>hoje</b>. '
          'Se nenhuma TV estiver conectada, o sistema avisa e não envia.'),
    ('img', '06-agenda-avisar.png', 'Menu de ações da linha do paciente, com Avisar chegada.'),
    ('img', '06b-aviso-enviado.png', 'Confirmação: "Aviso enviado para o painel."'),
    ('p', 'Na TV aparece <b>NOVA CHEGADA</b> com o nome do profissional em destaque e o do paciente abaixo, uma barra de tempo e o som. '
          'Cada chamada fica na tela pelo tempo do cartão; a anterior fica no canto, em "Chamada anterior". Se o mesmo paciente for avisado de novo, a TV mostra outro cartão.'),
    ('img', '07-tv-nova-chegada.png', 'TV: Nova chegada, com o profissional, o paciente, a barra de tempo e o selo da data comemorativa (Outubro Rosa).'),

    ('h2', 'O que o profissional recebe'),
    ('p', 'O profissional logado vê a mensagem <b>"Nome do paciente foi chamado."</b> (título <b>Chamado do painel</b>), por 10 segundos, e o celular vibra. '
          'Para receber também com o sistema minimizado, ao entrar o sistema oferece <b>ativar as notificações</b>: aceite a permissão do navegador. '
          'Depois disso a confirmação é "Este dispositivo receberá os chamados do painel."'),

    ('h2', 'Conferir as chamadas do dia'),
    ('p', 'Na Agenda, em <b>Mais opções → Ver chamadas do painel</b>, aparece a lista com Profissional, Paciente, quando foi criada, quando expira e a situação. '
          'Sem chamadas, o sistema mostra os <b>aniversariantes do dia</b>.'),
    ('img', '08-chamadas.png', 'Chamadas do painel: quem foi avisado, a hora e a situação.'),

    ('h2', 'Aniversariantes e datas comemorativas'),
    ('p', 'Quando não há chegada, a TV mostra <b>Aniversariantes do dia</b> com a mensagem <b>Parabéns!</b> e os nomes (pacientes da clínica que fazem aniversário no dia). '
          'No alto aparecem o nome da cidade, a data e hora e o clima; e, em datas comemorativas (Outubro Rosa, Novembro Azul, Natal etc.), um selo discreto com o nome da campanha.'),

    ('h2', 'Problemas comuns'),
    ('tabelagen', ['Sintoma', 'Causa provável', 'O que fazer'],
     [['Menu "Painel de chegada" não aparece', 'Módulo desligado na clínica, ou usuário não é Administrador', 'Ligar na Área do Administrador; sair e entrar de novo'],
      ['"Nenhuma TV do painel está conectada"', 'TV desligada, sem autorização ou autorização vencida', 'Abrir /painel-chegada na TV e autorizar de novo (passo 3)'],
      ['Aviso criado, mas a TV não toca som', 'O navegador bloqueia som sem clique', 'Clicar uma vez na tela da TV'],
      ['"Agendamento inválido para aviso"', 'O atendimento não é de hoje', 'O aviso só vale para o dia'],
      ['Profissional não recebe o chamado', 'Não está logado, ou não ativou as notificações', 'Entrar no sistema e aceitar as notificações do navegador']],
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
