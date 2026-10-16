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

VERSAO = '1.0'
DATA = '16/10/2026'
TITULO = 'Efetividade do Aviso por WhatsApp'
SUBTITULO = 'O aviso de lembrete vale a pena? Faltas, respostas e custo por falta evitada'
VIDEO_NOME = None
INTRO = 'Para quem usa: administrador da clínica com o módulo WhatsApp Meta ativo. Onde fica: menu lateral → Relatórios → cartão WhatsApp Meta → Efetividade do aviso. O cartão só aparece para clínicas com o módulo WhatsApp Meta. ## 1. Para que serve'
RODAPE = ('Documento elaborado a partir do manual da funcionalidade (docs/WHATSAPP_META_EFETIVIDADE_MANUAL.md do ApiClinica) e da leitura do código da tela. '
          'Não há capturas de tela nesta versão: o banco de testes local não tem mensagens do WhatsApp Meta suficientes para ilustrar os números.')

blocks = [('p',
  'A clínica envia um lembrete pelo WhatsApp na véspera da consulta. Esta tela responde se esse aviso **vale '
  'a pena**:'),
 ('p', '• o paciente recebe e lê a mensagem?'),
 ('p', '• o paciente responde (confirma ou avisa que não vai)?'),
 ('p', '• quem recebeu o aviso falta menos do que quem não recebeu?'),
 ('p', '• quanto custa cada falta evitada?'),
 ('p',
  'A tela cruza três informações: o que aconteceu com a mensagem (enviada, entregue, lida), o que o paciente '
  'respondeu e o que foi lançado na agenda naquele dia (presente, faltou, desmarcou).'),
 ('h2', '2. Antes de usar'),
 ('p',
  '• Para equipe técnica: aplicar a migrations '
  '`BLL/docs/163_WhatsApp_Meta_Efetividade_Abertura_Link_Motivo_Nao_Envio.sql` e '
  '`BLL/docs/164_WhatsApp_Meta_Webhook_Remetente.sql` **antes** de publicar a API.'),
 ('p',
  '• O módulo WhatsApp Meta precisa estar ativo e o lembrete configurado (Configurações → WhatsApp Meta).'),
 ('p',
  '• A recepção precisa **lançar presença e falta na agenda**. Sessão sem lançamento não entra no cálculo da '
  'taxa de falta.'),
 ('p',
  '• A tela só considera datas **que já passaram**. A consulta de hoje e as futuras aparecem a partir de '
  'amanhã.'),
 ('p', '• Só o administrador enxerga a tela.'),
 ('h2', '3. Como usar'),
 ('p',
  '1. Escolha o período em **De** e **Até**. Ao abrir, a tela mostra os últimos 90 dias. O máximo é 366 '
  'dias.'),
 ('p',
  '2. Se quiser olhar um profissional só, escolha-o em **Profissional**; a tela busca de novo na hora. A '
  'lista vem dos profissionais com agendamento no período; para trocar o período mantendo a lista completa, '
  'volte antes para **Todos**.'),
 ('p',
  '3. Se quiser ver o custo, informe o **Custo por mensagem (R$)**. O valor fica salvo no seu navegador e é '
  'usado só nos cálculos da tela. Consulte o preço na tabela da Meta, porque ele muda por país e por tipo de '
  'mensagem.'),
 ('p', '4. Clique em **Buscar**.'),
 ('p', '5. Use **Excel (CSV)** para baixar os números.'),
 ('h2', '4. Como ler cada parte'),
 ('h2', '4.1 Indicadores do topo'),
 ('tabelagen',
  ['Indicador', 'O que significa'],
  [['Taxa de falta com aviso recebido', 'Entre os pacientes cujo aviso chegou ao celular, quantos faltaram'],
   ['Taxa de falta sem aviso recebido',
    'Entre os que não receberam (sem aviso, sem autorização ou mensagem que não chegou), quantos faltaram'],
   ['Diferença',
    'Taxa sem aviso menos taxa com aviso, em pontos percentuais. **Positivo** = quem recebeu faltou menos'],
   ['Faltas evitadas (estimativa)',
    'Diferença das taxas multiplicada pelas sessões de quem recebeu. É uma estimativa, não uma contagem '
    'exata'],
   ['Mensagens enviadas',
    'Mensagens de verdade enviadas. Um paciente com dois horários no dia recebe uma só mensagem'],
   ['Custo por falta evitada',
    'Custo total das mensagens dividido pelas faltas evitadas. Só aparece se você informou o custo'],
   ['Responderam (dos entregues)', 'Quantos dos que receberam confirmaram ou avisaram ausência'],
   ['Tempo mediano até responder',
    'Metade dos pacientes respondeu em menos que esse tempo. Logo abaixo, com quanta antecedência quem '
    'avisou ausência avisou']],
  [8.75, 8.75]),
 ('h2', '4.2 Do agendamento à resposta'),
 ('p',
  'Mostra onde as pessoas "caem" no caminho: agendamentos no período → aviso criado → enviado → entregue → '
  'lido → abriu o link → respondeu (pelo link ou no WhatsApp).'),
 ('p',
  '• Muita queda entre **agendamentos** e **aviso criado**: pacientes sem autorização de WhatsApp, sem '
  'telefone válido ou excluídos pelos filtros do lembrete.'),
 ('p',
  '• Queda entre **enviado** e **entregue**: número errado ou sem WhatsApp. Veja a tabela de falhas no fim '
  'da tela.'),
 ('p',
  '• Queda entre **entregue** e **lido**: o paciente não abriu a conversa, ou desativou o recibo de leitura. '
  'Nesse caso ele pode ter lido e aparecer só como entregue.'),
 ('p',
  '• **Abriu o link** conta quem abriu a página de confirmação, mesmo sem responder. Pode ser maior que '
  '"lido" pelo mesmo motivo do recibo de leitura. Só é registrado a partir da data em que a atualização do '
  'sistema entrou; antes disso, só quem respondeu aparece. Quem abre e não responde mostra que o aviso '
  'chamou atenção, mas o paciente não decidiu.'),
 ('h2', '4.3 Taxa de falta por mês'),
 ('p',
  'Duas barras por mês: azul para quem recebeu o aviso, cinza para quem não recebeu. Passe o mouse (ou '
  'toque) em uma barra para ver o percentual e quantas sessões entraram.'),
 ('p',
  'Os meses **anteriores ao primeiro aviso** mostram só a barra cinza. Essa é a taxa de falta da clínica '
  'antes de ativar o módulo, e é a melhor comparação do "antes e depois".'),
 ('h2', '4.4 O que o paciente fez com o aviso × o que aconteceu na sessão'),
 ('p', 'Cada linha é uma situação do aviso:'),
 ('p', '• **Sem aviso**: não foi enviado.'),
 ('p', '• **Aviso não entregue**: foi enviado e não chegou.'),
 ('p', '• **Entregue, sem resposta** e **Lido, sem resposta**: chegou, e o paciente não respondeu.'),
 ('p', '• **Confirmou presença** e **Avisou ausência**: o paciente respondeu pelo link.'),
 ('p',
  'As colunas mostram o que ficou na agenda. A **taxa de falta** = (faltas + ausências justificadas) ÷ '
  '(presentes + faltas + ausências justificadas). Desmarcações, remarcações e sessões sem lançamento não '
  'entram nessa conta.'),
 ('p',
  'Pergunta útil: **quem confirmou falta bem menos do que quem não respondeu?** Se for quase igual, o botão '
  'de confirmar pouco ajuda e o valor está no lembrete em si.'),
 ('h2', '4.5 Por que não houve aviso'),
 ('p', 'Separa os agendamentos sem aviso pelo motivo:'),
 ('p',
  '• **Sem autorização de WhatsApp ou telefone inválido**: o paciente não deu consentimento ou o telefone '
  'não serve.'),
 ('p', '• **Sem template aprovado**: a clínica estava sem a mensagem aprovada na Meta no dia.'),
 ('p',
  '• **Não identificado**: excluído pelos filtros do lembrete, marcado depois do disparo do dia, ou data '
  'anterior ao registro dos motivos.'),
 ('p',
  'O motivo só é gravado a cada geração do lembrete, a partir da atualização. Para períodos antigos, quase '
  'tudo cai em "não identificado". Use a taxa de falta de cada motivo para avaliar se o grupo sem aviso é '
  'comparável a quem recebeu.'),
 ('h2', '4.6 Quem recebeu o aviso e não usou o link'),
 ('p', 'Entre os pacientes que receberam (ou leram) o aviso e **não** responderam pelo link, separa:'),
 ('p',
  '• **Respondeu no WhatsApp, sem usar o link**: escreveu na conversa (texto, áudio ou imagem) respondendo '
  'ao aviso, ou da mesma linha em até 48 horas depois do envio e antes do fim do dia da consulta.'),
 ('p', '• **Não respondeu de nenhum modo**.'),
 ('p',
  'Compare a taxa de falta dos dois. Se quem respondeu falta bem menos, vale incentivar a resposta; se for '
  'igual, a resposta não é o que pesa.'),
 ('p', 'Cuidados:'),
 ('p',
  '• O sistema só registra **que** houve resposta; o conteúdo da mensagem não é lido nem exibido, e não dá '
  'para saber se foi "vou" ou "não vou".'),
 ('p',
  '• A ligação com o aviso usa o telefone de quem escreveu (comparando os 8 últimos dígitos) e só funciona '
  'para mensagens recebidas depois da atualização que passou a guardar o telefone do remetente. Para '
  'períodos anteriores, só as respostas feitas com "responder" na mensagem do aviso são encontradas.'),
 ('p',
  '• Uma mensagem sobre outro assunto, enviada pelo mesmo telefone nesse prazo, também conta como resposta.'),
 ('h2', '4.7 Por profissional, dia, horário e plano'),
 ('p',
  'Escolha a aba. Cada linha compara a taxa de falta de quem recebeu e de quem não recebeu naquele grupo. '
  'Serve para decidir onde manter o aviso e onde ele não faz diferença (e então ajustar os filtros em '
  'Configurações → WhatsApp Meta).'),
 ('h2', '4.8 Mensagens com falha'),
 ('p', 'Lista os códigos de erro devolvidos pela Meta e quantas mensagens falharam por cada um.'),
 ('h2', '5. Avisos da tela'),
 ('p',
  '• **"Poucas sessões com resultado lançado"**: algum dos dois grupos tem menos de 30 sessões com presença '
  'ou falta lançada. Os percentuais não permitem concluir nada. Aumente o período ou peça à recepção para '
  'lançar as presenças.'),
 ('p',
  '• **"X agendamentos sem presença ou falta lançada"**: ficam fora da taxa de falta. Quanto mais alto esse '
  'número, menos confiável o resultado.'),
 ('h2', '6. Cuidados ao interpretar'),
 ('p',
  '1. **Quem recebe o aviso não é igual a quem não recebe.** Pacientes com WhatsApp autorizado podem faltar '
  'menos de qualquer jeito. Por isso, olhe também o "antes e depois" no gráfico mensal.'),
 ('p',
  '2. **A estimativa de faltas evitadas é aproximada.** Use para ter uma ordem de grandeza, não para prestar '
  'contas exatas.'),
 ('p',
  '3. **A confirmação é uma intenção.** Uma ausência avisada não cancela a agenda; a vaga continua ocupada '
  'até alguém desmarcar.'),
 ('p', '4. **Leitura**: depende do recibo de leitura do paciente.'),
 ('h2', '7. Perguntas frequentes'),
 ('p',
  '**A tela mostra tudo zerado.** Confira se há agendamentos com data passada no período e se o módulo '
  'enviou lembretes.'),
 ('p',
  '**Por que não vejo a consulta de hoje?** A tela só mostra datas passadas, porque o resultado da sessão só '
  'existe depois que ela acontece.'),
 ('p', '**O custo não aparece.** Informe o custo por mensagem no campo da tela.'),
 ('p',
  '**Diferença negativa.** Quem recebeu o aviso faltou mais. Verifique o tamanho da amostra e o "antes e '
  'depois" antes de tirar conclusão.'),
 ('h2', '8. Regras usadas no cálculo (para conferência)'),
 ('p', '• Cada agendamento do período entra uma vez por data.'),
 ('p',
  '• A sessão da data é a N-ésima ocorrência do dia da semana no mês: 1ª quinta = sessão 1, 2ª quinta = '
  'sessão 2, e assim até a 5ª. O resultado vem do status daquela sessão na agenda.'),
 ('p',
  '• Presente = 3. Faltou = 4. Ausência justificada = 5. Paciente desmarcou = 1. Profissional desmarcou = 2. '
  'Remarcação = 6. Qualquer outro valor é "sem lançamento".'),
 ('p',
  '• "Receberam o aviso" = mensagem entregue, lida ou respondida. "Não receberam" = sem aviso ou aviso não '
  'entregue.')]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Efetividade_WhatsApp.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Efetividade_WhatsApp_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Efetividade_WhatsApp.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
