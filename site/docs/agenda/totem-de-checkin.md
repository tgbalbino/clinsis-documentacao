# Totem de Check-in

Tela da portaria onde o paciente, ou o responsável, registra a chegada sozinho informando CPF e data de nascimento. A recepção vê o selo de chegada na agenda. Explica como ativar, autorizar o equipamento e o que o paciente vê.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Totem-de-Checkin/Documentacao_Totem_de_Checkin_Simplificado.pdf)

## Vídeo narrado

*Vídeo em processo de publicação — o link será adicionado aqui assim que estiver disponível no YouTube.*

## Conteúdo completo do manual

---


_O paciente (ou o responsável) registra a chegada sozinho na portaria, com CPF e data de nascimento_

Versão 1.0 — 16/10/2026

O Totem de check-in é a tela da portaria onde o paciente, ou o responsável por ele, registra a chegada sem usuário e senha: basta informar o CPF e a data de nascimento. A recepção vê um selo verde com o horário da chegada ao lado do nome do paciente na Agenda do dia. O totem apenas avisa a chegada: o Check-in da recepção (pagamento, Plano Próprio) continua sendo feito normalmente. O recurso vem desligado e é ativado pelo administrador da clínica.


---

## Onde fica cada coisa

| O que | Onde | Quem acessa |
|---|---|---|
| Ativar e configurar o totem | Menu Tabelas Aux. → Totem de check-in (/totem/configuracao) | Somente Administrador |
| Tela do totem (a que o paciente usa) | /totem, aberta no equipamento da portaria | Sem login (precisa ser autorizada uma vez) |
| Autorizar um totem | /totem/autorizar, aberta pelo QR code lido no celular do administrador | Somente Administrador logado |
| Ver quem chegou | Selo verde com o horário, antes do nome do paciente, na Agenda do dia | Recepção e demais usuários da agenda |

## Antes de começar

| Requisito | Detalhe |
|---|---|
| Paciente com CPF e data de nascimento | É com esses dois dados que o paciente se identifica no totem. |
| Responsável (opcional) | Cadastrado no paciente, com CPF, data de nascimento e vínculo ativo. Com o totem ativo, a data de nascimento do responsável passa a ser obrigatória. Para achar quem está sem ela: Cadastros → Pessoa → Filtros, marque Responsável e Sem data de nascimento. |
| Atendimento marcado para hoje | O totem só mostra o que está agendado no dia. Atendimentos desmarcados, com falta, justificados ou remarcados não aparecem. |
| Scripts do banco (suporte) | Antes de publicar a API: 206_Totem_Auto_Checkin.sql, 207_Responsaveis_Paciente.sql e 209_Totem_Responsavel.sql. |

## Passo 1: ativar e configurar (administrador)

Entre com um usuário Administrador, abra Tabelas Aux. → Totem de check-in, marque Ativar o totem nesta clínica, ajuste os valores se precisar e clique em Salvar.


| Campo | Para que serve | Padrão |
|---|---|---|
| Liberar quantos minutos antes | Até quanto tempo antes do horário o paciente pode registrar a chegada (máx. 240) | 60 |
| Aceitar até quantos minutos depois | Até quanto tempo depois do horário ainda aceita (máx. 240) | 30 |
| Inatividade para voltar ao início | A tela volta ao início sozinha se ninguém tocar (segundos) | 30 |
| Validade da autorização | Depois desse prazo o totem pede nova autorização (horas) | 720 (30 dias) |
| Tentativas erradas antes de bloquear | Erros de CPF/nascimento antes de bloquear aquele CPF | 5 |
| Bloqueio (minutos) | Tempo do bloqueio | 10 |
| Mensagem para Plano Próprio | Texto mostrado ao paciente de Plano Próprio | Chegada registrada. Dirija-se à recepção. |

## Passo 2: abrir o totem na portaria

No computador ou tablet da portaria, abra o navegador no endereço do sistema acrescido de /totem. A tela mostra Autorize este totem, com um QR code e um código de 6 dígitos.


## Passo 3: autorizar o totem (administrador)

Com o Administrador logado, leia o QR code com o celular. Dê um nome ao totem (por exemplo, "Totem da recepção") e clique em Autorizar totem. O QR code vale por 5 minutos; se expirar, a própria tela gera outro.



Em poucos segundos o equipamento troca para Bem-vindo(a), pronto para uso.


## Como o paciente usa

Quem chega toca em Registrar chegada, digita o CPF e depois a data de nascimento (somente números). Os dois são da mesma pessoa, a que está diante do totem: o paciente usa os próprios dados; o responsável usa os dele, não os do paciente.



Identificada a pessoa, o totem mostra os atendimentos de hoje. Marque o que está chegando e toque em Confirmar chegada.



| Quem está no totem | CPF e nascimento digitados | O que aparece |
|---|---|---|
| Paciente | Os do próprio paciente | Os atendimentos dele |
| Responsável (pai, mãe, avó, babá…) | Os do responsável | Os atendimentos dos pacientes ligados a ele; com mais de um dependente, o nome de cada paciente |

> ⚠️ Criança cadastrada com o CPF do pai ou da mãe: com o CPF do responsável e o nascimento do responsável, ele entra como responsável; com o CPF do responsável e o nascimento da criança, entra como o próprio paciente. Os dois caminhos funcionam.

> ⚠️ Sugestão de aviso para colar ao lado do totem: "Digite o CPF e a data de nascimento de quem está aqui agora. Se você é o responsável pelo paciente, use os SEUS dados, não os do paciente. Em caso de dúvida, procure a recepção."

## O que o totem responde

| Situação | O que o totem mostra |
|---|---|
| Dentro da janela de horário | Chegada registrada, "Aguarde ser chamado" |
| Plano Próprio | Chegada registrada e a mensagem para seguir à recepção |
| Chegou cedo demais | "Ainda é cedo para o seu horário" |
| Passou da janela | "O horário do seu atendimento já passou. Procure a recepção" |
| Já registrado, ou já fez check-in | "Sua chegada já foi registrada" |
| Sem atendimento hoje | "Não encontramos agendamento para hoje. Procure a recepção" |
| CPF/nascimento não conferem, ou bloqueado | Mensagem genérica "Procure a recepção" (não revela se o CPF existe) |

## O que a recepção vê

Na Agenda do dia, antes do nome do paciente aparece um selo verde com um ✔ e o horário da chegada. Ao passar o mouse, o selo diz "Chegada registrada no totem às HH:mm". A tela consulta a cada 30 segundos. O totem não faz check-in financeiro nem baixa pagamento: o Check-in da recepção continua normal.


## Gerenciar os totens

Na mesma tela Totem de check-in, a lista Totens autorizados mostra nome, quando foi autorizado, validade e último acesso. O botão Revogar desliga aquele equipamento na hora (ele volta ao QR code). Para parar de usar o totem em toda a clínica, desmarque Ativar o totem nesta clínica e salve.


## Segurança e privacidade

O totem usa uma credencial própria, guardada só como hash, com validade e possibilidade de revogação, que só funciona nas rotas do totem e só para a clínica que o autorizou. A tela nunca mostra o CPF (só o primeiro nome e o horário) e apaga os dados digitados depois da identificação. Há bloqueio por CPF e por totem após erros, com registro de cada tentativa (o CPF é guardado só como código irreversível). Qualquer toque reinicia a contagem de inatividade.

Equipamento recomendado: computador com Chrome ou Edge em modo quiosque (--kiosk --app=https://seu-sistema/totem) ou tablet Android com Fully Kiosk. A credencial fica no navegador do equipamento: limpar os dados do navegador exige autorizar o totem de novo.

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| "Totem desativado. Procure a recepção" | Opção desmarcada na configuração | Marcar Ativar o totem nesta clínica e salvar |
| Volta ao QR de autorização sozinho | Autorização expirada ou revogada | Autorizar de novo (passo 3) |
| Responsável não é reconhecido | Sem data de nascimento, sem CPF, vínculo inativo ou paciente inativo | Completar o cadastro do responsável no paciente |
| Paciente "não encontrado" com dados certos | CPF/nascimento diferentes do cadastro, ou bloqueio temporário | Conferir o cadastro; aguardar o tempo de bloqueio |
| Atendimento não aparece | Fora do dia, desmarcado, ou fora da janela | Conferir a agenda e a janela configurada |
| "Sem conexão" no totem | API indisponível ou rede da portaria | Verificar a rede; a tela tenta de novo sozinha |
| Item "Totem de check-in" não aparece no menu | Usuário não é Administrador | Entrar com perfil Administrador |
