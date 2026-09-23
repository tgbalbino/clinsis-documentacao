# Cadastro de Serviços

_Para que serve e onde é utilizado (Tabelas Aux. → Serviços)_

Versão 1.0 — 22/09/2026

Um Serviço é um item simples de "nome + valor" — como um item de tabela de preços — usado como base para montar os itens de um Contrato. Este manual explica o cadastro e, principalmente, onde ele entra em uso dentro do sistema.

Vídeo narrado desta rotina: `video-cadastro-servicos-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

## O que é um Serviço

Pense num Serviço como um item de catálogo: um nome ("Sessão de Fisioterapia", "Avaliação Inicial", "Pacote 10 sessões") e um valor sugerido. Ao montar um Contrato, em vez de digitar manualmente a descrição e o valor de cada item, o usuário busca um Serviço já cadastrado e usa isso como ponto de partida.

O cadastro é bem enxuto: só Descrição e Preço. Não existe ativo/inativo, categoria, nem vínculo com convênio — e não há como excluir um Serviço já cadastrado pela tela, ele permanece disponível permanentemente na lista.

![Lista de Serviços (Tabelas Aux. → Serviços), com Nome e Preço de cada um.](00-lista-servicos.png)

_Lista de Serviços (Tabelas Aux. → Serviços), com Nome e Preço de cada um._

![Tela de cadastro: só dois campos, Serviço (nome) e Preço.](01-cadastro-servico-vazio.png)

_Tela de cadastro: só dois campos, Serviço (nome) e Preço._

## Onde é utilizado: exclusivamente no módulo Contrato

> ⚠️ Apesar do nome "Serviço" sugerir algo amplo (faturamento, convênio, guias), na prática ele é usado em um único lugar do sistema: a aba "Serviços" dentro do cadastro de Contrato. Guia de Faturamento, Cobrança de Paciente e Tabela de Preços de convênio usam outro conceito (Especialidade), sem nenhuma relação com este cadastro.

Dentro de um Contrato, cada linha de serviço contratado (Serviço + Quantidade de sessões + Valor da sessão) fica registrada, e o Valor Total do Contrato é a soma de todas essas linhas — calculado automaticamente pelo sistema, sem que o usuário precise somar nada manualmente.

![Aba "Serviços" dentro do cadastro de Contrato: lista os itens já adicionados (Serviço, Qtd, Valor Sessão, Valor Total) e o botão "Novo".](02-contrato-aba-servicos.png)

_Aba "Serviços" dentro do cadastro de Contrato: lista os itens já adicionados (Serviço, Qtd, Valor Sessão, Valor Total) e o botão "Novo"._

![Ao clicar em "Novo", abre a busca de Serviço: mostra nome e preço de cada um cadastrado, com um botão verde para selecionar.](04-modal-buscar-servico-resultado.png)

_Ao clicar em "Novo", abre a busca de Serviço: mostra nome e preço de cada um cadastrado, com um botão verde para selecionar._

![Depois de escolher o Serviço, o valor sugerido já vem preenchido; falta só informar a Quantidade de sessões. O Valor Total é calculado automaticamente (Quantidade × Valor).](06-contrato-servico-qtd-preenchida.png)

_Depois de escolher o Serviço, o valor sugerido já vem preenchido; falta só informar a Quantidade de sessões. O Valor Total é calculado automaticamente (Quantidade × Valor)._

![Serviço adicionado: a linha aparece na tabela do contrato, e o "Total Serviços" do contrato é atualizado.](07-contrato-servico-adicionado.png)

_Serviço adicionado: a linha aparece na tabela do contrato, e o "Total Serviços" do contrato é atualizado._

## Outros pontos onde o Serviço aparece

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Cálculo do Valor Total do Contrato | A soma de todas as linhas de serviço do contrato define o valor total dele, usado depois para comparar com os pagamentos/acertos lançados ("Falta Acertar"). | ContratoServicoRepository.cs |
| Renovação de Contrato | Ao renovar um contrato, o sistema copia automaticamente os mesmos Serviços/quantidades/valores para o contrato novo. Se o contrato antigo não tiver nenhum serviço, a renovação é bloqueada. | ContratoRenovacaoService.cs |
| Impressão do Contrato | No layout de impressão do contrato (Tabelas Aux. → Layout Contrato), existe um placeholder "TabelaServicos" que renderiza a lista de serviços contratados no PDF/documento impresso. | contrato-laiout-config.component.ts |

> ⚠️ Um Serviço só pode ser adicionado, alterado ou removido de um contrato enquanto ele estiver ativo e ainda não assinado (nem com uma solicitação de assinatura eletrônica em andamento) — depois de assinado, o contrato fica travado.
