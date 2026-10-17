# Painel de Chegada (TV)

_Avisar o profissional, na TV e no celular, que o paciente chegou_

Versão 1.0 — 16/10/2026

O Painel de chegada mostra, numa TV da clínica, o nome do profissional e do paciente que acabou de chegar, com um aviso sonoro. Ao mesmo tempo, o profissional recebe o chamado no sistema (e no celular, se ativar as notificações). O aviso sai do Check-in ("Notificar profissional") ou do botão Avisar chegada da Agenda. Quando não há chegada, a TV mostra a data, a hora, o clima e os aniversariantes do dia. O módulo é liberado por clínica pela Área do Administrador e vem desligado.

Assista ao vídeo narrado desta rotina: [https://youtu.be/CX3IduHG7Kg](https://youtu.be/CX3IduHG7Kg)

---

## Como funciona

| Peça | Para que serve |
|---|---|
| TV (/painel-chegada) | Tela cheia que fica ligada na recepção ou no corredor. Mostra a chegada, o som e os aniversariantes. Não tem login: é autorizada uma vez por QR code. |
| Configuração (Tabelas Aux. → Painel de chegada) | Ativa o painel e define duração do aviso, tempo de cada cartão, som, volume, forma de mostrar o nome do paciente e limite de TVs. Somente Administrador. |
| Aviso de chegada | Criado pelo Check-in (modal "Notificar profissional") ou pelo botão Avisar chegada na Agenda. |
| Chamado ao profissional | O profissional vê "Fulano foi chamado" na tela do sistema e, com as notificações ativas, recebe o aviso também no celular ou no computador. |

## Passo 1: liberar e configurar

Na Área do Administrador (/area), no cadastro da clínica, marque Painel de chegada na TV. Depois, com um usuário Administrador, abra Tabelas Aux. → Painel de chegada, marque Ativar módulo de painel de chegada, ajuste os campos e clique em Salvar. Quem já estava logado precisa sair e entrar de novo para o menu aparecer.

![Configuração do painel: ativação, tempos, som, volume, nome do paciente e TVs autorizadas. Embaixo, a presença da TV.](01-configuracao.png)

_Configuração do painel: ativação, tempos, som, volume, nome do paciente e TVs autorizadas. Embaixo, a presença da TV._

| Campo | Para que serve |
|---|---|
| Duração do aviso (minutos) | Por quanto tempo a chegada continua na fila da TV (de 1 a 60). |
| Tempo de cada cartão (segundos) | Quanto tempo cada chamada fica na tela antes de passar para a próxima (de 5 a 30). |
| Som e Volume | Suave, Neutro, Acessível, Piano ambiente ou Sem som. O botão Ouvir som toca uma prévia. |
| Nome do paciente | Primeiro nome + inicial (mais discreto, recomendado para sala de espera) ou Nome completo. |
| Máximo de TVs autorizadas | Quantas TVs podem estar conectadas ao mesmo tempo (de 1 a 20). |
| Validade da autorização (horas) | Depois desse prazo a TV pede nova autorização (de 1 a 72). |

A seção Presença da TV informa se há TV conectada ("TV conectada (1)" ou "Nenhuma TV conectada"). Na Agenda, se o painel estiver ligado e nenhuma TV conectada, aparece um aviso amarelo: "Painel de chegada indisponível: nenhum dispositivo conectado. Os avisos não serão exibidos.", com o link Como conectar a TV.

![Agenda avisando que nenhuma TV está conectada ao painel.](02-agenda-sem-tv.png)

_Agenda avisando que nenhuma TV está conectada ao painel._

## Passo 2: abrir a TV

No navegador da TV (ou do computador ligado a ela), abra o endereço do sistema acrescido de /painel-chegada e deixe em tela cheia. Aparece Autorize esse dispositivo, com um QR code e um código de 6 dígitos.

![TV ainda não autorizada: QR code e código.](03-tv-qr.png)

_TV ainda não autorizada: QR code e código._

## Passo 3: autorizar a TV

Com o celular da recepção, logado como administrador, leia o QR code e clique em Autorizar. Em poucos segundos a TV passa para Aguardando chegadas.

![Página aberta pelo QR code: confirmar a autorização da TV.](04-autorizar.png)

_Página aberta pelo QR code: confirmar a autorização da TV._

![TV autorizada; a página fecha sozinha.](04b-autorizado.png)

_TV autorizada; a página fecha sozinha._

![TV aguardando chegadas. A primeira vez pede um clique na tela para liberar o som.](05-tv-aguardando.png)

_TV aguardando chegadas. A primeira vez pede um clique na tela para liberar o som._

> ⚠️ O navegador só toca som depois de um clique na página. Por isso, ao ligar a TV, clique uma vez na tela: o rodapé deixa de mostrar "Clique na tela para ativar o som" e o ícone do alto-falante fica ativo.

## Avisar a chegada do paciente

Pelo Check-in. Ao confirmar um Check-in (módulo e painel ligados), o sistema abre Notificar profissional: "Deseja avisar o profissional que o paciente chegou?". Cada horário do paciente aparece com o profissional. Marque os que quiser e clique em Avisar agora, ou em Agora não para seguir sem avisar. O resultado é "N aviso(s) enviado(s) para o painel".

Pela Agenda. Na linha do paciente, abra o menu de ações (os três pontinhos) e clique em Avisar chegada. O botão só aparece para atendimentos de hoje. Se nenhuma TV estiver conectada, o sistema avisa e não envia.

![Menu de ações da linha do paciente, com Avisar chegada.](06-agenda-avisar.png)

_Menu de ações da linha do paciente, com Avisar chegada._

![Confirmação: "Aviso enviado para o painel."](06b-aviso-enviado.png)

_Confirmação: "Aviso enviado para o painel."_

Na TV aparece NOVA CHEGADA com o nome do profissional em destaque e o do paciente abaixo, uma barra de tempo e o som. Cada chamada fica na tela pelo tempo do cartão; a anterior fica no canto, em "Chamada anterior". Se o mesmo paciente for avisado de novo, a TV mostra outro cartão.

![TV: Nova chegada, com o profissional, o paciente, a barra de tempo e o selo da data comemorativa (Outubro Rosa).](07-tv-nova-chegada.png)

_TV: Nova chegada, com o profissional, o paciente, a barra de tempo e o selo da data comemorativa (Outubro Rosa)._

## O que o profissional recebe

O profissional logado vê a mensagem "Nome do paciente foi chamado." (título Chamado do painel), por 10 segundos, e o celular vibra. Para receber também com o sistema minimizado, ao entrar o sistema oferece ativar as notificações: aceite a permissão do navegador. Depois disso a confirmação é "Este dispositivo receberá os chamados do painel."

## Conferir as chamadas do dia

Na Agenda, em Mais opções → Ver chamadas do painel, aparece a lista com Profissional, Paciente, quando foi criada, quando expira e a situação. Sem chamadas, o sistema mostra os aniversariantes do dia.

![Chamadas do painel: quem foi avisado, a hora e a situação.](08-chamadas.png)

_Chamadas do painel: quem foi avisado, a hora e a situação._

## Aniversariantes e datas comemorativas

Quando não há chegada, a TV mostra Aniversariantes do dia com a mensagem Parabéns! e os nomes (pacientes da clínica que fazem aniversário no dia). No alto aparecem o nome da cidade, a data e hora e o clima; e, em datas comemorativas (Outubro Rosa, Novembro Azul, Natal etc.), um selo discreto com o nome da campanha.

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| Menu "Painel de chegada" não aparece | Módulo desligado na clínica, ou usuário não é Administrador | Ligar na Área do Administrador; sair e entrar de novo |
| "Nenhuma TV do painel está conectada" | TV desligada, sem autorização ou autorização vencida | Abrir /painel-chegada na TV e autorizar de novo (passo 3) |
| Aviso criado, mas a TV não toca som | O navegador bloqueia som sem clique | Clicar uma vez na tela da TV |
| "Agendamento inválido para aviso" | O atendimento não é de hoje | O aviso só vale para o dia |
| Profissional não recebe o chamado | Não está logado, ou não ativou as notificações | Entrar no sistema e aceitar as notificações do navegador |
