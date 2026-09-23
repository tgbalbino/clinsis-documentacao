# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = "2.0"
DATA = "23/09/2026"
TITULO = "Dashboard de Agenda"
SUBTITULO = "O que significa cada informação e como conferir cada uma no sistema"
VIDEO_NOME = "video-dashboard-agenda-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('O <b>Dashboard de Agenda</b> reúne, num só lugar, números sobre os atendimentos de um '
         'período: sessões, pacientes, presença/falta, ocupação da agenda e faturamento por convênio. '
         'Este manual explica <b>o que cada card, gráfico e tabela representa</b>, <b>como o número é '
         'calculado</b> e, principalmente, <b>como conferir cada valor dentro do sistema</b> — com um '
         'exemplo real passo a passo (Setembro/2026).')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Onde encontrar e o filtro de período'),
    ('p', 'Acesso em <b>Agenda → Dashboard Agenda</b> (perfil administrador). Os filtros são '
          '<b>Período - Início</b> e <b>Período - Fim</b>; ao abrir, vêm com o <b>mês corrente</b>, e o '
          'botão de borracha volta a esse padrão. O filtro de Profissional existe no sistema, mas não '
          'aparece na tela: o Dashboard sempre mostra todos os profissionais juntos.'),
    ('img', '40-dashboard-setembro-cards.png', 'Dashboard filtrado para Setembro/2026 (01/09 a 30/09) — os números deste exemplo serão conferidos abaixo.'),

    ('h2', 'Atenção: o que o Dashboard conta como "sessão"'),
    ('aviso', '<b>O Dashboard só enxerga sessões que já têm uma data registrada.</b> O sistema só grava '
              'essa data quando a sessão é marcada como <b>PRESENTE, AUSENTE, AUSENTE - JUSTIFICATIVA ou '
              'REMARCAÇÃO</b>. Por isso: (1) sessões ainda pendentes ("****", sem marcação) '
              '<b>não aparecem</b>; (2) <b>PAC. DESMARCOU</b> e <b>PRO. DESMARCOU</b> <b>não aparecem</b> '
              '(as fatias "Desmarcado" do gráfico normalmente ficam vazias). Em outras palavras, o '
              'Dashboard mostra <b>sessões registradas</b>, e não todas as sessões agendadas.'),
    ('p', '<b>Exemplo real (Agenda de Setembro/2026):</b> a agenda tem 165 sessões previstas — 150 ainda '
          'pendentes, 10 marcadas como Presente e 5 como Ausente. O Dashboard mostra <b>15</b> '
          '(10 + 5). Os relatórios de Agenda (que contam as sessões previstas) mostram 165.'),

    ('h2', 'Exemplo passo a passo: conferindo Total de Sessões, Presença e Absenteísmo'),
    ('p', 'Estes números do Dashboard de Setembro: <b>Total de Sessões = 15</b>, <b>Taxa de Presença = '
          '66,7%</b>, <b>Taxa de Absenteísmo = 33,3%</b>. Para conferir dentro da Agenda:'),
    ('tabelagen', ['Passo', 'O que fazer'],
     [
         ['1', 'Menu <b>Agenda</b> → na linha do mês (2026 / SETEMBRO) clique em <b>Ver Agenda</b>.'],
         ['2', 'Clique em <b>Filtros</b>. No campo <b>Sessão 1</b>, escolha <b>PRESENTE</b> e clique em <b>Filtrar</b>. Veja no rodapé: <b>"Total de registros: 8"</b>.'],
         ['3', 'Repita trocando para <b>Sessão 2</b> (resultado: 1), <b>Sessão 3</b> (1), <b>Sessão 4</b> (0) e <b>Sessão 5</b> (0). Some: 8 + 1 + 1 = <b>10 presentes</b>.'],
         ['4', 'Repita tudo com <b>AUSENTE</b>: Sessão 1 = 3, Sessão 2 = 2, demais 0. Soma = <b>5 ausentes</b>.'],
         ['5', 'Total de Sessões = 10 + 5 = <b>15</b>. Taxa de Presença = 10 ÷ 15 = <b>66,7%</b>. Taxa de Absenteísmo = 5 ÷ 15 = <b>33,3%</b>. Bate com o Dashboard.'],
     ], [1.6, 15.9]),
    ('img', '22-agendamento-grade-mes.png', 'Tela Agenda de Setembro/2026 (Ver Agenda): sem filtros mostra 150 linhas de agendamento (cada linha pode ter até 5 sessões).'),
    ('img', '23a-modal-filtro-sessao1-presente.png', 'Filtros → Sessão 1 = PRESENTE.'),
    ('img', '23-agendamento-filtro-sessao1-presente.png', 'Resultado: "Total de registros: 8" — as linhas cuja Sessão 1 é PRESENTE.'),
    ('aviso', 'Por que somar as 5 colunas? A grade tem <b>uma linha por agendamento</b>, com até 5 sessões '
              '(Sessão 1 a 5). O Dashboard conta <b>cada sessão</b>, então é preciso somar o resultado de '
              'cada coluna. Se o período passar de um mês, repita para cada mês (a Agenda é mensal) e '
              'some — o Dashboard usa a <b>data da sessão</b>, não o mês da agenda.'),

    ('h2', 'Taxa de Absenteísmo: o que é e como conferir'),
    ('p', '<b>Absenteísmo</b> é a taxa de faltas: <b>Ausentes ÷ (Presentes + Ausentes) × 100</b>. É o '
          'complemento exato da Taxa de Presença (as duas somam 100%). Só entram na conta as sessões '
          'marcadas <b>PRESENTE</b> e <b>AUSENTE</b>; <b>AUSENTE - JUSTIFICATIVA</b>, remarcações e '
          'desmarcações <b>ficam fora</b> da fórmula.'),
    ('p', '<b>Como conferir na Agenda:</b> use o passo a passo acima (Filtros → Sessão 1 a 5 = AUSENTE e '
          'PRESENTE) e faça a divisão. Exemplo de Setembro: 5 ÷ (10 + 5) = 33,3%.'),
    ('img', '24-relatorio-qtd-marcacao.png', 'Alternativa mais rápida: Relatórios → Agenda - Qtd Marcação (escolha a Agenda 2026/SETEMBRO) traz Presentes e Ausentes por profissional.'),
    ('aviso', 'Cuidados ao usar o relatório "Agenda - Qtd Marcação": (1) a linha <b>TOTAL soma só a '
              'página que está na tela</b> — em Setembro a página 1 mostra 5 presentes / 2 ausentes e a '
              'página 2 mostra 5 / 3; some as páginas (total real: <b>10 presentes e 5 ausentes</b>). '
              '(2) A coluna <b>Ausentes</b> desse relatório <b>inclui</b> "Ausente - Justificativa", '
              'enquanto o Dashboard conta só AUSENTE. (3) A coluna "Qtde. Sessões" é o número de '
              'sessões <b>previstas</b> (165 em Setembro), não as registradas (15).'),

    ('h2', 'Os 8 cards do topo — o que são e como conferir'),
    ('tabelagen', ['Card', 'O que é / como é calculado', 'Como conferir no sistema'],
     [
         ['Total de Sessões', 'Quantidade de sessões <b>registradas</b> (com data) no período: Presente, Ausente, Ausente-Justificativa e Remarcação.', 'Agenda → Ver Agenda → Filtros → somar as colunas Sessão 1 a 5 por status (exemplo acima).'],
         ['Pacientes Atendidos', 'Pacientes <b>distintos</b> com ao menos uma sessão registrada no período (inclui quem faltou).', 'Na Agenda filtrada (Sessão = PRESENTE/AUSENTE), contar os nomes diferentes da coluna Paciente.'],
         ['Taxa de Presença', 'Presentes ÷ (Presentes + Ausentes) × 100.', 'Contagens de PRESENTE e AUSENTE na Agenda (exemplo acima).'],
         ['Taxa de Absenteísmo', 'Ausentes ÷ (Presentes + Ausentes) × 100.', 'Idem — ver seção anterior.'],
         ['Pacientes Novos', 'Pacientes cuja <b>primeira sessão registrada de toda a história</b> cai dentro do período.', 'Relatórios → Histórico do Paciente (aba Agenda). A lista vem do mais recente para o mais antigo: vá até a <b>última página</b> para ver a primeira sessão.'],
         ['Pacientes Recorrentes', 'Pacientes do período que já tinham sessão registrada <b>antes</b> do início do período.', 'Mesma consulta acima (primeira sessão anterior ao início do período).'],
         ['Dias de Antecedência (média)', 'Média de dias entre a data de inclusão do agendamento e a data da sessão.', '<b>Não há tela que mostre a data de inclusão do agendamento</b> — hoje só é possível conferir por consulta ao banco. Ver "Relatórios previstos".'],
         ['Taxa de Ocupação', 'Total de Sessões ÷ Capacidade Total × 100 (o card mostra "15 de 629"). Capacidade = horários configurados para os profissionais no período, descontados os feriados.', 'Agenda → <b>Prof. horários</b> (escolha o profissional) lista os horários semanais/avulsos configurados. A capacidade é a soma desses horários ao longo dos dias do período. Não há tela que já traga o total.'],
     ], [3.0, 7.2, 7.3]),
    ('img', '42-prof-horarios.png', 'Agenda → Prof. horários (Profissional 01, Setembro/2026): cada linha da tabela é um horário disponível; a capacidade do card soma esses horários pelos dias do período.'),
    ('aviso', '<b>Taxa de Ocupação</b>: como só as sessões registradas entram no numerador, a taxa fica '
              'baixa em meses em andamento (2,4% em Setembro, com muitas sessões ainda pendentes). '
              'Férias ou bloqueios de um profissional específico não são descontados da capacidade — só '
              'feriados cadastrados em Tabelas Aux. → Feriados (isso já aparece no tooltip do card).'),

    ('h2', 'Gráficos'),
    ('tabelagen', ['Gráfico', 'O que mostra', 'Como conferir'],
     [
         ['Presença x Ausência x Desmarcações (pizza)', 'Sessões registradas por status. As fatias "Desmarcado Paciente/Profissional" normalmente ficam vazias (esses status não gravam data).', 'Mesmas contagens da Agenda por status (Filtros → Sessão n).'],
         ['Evolução Diária', 'Presentes e Ausentes de cada dia do período.', 'Agenda → Filtros → campo <b>Data</b> (um dia) + Sessão n = PRESENTE/AUSENTE; ou Relatório "Marcação sessão dia" (Agenda → Relatórios).'],
         ['Sessões por Faixa Etária', 'Sessões por idade do paciente <b>na data da sessão</b> (0–10, 11–20, 21–30, 31–40, 41+).', 'Sem tela de conferência; usa a data de nascimento do cadastro do paciente.'],
     ], [4.0, 7.0, 6.5]),
    ('img', '11-graficos.png', 'Gráficos de pizza (status) e de linha (evolução diária).'),

    ('h2', 'Tabelas do Dashboard'),
    ('tabelagen', ['Tabela', 'O que mostra', 'Como conferir'],
     [
         ['Por Profissional', 'Sessões, Presentes e Ausentes de cada profissional.', 'Agenda → Filtros → Profissionais (marque um) + Sessão n; ou relatório Agenda - Qtd Marcação (uma linha por profissional).'],
         ['Por Especialidade', 'Sessões registradas por especialidade.', 'Agenda: a coluna Espec. tem filtro no cabeçalho; combine com Sessão n.'],
         ['Particular x Convênio', 'Sessões particulares × demais (sem marcação de Particular conta como Convênio).', 'Agenda → Filtros → Particular (Sim/Não) + Sessão n.'],
         ['Por Operadora', 'Sessões por convênio/operadora.', 'Agenda: coluna Plano (filtro no cabeçalho) + Sessão n.'],
         ['Por Método / Por Programa', 'Só aparecem se a clínica usa Método/Programa; contam sessões que têm essa informação.', 'Agenda → Filtros → Método (e coluna de programa, se habilitada).'],
         ['Dias e Horários Mais Concorridos', 'Top 10 de dia da semana + horário com mais sessões registradas.', 'Agenda: filtros de cabeçalho <b>Dia</b> e <b>Hora</b> (ou Filtros → Dias) + Sessão n. Lembre: o Dashboard conta sessões; a grade conta linhas.'],
     ], [3.4, 6.6, 7.5]),
    ('img', '12-tabelas-profissional-especialidade.png', 'Tabelas Por Profissional, Por Especialidade, Particular x Convênio e Por Operadora.'),

    ('h2', 'Faturamento por Convênio: de onde vem e como conferir'),
    ('aviso', '<b>Este é o único quadro que não usa a data da sessão.</b> O período filtra a <b>data do '
              'pagamento (baixa)</b> registrado no Financeiro. Uma sessão de um mês pode ser paga em '
              'outro.'),
    ('p', '<b>De onde vem:</b> só entram <b>guias de faturamento</b> (Doc. Faturamento) que já tiveram '
          '<b>baixa</b> em Contas a Receber dentro do período. <b>Valor Faturado</b> = valor da guia '
          'faturada; <b>Valor Recebido</b> = soma das baixas (valor pago) dessa conta. Guias faturadas '
          'sem nenhuma baixa no período não aparecem.'),
    ('img', '43-faturamento-corrigido.png', 'Quadro Faturamento por Convênio (01/01 a 30/09/2026): Operadora PROPRIO — Faturado R$ 1.223,00 / Recebido R$ 1.373,00.'),
    ('p', '<b>Como conferir hoje:</b> (1) <b>Doc. Faturamento → Listar</b> (botão "Listar Últimos" ou '
          '"Filtros") mostra as guias: número, paciente, emissão, sessões, status, localização e a coluna '
          'Faturamento; (2) <b>Relatórios → Financeiro - Recebimentos (Contas a Receber)</b>, com '
          '<b>Filtros → Data inicial/final</b> = o período do Dashboard, lista as baixas (data, forma, '
          'valor original, valor pago) com o total no rodapé.'),
    ('p', '<b>No exemplo:</b> aparecem 4 baixas com o nome "PROPRIO" na coluna Paciente. Três delas '
          'têm valor original de R$ 1.223,00 (a conta da guia): R$ 1.023,00 + R$ 200,00 + R$ 150,00 = '
          '<b>R$ 1.373,00 recebidos</b>, que é o valor do quadro. A quarta (R$ 180,00, valor original '
          'R$ 200,00) é de <b>outra conta a receber, que não é de guia</b>, e por isso não entra no quadro.'),
    ('img', '32-relatorio-recebimentos-periodo.png', 'Financeiro - Recebimentos com período 01/01 a 30/09/2026: as baixas de "PROPRIO" somam o Valor Recebido do quadro.'),
    ('aviso', '<b>Correção realizada nesta revisão:</b> o quadro estava somando o valor faturado da guia '
              '<b>uma vez para cada baixa</b> (uma guia de R$ 1.223,00 com 3 baixas aparecia como '
              'R$ 3.669,00). Já corrigido: agora cada guia é contada uma única vez. <b>Limitação:</b> '
              'nenhuma tela do sistema agrupa faturado/recebido por operadora — a conferência por convênio '
              'é manual (identificando as guias de cada operadora em Doc. Faturamento → Listar).'),

    ('h2', 'Quadro resumo: onde conferir cada informação'),
    ('tabelagen', ['Informação do Dashboard', 'Onde conferir', 'Observação'],
     [
         ['Total de Sessões, Presentes, Ausentes, Taxas', 'Agenda → Ver Agenda → Filtros (Sessão 1 a 5)', 'Somar as 5 colunas; repetir por mês.'],
         ['Por profissional / status', 'Relatórios → Agenda - Qtd Marcação', 'TOTAL só da página; "Ausentes" inclui justificativas.'],
         ['Cards/contagens de um mês', 'Relatórios → Relatório Agenda (Agenda → botão Relatório)', 'Mostra Presentes/Ausentes/desmarcações do mês da agenda.'],
         ['Presença de um dia', 'Relatórios → Presença Diária (por data de marcação)', 'A data é a do <b>registro</b> da marcação, não a da sessão.'],
         ['Pacientes Novos/Recorrentes', 'Relatórios → Histórico do Paciente → aba Agenda', 'Ir à última página para ver a 1ª sessão.'],
         ['Taxa de Ocupação (capacidade)', 'Agenda → Prof. horários', 'Somar horários × dias; descontar feriados.'],
         ['Faturamento por Convênio', 'Doc. Faturamento → Listar + Relatórios → Financeiro - Recebimentos', 'Sem agrupamento por operadora.'],
         ['Dias de Antecedência', '— (sem tela)', 'Só por consulta ao banco.'],
         ['Faixa etária', '— (sem tela)', 'Idade calculada na data da sessão.'],
     ], [5.0, 7.0, 5.5]),

    ('h2', 'Diferenças entre o Dashboard e as telas da Agenda'),
    ('tabelagen', ['Ponto', 'Dashboard', 'Telas da Agenda / relatórios'],
     [
         ['Período', 'Intervalo livre de datas (data da sessão).', 'Um mês de Agenda por vez.'],
         ['O que conta', 'Sessões com data registrada (Presente, Ausente, Justificada, Remarcação).', 'Agenda mostra todas as linhas; "Qtd Marcação" conta sessões previstas.'],
         ['Ausente', 'Só status AUSENTE.', 'Qtd Marcação soma AUSENTE + AUSENTE-JUSTIFICATIVA.'],
         ['Totais', 'Do período inteiro.', 'Qtd Marcação: TOTAL só da página exibida.'],
     ], [3.0, 7.0, 7.5]),
    ('aviso', 'Previsão de melhorias: foi elaborado um plano para criar relatórios que permitam conferir '
              'todos os números do Dashboard diretamente (sessões por período, pacientes novos, '
              'capacidade e faturamento por convênio), além de decidir se o Dashboard deve passar a contar '
              'também as sessões agendadas e desmarcadas. Enquanto isso, use os caminhos acima.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Agenda.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Agenda_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Agenda.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
