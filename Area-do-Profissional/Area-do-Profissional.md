# Área do Profissional

Este manual explica o que o **profissional de saúde** vê e pode fazer no ClinSis.

O menu do profissional é menor que o do administrador. Algumas opções só aparecem se a clínica ativou o módulo ou a configuração correspondente.

## Menu do profissional

| Opção do menu | Aparece quando |
|---|---|
| Agenda | Módulo Agenda ativo |
| Pacientes | Configuração "Profissional pode ver pacientes" ativa |
| Prontuário | Módulo Prontuário ativo |
| Atendimento (Listar) | Módulo Receituário ativo |
| Atendimento > Pacientes do dia | Módulo Receituário ativo **e** clínica no modelo consultório |
| Protocolo | Módulo Protocolo ativo |
| Perfil | Sempre |
| Home | Sempre |
| Sair | Sempre |

!!! note "Não achou uma opção?"
    Se falta uma opção do menu, o módulo ou a configuração não está ativo na sua clínica. Fale com o administrador.

O profissional **não vê** os menus de Cadastros, Tabelas Auxiliares, Financeiro, Relatórios, Caixa e Doc. Faturamento. Também não vê o link "Documentação" do menu.

---

## Home

**Para que serve:** tela inicial, com atalhos e um resumo do seu dia.

**Como acessar:** clique em **Home** no menu.

### Cartões de atalho

- **Agenda**: lista os dois últimos meses de agenda. Ao lado de cada mês há o botão **Agenda resumida**. Há também o link **Agenda detalhada**, que abre a lista de pacientes do dia.
- **Prontuário**: abre seus prontuários. Tem o link **Textos padrões**. Só aparece com o módulo Prontuário ativo.
- **Protocolo**: só aparece com o módulo Protocolo ativo.
- **Atendimentos**: abre "Pacientes do dia" do consultório. Só aparece se a clínica for consultório.
- **Alterar Perfil**: aparece somente se o seu usuário tem um segundo perfil de acesso.

### Resumo do dia

Faixa com números de hoje. Só aparece se a clínica ativou essa configuração.

- Total de Pacientes
- Total de Presentes
- Relatórios Finalizados
- Relatórios Abertos
- Evoluções Finalizadas
- Evoluções Abertas

Em **Pendências gerais** você vê:

- Evoluções Abertas no Geral
- Relatórios Abertos no Geral

!!! note
    Pendência é algo que você começou e ainda não finalizou.

---

## Agenda

**Para que serve:** ver os meses de agenda e entrar na sua agenda.

**Como acessar:** menu **Agenda**.

**O que você vê:** uma lista de Ano/Mês. Em cada linha, o botão **Acessar** abre a Agenda resumida do mês.

Se a clínica **não** for consultório, aparece o link **Ver lista simples de pacientes do dia**.

!!! warning "O que o profissional não pode"
    Não pode criar nem remover agendas. Não vê os botões Relatório, Prof. horários, Ver Agenda e Divergência Sessões. Esses são do administrador e do atendente.

### Agenda resumida

**Para que serve:** ver seus pacientes agendados no mês.

**Como acessar:** em Agenda, clique em **Acessar**. Ou, na Home, clique em **Agenda resumida**.

**Recursos:**

- **Ver Pacientes / Ver Planilha**: alterna entre a visão por paciente e a visão em tabela.
- **Pacientes do dia**: marque a caixa, informe a data e clique em **Carregar**.
- **Confirmação WhatsApp**: só aparece se o módulo WhatsApp estiver ativo.
- Lista **Meus Pacientes**: aparece só se existirem outros profissionais vinculados como origem de pacientes (a confirmar a regra exata).
- Na tabela: filtros por Dia, Data, Hora e Paciente.
- Um ícone verde ao lado do paciente indica que o prontuário de evolução diária de hoje já foi finalizado.

**Criar prontuário a partir da agenda:** dê dois cliques no paciente (ou clique em **Prontuários**, na visão por paciente).

1. Escolha o **Tipo** de prontuário.
2. Escolha a **Especialidade**.
3. Confirme a inclusão.

!!! warning
    Se a clínica bloqueou a criação de prontuários, nada acontece ao clicar. Para prontuário de evolução diária há uma regra de data (não é permitido para data futura). Detalhes exatos a confirmar.

### Pacientes do dia (Agenda detalhada)

**Como acessar:** link **Agenda detalhada** na Home, ou **Ver lista simples de pacientes do dia** na Agenda.

**O que você vê:** escolha a data e clique em **Pesquisar**. A lista mostra:

- Dia e Hora
- Paciente
- Celular
- Situação da guia
- Operadora
- Programa
- Observação
- Status das sessões S1 a S5

Se a clínica permitir, aparece o botão **Marcar Presença** em cada linha.

---

## Pacientes

**Para que serve:** consultar o cadastro dos pacientes.

**Como acessar:** menu **Pacientes**. Só aparece com a configuração "Profissional pode ver pacientes" ativa. Sem ela, o sistema volta para a Home.

**O que você pode:**

- Ver a lista e abrir o cadastro de um paciente existente.

**O que você NÃO pode:**

- Cadastrar paciente novo. O botão de cadastrar fica oculto.
- Baixar a ficha do paciente. O botão fica oculto.
- Alterar os dados adicionais do paciente. Os campos ficam bloqueados.
- Abrir a tela de cadastro sem escolher um paciente da lista.

!!! note "A confirmar"
    Se outras abas do cadastro do paciente também ficam somente leitura para o profissional.

---

## Prontuário

**Para que serve:** criar, preencher e finalizar prontuários e relatórios dos seus pacientes.

**Como acessar:** menu **Prontuário**. Só aparece com o módulo Prontuário ativo.

### Lista de prontuários

Para ver a lista, use **Pesquisa** e escolha o **Tipo** (obrigatório).

**Filtros:** Nº do prontuário, nome do paciente, emissão (data inicial e final), inclusão (data inicial e final), Finalizado (Todos, Finalizado ou Digitação), Ordenação (mais recentes, paciente, emissão) e Tags (se ativas).

**Colunas:** Nº, Profissional, Paciente, Mãe, Situação, Início, Finalização e Emissão.

- A lista mostra o **seu** profissional automaticamente.
- Uma etiqueta **compartilhado** indica um relatório de outro profissional da mesma especialidade.
- Linhas em cor diferente indicam prontuário atrasado.

**Botões:**

| Botão | O que faz |
|---|---|
| **Novo** | Cria um prontuário (escolhe o paciente). Não aparece se a clínica bloqueou a criação. |
| Olho | Visualiza o prontuário. |
| Bloco amarelo | Abre para preencher. Só nos prontuários que são seus. |
| Lixeira | Exclui. Só prontuário seu que ainda está em **Digitação**. |
| tags | Mostra as tags do prontuário (se ativas). |
| Impressora (rodapé) | Gera o PDF dos prontuários que você marcou. Só dá para marcar os finalizados. |

!!! warning "Não pode"
    Não pode excluir prontuário finalizado nem prontuário de outro profissional. Não pode exportar CSV (é do administrador).

!!! note "Atalho pela notificação"
    Ao abrir pelo aviso de prontuários não finalizados, a lista já vem filtrada em Digitação.

### Preencher o prontuário

1. Abra o prontuário no bloco amarelo.
2. Informe a **Data de emissão**.
3. Responda cada **Alínea** (pergunta). Use **Anterior** e **Próxima** para navegar.
4. Clique em **Salvar**.
5. Quando todas as alíneas estiverem respondidas, clique em **Finalizar**.

**Tipos de resposta:**

- Texto livre (até 50.000 caracteres).
- Sim ou Não.
- Arquivo PDF: envie o arquivo ou visualize o já salvo.

Se houver **Texto Padrão** cadastrado, escolha na lista para inserir.

!!! warning
    Inserir um texto padrão apaga o que você já digitou no campo.

!!! warning
    Depois de **Finalizar**, o prontuário não pode mais ser editado por você. Somente o administrador pode reabrir.

### Visualizar e imprimir

Mostra todas as alíneas. Com o prontuário finalizado, use **Página de impressão / Download**. A tela também tem link para baixar o modelo do formulário, quando existir.

### Textos padrões

**Como acessar:** na Home, cartão Prontuário, link **Textos padrões**.

**Para que serve:** guardar textos que você usa sempre.

**Como usar:**

1. Clique em **Novo**.
2. Escolha o **Tipo de prontuário**.
3. Digite o **Título** (máximo 20 caracteres).
4. Digite o **Texto**.
5. Clique em **Salvar**.

Para mudar, use **Visualizar/Alterar**. Para apagar, use a lixeira. O tipo não pode ser trocado depois de salvo.

---

## Atendimento (receituário)

**Para que serve:** registrar consultas com receita de medicamentos e pedido de exames.

**Como acessar:** menu **Atendimento**. Só aparece com o módulo Receituário ativo.

### Atendimento > Listar

Mostra **seus** atendimentos.

**Filtros:** paciente, data inicial e final, e "Filtrar atendimentos do dia atual".

**Botões por linha:**

- **Finalizar Atendimento** (só se ainda não finalizado).
- **Visualizar**: abre o atendimento.
- **Imp. Completo**, **Imp. Exames** e **Imp. Medicamentos**.

### Ficha do atendimento

- **Novo Medicamento** e **Novo Exame**.
- **Anamnese** (preenchimento pelo prontuário).
- **Observação** (opcional).

Depois de finalizado, a ficha fica somente para leitura.

### Atendimento > Pacientes do dia

**Como acessar:** menu **Atendimento > Pacientes do dia**, ou cartão **Atendimentos** na Home. Só para clínica no modelo consultório.

**O que você vê:** Paciente, Data, Horário e se está Finalizado.

- **Atendimento**: abre a ficha (ou dois cliques na linha).
- **Finalizar Atendimento**.
- **Ver últimos atendimentos**: abre a lista de atendimentos do paciente em outra aba.

!!! note "A confirmar"
    A tela também abre para a clínica de código 1 mesmo sem ser consultório, mas o menu só mostra a opção para consultório.

---

## Protocolo

**Para que serve:** registrar e acompanhar solicitações com prazo, entre pessoas da clínica.

**Como acessar:** menu **Protocolo**. Só aparece com o módulo Protocolo ativo.

**Lista:** Protocolo, data de alteração, data limite, solicitante, usuário e profissional destinatários, tipo, status, prazo em dias, atendido e data de finalização.

**Filtros:** tipo, status, solicitante, destinatário, atendido e período de inclusão.

**Novo protocolo:** botão **Novo**. Campos: Tipo, Situação, Data Limite, Prazo de entrega (dias), Solicitante, Usuário destinatário, Profissional destinatário e Data do atendimento.

!!! note "A confirmar"
    Regras de quem pode alterar ou finalizar um protocolo. Há também o botão **Exportar CSV** na lista (a confirmar se está liberado para o profissional).

---

## Perfil

**Para que serve:** cuidar dos dados da sua conta.

**Como acessar:** menu **Perfil**.

**O que você vê:** seu nome, e-mail, situação (Ativo ou Inativo), perfil de acesso e data de cadastro.

### Alterar dados

Altere Nome, E-mail e Data de nascimento. Digite sua senha para confirmar.

### Alterar senha

Informe a senha atual, a nova senha e repita a nova senha.

---

## Resumo do que o profissional não faz

- Não cria nem remove agendas.
- Não cadastra pacientes.
- Não exclui prontuário finalizado nem de outro profissional.
- Não reabre prontuário finalizado.
- Não acessa Financeiro, Relatórios, Caixa, Doc. Faturamento nem Tabelas Auxiliares.
