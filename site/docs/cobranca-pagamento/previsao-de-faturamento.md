# Previsão de Faturamento da Agenda

Estima quanto a clínica deve faturar no mês com base na agenda, nos valores cadastrados e na probabilidade histórica de comparecimento. Serve para planejar o caixa, acompanhar a meta e conferir agenda e financeiro. O manual explica a configuração, como o valor é calculado e como conferir cada número.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Previsao-de-Faturamento/Documentacao_Previsao_de_Faturamento_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/Aft3I2vvkLk?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/Aft3I2vvkLk)

## Conteúdo completo do manual

---


_Quanto a clínica deve faturar no mês: para que serve, como configurar, de onde vêm os valores e como conferir_

Versão 1.0 — 29/09/2026

A Previsão de Faturamento da Agenda estima, semana a semana, quanto a clínica vai faturar com a agenda de um mês: soma o que já foi realizado e projeta o que ainda está agendado. Cada estimativa é guardada como uma "foto" da semana, então dá para acompanhar a evolução, ver o que mudou, conferir com o financeiro e, no fim do mês, medir o quanto a previsão acertou.


---

## Para que serve

Responde à pergunta "quanto vamos faturar neste mês?" antes de o mês terminar. Em vez de esperar o fechamento, a direção acompanha uma previsão que se atualiza toda semana e mostra: quanto já está realizado, quanto ainda vem pela agenda, quanto mudou em relação à semana anterior e desde o início do mês, e se há divergência entre o que a agenda mostra e o que o financeiro gerou.

> ⚠️ Só o perfil Administrador acessa esta funcionalidade. As previsões são calculadas apenas para agendas de mês já criadas.

## Onde fica

| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Relatórios → Cobrança → "Acessar Previsão de Faturamento da Agenda" | Tela principal: escolher a agenda, gerar a previsão, ver a evolução semanal e abrir as conferências. |
| Tabelas Aux. → Prev. Faturamento | Configuração da regra: quais status de sessão contam como faturáveis. Também aberta pelo botão "Configurar status" da tela principal. |


## 1. Configuração: quais sessões contam como faturáveis

Antes de gerar a primeira previsão é preciso dizer ao sistema quais status de sessão geram faturamento. Em Tabelas Aux. → Prev. Faturamento aparece a lista de status da agenda (Presente, Ausente, Ausente - Justificativa, Desmarcações, Remarcação…). Marque os que a clínica fatura e clique em Salvar configuração. O quadro azul confirma a regra escolhida.


> ⚠️ Cada vez que a regra é salva, ganha uma nova versão. Cada previsão gerada registra o critério usado (por exemplo, "Status faturáveis: PRESENTE, ...") e o mantém congelado — mudar a regra depois não altera as previsões antigas. Sem ao menos um status marcado, o sistema não gera previsão ("Configure ao menos um status faturável antes de gerar a previsão"). Escolha com cuidado: a maioria das clínicas marca só Presente (e, se cobra a falta, Ausente).

## 2. Como a previsão é gerada

Há duas formas, e as duas produzem a mesma "foto":

| Forma | Como funciona |
|---|---|
| Automática | Todos os dias de madrugada o sistema verifica as agendas do mês. Se a agenda ainda não tem previsão, cria a Inicial. Nas segundas-feiras cria a Semanal. Só roda para clínicas que já configuraram os status faturáveis. |
| Manual | Na tela principal escolha a Agenda (mês/ano), a Data de referência e o Tipo (Inicial, Semanal ou Fechamento) e clique em Gerar previsão. Use o tipo Fechamento ao terminar o mês para registrar o resultado final. |

Existe uma previsão de cada tipo por semana e por agenda: se ela já existe, gerar de novo apenas mostra a existente. A data de referência define até que dia as sessões contam como realizadas.

## 3. Como o valor é calculado

O sistema analisa cada marcação da agenda (um paciente, com um profissional e uma especialidade, com de 1 a 5 sessões no mês) e classifica cada sessão:

| Classificação | O que é | Entra na previsão? |
|---|---|---|
| Realizada faturável | Sessão com status marcado como faturável, com data até a data de referência. | Sim, com o valor cheio. |
| Encerrada não faturável | Sessão já encerrada com status que não é faturável (ex.: ausência não cobrada). | Não. |
| Futura | Sessões contratadas que ainda não foram encerradas (total de sessões menos as encerradas). | Sim, mas ponderadas pela probabilidade (abaixo). |

Previsão da marcação = (sessões realizadas faturáveis × valor) + (sessões futuras × valor × probabilidade). Vagas vazias na agenda não entram na previsão. O sistema calcula também o potencial máximo (se todas as sessões fossem faturadas) e o desconto previsto (diferença entre valor bruto e líquido).

## A probabilidade histórica

Nem toda sessão futura acontece, por isso ela entra na previsão multiplicada por uma probabilidade calculada com o histórico dos 6 meses anteriores: a proporção de sessões que acabaram em status faturável, com um pequeno ajuste para não oscilar demais. Se a clínica tem pouco histórico (menos de 20 sessões classificadas), usa-se o padrão de 85%. A taxa usada aparece na tela de cada previsão (no exemplo, 54,5%).

## 4. De onde vêm os valores (preço de cada sessão)

O preço vem das tabelas de Tab. Cobrança (Tabelas Aux. → Tab. Cobrança), na seguinte ordem de prioridade — a primeira que existir é usada:

| Atendimento | Ordem de busca do valor | Aparece como "Origem do preço" |
|---|---|---|
| Particular | 1º valor do Profissional + Especialidade; 2º valor da Especialidade. | Profissional/especialidade ou Especialidade |
| Convênio | 1º valor da Operadora + Especialidade; 2º valor da Especialidade. | Operadora/especialidade ou Especialidade |

Se a tabela tiver valores por Tipo de Marcação (por exemplo, Avaliação e Consulta), vale o valor do tipo da marcação; se não houver específico, usa o valor "para todos os tipos". O valor bruto é o valor cobrado; o valor líquido é o valor com desconto, quando a tabela tem um valor com desconto preenchido — caso contrário, líquido = bruto.

> ⚠️ Marcação sem nenhum preço configurado fica com valor zero e aparece em amarelo no detalhamento e na lista de Pendências ("Sem preço"). Cadastre o valor em Tab. Cobrança e gere a previsão de novo.

## 5. A tela principal


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Previsão líquida atual | Valor líquido da previsão mais recente, com o bruto logo abaixo. |
| Desde a primeira previsão | Diferença entre a previsão atual e a primeira do mês (valor e %). Verde sobe, vermelho cai. |
| Financeiro gerado | Total líquido dos títulos de Contas a Receber já gerados para esta agenda (Cobrança de Paciente) e quanto já foi recebido. |
| Agenda atual | Quantidade de pacientes, de sessões e de marcações sem preço. |
| Critério e probabilidade | Faixa de informação com os status faturáveis usados e a probabilidade histórica aplicada. |
| Evolução semanal | Uma linha por previsão: previsão bruta, descontos, líquida, variação em relação à semana anterior e desde o início, e financeiro gerado. Botões: Detalhes, Conciliação, Movimentações e Pendências. |

## 6. Como conferir

Cada linha da evolução tem quatro botões de conferência. Use esta ordem:

## Detalhes: conferir marcação por marcação

Lista cada marcação da previsão, com paciente, profissional, especialidade, modalidade (Particular ou Convênio), quantidade de sessões, realizadas e futuras, valor bruto e líquido, a origem do preço, a probabilidade e a previsão líquida. No topo: previsão filtrada, realizado operacional e futuro agendado "cheio" (sem ponderar). Dá para pesquisar e mostrar só os itens sem preço; o botão "Ver sessões" abre cada sessão com data, status e classificação.


> ⚠️ Exemplo para conferir a conta: PACIENTE 41 (Psicólogo, valor R$ 25,00) tem 4 sessões, 1 realizada e 3 futuras. Previsão = 1 × 25,00 + 3 × 25,00 × 54,5% = 25,00 + 40,91 = R$ 65,91, exatamente o valor da linha.

## Conciliação: agenda × financeiro

Compara, paciente a paciente, o realizado operacional (o que a agenda diz que foi realizado) com o financeiro líquido (o que já virou título em Contas a Receber para esta agenda), além do desconto, do valor recebido, da diferença e da quantidade de títulos. A coluna Situação indica o resultado:

| Situação | O que significa |
|---|---|
| Conciliado | Agenda e financeiro batem (diferença de até 1 centavo). |
| Sem conta a receber | Há realizado na agenda, mas nenhum título financeiro: falta gerar a cobrança do paciente. |
| Sem realização na agenda | Há título financeiro sem sessão realizada correspondente. |
| Divergência de valor | Os dois têm valor, mas diferentes. |
| Recebimento parcial | Bate, mas só parte do valor foi recebida. |


## Movimentações: o que mudou desde a semana anterior

Compara a previsão com a anterior e lista o que fez o valor subir ou cair, com totais de aumentos, reduções e variação líquida. Os motivos possíveis: Paciente incluído, Paciente removido, Preço/desconto, Status/realização, Sessões, Alteração cadastral (profissional, especialidade ou operadora) e Recálculo da probabilidade.


## Pendências: o que precisa de correção

Reúne as inconsistências que distorcem a previsão: Sem conta a receber, Sem realização na agenda, Divergência de valor, Sem preço (marcação sem valor em Tab. Cobrança) e Quantidade inconsistente (mais sessões classificadas do que as contratadas). Resolva as pendências e gere a previsão da semana seguinte.


## Fechamento e precisão: a previsão acertou?

Ao clicar em Fechamento e precisão, o sistema compara cada previsão do mês com o resultado final (o financeiro líquido gerado no fechamento, ou o da última previsão se não houver fechamento) e mostra o erro em valor e em porcentagem, além da variação desde a primeira previsão. É a forma de saber se a estimativa é confiável. Enquanto não houver faturamento financeiro no fechamento, o erro percentual aparece como "N/A".


## Passo a passo para a conferência semanal

| Passo | O que fazer |
|---|---|
| 1 | Abra Relatórios → Previsão de Faturamento da Agenda e escolha a agenda do mês. |
| 2 | Confira o critério (status faturáveis) e a probabilidade na faixa de informação. |
| 3 | Abra Pendências: corrija preços faltantes e quantidades inconsistentes. |
| 4 | Abra Conciliação com "Somente divergências" marcado e gere as cobranças que faltam (Cobrança de Paciente). |
| 5 | Abra Movimentações para entender o que explica a variação da semana. |
| 6 | No fim do mês, gere a previsão Fechamento e veja a precisão. |

## Pontos de atenção

> ⚠️ Cada previsão é uma foto: o que muda na agenda depois de gerada não altera aquela previsão — gere a próxima semana para refletir a mudança. Previsões geradas antes da etapa de conciliação podem não ter os títulos financeiros nem as sessões detalhadas, e aparecem vazias nessas telas.

> ⚠️ O financeiro gerado considera apenas os títulos de Contas a Receber criados pela Cobrança de Paciente para a agenda; recebimentos de Contrato, Checkin e lançamentos manuais não entram nessa comparação.
