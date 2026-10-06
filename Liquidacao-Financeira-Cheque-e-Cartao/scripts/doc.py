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
DATA = '06/10/2026'
NOME = 'Controle_de_Cheques_e_Liquidacao'
TITULO = "Controle de Cheques e Liquidação Financeira"
SUBTITULO = "Cheque e cartão: o dinheiro só entra na conta quando é compensado ou repassado"
VIDEO_NOME = "video-controle-de-cheques-liquidacao-com-legenda.mp4"
INTRO = ('Quando o paciente paga com <b>cheque</b> ou com <b>cartão de crédito</b>, o título é quitado na hora, '
         'mas o dinheiro só chega à conta da clínica dias depois. Este manual mostra como o ClinSis controla esse '
         'intervalo: cada <b>cheque</b> é cadastrado com seus dados (banco, agência, conta, série, número e emitente), '
         'pode pagar mais de um título, e a conta só é movimentada quando o cheque é <b>compensado</b>. '
         'No cartão, cada parcela repassada pelo banco é confirmada separadamente. Também explica a devolução do '
         'cheque com nova cobrança e o cheque emitido pela clínica nos pagamentos.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'A ideia: baixar o título não é o dinheiro entrar'),
    ('p', 'Com <b>dinheiro, PIX ou débito</b>, a baixa do título já lança o valor na conta financeira. Com '
          '<b>cheque</b> e <b>cartão de crédito</b> é diferente: o título é quitado na baixa, mas o saldo da conta '
          'só muda quando o banco de fato compensa o cheque ou repassa a parcela do cartão. Até lá, o valor aparece '
          'como <b>a receber</b> (ou a pagar), sem inflar o saldo da conta.'),
    ('p', 'Cada forma de pagamento escolhe o seu comportamento em <b>Tabelas Aux. → Formas de Pagamento</b>:'),
    ('tabelagen', ['Política', 'O que acontece na baixa', 'Exemplo'],
     [['Imediata', 'O valor entra na conta financeira na hora.', 'Dinheiro, PIX, débito'],
      ['Compensação manual', 'O título é quitado e o cheque fica em carteira até ser compensado na tela Cheques.', 'Cheque'],
      ['Repasse programado', 'O título é quitado e o banco repassa em parcelas, com prazo, intervalo e taxa do contrato.', 'Cartão de crédito']],
     [3.5, 10, 4]),
    ('img', '01-config-formas.png', 'Formas de Pagamento: a política de cada forma define se o dinheiro entra na hora ou depois.'),

    ('h2', 'Receber com cheque: cadastrando o cheque na baixa'),
    ('p', 'Na baixa de uma conta a receber, escolha a forma <b>Cheque</b>. Aparece o quadro <b>Cheque recebido</b>, com '
          'duas opções: <b>Cheque novo</b> (cadastra o cheque agora) ou <b>Cheque já cadastrado</b> (usa um cheque que '
          'já está em carteira). A conta financeira da baixa é o <b>caixa</b>, pois o cheque ainda não foi depositado.'),
    ('tabela', [
        ('Banco, Agência e Conta', 'Dados da conta do emitente, impressos no cheque. O banco vem da lista de bancos.', 'Cheque.IdBanco / Agencia / Conta'),
        ('Série e Nº do cheque', 'Identificação do cheque. A série é opcional.', 'Cheque.Serie / Numero'),
        ('Valor do cheque', 'Valor de face. Em branco vale o valor da baixa. Informe o total quando o mesmo cheque pagar mais de um título.', 'Cheque.Valor'),
        ('Emissão', 'Data em que o cheque foi emitido (opcional, não pode ser futura).', 'Cheque.DataEmissao'),
        ('Bom para', 'Data prevista de compensação (cheque pré-datado). É a previsão usada nas listas e no fluxo de caixa.', 'Cheque.BomPara'),
        ('CPF/CNPJ do emitente', 'Quem assinou o cheque. A pessoa precisa estar cadastrada: ao digitar o CPF/CNPJ o sistema mostra o nome ou oferece o link para cadastrar.', 'Cheque.IdPessoaEmitente'),
    ]),
    ('img', '02-baixa-cheque-novo.png', 'Baixa de R$ 450,00 com cheque novo de R$ 700,00: o emitente foi localizado pelo CPF.'),
    ('img', '03-baixa-cheque-confirmacao.png', 'Confirmação da baixa. A conta a receber fica quitada, mas nenhum valor entra na conta ainda.'),
    ('aviso', 'O valor do cheque não pode ser menor que o valor da baixa, e o "bom para" não pode ser anterior à data da baixa.'),

    ('h2', 'Um cheque pagando mais de um título'),
    ('p', 'O paciente pode pagar dois títulos com um único cheque. Na primeira baixa cadastre o cheque com o valor total '
          '(R$ 700,00 neste exemplo); na segunda, escolha <b>Cheque já cadastrado</b>. O saldo do cheque diminui a cada título.'),
    ('p', '<b>Como o sistema reconhece o mesmo cheque:</b> pela combinação de banco, agência, conta, série e número. '
          'Zeros à esquerda e pontuação são ignorados, então <i>000482</i> e <i>482</i> são o mesmo cheque. O mesmo número em '
          'outra conta ou série é outro cheque. Se você tentar cadastrar de novo um cheque que já existe, a tela avisa e '
          'oferece o botão <b>Usar este cheque</b>.'),
    ('img', '04-cheque-duplicado.png', 'O cheque 482 foi digitado de novo: a tela reconhece o cheque 000482 já cadastrado e oferece usá-lo.'),
    ('img', '05-cheque-da-carteira.png', 'Cheque já cadastrado selecionado, com o saldo disponível: R$ 250,00 abatidos dos R$ 700,00.'),

    ('h2', 'A tela Cheques'),
    ('p', 'Acesso em <b>Financeiro → Movimentos → Cheques</b>. Reúne todos os cheques recebidos e emitidos, com o valor, '
          'o saldo ainda sem título, a quantidade de títulos e o "bom para". Cheques vencidos aparecem em vermelho.'),
    ('img', '06-lista-cheques.png', 'Lista de cheques em carteira: o cheque 000482 de R$ 700,00 paga 2 títulos e não tem saldo.'),
    ('tabelagen', ['Filtro', 'Para que serve'],
     [['Situação', 'Em carteira, Compensado, Devolvido ou Cancelado.'],
      ['Tipo', 'Cheques recebidos dos pacientes ou emitidos pela clínica.'],
      ['Número', 'Procura pelo número ignorando zeros à esquerda.'],
      ['Banco e Emitente', 'Por banco ou por nome/CPF/CNPJ de quem assinou.'],
      ['Bom para (período)', 'Cheques previstos para compensar em um intervalo.'],
      ['Somente vencidos', 'Cheques em carteira cujo "bom para" já passou.'],
      ['Com saldo a vincular', 'Cheques que ainda cabem em novos títulos.']],
     [4.5, 13]),
    ('tabelagen', ['Situação', 'Significado'],
     [['Em carteira', 'Cadastrado e aguardando compensação. Aceita novos títulos enquanto tiver saldo.'],
      ['Compensado', 'O banco compensou: o valor foi lançado na conta financeira.'],
      ['Devolvido', 'O banco devolveu (sem fundos, por exemplo). Os títulos continuam quitados.'],
      ['Cancelado', 'Cheque lançado por engano, sem títulos. A mesma numeração pode ser cadastrada de novo.']],
     [4, 13.5]),
    ('p', 'O botão <b>Ver</b> abre o detalhe do cheque com os títulos pagos por ele.'),
    ('img', '07-detalhe-cheque.png', 'Detalhe do cheque: os dois títulos pagos, com paciente, valor e situação.'),

    ('h2', 'Liquidações Financeiras e o cheque'),
    ('p', 'A tela <b>Liquidações Financeiras</b> lista tudo o que está aguardando entrar ou sair da conta: cheques e '
          'parcelas de cartão. Para as linhas de cheque aparece o botão <b>Ver cheque</b> no lugar de liquidar, devolver '
          'e cancelar: <b>o cheque é compensado, devolvido e cancelado pela tela Cheques</b>, de uma só vez para todos os '
          'títulos, gerando um único movimento no extrato mesmo quando paga vários títulos. Dá para procurar um cheque '
          'pelo número ou pela pessoa.'),
    ('img', '08-liquidacoes-cheque.png', 'Liquidações: as duas linhas do cheque mostram o número, a pessoa e "Ver cheque".'),

    ('h2', 'Compensar o cheque'),
    ('p', 'Quando o banco compensar, clique em <b>Compensar</b>. Informe a <b>data da compensação</b> e a <b>conta do depósito</b> '
          '(onde o cheque foi depositado). O cheque só pode ser compensado quando <b>todo o seu valor estiver vinculado a '
          'títulos</b>; se sobrar saldo, vincule o restante em outra baixa ou ajuste o valor do cheque.'),
    ('img', '09-compensar-cheque.png', 'Compensação do cheque de R$ 700,00 na conta Banco Brasil.'),
    ('img', '10-cheque-compensado.png', 'O cheque passa para Compensado.'),
    ('p', 'Em <b>Movimentos Financeiros</b> aparece <b>um único lançamento</b> de entrada, "Compensação de cheque", pelo valor '
          'total do cheque, pronto para a conciliação com o extrato do banco.'),
    ('img', '11-movimentos.png', 'Um único movimento de R$ 700,00 pela compensação do cheque, mesmo tendo pago dois títulos.'),

    ('h2', 'Devolução do cheque'),
    ('p', 'Se o banco devolver o cheque, use <b>Devolver</b> (em carteira ou já compensado). Informe a data e o motivo. '
          'Se o cheque já tinha sido compensado, o sistema cria um <b>movimento inverso</b> (estorno) e preserva o original. '
          'Os títulos pagos <b>continuam quitados</b>; para cobrar o paciente, o sistema pode gerar uma <b>nova cobrança por '
          'título</b>, com o vencimento escolhido e uma tarifa opcional (somada apenas à primeira cobrança).'),
    ('img', '12-devolver-cheque.png', 'Devolução com a prévia das cobranças: R$ 465,00 (450 + tarifa de 15) e R$ 250,00.'),
    ('img', '13-cheque-devolvido.png', 'O cheque devolvido. O estorno foi lançado uma única vez.'),
    ('img', '14-cobrancas-devolucao.png', 'As novas cobranças aparecem em Contas a Receber com a origem "Cobrança de devolução".'),
    ('aviso', 'A devolução vale para o cheque inteiro: não é possível devolver só um dos títulos. O cheque devolvido deixa de aceitar novos títulos.'),

    ('h2', 'Alterar e cancelar um cheque'),
    ('p', '<b>Alterar</b> muda o valor, a emissão, o "bom para" e a observação de um cheque em carteira; a identificação '
          '(banco, agência, conta, série e número) não muda. O valor não pode ficar abaixo do que já foi vinculado a títulos, '
          'e o novo "bom para" vale para todos os títulos do cheque.'),
    ('p', '<b>Cancelar</b> serve para um cheque lançado por engano e <b>sem nenhum título</b>. Se houver títulos, cancele '
          'antes as baixas deles. Cheque cancelado libera a mesma numeração para um novo cadastro.'),

    ('h2', 'Pagar com cheque emitido pela clínica'),
    ('p', 'Na baixa de uma conta a pagar com a forma <b>Cheque</b>, informe a <b>conta sacada</b> (a conta bancária da clínica '
          'contra a qual o cheque é emitido), a série, o número e o "bom para". Banco, agência e conta do cheque vêm da '
          'conta sacada. Assim como no recebimento, o mesmo cheque pode pagar mais de uma conta a pagar.'),
    ('img', '21-pagar-cheque-emitido.png', 'Pagamento do aluguel com cheque emitido contra a conta Banco Brasil.'),
    ('img', '22-lista-cheque-emitido.png', 'O cheque emitido aparece na tela Cheques como "Emitido", em carteira.'),
    ('img', '23-alterar-cheque.png', 'Alterar o cheque: valor, emissão, "bom para" e observação.'),
    ('p', 'Quando o cheque for descontado pelo fornecedor, use <b>Compensar</b>: o valor sai da <b>conta sacada</b> automaticamente, '
          'sem precisar escolher a conta.'),
    ('img', '24-compensar-cheque-emitido.png', 'Compensação do cheque emitido: a saída é lançada na conta sacada.'),
    ('aviso', 'Um cheque recebido de paciente ainda não pode ser repassado a fornecedor (endosso) nos pagamentos. '
              'Em pagamentos use apenas cheques emitidos pela clínica.'),

    ('h2', 'Cartão de crédito parcelado'),
    ('p', 'Na baixa com cartão de crédito, escolha a quantidade de parcelas. O aviso mostra como o banco vai repassar: '
          '<b>uma parcela por mês</b>, a primeira na previsão e as demais conforme o intervalo e a taxa do contrato da forma.'),
    ('img', '15-baixa-cartao.png', 'Baixa de R$ 900,00 no cartão em 3x: o aviso informa o repasse em 3 parcelas.'),
    ('img', '16-parcelas-repasse.png', 'Cada parcela é uma liquidação separada, com a previsão de repasse e a taxa prevista.'),
    ('p', 'Quando o banco repassar uma parcela, clique em <b>Liquidar</b> naquela linha. O sistema sugere o valor líquido '
          '(parcela menos a taxa prevista); confira com o que o banco creditou e ajuste se for diferente.'),
    ('img', '17-liquidar-parcela.png', 'Liquidação da parcela 1/3 com a taxa prevista pelo contrato.'),
    ('img', '18-parcela-liquidada.png', 'Parcela liquidada: o movimento de entrada é pelo valor líquido e indica a parcela.'),
    ('p', 'Cada parcela pode ser <b>devolvida</b> (chargeback) separadamente, gerando a nova cobrança só daquele valor.'),
    ('aviso', 'Não é possível cancelar a baixa de um título cujo cartão já teve parcela repassada, nem a de um cheque já '
              'compensado: o sistema bloqueia e explica o motivo.'),
    ('img', '20-cancelar-bloqueado.png', 'Tentativa de cancelar a baixa de um cartão com parcela já repassada: bloqueada.'),

    ('h2', 'Filtros e fluxo de caixa projetado'),
    ('p', 'A tela de Liquidações pode ser filtrada por situação, direção (entrada ou saída), período de previsão, conta '
          'financeira, número do cheque ou documento, pessoa e "somente vencidas". Os cartões no topo somam o que está a '
          'receber e a pagar, destacando o que já venceu.'),
    ('img', '25-filtros.png', 'Filtros por conta financeira e período de previsão.'),
    ('p', 'O <b>Fluxo de Caixa</b> passa a mostrar o previsto: os cheques e as parcelas de cartão entram na data prevista, '
          'separados do que já foi realizado.'),
    ('img', '26-fluxo-projetado.png', 'Fluxo de caixa com o previsto dos cheques e das parcelas de cartão.'),

    ('h2', 'Resumo das regras'),
    ('tabelagen', ['Situação', 'O que o sistema faz'],
     [['Baixa com cheque', 'Quita o título, cadastra (ou usa) o cheque e não mexe no saldo da conta.'],
      ['Cheque que paga vários títulos', 'O saldo do cheque diminui a cada título; a compensação só é liberada com o valor todo vinculado.'],
      ['Compensação', 'Um único movimento pelo valor do cheque, na conta do depósito (ou na conta sacada, no emitido).'],
      ['Devolução', 'Estorno único se já compensado; títulos continuam quitados; nova cobrança por título, se escolhida.'],
      ['Cheque duplicado', 'Mesmo banco, agência, conta, série e número (ignorando zeros) é o mesmo cheque: não cadastra de novo.'],
      ['Cancelar baixa', 'Cheque em carteira: cancela e reabre o saldo. Cheque compensado ou cartão repassado: bloqueado.'],
      ['Cartão', 'Uma liquidação por parcela, com taxa e prazo do contrato; liquidar e devolver por parcela.']],
     [4.5, 13]),
]

render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
