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
TITULO = "Contrato com Assinatura Digital (D4Sign)"
SUBTITULO = "Envio para assinatura eletrônica, acompanhamento e fechamento automático"
VIDEO_NOME = "video-contrato-d4sign-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('Este manual complementa o de <b>Contrato (sem assinatura digital)</b>, cobrindo o que muda '
         'quando a clínica usa a integração com a <b>D4Sign</b> para colher a assinatura do paciente '
         'eletronicamente, em vez de assinar manualmente no sistema. O ciclo de vida do contrato '
         '(Criado → Assinado → Fechado, com geração automática de Conta a Receber) continua o mesmo — '
         'o que muda é <b>como</b> a assinatura acontece: em vez de um clique interno, o paciente '
         'assina de verdade, remotamente, e o próprio sistema fecha o contrato sozinho assim que a '
         'assinatura é confirmada.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste, '
          'usando a conta Sandbox real da D4Sign. Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Configuração prévia (feita uma vez pela equipe técnica)'),
    ('p', 'Antes de qualquer contrato poder ser enviado para assinatura, a integração precisa estar '
          'configurada em <b>Tabelas Aux. → D4Sign</b> (rota <font face="Courier">/aux/d4sign</font>): '
          'token de acesso da conta D4Sign, UUID do cofre onde os documentos são guardados, ambiente '
          '(Sandbox para testes ou Produção) e a URL pública do webhook — o endereço que a D4Sign chama '
          'de volta para avisar o ClinSis quando algo acontece com a assinatura (documento visualizado, '
          'assinado, finalizado, cancelado).'),
    ('img', '00-config-d4sign.png',
     'Tela de Configuração D4Sign: integração ativa, ambiente Sandbox, cofre "Contratos", URL do '
     'webhook e credenciais já configuradas (mascaradas, com "✓" indicando que estão salvas). O botão '
     '"Testar conexão" confirma que o ClinSis consegue falar com a D4Sign.'),
    ('aviso', 'A URL do webhook precisa ser um endereço público (HTTPS) que realmente chegue até a API '
              'do ClinSis. Em produção, é o domínio real do servidor; em ambiente de desenvolvimento, é '
              'comum usar um túnel temporário (ex.: Cloudflare Tunnel) apontando para a máquina local — '
              'só funciona enquanto esse túnel estiver rodando.'),

    ('h2', 'Enviando o contrato para assinatura eletrônica'),
    ('p', 'Com o contrato criado, serviços e condição de pagamento preenchidos (igual à versão sem '
          'D4Sign), em vez de marcar "assinado" manualmente, clique em <b>"Enviar para assinatura"</b>. '
          'O sistema avisa que, após o envio, os dados do contrato ficam bloqueados — ele deixa de '
          'poder ser editado a partir daqui.'),
    ('img', '01-contrato-pronto-enviar-assinatura.png', 'Contrato pronto (serviços e pagamento batendo), com o botão "Enviar para assinatura" disponível.'),
    ('img', '02-confirmar-enviar-assinatura.png', 'Confirmação: "Deseja enviar este contrato para assinatura eletrônica? Após o envio, os dados ficarão bloqueados."'),
    ('p', 'Ao confirmar, o sistema, em sequência: gera o PDF do contrato, envia esse PDF para a D4Sign, '
          'cadastra o(s) signatário(s) e dispara o convite de assinatura por e-mail. O signatário é o '
          '<b>responsável</b> do contrato, se houver um cadastrado, ou o <b>próprio paciente</b> quando '
          'não há responsável — o e-mail usado é sempre o que está no cadastro da pessoa no ClinSis.'),
    ('img', '02b-modal-enviado-com-sucesso.png',
     'Modal de confirmação: "O contrato foi enviado com sucesso para a assinatura eletrônica. Oriente o '
     'paciente/responsável a verificar o e-mail ou o WhatsApp cadastrado para localizar o link de '
     'assinatura enviado pela D4Sign."'),
    ('img', '07-contrato-aguardando-assinatura-bloqueado.png',
     'Contrato com o badge "Aguardando assinaturas": todos os campos ficam somente leitura, e no '
     'rodapé aparecem os botões de Sincronizar (ícone circular) e Cancelar solicitação (ícone de '
     'proibido), no lugar de Salvar.'),

    ('h2', 'Acompanhando a assinatura'),
    ('p', 'A assinatura em si acontece <b>fora do ClinSis</b>, na página da D4Sign — o paciente/'
          'responsável recebe o e-mail, abre o link, confere e assina o documento eletronicamente. '
          'Dentro do ClinSis, a aba <b>"Histórico da assinatura"</b> do contrato registra cada evento '
          'recebido (documento enviado, visualizado, assinado, finalizado), com data e situação '
          '(Processado/Pendente).'),
    ('img', '05-historico-assinatura.png',
     'Aba Histórico da assinatura: cada linha é um evento — no exemplo, o evento "Finalizado" foi '
     'capturado por uma sincronização manual (SYNC_4), e um cancelamento anterior aparece registrado '
     'também.'),
    ('aviso', 'Normalmente, o ClinSis fica sabendo que a assinatura avançou <b>automaticamente</b>, via '
              'webhook: assim que a D4Sign confirma um evento, ela avisa o ClinSis na hora, sem precisar '
              'de nenhuma ação da equipe. Se por algum motivo esse aviso automático não chegar (problema '
              'de rede, webhook temporariamente fora do ar), existe o botão <b>Sincronizar com a '
              'D4Sign</b> (ícone circular) para consultar o status manualmente a qualquer momento — foi '
              'exatamente esse botão que capturou o "Finalizado" no exemplo acima.'),

    ('h2', 'Fechamento automático após a assinatura'),
    ('p', 'Assim que a assinatura é confirmada (via webhook ou via Sincronizar), o ClinSis marca o '
          'contrato como <b>Assinado</b> e tenta <b>fechá-lo automaticamente</b> — o mesmo processo do '
          'botão manual "Fechar Contrato": gera as parcelas em Contas a Receber e trava o contrato '
          'definitivamente. Tudo isso acontece sem qualquer clique da equipe.'),
    ('img', '04-contrato-fechado-automaticamente.png',
     'Contrato com os badges "Assinatura finalizada" e "Contrato fechado em 18/09/2026" — e o botão '
     '"PDF assinado", que baixa o documento já assinado eletronicamente.'),
    ('img', '06-conta-a-receber-gerada.png',
     'Conferindo em Contas a Receber: a parcela gerada pelo fechamento automático deste contrato '
     'aparece normalmente, com Situação "Aberto" — igual à versão sem D4Sign.'),
    ('aviso', 'Se o fechamento automático falhar por algum motivo (ex.: parâmetro de Plano de Conta ou '
              'Centro de Custo do Contrato não configurado), o contrato fica assinado mas não fechado, '
              'e um alerta amarelo aparece na tela do próprio contrato explicando o motivo da falha — '
              'basta corrigir a causa e clicar em "Fechar Contrato" manualmente para reprocessar. Não '
              'existe hoje uma lista/relatório central de contratos com falha de fechamento; a '
              'conferência é feita contrato por contrato.'),

    ('h2', 'Cancelando uma solicitação de assinatura'),
    ('p', 'Enquanto a assinatura ainda não foi concluída, é possível clicar no ícone de '
          '<b>cancelar solicitação</b> (proibido, vermelho) para desistir do envio. O sistema cancela o '
          'documento na D4Sign e o contrato volta a ficar liberado para edição — os serviços e a '
          'condição de pagamento podem ser revisados e o contrato pode ser reenviado para assinatura '
          'depois. Se o documento já tiver sido finalizado (assinado por todos) no momento do '
          'cancelamento, o sistema não cancela — em vez disso, apenas atualiza o status para refletir '
          'que já foi assinado.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contrato_D4Sign.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contrato_D4Sign_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Contrato_D4Sign.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
