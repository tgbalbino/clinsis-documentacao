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
DATA = "23/09/2026"
TITULO = "Prontuário — Auditoria e Relatórios"
SUBTITULO = "Como conferir se cada atendimento gerou prontuário: Auditoria, Produção e Atendimentos Sequenciais"
VIDEO_NOME = "video-prontuario-auditoria-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('Este manual é para o <b>administrador</b>. Ele explica como conferir, mês a mês, se os atendimentos realizados '
         '(presenças) geraram <b>prontuários finalizados</b>, quais ficaram em digitação e quais estão <b>sem tag</b>. '
         'São três relatórios em <b>Relatórios</b>: <b>Auditoria de Prontuários</b>, <b>Produção de Prontuários</b> e '
         '<b>Atendimentos Sequenciais</b>, além das configurações da clínica que mudam a contagem.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de homologação, clínica de '
          'testes "Homologação" (Clínica 1), com o usuário administrador de teste. Nenhum dado de produção foi acessado. '
          'Os números dos exemplos são de Setembro/2026 nessa clínica de teste.')

blocks = [
    ('h2', 'Para que serve cada relatório'),
    ('tabelagen', ['Relatório', 'Pergunta que responde', 'Onde'],
     [
         ['Auditoria de Prontuários', 'Cada profissional fez prontuário dos atendimentos que realizou no mês?', 'Relatórios (painel) → Auditoria'],
         ['Produção de Prontuários', 'Quantos prontuários foram finalizados, estão em digitação ou foram excluídos por profissional e tipo, em um período?', 'Relatórios (painel) → Produção de Prontuários'],
         ['Atendimentos Sequenciais', 'Quais atendimentos em horários seguidos o sistema junta como um só na auditoria?', 'Relatórios (painel) → Atendimentos Sequenciais'],
     ], [4.5, 8.0, 5.0]),

    ('h2', '1. Auditoria de Prontuários'),
    ('img', '01-auditoria.png', 'Filtros da auditoria: Agenda e Tipo são obrigatórios; Profissional, Método e Tag são opcionais.'),
    ('tabelagen', ['Filtro', 'Para que serve'],
     [
         ['Agenda *', 'O mês da agenda a auditar (ex.: 2026 - SETEMBRO). É obrigatório.'],
         ['Tipo de Prontuário *', 'Qual tipo conferir (Anamnese, Evolução diária...). Obrigatório: cada consulta olha um tipo por vez.'],
         ['Profissional', 'Restringe a um profissional.'],
         ['Método', 'Restringe aos atendimentos desse método de atendimento (e, se a clínica usa tags, aos prontuários com essa tag).'],
         ['Tag', 'Só prontuários que tenham essa tag.'],
         ['Tipo de Relatório', '<b>Sintético</b> (uma linha por profissional) ou <b>Analítico</b> (uma linha por profissional e paciente).'],
     ], [4.5, 13.0]),
    ('img', '04-sintetico.png', 'Auditoria sintética de Setembro/2026, tipo Anamnese.'),
    ('tabela', [
        ('Presenças', 'Quantidade de sessões marcadas como Presente na agenda do mês (data da sessão registrada). É o número de atendimentos realizados.', 'AgendaProfissionalDiaPac (status 3)'),
        ('Finalizado', 'Prontuários do tipo escolhido com situação Finalizada e data de emissão dentro do mês. Prontuários excluídos não contam.', 'Prontuario.Situacao = F'),
        ('Não Finalizado', 'Prontuários em Digitação (rascunho). Rascunhos sem data de emissão entram pelo mês da criação.', 'Prontuario.Situacao = D'),
        ('Sem Tag', 'Prontuários sem nenhuma tag (relevante nas clínicas que usam tags).', 'ProntuarioTag'),
    ]),
    ('p', 'A linha do profissional fica em <b>vermelho</b> quando o número de <b>Finalizado é diferente de Presenças</b>. Em regra, cada presença deveria '
          'ter um prontuário finalizado. No exemplo, o PSICANALISTA tem 5 presenças, mas só 2 prontuários finalizados, então merece conferência.'),
    ('img', '05-analitico.png', 'Analítico: mostra por paciente onde falta prontuário (por exemplo, paciente com presença e nenhum prontuário finalizado).'),
    ('p', 'Use <b>Exportar</b> (depois de pesquisar) para baixar o resultado em <b>CSV</b> (arquivo "AuditoriaProntuario.csv", com o tipo e a agenda no topo).'),
    ('img', '10-sintetico-evolucao.png', 'Tipo Evolução diária em Setembro/2026: 4 prontuários em digitação e 14 finalizados para o PSICANALISTA.'),
    ('aviso', '<b>Correções feitas nesta documentação:</b> (1) rascunhos sem data de emissão não entravam no mês e por isso "Não Finalizado" ficava '
              'menor do que o real (em Setembro havia 4 rascunhos de Evolução diária e o relatório mostrava só 1); agora usam a data de criação. '
              '(2) O relatório de <b>Produção</b> contava prontuários excluídos também como Finalizado/Digitação; agora conta só os ativos e mostra os '
              'excluídos à parte.'),
    ('aviso', '<b>Limites a saber:</b> o relatório conta prontuários pela data de emissão; e existe uma coluna "Fora da Agenda" (prontuário de paciente '
              'sem marcação no mês) que está oculta temporariamente na tela, em revisão.'),

    ('h2', '2. Produção de Prontuários'),
    ('img', '07-producao-resultado.png', 'Produção de Anamnese entre 01/09 e 30/09/2026: por profissional e tipo.'),
    ('p', 'Escolha o <b>Tipo de Relatório</b> (<b>Total do Período</b> ou <b>Diário</b>), o tipo de prontuário, o período de emissão, e opcionalmente '
          'profissional e tag. As colunas são <b>Finalizado</b>, <b>Digitação</b> e <b>Excluído</b>. O modo Diário abre uma linha por dia de emissão. '
          'Ao contrário da auditoria, este relatório não olha as presenças da agenda: mede apenas a produção de prontuários.'),

    ('h2', '3. Configurações da clínica que mudam a auditoria'),
    ('p', 'Três opções da Configuração Auxiliar (ativadas por clínica pelos scripts 137 e 138) alteram a contagem e o comportamento do prontuário:'),
    ('tabelagen', ['Opção', 'O que muda'],
     [
         ['PRONTUARIO_TAGS', 'Liga as tags no prontuário e o filtro de Método/Tag na auditoria. O profissional precisa ter ao menos 1 tag para finalizar.'],
         ['PRONT_TAG_AUTO', 'Ao criar o prontuário, aplica a tag do método da agenda quando o paciente tem um único método no mês com o profissional.'],
         ['AUD_PRONT_DUPLO_1', '<b>Atendimento duplo conta como 1</b> nas Presenças da auditoria: dois horários consecutivos (mesma agenda, profissional, paciente, método e dia da semana) contam uma presença só, pois gera-se um único prontuário.'],
     ], [4.5, 13.0]),
    ('p', 'As três estão ligadas na Clínica 1 (Homologação). Os scripts <b>137</b> (clínica 6, com métodos e preenchimento de tags) e <b>138</b> (clínicas 1 e 6) só '
          'cadastram e habilitam essas opções, e podem ser executados mais de uma vez.'),

    ('h2', '4. Atendimentos Sequenciais'),
    ('p', 'Este relatório mostra os pares (ou cadeias) de horários que o sistema trata como um atendimento único quando <b>AUD_PRONT_DUPLO_1</b> está ligada. '
          'Escolha a <b>Agenda</b> (obrigatória), e opcionalmente Profissional e Método.'),
    ('img', '06-sequenciais-resultado.png', 'Atendimentos sequenciais de Setembro/2026: paciente, método, dia, horários e as presenças de cada horário.'),
    ('tabelagen', ['Coluna', 'Significado'],
     [
         ['Dia / Horários', 'Dia da semana e os dois horários seguidos (ex.: Segunda, 12:20 - 12:30).'],
         ['Presenças 1º horário / 2º horário', 'Quantas vezes o paciente esteve presente em cada um dos dois horários no mês.'],
         ['Atendimento Sequencial', 'Em quantas datas os <b>dois</b> horários tiveram presença ao mesmo tempo. Cada uma dessas datas conta como <b>1</b> na auditoria.'],
     ], [5.5, 12.0]),
    ('aviso', '<b>Como conferir:</b> para cada par listado, a Auditoria conta <b>1 atendimento por data</b> em que houve presença nos dois horários, e não 2. '
              'Assim, um paciente com dois horários seguidos e presença nos dois gera um só prontuário esperado.'),

    ('h2', 'Roteiro de conferência mensal'),
    ('tabelagen', ['Passo', 'O que fazer'],
     [
         ['1', 'Abra a Auditoria (sintético) do mês e do tipo principal (ex.: Evolução diária).'],
         ['2', 'Procure as linhas em vermelho (Finalizado diferente de Presenças).'],
         ['3', 'Veja o analítico dessas linhas para achar o paciente sem prontuário.'],
         ['4', 'Confira a coluna Não Finalizado e cobre os rascunhos; confira Sem Tag, se a clínica usa tags.'],
         ['5', 'Se a diferença vier de atendimentos em horários seguidos, confira no relatório de Atendimentos Sequenciais.'],
         ['6', 'Use a Produção para acompanhar o total finalizado no período e exporte em CSV quando precisar.'],
     ], [2.0, 15.5]),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Auditoria.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Auditoria_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Auditoria.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
