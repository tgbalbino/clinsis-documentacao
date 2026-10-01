# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.0'
DATA = '30/09/2026'
TITULO = 'Conciliação Bancária (OFX)'
SUBTITULO = 'Como conferir o extrato do banco com os Movimentos Financeiros do ClinSis usando o arquivo OFX'
VIDEO_NOME = "https://youtu.be/17EE36VWZHM"
INTRO = ('A <b>Conciliação Bancária (OFX)</b> confere o extrato do banco com os <b>Movimentos Financeiros</b> do ClinSis. '
         'Você baixa o extrato no internet banking em formato <b>OFX</b>, envia o arquivo ao sistema e ele mostra, linha por linha, '
         'o que já está lançado no ClinSis, o que só aparece no banco e o que só aparece no sistema. As linhas que batem podem ser '
         'conciliadas de uma só vez, sem digitar nada.')
RODAPE = ('Documento gerado por teste manual guiado em ambiente local de homologação, clínica de testes "Homologação" '
          '(Clínica 1), usuário administrador de teste. O extrato usado nos exemplos é fictício, criado só para esta documentação.')

blocks = [
    ('h2', 'Para que serve'),
    ('p', '<b>Conciliar</b> é confirmar que cada movimento registrado no sistema realmente apareceu no banco, com o mesmo valor. '
          'Isso evita diferenças no saldo, pagamentos lançados em duplicidade ou recebimentos que nunca caíram na conta. '
          'No ClinSis a conciliação é feita por <b>Conta Financeira</b>: você escolhe a conta, envia o extrato dela e confere.'),
    ('aviso', 'Só o perfil <b>Administrador</b> acessa esta tela. A leitura do arquivo <b>não grava nada</b>: os movimentos só são '
              'marcados como conciliados quando você clica em <b>Conciliar marcados</b>.'),

    ('h2', 'Onde fica no sistema'),
    ('p', 'Menu <b>Financeiro → Movimentos → Conciliação OFX</b>. O resultado da conciliação aparece em '
          '<b>Financeiro → Movimentos → Movimentos Financeiros</b>, na coluna <b>Conciliado</b>.'),
    ('img', '00-tela-inicial.png', 'Conciliação Bancária (OFX): escolha a conta financeira, o arquivo do extrato e clique em Ler extrato.'),

    ('h2', 'Antes de começar'),
    ('tabelagen', ['Item', 'O que conferir'], [
        ['Conta Financeira', 'A conta precisa estar cadastrada em Cadastros → Conta Financeira. Se possível, preencha banco, agência e conta: o sistema usa esses dados para avisar quando o arquivo é de outra conta.'],
        ['Arquivo OFX', 'No internet banking, procure por Extrato → Exportar (ou Salvar) e escolha o formato <b>OFX</b> (às vezes chamado de "Money" ou "Quicken"). Tamanho máximo: 2 MB.'],
        ['Lançamentos no sistema', 'Os pagamentos e recebimentos já devem estar registrados no ClinSis (baixas de Contas a Pagar e a Receber e transferências). A conciliação só liga o que já existe; ela não cria lançamentos.'],
    ], [4, 13.5]),
    ('p', 'O ClinSis tem leitura própria para Banco do Brasil, Santander, Sicredi e Sicoob. Arquivos de outros bancos usam a leitura padrão do formato OFX e costumam funcionar igual.'),
    ('img', '01-movimentos-antes.png', 'Movimentos Financeiros antes da conciliação: a coluna Conciliado mostra Sim ou Não para cada movimento.'),

    ('h2', 'Passo a passo'),
    ('tabelagen', ['Passo', 'O que fazer'], [
        ['1', 'Em <b>Conta Financeira</b>, escolha a conta do extrato.'],
        ['2', 'Em <b>Arquivo do extrato (.ofx)</b>, clique em <b>Choose File</b> (Escolher arquivo) e selecione o OFX baixado do banco.'],
        ['3', 'Clique em <b>Ler extrato</b>. O sistema mostra o banco, a agência, a conta, o período e o saldo final do arquivo, e compara cada linha com os movimentos da conta.'],
        ['4', 'Confira a lista (veja as situações abaixo). As linhas encontradas já vêm marcadas; desmarque as que não concordar.'],
        ['5', 'Clique em <b>Conciliar marcados</b>. O sistema confirma quantos movimentos foram conciliados e recarrega a lista.'],
    ], [2.2, 15.3]),
    ('img', '02-arquivo-escolhido.png', 'Conta e arquivo escolhidos, prontos para clicar em Ler extrato.'),
    ('img', '03-resultado.png', 'Resultado da leitura: cada linha do extrato com a situação e o movimento do sistema que combina com ela.'),

    ('h2', 'Como o sistema encontra o par'),
    ('p', 'Para cada linha do extrato, o ClinSis procura um movimento da mesma conta que ainda não esteja conciliado, seguindo estas regras:'),
    ('tabelagen', ['Regra', 'Detalhe'], [
        ['Mesmo tipo', 'Crédito do extrato com <b>Entrada</b> do sistema; débito com <b>Saída</b>.'],
        ['Mesmo valor', 'O valor precisa ser exatamente igual (em reais e centavos).'],
        ['Data próxima', 'A data do movimento pode diferir até <b>3 dias</b> da data do extrato (o banco costuma compensar depois do lançamento).'],
        ['Um para um', 'Cada movimento do sistema é usado uma única vez. Se houver vários candidatos, vale o de data mais próxima e, em empate, o de histórico mais parecido.'],
    ], [4, 13.5]),
    ('aviso', 'O sistema apenas <b>sugere</b>. Quem confirma é você. Antes de clicar em Conciliar marcados, olhe principalmente os valores repetidos (por exemplo, três recebimentos de R$ 150,00), pois o par sugerido pode não ser o que você imaginava.'),

    ('h2', 'As situações de cada linha'),
    ('tabelagen', ['Situação', 'Significado', 'O que fazer'], [
        ['Encontrado no sistema', 'Existe um movimento com mesmo tipo, valor e data próxima. A linha vem marcada.', 'Conferir e manter marcada para conciliar.'],
        ['Já conciliado', 'Essa linha do extrato já foi ligada a um movimento em outra conciliação.', 'Nada. Reenviar o mesmo arquivo é seguro: nada é conciliado duas vezes.'],
        ['Só no extrato', 'O banco registrou, mas não há movimento equivalente no sistema (por exemplo, uma tarifa ou um TED recebido que ninguém lançou).', 'Registrar o lançamento no ClinSis (por exemplo, dando baixa na conta a pagar ou a receber correspondente) e ler o extrato de novo.'],
        ['Só no sistema', 'Aparece na tabela "Movimentos do sistema sem lançamento no extrato": o movimento existe no período do arquivo, mas o banco não trouxe uma linha igual.', 'Verificar se o valor ou a data estão diferentes do banco, se ainda não compensou, ou se foi lançado na conta errada.'],
    ], [3.6, 7.6, 6.3]),
    ('img', '04-conciliando-aviso.png', 'Depois de Conciliar marcados, o sistema avisa quantos movimentos foram conciliados e atualiza a lista.'),

    ('h2', 'Depois de conciliar'),
    ('p', 'Em <b>Movimentos Financeiros</b>, os movimentos conciliados passam a mostrar <b>Sim</b> na coluna Conciliado, e o quadro <b>Conciliação</b> no topo '
          'mostra o valor conciliado, o valor não conciliado e o percentual. Se conciliar uma linha por engano, use o botão amarelo '
          '<b>Desfazer conciliação</b> do movimento: ele volta a ficar disponível e a linha do extrato também.'),
    ('img', '06-movimentos-depois.png', 'Movimentos Financeiros depois da conciliação: movimentos com Sim, e os que ficaram pendentes com Não.'),

    ('h2', 'Avisos e erros'),
    ('tabelagen', ['Mensagem', 'Causa', 'O que fazer'], [
        ['A agência (ou conta, ou banco) do arquivo é diferente da conta selecionada', 'O OFX é de outra conta bancária, ou o cadastro da Conta Financeira está com agência/conta diferente da real.', 'Confirme se escolheu a conta certa. Se o cadastro estiver errado, corrija em Cadastros → Conta Financeira. O sistema tolera o dígito verificador.'],
        ['Arquivo não é um OFX válido', 'O arquivo escolhido não é um extrato OFX (por exemplo, é um PDF ou CSV renomeado).', 'Baixe novamente no banco escolhendo o formato OFX.'],
        ['O arquivo não possui transações', 'O período do extrato está vazio.', 'Gere o extrato de um período com movimentação.'],
        ['Arquivo OFX muito grande', 'Mais de 2 MB.', 'Gere o extrato por período menor (por exemplo, mês a mês).'],
        ['Transação do extrato já conciliada com outro movimento', 'Duas pessoas conciliaram a mesma linha ao mesmo tempo.', 'Leia o extrato de novo para ver a situação atual.'],
    ], [5.2, 6.3, 6]),
    ('img', '07-aviso-conta-diferente.png', 'Aviso amarelo quando o arquivo é de outra agência: a leitura continua, mas confira a conta antes de conciliar.'),
    ('img', '08-arquivo-invalido.png', 'Mensagem quando o arquivo escolhido não é um OFX válido.'),

    ('h2', 'Boas práticas'),
    ('tabelagen', ['Recomendação', 'Por quê'], [
        ['Concilie com frequência (semanal ou mensal)', 'Períodos menores têm menos linhas e as diferenças são mais fáceis de achar.'],
        ['Registre tudo no sistema antes de ler o extrato', 'Quanto mais lançamentos já estiverem no ClinSis, mais linhas são encontradas automaticamente.'],
        ['Confira valores repetidos', 'Movimentos iguais podem ser ligados a linhas diferentes das que você imaginava.'],
        ['Não altere o arquivo OFX', 'O identificador de cada transação (FITID) vem do banco e é usado para não conciliar a mesma linha duas vezes.'],
        ['Use uma Conta Financeira por conta bancária', 'A conciliação compara só os movimentos da conta escolhida.'],
    ], [6.5, 11]),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Conciliacao_Bancaria_OFX.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Conciliacao_Bancaria_OFX_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Conciliacao_Bancaria_OFX.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
