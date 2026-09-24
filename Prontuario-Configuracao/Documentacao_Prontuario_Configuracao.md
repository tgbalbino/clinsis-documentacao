# Prontuário — Configuração

_Tipos de prontuário, Alíneas e Textos padrão: o que são, como cadastrar e para que servem_

Versão 1.0 — 23/09/2026

Antes de um profissional preencher um prontuário, a clínica precisa definir quais tipos de prontuário existem (Anamnese, Evolução, Relatório...) e quais campos cada tipo tem (as alíneas). Este manual explica essas duas configurações, feitas pelo administrador, e os Textos padrão, que cada profissional cria para agilizar o preenchimento. O uso do dia a dia (criar, preencher, finalizar) e a auditoria estão em manuais próprios.

Assista ao vídeo narrado desta rotina: [https://youtu.be/X4ClyuUIsAE](https://youtu.be/X4ClyuUIsAE)
---

## Visão geral: o que configurar e quem faz

| Configuração | Quem faz | Onde |
|---|---|---|
| Tipo de prontuário | Administrador | Menu Prontuário → Tipos |
| Alíneas do tipo (os campos) | Administrador | Menu Prontuário → Alíneas |
| Texto padrão | Cada profissional (são pessoais) | Menu Prontuário → Textos padrão (área do profissional) |

A ordem natural é: 1) criar o Tipo, 2) cadastrar as Alíneas dele, 3) cada profissional cria seus Textos padrão. Só depois o profissional consegue criar e preencher prontuários daquele tipo. As telas só aparecem se o módulo Prontuário estiver ligado para a clínica.

## 1. Tipos de prontuário

Um Tipo é uma categoria de documento clínico. Exemplos da clínica de teste: Anamnese, Evolução diária, Rel. Acompanhamento Mensal, Declaração, Relatório técnico. Acesso: Prontuário → Tipos (perfil administrador).

![Lista de tipos da clínica: nome do tipo, se é visível na agenda e as ações (editar, Modelo, excluir).](01-tipos.png)

_Lista de tipos da clínica: nome do tipo, se é visível na agenda e as ações (editar, Modelo, excluir)._

Novo: informe apenas o nome do tipo e clique em Salvar. O tipo nasce sem nenhuma alínea, então ainda não serve para preencher: o próximo passo é cadastrar as alíneas.

![Novo tipo: só o nome é pedido.](02-tipo-novo.png)

_Novo tipo: só o nome é pedido._

Editar (botão amarelo): permite ajustar dois campos.

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Dias | Número gravado no tipo e copiado para cada prontuário criado. Hoje nenhuma tela usa esse número, então preenchê-lo não muda o comportamento do sistema. | ProntuarioTipo.Dias |
| Visível na agenda para preenchimento dos profissionais? | Quando marcado, o tipo aparece na lista de tipos da tela Agenda resumida, permitindo criar o prontuário direto a partir da agenda. Na lista de Tipos aparece como "Sim" ou "Não". | ProntuarioTipo.VisivelNaAgenda |

![Editar tipo: Dias e "Visível na agenda". Ao salvar, a tela mostra "Salvo!" e a lista atualiza a coluna "Visível na agenda".](04-tipo-alterar.png)

_Editar tipo: Dias e "Visível na agenda". Ao salvar, a tela mostra "Salvo!" e a lista atualiza a coluna "Visível na agenda"._

Modelo (botão azul ou verde): serve para anexar ao tipo um arquivo de modelo (por exemplo, um formulário em Word) que os profissionais podem baixar na tela Prontuário. O botão fica verde quando o tipo já tem modelo. O arquivo é guardado no armazenamento de arquivos da clínica (S3); nesta demonstração o envio não foi testado, pois o ambiente de teste não tem esse armazenamento configurado.

Excluir (botão vermelho): pede confirmação. Não é possível excluir um tipo que já tenha prontuários — o sistema avisa "Este tipo está vinculado a prontuário, não pode ser removido". Quando o tipo nunca foi usado, ele é excluído junto com suas alíneas, textos padrão, modelo e vínculos De-Para.

![Confirmação ao excluir um tipo.](15-tipo-excluir.png)

_Confirmação ao excluir um tipo._

> ⚠️ Correção feita nesta documentação: antes, excluir um tipo deixava suas alíneas "órfãs" no banco. Como o próximo tipo criado reaproveita o mesmo número interno, ele aparecia já com alíneas que ninguém cadastrou (foi assim que uma alínea "Descritiva" apareceu num tipo novo durante o teste). Agora a exclusão remove tudo junto. Para limpar registros órfãos antigos existe o script 139_Limpar_Orfaos_De_Prontuario_Tipo_Removido.sql, que precisa ser executado no banco de cada ambiente.

## 2. Alíneas

A Alínea é cada campo (ou seção) do prontuário: "Queixa principal", "Conduta", "Resumo do atendimento"... O profissional preenche uma alínea por vez. Acesso: Prontuário → Alíneas (administrador). A lista mostra as alíneas de todos os tipos, ou só as do tipo escolhido no filtro do topo.

![Nova alínea: escolha o tipo de prontuário, o tipo de campo e digite o nome da alínea.](07-alinea-nova.png)

_Nova alínea: escolha o tipo de prontuário, o tipo de campo e digite o nome da alínea._

| Tipo de campo | Como o profissional preenche |
|---|---|
| Texto | Caixa de texto livre (aceita os Textos padrão). |
| Sim ou Não | Lista com as opções Sim/Não. |
| Arquivo - Upload | Anexo de um arquivo (por exemplo, um laudo em PDF ou imagem). |

Depois de Salvar, a janela continua aberta para você cadastrar várias alíneas seguidas; use Fechar ao terminar. O sistema não impede duas alíneas com o mesmo nome no mesmo tipo, então confira para não duplicar.

![Filtrando pelo tipo, a lista mostra o tipo de campo e o nome de cada alínea, na ordem em que aparecerão para o profissional.](08-alineas-do-tipo.png)

_Filtrando pelo tipo, a lista mostra o tipo de campo e o nome de cada alínea, na ordem em que aparecerão para o profissional._

Ordem: quando um tipo específico está filtrado, aparecem as setas para subir e descer cada alínea. Depois de reordenar, clique em Salvar (botão amarelo) para gravar a nova ordem.

![Após mover uma alínea, aparece o botão Salvar para gravar a ordem.](09-alineas-ordenar.png)

_Após mover uma alínea, aparece o botão Salvar para gravar a ordem._

![Ordem salva ("Salvo!"): "Conduta e orientações" passou a ser a primeira.](10-alineas-ordem-salva.png)

_Ordem salva ("Salvo!"): "Conduta e orientações" passou a ser a primeira._

Excluir uma alínea (botão vermelho) pede confirmação. Se a clínica tiver a configuração auxiliar BLOCK_ADD_PRONT (bloqueio de novos lançamentos de prontuário), os botões Novo e excluir desta tela deixam de aparecer, e o cadastro de alíneas fica somente para consulta.

![Confirmação ao excluir uma alínea.](14-alinea-excluir.png)

_Confirmação ao excluir uma alínea._

## 3. Textos padrão

Um Texto padrão é um trecho pronto que o profissional insere numa alínea de texto com um clique, em vez de digitar tudo de novo. Cada profissional cria os seus, por tipo de prontuário. Acesso: Prontuário → Textos padrão, na área do profissional.

![Novo texto padrão: tipo de prontuário, título (máximo 20 caracteres) e o texto.](11-texto-padrao-novo.png)

_Novo texto padrão: tipo de prontuário, título (máximo 20 caracteres) e o texto._

![Lista dos textos do profissional, com o título e os botões Visualizar/Alterar e excluir.](12-texto-padrao-lista.png)

_Lista dos textos do profissional, com o título e os botões Visualizar/Alterar e excluir._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Prontuário tipo | Em quais prontuários este texto estará disponível. Não pode ser trocado depois de salvo. | ProntuarioTextoPadrao.IdProntuarioTipo |
| Título | Nome curto que o profissional vê na lista ao inserir (máximo 20 caracteres). | ProntuarioTextoPadrao.Titulo |
| Texto | O conteúdo que será inserido na alínea. | ProntuarioTextoPadrao.Texto |

![Confirmação ao excluir um texto padrão.](13-texto-padrao-excluir.png)

_Confirmação ao excluir um texto padrão._

## Itens ligados a esta configuração

| Item | O que é | Onde está |
|---|---|---|
| Relatório Compartilhado(Prontuários) | Define se um profissional vê o prontuário finalizado de outro. | Cadastro de Especialidades (manual próprio) |
| De-Para de prontuário | Forma antiga de autorizar um profissional a ver prontuários de outro. Está oculta do menu e sendo substituída pelo Relatório Compartilhado. | Rota /prontuario/depara (não aparece no menu) |
| Tags do prontuário | Rótulos por método de atendimento; ligadas por configuração da clínica (PRONTUARIO_TAGS). | Manuais "Uso do Prontuário" e "Auditoria de Prontuário" |

> ⚠️ Resumo dos cuidados: (1) crie primeiro o tipo e as alíneas; (2) evite excluir ou reordenar alíneas de um tipo já em uso, pois isso muda o formulário dos prontuários em andamento; (3) tipo com prontuários não pode ser excluído; (4) textos padrão são pessoais de cada profissional.
