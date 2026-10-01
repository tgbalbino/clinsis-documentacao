# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.1'
DATA = '29/09/2026'
TITULO = 'Dashboard Financeiro e Fluxo de Caixa'
SUBTITULO = 'O que é cada informação exibida na tela e de onde ela vem no sistema'
VIDEO_NOME = "https://youtu.be/WCa8gVOdXKE"
INTRO = ('O <b>Dashboard Financeiro</b> resume, num período escolhido, o que entrou, o que saiu, o saldo de cada conta e '
         'os maiores pagamentos e recebimentos. O <b>Fluxo de Caixa</b> mostra a movimentação dia a dia (ou por semana/mês) e '
         'ainda projeta o saldo futuro a partir das contas a pagar e a receber em aberto. Este documento explica cada '
         'campo das duas telas.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', '1. Dashboard Financeiro'),
    ('p', 'Acesso em <b>Financeiro → Dashboard</b>. Mostra um resumo financeiro da clínica dentro do período escolhido, '
          'com opção de restringir por Conta Financeira, Centro de Custo e Plano de Conta.'),
    ('h2', 'Filtros e botões do topo'),
    ('p', '<b>Período - Início / Período - Fim</b> definem o intervalo (com base na data do movimento financeiro). '
          '<b>Conta Financeira</b>, <b>Centro de Custo</b> e <b>Plano de Conta</b> são opcionais: "Todas"/"Todos" traz tudo. '
          'O botão azul <b>Buscar</b> carrega os dados e o botão só com o ícone de borracha <b>Limpa</b> os filtros. '
          'No celular, os filtros ficam recolhidos numa barra com o resumo do período e a quantidade de filtros aplicados; '
          'toque nela para abrir.'),
    ('img', '00-dashboard-inicial.png', 'Tela ao abrir, antes de aplicar qualquer filtro.'),
    ('h2', 'Indicadores do topo (caixas coloridas)'),
    ('img', '02-dashboard-resultado.png', 'Resultado após clicar em "Buscar": indicadores, juros/descontos, saldo por conta, entradas/saídas por plano de conta, rankings e comparativo mensal.'),
    ('tabela', [
        ('Entradas (caixa verde)', 'Soma de todos os lançamentos de entrada do período, dentro do filtro de conta, centro de custo e plano de conta escolhidos.', 'MovimentoFinanceiro (TipoMovimento = 1)'),
        ('Saídas (caixa vermelha)', 'Igual ao anterior, somando os lançamentos de saída.', 'MovimentoFinanceiro (TipoMovimento = 2)'),
        ('Resultado do Período (caixa azul)', 'Entradas − Saídas do período (cálculo simples, feito na própria tela).', 'Cálculo na tela'),
        ('Saldo das Contas (caixa amarela)', 'Soma do saldo atual de cada Conta Financeira ativa. É o saldo acumulado de toda a história da conta e não fica restrito ao período do filtro.', 'MovimentoFinanceiro por conta'),
        ('Juros Recebido', 'Soma dos juros registrados nas baixas de Contas a Receber cuja data de pagamento caiu no período.', 'ContaReceberBaixa'),
        ('Desconto Concedido', 'Soma do desconto dado ao paciente nas baixas de Contas a Receber no período.', 'ContaReceberBaixa'),
        ('Juros Pago', 'Soma dos juros pagos nas baixas de Contas a Pagar no período (por atraso).', 'ContaPagarBaixa'),
        ('Desconto Obtido', 'Soma do desconto conseguido nas baixas de Contas a Pagar no período.', 'ContaPagarBaixa'),
    ]),
    ('h2', 'Tabelas do meio da tela'),
    ('tabela', [
        ('Saldo por Conta Financeira', 'Uma linha para cada Conta Financeira ativa, com o saldo acumulado desde o início (entradas menos saídas), sem depender do período. Fica em vermelho quando o saldo é negativo.', 'MovimentoFinanceiro'),
        ('Entradas por Plano de Conta', 'Soma das entradas do período agrupadas pelo Plano de Conta de cada lançamento. Sem plano, aparece como "Sem plano de conta".', 'MovimentoFinanceiro'),
        ('Saídas por Plano de Conta', 'Mesma lógica, somando as saídas do período por Plano de Conta.', 'MovimentoFinanceiro'),
    ]),
    ('h2', 'Rankings e comparativo mensal'),
    ('tabela', [
        ('Maiores Pagamentos por Pessoa', 'Para cada pessoa (fornecedor/prestador), soma o valor pago mais os juros pagos nas baixas de Contas a Pagar do período, do maior para o menor.', 'ContaPagarBaixa'),
        ('Maiores Recebimentos por Pessoa', 'Igual, para Contas a Receber: valor recebido mais juros, do maior para o menor.', 'ContaReceberBaixa'),
        ('Comparativo Mensal — Entradas/Saídas/Resultado', 'Compara o mês informado com o imediatamente anterior, com a mesma lógica de Entradas/Saídas do topo, sem os filtros de conta, centro de custo e plano.', 'MovimentoFinanceiro'),
        ('Comparativo Mensal — Variação', '(atual − anterior) ÷ anterior × 100. Verde quando positiva ou zero, vermelha quando negativa; fica "-" quando o mês anterior não teve valor.', 'Cálculo na tela'),
    ]),

    ('h2', '2. Fluxo de Caixa'),
    ('p', 'Acesso em <b>Financeiro → Fluxo de Caixa</b>. Mostra a movimentação dia a dia (ou agrupada por semana/mês) dentro de um '
          'período, separando o que já aconteceu ("Realizado") do que está previsto ("Projetado", a partir das contas a pagar e '
          'a receber ainda em aberto).'),
    ('h2', 'Filtros'),
    ('p', 'Além do período, conta, centro de custo e plano de conta (iguais aos do Dashboard), a tela tem <b>Mostrar</b> '
          '(Realizado + Projetado, Somente Realizado ou Somente Projetado) e, com "Somente Realizado", o campo <b>Agrupamento</b> '
          '(Dia, Semana ou Mês). O botão <b>Buscar</b> carrega os dados e o botão de borracha limpa os filtros.'),
    ('aviso', 'O intervalo entre a data de início e a de fim não pode passar de <b>2 anos</b> no Fluxo de Caixa; períodos maiores '
              'são recusados e a tela não atualiza. Escolha um período menor.'),
    ('img', '10-fluxo-inicial.png', 'Tela ao abrir, antes de aplicar qualquer filtro.'),
    ('img', '11-fluxo-resultado.png', 'Indicadores de resumo, bloco "Fluxo de Caixa Projetado", gráfico e tabela, logo após "Buscar".'),
    ('tabela', [
        ('Saldo Inicial', 'Saldo acumulado de todos os movimentos registrados antes da data de início do filtro: quanto já existia em caixa na véspera do período.', 'MovimentoFinanceiro'),
        ('Entradas / Saídas', 'Soma das entradas e saídas dentro do período filtrado (mesma lógica do Dashboard).', 'MovimentoFinanceiro'),
        ('Resultado', 'Entradas − Saídas do período.', 'Cálculo na tela'),
        ('Saldo Final', 'Saldo Inicial + Resultado: o saldo em caixa no último dia do período.', 'Cálculo na tela'),
    ]),
    ('h2', 'Bloco "Fluxo de Caixa Projetado" (previsão)'),
    ('p', 'Aparece quando "Mostrar" inclui "Projetado".'),
    ('tabela', [
        ('Saldo Atual', 'Saldo de todos os movimentos financeiros já registrados até hoje (histórico completo): o ponto de partida da projeção.', 'MovimentoFinanceiro'),
        ('Recebimentos Previstos', 'Soma do saldo em aberto das Contas a Receber com vencimento antes da data de fim do filtro.', 'ContaReceber'),
        ('Pagamentos Previstos', 'Soma do saldo em aberto das Contas a Pagar não canceladas com vencimento antes da data de fim do filtro.', 'ContaPagar'),
        ('Saldo Projetado', 'Saldo Atual + Recebimentos Previstos − Pagamentos Previstos: estimativa do que vai sobrar em caixa na data de fim, se tudo for recebido/pago como previsto.', 'Cálculo na tela'),
    ]),
    ('h2', 'Gráfico e tabela por período'),
    ('p', 'O gráfico <b>Saldo acumulado</b> desenha a evolução da coluna "Saldo Acumulado" da tabela logo abaixo.'),
    ('tabela', [
        ('Período', 'Cada linha é um dia (ou semana/mês, conforme o Agrupamento) dentro do intervalo filtrado.', 'Filtro de período'),
        ('Entradas / Saídas da linha', 'Soma das entradas e saídas daquele dia, semana ou mês.', 'MovimentoFinanceiro'),
        ('Resultado da linha', 'Entradas − Saídas daquele período; vermelho quando negativo.', 'Cálculo na tela'),
        ('Saldo Acumulado', 'Saldo Inicial somado, linha a linha, ao Resultado de cada período; vermelho quando negativo.', 'Cálculo na tela'),
    ]),
    ('h2', 'Por Conta Financeira e Por Centro de Custo'),
    ('tabela', [
        ('Por Conta Financeira', 'Para cada Conta Financeira ativa, soma as entradas e saídas do período e calcula o Resultado. A linha Total soma todas as contas.', 'MovimentoFinanceiro'),
        ('Por Centro de Custo', 'Mesma lógica por Centro de Custo (sem centro aparece como "Sem centro de custo"), ordenado pelo resultado, do maior para o menor.', 'MovimentoFinanceiro'),
    ]),
    ('h2', 'Exemplo com Agrupamento = Mês'),
    ('p', 'Com "Somente Realizado" e Agrupamento "Mês", a tabela passa a ter uma linha por mês em vez de uma por dia, mais fácil de ler em períodos longos.'),
    ('img', '12-fluxo-agrupado-mes.png', 'Mesmo tipo de consulta, agora agrupada por mês.'),

    ('h2', 'Pontos de atenção'),
    ('aviso', 'Todos os valores em dinheiro aparecem no formato R$ 0.000,00 e saldos ou resultados negativos ficam em vermelho. '
              'Nos indicadores: verde = entradas, vermelho = saídas, azul = resultado, amarelo = saldo e cinza = informações '
              'auxiliares (juros, desconto e saldo inicial).'),
    ('aviso', 'O indicador "Saldo das Contas" e a tabela "Saldo por Conta Financeira" mostram sempre o saldo acumulado de toda a '
              'história da conta, independentemente do período escolhido; já Entradas, Saídas e Resultado respeitam o período.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Financeiro_e_Fluxo_de_Caixa.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Financeiro_e_Fluxo_de_Caixa_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Dashboard_Financeiro_e_Fluxo_de_Caixa.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
