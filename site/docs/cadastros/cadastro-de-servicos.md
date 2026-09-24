# Cadastro de Serviços

_Para que serve e onde é utilizado (Tabelas Aux. → Serviços)_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Cadastro-de-Servicos/Documentacao_Cadastro_Servicos_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/uotROr-rj6s?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/uotROr-rj6s)

## Conteúdo completo do manual

---


_Para que serve e onde é utilizado (Tabelas Aux. → Serviços)_

Versão 1.0 — 22/09/2026

Um Serviço é um item simples de "nome + valor" — como um item de tabela de valores — usado como base para montar os itens de um Contrato. Este manual explica o cadastro e, principalmente, onde ele entra em uso dentro do sistema.


---

## O que é um Serviço

Pense num Serviço como um item de catálogo: um nome ("Sessão de Fisioterapia", "Avaliação Inicial", "Pacote 10 sessões") e um valor sugerido. Ao montar um Contrato, em vez de digitar manualmente a descrição e o valor de cada item, o usuário busca um Serviço já cadastrado e usa isso como ponto de partida.

O cadastro é bem enxuto: só Descrição e Preço. Não existe ativo/inativo, categoria, nem vínculo com convênio — e não há como excluir um Serviço já cadastrado pela tela, ele permanece disponível permanentemente na lista.



## Onde é utilizado: exclusivamente no módulo Contrato

> ⚠️ Apesar do nome "Serviço" sugerir algo amplo (faturamento, convênio, guias), na prática ele é usado em um único lugar do sistema: a aba "Serviços" dentro do cadastro de Contrato. Guia de Faturamento, Cobrança de Paciente e Tabela de Valores de convênio usam outro conceito (Especialidade), sem nenhuma relação com este cadastro.

Dentro de um Contrato, cada linha de serviço contratado (Serviço + Quantidade de sessões + Valor da sessão) fica registrada, e o Valor Total do Contrato é a soma de todas essas linhas — calculado automaticamente pelo sistema, sem que o usuário precise somar nada manualmente.





## Outros pontos onde o Serviço aparece

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Cálculo do Valor Total do Contrato | A soma de todas as linhas de serviço do contrato define o valor total dele, usado depois para comparar com os pagamentos/acertos lançados ("Falta Acertar"). |
| Renovação de Contrato | Ao renovar um contrato, o sistema copia automaticamente os mesmos Serviços/quantidades/valores para o contrato novo. Se o contrato antigo não tiver nenhum serviço, a renovação é bloqueada. |
| Impressão do Contrato | No layout de impressão do contrato (Tabelas Aux. → Layout Contrato), existe um placeholder "TabelaServicos" que renderiza a lista de serviços contratados no PDF/documento impresso. |

> ⚠️ Um Serviço só pode ser adicionado, alterado ou removido de um contrato enquanto ele estiver ativo e ainda não assinado (nem com uma solicitação de assinatura eletrônica em andamento) — depois de assinado, o contrato fica travado.
