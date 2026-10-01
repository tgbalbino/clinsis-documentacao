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

VERSAO = '1.2'
DATA = '29/09/2026'
TITULO = 'Contas a Pagar'
SUBTITULO = 'Cadastrar e pagar as contas da clínica, com indicadores de vencimento'
VIDEO_NOME = "https://youtu.be/LIRC0NJ6Z3c"
INTRO = 'Contas a Pagar é onde ficam todas as despesas da clínica: as lançadas manualmente aqui e também as que chegam automaticamente de outras rotinas, como Contas Recorrentes e Pagamento de Profissionais. A partir dela dá pra acompanhar o que está em aberto, vencido, vencendo hoje ou a vencer, e lançar os pagamentos (baixas) de cada conta. Assim como as demais telas financeiras, exige Plano de Conta e Centro de Custo já cadastrados.'
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [('h2', 'Barra de ações'),
 ('p', 'Abaixo dos indicadores fica a barra de ações: o botão azul <b>Novo</b> (em destaque), o botão <b>Filtros</b> — que mostra um número quando há filtro aplicado, com um <b>✕</b> ao lado para limpar tudo — o botão <b>Filtro rápido</b> (veja abaixo) e o botão de <b>Atualizar</b>, só com o ícone. A lista mostra <b>30 registros por página</b>; use a paginação no canto direito para ver os demais. Só a lista rola; os indicadores e a barra ficam sempre visíveis. Esta tela só aparece no menu quando o módulo de Contas a Pagar está habilitado para a clínica.'),
 ('h2', 'Indicadores do topo'),
 ('p',
  'Cinco caixas resumem a situação das contas: Em Aberto (soma de tudo que ainda não foi pago), Vencido (em '
  'aberto com vencimento no passado), Vence Hoje, A Vencer (em aberto com vencimento futuro) e Pago no Mês '
  '(soma do que já foi baixado no mês atual).'),
 ('img', '00-lista-inicial.png', 'Tela inicial de Contas a Pagar, com indicadores e a lista de contas.'),
 ('h2', 'Filtro rápido'),
 ('p', 'Ao lado do botão Filtros, o botão <b>Filtro rápido</b> (atalho: tecla <b>F2</b>) abre uma janelinha para filtrar a lista pelo <b>nome da pessoa</b> (parte do nome) e/ou pelo <b>valor</b> — o sistema considera o valor original ou o saldo restante. Ele vale junto com os filtros da tela, mostra um contador quando está ativo e tem um ✕ para limpá-lo. Na janela, Enter aplica e o botão Limpar remove o filtro.'),
 ('img', '00b-filtro-rapido.png', 'Janela do Filtro rápido: nome da pessoa e valor.'),
 ('h2', 'Cadastrando uma conta a pagar (exemplo)'),
 ('p',
  'Clique em Novo. No exemplo abaixo, lançamos uma compra de material de escritório de R$ 350,00, tipo '
  'documento Boleto, vencendo hoje.'),
 ('img',
  '01-novo-modal-preenchido.png',
  'Cadastro de exemplo: Favorecido, Plano de Contas, Centro de Custo, Descrição, Valor e datas preenchidos.'),
 ('tabela',
  [('Favorecido (Pessoa)',
    'Para quem a clínica está pagando (fornecedor, prestador, profissional).',
    'Obrigatório'),
   ('Plano de Contas',
    'Categoria da despesa (ex.: Material de Consumo). Precisa estar cadastrado antes.',
    'Obrigatório'),
   ('Centro de Custo',
    'Setor da clínica responsável pela despesa. Precisa estar cadastrado antes.',
    'Obrigatório'),
   ('Valor Original', 'Valor total da conta antes de qualquer pagamento parcial.', 'Obrigatório'),
   ('Tipo Documento',
    'Boleto, Nota Fiscal, Contrato ou Pag. Profissional — este último é o tipo usado quando a conta vem da '
    'rotina de Pagamento de Profissionais.',
    'Obrigatório'),
   ('Competência (MM/AAAA)',
    'Mês/ano de referência da despesa (pode ser diferente do mês do vencimento).',
    'Obrigatório'),
   ('Data Vencimento', 'Data limite para pagamento sem juros/atraso.', 'Obrigatório')]),
 ('img', '02-apos-salvar.png', 'Depois de salvar, a nova conta aparece na lista, com Situação "1 - Aberto".'),
 ('h2', 'Pagando (baixando) uma conta'),
 ('p',
  'O botão verde com o cifrão ($), na linha da conta, abre a tela de Pagamento / Acerto. É possível lançar '
  'mais de um pagamento para a mesma conta (pagamentos parciais) até o saldo chegar a zero.'),
 ('img',
  '03-pagamento-preenchido.png',
  'Pagamento preenchido: Valor Pago, Forma de Pagamento (Cartão de Crédito) e Conta Financeira (Banco '
  'Brasil).'),
 ('img',
  '04-apos-lancar-pagamento.png',
  'Depois de clicar em Lançar: o pagamento aparece na tabela "Acertos / Pagamentos da Conta", com opção de '
  'ver Detalhes ou Cancelar o acerto.'),
 ('tabela',
  [('Valor Pago', 'Quanto está sendo pago nesse acerto.', 'ContaPagarBaixaController.cs'),
   ('Juros Pago',
    'Juros cobrados por atraso, se houver, somados ao valor pago.',
    'ContaPagarBaixaController.cs'),
   ('Desconto', 'Só é aceito quando o pagamento quita a conta inteira.', 'ContaPagarBaixaController.cs'),
   ('Forma Pagamento', 'Dinheiro, Cartão, PIX, etc.', 'Obrigatório'),
   ('Conta Financeira',
    'De qual conta bancária/caixa o dinheiro realmente saiu — usada para conferir o extrato e alimentar o '
    'Fluxo de Caixa.',
    'Obrigatório')]),
 ('aviso',
  'Contas a Pagar é o destino de lançamentos automáticos vindos de outras rotinas: Contas Recorrentes '
  '(despesas que se repetem) e Pagamento de Profissionais (repasse calculado a partir dos atendimentos do '
  'mês) — ambas criam a conta aqui sozinhas, sem o usuário precisar cadastrar manualmente.')]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_a_Pagar.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_a_Pagar_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_a_Pagar.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
