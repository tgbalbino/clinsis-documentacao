# Cadastro de Centro de Custo

_Como organizar a clínica em setores para saber onde o dinheiro entra e sai_

## Documentação em PDF

- [📄 Manual completo (com origem técnica no banco)](../assets/Cadastro-Centro-de-Custo/Documentacao_Cadastro_Centro_de_Custo.pdf)
- [📄 Manual simplificado](../assets/Cadastro-Centro-de-Custo/Documentacao_Cadastro_Centro_de_Custo_Simplificado.pdf)

## Vídeo narrado

*Vídeo em processo de publicação — o link será adicionado aqui assim que estiver disponível no YouTube.*

## Conteúdo completo do manual

*As capturas de tela deste trecho estão no PDF acima — aqui fica só o texto.*

---


_Como organizar a clínica em setores para saber onde o dinheiro entra e sai_

Versão 1.0 — 17/09/2026

O Centro de Custo identifica QUAL SETOR da clínica está envolvido em uma entrada ou saída de dinheiro (ex.: "Consultório 1", "Recepção", "Administrativo/Financeiro"). Junto com o Plano de Contas, é um cadastro pré-requisito das demais telas financeiras (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin com pagamento, fechamento de Contrato). Recomendamos configurar essa tela antes de usar as demais rotinas financeiras.

Vídeo narrado desta rotina: `video-cadastro-centro-de-custo.mp4`

---

## Diferença entre Plano de Conta e Centro de Custo

É comum confundir os dois: o Plano de Conta responde "o que é" o lançamento (ex.: Aluguel, Consulta por Convênio), enquanto o Centro de Custo responde "de onde/para qual setor" (ex.: Recepção, Consultório 1). O mesmo lançamento de "Aluguel" pode ser dividido entre Centros de Custo diferentes se a clínica tiver mais de uma unidade ou setor pagando aluguel separadamente.


## Cadastrando um novo Centro de Custo (exemplo)

Clique em Novo. A tela é bem simples: só pede a Descrição do setor e se ele está Ativo. No exemplo abaixo, criamos o centro de custo "FISIOTERAPIA".


| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Descrição | Nome do setor/área da clínica, como vai aparecer em todos os relatórios e telas financeiras. | Obrigatório; máx. 100 caracteres |
| Ativo | Centros inativos continuam existindo (para não quebrar lançamentos antigos), mas somem das listas de seleção ao lançar novas contas a pagar/receber. | CentroCustoController.cs |


## Filtrando centros de custo cadastrados

O botão Filtros permite buscar por Descrição ou Situação (Ativo/Inativo), útil quando a clínica tem muitos setores cadastrados.


## Atalho: Importar Centros de Custo Padrão

Quando não existe nenhum centro de custo cadastrado ainda, a tela mostra um botão "Importar Centros de Custo Padrão", que cria de uma vez uma lista pronta de setores comuns em clínicas (Recepção, Consultório, Administrativo/Financeiro, etc.).

> ⚠️ Este cadastro não gera Conta a Pagar nem Conta a Receber por si só — ele só define os setores que serão usados quando essas contas forem lançadas em outras telas do sistema (Contas a Pagar, Contas a Receber, Contas Recorrentes, Checkin, Contrato).
