# Prontuário — Uso pelo Profissional

_Criar, preencher, finalizar, consultar e imprimir prontuários_

Versão 1.0 — 23/09/2026

Este manual mostra o dia a dia do prontuário para o profissional: como criar um prontuário para um paciente da agenda, preencher as alíneas, usar textos padrão e tags, finalizar, consultar, imprimir em PDF e excluir um rascunho. Os tipos e as alíneas (o formulário) são configurados antes, no manual "Prontuário — Configuração". A conferência gerencial (auditoria) tem manual próprio.

Vídeo narrado desta rotina: `video-prontuario-uso-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

## Quem faz o quê

| Perfil | O que pode fazer |
|---|---|
| Profissional | Criar, preencher, finalizar, consultar, imprimir e excluir rascunhos dos seus prontuários; ver prontuários finalizados de outros, se a Especialidade compartilhar. |
| Administrador | Consultar e imprimir; exportar a lista em CSV. Não cria prontuário pela tela do profissional. |
| Atendente | Acessa a lista de prontuários (link "Prontuário" do menu), sem criar nem editar. |

O acesso é por Prontuário no menu lateral (na área do profissional). O módulo Prontuário precisa estar ligado para a clínica.

## 1. Encontrar prontuários (a lista)

Ao abrir a tela, aparece a janela Filtrar. O Tipo é obrigatório (Anamnese, Evolução diária...). Os demais filtros são opcionais.

![Filtros: número do prontuário, tipo (obrigatório), nome do paciente, datas de emissão e de inclusão, situação (Finalizado), ordenação e tags.](01-inbox.png)

_Filtros: número do prontuário, tipo (obrigatório), nome do paciente, datas de emissão e de inclusão, situação (Finalizado), ordenação e tags._

| Filtro | Para que serve |
|---|---|
| Nº Prontuário | Busca direto pelo número do prontuário (só o número, sem zeros à esquerda). |
| Tipo * | Obrigatório. A lista mostra um tipo por vez. |
| Nome do Paciente | Parte do nome. |
| Emissão inicial / final | Data de emissão (a data do documento, informada ao finalizar). |
| Inclusão inicial / final | Data em que o prontuário foi criado. |
| Finalizado | Todos, só finalizados ou só em digitação. |
| Ordenação | Mais recentes primeiro, entre outras. |
| Tags | Só aparece se a clínica usa tags. Com nenhuma marcada, retorna todos. |

![Resultado do filtro: número, profissional, paciente, mãe, situação, datas e as ações da linha.](13-lista-filtrada.png)

_Resultado do filtro: número, profissional, paciente, mãe, situação, datas e as ações da linha._

Situação: Digitação (rascunho, ainda editável) ou Finalizada (travada). Ações de cada linha: olho (visualizar), tags (ver as tags do prontuário, quando a clínica usa tags), amarelo (abrir para preencher, só nos seus prontuários) e lixeira (só nos seus rascunhos). A caixa de seleção existe só nos finalizados e serve para imprimir.

## 2. Criar um prontuário

Depois de filtrar por um tipo, clique em Novo. A janela "Selecionar Paciente" tem duas abas: Buscar da agenda e Buscar por dados.

![Janela para selecionar o paciente e a especialidade.](05-novo-menu.png)

_Janela para selecionar o paciente e a especialidade._

!["Listar Pacientes da agenda atual" mostra os pacientes do profissional na agenda do mês, para marcar um ou vários.](06-pacientes-agenda.png)

_"Listar Pacientes da agenda atual" mostra os pacientes do profissional na agenda do mês, para marcar um ou vários._

Marque o(s) paciente(s), escolha a Especialidade (obrigatória: ela é gravada no prontuário e é ela que define o "Relatório Compartilhado") e clique em Adicionar. Pacientes que já têm um rascunho do mesmo tipo não aparecem para não criar duplicado. Quando se cria um só, o sistema já abre o prontuário para preenchimento.

![Paciente e especialidade selecionados, prontos para Adicionar.](07-selecionar-paciente.png)

_Paciente e especialidade selecionados, prontos para Adicionar._

> ⚠️ Regra da Evolução diária: esse tipo não pode ser criado com data mais de 1 dia no futuro.

## 3. Preencher o prontuário

![Prontuário recém-criado: dados do paciente, data de emissão, tags e a primeira alínea.](08-apos-adicionar.png)

_Prontuário recém-criado: dados do paciente, data de emissão, tags e a primeira alínea._

| Área da tela | Como funciona |
|---|---|
| Cabeçalho | Tipo, paciente, mãe e o número do prontuário (N°). |
| Data de emissão | Vem com a data de hoje. Ajuste se necessário e use o Salvar ao lado. É a data que aparece no documento. |
| Tags | Escolha uma tag na lista e clique em Salvar; para remover, use a lixeira ao lado da tag. Só existe se a clínica usa tags. |
| Alínea | Cada alínea é um campo do formulário. Use Anterior / Próxima para navegar; o "1/1" mostra a posição. |
| Descrever | Caixa de texto da alínea, com contador de caracteres. Salvar grava só a alínea atual ("Texto Salvo."). |
| Texto Padrão | Lista dos seus textos padrão do tipo. Ao escolher um, o sistema pergunta se deseja inserir. |

![Ao escolher um texto padrão, a confirmação avisa que o texto já digitado no campo será apagado.](09-texto-padrao-confirmar.png)

_Ao escolher um texto padrão, a confirmação avisa que o texto já digitado no campo será apagado._

> ⚠️ Atenção: inserir um texto padrão substitui o que já foi digitado na alínea. Insira o texto padrão primeiro e complemente depois.

![Alínea salva. O botão Finalizar só aparece depois que há texto salvo.](10-alinea-salva.png)

_Alínea salva. O botão Finalizar só aparece depois que há texto salvo._

Para alíneas do tipo Sim ou Não aparece uma lista de opções, e nas do tipo Arquivo há o envio de um anexo. Cada alínea é salva separadamente.

## 4. Tags

As tags identificam o método de atendimento (por exemplo, "Padrão" ou "Jedi") e são usadas na Auditoria de Prontuário. Só aparecem se a clínica tem a opção PRONTUARIO_TAGS. Como elas entram no prontuário:

| Quando | O que acontece |
|---|---|
| Ao criar o prontuário | Se a clínica tem a opção PRONT_TAG_AUTO e o paciente tem um único método na agenda do mês com esse profissional, a tag desse método é aplicada sozinha. Com mais de um método (ou nenhum), não marca. |
| Ao abrir o prontuário | O sistema aplica as tags sugeridas pelos métodos da agenda do mês da emissão e por tags de outros prontuários do mesmo mês (no teste, um paciente com dois métodos recebeu as duas tags ao abrir). |
| Manualmente | Escolha na lista e clique em Salvar. Só é possível mexer nas tags enquanto o prontuário não estiver finalizado. |
| Ao finalizar | Se a clínica usa tags e existem tags cadastradas, é preciso ter ao menos 1 tag, senão a tela avisa "Informe ao menos 1 tag antes de finalizar o prontuário". |

![Depois de finalizado, as tags são consultadas pelo botão "tags" da linha na lista.](14-tags-modal.png)

_Depois de finalizado, as tags são consultadas pelo botão "tags" da linha na lista._

> ⚠️ Correção feita nesta documentação: a tag automática ao criar o prontuário não funcionava, porque o cálculo do mês dependia da data de emissão, que só existe ao finalizar. Agora usa a data de criação, e ela é aplicada corretamente (testado: paciente com método único recebeu a tag na criação).

## 5. Finalizar

Clique em Finalizar. A janela confirma a data de emissão que será usada; escolha Sim para concluir.

![Confirmação de finalização com a data de emissão.](11-finalizar-confirmar.png)

_Confirmação de finalização com a data de emissão._

![Prontuário finalizado: os campos ficam bloqueados (cinza) e as tags saem da tela de edição.](12-finalizado.png)

_Prontuário finalizado: os campos ficam bloqueados (cinza) e as tags saem da tela de edição._

| Depois de finalizar | Regra |
|---|---|
| Edição | Não é mais possível alterar textos. Se tentar (por exemplo, por outra tela), o servidor responde "Não é possível salvar. O prontuário está finalizado." |
| Exclusão | Prontuário finalizado não é excluído (a tela não mostra a lixeira e agora o servidor também recusa). |
| Reabrir | Não há botão de reabrir na tela do profissional; a reabertura é uma operação restrita (perfil 50) feita fora da tela de prontuário. |
| Quem edita | Somente o profissional dono do prontuário. Outro profissional nunca altera, mesmo com Relatório Compartilhado (que é só leitura). |

## 6. Consultar e imprimir

O olho abre a visualização (só leitura), que também traz o botão Página de impressão / Download.

![Visualização do prontuário finalizado.](15-visualizar.png)

_Visualização do prontuário finalizado._

Para gerar o PDF direto da lista, marque a caixa dos prontuários finalizados e clique no ícone da impressora. Só é possível imprimir de um paciente por vez ("Selecione documentos de apenas 1 paciente"). O arquivo baixa como "pac_&lt;nome do paciente&gt;_&lt;data e hora&gt;.pdf".

![Prontuário finalizado marcado; o ícone da impressora gera o PDF.](16-selecionar-imprimir.png)

_Prontuário finalizado marcado; o ícone da impressora gera o PDF._

![PDF gerado: cabeçalho com dados do paciente, as alíneas preenchidas, marca d'água da clínica e linha de assinatura e carimbo.](18-pdf-prontuario.png)

_PDF gerado: cabeçalho com dados do paciente, as alíneas preenchidas, marca d'água da clínica e linha de assinatura e carimbo._

> ⚠️ Correção feita nesta documentação: o nome do arquivo saía como "pac__data.pdf", sem o nome do paciente. Agora inclui o nome (ex.: "pac_Paciente_0005_23-09-2026 17-49.pdf"). O modelo do PDF (1, 2 ou 3) é definido por tipo de prontuário na configuração da clínica.

## 7. Excluir um rascunho

A lixeira aparece só nos seus rascunhos (situação Digitação).

![Rascunho na lista: aparecem olho, tags, abrir e lixeira; sem caixa de impressão.](19-lista-rascunho.png)

_Rascunho na lista: aparecem olho, tags, abrir e lixeira; sem caixa de impressão._

![Confirmação da exclusão do rascunho.](20-excluir-rascunho.png)

_Confirmação da exclusão do rascunho._

| Situação do rascunho | O que a exclusão faz |
|---|---|
| Nenhuma alínea salva | Apaga o prontuário de vez (junto com as tags). |
| Já tem texto salvo | Marca como excluído: some da lista, mas o registro é preservado no banco. |

> ⚠️ Correção feita nesta documentação: excluir um rascunho que tinha tag (inclusive a automática) falhava em silêncio, porque a tag impedia a exclusão no banco. Agora as tags saem junto (testado com o rascunho criado durante o teste).

## 8. Ver prontuários de outros profissionais

Um profissional só vê o prontuário finalizado de outro se a Especialidade do prontuário estiver com "Relatório Compartilhado(Prontuários)" e o paciente já tiver prontuário com ele. Nível 1: só quem atende a mesma especialidade. Nível 2: qualquer profissional com paciente em comum. O compartilhamento é sempre somente leitura. Detalhes no manual "Cadastro de Especialidades".

A tela Prontuários por paciente (menu Prontuário do administrador e do profissional) reúne o histórico de um paciente: escolha o paciente (só aparecem pacientes ativos), o tipo e, se quiser, o profissional, e pesquise. Esta consulta não foi demonstrada em vídeo.

## Mensagens e cuidados

| Mensagem | O que significa |
|---|---|
| "Tipo não enviado" / "Paciente não encontrado" | Faltou escolher o tipo ou o paciente. |
| "Operação não permitida" | O prontuário é de outro profissional (só o dono altera). |
| "Não é possível salvar. O prontuário está finalizado." | Prontuário já finalizado. |
| "Informe ao menos 1 tag antes de finalizar o prontuário" | A clínica exige tag e nenhuma foi marcada. |
| "Selecione documentos de apenas 1 paciente" | Na impressão, marque prontuários de um único paciente. |
| "Este tipo está vinculado a prontuário..." | Ao excluir um tipo que já tem prontuários (na Configuração). |

> ⚠️ Resumo: (1) o profissional só edita o que é seu; (2) finalizar trava o prontuário; (3) inserir texto padrão apaga o texto da alínea; (4) imprima um paciente por vez; (5) o Relatório Compartilhado é só leitura.
