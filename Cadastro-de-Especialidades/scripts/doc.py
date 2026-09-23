# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = "1.0"
DATA = "22/09/2026"
TITULO = "Cadastro de Especialidades"
SUBTITULO = '"Tipo de Cobrança" e "Relatório Compartilhado(Prontuários)" explicados com exemplos'
VIDEO_NOME = "video-especialidade-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('O cadastro de <b>Especialidade</b> (Psicologia, Fisioterapia, Fonoaudiologia, etc.) tem duas '
         'configurações que mudam o comportamento de outras partes do sistema, mas cujo efeito nem '
         'sempre é óbvio pelo nome: <b>Tipo de Cobrança</b> (usada só no Pagamento de Profissionais) e '
         '<b>Relatório Compartilhado(Prontuários)</b> (usada só no Prontuário). Este manual explica as '
         'duas em detalhe, com exemplos.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Onde fica o cadastro'),
    ('p', 'Acesso em <b>Tabelas Aux. → Especialidade</b> (rota <i>aux/especialidade</i>). Além de '
          'Descrição, Abreviação e Ativo, cada especialidade tem os dois campos explicados abaixo — '
          'que <b>não afetam o cadastro em si</b>, e sim como outras telas do sistema se comportam para '
          'os atendimentos daquela especialidade.'),
    ('img', '00-lista-especialidades.png',
     'Lista de Especialidades já mostra as colunas "Tipo de Cobrança" e "Relatório Compartilhado" — repare como cada uma tem uma combinação diferente.'),
    ('img', '01-cadastro-tipo-cobranca-rel-compartilhado.png',
     'Modal de cadastro: os campos "Tipo de Cobrança" e "Relatório Compartilhado(Prontuários)", com a explicação já disponível na própria tela (texto pequeno abaixo do segundo campo).'),

    ('h2', 'Tipo de Cobrança — usado só no Pagamento de Profissionais'),
    ('p', 'Essa opção só é lida em <b>um único lugar do sistema</b>: o cálculo do relatório de '
          '<b>Pagamento de Profissionais</b> (analítico e resumido). Ela não afeta a cobrança do '
          'paciente/convênio nem a geração de guias — só quanto o profissional recebe pelo '
          'atendimento.'),
    ('tabela', [
        ('Por Sessão', 'Paga uma vez para CADA sessão realizada (presença confirmada) no mês, dentro daquele agendamento.', 'Relatorio_Query.cs'),
        ('Paciente', 'Paga só 1 vez por paciente/agendamento no mês, não importa quantas sessões ele teve — é um valor "fechado" por paciente, não por sessão.', 'Relatorio_Query.cs'),
    ]),
    ('aviso', '<b>Exemplo:</b> a especialidade "Fonoaudiologia" está configurada como <i>Por Sessão</i>. '
              'Se o paciente João teve 4 sessões confirmadas no mês com a profissional Maria, o '
              'relatório de Pagamento de Profissionais calcula <b>4 sessões a pagar</b> (4 × valor da '
              'sessão) para Maria. Já a especialidade "Avaliação Neuropsicológica" está configurada como '
              '<i>Paciente</i>: mesmo que o paciente tenha tido 3 sessões marcadas naquele mês, o '
              'sistema conta <b>apenas 1 unidade a pagar</b> — o "pacote" é pago uma única vez, e não '
              'por sessão.'),
    ('p', 'Faz sentido usar <i>Paciente</i> em especialidades que cobram um valor fechado por avaliação '
          'ou processo (mesmo que ele tome várias sessões), e <i>Por Sessão</i> nas especialidades onde '
          'o profissional é remunerado por atendimento individual.'),

    ('h2', 'Relatório Compartilhado(Prontuários) — usado só no Prontuário'),
    ('p', 'Controla se um profissional consegue ver o <b>prontuário já finalizado</b> de OUTRO '
          'profissional, quando os dois atendem o mesmo paciente. Um prontuário em rascunho/digitação '
          '<b>nunca</b> é compartilhado, não importa a configuração — só depois de finalizado.'),
    ('tabela', [
        ('Não', 'Prontuários finalizados dessa especialidade nunca ficam visíveis para outro profissional (só quem escreveu, ou um administrador).', 'ProntuarioRepository.cs'),
        ('Somente mesma especialidade', 'Outro profissional só vê o prontuário se ele também for da mesma especialidade E também atender aquele paciente.', 'ProntuarioRepository.cs'),
        ('Qualquer profissional do mesmo paciente', 'Qualquer profissional que atenda aquele paciente pode ver o prontuário finalizado, mesmo sendo de outra especialidade.', 'ProntuarioRepository.cs'),
    ]),
    ('aviso', '<b>Exemplo:</b> a especialidade "Psicologia" está configurada como <i>Somente mesma '
              'especialidade</i>. A psicóloga Ana atende o paciente Pedro e finaliza um prontuário. A '
              'psicóloga Beatriz, que também atende Pedro, <b>consegue ver</b> o prontuário finalizado '
              'de Ana. Mas o fisioterapeuta Carlos, que também atende Pedro, <b>não consegue</b>, pois '
              'não é da mesma especialidade. Se a especialidade fosse <i>Qualquer profissional do mesmo '
              'paciente</i>, Carlos também conseguiria ver.'),
    ('p', 'Na tela de Prontuário (acesso do profissional), existe o campo <b>"Emitente"</b>, que só '
          'aparece para o usuário logado como Profissional: ao escolher uma opção diferente de '
          '"Próprio", a lista passa a trazer também prontuários de outros profissionais — e é '
          'exatamente essa configuração da Especialidade que decide quais prontuários de terceiros '
          'aparecem nessa busca.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Especialidade.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Especialidade_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Especialidade.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
