# Área do Profissional

_O que o profissional de saúde vê e pode fazer no ClinSis_

Versão 1.0 — 24/09/2026

Este manual mostra, passo a passo, o dia a dia do profissional de saúde no ClinSis: a Home, a agenda e os pacientes do dia, os pacientes, os prontuários e relatórios, os textos padrões, o atendimento, o protocolo e o perfil. O menu do profissional é menor que o do administrador, e algumas opções só aparecem se a clínica ativou o módulo correspondente.

Vídeo narrado desta rotina: `video-area-do-profissional-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

# 1. Menu e Home do profissional

O menu do profissional é menor que o do administrador. Algumas opções só aparecem se a clínica ativou o módulo ou a configuração correspondente.

| Opção do menu | Aparece quando |
|---|---|
| Agenda | Módulo Agenda ativo |
| Pacientes | Configuração "Profissional pode ver pacientes" ativa |
| Prontuário | Módulo Prontuário ativo |
| Atendimento (Listar) | Módulo Receituário ativo |
| Atendimento > Pacientes do dia | Módulo Receituário ativo e clínica no modelo consultório |
| Protocolo | Módulo Protocolo ativo |
| Perfil, Home e Sair | Sempre |

> ⚠️ Se falta uma opção no menu, o módulo ou a configuração não está ativo na sua clínica. Fale com o administrador. O profissional não vê os menus de Cadastros, Tabelas Auxiliares, Financeiro, Relatórios, Caixa e Doc. Faturamento.

![Home do profissional: cartões de atalho (Agenda, Prontuário, Protocolo, Atendimentos), resumo do dia e pendências gerais.](p01-home.png)

_Home do profissional: cartões de atalho (Agenda, Prontuário, Protocolo, Atendimentos), resumo do dia e pendências gerais._

## Cartões de atalho

| Cartão | O que faz |
|---|---|
| Agenda | Lista os dois últimos meses de agenda, cada um com o botão Agenda resumida. O link Agenda detalhada abre a lista de pacientes do dia. |
| Prontuário | Abre seus prontuários e tem o link Textos padrões. Só aparece com o módulo Prontuário ativo. |
| Protocolo | Só aparece com o módulo Protocolo ativo. |
| Atendimentos | Abre "Pacientes do dia" do consultório. Só aparece se a clínica for consultório. |
| Alterar Perfil | Só aparece se o seu usuário tem um segundo perfil de acesso. |

## Resumo do dia e pendências

Se a clínica ativou essa configuração, aparece uma faixa com os números de hoje: Total de Pacientes, Total de Presentes, Relatórios Finalizados, Relatórios Abertos, Evoluções Finalizadas e Evoluções Abertas. Em Pendências gerais você vê as Evoluções Abertas e os Relatórios Abertos no geral. Pendência é algo que você começou e ainda não finalizou.

# 2. Agenda

Menu Agenda: lista de Ano/Mês. Em cada linha, o botão Acessar abre a Agenda resumida do mês. Se a clínica não for consultório, aparece também o link Ver lista simples de pacientes do dia.

![Menu Agenda do profissional: só o botão Acessar por mês.](p02-agenda.png)

_Menu Agenda do profissional: só o botão Acessar por mês._

> ⚠️ O profissional não pode criar nem remover agendas, e não vê os botões Relatório, Prof. horários, Ver Agenda e Divergência Sessões. Esses são do administrador e do atendente.

## Agenda resumida

Mostra os seus pacientes agendados no mês. Recursos:

| Recurso | Como usar |
|---|---|
| Ver Pacientes / Ver Planilha | Alterna entre a visão por paciente e a visão em tabela. |
| Pacientes do dia | Marque a caixa, informe a data e clique em Carregar. |
| Confirmação WhatsApp | Só aparece se o módulo WhatsApp estiver ativo. |
| Filtros da tabela | Filtre por Dia, Data, Hora e Paciente. |
| Ícone verde ao lado do paciente | Indica que o prontuário de evolução diária de hoje já foi finalizado. |

![Agenda resumida do mês: dia, hora e paciente de cada horário.](p03-agenda-resumida.png)

_Agenda resumida do mês: dia, hora e paciente de cada horário._

Criar prontuário a partir da agenda: dê dois cliques no paciente (ou clique em Prontuários, na visão por paciente), escolha o Tipo de prontuário, a Especialidade e confirme a inclusão.

> ⚠️ Se a clínica bloqueou a criação de prontuários, nada acontece ao clicar. Para prontuário de evolução diária, não é permitido usar data futura.

## Pacientes do dia (Agenda detalhada)

Acesse pelo link Agenda detalhada da Home, ou Ver lista simples de pacientes do dia na Agenda. Escolha a data e clique em Pesquisar. A lista mostra dia, hora, paciente, celular, situação da guia, operadora, programa, observação e o status das sessões S1 a S5. Se a clínica permitir, aparece o botão Marcar Presença em cada linha.

![Pacientes por Dia: lista do dia com status das sessões e o botão Marcar Presença.](p03b-pacientes-dia.png)

_Pacientes por Dia: lista do dia com status das sessões e o botão Marcar Presença._

# 3. Pacientes

Menu Pacientes, só com a configuração "Profissional pode ver pacientes" ativa. Sem ela, o sistema volta para a Home. O profissional pode ver a lista e abrir o cadastro de um paciente existente.

![Lista de pacientes (dados ocultados neste manual).](p04-pacientes.png)

_Lista de pacientes (dados ocultados neste manual)._

| O profissional NÃO pode | Detalhe |
|---|---|
| Cadastrar paciente novo | O botão de cadastrar fica oculto. |
| Baixar a ficha do paciente | O botão fica oculto. |
| Alterar os dados adicionais | Os campos ficam bloqueados. |
| Abrir o cadastro sem escolher paciente | É preciso abrir a partir da lista. |

# 4. Prontuário

Menu Prontuário (com o módulo Prontuário ativo): criar, preencher e finalizar prontuários e relatórios dos seus pacientes.

## Lista de prontuários

Para ver a lista, use Pesquisa e escolha o Tipo (obrigatório). Filtros: Nº do prontuário, nome do paciente, emissão e inclusão (data inicial e final), Finalizado (Todos, Finalizado ou Digitação), Ordenação e Tags (se ativas).

![Filtro de prontuários: o Tipo é obrigatório.](p05-prontuarios-filtro.png)

_Filtro de prontuários: o Tipo é obrigatório._

A lista mostra automaticamente o seu profissional, com as colunas Nº, Profissional, Paciente, Mãe, Situação, Início, Finalização e Emissão. Uma etiqueta compartilhado indica um relatório de outro profissional da mesma especialidade; linhas em cor diferente indicam prontuário atrasado.

![Lista de prontuários do tipo Evolução diária, com Situação Finalizada ou Digitação.](p05b-prontuarios-lista.png)

_Lista de prontuários do tipo Evolução diária, com Situação Finalizada ou Digitação._

| Botão | O que faz |
|---|---|
| Novo | Cria um prontuário (escolhe o paciente). Não aparece se a clínica bloqueou a criação. |
| Olho | Visualiza o prontuário. |
| Bloco amarelo | Abre para preencher. Só nos prontuários que são seus. |
| Lixeira | Exclui. Só prontuário seu que ainda está em Digitação, com confirmação. |
| tags | Mostra as tags do prontuário (se ativas). |
| Impressora (rodapé) | Gera o PDF dos prontuários marcados. Só é possível marcar os finalizados. |

![Novo prontuário: escolha o paciente (da agenda atual ou por dados) e a especialidade.](p05c-prontuario-novo.png)

_Novo prontuário: escolha o paciente (da agenda atual ou por dados) e a especialidade._

> ⚠️ O profissional não pode excluir prontuário finalizado nem de outro profissional, e não exporta CSV (isso é do administrador).

## Preencher o prontuário

1. Abra o prontuário no bloco amarelo. 2. Informe a Data de emissão. 3. Responda cada Alínea (pergunta), usando Anterior e Próxima. 4. Clique em Salvar. 5. Com todas as alíneas respondidas, clique em Finalizar.

![Preenchimento do prontuário: data de emissão, tags, alínea, texto e os botões Salvar e Finalizar.](p06c-prontuario-preencher.png)

_Preenchimento do prontuário: data de emissão, tags, alínea, texto e os botões Salvar e Finalizar._

| Tipo de resposta | Como funciona |
|---|---|
| Texto livre | Até 50.000 caracteres. |
| Sim ou Não | Marque a opção. |
| Arquivo PDF | Envie o arquivo ou visualize o já salvo. |
| Texto Padrão | Escolha o texto na lista para inserir. |

> ⚠️ Inserir um texto padrão apaga o que você já digitou no campo. E, depois de Finalizar, o prontuário não pode mais ser editado por você: somente o administrador pode reabrir.

## Visualizar e imprimir

A visualização mostra todas as alíneas. Com o prontuário finalizado, use Página de impressão / Download.

![Prontuário finalizado em modo de visualização.](p06-prontuario-visualizar.png)

_Prontuário finalizado em modo de visualização._

## Textos padrões

Na Home, no cartão Prontuário, o link Textos padrões guarda textos que você usa sempre. Clique em Novo, escolha o Tipo de prontuário, digite o Título (máximo de 20 caracteres) e o Texto, e clique em Salvar. Para mudar, use Visualizar/Alterar; para apagar, a lixeira. O tipo não pode ser trocado depois de salvo.

![Lista de textos padrões por tipo de prontuário.](p07-textos-padrao.png)

_Lista de textos padrões por tipo de prontuário._

![Novo texto padrão: tipo, título e texto.](p07b-texto-padrao-novo.png)

_Novo texto padrão: tipo, título e texto._

# 5. Atendimento (receituário)

Menu Atendimento, com o módulo Receituário ativo: registra consultas com receita de medicamentos e pedido de exames. Em Atendimento > Listar aparecem os seus atendimentos, com filtros por paciente, data inicial e final e "Filtrar atendimentos do dia atual".

![Atendimentos: lista com Profissional, Paciente, Data, Horário e Finalizado.](p08-atendimento.png)

_Atendimentos: lista com Profissional, Paciente, Data, Horário e Finalizado._

| Botão por linha | O que faz |
|---|---|
| Finalizar Atendimento | Só aparece se o atendimento ainda não foi finalizado. |
| Visualizar | Abre o atendimento. |
| Imp. Completo, Imp. Exames e Imp. Medicamentos | Imprimem o atendimento inteiro ou só exames ou só medicamentos. |

Na ficha do atendimento há Novo Medicamento, Novo Exame, Anamnese (preenchimento pelo prontuário) e Observação (opcional). Depois de finalizado, a ficha fica somente para leitura.

Atendimento > Pacientes do dia (clínica no modelo consultório): mostra Paciente, Data, Horário e se está Finalizado. Use Atendimento para abrir a ficha (ou dois cliques na linha), Finalizar Atendimento e Ver últimos atendimentos.

# 6. Protocolo

Menu Protocolo (com o módulo Protocolo ativo): registrar e acompanhar solicitações com prazo, entre pessoas da clínica.

![Lista de protocolos: datas, solicitante, destinatários, tipo, status, prazo e atendido.](p09-protocolo.png)

_Lista de protocolos: datas, solicitante, destinatários, tipo, status, prazo e atendido._

A lista tem protocolo, data de alteração, data limite, solicitante, usuário e profissional destinatários, tipo, status, prazo em dias, atendido e data de finalização. Filtre por tipo, status, solicitante, destinatário, atendido e período de inclusão. Para criar, clique em Novo e informe Tipo, Situação, Data Limite, Prazo de entrega (dias), Solicitante, Usuário destinatário, Profissional destinatário e Data do atendimento.

# 7. Perfil

Menu Perfil: cuidar dos dados da sua conta. Mostra nome, e-mail, situação (Ativo ou Inativo), perfil de acesso e data de cadastro.

![Perfil: dados da conta (e-mail ocultado neste manual) e as opções Alterar Dados e Alterar Senha.](p10-perfil.png)

_Perfil: dados da conta (e-mail ocultado neste manual) e as opções Alterar Dados e Alterar Senha._

| Opção | Como usar |
|---|---|
| Alterar Dados | Altere Nome, E-mail e Data de nascimento. Digite sua senha para confirmar. |
| Alterar Senha | Informe a senha atual, a nova senha e repita a nova senha. |

# 8. Resumo: o que o profissional não faz

| Não faz | Quem faz |
|---|---|
| Criar ou remover agendas | Administrador / Atendente |
| Cadastrar pacientes | Administrador / Atendente |
| Excluir prontuário finalizado ou de outro profissional | Ninguém pelo profissional; só exclui o próprio prontuário em Digitação |
| Reabrir prontuário finalizado | Administrador |
| Acessar Financeiro, Relatórios, Caixa, Doc. Faturamento e Tabelas Auxiliares | Administrador / Atendente |
