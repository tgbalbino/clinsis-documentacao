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
TITULO = 'Cadastro de Plano de Contas'
SUBTITULO = 'Como organizar as categorias de receitas e despesas da clínica'
VIDEO_NOME = "https://youtu.be/KJhezxjX10w"
INTRO = 'O Plano de Contas é a lista de categorias usada para classificar toda entrada e saída de dinheiro da clínica (ex.: "Consulta por Convênio", "Aluguel", "Material de Consumo"). Ele é um cadastro pré-requisito: praticamente todas as outras telas financeiras do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin com pagamento, fechamento de Contrato) exigem que o lançamento tenha um Plano de Conta selecionado. Por isso, recomendamos configurar o Plano de Contas antes de usar as demais rotinas financeiras.'
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [('h2', 'Barra de ações'),
 ('p',
  'No alto da lista ficam os controles da tela: o botão azul <b>Novo</b> (destaque), o botão <b>Filtros</b> — que '
  'mostra um número quando há filtro aplicado, ao lado de um <b>✕</b> para limpar tudo de uma vez — e o botão só com o '
  'ícone de <b>Atualizar</b>. No canto direito, <b>Árvore</b> e <b>Lista</b> trocam a forma de visualização. Só a lista '
  'rola; o título e a barra de ações continuam sempre visíveis.'),
 ('img', '00-arvore-inicial.png', 'Tela do Plano de Contas com a barra de ações (Novo, Filtros, Atualizar) e a visão em Árvore.'),
 ('h2', 'Duas formas de visualizar: Árvore ou Lista'),
 ('p',
  'A tela abre no modo Árvore, que agrupa as contas em três grupos fixos — 1 - RECEITAS, 2 - DESPESAS e 3 - '
  'OUTROS — e permite até 2 níveis dentro de cada grupo (uma conta "pai" e suas contas "filhas"). O botão '
  'Lista, no canto superior direito, troca para uma tabela simples com todas as contas cadastradas, sem a '
  'hierarquia visual.'),
 ('img',
  '01-lista.png',
  'A mesma informação na visão em Lista, com colunas Código, Descrição, Tipo, Pai e Ativo.'),
 ('h2', 'Cadastrando uma nova conta (exemplo)'),
 ('p',
  'Clique em Novo. No exemplo abaixo, criamos a conta "MATERIAL DE ESCRITORIO" como uma conta filha de "2 - '
  'Despesas" — ou seja, ela aparece dentro do grupo de despesas, como mais uma categoria de gasto.'),
 ('img',
  '02-novo-modal-preenchido.png',
  'Cadastro de uma nova conta: Tipo = Despesa, Código gerado automaticamente (2.11), Descrição preenchida e '
  'Pai = "2 - Despesas".'),
 ('tabela',
  [('Tipo',
    'D (Despesa) ou R (Receita) — define se a conta vai aparecer no grupo de Receitas ou de Despesas.',
    'Obrigatório; validado em PlanoContaController.cs (Criar/Alterar)'),
   ('Código',
    'Gerado automaticamente pelo sistema ao criar uma conta nova (não é digitado) — segue a numeração do '
    'grupo/conta pai.',
    'PlanoContaController.cs'),
   ('Descrição',
    'Nome da categoria, como vai aparecer em todos os relatórios e telas financeiras (ex.: "Aluguel", '
    '"Consulta por Convênio").',
    'Obrigatório; máx. 100 caracteres'),
   ('Plano de Conta Pai',
    'Opcional. Se preenchido, a nova conta vira uma "conta filha" da selecionada — usado para detalhar uma '
    'categoria maior. Sistema permite no máximo 2 níveis.',
    'PlanoContaController.cs'),
   ('Ativo',
    'Contas inativas continuam existindo (para não quebrar lançamentos antigos), mas somem das listas de '
    'seleção ao lançar novas contas a pagar/receber.',
    'PlanoContaController.cs')]),
 ('img',
  '03-apos-salvar.png',
  'Depois de salvar, a nova conta "MATERIAL DE ESCRITORIO" (2.11) já aparece na árvore, dentro do grupo '
  'Despesas.'),
 ('h2', 'Filtrando contas cadastradas'),
 ('p',
  'O botão Filtros abre uma busca por Código, Descrição, Tipo, conta Pai ou Situação (Ativo/Inativo), útil '
  'quando o plano de contas cresce e fica mais difícil de navegar olhando a árvore inteira.'),
 ('img', '04-filtro-preenchido.png', 'Filtro por Descrição contendo "MATERIAL".'),
 ('img', '05-resultado-filtro.png', 'Resultado: só as contas que batem com o filtro aparecem na lista.'),
 ('h2', 'Atalho: Importar Plano de Contas Padrão'),
 ('p',
  'Quando não existe nenhuma conta cadastrada ainda, a tela mostra um botão "Importar Plano de Contas '
  'Padrão", que cria de uma vez uma lista pronta de contas comuns para clínicas (Consulta Particular, '
  'Consulta por Convênio, Aluguel, Energia Elétrica, Folha de Pagamento, etc.) — um bom ponto de partida '
  'para não precisar cadastrar tudo manualmente.'),
 ('aviso',
  'Este cadastro não gera Conta a Pagar nem Conta a Receber por si só — ele só define as categorias que '
  'serão usadas quando essas contas forem lançadas em outras telas do sistema (Contas a Pagar, Contas a '
  'Receber, Contas Recorrentes, Checkin, Contrato).')]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Plano_de_Contas.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Plano_de_Contas_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Plano_de_Contas.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
