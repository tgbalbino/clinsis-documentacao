# Prontuário — Uso pelo Profissional

_Criar, preencher, finalizar, consultar e imprimir prontuários_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Prontuario-Uso/Documentacao_Prontuario_Uso_Simplificado.pdf)

## Vídeo narrado

- [▶️ Assistir o vídeo no YouTube](https://youtu.be/XPTXN2u41Ps)

## Conteúdo completo do manual

*As capturas de tela deste trecho estão no PDF acima — aqui fica só o texto.*

---


_Criar, preencher, finalizar, consultar e imprimir prontuários_

Versão 1.0 — 23/09/2026

Este manual mostra o dia a dia do prontuário para o profissional: como criar um prontuário para um paciente da agenda, preencher as alíneas, usar textos padrão e tags, finalizar, consultar, imprimir em PDF e excluir um rascunho. Os tipos e as alíneas (o formulário) são configurados antes, no manual "Prontuário — Configuração". A conferência gerencial (auditoria) tem manual próprio.

Assista ao vídeo narrado desta rotina: [https://youtu.be/XPTXN2u41Ps](https://youtu.be/XPTXN2u41Ps)
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


Situação: Digitação (rascunho, ainda editável) ou Finalizada (travada). Ações de cada linha: olho (visualizar), tags (ver as tags do prontuário, quando a clínica usa tags), amarelo (abrir para preencher, só nos seus prontuários) e lixeira (só nos seus rascunhos). A caixa de seleção existe só nos finalizados e serve para imprimir.

## 2. Criar um prontuário

Depois de filtrar por um tipo, clique em Novo. A janela "Selecionar Paciente" tem duas abas: Buscar da agenda e Buscar por dados.



Marque o(s) paciente(s), escolha a Especialidade (obrigatória: ela é gravada no prontuário e é ela que define o "Relatório Compartilhado") e clique em Adicionar. Pacientes que já têm um rascunho do mesmo tipo não aparecem para não criar duplicado. Quando se cria um só, o sistema já abre o prontuário para preenchimento.


> ⚠️ Regra da Evolução diária: esse tipo não pode ser criado com data mais de 1 dia no futuro.

## 3. Preencher o prontuário


| Área da tela | Como funciona |
|---|---|
| Cabeçalho | Tipo, paciente, mãe e o número do prontuário (N°). |
| Data de emissão | Vem com a data de hoje. Ajuste se necessário e use o Salvar ao lado. É a data que aparece no documento. |
| Tags | Escolha uma tag na lista e clique em Salvar; para remover, use a lixeira ao lado da tag. Só existe se a clínica usa tags. |
| Alínea | Cada alínea é um campo do formulário. Use Anterior / Próxima para navegar; o "1/1" mostra a posição. |
| Descrever | Caixa de texto da alínea, com contador de caracteres. Salvar grava só a alínea atual ("Texto Salvo."). |
| Texto Padrão | Lista dos seus textos padrão do tipo. Ao escolher um, o sistema pergunta se deseja inserir. |


> ⚠️ Atenção: inserir um texto padrão substitui o que já foi digitado na alínea. Insira o texto padrão primeiro e complemente depois.


Para alíneas do tipo Sim ou Não aparece uma lista de opções, e nas do tipo Arquivo há o envio de um anexo. Cada alínea é salva separadamente.

## 4. Tags

As tags identificam o método de atendimento (por exemplo, "Padrão" ou "Jedi") e são usadas na Auditoria de Prontuário. Só aparecem se a clínica tem a opção PRONTUARIO_TAGS. Como elas entram no prontuário:

| Quando | O que acontece |
|---|---|
| Ao criar o prontuário | Se a clínica tem a opção PRONT_TAG_AUTO e o paciente tem um único método na agenda do mês com esse profissional, a tag desse método é aplicada sozinha. Com mais de um método (ou nenhum), não marca. |
| Ao abrir o prontuário | O sistema aplica as tags sugeridas pelos métodos da agenda do mês da emissão e por tags de outros prontuários do mesmo mês (no teste, um paciente com dois métodos recebeu as duas tags ao abrir). |
| Manualmente | Escolha na lista e clique em Salvar. Só é possível mexer nas tags enquanto o prontuário não estiver finalizado. |
| Ao finalizar | Se a clínica usa tags e existem tags cadastradas, é preciso ter ao menos 1 tag, senão a tela avisa "Informe ao menos 1 tag antes de finalizar o prontuário". |



## 5. Finalizar

Clique em Finalizar. A janela confirma a data de emissão que será usada; escolha Sim para concluir.



| Depois de finalizar | Regra |
|---|---|
| Edição | Não é mais possível alterar textos. Se tentar (por exemplo, por outra tela), o servidor responde "Não é possível salvar. O prontuário está finalizado." |
| Exclusão | Prontuário finalizado não é excluído (a tela não mostra a lixeira e agora o servidor também recusa). |
| Reabrir | Não há botão de reabrir na tela do profissional; a reabertura é uma operação restrita (perfil 50) feita fora da tela de prontuário. |
| Quem edita | Somente o profissional dono do prontuário. Outro profissional nunca altera, mesmo com Relatório Compartilhado (que é só leitura). |

## 6. Consultar e imprimir

O olho abre a visualização (só leitura), que também traz o botão Página de impressão / Download.


Para gerar o PDF direto da lista, marque a caixa dos prontuários finalizados e clique no ícone da impressora. Só é possível imprimir de um paciente por vez ("Selecione documentos de apenas 1 paciente"). O arquivo baixa como "pac_&lt;nome do paciente&gt;_&lt;data e hora&gt;.pdf".




## 7. Excluir um rascunho

A lixeira aparece só nos seus rascunhos (situação Digitação).



| Situação do rascunho | O que a exclusão faz |
|---|---|
| Nenhuma alínea salva | Apaga o prontuário de vez (junto com as tags). |
| Já tem texto salvo | Marca como excluído: some da lista, mas o registro é preservado no sistema. |


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
