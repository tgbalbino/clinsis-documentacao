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

VERSAO = '1.2'
DATA = '29/09/2026'
TITULO = "Pagamento de Profissionais"
SUBTITULO = "Calcular e gerar, de uma vez, o repasse de todos os profissionais do mês"
VIDEO_NOME = "https://youtu.be/PkvsWwKU2nM"
INTRO = ('Pagamento de Profissionais calcula, a partir dos atendimentos realizados no mês, quanto '
         'a clínica deve repassar para cada profissional — e gera a Conta a Pagar correspondente '
         'com um clique, em vez de lançar uma conta manual pra cada profissional. Para isso '
         'funcionar, é preciso configurar ANTES uma <b>Tabela de Valores para Pagamento</b> '
         '(Tabelas Aux. → Tab. Pagamento), com o valor pago por sessão/atendimento e vinculando '
         'o mês (Agenda) que vai usar essa tabela.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Configuração prévia: Tabela de Valores para Pagamento'),
    ('p', 'Em <b>Tabelas Aux. → Tab. Pagamento</b> '
          'fica a lista de "tabelas de valores" — cada uma agrupa um conjunto de valores usados para '
          'calcular o repasse dos profissionais. Ao abrir uma tabela (botão da engrenagem), '
          'três abas organizam a configuração:'),
    ('img', '00-vigencia-lista.png', 'Lista de tabelas de valores para pagamento. No exemplo, a "Tabela 2026" já está ativa.'),
    ('tabela', [
        ('Aba Agenda', 'Quais competências (mês/ano) usam esta tabela de valores. Sem vincular o mês aqui, o sistema recusa gerar o pagamento daquele mês.', 'ConfigAgendaProfEspecPagtoController.cs'),
        ('Aba Especialidades', 'Valor padrão por Especialidade (ex.: Fisioterapeuta, Psicólogo), aplicado a todos os profissionais daquela especialidade que não tiverem um valor específico.', 'ConfigProfissionalEspecialidadePagtoController.cs'),
        ('Aba Profissionais', 'Valor específico por Profissional + Especialidade, que sobrepõe o valor padrão da aba Especialidades quando presente.', 'ConfigProfissionalEspecialidadePagtoController.cs'),
    ]),
    ('img', '01-vigencia-gerenciar-agenda.png', 'Aba Agenda: lista de competências (2026/Setembro, 2026/Agosto, etc.) já vinculadas a esta tabela de valores.'),
    ('img', '02-vigencia-gerenciar-profissionais.png', 'Aba Profissionais: lista de profissionais; o botão "$" abre o cadastro dos valores daquele profissional por especialidade.'),

    ('h2', '"Valor" e "Valor Convênio": qual dos dois é usado no cálculo'),
    ('p', 'Tanto na aba Especialidades quanto na aba Profissionais, cada linha tem dois campos de valor: '
          '<b>Valor</b> e <b>Valor Convênio</b>. Pela lógica do nome, seria esperado que o sistema usasse '
          'automaticamente o Valor Convênio quando o atendimento foi feito por um paciente de convênio, e o '
          'Valor normal quando foi particular.'),
    ('img', '13-vigencia-aba-especialidades.png',
     'Aba Especialidades: cada linha tem as colunas Tipo de Marcação, Valor e Valor Convênio — no exemplo, '
     '"Terapeuta Ocupacional / Todos os tipos" vale R$ 2,00 e "Fisioterapeuta" tem Valor R$ 3,00 e Valor '
     'Convênio R$ 2,00 preenchido.'),
    ('aviso', 'Isso <b>não acontece hoje</b>. Conferindo o cálculo do relatório, o sistema sempre usa o campo '
              '<b>Valor</b> para calcular o repasse, independentemente do atendimento ser particular ou de '
              'convênio — o campo Valor Convênio fica salvo no cadastro, mas não entra em nenhuma conta. Na '
              'prática, preencher o Valor Convênio hoje não muda o valor pago ao profissional. Recomendamos '
              'não contar com uma diferenciação automática por convênio nesta tela e alinhar com a equipe de '
              'desenvolvimento se essa distinção deveria estar ativa.'),

    ('h2', '"Tipo de Marcação": valores diferentes por tipo de atendimento'),
    ('p', 'O campo <b>Tipo de Marcação</b> (ex.: "Todos os tipos", "Avaliação", "Consulta/Sessão") permite '
          'cadastrar um valor de pagamento diferente conforme o tipo de marcação escolhido no agendamento do '
          'paciente. Por padrão existe uma linha "Todos os tipos", que serve de valor genérico; é possível '
          'clicar no botão "+" e adicionar uma linha específica para "Avaliação" ou "Consulta/Sessão" com um '
          'valor próprio.'),
    ('p', '<b>Exemplo real do ambiente de testes:</b> na aba Especialidades, "Terapeuta Ocupacional" tem duas '
          'linhas: "Todos os tipos" = R$ 2,00 e "Avaliação" = R$ 3,00 (ver print acima) — um agendamento de '
          'Avaliação paga R$ 3,00, e qualquer outro tipo (Consulta/Sessão) paga R$ 2,00 pela linha genérica.'),
    ('img', '14-vigencia-modal-valores-profissional.png',
     'O mesmo vale na aba Profissionais: o "Profissional 01" tem valor específico para Psicólogo — "Todos os '
     'tipo" = R$ 10,00 e "Consulta/Ses[são]" = R$ 2,00 — sobrepondo, só para ele, o valor padrão de Psicólogo '
     'da aba Especialidades (R$ 80,00).'),

    ('h2', '"Tipo de Cobrança" da Especialidade: por sessão ou por paciente'),
    ('p', 'Esse campo <b>não fica na Tabela de Valores</b> — ele é configurado no cadastro da própria '
          '<b>Especialidade</b> (Cadastros → Especialidades), no campo <b>Tipo de Cobrança</b>, com duas '
          'opções: <b>Por Sessão</b> ou <b>Paciente</b>. Mesmo estando em outra tela, ele afeta diretamente '
          'como o Pagamento de Profissionais conta as sessões:'),
    ('img', '15-especialidade-lista-tipocobranca.png',
     'Cadastros → Especialidades: a lista já mostra a coluna Tipo de Cobrança de cada especialidade — no '
     'ambiente de testes, todas estão configuradas como "Por Sessão".'),
    ('img', '16-especialidade-cadastro-tipocobranca.png',
     'Abrindo "Editar" numa especialidade (ex.: Fisioterapeuta), o campo Tipo de Cobrança aparece no cadastro, '
     'com as opções Por Sessão / Paciente.'),
    ('tabela', [
        ('Por Sessão', 'O profissional é pago por cada sessão cujo status esteja marcado no filtro do relatório (ver "Quais sessões entram no pagamento"). Se o agendamento tem 5 sessões previstas e 3 estão com um status marcado, contam 3 sessões pagáveis.', 'Especialidade.TipoCobranca = 1'),
        ('Paciente', 'O profissional é pago no máximo 1 vez por agendamento/paciente naquele período, não importa quantas sessões (1 a 5) ele teve — é um valor "por pacote", não por sessão avulsa. O campo "Considera Marcação" do relatório define se o pacote exige ao menos uma sessão num status marcado.', 'Especialidade.TipoCobranca = 2'),
    ]),
    ('p', '<b>Exemplo numérico:</b> Especialidade "Fisioterapia" com Valor = R$ 50,00 e um agendamento com 5 '
          'sessões previstas no mês, das quais 3 foram confirmadas como realizadas. Se o Tipo de Cobrança da '
          'especialidade for <b>Por Sessão</b>, o valor total é 3 × R$ 50 = <b>R$ 150,00</b>. Se for '
          '<b>Paciente</b>, o valor total é 1 × R$ 50 = <b>R$ 50,00</b> — paga uma única vez pelo pacote do '
          'mês, mesmo que várias sessões tenham ocorrido.'),

    ('h2', 'Quando criar uma nova Tabela de Valores'),
    ('p', 'Seria natural imaginar que, ao reajustar valores, bastaria criar uma <b>nova</b> Tabela de Valores e '
          'vincular só os meses futuros a ela, preservando os valores antigos dos meses já vinculados à tabela '
          'anterior. É importante entender como o sistema realmente se comporta hoje antes de fazer isso:'),
    ('aviso', 'O cálculo do relatório usa sempre a Tabela de Valores <b>mais recentemente cadastrada que estiver '
              'marcada como "Ativo = Sim"</b> para toda a clínica — e não, especificamente, a tabela vinculada '
              'àquele mês na aba Agenda. A aba Agenda só controla se aquele mês pode ou não entrar no cálculo '
              '(precisa estar vinculado a alguma tabela), mas os <b>valores</b> aplicados vêm sempre da tabela '
              'ativa mais nova. Ou seja: editar um Valor numa tabela existente, ou ativar uma tabela nova, pode '
              'alterar o cálculo de meses antigos que ainda não tiveram o pagamento gerado — a única coisa que '
              'realmente fica "congelada" é a <b>Conta a Pagar já gerada</b>; uma vez gerada, ela não é '
              'recalculada.'),
    ('p', 'Na prática, para reajustar valores com segurança: gere e confira a Conta a Pagar dos meses fechados '
          '<b>antes</b> de alterar valores ou ativar uma tabela nova, já que o sistema recalcula pelo valor mais '
          'recente ativo no momento em que o relatório é rodado — não pelo valor vigente na época do '
          'atendimento. Se notar valores de meses antigos mudando ao reajustar uma tabela nova, isso é o '
          'comportamento atual do sistema, e vale reportar à equipe de desenvolvimento para avaliar se é assim '
          'que deveria funcionar.'),

    ('h2', 'Relatório de Pagamento de Profissionais (sintético)'),
    ('p', 'Rota <font face="Courier">/relatorio/pagamento/profissional/agrupado</font>. Clique em '
          '<b>Filtros</b>, escolha a <b>Agenda</b> (mês/ano) que quer calcular, e clique em '
          '<b>Filtrar</b>. O relatório mostra, por Profissional e Especialidade, quantas sessões '
          'foram realizadas, quantas entram no cálculo do pagamento, e o Valor Total a repassar.'),
    ('img', '05-resultado-agenda-vinculada.png',
     'Resultado para Setembro/2026 (mês já vinculado à Tabela 2026): 4 linhas com Valor Total calculado, somando R$ 67,00.'),
    ('tabela', [
        ('Agenda (filtro)', 'Mês/ano que será calculado — precisa estar vinculado a uma Tabela de Valores.', 'Obrigatório'),
        ('Profissional (filtro)', 'Restringe o relatório a um profissional específico.', 'Opcional'),
        ('Status (filtro)', 'Quais situações de sessão são pagas (Presente, Ausente, Remarcação etc.). <b>É este filtro que define o quantitativo de sessões a pagar</b> — veja a seção seguinte. Vem com todos os status marcados.', 'Obrigatório ter ao menos 1 marcado'),
        ('Considera Marcação (filtro)', 'Só tem efeito em especialidades com Tipo de Cobrança "Paciente": "Sim" (padrão) paga o agendamento se ao menos uma sessão estiver num status marcado; "Não" paga todo agendamento do mês, independentemente da marcação.', 'Opcional'),
        ('Qtd. Horários', 'Quantos agendamentos (paciente + horário) entraram no cálculo — só entram os que têm ao menos uma sessão num status marcado.', 'RelatorioRepository.cs'),
        ('Sessões / Sessões Pagamento', 'Sessões: total de sessões previstas nesses agendamentos. Sessões Pagamento: quantas delas estão num dos Status marcados no filtro (e já com a data registrada).', 'RelatorioRepository.cs'),
        ('Valor Total', 'Sessões Pagamento × Valor da sessão (da aba Profissionais ou Especialidades da Tabela de Valores). Só fica com checkbox pra selecionar se for maior que zero.', 'RelatorioRepository.cs'),
    ]),

    ('h2', 'Quais sessões entram no pagamento: o filtro de Status'),
    ('p', 'O quantitativo de <b>Sessões Pagamento</b> não é fixo: ele depende dos <b>Status marcados no filtro</b> '
          'do relatório. Cada agendamento do mês tem até 5 sessões, e cada sessão recebe na Agenda uma situação '
          '(Presente, Ausente, Ausente - Justificativa, Remarcação, Pac. Desmarcou, Pro. Desmarcou). Ao calcular, o '
          'sistema olha sessão por sessão e <b>só conta as que estão num dos status marcados</b>. Por isso, o mesmo '
          'mês pode dar valores diferentes dependendo do que foi marcado no filtro.'),
    ('img', '17-filtro-status-todos.png',
     'Filtros do relatório com a lista de Status aberta. Ao abrir a tela, todos os status já vêm marcados — '
     'ou seja, por padrão faltas (Ausente), faltas justificadas e remarcações também são pagas.'),
    ('tabelagen', ['Status da sessão', 'Se estiver marcado no filtro, a sessão é paga?'], [
        ('PRESENTE', 'Sim.'),
        ('AUSENTE', 'Sim — a falta do paciente é paga ao profissional como se fosse uma sessão. Desmarque se a clínica não paga faltas.'),
        ('AUSENTE - JUSTIFICATIVA', 'Sim — mesma regra do Ausente.'),
        ('REMARCAÇÃO', 'Sim.'),
        ('PAC. DESMARCOU / PRO. DESMARCOU', 'Normalmente não. Ao marcar uma sessão como desmarcada, o sistema não registra a data dela, e o '
                                           'cálculo só conta sessões com data registrada. A exceção é a sessão que já tinha sido marcada '
                                           'antes com outro status (ex.: Presente) e depois foi trocada para desmarcação: ela mantém a data '
                                           'anterior e passa a contar.'),
        ('Sessão ainda sem marcação', 'Nunca — nem com todos os status marcados. Sessões com data futura também só contam depois que a data chegar.'),
    ], [5.2, 11.8]),
    ('p', '<b>Exemplo real (Setembro/2026, ambiente de testes).</b> Na linha do profissional "PSICANALISTA", '
          'especialidade Terapeuta Ocupacional, com valor de R$ 3,88 por sessão, há no mês 2 sessões marcadas como '
          'Presente e 3 marcadas como Ausente (as demais sessões previstas ainda não foram marcadas). Rodando o mesmo '
          'relatório com três combinações de Status:'),
    ('tabelagen', ['Status marcados no filtro', 'Qtd. Horários', 'Sessões', 'Sessões Pagamento', 'Valor Total (PSICANALISTA / T.O.)', 'Total do relatório'], [
        ('Todos (padrão da tela)', '4', '17', '5', 'R$ 19,40 (5 × 3,88)', 'R$ 93,93'),
        ('Somente PRESENTE', '2', '8', '2', 'R$ 7,76 (2 × 3,88)', 'R$ 82,29'),
        ('Somente AUSENTE + AUSENTE - JUSTIFICATIVA', '2', '9', '3', 'R$ 11,64 (3 × 3,88)', 'R$ 11,64'),
    ], [4.6, 2.0, 1.7, 2.3, 3.6, 2.8]),
    ('p', 'Repare que as 5 sessões pagas com "Todos" são exatamente as 2 presenças + as 3 faltas. As colunas '
          '"Qtd. Horários" e "Sessões" também mudam, porque um agendamento só aparece se tiver ao menos uma sessão '
          'num status marcado.'),
    ('img', '18-sintetico-todos-status.png',
     'Todos os status marcados: PSICANALISTA / Terapeuta Ocupacional com 5 Sessões Pagamento (R$ 19,40); total do relatório R$ 93,93.'),
    ('img', '19-filtro-status-somente-presente.png',
     'Para pagar só atendimentos realizados: clique em "Limpar" e marque apenas PRESENTE.'),
    ('img', '20-sintetico-somente-presente.png',
     'Somente PRESENTE: a mesma linha cai para 2 Sessões Pagamento (R$ 7,76) e o total do relatório para R$ 82,29 — as faltas deixaram de ser pagas.'),
    ('img', '21-sintetico-somente-ausentes.png',
     'Somente AUSENTE e AUSENTE - JUSTIFICATIVA: sobra apenas a linha que tem faltas, com as 3 sessões de falta (R$ 11,64). '
     'Útil para ver quanto das faltas está sendo pago.'),
    ('img', '22-analitico-somente-ausentes.png',
     'O relatório analítico com o mesmo filtro mostra de quais pacientes são essas faltas: Paciente 000 (2) e Paciente 0005 (1).'),
    ('aviso', 'O botão <b>Gerar Contas a Pagar</b> usa os Status que estão marcados no filtro naquele momento: o valor '
              'gravado na conta é exatamente o que aparece na tela. Por isso, <b>confira o filtro de Status antes de '
              'gerar</b>, de acordo com a regra da clínica (ex.: pagar faltas ou não). Depois de gerada, a conta não '
              'muda se o filtro for alterado, e a linha continua marcada como "Conta a pagar gerada" com qualquer '
              'combinação de status.'),
    ('p', '<b>Tipo de Cobrança "Paciente".</b> Nessas especialidades o profissional recebe no máximo 1 vez por '
          'agendamento. Com "Considera Marcação = Sim" (padrão), o agendamento só é pago se ao menos uma sessão '
          'estiver num status marcado — ex.: com somente PRESENTE marcado, um paciente que faltou a todas as sessões '
          'do mês não gera pagamento. Com "Considera Marcação = Não", todo agendamento do mês é pago 1 vez, '
          'independentemente dos status. Para especialidades "Por Sessão", o campo Considera Marcação não muda nada.'),

    ('h2', 'Relatório de Pagamento de Profissionais (analítico)'),
    ('p', 'Rota <font face="Courier">/relatorio/pagamento/profissional</font> (sem "/agrupado"). É a versão '
          '<b>detalhada</b> do mesmo cálculo do relatório sintético: em vez de uma linha por Profissional + '
          'Especialidade, mostra <b>uma linha por Paciente + Profissional + Especialidade</b>, com os mesmos '
          'totais de sessões e valor. Os filtros são os mesmos (Agenda, Profissional, Status, Sessões Cobrar, '
          'Valor de Pagamento, Considera Marcação), mas essa tela <b>não tem botão para gerar Conta a Pagar</b> '
          '— só "Filtros" e "Exportar".'),
    ('img', '11-analitico-inicial.png', 'Tela inicial do relatório analítico, antes de aplicar o filtro de Agenda.'),
    ('img', '12-analitico-resultado.png',
     'Mesma Agenda (Setembro/2026) do exemplo do relatório sintético, agora aberta paciente a paciente: o total '
     'geral (R$ 67,00) bate exatamente com o valor do sintético, só que dividido em várias linhas.'),
    ('p', 'Serve como tela de <b>conferência/auditoria</b> antes de gerar o pagamento em lote pelo relatório '
          'sintético: permite ver, paciente por paciente, exatamente quais sessões estão entrando no valor '
          'total de cada profissional — útil para investigar uma diferença inesperada (por exemplo, uma sessão '
          'que não deveria contar, ou um paciente que faltou e foi contabilizado por engano) antes de confirmar '
          'a geração da conta, ou para exportar e conferir com uma agenda física.'),

    ('h2', 'Exportar para planilha (CSV)'),
    ('p', 'Os dois relatórios (sintético e analítico) têm o botão <b>Exportar</b>, logo acima da tabela. Ele gera um arquivo <b>CSV</b>, que abre no Excel, com <b>todos os registros</b> do filtro aplicado — não só os da página exibida. Aplique antes os filtros (agenda, profissional, status e "Considera Marcação") e clique em Exportar. Se o filtro não tiver nenhum registro, nenhum arquivo é gerado.'),
    ('img', '24-sintetico-exportar.png', 'Relatório sintético com o botão Exportar acima da tabela.'),
    ('tabelagen', ['Relatório', 'Nome do arquivo', 'Colunas do CSV'], [
        ['Sintético (agrupado)', 'pagamento_profissional_agrupado_(data e hora).csv', 'Profissional, Especialidade, QtdPacientes, Sessoes, SessoesPagar, ValorSessao, ValorTotal e ContaPagarGerada (Sim/Não).'],
        ['Analítico', 'pagamento_profissional_(data e hora).csv', 'Profissional, Especialidade, Paciente, Sessoes, SessoesPagar, ValorSessao e ValorTotal.'],
    ], [3.6, 6, 7.9]),
    ('aviso', 'O arquivo usa ponto e vírgula como separador e os valores no formato brasileiro (ex.: 136,00). As mesmas regras da tela valem na exportação: a agenda precisa estar vinculada a uma Tabela de Valores para Pagamento; caso contrário aparece a mensagem "Agenda não vinculada a uma conf. Pagamento". Exportar não gera Conta a Pagar: serve só para conferência e controle.'),

    ('h2', 'Gerando a Conta a Pagar'),
    ('p', 'Marque o checkbox das linhas desejadas (ou use o botão no canto superior direito da '
          'tabela pra marcar todas) e clique em <b>Gerar Contas a Pagar</b>. Preencha Plano de '
          'Contas, Centro de Custo e Data de Vencimento (os três são obrigatórios), e confirme em '
          '<b>Sim / Gerar</b>.'),
    ('img', '07-modal-gerar-preenchido.png',
     'Modal "Gerar contas a pagar" preenchido: Plano de Contas "Honorário Médico", Centro de Custo "Administrativo / Financeiro" e Data de Vencimento de hoje, para a linha do Profissional 01 selecionada.'),
    ('img', '08-apos-gerar.png',
     'Depois de gerar: aviso "1 conta(s) a pagar gerada(s) com sucesso" e a linha marca "Conta a pagar gerada" (não pode mais ser selecionada de novo).'),

    ('h2', 'Onde a conta gerada aparece — e por que ela nasce "Em Aberto"'),
    ('p', 'A conta criada aparece normalmente na tela de <b>Contas a Pagar</b>, com o Favorecido '
          '(o profissional), o Plano de Contas (ex.: "Honorário Médico"), o Centro de Custo e o '
          'valor calculado. Ela nasce com Situação <b>"1 - Aberto"</b> e Valor Pago R$ 0,00 — ou '
          'seja, o Pagamento de Profissionais só calcula e <b>registra a dívida</b> com o '
          'profissional; ele não marca como pago sozinho. O pagamento em si só é registrado depois, '
          'manualmente, quando a clínica realmente faz o repasse: usando o botão de Pagamento/Acerto '
          'dessa conta (o mesmo botão "$" já visto na rotina de Contas a Pagar) para dar baixa '
          'quando o dinheiro sair de fato.'),
    ('img', '10-conta-a-pagar-gerada-pelo-pagamento-profissional.png',
     'Conferindo em Contas a Pagar: a conta do "Profissional 01" (Plano de Contas "Honorário Médico", R$ 40,00) aparece com Situação "1 - Aberto" e Valor Pago R$ 0,00 — pendente só da baixa quando o pagamento for efetivamente feito.'),

    ('h2', 'Quando o mês não está vinculado a nenhuma tabela de valores'),
    ('p', 'Se a Agenda (mês/ano) escolhida no filtro ainda não foi vinculada a nenhuma Tabela de '
          'Valores (aba Agenda, tela de configuração), o sistema recusa com o aviso '
          '<b>"Agenda não vinculada a uma conf. Pagamento"</b> — é preciso voltar em Tabelas Aux. → '
          'Tab. Pagamento e vincular aquele mês antes de tentar gerar o pagamento dele.'),
    ('img', '09-agenda-nao-vinculada-sem-linhas.png',
     'Exemplo real: ao filtrar por um mês (Abril/2026) que não está vinculado a nenhuma tabela, o relatório vem vazio e aparece o aviso de erro.'),

    ('aviso', 'Esta é uma das rotinas que <b>geram Conta a Pagar automaticamente</b>: em vez de '
              'lançar manualmente uma conta para cada profissional todo mês, o sistema calcula e '
              'gera tudo de uma vez a partir dos atendimentos realizados e da Tabela de Valores '
              'configurada — o Plano de Contas usado costuma ser algo como "Honorário Médico" e o '
              'Tipo de Documento fica marcado como "Pag. Profissional" na Conta a Pagar gerada. '
              'Diferente do Checkin (que já gera a conta paga), aqui a conta nasce <b>em aberto</b>: '
              'a baixa/pagamento em si é um passo manual separado, feito quando a clínica realmente '
              'repassa o valor ao profissional.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Pagamento_de_Profissionais.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Pagamento_de_Profissionais_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Pagamento_de_Profissionais.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
