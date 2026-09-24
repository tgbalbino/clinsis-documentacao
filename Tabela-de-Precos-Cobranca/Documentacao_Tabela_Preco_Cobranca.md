# Tabela de Preços para Cobrança

_Cadastro por Especialidade/Profissional/Operadora e reajuste de preço em massa_

Versão 1.0 — 22/09/2026

A Tabela de Preços para Cobrança (Tabelas Aux. → Tab. Cobrança) define quanto cobrar do paciente por sessão particular. É essa tabela que o relatório de Cobrança de Paciente usa para calcular o valor a receber todo mês. Este manual cobre as três formas de configurar o valor (Especialidade, Profissional e Operadora) e a ferramenta de reajuste de preço em massa.

Assista ao vídeo narrado desta rotina: [https://youtu.be/mFThg03z-RY](https://youtu.be/mFThg03z-RY)
---

## Diferença em relação à Tabela de Pagamento

Ao contrário da Tabela de Preços para Pagamento, aqui não existe o conceito de várias tabelas/vigências — é uma configuração única e sempre "viva" por clínica, sem histórico de versões nem status Ativo/Inativo. A tela tem três abas, cada uma com um escopo diferente de valor.

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Especialidade | Valor padrão por Especialidade, usado quando não há valor específico do profissional nem da operadora. | ConfigCobrancaEspecPagto |
| Profissional | Valor específico por Profissional × Especialidade, que sobrepõe o valor padrão só para aquele profissional. | ConfigCobrancaProfEspecPagto |
| Operadora | Valor específico por Operadora (convênio) × Especialidade, que sobrepõe o valor padrão para atendimentos daquela operadora. | ConfigCobrancaOperadoraEspecPagto |

![Aba "Especialidade": valor padrão (Valor e Valor Social) por especialidade, com filtro e exportação em CSV.](00-aba-especialidade.png)

_Aba "Especialidade": valor padrão (Valor e Valor Social) por especialidade, com filtro e exportação em CSV._

![Aba "Profissional": ao abrir um profissional, aparece a grade de valores específicos dele.](05-modal-valores-profissional.png)

_Aba "Profissional": ao abrir um profissional, aparece a grade de valores específicos dele._

![Aba "Operadora": escolha a operadora no topo e configure o valor por especialidade específico para ela.](06-aba-operadora.png)

_Aba "Operadora": escolha a operadora no topo e configure o valor por especialidade específico para ela._

## Reajuste de preço em massa

O mesmo card "Manutenção rápida de preços" usado na Tabela de Pagamento aparece aqui também, nas três abas — reajustando sempre o escopo da aba em que está (Especialidade = valor padrão geral; Profissional = só daquele profissional; Operadora = só daquela operadora).

![Botão "Reajustar preços" expande o formulário: percentual e quais campos reajustar (Valor cobrado e/ou Valor social).](01-reajuste-formulario-aberto.png)

_Botão "Reajustar preços" expande o formulário: percentual e quais campos reajustar (Valor cobrado e/ou Valor social)._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| 1. Percentual de reajuste | Número positivo (aumento) ou negativo (desconto). Limite: maior que -100% e até 1000%. | ReajustePrecoController.cs |
| 2. Campos a reajustar | Marque "Valor cobrado", "Valor social", ou os dois. | reajuste-preco.component.html |
| 3. Calcular prévia | Mostra o valor atual e o valor novo de cada especialidade — sem gravar nada ainda. | ReajustePreco/cobranca(/profissional\|/operadora)/simular |
| 4. Confirmar reajuste | Só depois de conferir a prévia, grava de fato, com uma confirmação extra. | ReajustePreco/cobranca(/profissional\|/operadora)/confirmar |

![Prévia de um reajuste de 8%: Valor atual/novo e Social atual/novo de cada especialidade, em verde os valores que mudam.](02-reajuste-previa.png)

_Prévia de um reajuste de 8%: Valor atual/novo e Social atual/novo de cada especialidade, em verde os valores que mudam._

!["11 valor(es) reajustado(s) com sucesso" — grade já atualizada com os novos valores.](03-reajuste-confirmado.png)

_"11 valor(es) reajustado(s) com sucesso" — grade já atualizada com os novos valores._

> ⚠️ A prévia não altera nada — só a confirmação grava de verdade. Se algum valor mudar entre a prévia e a confirmação (outra pessoa editando ao mesmo tempo), o sistema recusa e pede uma nova prévia. Linhas com Valor Social vazio não são alteradas, mesmo com o campo marcado, e cada confirmação fica registrada no log do sistema.
