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
TITULO = "Movimentos Financeiros"
SUBTITULO = "O que é, de onde vem e para que serve o extrato de cada Conta Financeira"
VIDEO_NOME = "video-movimentos-financeiros-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('<b>Movimentos Financeiros</b> é o extrato interno do sistema: cada linha é uma entrada ou '
         'saída de dinheiro em uma Conta Financeira específica (um banco ou o caixa), com data, valor '
         'e origem. A tela serve para <b>conferir esse extrato contra o extrato real do banco</b> '
         '(conciliação), fazer transferências entre contas do sistema e, se necessário, excluir um '
         'lançamento incorreto.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'O que é e de onde vem cada linha'),
    ('p', 'Acesso em <b>Financeiro → Movimentos → Movimentos Financeiros</b> (rota '
          '<i>financeiro/movimentos</i>). Cada linha da lista representa um lançamento numa Conta '
          'Financeira, gerado automaticamente pelo sistema — nesta tela não existe um botão de '
          '"lançamento manual avulso"; as únicas formas de gerar uma linha nova aqui são as baixas do '
          'financeiro e a Transferência entre Contas (explicada mais abaixo).'),
    ('img', '00-lista-e-indicador-conciliacao.png', 'Lista de Movimentos Financeiros com os filtros e o card de Conciliação no topo.'),
    ('tabela', [
        ('Baixa de Conta a Pagar', 'Toda vez que um pagamento é registrado com uma Conta Financeira informada, gera uma linha de Saída.', 'ContaPagarBaixaRepository.cs'),
        ('Baixa de Conta a Receber', 'Todo recebimento registrado com uma Conta Financeira informada gera uma linha de Entrada.', 'ContaReceberBaixaRepository.cs'),
        ('Transferência entre Contas', 'O botão "Nova Transferência" desta própria tela gera duas linhas ao mesmo tempo: uma Saída na conta de origem e uma Entrada na conta de destino.', 'MovimentoFinanceiroRepository.cs (Transferir)'),
    ]),
    ('aviso', 'Se uma baixa de Conta a Pagar/Receber for cancelada ou excluída, o sistema '
              '<b>remove automaticamente</b> (some da lista) o Movimento Financeiro que ela tinha '
              'gerado — não é preciso fazer nada manualmente nesta tela nesse caso.'),

    ('h2', 'Para que serve'),
    ('p', 'É a base para três outras telas do módulo Financeiro: o saldo de cada Conta Financeira, o '
          '<b>Fluxo de Caixa</b> e o <b>Dashboard Financeiro</b> são todos calculados a partir dessas '
          'mesmas linhas. Na prática, esta tela funciona como o "extrato bancário" de cada conta dentro '
          'do sistema, usado para <b>conciliar</b> com o extrato real do banco.'),

    ('h2', 'Filtros'),
    ('tabela', [
        ('Período - Início/Fim', 'Obrigatório; vem com o mês corrente por padrão.', 'DataMovimento'),
        ('Conta Financeira', 'Filtra só os lançamentos de uma conta.', 'IdContaFinanceira'),
        ('Tipo', 'Entrada ou Saída.', 'TipoMovimento'),
        ('Origem', 'Conta a Pagar, Conta a Receber ou Transferência.', 'Origem'),
        ('Conciliado', 'Sim, Não ou Todos.', 'Conciliado'),
    ]),

    ('h2', 'Card "Conciliação"'),
    ('p', 'Mostra três números — <b>Total</b>, <b>Conciliado</b> (verde) e <b>Não Conciliado</b> '
          '(vermelho) — e uma barra de progresso, somando o valor de todos os lançamentos do período '
          '(e da conta, se filtrada). É recalculado toda vez que "Buscar" é clicado.'),

    ('h2', 'Conciliar / Desconciliar'),
    ('p', 'O botão verde (✓) marca o lançamento como <b>conciliado</b> — ou seja, confirma que aquele '
          'valor bate com o extrato real do banco naquele dia. É uma ação de um clique, sem pedir '
          'motivo. Um lançamento conciliado ganha o botão amarelo <b>"Desconciliar"</b> (desfazer), '
          'caso a conciliação tenha sido feita por engano.'),
    ('img', '01-apos-conciliar.png', 'Linha conciliada: "Sim" em verde na coluna Conciliado e o botão amarelo de desconciliar.'),
    ('aviso', 'Um lançamento <b>conciliado não pode ser excluído</b> diretamente — é preciso '
              'desconciliar primeiro (o botão vermelho de excluir some da linha assim que ela é '
              'conciliada).'),

    ('h2', 'Excluir um lançamento'),
    ('p', 'O botão vermelho (lixeira), disponível só em linhas não conciliadas, pede o '
          '<b>Motivo da exclusão</b> antes de confirmar.'),
    ('img', '02-modal-motivo-exclusao.png', 'Modal "Excluir Movimento Financeiro" pedindo o motivo.'),
    ('aviso', 'Excluir um lançamento aqui é uma ação isolada: <b>não desfaz</b> a baixa de Conta a '
              'Pagar/Receber que o gerou — só remove esta linha específica do extrato. Se o lançamento '
              'excluído era referente a uma baixa, o ideal é cancelar a baixa na tela de origem, não '
              'excluir por aqui.'),

    ('h2', 'Nova Transferência entre Contas'),
    ('p', 'Usada para registrar uma movimentação interna, como um saque do banco para reforçar o '
          'caixa físico, ou um depósito do dinheiro do caixa na conta bancária. Pede Data, Conta de '
          'Origem, Conta de Destino (diferentes entre si), Valor, <b>Plano de Contas</b>, '
          '<b>Centro de Custo</b> e um Histórico opcional.'),
    ('img', '03-nova-transferencia-preenchida.png', 'Modal "Nova Transferência entre Contas" preenchido.'),
    ('img', '04-apos-transferencia.png',
     'Após salvar: duas novas linhas aparecem na lista, uma Entrada na conta de destino e uma Saída na conta de origem, ambas com Origem "Transferência".'),
    ('aviso', 'Assim como qualquer outro lançamento financeiro do sistema, a transferência exige um '
              'Plano de Contas e um Centro de Custo — são usados para que ela também apareça '
              'corretamente classificada nos relatórios de Fluxo de Caixa "Por Plano de Conta" e '
              '"Por Centro de Custo".'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Movimentos_Financeiros.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Movimentos_Financeiros_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Movimentos_Financeiros.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
