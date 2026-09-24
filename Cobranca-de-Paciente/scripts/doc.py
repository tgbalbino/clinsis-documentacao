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
DATA = "18/09/2026"
TITULO = "Cobrança de Paciente"
SUBTITULO = "Calcular e gerar, de uma vez, a cobrança de todos os pacientes particulares do mês"
VIDEO_NOME = "https://youtu.be/AdzPSoJ7_4I"
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
