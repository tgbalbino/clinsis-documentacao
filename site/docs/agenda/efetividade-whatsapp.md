# Efetividade do Aviso por WhatsApp

Mostra se o lembrete por WhatsApp vale a pena: taxa de falta de quem recebeu e de quem não recebeu o aviso, respostas, faltas evitadas e custo por falta evitada.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Efetividade-WhatsApp/Documentacao_Efetividade_WhatsApp_Simplificado.pdf)

## Vídeo narrado

*Vídeo em processo de publicação — o link será adicionado aqui assim que estiver disponível no YouTube.*

## Conteúdo completo do manual

---


_O aviso de lembrete vale a pena? Faltas, respostas e custo por falta evitada_

Versão 1.0 — 16/10/2026

Para quem usa: administrador da clínica com o módulo WhatsApp Meta ativo. Onde fica: menu lateral → Relatórios → cartão WhatsApp Meta → Efetividade do aviso. O cartão só aparece para clínicas com o módulo WhatsApp Meta. ## 1. Para que serve

---

A clínica envia um lembrete pelo WhatsApp na véspera da consulta. Esta tela responde se esse aviso **vale a pena**:

• o paciente recebe e lê a mensagem?

• o paciente responde (confirma ou avisa que não vai)?

• quem recebeu o aviso falta menos do que quem não recebeu?

• quanto custa cada falta evitada?

A tela cruza três informações: o que aconteceu com a mensagem (enviada, entregue, lida), o que o paciente respondeu e o que foi lançado na agenda naquele dia (presente, faltou, desmarcou).

## 2. Antes de usar

• Para equipe técnica: aplicar a migrations `BLL/docs/163_WhatsApp_Meta_Efetividade_Abertura_Link_Motivo_Nao_Envio.sql` e `BLL/docs/164_WhatsApp_Meta_Webhook_Remetente.sql` **antes** de publicar a API.

• O módulo WhatsApp Meta precisa estar ativo e o lembrete configurado (Configurações → WhatsApp Meta).

• A recepção precisa **lançar presença e falta na agenda**. Sessão sem lançamento não entra no cálculo da taxa de falta.

• A tela só considera datas **que já passaram**. A consulta de hoje e as futuras aparecem a partir de amanhã.

• Só o administrador enxerga a tela.

## 3. Como usar

1. Escolha o período em **De** e **Até**. Ao abrir, a tela mostra os últimos 90 dias. O máximo é 366 dias.

2. Se quiser olhar um profissional só, escolha-o em **Profissional**; a tela busca de novo na hora. A lista vem dos profissionais com agendamento no período; para trocar o período mantendo a lista completa, volte antes para **Todos**.

3. Se quiser ver o custo, informe o **Custo por mensagem (R$)**. O valor fica salvo no seu navegador e é usado só nos cálculos da tela. Consulte o preço na tabela da Meta, porque ele muda por país e por tipo de mensagem.

4. Clique em **Buscar**.

5. Use **Excel (CSV)** para baixar os números.

## 4. Como ler cada parte

## 4.1 Indicadores do topo

| Indicador | O que significa |
|---|---|
| Taxa de falta com aviso recebido | Entre os pacientes cujo aviso chegou ao celular, quantos faltaram |
| Taxa de falta sem aviso recebido | Entre os que não receberam (sem aviso, sem autorização ou mensagem que não chegou), quantos faltaram |
| Diferença | Taxa sem aviso menos taxa com aviso, em pontos percentuais. **Positivo** = quem recebeu faltou menos |
| Faltas evitadas (estimativa) | Diferença das taxas multiplicada pelas sessões de quem recebeu. É uma estimativa, não uma contagem exata |
| Mensagens enviadas | Mensagens de verdade enviadas. Um paciente com dois horários no dia recebe uma só mensagem |
| Custo por falta evitada | Custo total das mensagens dividido pelas faltas evitadas. Só aparece se você informou o custo |
| Responderam (dos entregues) | Quantos dos que receberam confirmaram ou avisaram ausência |
| Tempo mediano até responder | Metade dos pacientes respondeu em menos que esse tempo. Logo abaixo, com quanta antecedência quem avisou ausência avisou |

## 4.2 Do agendamento à resposta

Mostra onde as pessoas "caem" no caminho: agendamentos no período → aviso criado → enviado → entregue → lido → abriu o link → respondeu (pelo link ou no WhatsApp).

• Muita queda entre **agendamentos** e **aviso criado**: pacientes sem autorização de WhatsApp, sem telefone válido ou excluídos pelos filtros do lembrete.

• Queda entre **enviado** e **entregue**: número errado ou sem WhatsApp. Veja a tabela de falhas no fim da tela.

• Queda entre **entregue** e **lido**: o paciente não abriu a conversa, ou desativou o recibo de leitura. Nesse caso ele pode ter lido e aparecer só como entregue.

• **Abriu o link** conta quem abriu a página de confirmação, mesmo sem responder. Pode ser maior que "lido" pelo mesmo motivo do recibo de leitura. Só é registrado a partir da data em que a atualização do sistema entrou; antes disso, só quem respondeu aparece. Quem abre e não responde mostra que o aviso chamou atenção, mas o paciente não decidiu.

## 4.3 Taxa de falta por mês

Duas barras por mês: azul para quem recebeu o aviso, cinza para quem não recebeu. Passe o mouse (ou toque) em uma barra para ver o percentual e quantas sessões entraram.

Os meses **anteriores ao primeiro aviso** mostram só a barra cinza. Essa é a taxa de falta da clínica antes de ativar o módulo, e é a melhor comparação do "antes e depois".

## 4.4 O que o paciente fez com o aviso × o que aconteceu na sessão

Cada linha é uma situação do aviso:

• **Sem aviso**: não foi enviado.

• **Aviso não entregue**: foi enviado e não chegou.

• **Entregue, sem resposta** e **Lido, sem resposta**: chegou, e o paciente não respondeu.

• **Confirmou presença** e **Avisou ausência**: o paciente respondeu pelo link.

As colunas mostram o que ficou na agenda. A **taxa de falta** = (faltas + ausências justificadas) ÷ (presentes + faltas + ausências justificadas). Desmarcações, remarcações e sessões sem lançamento não entram nessa conta.

Pergunta útil: **quem confirmou falta bem menos do que quem não respondeu?** Se for quase igual, o botão de confirmar pouco ajuda e o valor está no lembrete em si.

## 4.5 Por que não houve aviso

Separa os agendamentos sem aviso pelo motivo:

• **Sem autorização de WhatsApp ou telefone inválido**: o paciente não deu consentimento ou o telefone não serve.

• **Sem template aprovado**: a clínica estava sem a mensagem aprovada na Meta no dia.

• **Não identificado**: excluído pelos filtros do lembrete, marcado depois do disparo do dia, ou data anterior ao registro dos motivos.

O motivo só é gravado a cada geração do lembrete, a partir da atualização. Para períodos antigos, quase tudo cai em "não identificado". Use a taxa de falta de cada motivo para avaliar se o grupo sem aviso é comparável a quem recebeu.

## 4.6 Quem recebeu o aviso e não usou o link

Entre os pacientes que receberam (ou leram) o aviso e **não** responderam pelo link, separa:

• **Respondeu no WhatsApp, sem usar o link**: escreveu na conversa (texto, áudio ou imagem) respondendo ao aviso, ou da mesma linha em até 48 horas depois do envio e antes do fim do dia da consulta.

• **Não respondeu de nenhum modo**.

Compare a taxa de falta dos dois. Se quem respondeu falta bem menos, vale incentivar a resposta; se for igual, a resposta não é o que pesa.

Cuidados:

• O sistema só registra **que** houve resposta; o conteúdo da mensagem não é lido nem exibido, e não dá para saber se foi "vou" ou "não vou".

• A ligação com o aviso usa o telefone de quem escreveu (comparando os 8 últimos dígitos) e só funciona para mensagens recebidas depois da atualização que passou a guardar o telefone do remetente. Para períodos anteriores, só as respostas feitas com "responder" na mensagem do aviso são encontradas.

• Uma mensagem sobre outro assunto, enviada pelo mesmo telefone nesse prazo, também conta como resposta.

## 4.7 Por profissional, dia, horário e plano

Escolha a aba. Cada linha compara a taxa de falta de quem recebeu e de quem não recebeu naquele grupo. Serve para decidir onde manter o aviso e onde ele não faz diferença (e então ajustar os filtros em Configurações → WhatsApp Meta).

## 4.8 Mensagens com falha

Lista os códigos de erro devolvidos pela Meta e quantas mensagens falharam por cada um.

## 5. Avisos da tela

• **"Poucas sessões com resultado lançado"**: algum dos dois grupos tem menos de 30 sessões com presença ou falta lançada. Os percentuais não permitem concluir nada. Aumente o período ou peça à recepção para lançar as presenças.

• **"X agendamentos sem presença ou falta lançada"**: ficam fora da taxa de falta. Quanto mais alto esse número, menos confiável o resultado.

## 6. Cuidados ao interpretar

1. **Quem recebe o aviso não é igual a quem não recebe.** Pacientes com WhatsApp autorizado podem faltar menos de qualquer jeito. Por isso, olhe também o "antes e depois" no gráfico mensal.

2. **A estimativa de faltas evitadas é aproximada.** Use para ter uma ordem de grandeza, não para prestar contas exatas.

3. **A confirmação é uma intenção.** Uma ausência avisada não cancela a agenda; a vaga continua ocupada até alguém desmarcar.

4. **Leitura**: depende do recibo de leitura do paciente.

## 7. Perguntas frequentes

**A tela mostra tudo zerado.** Confira se há agendamentos com data passada no período e se o módulo enviou lembretes.

**Por que não vejo a consulta de hoje?** A tela só mostra datas passadas, porque o resultado da sessão só existe depois que ela acontece.

**O custo não aparece.** Informe o custo por mensagem no campo da tela.

**Diferença negativa.** Quem recebeu o aviso faltou mais. Verifique o tamanho da amostra e o "antes e depois" antes de tirar conclusão.

## 8. Regras usadas no cálculo (para conferência)

• Cada agendamento do período entra uma vez por data.

• A sessão da data é a N-ésima ocorrência do dia da semana no mês: 1ª quinta = sessão 1, 2ª quinta = sessão 2, e assim até a 5ª. O resultado vem do status daquela sessão na agenda.

• Presente = 3. Faltou = 4. Ausência justificada = 5. Paciente desmarcou = 1. Profissional desmarcou = 2. Remarcação = 6. Qualquer outro valor é "sem lançamento".

• "Receberam o aviso" = mensagem entregue, lida ou respondida. "Não receberam" = sem aviso ou aviso não entregue.
