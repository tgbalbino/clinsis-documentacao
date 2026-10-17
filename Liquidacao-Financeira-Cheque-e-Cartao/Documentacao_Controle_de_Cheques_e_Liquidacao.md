# Controle de Cheques e Liquidação Financeira

_Cheque e cartão: o dinheiro só entra na conta quando é compensado ou repassado_

Versão 1.0 — 06/10/2026

Quando o paciente paga com cheque ou com cartão de crédito, o título é quitado na hora, mas o dinheiro só chega à conta da clínica dias depois. Este manual mostra como o ClinSis controla esse intervalo: cada cheque é cadastrado com seus dados (banco, agência, conta, série, número e emitente), pode pagar mais de um título, e a conta só é movimentada quando o cheque é compensado. No cartão, cada parcela repassada pelo banco é confirmada separadamente. Também explica a devolução do cheque com nova cobrança e o cheque emitido pela clínica nos pagamentos.

Assista ao vídeo narrado desta rotina: [https://youtu.be/HwchLf2HIFE](https://youtu.be/HwchLf2HIFE)

---

## A ideia: baixar o título não é o dinheiro entrar

Com dinheiro, PIX ou débito, a baixa do título já lança o valor na conta financeira. Com cheque e cartão de crédito é diferente: o título é quitado na baixa, mas o saldo da conta só muda quando o banco de fato compensa o cheque ou repassa a parcela do cartão. Até lá, o valor aparece como a receber (ou a pagar), sem inflar o saldo da conta.

Cada forma de pagamento escolhe o seu comportamento em Tabelas Aux. → Formas de Pagamento:

| Política | O que acontece na baixa | Exemplo |
|---|---|---|
| Imediata | O valor entra na conta financeira na hora. | Dinheiro, PIX, débito |
| Compensação manual | O título é quitado e o cheque fica em carteira até ser compensado na tela Cheques. | Cheque |
| Repasse programado | O título é quitado e o banco repassa em parcelas, com prazo, intervalo e taxa do contrato. | Cartão de crédito |

![Formas de Pagamento: a política de cada forma define se o dinheiro entra na hora ou depois.](01-config-formas.png)

_Formas de Pagamento: a política de cada forma define se o dinheiro entra na hora ou depois._

## Receber com cheque: cadastrando o cheque na baixa

Na baixa de uma conta a receber, escolha a forma Cheque. Aparece o quadro Cheque recebido, com duas opções: Cheque novo (cadastra o cheque agora) ou Cheque já cadastrado (usa um cheque que já está em carteira). A conta financeira da baixa é o caixa, pois o cheque ainda não foi depositado.

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Banco, Agência e Conta | Dados da conta do emitente, impressos no cheque. O banco vem da lista de bancos. | Cheque.IdBanco / Agencia / Conta |
| Série e Nº do cheque | Identificação do cheque. A série é opcional. | Cheque.Serie / Numero |
| Valor do cheque | Valor de face. Em branco vale o valor da baixa. Informe o total quando o mesmo cheque pagar mais de um título. | Cheque.Valor |
| Emissão | Data em que o cheque foi emitido (opcional, não pode ser futura). | Cheque.DataEmissao |
| Bom para | Data prevista de compensação (cheque pré-datado). É a previsão usada nas listas e no fluxo de caixa. | Cheque.BomPara |
| CPF/CNPJ do emitente | Quem assinou o cheque. A pessoa precisa estar cadastrada: ao digitar o CPF/CNPJ o sistema mostra o nome ou oferece o link para cadastrar. | Cheque.IdPessoaEmitente |

![Baixa de R$ 450,00 com cheque novo de R$ 700,00: o emitente foi localizado pelo CPF.](02-baixa-cheque-novo.png)

_Baixa de R$ 450,00 com cheque novo de R$ 700,00: o emitente foi localizado pelo CPF._

![Confirmação da baixa. A conta a receber fica quitada, mas nenhum valor entra na conta ainda.](03-baixa-cheque-confirmacao.png)

_Confirmação da baixa. A conta a receber fica quitada, mas nenhum valor entra na conta ainda._

> ⚠️ O valor do cheque não pode ser menor que o valor da baixa, e o "bom para" não pode ser anterior à data da baixa.

## Um cheque pagando mais de um título

O paciente pode pagar dois títulos com um único cheque. Na primeira baixa cadastre o cheque com o valor total (R$ 700,00 neste exemplo); na segunda, escolha Cheque já cadastrado. O saldo do cheque diminui a cada título.

Como o sistema reconhece o mesmo cheque: pela combinação de banco, agência, conta, série e número. Zeros à esquerda e pontuação são ignorados, então 000482 e 482 são o mesmo cheque. O mesmo número em outra conta ou série é outro cheque. Se você tentar cadastrar de novo um cheque que já existe, a tela avisa e oferece o botão Usar este cheque.

![O cheque 482 foi digitado de novo: a tela reconhece o cheque 000482 já cadastrado e oferece usá-lo.](04-cheque-duplicado.png)

_O cheque 482 foi digitado de novo: a tela reconhece o cheque 000482 já cadastrado e oferece usá-lo._

![Cheque já cadastrado selecionado, com o saldo disponível: R$ 250,00 abatidos dos R$ 700,00.](05-cheque-da-carteira.png)

_Cheque já cadastrado selecionado, com o saldo disponível: R$ 250,00 abatidos dos R$ 700,00._

## A tela Cheques

Acesso em Financeiro → Movimentos → Cheques. Reúne todos os cheques recebidos e emitidos, com o valor, o saldo ainda sem título, a quantidade de títulos e o "bom para". Cheques vencidos aparecem em vermelho.

![Lista de cheques em carteira: o cheque 000482 de R$ 700,00 paga 2 títulos e não tem saldo.](06-lista-cheques.png)

_Lista de cheques em carteira: o cheque 000482 de R$ 700,00 paga 2 títulos e não tem saldo._

| Filtro | Para que serve |
|---|---|
| Situação | Em carteira, Compensado, Devolvido ou Cancelado. |
| Tipo | Cheques recebidos dos pacientes ou emitidos pela clínica. |
| Número | Procura pelo número ignorando zeros à esquerda. |
| Banco e Emitente | Por banco ou por nome/CPF/CNPJ de quem assinou. |
| Bom para (período) | Cheques previstos para compensar em um intervalo. |
| Somente vencidos | Cheques em carteira cujo "bom para" já passou. |
| Com saldo a vincular | Cheques que ainda cabem em novos títulos. |

| Situação | Significado |
|---|---|
| Em carteira | Cadastrado e aguardando compensação. Aceita novos títulos enquanto tiver saldo. |
| Compensado | O banco compensou: o valor foi lançado na conta financeira. |
| Devolvido | O banco devolveu (sem fundos, por exemplo). Os títulos continuam quitados. |
| Cancelado | Cheque lançado por engano, sem títulos. A mesma numeração pode ser cadastrada de novo. |

O botão Ver abre o detalhe do cheque com os títulos pagos por ele.

![Detalhe do cheque: os dois títulos pagos, com paciente, valor e situação.](07-detalhe-cheque.png)

_Detalhe do cheque: os dois títulos pagos, com paciente, valor e situação._

## Liquidações Financeiras e o cheque

A tela Liquidações Financeiras lista tudo o que está aguardando entrar ou sair da conta: cheques e parcelas de cartão. Para as linhas de cheque aparece o botão Ver cheque no lugar de liquidar, devolver e cancelar: o cheque é compensado, devolvido e cancelado pela tela Cheques, de uma só vez para todos os títulos, gerando um único movimento no extrato mesmo quando paga vários títulos. Dá para procurar um cheque pelo número ou pela pessoa.

![Liquidações: as duas linhas do cheque mostram o número, a pessoa e "Ver cheque".](08-liquidacoes-cheque.png)

_Liquidações: as duas linhas do cheque mostram o número, a pessoa e "Ver cheque"._

## Compensar o cheque

Quando o banco compensar, clique em Compensar. Informe a data da compensação e a conta do depósito (onde o cheque foi depositado). O cheque só pode ser compensado quando todo o seu valor estiver vinculado a títulos; se sobrar saldo, vincule o restante em outra baixa ou ajuste o valor do cheque.

![Compensação do cheque de R$ 700,00 na conta Banco Brasil.](09-compensar-cheque.png)

_Compensação do cheque de R$ 700,00 na conta Banco Brasil._

![O cheque passa para Compensado.](10-cheque-compensado.png)

_O cheque passa para Compensado._

Em Movimentos Financeiros aparece um único lançamento de entrada, "Compensação de cheque", pelo valor total do cheque, pronto para a conciliação com o extrato do banco.

![Um único movimento de R$ 700,00 pela compensação do cheque, mesmo tendo pago dois títulos.](11-movimentos.png)

_Um único movimento de R$ 700,00 pela compensação do cheque, mesmo tendo pago dois títulos._

## Devolução do cheque

Se o banco devolver o cheque, use Devolver (em carteira ou já compensado). Informe a data e o motivo. Se o cheque já tinha sido compensado, o sistema cria um movimento inverso (estorno) e preserva o original. Os títulos pagos continuam quitados; para cobrar o paciente, o sistema pode gerar uma nova cobrança por título, com o vencimento escolhido e uma tarifa opcional (somada apenas à primeira cobrança).

![Devolução com a prévia das cobranças: R$ 465,00 (450 + tarifa de 15) e R$ 250,00.](12-devolver-cheque.png)

_Devolução com a prévia das cobranças: R$ 465,00 (450 + tarifa de 15) e R$ 250,00._

![O cheque devolvido. O estorno foi lançado uma única vez.](13-cheque-devolvido.png)

_O cheque devolvido. O estorno foi lançado uma única vez._

![As novas cobranças aparecem em Contas a Receber com a origem "Cobrança de devolução".](14-cobrancas-devolucao.png)

_As novas cobranças aparecem em Contas a Receber com a origem "Cobrança de devolução"._

> ⚠️ A devolução vale para o cheque inteiro: não é possível devolver só um dos títulos. O cheque devolvido deixa de aceitar novos títulos.

## Alterar e cancelar um cheque

Alterar muda o valor, a emissão, o "bom para" e a observação de um cheque em carteira; a identificação (banco, agência, conta, série e número) não muda. O valor não pode ficar abaixo do que já foi vinculado a títulos, e o novo "bom para" vale para todos os títulos do cheque.

Cancelar serve para um cheque lançado por engano e sem nenhum título. Se houver títulos, cancele antes as baixas deles. Cheque cancelado libera a mesma numeração para um novo cadastro.

## Pagar com cheque emitido pela clínica

Na baixa de uma conta a pagar com a forma Cheque, informe a conta sacada (a conta bancária da clínica contra a qual o cheque é emitido), a série, o número e o "bom para". Banco, agência e conta do cheque vêm da conta sacada. Assim como no recebimento, o mesmo cheque pode pagar mais de uma conta a pagar.

![Pagamento do aluguel com cheque emitido contra a conta Banco Brasil.](21-pagar-cheque-emitido.png)

_Pagamento do aluguel com cheque emitido contra a conta Banco Brasil._

![O cheque emitido aparece na tela Cheques como "Emitido", em carteira.](22-lista-cheque-emitido.png)

_O cheque emitido aparece na tela Cheques como "Emitido", em carteira._

![Alterar o cheque: valor, emissão, "bom para" e observação.](23-alterar-cheque.png)

_Alterar o cheque: valor, emissão, "bom para" e observação._

Quando o cheque for descontado pelo fornecedor, use Compensar: o valor sai da conta sacada automaticamente, sem precisar escolher a conta.

![Compensação do cheque emitido: a saída é lançada na conta sacada.](24-compensar-cheque-emitido.png)

_Compensação do cheque emitido: a saída é lançada na conta sacada._

> ⚠️ Um cheque recebido de paciente ainda não pode ser repassado a fornecedor (endosso) nos pagamentos. Em pagamentos use apenas cheques emitidos pela clínica.

## Cartão de crédito parcelado

Na baixa com cartão de crédito, escolha a quantidade de parcelas. O aviso mostra como o banco vai repassar: uma parcela por mês, a primeira na previsão e as demais conforme o intervalo e a taxa do contrato da forma.

![Baixa de R$ 900,00 no cartão em 3x: o aviso informa o repasse em 3 parcelas.](15-baixa-cartao.png)

_Baixa de R$ 900,00 no cartão em 3x: o aviso informa o repasse em 3 parcelas._

![Cada parcela é uma liquidação separada, com a previsão de repasse e a taxa prevista.](16-parcelas-repasse.png)

_Cada parcela é uma liquidação separada, com a previsão de repasse e a taxa prevista._

Quando o banco repassar uma parcela, clique em Liquidar naquela linha. O sistema sugere o valor líquido (parcela menos a taxa prevista); confira com o que o banco creditou e ajuste se for diferente.

![Liquidação da parcela 1/3 com a taxa prevista pelo contrato.](17-liquidar-parcela.png)

_Liquidação da parcela 1/3 com a taxa prevista pelo contrato._

![Parcela liquidada: o movimento de entrada é pelo valor líquido e indica a parcela.](18-parcela-liquidada.png)

_Parcela liquidada: o movimento de entrada é pelo valor líquido e indica a parcela._

Cada parcela pode ser devolvida (chargeback) separadamente, gerando a nova cobrança só daquele valor.

> ⚠️ Não é possível cancelar a baixa de um título cujo cartão já teve parcela repassada, nem a de um cheque já compensado: o sistema bloqueia e explica o motivo.

![Tentativa de cancelar a baixa de um cartão com parcela já repassada: bloqueada.](20-cancelar-bloqueado.png)

_Tentativa de cancelar a baixa de um cartão com parcela já repassada: bloqueada._

## Filtros e fluxo de caixa projetado

A tela de Liquidações pode ser filtrada por situação, direção (entrada ou saída), período de previsão, conta financeira, número do cheque ou documento, pessoa e "somente vencidas". Os cartões no topo somam o que está a receber e a pagar, destacando o que já venceu.

![Filtros por conta financeira e período de previsão.](25-filtros.png)

_Filtros por conta financeira e período de previsão._

O Fluxo de Caixa passa a mostrar o previsto: os cheques e as parcelas de cartão entram na data prevista, separados do que já foi realizado.

![Fluxo de caixa com o previsto dos cheques e das parcelas de cartão.](26-fluxo-projetado.png)

_Fluxo de caixa com o previsto dos cheques e das parcelas de cartão._

## Resumo das regras

| Situação | O que o sistema faz |
|---|---|
| Baixa com cheque | Quita o título, cadastra (ou usa) o cheque e não mexe no saldo da conta. |
| Cheque que paga vários títulos | O saldo do cheque diminui a cada título; a compensação só é liberada com o valor todo vinculado. |
| Compensação | Um único movimento pelo valor do cheque, na conta do depósito (ou na conta sacada, no emitido). |
| Devolução | Estorno único se já compensado; títulos continuam quitados; nova cobrança por título, se escolhida. |
| Cheque duplicado | Mesmo banco, agência, conta, série e número (ignorando zeros) é o mesmo cheque: não cadastra de novo. |
| Cancelar baixa | Cheque em carteira: cancela e reabre o saldo. Cheque compensado ou cartão repassado: bloqueado. |
| Cartão | Uma liquidação por parcela, com taxa e prazo do contrato; liquidar e devolver por parcela. |
