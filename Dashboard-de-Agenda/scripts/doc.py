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
TITULO = "Dashboard de Agenda"
SUBTITULO = "O que significa cada informação da tela e como conferir cada uma no sistema"
VIDEO_NOME = "video-dashboard-agenda-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('O <b>Dashboard de Agenda</b> reúne, num só lugar, os principais números sobre os '
         'atendimentos agendados num período: quantas sessões aconteceram, quantos pacientes '
         'foram atendidos, taxas de presença/falta, ocupação da agenda e outros recortes '
         '(por profissional, especialidade, convênio, faixa etária, etc.). Este manual explica '
         '<b>o que cada card, gráfico e tabela representa</b> e, principalmente, <b>como o número é '
         'calculado</b> — para que qualquer valor exibido possa ser conferido manualmente se necessário.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Onde encontrar e o filtro de período'),
    ('p', 'Acesso em <b>Agenda → Dashboard Agenda</b> (restrito ao perfil administrador). Os únicos '
          'filtros da tela são <b>Período - Início</b> e <b>Período - Fim</b>; ao abrir a tela, eles já '
          'vêm preenchidos com o <b>mês corrente</b> (do dia 1 ao último dia do mês), e o botão '
          '"Limpar" (ícone de borracha) volta a esse padrão.'),
    ('img', '10-topo-cards.png', 'Filtros de período e os 8 cards de resumo no topo da tela.'),
    ('aviso', 'Existe um filtro de <b>Profissional</b> já implementado no backend, mas ele '
              '<b>não aparece na tela</b> hoje — na prática, o Dashboard sempre mostra todos os '
              'profissionais juntos, sem opção de filtrar por um profissional específico.'),
    ('p', 'Praticamente todos os blocos da tela contam <b>sessões</b> dentro do período — e "sessão" '
          'aqui é cada <b>data de atendimento</b> agendada (um agendamento recorrente de segunda e '
          'quarta, por exemplo, gera uma sessão para cada dia). A única exceção é o quadro '
          '"Faturamento por Convênio", explicado ao final, que usa outra data.'),

    ('h2', 'Os 8 cards do topo'),
    ('tabela', [
        ('Total de Sessões', 'Quantidade de sessões agendadas no período, com qualquer status (inclui as que ainda nem aconteceram, faltas e desmarcações).', 'Contagem de sessões no período'),
        ('Pacientes Atendidos', 'Quantidade de pacientes distintos que têm ao menos uma sessão no período. O nome pode sugerir "que compareceram", mas conta qualquer status, inclusive falta e desmarcação.', 'Pacientes distintos com sessão no período'),
        ('Taxa de Presença', 'Presentes ÷ (Presentes + Ausentes) × 100. Só compara quem esteve presente com quem faltou puro — não entra no cálculo quem desmarcou, teve ausência justificada ou está sem status.', 'Presentes / (Presentes + Ausentes)'),
        ('Taxa de Absenteísmo', 'Ausentes ÷ (Presentes + Ausentes) × 100 — é o espelho exato da Taxa de Presença (as duas somam 100%). Mesma ressalva: ignora desmarcações e ausência justificada.', 'Ausentes / (Presentes + Ausentes)'),
        ('Pacientes Novos', 'Entre os pacientes atendidos no período, quantos tiveram a <b>primeira sessão de toda a história</b> deles na clínica dentro desse período.', 'Primeira sessão do paciente cai dentro do período'),
        ('Pacientes Recorrentes', 'O restante dos pacientes atendidos: já tinham ao menos uma sessão <b>antes</b> do início do período filtrado.', 'Primeira sessão do paciente é anterior ao período'),
        ('Dias de Antecedência (média)', 'Média de quantos dias antes da sessão o agendamento foi cadastrado no sistema (data do agendamento menos data de inclusão do registro).', 'Média de (Data da Sessão − Data de Cadastro)'),
        ('Taxa de Ocupação', 'Total de Sessões ÷ Capacidade Total da agenda × 100. O número entre parênteses no card mostra as duas partes da conta (ex.: "70 de 2319").', 'Total de Sessões / Capacidade Total'),
    ]),
    ('aviso', '<b>Taxa de Ocupação</b> tem um ícone de informação (ⓘ) com a explicação completa direto '
              'na tela: a "capacidade" soma todos os horários fixos e avulsos configurados na Agenda de '
              'cada profissional no período, já descontando os feriados cadastrados em '
              '<b>Tabelas Aux. → Feriados</b>. <b>Férias ou bloqueios individuais de um profissional '
              'específico ainda não são descontados</b> dessa capacidade — então, se algum profissional '
              'tirou férias no período, a taxa de ocupação real fica um pouco menor do que a exibida '
              '(o denominador conta uma capacidade maior do que a disponível de fato).'),

    ('h2', 'Gráfico "Presença x Ausência x Desmarcações"'),
    ('p', 'Pizza com todas as sessões do período divididas pelo status: Presentes, Ausentes, Ausência '
          'Justificada, Desmarcado Paciente, Desmarcado Profissional e Remarcações.'),
    ('img', '11-graficos.png', 'Gráfico de pizza (status das sessões) e gráfico de linha (evolução diária) lado a lado.'),
    ('aviso', 'Sessões sem nenhum status definido ("em aberto", ainda não marcadas como presente/falta) '
              'não aparecem em nenhuma fatia desse gráfico nem em nenhum outro card — elas só entram no '
              'card "Total de Sessões". Se o total de sessões for maior que a soma de todas as fatias, é '
              'porque existem sessões sem status no período.'),

    ('h2', 'Gráfico "Evolução Diária"'),
    ('p', 'Duas linhas — Presentes e Ausentes — mostrando, dia a dia dentro do período, quantas sessões '
          'tiveram cada um desses dois status. As demais categorias (desmarcação, ausência justificada) '
          'não entram nesse gráfico, só no de pizza acima.'),

    ('h2', 'Tabelas "Por Profissional", "Por Especialidade" e "Particular x Convênio"'),
    ('img', '12-tabelas-profissional-especialidade.png',
     'Tabelas "Por Profissional" (sessões/presentes/ausentes), "Por Especialidade" e "Particular x Convênio"/"Por Operadora".'),
    ('tabela', [
        ('Por Profissional', 'Sessões, Presentes e Ausentes de cada profissional no período, ordenado do maior para o menor número de sessões.', 'Agrupado por profissional'),
        ('Por Especialidade', 'Total de sessões de cada especialidade no período.', 'Agrupado por especialidade da agenda'),
        ('Particular x Convênio', 'Quantas sessões foram marcadas como Particular e quantas como Convênio.', 'Campo "Particular" da agenda'),
        ('Por Operadora', 'Total de sessões de cada operadora/convênio.', 'Agrupado por operadora da agenda'),
    ]),
    ('aviso', 'A coluna <b>"Desmarcações"</b> que aparece em outras telas do sistema, quando existir '
              'aqui, soma Desmarcado Paciente + Desmarcado Profissional num único número (não separa '
              'quem desmarcou). Já no card "Particular x Convênio": uma sessão sem essa marcação '
              'preenchida é contabilizada como <b>Convênio</b>, não fica de fora da conta.'),

    ('h2', '"Por Método" e "Por Programa"'),
    ('img', '13-metodo-programa.png', 'Tabelas "Por Método" e "Por Programa" — só aparecem se a clínica tiver essas opções habilitadas.'),
    ('p', 'Esses dois quadros só aparecem se a clínica tiver, no cadastro dela, a exibição de Método e/ou '
          'de Programa da Agenda habilitada. Contam sessões que têm um Método/Programa definido — '
          'sessões sem essa informação preenchida não entram na lista, mesmo que o quadro esteja visível.'),

    ('h2', 'Gráfico "Sessões por Faixa Etária"'),
    ('p', 'Sessões agrupadas pela <b>idade do paciente na data de cada sessão</b> (não a idade atual '
          'dele), em faixas de 0–10, 11–20, 21–30, 31–40 e 41 anos ou mais. Por isso, um mesmo paciente '
          'pode contribuir para faixas diferentes se tiver sessões espalhadas por datas distantes '
          '(ex.: fazendo aniversário de faixa no meio do período analisado).'),
    ('img', '14-faixa-etaria-dias-horarios.png', 'Gráfico de barras por faixa etária e tabela "Dias e Horários Mais Concorridos".'),

    ('h2', 'Tabela "Dias e Horários Mais Concorridos"'),
    ('p', 'Mostra as combinações de dia da semana + horário com mais sessões marcadas no período — útil '
          'para identificar os horários de pico da agenda. A tela exibe apenas o <b>Top 10</b>; existem '
          'mais combinações calculadas por trás, mas só as 10 primeiras (por quantidade de sessões) são '
          'mostradas.'),

    ('h2', 'Tabela "Faturamento por Convênio"'),
    ('img', '15-faturamento-convenio.png', 'Faturamento por Convênio: valor faturado e valor recebido, por operadora.'),
    ('aviso', '<b>Esta é a única tabela da tela que NÃO usa a data da sessão.</b> O próprio título traz '
              'o aviso "(por data de recebimento, não por data da sessão)": o período do filtro aqui '
              'passa a valer sobre a <b>data em que a baixa do pagamento da guia foi registrada no '
              'Financeiro</b>. Uma sessão atendida em um mês pode ter sua guia recebida (e portanto '
              'contabilizada aqui) só em outro mês.'),
    ('tabela', [
        ('Valor Faturado', 'Soma do valor das guias de faturamento cujo recebimento caiu dentro do período filtrado.', 'Guias com baixa no período'),
        ('Valor Recebido', 'Soma do valor efetivamente pago (baixado) dessas guias no período.', 'Baixas de Conta a Receber no período'),
    ]),
    ('aviso', 'Guias já faturadas mas que <b>ainda não tiveram nenhuma baixa de recebimento</b> não '
              'aparecem nessa lista — o quadro mostra só o que já foi efetivamente recebido no período.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Agenda.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Agenda_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Agenda.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
