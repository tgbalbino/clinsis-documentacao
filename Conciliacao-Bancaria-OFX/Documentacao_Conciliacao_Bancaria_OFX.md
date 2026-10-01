# Conciliação Bancária (OFX)

_Como conferir o extrato do banco com os Movimentos Financeiros do ClinSis usando o arquivo OFX_

Versão 1.0 — 30/09/2026

A Conciliação Bancária (OFX) confere o extrato do banco com os Movimentos Financeiros do ClinSis. Você baixa o extrato no internet banking em formato OFX, envia o arquivo ao sistema e ele mostra, linha por linha, o que já está lançado no ClinSis, o que só aparece no banco e o que só aparece no sistema. As linhas que batem podem ser conciliadas de uma só vez, sem digitar nada.

Assista ao vídeo narrado desta rotina: [https://youtu.be/17EE36VWZHM](https://youtu.be/17EE36VWZHM)

---

## Para que serve

Conciliar é confirmar que cada movimento registrado no sistema realmente apareceu no banco, com o mesmo valor. Isso evita diferenças no saldo, pagamentos lançados em duplicidade ou recebimentos que nunca caíram na conta. No ClinSis a conciliação é feita por Conta Financeira: você escolhe a conta, envia o extrato dela e confere.

> ⚠️ Só o perfil Administrador acessa esta tela. A leitura do arquivo não grava nada: os movimentos só são marcados como conciliados quando você clica em Conciliar marcados.

## Onde fica no sistema

Menu Financeiro → Movimentos → Conciliação OFX. O resultado da conciliação aparece em Financeiro → Movimentos → Movimentos Financeiros, na coluna Conciliado.

![Conciliação Bancária (OFX): escolha a conta financeira, o arquivo do extrato e clique em Ler extrato.](00-tela-inicial.png)

_Conciliação Bancária (OFX): escolha a conta financeira, o arquivo do extrato e clique em Ler extrato._

## Antes de começar

| Item | O que conferir |
|---|---|
| Conta Financeira | A conta precisa estar cadastrada em Cadastros → Conta Financeira. Se possível, preencha banco, agência e conta: o sistema usa esses dados para avisar quando o arquivo é de outra conta. |
| Arquivo OFX | No internet banking, procure por Extrato → Exportar (ou Salvar) e escolha o formato OFX (às vezes chamado de "Money" ou "Quicken"). Tamanho máximo: 2 MB. |
| Lançamentos no sistema | Os pagamentos e recebimentos já devem estar registrados no ClinSis (baixas de Contas a Pagar e a Receber e transferências). A conciliação só liga o que já existe; ela não cria lançamentos. |

O ClinSis tem leitura própria para Banco do Brasil, Santander, Sicredi e Sicoob. Arquivos de outros bancos usam a leitura padrão do formato OFX e costumam funcionar igual.

![Movimentos Financeiros antes da conciliação: a coluna Conciliado mostra Sim ou Não para cada movimento.](01-movimentos-antes.png)

_Movimentos Financeiros antes da conciliação: a coluna Conciliado mostra Sim ou Não para cada movimento._

## Passo a passo

| Passo | O que fazer |
|---|---|
| 1 | Em Conta Financeira, escolha a conta do extrato. |
| 2 | Em Arquivo do extrato (.ofx), clique em Choose File (Escolher arquivo) e selecione o OFX baixado do banco. |
| 3 | Clique em Ler extrato. O sistema mostra o banco, a agência, a conta, o período e o saldo final do arquivo, e compara cada linha com os movimentos da conta. |
| 4 | Confira a lista (veja as situações abaixo). As linhas encontradas já vêm marcadas; desmarque as que não concordar. |
| 5 | Clique em Conciliar marcados. O sistema confirma quantos movimentos foram conciliados e recarrega a lista. |

![Conta e arquivo escolhidos, prontos para clicar em Ler extrato.](02-arquivo-escolhido.png)

_Conta e arquivo escolhidos, prontos para clicar em Ler extrato._

![Resultado da leitura: cada linha do extrato com a situação e o movimento do sistema que combina com ela.](03-resultado.png)

_Resultado da leitura: cada linha do extrato com a situação e o movimento do sistema que combina com ela._

## Como o sistema encontra o par

Para cada linha do extrato, o ClinSis procura um movimento da mesma conta que ainda não esteja conciliado, seguindo estas regras:

| Regra | Detalhe |
|---|---|
| Mesmo tipo | Crédito do extrato com Entrada do sistema; débito com Saída. |
| Mesmo valor | O valor precisa ser exatamente igual (em reais e centavos). |
| Data próxima | A data do movimento pode diferir até 3 dias da data do extrato (o banco costuma compensar depois do lançamento). |
| Um para um | Cada movimento do sistema é usado uma única vez. Se houver vários candidatos, vale o de data mais próxima e, em empate, o de histórico mais parecido. |

> ⚠️ O sistema apenas sugere. Quem confirma é você. Antes de clicar em Conciliar marcados, olhe principalmente os valores repetidos (por exemplo, três recebimentos de R$ 150,00), pois o par sugerido pode não ser o que você imaginava.

## As situações de cada linha

| Situação | Significado | O que fazer |
|---|---|---|
| Encontrado no sistema | Existe um movimento com mesmo tipo, valor e data próxima. A linha vem marcada. | Conferir e manter marcada para conciliar. |
| Já conciliado | Essa linha do extrato já foi ligada a um movimento em outra conciliação. | Nada. Reenviar o mesmo arquivo é seguro: nada é conciliado duas vezes. |
| Só no extrato | O banco registrou, mas não há movimento equivalente no sistema (por exemplo, uma tarifa ou um TED recebido que ninguém lançou). | Registrar o lançamento no ClinSis (por exemplo, dando baixa na conta a pagar ou a receber correspondente) e ler o extrato de novo. |
| Só no sistema | Aparece na tabela "Movimentos do sistema sem lançamento no extrato": o movimento existe no período do arquivo, mas o banco não trouxe uma linha igual. | Verificar se o valor ou a data estão diferentes do banco, se ainda não compensou, ou se foi lançado na conta errada. |

![Depois de Conciliar marcados, o sistema avisa quantos movimentos foram conciliados e atualiza a lista.](04-conciliando-aviso.png)

_Depois de Conciliar marcados, o sistema avisa quantos movimentos foram conciliados e atualiza a lista._

## Depois de conciliar

Em Movimentos Financeiros, os movimentos conciliados passam a mostrar Sim na coluna Conciliado, e o quadro Conciliação no topo mostra o valor conciliado, o valor não conciliado e o percentual. Se conciliar uma linha por engano, use o botão amarelo Desfazer conciliação do movimento: ele volta a ficar disponível e a linha do extrato também.

![Movimentos Financeiros depois da conciliação: movimentos com Sim, e os que ficaram pendentes com Não.](06-movimentos-depois.png)

_Movimentos Financeiros depois da conciliação: movimentos com Sim, e os que ficaram pendentes com Não._

## Avisos e erros

| Mensagem | Causa | O que fazer |
|---|---|---|
| A agência (ou conta, ou banco) do arquivo é diferente da conta selecionada | O OFX é de outra conta bancária, ou o cadastro da Conta Financeira está com agência/conta diferente da real. | Confirme se escolheu a conta certa. Se o cadastro estiver errado, corrija em Cadastros → Conta Financeira. O sistema tolera o dígito verificador. |
| Arquivo não é um OFX válido | O arquivo escolhido não é um extrato OFX (por exemplo, é um PDF ou CSV renomeado). | Baixe novamente no banco escolhendo o formato OFX. |
| O arquivo não possui transações | O período do extrato está vazio. | Gere o extrato de um período com movimentação. |
| Arquivo OFX muito grande | Mais de 2 MB. | Gere o extrato por período menor (por exemplo, mês a mês). |
| Transação do extrato já conciliada com outro movimento | Duas pessoas conciliaram a mesma linha ao mesmo tempo. | Leia o extrato de novo para ver a situação atual. |

![Aviso amarelo quando o arquivo é de outra agência: a leitura continua, mas confira a conta antes de conciliar.](07-aviso-conta-diferente.png)

_Aviso amarelo quando o arquivo é de outra agência: a leitura continua, mas confira a conta antes de conciliar._

![Mensagem quando o arquivo escolhido não é um OFX válido.](08-arquivo-invalido.png)

_Mensagem quando o arquivo escolhido não é um OFX válido._

## Boas práticas

| Recomendação | Por quê |
|---|---|
| Concilie com frequência (semanal ou mensal) | Períodos menores têm menos linhas e as diferenças são mais fáceis de achar. |
| Registre tudo no sistema antes de ler o extrato | Quanto mais lançamentos já estiverem no ClinSis, mais linhas são encontradas automaticamente. |
| Confira valores repetidos | Movimentos iguais podem ser ligados a linhas diferentes das que você imaginava. |
| Não altere o arquivo OFX | O identificador de cada transação (FITID) vem do banco e é usado para não conciliar a mesma linha duas vezes. |
| Use uma Conta Financeira por conta bancária | A conciliação compara só os movimentos da conta escolhida. |
