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
NOME = 'Revisao_Cadastral'
TITULO = "Revisão Cadastral de Pacientes"
SUBTITULO = "Como manter endereço e contato dos pacientes atualizados: lista de pendentes, aviso na agenda e no check-in"
VIDEO_NOME = "https://youtu.be/j99n-ywnZyA"
INTRO = ('Cadastro desatualizado atrapalha a clínica: telefone que não atende, lembrete que não chega, cobrança enviada '
         'para o endereço errado. O módulo <b>Revisão cadastral</b> ajuda a manter o cadastro do paciente em dia, '
         'com foco em <b>endereço</b> e <b>contato</b>. Ele mostra, numa lista, quem precisa de revisão, e avisa na '
         '<b>agenda do dia</b>, no <b>check-in</b> e no próprio <b>cadastro do paciente</b>. O prazo para sugerir uma nova '
         'revisão (em dias) é um <b>parâmetro</b> da clínica. O módulo vem <b>desligado</b> e é liberado por clínica pela '
         'Área do Administrador.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado. Os pacientes e as datas do exemplo foram ajustados só para este manual.')

blocks = [
    ('h2', 'Quando o cadastro precisa de revisão'),
    ('p', 'O sistema considera que o cadastro de um paciente <b>ativo</b> precisa de revisão quando acontece '
          '<b>pelo menos uma</b> destas situações:'),
    ('tabelagen', ['Situação', 'Como aparece', 'Exemplo'],
     [['Nunca revisado ou prazo vencido', 'Selo amarelo <b>Vencido</b> (ou <b>Nunca revisado</b>)',
       'Última revisão há 420 dias e o prazo da clínica é de 365 dias'],
      ['Endereço incompleto', 'Selo vermelho <b>Endereço</b>', 'Falta CEP, logradouro, número, bairro ou município'],
      ['Sem contato', 'Selo vermelho <b>Contato</b>', 'Nenhum celular, telefone ou e-mail preenchido']],
     [5, 6, 7]),
    ('aviso', 'Endereço incompleto e falta de contato valem <b>mesmo dentro do prazo</b>: um cadastro sem telefone '
              'precisa ser revisado hoje, não daqui a um ano.'),

    ('h2', 'Como ativar o módulo (administrador do sistema)'),
    ('p', 'O módulo é liberado por clínica, como os demais módulos do ClinSis. Na <b>Área do Administrador</b> '
          '(endereço <b>/area</b>), abra <b>Clínicas</b>, entre no cadastro da clínica e marque a opção '
          '<b>Revisão cadastral de pacientes</b>. Salve.'),
    ('aviso', 'Depois de ligar, os usuários da clínica precisam <b>sair e entrar de novo</b> no sistema: o módulo '
              'chega junto com o login. Desligado, nada do que está neste manual aparece.'),

    ('h2', 'Como definir o prazo (parâmetro)'),
    ('p', 'Em <b>Tabelas Aux. → Parâmetros</b> existe o parâmetro <b>RevisaoCadastralDias</b>, que define de quantos em '
          'quantos dias o cadastro deve ser revisado. O padrão é <b>365 dias</b>. Aceita de <b>30 a 1.825 dias</b>; '
          'um valor vazio, inválido ou fora dessa faixa volta ao padrão. Clique no lápis amarelo para alterar.'),
    ('img', '05-parametro.png', 'Tela de Parâmetros: o parâmetro de revisão cadastral, com valor 365.'),

    ('h2', 'Lista de pacientes para revisar'),
    ('p', 'Com o módulo ligado, aparece o menu <b>Paciente → Revisão cadastral</b> (para atendente e administrador). '
          'A lista mostra os pacientes ativos pendentes, dos mais antigos para os mais recentes, com nome, CPF, contato, '
          'data da última revisão (e quantos dias faz) e o motivo. No canto direito ficam o prazo em vigor e o total de pacientes.'),
    ('img', '02-lista.png', 'Lista de pendentes: prazo de 365 dias e 11 pacientes. Os selos mostram o motivo de cada um.'),
    ('p', 'Para trabalhar um grupo de cada vez, use o filtro <b>Motivo</b>: <i>Revisão vencida ou nunca feita</i>, '
          '<i>Endereço incompleto</i> ou <i>Sem celular, telefone ou e-mail</i>. Também dá para buscar pelo nome.'),
    ('img', '03-filtro-endereco.png', 'Filtro Endereço incompleto: só o paciente com o endereço faltando.'),
    ('img', '03b-filtro-contato.png', 'Filtro Sem celular, telefone ou e-mail.'),
    ('p', 'O botão com o lápis, em cada linha, abre o <b>cadastro do paciente</b> para conferir e atualizar os dados.'),

    ('h2', 'Confirmar que o cadastro está atualizado'),
    ('p', 'A revisão é registrada (data e usuário) de duas formas:'),
    ('tabelagen', ['Forma', 'Quando usar'],
     [['Salvar o cadastro do paciente', 'Você corrigiu endereço ou contato e salvou. Só conta como revisão se endereço e contato '
       'mínimos estiverem preenchidos; salvar com dado faltando não revisa.'],
      ['Botão <b>Confirmar dados atualizados</b> (no cadastro) ou <b>Marcar como revisado</b> (na lista)',
       'Você conferiu com o paciente e os dados já estavam corretos. Na lista, marque vários pacientes e confirme de uma vez.']],
     [6.5, 11.5]),
    ('img', '04-confirmar-lote.png', 'Marcar como revisado em lote: o sistema pede confirmação antes de gravar.'),
    ('img', '10-lista-depois.png', 'Depois de confirmar, o paciente sai da lista (de 11 para 10 pacientes).'),

    ('h2', 'Aviso na agenda do dia'),
    ('p', 'Na agenda, o paciente que precisa de revisão ganha um pequeno <b>cartão amarelo</b> antes do nome. Ao passar o '
          'mouse aparece o motivo, e o clique leva direto ao cadastro. Assim a recepção percebe o aviso antes mesmo do paciente chegar.'),
    ('img', '06-agenda-selo.png', 'Agenda: o cartão amarelo ao lado do nome do paciente indica cadastro a revisar.'),

    ('h2', 'Aviso no check-in'),
    ('p', 'No <b>check-in</b>, ao ler o cartão do paciente, uma faixa amarela informa o motivo. O aviso <b>não bloqueia</b> '
          'o check-in. O link <b>Abrir cadastro em outra aba</b> permite conferir os dados sem perder o atendimento em andamento.'),
    ('img', '07-checkin-aviso.png', 'Check-in: aviso de revisão com o motivo, acima dos agendamentos do dia.'),

    ('h2', 'Aviso no cadastro do paciente'),
    ('p', 'Ao abrir o cadastro de um paciente que precisa de revisão, aparece uma faixa amarela no topo com o motivo e o '
          'botão <b>Confirmar dados atualizados</b>.'),
    ('img', '08-cadastro-aviso.png', 'Cadastro do paciente com a faixa de revisão e o botão de confirmação.'),
    ('p', 'Ao confirmar, o sistema grava a revisão, a faixa some e o paciente deixa de aparecer na lista, na agenda e no check-in. '
          'Se houver alterações ainda não salvas no formulário, o sistema pede para salvar antes de confirmar.'),
    ('img', '09-cadastro-confirmado.png', 'Revisão confirmada: a faixa de aviso desapareceu.'),

    ('h2', 'Regras importantes'),
    ('tabelagen', ['Assunto', 'Como funciona'],
     [['Quem entra na lista', 'Somente pacientes <b>ativos</b>. Paciente inativo não aparece.'],
      ['Pacientes novos', 'Nascem com a data do cadastro como data da primeira revisão.'],
      ['Quando o módulo é ligado', 'Os pacientes existentes partem da data da última alteração do cadastro, para ninguém aparecer '
       'como vencido de uma só vez.'],
      ['Editar por outras telas', 'Alterar a pessoa pelo painel de Pessoa não conta como revisão; use o cadastro do paciente.'],
      ['Menores de idade', 'A revisão olha os dados do próprio paciente. Os dados do responsável não são avaliados nesta versão.'],
      ['Módulo desligado', 'Nenhuma tela, aviso ou menu do módulo aparece e as consultas retornam vazio.']],
     [5, 13]),
    ('aviso', 'Revisar é conferir com o paciente: pergunte se o telefone e o endereço continuam os mesmos antes de confirmar.'),
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
