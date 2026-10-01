# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/_scripts-comuns"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts-comuns"))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.1'
DATA = '29/09/2026'
TITULO = 'Contas Recorrentes'
SUBTITULO = 'Contas que se repetem todo mês (ou a cada período) geradas automaticamente'
VIDEO_NOME = "https://youtu.be/74XN1Jb4f_c"
INTRO = 'Contas Recorrentes serve para cadastrar UMA VEZ uma despesa ou receita que se repete sempre (ex.: aluguel, mensalidade de software, salário de um profissional fixo) e deixar o próprio sistema gerar automaticamente o lançamento em Contas a Pagar (ou Contas a Receber) a cada novo período — sem precisar cadastrar tudo de novo todo mês. Esta rotina exige Plano de Conta, Centro de Custo e um Favorecido (Pessoa) já cadastrados antes de usar.'
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [('h2', 'Barra de ações'),
 ('p', 'No alto da lista ficam o botão azul <b>Novo</b> (em destaque), o botão <b>Filtros</b> — que mostra um número quando há filtro aplicado, com um <b>✕</b> ao lado para limpar tudo —, o botão de <b>Atualizar</b>, só com o ícone, e o botão discreto <b>Log do Job</b>, que abre o histórico das execuções automáticas.'),
 ('img', '00-lista-inicial.png', 'Lista de Contas Recorrentes com a barra de ações (Novo, Filtros, Atualizar e Log do Job).'),
 ('h2', 'Tela inicial'),
 ('p',
  'Lista todas as contas recorrentes já cadastradas, com Favorecido, Plano de Contas, Centro de Custo, '
  'Descrição, Frequência, Dia de Vencimento, período de vigência (Início/Fim) e Valor.'),
 ('img', '00-lista-inicial.png', 'Tela inicial de Contas Recorrentes.'),
 ('h2', 'Cadastrando uma nova conta recorrente (exemplo)'),
 ('p',
  'Clique em Novo. No exemplo abaixo, cadastramos um aluguel de R$ 1.500,00, mensal, vencendo todo dia 10, '
  'começando hoje.'),
 ('img',
  '01-novo-modal-preenchido.png',
  'Cadastro de exemplo: aluguel mensal de R$ 1.500,00, vencendo dia 10.'),
 ('tabela',
  [('Favorecido',
    'Pessoa (fornecedor, profissional, cliente) para quem o pagamento é feito ou de quem o recebimento vem.',
    'Obrigatório'),
   ('Plano de Contas',
    'Categoria do lançamento (ex.: Aluguel). Precisa estar cadastrado antes, na tela de Plano de Contas.',
    'Obrigatório; validado em ContaRecorrenteController.cs'),
   ('Centro de Custo',
    'Setor da clínica responsável pelo lançamento. Precisa estar cadastrado antes, na tela de Centro de '
    'Custo.',
    'Obrigatório; validado em ContaRecorrenteController.cs'),
   ('Descrição', 'Texto livre identificando o lançamento nas contas geradas.', 'Obrigatório'),
   ('Valor', 'Valor de cada parcela gerada automaticamente.', 'Obrigatório'),
   ('Dia Vencimento', 'Dia do mês (1 a 31) em que a conta gerada deve vencer.', 'Obrigatório'),
   ('Frequência',
    'De quanto em quanto tempo o sistema gera uma nova conta: Mensal, Bimestral, Trimestral, Semestral ou '
    'Anual.',
    'Obrigatório'),
   ('Data Início / Data Fim',
    'Período em que a recorrência vale. Data Fim vazia = sem previsão de encerramento.',
    'Data Início obrigatória'),
   ('Gerar Antecedência',
    'Quantos dias antes do vencimento o sistema já pode gerar a conta (para dar tempo de conferir/pagar '
    'antes do prazo).',
    'Opcional, padrão 0')]),
 ('img', '02-apos-salvar.png', 'Depois de salvar, a nova recorrência aparece na lista.'),
 ('h2', 'Como a geração automática acontece'),
 ('p',
  'Todos os dias, um job (rotina automática) do sistema roda de madrugada e verifica quais contas '
  'recorrentes precisam gerar um novo lançamento naquele dia (considerando a frequência, o dia de vencimento '
  'e a antecedência configurada). Quando isso acontece, o sistema cria automaticamente uma nova Conta a '
  'Pagar (ou Conta a Receber, dependendo do tipo do Plano de Conta) — sem nenhuma ação manual do usuário.'),
 ('p',
  'Para conferir isso sem esperar até a madrugada, esta tela tem o botão Log do Job, que mostra o histórico '
  'de execuções e também permite forçar a execução agora — útil para testar ou para gerar uma conta que '
  'ficou pendente.'),
 ('img',
  '03-log-job.png',
  'Histórico de execuções do job de contas recorrentes, com a opção "Forçar Execução Agora".'),
 ('img',
  '04-log-job-executado.png',
  'Depois de forçar a execução: uma nova linha aparece no histórico (Status "OK", "Qtd. Gerada" = quantas '
  'contas foram criadas nessa rodada) e um aviso confirma quantas contas foram geradas.'),
 ('h2', 'Onde a conta gerada aparece'),
 ('p',
  'A conta criada automaticamente pelo job aparece normalmente na tela de Contas a Pagar (ou Contas a '
  'Receber, se o Plano de Conta for do tipo Receita), como qualquer outro lançamento — só que já vem com '
  'Favorecido, Plano de Conta, Centro de Custo, Descrição e Valor preenchidos automaticamente, prontos para '
  'conferência e pagamento.'),
 ('img',
  '05-conta-pagar-gerada.png',
  'Tela de Contas a Pagar mostrando a conta "ALUGUEL DA SALA 2" gerada automaticamente pelo job, já com '
  'vencimento no dia 10 configurado.'),
 ('aviso',
  'Esta é uma das rotinas que geram Conta a Pagar/Receber automaticamente: o usuário cadastra a recorrência '
  'uma única vez, e o sistema cuida de criar os lançamentos a cada período, sem precisar repetir o cadastro '
  'manualmente todo mês.')]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_Recorrentes.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_Recorrentes_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_Recorrentes.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
