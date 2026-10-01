# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = "1.1"
DATA = "26/09/2026"
TITULO = "Cobrança de Paciente"
SUBTITULO = "Calcular e gerar, de uma vez, a cobrança de todos os pacientes particulares do mês"
VIDEO_NOME = "https://youtu.be/ViW55USFc6I"
INTRO = ('Cobrança de Paciente calcula, a partir dos atendimentos particulares realizados no mês, '
         'quanto cada paciente deve pagar pelas sessões que teve — e gera a Conta a Receber '
         'correspondente com um clique, em vez de lançar uma conta manual pra cada paciente. Para '
         'isso funcionar, é preciso configurar ANTES uma <b>Tabela de Valores para Cobrança</b> '
         '(Tabelas Aux. → Tab. Cobrança), com o valor cobrado por sessão/atendimento particular.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Configuração prévia: Tabela de Valores para Cobrança'),
    ('p', 'Em <b>Tabelas Aux. → Tab. Cobrança</b> (rota <font face="Courier">/aux/cobranca/gerenciar</font>) '
          'fica a configuração dos valores cobrados de cada paciente particular, organizada em três abas:'),
    ('img', '00-cobranca-config-especialidade.png',
     'Aba Especialidade: valor cobrado por sessão de cada especialidade, aplicado a qualquer profissional '
     'que não tenha um valor específico cadastrado (ex.: Fisioterapeuta R$ 2,00, Terapeuta Ocupacional R$ 1,99).'),
    ('tabela', [
        ('Aba Especialidade', 'Valor padrão cobrado por sessão de cada especialidade, aplicado a todos os profissionais que não tiverem um valor específico.', 'ConfigCobrancaEspecPagtoController.cs'),
        ('Aba Profissional', 'Valor específico por Profissional + Especialidade, que sobrepõe o valor padrão da aba Especialidade quando presente.', 'ConfigCobrancaProfEspecPagtoController.cs'),
        ('Aba Operadora', 'Valores específicos por Operadora de convênio (colunas Valor e Valor Social), usados quando o relatório de cobrança de convênio for aplicável.', 'ConfigCobrancaRepository.cs'),
    ]),
    ('img', '01-cobranca-config-profissional.png', 'Aba Profissional: lista de profissionais da clínica com os valores específicos por especialidade.'),
    ('img', '02-cobranca-config-operadora.png', 'Aba Operadora: valores de cobrança específicos por convênio (colunas Valor e Valor Social).'),
    ('aviso', 'Assim como acontece no Pagamento de Profissionais, o campo <b>Valor Social</b> (nas abas '
              'Especialidade e Operadora) fica salvo no cadastro, mas <b>não é usado hoje no cálculo da '
              'cobrança</b> — o relatório sempre soma pelo campo "Valor" normal. Não conte com uma '
              'diferenciação automática de valor social nesta tela.'),

    ('h2', 'Relatório de Cobrança de Paciente (sintético)'),
    ('p', 'Rota <font face="Courier">/relatorio/valorreceber/agrupado</font>. Clique em <b>Filtros</b>, '
          'escolha a <b>Agenda</b> (mês/ano) que quer calcular, marque os Status de sessão que devem '
          'entrar na cobrança e clique em <b>Filtrar</b>. O relatório considera apenas agendamentos '
          '<b>Particulares</b> (convênio não entra aqui) e soma, por paciente, quanto ele deve pagar.'),
    ('img', '03-sintetico-inicial.png', 'Tela inicial do relatório sintético, antes de aplicar o filtro.'),
    ('img', '04-sintetico-filtro-preenchido.png', 'Filtro preenchido: Agenda de Setembro/2026 e todos os Status de sessão marcados.'),
    ('img', '05-sintetico-resultado.png',
     'Resultado: uma linha por paciente com o total de sessões e o Valor a Receber calculado — no exemplo, '
     '9 pacientes somando R$ 22,97.'),

    ('h2', 'Quais sessões entram na cobrança: o filtro de Status'),
    ('p', 'A quantidade de sessões cobradas de cada paciente não é fixa: ela depende dos <b>Status marcados no '
          'filtro</b> do relatório — a mesma regra do Pagamento de Profissionais. Cada agendamento do mês tem até '
          '5 sessões, e cada sessão recebe na Agenda uma situação (Presente, Ausente, Ausente - Justificativa, '
          'Remarcação, Pac. Desmarcou, Pro. Desmarcou). O sistema olha sessão por sessão e <b>só cobra as que '
          'estão num dos status marcados</b>. Por isso, o mesmo mês pode dar valores diferentes conforme o filtro.'),
    ('img', '13-filtro-status-todos.png',
     'Filtros do relatório com a lista de Status aberta. Ao abrir a tela, todos os status já vêm marcados — '
     'ou seja, por padrão as faltas (Ausente e Ausente - Justificativa) e as remarcações também são cobradas do paciente.'),
    ('tabelagen', ['Status da sessão', 'Se estiver marcado no filtro, a sessão é cobrada?'], [
        ('PRESENTE', 'Sim.'),
        ('AUSENTE', 'Sim — a falta é cobrada do paciente como uma sessão. Desmarque se a clínica não cobra faltas.'),
        ('AUSENTE - JUSTIFICATIVA', 'Sim — mesma regra do Ausente. Desmarque se a falta justificada não deve ser cobrada.'),
        ('REMARCAÇÃO', 'Sim.'),
        ('PAC. DESMARCOU / PRO. DESMARCOU', 'Normalmente não. Ao marcar uma sessão como desmarcada, o sistema não registra a data dela, e o '
                                           'cálculo só conta sessões com data registrada. A exceção é a sessão que já tinha sido marcada '
                                           'antes com outro status (ex.: Presente) e depois foi trocada para desmarcação: ela mantém a data '
                                           'anterior e passa a contar.'),
        ('Sessão ainda sem marcação', 'Nunca — nem com todos os status marcados. Sessões com data futura também só contam depois que a data chegar.'),
    ], [5.2, 11.8]),
    ('p', '<b>Exemplo real (Setembro/2026, ambiente de testes).</b> O "Paciente 0005" (Terapeuta Ocupacional, '
          'R$ 2,51 por sessão) tem 4 sessões previstas no mês, e a única já marcada foi uma falta (Ausente). Rodando '
          'o mesmo relatório com três combinações de Status:'),
    ('tabelagen', ['Status marcados no filtro', 'Paciente 0005', 'Sessões (total)', 'Valor a Receber (total)'], [
        ('Todos (padrão da tela)', 'Aparece: 1 sessão, R$ 2,51 (a falta é cobrada)', '11', 'R$ 27,39'),
        ('Somente PRESENTE', 'Não aparece — nada a cobrar', '10', 'R$ 24,87'),
        ('Somente AUSENTE + AUSENTE - JUSTIFICATIVA', 'Único paciente da lista: 1 sessão, R$ 2,51', '1', 'R$ 2,51'),
    ], [5.0, 6.0, 2.6, 3.4]),
    ('p', 'Repare que a diferença entre "Todos" e "Somente PRESENTE" (11 − 10 = 1 sessão; R$ 27,39 − R$ 24,87 = '
          'R$ 2,51) é exatamente a falta do Paciente 0005.'),
    ('img', '14-sintetico-todos-status.png',
     'Todos os status marcados: 11 sessões, R$ 27,39. O Paciente 0005 aparece com 1 sessão (a falta) e, neste '
     'ambiente de testes, já teve a Conta a Receber gerada — ou seja, a falta foi cobrada.'),
    ('img', '15-filtro-status-somente-presente.png',
     'Para cobrar só atendimentos realizados: clique em "Limpar" e marque apenas PRESENTE.'),
    ('img', '16-sintetico-somente-presente.png',
     'Somente PRESENTE: o Paciente 0005 sai da lista e o total cai para 10 sessões e R$ 24,87.'),
    ('img', '17-sintetico-somente-ausentes.png',
     'Somente AUSENTE e AUSENTE - JUSTIFICATIVA: aparece só quem tem falta no mês — útil para conferir quanto das faltas está sendo cobrado.'),
    ('img', '18-analitico-somente-ausentes.png',
     'O relatório analítico com o mesmo filtro mostra o detalhe: Paciente 0005, profissional PSICANALISTA, TO, 4 sessões previstas e 1 a receber.'),
    ('aviso', 'O botão <b>Gerar Conta a Receber</b> gera a conta com o Valor a Receber que está na tela, ou seja, '
              'calculado com os Status marcados naquele momento. Por isso, <b>confira o filtro de Status antes de '
              'gerar</b>, de acordo com a regra da clínica (ex.: cobrar faltas ou não). Depois de gerada, a conta não '
              'muda se o filtro for alterado.'),
    ('p', 'Diferente do Pagamento de Profissionais, a cobrança de paciente é sempre <b>por sessão</b>: o campo '
          '"Tipo de Cobrança" da Especialidade não é usado aqui, e esta tela não tem o filtro "Considera Marcação".'),

    ('h2', 'Gerando a Conta a Receber'),
    ('p', 'Marque o checkbox dos pacientes desejados (só aparece para quem tem Valor a Receber maior que '
          'zero) e clique em <b>Gerar Conta a Receber</b>. Preencha Data de Vencimento (mínimo hoje + 5 '
          'dias), Plano de Contas e Centro de Custo, todos obrigatórios, e confirme em <b>Sim / Gerar</b>.'),
    ('img', '06-sintetico-linha-selecionada.png', 'Paciente selecionado (Paciente 000, R$ 2,00) antes de abrir o modal de geração.'),
    ('img', '07-sintetico-modal-gerar-preenchido.png',
     'Modal "Gerar conta a receber" preenchido: Data de Vencimento 30/09/2026, Plano de Contas '
     '"Consulta Particular" e Centro de Custo "Administrativo / Financeiro".'),
    ('img', '08-sintetico-apos-gerar.png',
     'Depois de gerar: aviso "Contas a receber geradas com sucesso" no canto superior direito.'),

    ('h2', 'Onde a conta gerada aparece — e por que ela nasce "Em Aberto"'),
    ('p', 'A conta criada aparece na tela de <b>Contas a Receber</b>, com o nome do paciente, o Plano de '
          'Contas, o Centro de Custo e o valor calculado. Assim como no Pagamento de Profissionais, ela '
          'nasce com Situação <b>"Aberto"</b> e Saldo Restante igual ao valor total — o relatório só '
          'calcula e <b>registra a cobrança</b>; o recebimento em si (o paciente efetivamente pagando) é '
          'lançado depois, manualmente, dando baixa nessa conta quando o dinheiro entrar de fato.'),
    ('img', '09-conta-a-receber-gerada-pela-cobranca.png',
     'Conferindo em Contas a Receber: a conta do "Paciente 000" (Plano de Contas "Consulta Particular", '
     'R$ 2,00) aparece com Situação "Aberto" e Saldo Restante R$ 2,00 — pendente do recebimento.'),

    ('h2', 'Relatório de Cobrança de Paciente (analítico)'),
    ('p', 'Rota <font face="Courier">/relatorio/valorreceber</font> (sem "/agrupado"). É a versão '
          '<b>detalhada</b> do mesmo cálculo do relatório sintético: em vez de uma linha por paciente, '
          'mostra <b>uma linha por Paciente + Profissional + Especialidade</b>, com Sessões, Sessões a '
          'Receber, Valor da Sessão e Valor a Receber. Os filtros são os mesmos (Agenda, Especialidade, '
          'Paciente, Status), mas esta tela <b>não tem botão para gerar Conta a Receber</b> — só '
          '"Filtros" e "Exportar".'),
    ('img', '10-analitico-inicial.png', 'Tela inicial do relatório analítico, antes de aplicar o filtro.'),
    ('img', '11-analitico-resultado.png',
     'Mesma Agenda (Setembro/2026) do exemplo do sintético, agora aberta por Paciente + Profissional + '
     'Especialidade: o total geral (R$ 22,97) bate exatamente com o sintético.'),
    ('p', 'Serve como tela de <b>conferência/auditoria</b> antes de gerar a cobrança em lote pelo '
          'relatório sintético: permite ver exatamente quais sessões, de qual profissional, estão '
          'compondo o valor total de cada paciente antes de confirmar a geração.'),

    ('h2', 'Proteção contra cobrança em duplicidade'),
    ('p', 'Rodar o relatório sintético mais de uma vez para o mesmo mês <b>não gera cobrança duplicada</b>: '
          'assim que uma Conta a Receber é gerada para um paciente naquela Agenda, o relatório passa a '
          'marcar esse paciente como <b>"Conta a receber gerada"</b> e esconde o checkbox de seleção dele '
          '— só volta a aparecer selecionável se essa conta for cancelada. Isso evita cobrar o mesmo '
          'paciente duas vezes pelas mesmas sessões.'),
    ('img', '12-sintetico-com-cobrancas-ja-geradas.png',
     'Depois de gerado, o paciente já cobrado (ex.: "Paciente 0005") aparece com o aviso "Conta a receber '
     'gerada" no lugar do checkbox, impedindo nova seleção para aquele mesmo mês.'),

    ('aviso', 'Esta é uma das rotinas que <b>geram Conta a Receber automaticamente</b>: em vez de lançar '
              'manualmente uma conta para cada paciente todo mês, o sistema calcula e gera tudo de uma vez '
              'a partir dos atendimentos particulares realizados e da Tabela de Valores configurada — o '
              'Plano de Contas usado costuma ser algo como "Consulta Particular". Assim como no Pagamento '
              'de Profissionais, a conta nasce <b>em aberto</b>: a baixa/recebimento em si é um passo '
              'manual separado, feito quando o paciente realmente paga.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cobranca_de_Paciente.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cobranca_de_Paciente_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Cobranca_de_Paciente.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
