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
DATA = '07/10/2026'
NOME = 'Estorno_de_Baixas'
TITULO = "Estorno de Baixas"
SUBTITULO = "Contas a Receber e Contas a Pagar: como estornar e como conferir no Dashboard e nos relatórios"
VIDEO_NOME = "video-estorno-de-baixas-com-legenda.mp4"
INTRO = ('<b>Estornar</b> uma baixa é cancelar um recebimento ou um pagamento que foi lançado errado (conta errada, '
         'valor ou data incorretos, duplicidade, ou pagamento que não aconteceu). O ClinSis <b>não apaga</b> o lançamento: '
         'ele fica no histórico, marcado como estornado, com <b>quem</b> estornou, <b>quando</b> e <b>por quê</b>, e o título '
         'volta a ficar em aberto com o saldo integral. Este manual mostra o passo a passo nas Contas a Receber e nas '
         'Contas a Pagar e como conferir o efeito no <b>Dashboard Financeiro</b>, nos <b>relatórios</b> e nos '
         '<b>Movimentos Financeiros</b>.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado. Os valores do exemplo (R$ 400,00 recebido e R$ 350,00 pago, estornados) '
          'foram criados só para este manual.')

blocks = [
    ('h2', 'O exemplo deste manual'),
    ('p', 'Para mostrar o antes e o depois, foram lançadas quatro baixas em dinheiro no mesmo dia, na conta financeira '
          '<b>Caixa</b>: dois recebimentos (R$ 400,00 e R$ 250,00) e dois pagamentos (R$ 350,00 e R$ 120,00). '
          'Depois foram estornados o recebimento de <b>R$ 400,00</b> e o pagamento de <b>R$ 350,00</b>; os outros dois '
          'ficaram ativos para servir de comparação.'),
    ('tabelagen', ['Baixa', 'Valor', 'O que foi feito'],
     [['Recebimento — Paciente 0002', 'R$ 400,00', 'Estornado'],
      ['Recebimento — Paciente 0003', 'R$ 250,00', 'Mantido'],
      ['Pagamento — Energia elétrica', 'R$ 350,00', 'Estornado'],
      ['Pagamento — Material de limpeza', 'R$ 120,00', 'Mantido']],
     [8, 3.5, 6]),

    ('h2', 'Antes do estorno: o que os totais mostram'),
    ('p', 'Com as quatro baixas ativas, o <b>Dashboard Financeiro</b> do mês (<b>Financeiro → Dashboard</b>) mostra '
          '<b>Entradas R$ 650,00</b>, <b>Saídas R$ 470,00</b> e <b>Resultado do Período R$ 180,00</b>. O saldo da conta '
          'Caixa é de R$ 180,00.'),
    ('img', '01-dashboard-antes.png', 'Dashboard Financeiro antes do estorno: entradas R$ 650,00, saídas R$ 470,00, resultado R$ 180,00.'),
    ('p', 'Os relatórios <b>Recebimentos</b> e <b>Pagamentos</b> (menu <b>Relatórios</b>) listam as mesmas baixas, e '
          '<b>Financeiro → Movimentos → Mov. Financeiros</b> mostra um lançamento na conta Caixa para cada baixa.'),
    ('img', '02-rel-recebimentos-antes.png', 'Relatório de Recebimentos: as duas baixas ativas.'),
    ('img', '03-rel-pagamentos-antes.png', 'Relatório de Pagamentos: as duas baixas ativas.'),
    ('img', '04-movimentos-antes.png', 'Movimentos Financeiros: duas entradas e duas saídas na conta Caixa, total de R$ 1.120,00.'),

    ('h2', 'Como estornar um recebimento (Contas a Receber)'),
    ('p', 'Acesso em <b>Financeiro → Movimentos → Contas a Receber</b>. Localize o título (situação <b>Baixada</b>) e '
          'clique no botão verde de pagamento (<b>$</b>).'),
    ('img', '05-lista-receber-quitado.png', 'Contas a Receber: o título de R$ 400,00 está baixado, com saldo zerado.'),
    ('p', 'Na janela <b>Acertos / Recebimentos</b>, abra a aba <b>Histórico / Estornos</b>. Ela lista todas as baixas do '
          'título, ativas e estornadas. Para estornar, clique na <b>lixeira vermelha</b> da linha.'),
    ('img', '06-receber-historico.png', 'Aba Histórico / Estornos: a baixa de R$ 400,00 está ativa e tem o botão de estorno.'),
    ('p', 'O sistema pede o <b>motivo do cancelamento</b>, que é obrigatório. Os motivos são cadastrados em '
          '<b>Tabelas Aux. → Motivo Estorno</b>; no exemplo: <i>Recebimento lançado em conta errada</i>, '
          '<i>Valor ou data do recebimento incorretos</i>, <i>Recebimento registrado em duplicidade</i> e '
          '<i>Recebimento não realizado</i>.'),
    ('img', '07-receber-motivo.png', 'Escolha do motivo e confirmação do cancelamento.'),
    ('p', 'Depois de confirmar, aparece a mensagem <b>Estornado</b>. A baixa continua no histórico, em vermelho, com a '
          'data, o usuário e o motivo do estorno. O <b>Valor Restante</b> do título volta ao valor original, e a lixeira '
          'some: uma baixa estornada não pode ser estornada de novo.'),
    ('img', '08-receber-estornado.png', 'A baixa fica como Estornado, com data, usuário e motivo; o saldo volta a R$ 400,00.'),
    ('p', 'Na lista de Contas a Receber o título volta para <b>Aberto</b>, com o saldo integral. Se o lançamento estava '
          'errado, basta lançar a baixa correta.'),
    ('img', '09-receber-reaberto.png', 'O título voltou para Aberto, com saldo de R$ 400,00 (a baixa de R$ 250,00 do outro paciente segue Baixada).'),

    ('h2', 'Como estornar um pagamento (Contas a Pagar)'),
    ('p', 'Acesso em <b>Financeiro → Movimentos → Contas a Pagar</b>. Clique no botão verde de pagamento (<b>$</b>) da '
          'conta quitada.'),
    ('img', '10-lista-pagar-quitado.png', 'Contas a Pagar: energia elétrica de R$ 350,00, Quitada.'),
    ('p', 'Na janela <b>Pagamento / Acerto da Conta a Pagar</b>, abra a aba <b>Histórico / Estornos</b>. Para estornar, '
          'clique no botão vermelho de <b>cancelar</b> (círculo cortado). O botão azul <b>i</b> mostra os detalhes do pagamento.'),
    ('img', '11-pagar-historico.png', 'Histórico da conta: o pagamento de R$ 350,00 está ativo.'),
    ('p', 'Escolha o <b>motivo do cancelamento</b> (obrigatório) e clique em <b>Confirmar Cancelamento</b>.'),
    ('img', '12-pagar-motivo.png', 'Motivo do cancelamento do pagamento.'),
    ('p', 'O pagamento passa a aparecer como <b>Cancelado</b> e a janela informa o <b>Total Cancelado</b>.'),
    ('img', '13-pagar-estornado.png', 'Pagamento cancelado; total cancelado de R$ 350,00.'),
    ('img', '14-pagar-reaberto.png', 'A conta voltou para Aberto, com o saldo integral.'),

    ('h2', 'Conferência no Dashboard Financeiro'),
    ('p', 'Com o mesmo período, o Dashboard passa a refletir apenas as baixas ativas:'),
    ('tabelagen', ['Indicador', 'Antes', 'Depois', 'Diferença'],
     [['Entradas', 'R$ 650,00', 'R$ 250,00', '− R$ 400,00 (recebimento estornado)'],
      ['Saídas', 'R$ 470,00', 'R$ 120,00', '− R$ 350,00 (pagamento cancelado)'],
      ['Resultado do Período', 'R$ 180,00', 'R$ 130,00', 'Entradas − Saídas'],
      ['Saldo da conta Caixa', 'R$ 180,00', 'R$ 130,00', 'Saiu a entrada e voltou a saída']],
     [5, 3, 3, 6.5]),
    ('img', '15-dashboard-depois.png', 'Dashboard depois do estorno: entradas R$ 250,00, saídas R$ 120,00, resultado R$ 130,00.'),
    ('p', 'As tabelas <b>Entradas e Saídas por Plano de Conta</b> e <b>Maiores Pagamentos / Recebimentos por Pessoa</b> '
          'também deixam de contar o que foi estornado. O card <b>Recebido em atraso</b> desconta as baixas estornadas.'),

    ('h2', 'Conferência nos relatórios'),
    ('p', 'Os relatórios <b>Recebimentos</b> e <b>Pagamentos</b> têm o filtro <b>Situação</b>:'),
    ('tabelagen', ['Situação', 'O que lista'],
     [['Todas', 'Baixas ativas e estornadas. As estornadas ficam com o selo vermelho (Excluída no recebimento, Cancelado no pagamento).'],
      ['Somente ativas', 'Só as baixas que continuam valendo.'],
      ['Somente excluídas / canceladas', 'Só as estornadas, para auditoria.']],
     [5.5, 12]),
    ('img', '16-rel-recebimentos-todas.png', 'Recebimentos, situação Todas: a baixa estornada aparece como Excluída, mas o total é só das ativas (R$ 250,00).'),
    ('img', '17-rel-recebimentos-ativas.png', 'Situação Somente ativas: a baixa estornada sai da lista.'),
    ('img', '18-rel-pagamentos-depois.png', 'Pagamentos, situação Todas: o pagamento Cancelado aparece, mas o total soma só os ativos (R$ 120,00).'),
    ('aviso', 'Nos dois relatórios, os totais (rodapé e agrupamento Mensal por Forma de Pagamento) consideram somente '
              'as baixas ativas. Uma baixa estornada nunca soma, mesmo aparecendo na lista.'),

    ('h2', 'Conferência nos Movimentos Financeiros'),
    ('p', 'O lançamento gerado pela baixa <b>não é apagado</b> do banco de dados: ele é marcado como <b>excluído</b>, com o '
          'usuário, a data e o motivo do estorno. Por isso deixa de aparecer em <b>Movimentos Financeiros</b> e não entra '
          'mais nos saldos, no Dashboard, no extrato nem na conciliação bancária.'),
    ('img', '19-movimentos-depois.png', 'Movimentos Financeiros depois do estorno: só restam a entrada de R$ 250,00 e a saída de R$ 120,00.'),

    ('h2', 'O que o estorno altera no sistema'),
    ('tabela', [
        ('Baixa do recebimento', 'Marcada como excluída, com usuário, data e motivo. Continua no Histórico / Estornos.', 'ContaReceberBaixa.Excluido / ExcluidoIdUsuario / ExcluidoData / IdMotivo'),
        ('Título a receber', 'Volta para Aberto, com o saldo integral.', 'ContaReceber.Status / Saldo'),
        ('Baixa do pagamento', 'Marcada como cancelada, com usuário, data e motivo. Continua no Histórico / Estornos.', 'ContaPagarBaixa.Cancelado / DataCancelamento / IdUsuarioCancelamento / IdMotivo / MotivoCancelamento'),
        ('Conta a pagar', 'Volta para Aberto, com o saldo integral e o valor pago recalculado.', 'ContaPagar.Situacao / ValorPago / Saldo'),
        ('Movimento financeiro', 'Marcado como excluído, com usuário, data e motivo; sai de saldos, Dashboard e extrato.', 'MovimentoFinanceiro.Excluido / DataExclusao / IdUsuarioExclusao / IdMotivo / MotivoExclusao'),
        ('Caixa', 'Se a baixa foi feita em um caixa, o estorno registra uma observação nele (quem, quando e o motivo).', 'Caixa.Observacao'),
    ]),

    ('h2', 'Regras e bloqueios'),
    ('tabelagen', ['Situação', 'O que o sistema faz'],
     [['Motivo não informado', 'Não estorna. O motivo é obrigatório e precisa estar cadastrado para a rotina (Contas a Receber ou Contas a Pagar).'],
      ['Caixa da baixa já fechado', 'Bloqueia e orienta pedir a um administrador para reabrir o caixa antes de estornar.'],
      ['Cheque já compensado ou cartão com parcela repassada', 'Bloqueia o estorno direto. Antes é preciso devolver a liquidação financeira (veja o manual de Cheques e Liquidação).'],
      ['Baixa já estornada', 'Não oferece novo estorno (a lixeira some e o pagamento aparece como Cancelado).'],
      ['Título com baixa ativa', 'Uma conta a pagar com baixa registrada não pode ser cancelada: estorne primeiro a baixa.']],
     [5.5, 12]),
    ('aviso', 'Estornar não é excluir: tudo fica registrado para auditoria. Se o lançamento estava errado, estorne e lance a '
              'baixa correta em seguida.'),
]

render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
