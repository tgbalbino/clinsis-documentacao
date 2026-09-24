# -*- coding: utf-8 -*-
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "_scripts-comuns"))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = "2.2"
DATA = "24/09/2026"
TITULO = "Dashboard de Agenda"
SUBTITULO = "O que significa cada informação e como conferir cada uma no sistema"
VIDEO_NOME = "https://youtu.be/QAra0-JTD5w"
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
              '(por isso o gráfico não tem fatias de desmarcação). Em outras palavras, o '
              'Dashboard mostra <b>sessões registradas</b>, e não todas as sessões agendadas — a própria tela traz esse aviso e os cards foram renomeados para deixar isso claro.'),
    ('p', '<b>Exemplo real (Agenda de Setembro/2026):</b> a agenda tem 165 sessões previstas — 150 ainda '
          'pendentes, 10 marcadas como Presente e 5 como Ausente. O Dashboard mostra <b>15</b> '
          '(10 + 5). Os relatórios de Agenda (que contam as sessões previstas) mostram 165.'),

    ('h2', 'Exemplo passo a passo: conferindo Sessões Registradas, Presença e Absenteísmo'),
    ('p', 'Estes números do Dashboard de Setembro: <b>Sessões Registradas = 15</b>, <b>Taxa de Presença = '
          '66,7%</b>, <b>Taxa de Absenteísmo = 33,3%</b>. Para conferir dentro da Agenda:'),
    ('tabelagen', ['Passo', 'O que fazer'],
     [
         ['1', 'Menu <b>Agenda</b> → na linha do mês (2026 / SETEMBRO) clique em <b>Acessar</b>.'],
         ['2', 'Clique em <b>Filtros</b>. No campo <b>Sessão 1</b>, escolha <b>PRESENTE</b> e clique em <b>Filtrar</b>. Veja no rodapé: <b>"Total de registros: 8"</b>.'],
         ['3', 'Repita trocando para <b>Sessão 2</b> (resultado: 1), <b>Sessão 3</b> (1), <b>Sessão 4</b> (0) e <b>Sessão 5</b> (0). Some: 8 + 1 + 1 = <b>10 presentes</b>.'],
         ['4', 'Repita tudo com <b>AUSENTE</b>: Sessão 1 = 3, Sessão 2 = 2, demais 0. Soma = <b>5 ausentes</b>.'],
         ['5', 'Sessões Registradas = 10 + 5 = <b>15</b>. Taxa de Presença = 10 ÷ 15 = <b>66,7%</b>. Taxa de Absenteísmo = 5 ÷ 15 = <b>33,3%</b>. Bate com o Dashboard.'],
     ], [1.6, 15.9]),
    ('img', '22-agendamento-grade-mes.png', 'Tela Agenda de Setembro/2026 (botão Acessar): sem filtros mostra 150 linhas de agendamento (cada linha pode ter até 5 sessões).'),
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
    ('aviso', 'Sobre o relatório "Agenda - Qtd Marcação" (atualizado): a linha <b>TOTAL agora soma o mês '
              'inteiro</b>, em todas as páginas (Setembro: 165 sessões, <b>10 presentes, 5 ausentes</b>, '
              '0 ausência justificada), e a coluna <b>Ausência Justificada</b> é separada de Ausente, como no '
              'Dashboard. Atenção: "Qtde. Sessões" continua sendo o número de sessões <b>previstas</b> '
              '(165), não as registradas (15).'),

    ('h2', 'Os 8 cards do topo — o que são e como conferir'),
    ('tabelagen', ['Card', 'O que é / como é calculado', 'Como conferir no sistema'],
     [
         ['Sessões Registradas (antes "Total de Sessões")', 'Quantidade de sessões <b>registradas</b> (com data) no período: Presente, Ausente, Ausente-Justificativa e Remarcação.', 'Agenda → Acessar → Filtros → somar as colunas Sessão 1 a 5 por status (exemplo acima).'],
         ['Pacientes com Sessão Registrada (antes "Pacientes Atendidos")', 'Pacientes <b>distintos</b> com ao menos uma sessão registrada no período (inclui quem faltou).', 'Na Agenda filtrada (Sessão = PRESENTE/AUSENTE), contar os nomes diferentes da coluna Paciente.'],
         ['Taxa de Presença', 'Presentes ÷ (Presentes + Ausentes) × 100.', 'Contagens de PRESENTE e AUSENTE na Agenda (exemplo acima).'],
         ['Taxa de Absenteísmo', 'Ausentes ÷ (Presentes + Ausentes) × 100.', 'Idem — ver seção anterior.'],
         ['Pacientes Novos', 'Pacientes cuja <b>primeira sessão registrada de toda a história</b> cai dentro do período.', 'Relatórios → Histórico do Paciente (aba Agenda). A lista vem do mais recente para o mais antigo: vá até a <b>última página</b> para ver a primeira sessão.'],
         ['Pacientes Recorrentes', 'Pacientes do período que já tinham sessão registrada <b>antes</b> do início do período.', 'Mesma consulta acima (primeira sessão anterior ao início do período).'],
         ['Dias de Antecedência (média)', 'Média de dias entre a data de inclusão do agendamento e a data da sessão.', '<b>Não há tela que mostre a data de inclusão do agendamento</b> — hoje só é possível conferir por consulta ao banco. Ver "Relatórios previstos".'],
         ['Taxa de Ocupação', 'Total de Sessões ÷ Capacidade Total × 100 (o card mostra "15 de 629"). Capacidade = horários configurados para os profissionais no período, descontados os feriados.', 'Agenda → <b>Horários</b> (escolha o profissional) lista os horários semanais/avulsos configurados. A capacidade é a soma desses horários ao longo dos dias do período. Não há tela que já traga o total.'],
     ], [3.0, 7.2, 7.3]),
    ('img', '42-prof-horarios.png', 'Agenda → Horários (Profissional 01, Setembro/2026): em Horários cadastrados, cada dia da semana mostra os horários do profissional; a capacidade do card soma esses horários pelos dias do período.'),
    ('aviso', '<b>Taxa de Ocupação</b>: como só as sessões registradas entram no numerador, a taxa fica '
              'baixa em meses em andamento (2,4% em Setembro, com muitas sessões ainda pendentes). '
              'Férias ou bloqueios de um profissional específico não são descontados da capacidade — só '
              'feriados cadastrados em Tabelas Aux. → Feriados (isso já aparece no tooltip do card).'),

    ('h2', 'Gráficos'),
    ('tabelagen', ['Gráfico', 'O que mostra', 'Como conferir'],
     [
         ['Sessões Registradas por Status (pizza)', 'Presentes, Ausentes, Ausência Justificada e Remarcações. As fatias de Desmarcação foram retiradas: esses status não gravam data e nunca apareciam.', 'Mesmas contagens da Agenda por status (Filtros → Sessão n).'],
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
              'R$ 3.669,00). Já corrigido: agora cada guia é contada uma única vez. <b>Conferência por operadora:</b> '
              'o relatório <b>Financeiro - Recebimentos</b> agora tem a coluna e o filtro <b>Operadora</b> '
              '(pela guia faturada), e o <b>Relatório Guia Faturamento</b> tem a opção <b>Agrupar por Operadora</b>.'),

    ('h2', 'Previsto no mês da agenda: sessões previstas, pendentes e desmarcadas'),
    ('p', 'Logo abaixo do aviso, uma faixa de quatro cards mostra o <b>previsto no mês da agenda</b>: <b>Sessões Previstas</b> '
          '(soma das sessões de todos os agendamentos do mês), <b>Sessões Pendentes</b> (ainda sem marcação), '
          '<b>Desmarcadas pelo Paciente</b> e <b>Desmarcadas pelo Profissional</b>. Esses números vêm do status de cada sessão '
          'do agendamento, e por isso não dependem de haver uma data gravada.'),
    ('img', '48-dashboard-previstas.png', 'Setembro/2026: 165 sessões previstas, 150 pendentes, 0 desmarcadas pelo paciente e 0 pelo profissional.'),
    ('aviso', 'Cuidados: (1) esses quatro cards são sempre por <b>mês da agenda</b>; se o período informado não for de meses '
              'fechados (por exemplo, 10 a 20 de setembro), eles mostram o mês inteiro, e a tela avisa isso. '
              '(2) Como conferir: Sessões Previstas = coluna "Qtde. Sessões" do relatório Agenda - Qtd Marcação (165 em Setembro, '
              '95 em Agosto, 84 em Julho). (3) Sessões Previstas e Sessões Registradas nem sempre fecham exatamente com as '
              'Pendentes, porque remarcações e lançamentos fora do dia previsto entram de forma diferente (em Agosto, 87 pendentes + '
              '9 registradas = 96 para 95 previstas). Use como referência, não como igualdade contábil.'),
    ('h2', 'Como ver quais sessões compõem cada número (novo)'),
    ('p', 'Cada número do Dashboard pode ser aberto para mostrar <b>as sessões que o formam</b>. Clique em um dos cards '
          '(Sessões Registradas, Pacientes, Taxa de Presença, Taxa de Absenteísmo), em uma linha das tabelas Por '
          'Profissional, Por Especialidade ou Por Operadora, ou em Particular / Convênio. Para ver todas as sessões do '
          'período, use o botão <b>Ver sessões</b> ao lado de Buscar. A lista usa exatamente o mesmo critério do painel, '
          'então o total da lista é sempre igual ao número clicado.'),
    ('img', '44-dashboard-drilldown.png', 'Ao clicar em Taxa de Presença (Setembro/2026): as 10 sessões presentes, com paciente, profissional, especialidade, operadora, data de inclusão e dias de antecedência.'),
    ('h2', 'Listas de conferência dos demais cards'),
    ('p', 'Os cards que não são sessões também abrem uma lista, com o mesmo critério do painel: '
          '<b>Pacientes Novos</b> e <b>Pacientes Recorrentes</b> (paciente, data da primeira sessão de toda a história e '
          'sessões no período), <b>Taxa de Ocupação</b> (cada horário de profissional que compõe a capacidade, com data, dia '
          'da semana, profissional, horário e se é fixo ou avulso) e as linhas do quadro <b>Faturamento por Convênio</b> '
          '(uma linha por conta a receber, com quantidade de guias, valor faturado e valor recebido no período).'),
    ('img', '45-drilldown-novos.png', 'Pacientes Novos (Setembro/2026): 2 pacientes, cuja primeira sessão de toda a história cai dentro do período.'),
    ('img', '46-drilldown-capacidade.png', 'Taxa de Ocupação: a lista tem 629 linhas, uma para cada horário disponível; esse é o denominador da taxa (15 de 629).'),
    ('img', '47-drilldown-faturamento.png', 'Faturamento por Convênio, linha PROPRIO (01/01 a 30/09/2026): conta a receber 61, 1 guia, R$ 1.223,00 faturado e R$ 1.373,00 recebido; confere com o quadro.'),
    ('aviso', 'Como conferir: o número de linhas de cada lista (mostrado no título) deve ser igual ao número do card. '
              'Se algum horário da capacidade não deveria contar (por exemplo, um profissional em férias), ele aparece na lista '
              'e pode ser identificado ali.'),
    ('p', 'Use o botão <b>Exportar CSV</b> para levar a lista ao Excel. Colunas: Data, Sessão, Paciente, Idade, Profissional, '
          'Especialidade, Operadora, Particular, Método, Programa, Status, Data de inclusão e Dias de antecedência. '
          'A coluna Dias de antecedência é a que permite conferir o card "Dias de Antecedência (média)".'),

    ('h2', 'Quadro resumo: onde conferir cada informação'),
    ('tabelagen', ['Informação do Dashboard', 'Onde conferir', 'Observação'],
     [
         ['Sessões Registradas, Presentes, Ausentes, Taxas', 'Agenda → Acessar → Filtros (Sessão 1 a 5)', 'Somar as 5 colunas; repetir por mês.'],
         ['Por profissional / status', 'Relatórios → Agenda - Qtd Marcação', 'TOTAL do mês inteiro; "Ausência Justificada" em coluna própria.'],
         ['Cards/contagens de um mês', 'Relatórios → Relatório Agenda (Agenda → botão Relatório)', 'Mostra Presentes/Ausentes/desmarcações do mês da agenda.'],
         ['Presença de um dia', 'Relatórios → Presença Diária (por data de marcação)', 'A data é a do <b>registro</b> da marcação, não a da sessão.'],
         ['Pacientes Novos/Recorrentes', 'Relatórios → Histórico do Paciente → aba Agenda', 'Ir à última página para ver a 1ª sessão.'],
         ['Taxa de Ocupação (capacidade)', 'Agenda → Horários', 'Somar horários × dias; descontar feriados.'],
         ['Faturamento por Convênio', 'Doc. Faturamento → Listar + Relatórios → Financeiro - Recebimentos', 'Sem agrupamento por operadora.'],
         ['Dias de Antecedência', '— (sem tela)', 'Só por consulta ao banco.'],
         ['Faixa etária', '— (sem tela)', 'Idade calculada na data da sessão.'],
     ], [5.0, 7.0, 5.5]),

    ('h2', 'Diferenças entre o Dashboard e as telas da Agenda'),
    ('tabelagen', ['Ponto', 'Dashboard', 'Telas da Agenda / relatórios'],
     [
         ['Período', 'Intervalo livre de datas (data da sessão).', 'Um mês de Agenda por vez.'],
         ['O que conta', 'Sessões com data registrada (Presente, Ausente, Justificada, Remarcação).', 'Agenda mostra todas as linhas; "Qtd Marcação" conta sessões previstas.'],
         ['Ausente', 'Só status AUSENTE.', 'Qtd Marcação separa AUSENTE e Ausência Justificada.'],
         ['Totais', 'Do período inteiro.', 'Qtd Marcação: TOTAL do período inteiro.'],
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
