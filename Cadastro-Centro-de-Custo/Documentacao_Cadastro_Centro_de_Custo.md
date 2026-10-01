# Cadastro de Centro de Custo

_Como organizar a clínica em setores para saber onde o dinheiro entra e sai_

Versão 1.1 — 29/09/2026

O Centro de Custo identifica QUAL SETOR da clínica está envolvido em uma entrada ou saída de dinheiro (ex.: "Consultório 1", "Recepção", "Administrativo/Financeiro"). Junto com o Plano de Contas, é um cadastro pré-requisito das demais telas financeiras (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin com pagamento, fechamento de Contrato). Recomendamos configurar essa tela antes de usar as demais rotinas financeiras.

Assista ao vídeo narrado desta rotina: [https://youtu.be/TGcyxaZc2QY](https://youtu.be/TGcyxaZc2QY)

---

## Barra de ações

No alto da lista ficam o botão azul Novo (em destaque), o botão Filtros — que mostra um número quando há filtro aplicado, com um ✕ ao lado para limpar tudo de uma vez — e o botão de Atualizar, só com o ícone. Só a lista rola; o título e a barra de ações ficam sempre visíveis.

![Lista de Centros de Custo com a barra de ações (Novo, Filtros, Atualizar).](00-lista-inicial.png)

_Lista de Centros de Custo com a barra de ações (Novo, Filtros, Atualizar)._

## Diferença entre Plano de Conta e Centro de Custo

É comum confundir os dois: o Plano de Conta responde "o que é" o lançamento (ex.: Aluguel, Consulta por Convênio), enquanto o Centro de Custo responde "de onde/para qual setor" (ex.: Recepção, Consultório 1). O mesmo lançamento de "Aluguel" pode ser dividido entre Centros de Custo diferentes se a clínica tiver mais de uma unidade ou setor pagando aluguel separadamente.

![Tela inicial: lista simples com Descrição e Situação de cada centro de custo já cadastrado.](00-lista-inicial.png)

_Tela inicial: lista simples com Descrição e Situação de cada centro de custo já cadastrado._

## Cadastrando um novo Centro de Custo (exemplo)

Clique em Novo. A tela é bem simples: só pede a Descrição do setor e se ele está Ativo. No exemplo abaixo, criamos o centro de custo "FISIOTERAPIA".

![Cadastro de um novo Centro de Custo: Descrição = "FISIOTERAPIA".](01-novo-modal-preenchido.png)

_Cadastro de um novo Centro de Custo: Descrição = "FISIOTERAPIA"._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Descrição | Nome do setor/área da clínica, como vai aparecer em todos os relatórios e telas financeiras. | Obrigatório; máx. 100 caracteres |
| Ativo | Centros inativos continuam existindo (para não quebrar lançamentos antigos), mas somem das listas de seleção ao lançar novas contas a pagar/receber. | CentroCustoController.cs |

![Depois de salvar, "FISIOTERAPIA" já aparece na lista.](02-apos-salvar.png)

_Depois de salvar, "FISIOTERAPIA" já aparece na lista._

## Filtrando centros de custo cadastrados

O botão Filtros permite buscar por Descrição ou Situação (Ativo/Inativo), útil quando a clínica tem muitos setores cadastrados.

![Resultado do filtro por Descrição contendo "FISIO".](04-resultado-filtro.png)

_Resultado do filtro por Descrição contendo "FISIO"._

## Atalho: Importar Centros de Custo Padrão

Quando não existe nenhum centro de custo cadastrado ainda, a tela mostra um botão "Importar Centros de Custo Padrão", que cria de uma vez uma lista pronta de setores comuns em clínicas (Recepção, Consultório, Administrativo/Financeiro, etc.).

> ⚠️ Este cadastro não gera Conta a Pagar nem Conta a Receber por si só — ele só define os setores que serão usados quando essas contas forem lançadas em outras telas do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin, Contrato).
