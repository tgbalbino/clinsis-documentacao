# Cadastro de Plano de Contas

_Como organizar as categorias de receitas e despesas da clínica_

Versão 1.0 — 17/09/2026

O Plano de Contas é a lista de categorias usada para classificar toda entrada e saída de dinheiro da clínica (ex.: "Consulta por Convênio", "Aluguel", "Material de Consumo"). Ele é um cadastro pré-requisito: praticamente todas as outras telas financeiras do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin com pagamento, fechamento de Contrato) exigem que o lançamento tenha um Plano de Conta selecionado. Por isso, recomendamos configurar o Plano de Contas antes de usar as demais rotinas financeiras.

Assista ao vídeo narrado desta rotina: [https://youtu.be/m4e2BMEsMZg](https://youtu.be/m4e2BMEsMZg)
---

## Duas formas de visualizar: Árvore ou Lista

A tela abre no modo Árvore, que agrupa as contas em três grupos fixos — 1 - RECEITAS, 2 - DESPESAS e 3 - OUTROS — e permite até 2 níveis dentro de cada grupo (uma conta "pai" e suas contas "filhas"). O botão Lista, no canto superior direito, troca para uma tabela simples com todas as contas cadastradas, sem a hierarquia visual.

![Visão em árvore: contas de Receitas e Despesas já cadastradas, cada uma com seu código (ex.: 2.01, 2.02...).](00-arvore-inicial.png)

_Visão em árvore: contas de Receitas e Despesas já cadastradas, cada uma com seu código (ex.: 2.01, 2.02...)._

![A mesma informação na visão em Lista, com colunas Código, Descrição, Tipo, Pai e Ativo.](01-lista.png)

_A mesma informação na visão em Lista, com colunas Código, Descrição, Tipo, Pai e Ativo._

## Cadastrando uma nova conta (exemplo)

Clique em Novo. No exemplo abaixo, criamos a conta "MATERIAL DE ESCRITORIO" como uma conta filha de "2 - Despesas" — ou seja, ela aparece dentro do grupo de despesas, como mais uma categoria de gasto.

![Cadastro de uma nova conta: Tipo = Despesa, Código gerado automaticamente (2.11), Descrição preenchida e Pai = "2 - Despesas".](02-novo-modal-preenchido.png)

_Cadastro de uma nova conta: Tipo = Despesa, Código gerado automaticamente (2.11), Descrição preenchida e Pai = "2 - Despesas"._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Tipo | D (Despesa) ou R (Receita) — define se a conta vai aparecer no grupo de Receitas ou de Despesas. | Obrigatório; validado em PlanoContaController.cs (Criar/Alterar) |
| Código | Gerado automaticamente pelo sistema ao criar uma conta nova (não é digitado) — segue a numeração do grupo/conta pai. | PlanoContaController.cs |
| Descrição | Nome da categoria, como vai aparecer em todos os relatórios e telas financeiras (ex.: "Aluguel", "Consulta por Convênio"). | Obrigatório; máx. 100 caracteres |
| Plano de Conta Pai | Opcional. Se preenchido, a nova conta vira uma "conta filha" da selecionada — usado para detalhar uma categoria maior. Sistema permite no máximo 2 níveis. | PlanoContaController.cs |
| Ativo | Contas inativas continuam existindo (para não quebrar lançamentos antigos), mas somem das listas de seleção ao lançar novas contas a pagar/receber. | PlanoContaController.cs |

![Depois de salvar, a nova conta "MATERIAL DE ESCRITORIO" (2.11) já aparece na árvore, dentro do grupo Despesas.](03-apos-salvar.png)

_Depois de salvar, a nova conta "MATERIAL DE ESCRITORIO" (2.11) já aparece na árvore, dentro do grupo Despesas._

## Filtrando contas cadastradas

O botão Filtros abre uma busca por Código, Descrição, Tipo, conta Pai ou Situação (Ativo/Inativo), útil quando o plano de contas cresce e fica mais difícil de navegar olhando a árvore inteira.

![Filtro por Descrição contendo "MATERIAL".](04-filtro-preenchido.png)

_Filtro por Descrição contendo "MATERIAL"._

![Resultado: só as contas que batem com o filtro aparecem na lista.](05-resultado-filtro.png)

_Resultado: só as contas que batem com o filtro aparecem na lista._

## Atalho: Importar Plano de Contas Padrão

Quando não existe nenhuma conta cadastrada ainda, a tela mostra um botão "Importar Plano de Contas Padrão", que cria de uma vez uma lista pronta de contas comuns para clínicas (Consulta Particular, Consulta por Convênio, Aluguel, Energia Elétrica, Folha de Pagamento, etc.) — um bom ponto de partida para não precisar cadastrar tudo manualmente.

> ⚠️ Este cadastro não gera Conta a Pagar nem Conta a Receber por si só — ele só define as categorias que serão usadas quando essas contas forem lançadas em outras telas do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin, Contrato).
