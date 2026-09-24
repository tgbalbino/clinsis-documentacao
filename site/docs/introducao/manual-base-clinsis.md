# Manual Base do ClinSis

_O que é o sistema, o fluxo geral, os cadastros, a criação da agenda e as impressões_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Manual-Base-ClinSis/Documentacao_Manual_Base_ClinSis_Simplificado.pdf)

## Vídeo narrado

- [▶️ Assistir o vídeo no YouTube](https://youtu.be/r7iJc03azkw)

## Conteúdo completo do manual

*As capturas de tela deste trecho estão no PDF acima — aqui fica só o texto.*

---


_O que é o sistema, o fluxo geral, os cadastros, a criação da agenda e as impressões_

Versão 1.0 — 23/09/2026

Este é o manual de entrada do ClinSis. Ele explica, em linguagem simples, o que o sistema faz, como as partes se encaixam (Cadastros → Agenda → Atendimento/Prontuário → Financeiro), quais cadastros precisam existir antes de agendar, como criar a agenda do mês, como configurar os horários e agendar pacientes, e para que serve cada impressão da agenda.

Assista ao vídeo narrado desta rotina: [https://youtu.be/r7iJc03azkw](https://youtu.be/r7iJc03azkw)

---

# 1. O que é o ClinSis

O ClinSis é um sistema web de gestão para clínicas de atendimento em saúde (fisioterapia, fonoaudiologia, psicologia, nutrição, terapia ocupacional e outras). Ele reúne, num só lugar, o que a clínica faz todos os dias: cadastrar pacientes e profissionais, montar a agenda mensal, registrar o atendimento e o prontuário, faturar convênios e controlar o dinheiro que entra e sai.

Funciona pelo navegador (computador, tablet ou celular), sem instalar nada. Cada clínica tem os seus próprios dados, e cada pessoa da equipe entra com o seu login e enxerga só o que o seu perfil permite.


## Objetivos do sistema

| Objetivo | Como o ClinSis ajuda |
|---|---|
| Organizar a agenda | Agenda mensal por profissional, com horários, pacientes vinculados e controle de presença sessão a sessão. |
| Centralizar o cadastro | Um só cadastro de pacientes, profissionais, convênios (operadoras) e usuários, sem planilhas paralelas. |
| Registrar o atendimento | Prontuário do paciente feito pelo profissional, com modelos (tipos e alíneas) definidos pela clínica. |
| Controlar o financeiro | Contas a Receber (pacientes e convênios), Contas a Pagar (profissionais e despesas), Caixa, Fluxo de Caixa e Dashboard. |
| Dar visibilidade | Relatórios e dashboards de agenda, presença, produção e faturamento para a gestão decidir com números. |
| Controlar quem faz o quê | Perfis de acesso (Administrador, Atendente, Profissional), setores e permissões extras por usuário. |

## Funcionalidades base (menu lateral)

| Menu | Para que serve |
|---|---|
| Cadastros | Acessos, Clínica, Setores, Medicação, Exame, Paciente, Profissional, Operadora, Fornecedor e Pessoa. |
| Agenda | Criar a agenda do mês, definir os horários dos profissionais e agendar pacientes. |
| Dashboard Agenda | Painel gerencial com cartões, gráficos e tabelas da agenda (ocupação, presença, faturamento por convênio). |
| Atendimento | Lista dos atendimentos realizados pelos profissionais. |
| Prontuário | Tipos e alíneas (modelos), prontuário do profissional e prontuários por paciente. |
| Contrato | Contratos de atendimento com pacientes, inclusive com assinatura eletrônica (D4Sign). |
| Doc. Faturamento | Guias/documentos de faturamento de convênios e relatório de faturamento. |
| Caixa | Abertura e fechamento de caixa, solicitações de cancelamento e histórico. |
| Protocolo | Protocolos de atendimento (módulo opcional da clínica). |
| Tabelas Aux. | Configurações: Horários, Especialidade, Feriados, Formas de Pagamento, Tabelas de Preço, Parâmetros, Layout de Contrato, entre outras. |
| Relatórios | Relatórios de Cobrança, Paciente, Agenda, Prontuário, Pagamentos e Contratos. |
| Financeiro | Contas a Pagar, Contas a Receber, Movimentos Financeiros, Plano de Contas, Centro de Custos, Contas Financeiras, Dashboard e Fluxo de Caixa. |

> ⚠️ Alguns módulos (Contrato, Doc. Faturamento, Caixa, Protocolo, Check-In) são opcionais e só aparecem para clínicas que os contrataram/ativaram.

## Perfis de acesso

Cada usuário tem um perfil principal e, se necessário, um perfil secundário:

| Perfil | O que faz |
|---|---|
| Administrador | Acesso total: cadastros, configurações, acessos, agenda, financeiro e relatórios. |
| Atendente | Rotina da recepção: cadastros de pacientes, agenda e agendamentos, guias/faturamento e caixa. |
| Profissional | Vê a própria agenda e pacientes do dia, registra sessões e faz os prontuários. |

> ⚠️ Regra do sistema: um usuário não pode ter Administrador + Atendente ao mesmo tempo. Combinações com Profissional (ex.: Atendente + Profissional) são permitidas.

# 2. Fluxo geral do sistema

Tudo no ClinSis segue uma ordem natural. Cada etapa depende da anterior:


| Etapa | O que acontece |
|---|---|
| 1. Cadastros | Cadastra-se a clínica, os setores, as especialidades, os profissionais, os pacientes, os convênios e os acessos (logins) da equipe. |
| 2. Agenda | Cria-se a agenda do mês, definem-se os horários de cada profissional e vinculam-se os pacientes aos horários. |
| 3. Atendimento e Prontuário | A cada sessão marca-se presença ou ausência; o profissional registra o prontuário do paciente. |
| 4. Contas a Receber | O atendimento gera cobrança: pelo Check-in (particular), pela Cobrança de Paciente ou pelo faturamento de convênio. Cada cobrança vira uma Conta a Receber, que é baixada quando o pagamento entra. |
| 4. Contas a Pagar | O que a clínica deve pagar — despesas, fornecedores e o pagamento dos profissionais calculado a partir das sessões realizadas — vira Conta a Pagar, baixada quando é paga. |



Cada uma dessas rotinas financeiras e clínicas tem manual próprio nesta mesma biblioteca de documentação (Contas a Receber, Contas a Pagar, Checkin, Pagamento de Profissionais, Módulo de Caixa e outros). Este manual foca na base: Cadastros → Agenda.

# 3. Cadastros principais para a agenda

Antes de criar qualquer agenda, é preciso que estes cadastros existam. A ordem abaixo evita retrabalho, pois um depende do outro:

| Ordem | Cadastro | Menu | Por que é necessário |
|---|---|
| 1 | Clínica | Cadastros → Clínica | Dados da clínica (endereço, contato, responsável) e contadores de pacientes, profissionais e acessos. |
| 2 | Setores | Cadastros → Setores | Áreas da equipe (ex.: Recepção, Contabilidade). Usado ao criar o acesso de cada usuário. |
| 3 | Especialidades | Tabelas Aux. → Especialidade | Tipos de atendimento (Fisioterapia, Psicologia…). Cada agendamento tem uma especialidade. |
| 4 | Operadoras (convênios) | Cadastros → Operadora | Convênios/planos atendidos. Um atendimento é Particular ou vinculado a um plano. |
| 5 | Profissionais | Cadastros → Profissional | Quem atende. Só profissionais cadastrados podem ter horários na agenda. |
| 6 | Pacientes | Cadastros → Paciente | Quem é atendido. Só pacientes cadastrados podem ser vinculados a um horário. |
| 7 | Horários | Tabelas Aux. → Horários | Lista de horários que a clínica trabalha (07:00, 07:30…). Base para os horários de cada profissional. |
| 8 | Acessos | Cadastros → Acessos | Logins da equipe (Atendente, Profissional), com perfil e setor. |

## Clínica

Mostra os totais da clínica — pacientes, profissionais e acessos, ativos e inativos — e permite editar endereço, contato e o responsável (usado na geração de contratos). Também há o atalho Gerenciar imagens da clínica.


## Setores

Lista simples de setores (Financeiro, Contabilidade, Recepção…). Um setor pode ser ativado ou desativado. Ele é escolhido ao dar acesso a um usuário.


## Especialidades

Define os tipos de atendimento da clínica. Cada especialidade tem descrição, abreviação (que aparece na agenda, ex.: FONO), Tipo de Cobrança (Por Sessão ou Paciente) e Relatório Compartilhado (Prontuários), que controla se um profissional enxerga o prontuário finalizado de um colega. Os detalhes estão no manual "Cadastro de Especialidades".


## Profissionais

O cadastro do profissional reúne CPF, nome, data de nascimento, Locação, Nome Agenda (o nome curto que aparece na grade da agenda), registro profissional (conselho), endereço, contatos e se é estagiário. Os campos marcados com * são obrigatórios. O profissional pode ser ativado ou inativado (menu Profissional → Inativação).


## Pacientes

O cadastro do paciente pede CPF, titular, nome, data de nascimento, sexo, mãe, pai, estado civil, endereço e celular (campos com *), além de dados opcionais como RG, CPS (carteira do convênio), indicação médica, doença/alergia e responsável, com anexo de laudo. Depois de cadastrado, o paciente pode ser vinculado a horários da agenda. No menu Paciente também existem Entrada e Saída (registro do tipo, data e motivo da entrada ou saída do paciente no tratamento) e Inativação.


## Operadoras (convênios)

Cadastro dos convênios/planos atendidos pela clínica. No agendamento, o paciente atendido por convênio (Atendimento Particular = Não) é vinculado a uma operadora; o atendimento "PROPRIO" representa o particular. O submenu tem Listar, Cadastro e a relação de pacientes por operadora.


# 4. Cadastro de Acesso (usuários do sistema)

O acesso é o login de quem usa o sistema. Fica em Cadastros → Acessos e só é visível para o Administrador. A lista mostra, para cada usuário: se está ativo, nome, e-mail, data de cadastro, perfil, perfil secundário, setor e se controla caixa.


## Criando um novo acesso

Clique em Novo e informe o CPF da pessoa:


| Situação | O que o sistema faz |
|---|---|
| A pessoa já tem usuário no ClinSis | Pergunta "Deseja permitir acesso a ?". Escolha o Perfil (Atendente ou Profissional) e o Setor e confirme em "Sim, Permitir acesso". O login existente passa a valer também para esta clínica. |
| A pessoa ainda não tem usuário | Abre o formulário de criação: Login, E-mail, Nome, Perfil (Atendente ou Profissional) e Setor. Ao salvar, o usuário é criado com a senha padrão do sistema. |

> ⚠️ O perfil Administrador não é escolhido na criação; ele é definido depois, pela opção Editar do usuário.

## Gerenciando um acesso existente

Na coluna de ações (botão de engrenagem) de cada usuário há:


| Opção | Para que serve |
|---|---|
| Editar | Altera Perfil, Perfil Secundário, Setor e liga/desliga Controla Caixa (exige caixa aberto para o usuário lançar baixas). |
| Desativar / Ativar | Bloqueia ou libera o acesso do usuário à clínica, sem apagar o histórico. |
| Permissões | Permissões extras por usuário. Hoje existe "Permite gerenciar acessos", que libera a tela de Acessos para quem não é administrador. |
| bloquear dias | Define em quais dias da semana o usuário pode entrar (marque só os dias permitidos). |
| Resetar para senha padrão | Devolve a senha ao padrão do sistema, útil quando o usuário esquece a própria. |
| Log de acessos (botão no topo) | Histórico de quando cada usuário entrou no sistema. |




# 5. Criação da agenda

A agenda do ClinSis é mensal: existe uma agenda para cada mês/ano. Ela fica em Agenda no menu. A lista mostra todas as agendas criadas, da mais recente para a mais antiga, e cada uma tem os botões abaixo.


| Botão | Função |
|---|---|
| Relatório | Resumo do mês: quantidade de agendamentos, pacientes, sessões, presentes, ausentes e desmarcações. |
| Prof. horários | Define os horários de cada profissional naquele mês. |
| Ver Agenda | Abre a grade de agendamento (onde os pacientes são vinculados e as sessões marcadas). |
| Divergência Sessões | Lista os agendamentos cuja quantidade de Sessões difere das Sessões Esperadas do mês (quantas vezes o dia da semana acontece) e permite Ajustar, um a um ou em lote. |
| Lixeira (vermelho) | Remove a agenda do mês. |
| Remoção Rápida de Pacientes (link no topo) | Atalho para remover pacientes da agenda em lote. |

## Passo a passo: criar a agenda do mês

1. Clique em Novo. 2. Escolha o Mês e o Ano. 3. Se quiser aproveitar o mês anterior, marque Copiar agenda anterior e escolha qual agenda será clonada. 4. Clique em Salvar.


> ⚠️ Se a agenda escolhida não for a do mês corrente, o sistema pede uma confirmação extra. E só pode existir uma agenda por mês/ano: tentar criar de novo mostra a mensagem "Já existe uma agenda criada para (mês/ano)".

## Criar do zero ou copiar a anterior?

| Opção | O que acontece |
|---|---|
| Sem copiar | A agenda nasce vazia: é preciso definir os horários dos profissionais e vincular os pacientes. |
| Copiar agenda anterior | O sistema copia para o novo mês os horários dos profissionais e os pacientes já vinculados a eles. Os status das sessões (presente/ausente…) e as datas das sessões são zerados, pois o mês novo ainda não aconteceu. |

> ⚠️ Copiar a agenda anterior é o caminho mais rápido na rotina: os pacientes fixos continuam nos mesmos dias e horários, e você só ajusta as exceções.

# 6. Parametrização de horários

Há dois níveis de horários, e é importante não confundir:

| Nível | Onde |
|---|---|
| Horários da clínica | Tabelas Aux. → Horários |
| Horários do profissional | Agenda → Prof. horários |

## Horários da clínica (Tabelas Aux. → Horários)

Cada horário tem uma Situação (Ativo/Inativo) e um botão para ativar ou desativar. Só horários ativos aparecem na hora de montar a agenda do profissional. Há duas formas de cadastrar:


| Forma | Como usar |
|---|---|
| Novo (um a um) | Digite o horário no formato 00:00 (ex.: 08:30) e clique em Novo. |
| Gerar Horários (em lote) | Informe Horário Início, Horário Fim e o Intervalo (de 5 em 5 até de 50 em 50 minutos). O sistema cria todos os horários do período. |


## Horários do profissional (Agenda → Prof. horários)

Depois de criada a agenda do mês, clique em Prof. horários nela. A tela "Profissional Agenda" permite montar a grade de cada profissional.

1. Escolha o profissional (pela lista ou em "buscar profissional"). 2. Se a clínica trabalha com os dois formatos, escolha o Formato: SEMANAL (um dia da semana, que se repete o mês inteiro) ou DATA (um dia específico). 3. Marque o Dia (ou a Data). 4. Marque os Horários desejados (ou "Marcar todos"). 5. Clique em Incluir. Repita para os outros dias.


| Recurso | Para que serve |
|---|---|
| Manter Marcação | Ao incluir, mantém os horários marcados na tela, para repetir a mesma seleção em outro dia sem remarcar tudo. |
| Transferir horários/agenda para outro profissional | Passa a agenda deste profissional (horários e pacientes) para outro. Útil quando um profissional sai. |
| Clonar horários para outro profissional | Copia os horários deste profissional para outro, sem tirar do original. |
| Remover Todos os Horários deste profissional | Limpa toda a grade do profissional no mês. |
| Remover (caixas + lixeira) | Marque as linhas da tabela e use a lixeira para remover horários específicos. |

> ⚠️ Sem horários de profissional definidos, a grade de agendamento fica vazia: não há onde vincular pacientes.

# 7. Agendamento de pacientes

Com a agenda criada e os horários dos profissionais definidos, o agendamento é feito em Agenda → Ver Agenda (ou pelo botão Agendamento dentro de Prof. horários). A tela é uma grade: cada linha é um horário de um profissional em um dia da semana ou data.


As linhas em branco com o botão verde (+) são horários vagos. As linhas com o botão azul de engrenagem já têm paciente. A cor da linha pode indicar a situação da guia de faturamento. Use "Somente vagos" para listar apenas os horários livres.

## Como agendar um paciente

1. Na linha vaga, clique no botão verde (+). 2. Em "Vincular Paciente" pesquise pelo nome e selecione o paciente. 3. Preencha o formulário e clique em Salvar.



| Campo | O que informar |
|---|---|
| Atendimento Particular? * | Sim = paciente particular. Não = atendido por convênio; nesse caso aparecem também Plano (operadora), Cooparticipativo e Nº Doc Faturamento (guia). |
| Sessões * | Quantas sessões o paciente tem naquele horário no mês (a agenda tem até 5 colunas de sessão: Sessão 1 a Sessão 5, uma por ocorrência do dia da semana no mês). |
| Forma Atendimento * | Presencial ou Online. |
| Especialidade * | A especialidade do atendimento (ex.: FONO, PSICO). |
| Tipo Marcação * | NI (não informado), Avaliação ou Consulta/Sessão. |
| Método * e Programa * | Método terapêutico e programa/agrupamento definidos nas tabelas auxiliares da clínica. |
| Data Entrada | Data em que o paciente começou nesse horário. |
| Observação | Texto livre. Uma linha com observação mostra um ícone de comentário para leitura rápida. |

> ⚠️ Os campos marcados com * são obrigatórios. Para vincular mais de um paciente ao mesmo horário (por exemplo, atendimento em grupo), use Adicionar mais na linha.

## Ações sobre um agendamento existente

O botão de engrenagem de cada linha abre o menu de ações:


| Ação | Para que serve |
|---|---|
| Editar | Corrige os dados do agendamento (sessões, plano, especialidade, observação…). |
| Sessão | Marca o resultado de uma sessão (ex.: Presente, Ausente) no dia em que ela acontece. Abre a janela "Marcar Sessão" para escolher qual sessão (1 a 5). |
| Adicionar mais | Vincula outro paciente ao mesmo horário do profissional. |
| Desmarcar | Remove o paciente daquele horário (pede confirmação antes). |
| Entrada / Saída | Registra a entrada ou a saída do paciente no tratamento (tipo, data e motivo). |
| Trocar Profissional | Passa o paciente para outro profissional. |
| Horários Pac. | Gera o PDF com todos os horários do paciente no mês (veja a seção de impressões). |


> ⚠️ Também é possível marcar a sessão com duplo clique na célula da coluna Sessão 1…5 da linha do paciente.

## Ferramentas da tela de agendamento

| Botão | Função |
|---|---|
| Filtros | Filtra a grade por data, paciente, dias, profissionais, quantidade de sessões, método, cooparticipativo, particular e pelo status de cada sessão. |
| Relatórios | Abre a janela das impressões do dia (veja a seção 8). |
| Exportar | Exporta a agenda para arquivo CSV (planilha): com os filtros aplicados ou a agenda inteira. |
| Pesquisa rápida | Encontra rapidamente um profissional ou paciente na agenda. |
| Colunas | Escolhe quais colunas ficam visíveis na grade; a escolha fica salva para o usuário. |
| Somente vagos | Mostra só os horários sem paciente. |
| Anterior / Próxima agenda | Setas para navegar entre os meses. |


# 8. Impressões da agenda e seus objetivos

O ClinSis oferece impressões/relatórios da agenda para situações diferentes do dia a dia. A tabela resume qual usar em cada caso:

| Impressão | Onde encontrar |
|---|---|
| Atendimento Diário (PDF) | Ver Agenda → Relatórios |
| Marcação - Presença/Ausência (PDF) | Ver Agenda → Relatórios |
| Marcação sessão dia (tela) | Ver Agenda → Relatórios |
| Horários do paciente (PDF) | Ver Agenda → engrenagem da linha → Horários Pac. |
| Exportar agenda (CSV) | Ver Agenda → Exportar |
| Relatório da Agenda (tela) | Agenda → Relatório (na linha do mês) |
| Relatórios de Agenda (menu Relatórios) | Relatórios → Agenda |

## Relatórios do dia (Ver Agenda → Relatórios)

Escolha a data (dentro do mês da agenda) e o tipo: "Atendimento Diário", "Marcação - Presença/Ausência" ou "Marcação sessão dia". Os dois primeiros baixam um PDF; o terceiro abre na tela (botão Visualizar).


## Atendimento Diário

Mostra o dia da semana escolhido (ex.: QUARTA-FEIRA 23/09/2026) e, para cada profissional, os pacientes por horário, com colunas para assinatura do responsável e convênio e uma linha final ASSINATURA DO PROFISSIONAL. É a folha de presença impressa da recepção.


## Marcação - Presença/Ausência

Lista as sessões marcadas na data escolhida, com sessão, profissional, paciente, mãe e o status (PRESENTE, AUSENTE…).


## Marcação sessão dia (na tela)

Mostra data/hora em que cada marcação foi feita, profissional, paciente, usuário que marcou, status e data da sessão, com o total por status no rodapé. Ajuda a saber quem registrou o quê.


## Horários do paciente

Impressão individual: mês/ano, clínica, nome do paciente, usuário que gerou e a lista de dias da semana com horário e profissional. É o "comprovante" dos dias e horários do paciente.


## Relatório da Agenda e relatórios no menu Relatórios




> ⚠️ A Lista simples de pacientes do dia (link na tela Agenda) existe para o perfil Profissional e mostra somente os pacientes do próprio profissional naquele dia.

# 9. Resumo: da implantação ao primeiro agendamento

| Passo | Ação |
|---|---|
| 1 | Conferir os dados da clínica |
| 2 | Cadastrar setores |
| 3 | Cadastrar especialidades e operadoras |
| 4 | Cadastrar profissionais e pacientes |
| 5 | Cadastrar os horários da clínica |
| 6 | Criar os acessos da equipe |
| 7 | Criar a agenda do mês |
| 8 | Definir os horários de cada profissional |
| 9 | Vincular os pacientes aos horários |
| 10 | Marcar presença/ausência a cada sessão |
| 11 | Imprimir/conferir |

> ⚠️ A partir do segundo mês, o caminho é bem mais curto: criar a agenda copiando a anterior (passo 7 com "Copiar agenda anterior") já traz horários e pacientes. Só é preciso ajustar as exceções.
