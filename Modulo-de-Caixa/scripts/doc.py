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
TITULO = "Módulo de Caixa"
SUBTITULO = "Abertura, lançamentos, fechamento, solicitações de cancelamento e histórico"
VIDEO_NOME = "video-caixa-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('O módulo Caixa controla o dinheiro/valores que passam pela mão de cada atendente durante o '
         'dia: abertura com um fundo de troco, recebimentos e pagamentos feitos enquanto ele está '
         'aberto, sangrias/suprimentos manuais, e o fechamento no fim do expediente. <b>Cada usuário '
         'tem o seu próprio caixa</b> — não é um caixa único da clínica nem por consultório —, e mais '
         'de um atendente pode estar com o caixa aberto ao mesmo tempo.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Abrindo o caixa'),
    ('p', 'Em <b>Caixa → Meu caixa</b>, se você ainda não tem um caixa aberto, aparece o botão '
          '<b>"Abrir Caixa"</b>. É informado apenas o <b>valor inicial (fundo de troco)</b> em '
          'dinheiro — não há mais nenhum outro dado a preencher na abertura.'),
    ('img', '00-meu-caixa-inicial.png', 'Tela "Meu caixa" com o caixa fechado: badge "CAIXA FECHADO" e botão "Abrir Caixa".'),
    ('img', '02-abrir-caixa-preenchido.png', 'Modal de Abertura de Caixa com o valor inicial preenchido (R$ 100,00).'),
    ('img', '03-caixa-aberto-extrato-vazio.png', 'Caixa aberto: badge fica verde ("CAIXA ABERTO"), com a aba "Extrato" e o botão "Novo Lançamento".'),
    ('aviso', 'Só é possível ter <b>um caixa aberto por usuário</b> de cada vez — o sistema bloqueia '
              'abrir um segundo caixa enquanto o anterior não for fechado (ou reaberto por um '
              'administrador).'),

    ('h2', 'Lançamentos manuais: Suprimento e Sangria'),
    ('p', 'Com o caixa aberto, clique em <b>"Novo Lançamento"</b> para registrar uma entrada extra de '
          'dinheiro (<b>Suprimento</b>) ou uma retirada (<b>Sangria</b>) — por exemplo, reforçar o '
          'troco ou retirar dinheiro para um depósito. Escolha o tipo, a forma de pagamento, uma '
          'observação e o valor.'),
    ('img', '05-lancamento-suprimento-preenchido.png', 'Lançamento de Suprimento: forma de pagamento Dinheiro, valor R$ 50,00, com observação.'),
    ('img', '07-extrato-com-suprimento.png', 'Lançamento salvo e refletido no Extrato do caixa, com o ícone verde de entrada.'),
    ('aviso', '<b>Suprimento só pode ser feito em Dinheiro</b> — o sistema bloqueia qualquer outra '
              'forma de pagamento para esse tipo de lançamento (testado ao vivo: tentar suprimento em '
              'Cartão de Crédito é recusado com a mensagem "Suprimento só pode ser feito em '
              'dinheiro"). Já a Sangria também é sempre validada contra o saldo em espécie disponível '
              'no caixa — não é possível retirar mais dinheiro do que existe.'),

    ('h2', 'Recebimentos e pagamentos aparecem automaticamente'),
    ('p', 'A grande vantagem do caixa é que ele <b>não precisa de lançamento manual</b> para '
          'registrar dinheiro que já entrou ou saiu pelo sistema: toda baixa de <b>Conta a Receber</b> '
          'ou <b>Conta a Pagar</b> feita enquanto seu caixa está aberto entra automaticamente no '
          'extrato dele — não existe um passo extra de "lançar no caixa" depois de dar baixa numa '
          'conta.'),
    ('img', '08b-modal-baixa-preenchida.png', 'Dando baixa numa Conta a Receber (tela normal de Contas a Receber) com o caixa aberto.'),
    ('img', '10-extrato-com-entrada-refletida.png',
     'De volta em "Meu caixa": a baixa aparece automaticamente no Extrato, como uma entrada em nome '
     'do paciente — sem nenhum lançamento manual adicional.'),
    ('aviso', 'Isso só acontece para usuários com a opção <b>"Controla Caixa"</b> marcada no cadastro '
              'de acesso dele (Admin → Acessos). Se essa opção estiver desmarcada, o usuário consegue '
              'dar baixa em Contas a Receber/Pagar normalmente <b>mesmo sem caixa aberto</b>, e essas '
              'baixas não aparecem em nenhum caixa. Já um usuário com "Controla Caixa" marcado é '
              '<b>obrigado</b> a ter um caixa aberto para registrar qualquer recebimento — sem isso, o '
              'sistema recusa com a mensagem "Nenhum caixa aberto para o usuário".'),

    ('h2', 'Fechando o caixa'),
    ('p', 'Clique em <b>"Fechar Caixa"</b>. O sistema mostra um resumo com todas as Entradas (valor '
          'de abertura + suprimentos + recebimentos, agrupados por forma de pagamento) e Saídas '
          '(sangrias + pagamentos), e calcula o saldo final em espécie, em cheque e o saldo geral.'),
    ('img', '17-bloqueio-fechar-com-solicitacao-pendente.png', 'Resumo do fechamento: Entradas, Saídas e o Saldo do caixa calculado (em espécie, em cheque e geral).'),
    ('img', '15-apos-fechar-caixa.png', 'Confirmação "Caixa Fechado!" — badge volta a ficar cinza/fechado e o botão "Abrir Caixa" reaparece.'),
    ('aviso', 'O fechamento do ClinSis é <b>totalmente calculado pelo sistema</b> — não existe uma '
              'etapa de "contar o dinheiro físico" e digitar um valor diferente para comparar com o '
              'esperado (não há registro de sobra/quebra de caixa). O valor de fechamento gravado é '
              'sempre exatamente igual ao saldo calculado pelas entradas e saídas do próprio caixa.'),

    ('h2', 'Solicitação de cancelamento de lançamento'),
    ('p', 'Um lançamento manual (Suprimento/Sangria) pode ser cancelado, mas não diretamente — quem '
          'lançou clica em <b>"Cancelar"</b> na linha do Extrato para <b>solicitar</b> o cancelamento; '
          'só um administrador, na tela <b>Caixa → Solicitações</b>, efetiva o cancelamento de fato.'),
    ('img', '12-confirmar-solicitar-cancelamento.png', 'Solicitando o cancelamento de um lançamento de Suprimento a partir do Extrato.'),
    ('img', '18-solicitacoes-pendentes.png', 'Tela "Solicitações de cancelamento" (acesso só do administrador): lista as solicitações pendentes de todos os usuários.'),
    ('img', '20-solicitacoes-apos-aprovar.png', 'Depois de aprovado pelo administrador, o lançamento some da lista de pendentes.'),
    ('aviso', 'Enquanto existir uma solicitação de cancelamento pendente naquele caixa, <b>o fechamento '
              'fica bloqueado</b> — o sistema recusa com a mensagem "Não é possível fechar. Existe '
              'solicitação pendente de cancelamento". É preciso que um administrador aprove (ou o '
              'próprio usuário desfaça a solicitação, botão "Desfazer Cancelar") antes de conseguir '
              'fechar o caixa.'),

    ('h2', 'Histórico de caixas'),
    ('p', 'Em <b>Caixa → Listar</b>, é possível consultar caixas já abertos/fechados, filtrando por '
          'usuário e por período (é preciso informar usuário ou um intervalo de datas). Atendentes só '
          'veem os próprios caixas; administradores podem consultar de qualquer usuário.'),
    ('img', '23-listar-historico-caixas.png', 'Histórico de caixas do usuário, com valor de fechamento e valor em espécie de cada um.'),
    ('img', '22-extrato-caixa-fechado.png', 'Extrato de um caixa já fechado, acessado pelo botão "Extrato" — mesmo layout do extrato do caixa aberto.'),

    ('aviso', 'Reabrir um caixa já fechado só pode ser feito por um administrador, e exige informar '
              'um motivo (mínimo 5 caracteres) — é a única forma de corrigir um caixa fechado por '
              'engano ou com dados incompletos.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Modulo_Caixa.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Modulo_Caixa_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Modulo_Caixa.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
