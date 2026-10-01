# Cadastro de Plano de Contas

O Plano de Contas organiza as categorias de receitas e despesas da clínica (por exemplo, aluguel, salários, consultas). Cada lançamento financeiro é classificado nele, o que permite saber de onde vem e para onde vai o dinheiro. Cadastre-o antes de lançar contas a pagar e a receber.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Cadastro-Plano-de-Contas/Documentacao_Cadastro_Plano_de_Contas_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/KJhezxjX10w?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/KJhezxjX10w)

## Conteúdo completo do manual

---


_Como organizar as categorias de receitas e despesas da clínica_

Versão 1.1 — 29/09/2026

O Plano de Contas é a lista de categorias usada para classificar toda entrada e saída de dinheiro da clínica (ex.: "Consulta por Convênio", "Aluguel", "Material de Consumo"). Ele é um cadastro pré-requisito: praticamente todas as outras telas financeiras do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin com pagamento, fechamento de Contrato) exigem que o lançamento tenha um Plano de Conta selecionado. Por isso, recomendamos configurar o Plano de Contas antes de usar as demais rotinas financeiras.


---

## Barra de ações

No alto da lista ficam os controles da tela: o botão azul Novo (destaque), o botão Filtros — que mostra um número quando há filtro aplicado, ao lado de um ✕ para limpar tudo de uma vez — e o botão só com o ícone de Atualizar. No canto direito, Árvore e Lista trocam a forma de visualização. Só a lista rola; o título e a barra de ações continuam sempre visíveis.


## Duas formas de visualizar: Árvore ou Lista

A tela abre no modo Árvore, que agrupa as contas em três grupos fixos — 1 - RECEITAS, 2 - DESPESAS e 3 - OUTROS — e permite até 2 níveis dentro de cada grupo (uma conta "pai" e suas contas "filhas"). O botão Lista, no canto superior direito, troca para uma tabela simples com todas as contas cadastradas, sem a hierarquia visual.


## Cadastrando uma nova conta (exemplo)

Clique em Novo. No exemplo abaixo, criamos a conta "MATERIAL DE ESCRITORIO" como uma conta filha de "2 - Despesas" — ou seja, ela aparece dentro do grupo de despesas, como mais uma categoria de gasto.


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Tipo | D (Despesa) ou R (Receita) — define se a conta vai aparecer no grupo de Receitas ou de Despesas. *(obrigatório)* |
| Código | Gerado automaticamente pelo sistema ao criar uma conta nova (não é digitado) — segue a numeração do grupo/conta pai. |
| Descrição | Nome da categoria, como vai aparecer em todos os relatórios e telas financeiras (ex.: "Aluguel", "Consulta por Convênio"). *(obrigatório)* |
| Plano de Conta Pai | Opcional. Se preenchido, a nova conta vira uma "conta filha" da selecionada — usado para detalhar uma categoria maior. Sistema permite no máximo 2 níveis. |
| Ativo | Contas inativas continuam existindo (para não quebrar lançamentos antigos), mas somem das listas de seleção ao lançar novas contas a pagar/receber. |


## Filtrando contas cadastradas

O botão Filtros abre uma busca por Código, Descrição, Tipo, conta Pai ou Situação (Ativo/Inativo), útil quando o plano de contas cresce e fica mais difícil de navegar olhando a árvore inteira.



## Atalho: Importar Plano de Contas Padrão

Quando não existe nenhuma conta cadastrada ainda, a tela mostra um botão "Importar Plano de Contas Padrão", que cria de uma vez uma lista pronta de contas comuns para clínicas (Consulta Particular, Consulta por Convênio, Aluguel, Energia Elétrica, Folha de Pagamento, etc.) — um bom ponto de partida para não precisar cadastrar tudo manualmente.

> ⚠️ Este cadastro não gera Conta a Pagar nem Conta a Receber por si só — ele só define as categorias que serão usadas quando essas contas forem lançadas em outras telas do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin, Contrato).
