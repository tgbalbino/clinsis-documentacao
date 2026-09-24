# Tabela de Valores para Cobrança

_Cadastro por Especialidade/Profissional/Operadora e reajuste de preço em massa_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Tabela-de-Precos-Cobranca/Documentacao_Tabela_Preco_Cobranca_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/mFThg03z-RY?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/mFThg03z-RY)

## Conteúdo completo do manual

---


_Cadastro por Especialidade/Profissional/Operadora e reajuste de preço em massa_

Versão 1.0 — 22/09/2026

A Tabela de Valores para Cobrança (Tabelas Aux. → Tab. Cobrança) define quanto cobrar do paciente por sessão particular. É essa tabela que o relatório de Cobrança de Paciente usa para calcular o valor a receber todo mês. Este manual cobre as três formas de configurar o valor (Especialidade, Profissional e Operadora) e a ferramenta de reajuste de preço em massa.


---

## Diferença em relação à Tabela de Pagamento

Ao contrário da Tabela de Valores para Pagamento, aqui não existe o conceito de várias tabelas de valores — é uma configuração única e sempre "viva" por clínica, sem histórico de versões nem status Ativo/Inativo. A tela tem três abas, cada uma com um escopo diferente de valor.

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Especialidade | Valor padrão por Especialidade, usado quando não há valor específico do profissional nem da operadora. |
| Profissional | Valor específico por Profissional × Especialidade, que sobrepõe o valor padrão só para aquele profissional. |
| Operadora | Valor específico por Operadora (convênio) × Especialidade, que sobrepõe o valor padrão para atendimentos daquela operadora. |




## Reajuste de preço em massa

O mesmo card "Manutenção rápida de preços" usado na Tabela de Pagamento aparece aqui também, nas três abas — reajustando sempre o escopo da aba em que está (Especialidade = valor padrão geral; Profissional = só daquele profissional; Operadora = só daquela operadora).


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| 1. Percentual de reajuste | Número positivo (aumento) ou negativo (desconto). Limite: maior que -100% e até 1000%. |
| 2. Campos a reajustar | Marque "Valor cobrado", "Valor social", ou os dois. |
| 3. Calcular prévia | Mostra o valor atual e o valor novo de cada especialidade — sem gravar nada ainda. |
| 4. Confirmar reajuste | Só depois de conferir a prévia, grava de fato, com uma confirmação extra. |



> ⚠️ A prévia não altera nada — só a confirmação grava de verdade. Se algum valor mudar entre a prévia e a confirmação (outra pessoa editando ao mesmo tempo), o sistema recusa e pede uma nova prévia. Linhas com Valor Social vazio não são alteradas, mesmo com o campo marcado, e cada confirmação fica registrada no log do sistema.
