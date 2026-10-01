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
TITULO = 'Cadastro de Centro de Custo'
SUBTITULO = 'Como organizar a clínica em setores para saber onde o dinheiro entra e sai'
VIDEO_NOME = "https://youtu.be/TGcyxaZc2QY"
INTRO = 'O Centro de Custo identifica QUAL SETOR da clínica está envolvido em uma entrada ou saída de dinheiro (ex.: "Consultório 1", "Recepção", "Administrativo/Financeiro"). Junto com o Plano de Contas, é um cadastro pré-requisito das demais telas financeiras (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin com pagamento, fechamento de Contrato). Recomendamos configurar essa tela antes de usar as demais rotinas financeiras.'
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [('h2', 'Barra de ações'),
 ('p', 'No alto da lista ficam o botão azul <b>Novo</b> (em destaque), o botão <b>Filtros</b> — que mostra um número quando há filtro aplicado, com um <b>✕</b> ao lado para limpar tudo de uma vez — e o botão de <b>Atualizar</b>, só com o ícone. Só a lista rola; o título e a barra de ações ficam sempre visíveis.'),
 ('img', '00-lista-inicial.png', 'Lista de Centros de Custo com a barra de ações (Novo, Filtros, Atualizar).'),
('h2', 'Diferença entre Plano de Conta e Centro de Custo'),
 ('p',
  'É comum confundir os dois: o Plano de Conta responde "o que é" o lançamento (ex.: Aluguel, Consulta por '
  'Convênio), enquanto o Centro de Custo responde "de onde/para qual setor" (ex.: Recepção, Consultório 1). '
  'O mesmo lançamento de "Aluguel" pode ser dividido entre Centros de Custo diferentes se a clínica tiver '
  'mais de uma unidade ou setor pagando aluguel separadamente.'),
 ('img',
  '00-lista-inicial.png',
  'Tela inicial: lista simples com Descrição e Situação de cada centro de custo já cadastrado.'),
 ('h2', 'Cadastrando um novo Centro de Custo (exemplo)'),
 ('p',
  'Clique em Novo. A tela é bem simples: só pede a Descrição do setor e se ele está Ativo. No exemplo '
  'abaixo, criamos o centro de custo "FISIOTERAPIA".'),
 ('img', '01-novo-modal-preenchido.png', 'Cadastro de um novo Centro de Custo: Descrição = "FISIOTERAPIA".'),
 ('tabela',
  [('Descrição',
    'Nome do setor/área da clínica, como vai aparecer em todos os relatórios e telas financeiras.',
    'Obrigatório; máx. 100 caracteres'),
   ('Ativo',
    'Centros inativos continuam existindo (para não quebrar lançamentos antigos), mas somem das listas de '
    'seleção ao lançar novas contas a pagar/receber.',
    'CentroCustoController.cs')]),
 ('img', '02-apos-salvar.png', 'Depois de salvar, "FISIOTERAPIA" já aparece na lista.'),
 ('h2', 'Filtrando centros de custo cadastrados'),
 ('p',
  'O botão Filtros permite buscar por Descrição ou Situação (Ativo/Inativo), útil quando a clínica tem '
  'muitos setores cadastrados.'),
 ('img', '04-resultado-filtro.png', 'Resultado do filtro por Descrição contendo "FISIO".'),
 ('h2', 'Atalho: Importar Centros de Custo Padrão'),
 ('p',
  'Quando não existe nenhum centro de custo cadastrado ainda, a tela mostra um botão "Importar Centros de '
  'Custo Padrão", que cria de uma vez uma lista pronta de setores comuns em clínicas (Recepção, Consultório, '
  'Administrativo/Financeiro, etc.).'),
 ('aviso',
  'Este cadastro não gera Conta a Pagar nem Conta a Receber por si só — ele só define os setores que serão '
  'usados quando essas contas forem lançadas em outras telas do sistema (Contas a Pagar, Contas a Receber, '
  'Contas Recorrentes, Checkin, Contrato).')]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Centro_de_Custo.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Centro_de_Custo_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Centro_de_Custo.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
