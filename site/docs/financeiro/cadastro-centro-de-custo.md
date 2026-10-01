# Cadastro de Centro de Custo

O Centro de Custo divide a clínica em setores ou áreas (por exemplo, recepção, fisioterapia) para mostrar qual parte gera receita e qual gera despesa. Complementa o Plano de Contas, que diz o tipo do gasto, enquanto o Centro de Custo diz onde ele ocorreu.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Cadastro-Centro-de-Custo/Documentacao_Cadastro_Centro_de_Custo_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/TGcyxaZc2QY?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/TGcyxaZc2QY)

## Conteúdo completo do manual

---


_Como organizar a clínica em setores para saber onde o dinheiro entra e sai_

Versão 1.1 — 29/09/2026

O Centro de Custo identifica QUAL SETOR da clínica está envolvido em uma entrada ou saída de dinheiro (ex.: "Consultório 1", "Recepção", "Administrativo/Financeiro"). Junto com o Plano de Contas, é um cadastro pré-requisito das demais telas financeiras (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin com pagamento, fechamento de Contrato). Recomendamos configurar essa tela antes de usar as demais rotinas financeiras.


---

## Barra de ações

No alto da lista ficam o botão azul Novo (em destaque), o botão Filtros — que mostra um número quando há filtro aplicado, com um ✕ ao lado para limpar tudo de uma vez — e o botão de Atualizar, só com o ícone. Só a lista rola; o título e a barra de ações ficam sempre visíveis.


## Diferença entre Plano de Conta e Centro de Custo

É comum confundir os dois: o Plano de Conta responde "o que é" o lançamento (ex.: Aluguel, Consulta por Convênio), enquanto o Centro de Custo responde "de onde/para qual setor" (ex.: Recepção, Consultório 1). O mesmo lançamento de "Aluguel" pode ser dividido entre Centros de Custo diferentes se a clínica tiver mais de uma unidade ou setor pagando aluguel separadamente.


## Cadastrando um novo Centro de Custo (exemplo)

Clique em Novo. A tela é bem simples: só pede a Descrição do setor e se ele está Ativo. No exemplo abaixo, criamos o centro de custo "FISIOTERAPIA".


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Descrição | Nome do setor/área da clínica, como vai aparecer em todos os relatórios e telas financeiras. *(obrigatório)* |
| Ativo | Centros inativos continuam existindo (para não quebrar lançamentos antigos), mas somem das listas de seleção ao lançar novas contas a pagar/receber. |


## Filtrando centros de custo cadastrados

O botão Filtros permite buscar por Descrição ou Situação (Ativo/Inativo), útil quando a clínica tem muitos setores cadastrados.


## Atalho: Importar Centros de Custo Padrão

Quando não existe nenhum centro de custo cadastrado ainda, a tela mostra um botão "Importar Centros de Custo Padrão", que cria de uma vez uma lista pronta de setores comuns em clínicas (Recepção, Consultório, Administrativo/Financeiro, etc.).

> ⚠️ Este cadastro não gera Conta a Pagar nem Conta a Receber por si só — ele só define os setores que serão usados quando essas contas forem lançadas em outras telas do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin, Contrato).
