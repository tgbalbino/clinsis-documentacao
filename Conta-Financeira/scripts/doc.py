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
TITULO = "Cadastro de Conta Financeira"
SUBTITULO = "O que é, onde é usada e a validação Conta Financeira x Forma de Pagamento"
VIDEO_NOME = "video-conta-financeira-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('A <b>Conta Financeira</b> é o "cofre" onde o dinheiro da clínica realmente entra e sai: '
         'uma conta bancária (Banco do Brasil, Sicoob, etc.) ou o próprio caixa em dinheiro. '
         'Toda baixa (recebimento ou pagamento) informa em qual conta o valor caiu ou de qual conta '
         'ele saiu — é isso que permite conferir o extrato do banco, saber o saldo de cada conta e '
         'montar o Fluxo de Caixa. Este manual explica o cadastro, onde ele é usado e, principalmente, '
         'a regra que <b>amarra cada Conta Financeira às Formas de Pagamento permitidas nela</b>.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'O que é e para que serve'),
    ('p', 'Cada Conta Financeira representa <b>um lugar onde existe saldo</b>. Exemplos: "BANCO BRASIL" '
          '(conta corrente da clínica), "SICOOB CONTA CORRENTE" ou "CAIXA" (o dinheiro em espécie na '
          'recepção). Sem Conta Financeira o sistema não sabe <b>onde</b> o dinheiro foi parar, e por '
          'isso ela é obrigatória em toda baixa de Conta a Pagar e de Conta a Receber, e também na baixa automática do Checkin.'),
    ('p', 'O cadastro fica em <b>Financeiro → Cadastros → Contas Financeiras</b> (acesso do administrador).'),
    ('img', '00-lista-contas-financeiras.png',
     'Lista de Contas Financeiras. A coluna "Tipo" mostra "Banco" quando a conta tem dados bancários '
     'e "Caixa" quando é uma conta sem banco (dinheiro em espécie).'),

    ('h2', 'Cadastrando uma conta nova'),
    ('p', 'Clique em <b>Novo</b> e preencha. Só a <b>Descrição</b> é obrigatória; os demais campos '
          'são opcionais e servem para identificar a conta bancária.'),
    ('img', '10-novo-cadastro-completo.png',
     'Modal "Nova Conta Financeira" preenchido como conta bancária (Banco do Brasil, agência 0001, '
     'conta 12345-6 e chave PIX).'),
    ('tabela', [
        ('Descrição *', 'Nome que aparece em todas as telas de baixa, movimentos e fluxo de caixa. Sempre gravado em maiúsculas.', 'ContaFinanceira.Descricao'),
        ('Banco', 'Banco da conta (lista de bancos cadastrados). Deixe em branco para uma conta do tipo Caixa.', 'ContaFinanceira.IdBanco'),
        ('Agência', 'Agência bancária (até 20 caracteres).', 'ContaFinanceira.Agencia'),
        ('Conta', 'Número da conta (até 30 caracteres).', 'ContaFinanceira.Conta'),
        ('Chave PIX', 'Chave PIX da conta, só para consulta/identificação.', 'ContaFinanceira.ChavePix'),
        ('Ativo (só ao editar)', 'Conta inativa deixa de ser oferecida nas telas de baixa (só contas ativas aparecem na lista), mas o histórico é mantido.', 'ContaFinanceira.Ativo'),
        ('Tipo (badge Banco/Caixa)', 'Não é um campo: aparece como "Banco" se Banco/Agência/Conta estiverem preenchidos e como "Caixa" caso contrário.', 'Calculado na tela (conta-financeira-painel)'),
    ]),
    ('img', '11-lista-com-conta-nova.png', 'Conta "SICOOB CONTA CORRENTE" salva e já listada, com o tipo "Banco".'),
    ('img', '13-editar-conta.png', 'Ao editar, aparece também o campo "Ativo" (Ativo/Inativo).'),
    ('aviso', 'Uma conta <b>Inativa</b> é a forma correta de "aposentar" uma conta que já teve movimento: '
              'ela some das telas de baixa, mas o histórico de movimentos continua íntegro.'),

    ('h2', 'Onde a Conta Financeira é usada'),
    ('tabela', [
        ('Contas a Pagar — baixa', 'Campo <b>Conta Financeira (obrigatório)</b>: de qual conta o dinheiro saiu. Gera um movimento de Saída na conta.', 'ContaPagarBaixaRepository.cs'),
        ('Contas a Receber — baixa', 'Campo <b>Conta Financeira (obrigatório na tela: "Informe a conta financeira")</b>: em qual conta o dinheiro entrou. Gera um movimento de Entrada na conta.', 'ContaReceberBaixaRepository.cs'),
        ('Checkin de Paciente', 'A baixa automática do pagamento feito no Checkin usa a conta definida no parâmetro <b>IdContaFinanceiraCheckin</b>.', 'CheckinRepository.cs / Parametro'),
        ('Movimentos Financeiros', 'Extrato de todas as entradas/saídas, com filtro por conta. Também permite <b>Nova Transferência</b> entre duas contas.', 'MovimentoFinanceiro'),
        ('Fluxo de Caixa e Dashboard', 'Saldo, entradas e saídas por conta (quadro "Por Conta Financeira").', 'MovimentoFinanceiro'),
    ]),
    ('img', '22-movimentos-filtrado-caixa.png',
     'Movimentos Financeiros filtrado pela conta "CAIXA": só aparecem os lançamentos que passaram por ela '
     '(uma entrada de Conta a Receber e uma saída de Conta a Pagar).'),
    ('img', '21-fluxo-caixa.png',
     'Fluxo de Caixa: o quadro "Por Conta Financeira" (no rodapé) mostra entradas, saídas e resultado de '
     'cada conta cadastrada.'),

    ('h2', 'Validação Conta Financeira x Forma de Pagamento'),
    ('p', 'Nem toda forma de pagamento faz sentido em toda conta. Uma máquina de cartão, por exemplo, '
          'deposita na conta bancária — não existe "Cartão de Crédito" dentro da gaveta de dinheiro do '
          'caixa. Por isso cada Conta Financeira tem a sua própria lista de <b>Formas de Pagamento '
          'permitidas</b>, e o sistema <b>recusa</b> qualquer baixa que combine uma forma com uma conta '
          'em que ela não foi habilitada.'),
    ('p', 'Essa regra vale em <b>três lugares</b>: baixa de Conta a Receber, baixa de Conta a Pagar e '
          'pagamento do Checkin.'),

    ('h2', 'Como configurar (passo a passo)'),
    ('p', '<b>Passo 1 — Formas de pagamento da clínica.</b> Em <b>Tabelas Aux. → Formas de Pagamento</b> '
          'ficam as formas com as quais a clínica trabalha (Cartão de Crédito, Débito, Cheque, Dinheiro, Pix). '
          'Só as formas <b>ativas</b> aqui são oferecidas nas telas de baixa e servem de sugestão inicial '
          'para as contas novas.'),
    ('img', '23-formas-pagamento-clinica.png',
     'Formas de Pagamento da clínica: neste exemplo Cartão de Crédito, Dinheiro e Pix estão ativos; '
     'Cartão de Débito e Cheque estão desativados.'),
    ('p', '<b>Passo 2 — Formas permitidas em cada conta.</b> Na lista de Contas Financeiras, clique no '
          'botão azul <b>"Formas de pagamento desta conta"</b> (ícone de cheque) da linha desejada. '
          'Cada forma tem um botão: <b>Desabilitar</b> (vermelho) quando está permitida e '
          '<b>Habilitar</b> (verde) quando não está.'),
    ('img', '12-formas-conta-nova.png',
     'Formas de pagamento da conta nova "SICOOB": ao criar uma conta, o sistema já habilita todas as '
     'formas que estão ativas na clínica (Crédito, Dinheiro e Pix). Basta desabilitar as que não se aplicam.'),
    ('img', '02-formas-pagamento-antes.png', 'Conta "CAIXA" com Cartão de Crédito, Dinheiro e Pix habilitados.'),
    ('img', '03-formas-pagamento-depois.png',
     'Depois de clicar em "Desabilitar" no Cartão de Crédito: a conta CAIXA passa a aceitar só Dinheiro e Pix.'),
    ('aviso', 'Ao <b>criar</b> uma conta, o sistema já a deixa com todas as formas ativas da clínica '
              'habilitadas — é uma sugestão inicial. Confira sempre a lista e desabilite o que não se '
              'aplica àquela conta (ex.: cartão em uma conta "Caixa").'),

    ('h2', 'Exemplo prático: o que acontece na tela'),
    ('p', '<b>Exemplo 1 — Combinação não permitida (Conta a Receber).</b> Com a conta CAIXA aceitando '
          'apenas Dinheiro e Pix, tentamos receber R$ 1,00 escolhendo <b>Método Pagto = Cartão de '
          'Crédito</b> e <b>Conta Financeira = CAIXA</b>. O sistema recusa e mostra a orientação de '
          'como resolver.'),
    ('img', '05-erro-forma-nao-habilitada.png',
     'Baixa recusada: "Esta forma de pagamento não está habilitada para a conta financeira selecionada. '
     'Configure essa relação na tela de Conta Financeira."'),
    ('p', '<b>Exemplo 2 — Combinação permitida.</b> Trocando o método para <b>Dinheiro</b> (que a conta '
          'CAIXA aceita), a baixa é gravada normalmente e passa a aparecer no extrato da conta.'),
    ('img', '07-baixa-com-sucesso.png',
     'Baixa de R$ 1,00 em Dinheiro na conta CAIXA gravada com sucesso (aviso "Salvo" e a nova linha '
     'na lista de acertos).'),
    ('p', '<b>Exemplo 3 — Mesma regra em Contas a Pagar.</b> A baixa de uma Conta a Pagar com Cartão de '
          'Crédito saindo do CAIXA é recusada com a mesma mensagem. Aqui a Conta Financeira é obrigatória '
          '(asterisco vermelho no campo). Em Contas a Receber a tela também exige a conta, mesmo sem o asterisco.'),
    ('img', '26-contapagar-erro-forma-nao-habilitada.png',
     'Conta a Pagar: Cartão de Crédito na conta CAIXA recusado com a mensagem de forma não habilitada.'),
    ('aviso', '<b>Se aparecer essa mensagem no dia a dia</b>, há duas saídas: escolher outra Conta '
              'Financeira que aceite aquela forma (ex.: a conta bancária, para cartão) ou habilitar a '
              'forma na conta desejada pelo botão "Formas de pagamento desta conta".'),
    ('tabela', [
        ('Regra de validação', 'Ao gravar a baixa, o sistema consulta se existe o par (Conta Financeira, Forma de Pagamento) habilitado. Se não existir, recusa e não grava nada.', 'ContaFinanceiraPagamentoForma'),
        ('Onde é conferida', 'Baixa de Conta a Receber, baixa de Conta a Pagar e pagamento do Checkin (que usa a conta do parâmetro IdContaFinanceiraCheckin).', 'ContaReceberBaixaRepository.cs / ContaPagarBaixaRepository.cs / CheckinRepository.cs'),
    ]),

    ('h2', 'Conta Financeira do Checkin'),
    ('p', 'O pagamento feito no Checkin do paciente gera uma Conta a Receber e sua baixa automática. '
          'Como não existe um campo para o recepcionista escolher a conta, o sistema usa a definida no '
          'parâmetro <b>IdContaFinanceiraCheckin</b> (<b>Tabelas Aux. → Parâmetros</b>). '
          'A forma de pagamento escolhida no Checkin também é validada contra essa conta.'),
    ('img', '24-parametro-conta-financeira-checkin.png',
     'Tela de Parâmetros: a linha "Conta financeira usada na baixa automática do ContaReceber gerado '
     'pelo Checkin" aponta para "BANCO BRASIL".'),
    ('aviso', 'Se a conta configurada nesse parâmetro <b>não aceitar</b> a forma de pagamento escolhida '
              'no Checkin (por exemplo, o parâmetro apontando para o CAIXA e o paciente pagando no '
              'cartão), o Checkin é recusado com uma mensagem indicando o parâmetro e a tela de Conta '
              'Financeira para ajuste. Por isso, aponte o parâmetro para uma conta que aceite todas as '
              'formas usadas na recepção.'),

    ('h2', 'Excluir uma conta financeira'),
    ('p', 'O botão vermelho (lixeira) exclui a conta — <b>desde que ela nunca tenha sido usada</b>. Uma '
          'conta com movimentos financeiros não pode ser excluída, para não perder o histórico. O '
          'sistema explica o motivo e sugere o caminho correto: alterar o cadastro para Inativo.'),
    ('img', '15-resultado-exclusao-caixa.png',
     'Tentativa de excluir a conta CAIXA (que já tem movimentos): o sistema recusa e orienta a usar o status Inativo.'),
    ('img', '17-exclusao-conta-sem-movimentos-ok.png',
     'Conta "SICOOB" (criada agora, sem nenhum movimento) excluída com sucesso ("Removido!").'),
    ('aviso', 'Também não é possível excluir a conta que estiver configurada no parâmetro '
              '<b>IdContaFinanceiraCheckin</b>: primeiro troque o parâmetro para outra conta.'),

    ('h2', 'Atenção: usuários com "Controla Caixa"'),
    ('p', 'Se o usuário logado tem a opção <b>Controla Caixa</b> marcada no cadastro de acesso, '
          'qualquer baixa de Conta a Receber/Pagar exige que ele tenha o <b>caixa aberto</b> '
          '(Caixa → Meu caixa). Sem o caixa aberto, a baixa é recusada com mensagem específica — '
          'independentemente da Conta Financeira escolhida. Veja o manual do <b>Módulo de Caixa</b>.'),
    ('img', '09-erro-caixa-fechado.png',
     'Baixa recusada porque o usuário controla caixa e não há caixa aberto: "Nenhum caixa aberto para o '
     'usuário. Abra o caixa antes de registrar o recebimento."'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Conta_Financeira.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Conta_Financeira_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Conta_Financeira.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
