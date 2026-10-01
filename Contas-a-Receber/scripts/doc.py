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
TITULO = 'Contas a Receber'
SUBTITULO = 'Cadastrar e receber os valores que os pacientes/convênios devem à clínica'
VIDEO_NOME = "https://youtu.be/PFpYbTqKvFM"
INTRO = 'Contas a Receber reúne tudo que a clínica tem a receber: lançamentos manuais feitos aqui (em uma ou várias parcelas) e também os que chegam automaticamente de outras rotinas, como Checkin (quando há pagamento na hora), fechamento de Contrato e Cobrança de Paciente. A partir dela dá pra acompanhar o que está em aberto, vencido, vencendo hoje ou a vencer, e lançar os recebimentos (baixas). Também exige Plano de Conta e Centro de Custo já cadastrados.'
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [('h2', 'Barra de ações'),
 ('p', 'A barra de ações traz, nesta ordem, o botão azul Novo (em destaque), o botão Filtros — com contador de filtros aplicados e um ✕ para limpar tudo —, o botão de Atualizar, só com o ícone, e o botão Exportar. Só a lista rola; os indicadores e a barra ficam sempre visíveis.'),
 ('p', '**Filtro rápido:** ao lado de Filtros, o botão Filtro rápido (atalho: tecla F2) abre uma janelinha para filtrar a lista pelo nome da pessoa (parte do nome) e/ou pelo valor — o sistema considera o valor original ou o saldo restante. Ele vale junto com os filtros da tela, mostra um contador quando está ativo e tem um ✕ para limpá-lo. Na janela, Enter aplica e o botão Limpar remove o filtro.'),
 ('h2', 'Indicadores e como abrir a lista'),
 ('p', 'As mesmas cinco caixas de resumo de Contas a Pagar aparecem aqui: Em Aberto, Vencido, Vence Hoje, A Vencer e Recebido no Mês. Diferente de Contas a Pagar, a lista começa vazia — é preciso clicar em Filtros e depois em Buscar para carregar os lançamentos (dá pra buscar por paciente, situação, plano de conta, centro de custo, competência, entre outros).'),
 ('img', '00-lista-inicial.png', 'Tela inicial: indicadores e lista vazia, aguardando um filtro.'),
 ('img', '01-filtros.png', 'Janela de Filtros: é preciso informar um paciente ou escolher uma das opções de "+ Filtros" (como o N° do documento) antes de clicar em Buscar; sem isso a tela avisa "Selecione ao menos 1 filtro".'),
 ('img', '02-resultado-busca.png', 'Resultado da busca por paciente: as parcelas aparecem com a coluna "Origem" (preenchida quando o título veio de um Contrato) e o total no rodapé.'),
 ('h2', 'Filtro rápido'),
 ('p', 'Ao lado do botão Filtros, o botão <b>Filtro rápido</b> (atalho: tecla F2) abre uma janelinha para filtrar a lista pelo nome da pessoa (parte do nome) e/ou pelo valor — o sistema considera o valor original ou o saldo restante. Ele vale junto com os filtros da tela, mostra um contador quando está ativo e tem um ✕ para limpá-lo. Na janela, Enter aplica e o botão Limpar remove o filtro.'),
 ('img', '03-filtro-rapido.png', 'Janela do Filtro rápido: nome da pessoa e valor.'),
 ('h2', 'Cadastrando um recebimento — "Parcela Automática" (exemplo)'),
 ('p', 'O botão Novo abre um assistente de parcelas automáticas: você escolhe o paciente, o Plano de Contas e o Centro de Custo uma vez, informa quantas parcelas quer (e o valor de cada uma, ou o valor total dividido), e o sistema calcula as datas de vencimento de cada parcela automaticamente a partir de uma data-base. No exemplo, geramos 2 parcelas de R$ 150,00 para o paciente Paciente 0007.'),
 ('img', '04-parcela-preenchida.png', 'Dados preenchidos antes de gerar: paciente, plano, centro de custo, 2 parcelas de R$ 150,00 a partir de hoje.'),
 ('img', '05-preview-parcelas.png', 'Depois de clicar em "Gerar Parcelas": uma prévia mostra as 2 parcelas com suas datas de vencimento (hoje e daqui a 1 mês) antes de confirmar.'),
 ('tabela', [('Paciente', 'Para quem é o recebimento (quem deve o valor à clínica).', 'Obrigatório'),
 ('Plano de Contas / Centro de Custo', 'Mesma categoria/setor para todas as parcelas geradas.', 'Obrigatório; precisam existir antes'),
 ('Qtd Parcelas', 'Em quantas vezes o valor será dividido.', 'ContaReceberController.cs'),
 ('Data de Vencimento Base', 'Vencimento da primeira parcela (o dia do mês não pode ser maior que 24); as seguintes são geradas a partir dela (normalmente +1 mês por parcela).', 'ContaReceberController.cs'),
 ('Tipo Valor', '"Valor por parcela" (cada uma vale o valor informado) ou "Valor Total" (o valor informado é dividido pelas parcelas).', 'Obrigatório')]),
 ('img', '06-apos-confirmar.png', 'Depois de "Confirmar e Salvar Parcelas": mensagem de sucesso e as parcelas já lançadas.'),
 ('h2', 'Recebendo (baixando) uma parcela'),
 ('p', 'O botão verde com o cifrão ($), na linha da conta, abre a tela de Acertos / Recebimentos — mesmo padrão da baixa de Contas a Pagar. Ao lançar um pagamento que quita o valor, o sistema pede confirmação e explica que a parcela vai virar "Baixada". Quando o título veio de um Contrato, a forma de pagamento (e as parcelas do cartão) combinadas no acerto já vêm sugeridas, mas você pode trocar conforme o paciente realmente pagou.'),
 ('img', '09-baixa-preenchida.png', 'Recebimento preenchido: Valor, Método de Pagamento (Cartão de Crédito, com a escolha de Qtd. Parcelas) e Conta Financeira.'),
 ('img', '09b-confirmacao.png', 'Confirmação ao lançar o pagamento que quita a parcela: ao clicar em Sim, a situação passa a Baixada.'),
 ('img', '10-apos-lancar-baixa.png', 'Depois de confirmar: mensagem "Salvo", Valor Restante zerado, e opção de Emitir Recibo para o paciente.'),
 ('aviso', 'Contas a Receber é o destino de lançamentos automáticos de outras rotinas: Checkin (quando há pagamento na hora, já gera a conta baixada), fechamento de Contrato (um título para cada acerto à vista ou no cartão e uma parcela por mês para cada acerto em Crediário) e Cobrança de Paciente (geração em lote a partir de sessões realizadas). O filtro "Analítica" na tela de Filtros permite inclusive separar o que foi lançado manualmente do que veio do Checkin ou da Cobrança de Paciente. Os títulos gerados por um Contrato trazem a coluna "Origem" na lista (por exemplo, "Contrato 12 - Crediário 2/5" ou "Contrato 12 - Pix"), e a mesma informação aparece na tela de baixa.')]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_a_Receber.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_a_Receber_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Contas_a_Receber.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
