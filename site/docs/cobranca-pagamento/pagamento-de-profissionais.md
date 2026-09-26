# Pagamento de Profissionais

_Calcular e gerar, de uma vez, o repasse de todos os profissionais do mês_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Pagamento-de-Profissionais/Documentacao_Pagamento_de_Profissionais_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/0dVv7ctVDPE?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/0dVv7ctVDPE)

## Conteúdo completo do manual

---


_Calcular e gerar, de uma vez, o repasse de todos os profissionais do mês_

Versão 1.1 — 26/09/2026

Pagamento de Profissionais calcula, a partir dos atendimentos realizados no mês, quanto a clínica deve repassar para cada profissional — e gera a Conta a Pagar correspondente com um clique, em vez de lançar uma conta manual pra cada profissional. Para isso funcionar, é preciso configurar ANTES uma Tabela de Valores para Pagamento (Tabelas Aux. → Tab. Pagamento), com o valor pago por sessão/atendimento e vinculando o mês (Agenda) que vai usar essa tabela.


---

## Configuração prévia: Tabela de Valores para Pagamento

Em Tabelas Aux. → Tab. Pagamento fica a lista de "tabelas de valores" — cada uma agrupa um conjunto de valores usados para calcular o repasse dos profissionais. Ao abrir uma tabela (botão da engrenagem), três abas organizam a configuração:


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Aba Agenda | Quais competências (mês/ano) usam esta tabela de valores. Sem vincular o mês aqui, o sistema recusa gerar o pagamento daquele mês. |
| Aba Especialidades | Valor padrão por Especialidade (ex.: Fisioterapeuta, Psicólogo), aplicado a todos os profissionais daquela especialidade que não tiverem um valor específico. |
| Aba Profissionais | Valor específico por Profissional + Especialidade, que sobrepõe o valor padrão da aba Especialidades quando presente. |



## "Valor" e "Valor Convênio": qual dos dois é usado no cálculo

Tanto na aba Especialidades quanto na aba Profissionais, cada linha tem dois campos de valor: Valor e Valor Convênio. Pela lógica do nome, seria esperado que o sistema usasse automaticamente o Valor Convênio quando o atendimento foi feito por um paciente de convênio, e o Valor normal quando foi particular.


> ⚠️ Isso não acontece hoje. Conferindo o cálculo do relatório, o sistema sempre usa o campo Valor para calcular o repasse, independentemente do atendimento ser particular ou de convênio — o campo Valor Convênio fica salvo no cadastro, mas não entra em nenhuma conta. Na prática, preencher o Valor Convênio hoje não muda o valor pago ao profissional. Recomendamos não contar com uma diferenciação automática por convênio nesta tela e alinhar com a equipe de desenvolvimento se essa distinção deveria estar ativa.

## "Tipo de Marcação": valores diferentes por tipo de atendimento

O campo Tipo de Marcação (ex.: "Todos os tipos", "Avaliação", "Consulta/Sessão") permite cadastrar um valor de pagamento diferente conforme o tipo de marcação escolhido no agendamento do paciente. Por padrão existe uma linha "Todos os tipos", que serve de valor genérico; é possível clicar no botão "+" e adicionar uma linha específica para "Avaliação" ou "Consulta/Sessão" com um valor próprio.

Exemplo real do ambiente de testes: na aba Especialidades, "Terapeuta Ocupacional" tem duas linhas: "Todos os tipos" = R$ 2,00 e "Avaliação" = R$ 3,00 (ver print acima) — um agendamento de Avaliação paga R$ 3,00, e qualquer outro tipo (Consulta/Sessão) paga R$ 2,00 pela linha genérica.


## "Tipo de Cobrança" da Especialidade: por sessão ou por paciente

Esse campo não fica na Tabela de Valores — ele é configurado no cadastro da própria Especialidade (Cadastros → Especialidades), no campo Tipo de Cobrança, com duas opções: Por Sessão ou Paciente. Mesmo estando em outra tela, ele afeta diretamente como o Pagamento de Profissionais conta as sessões:



| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Por Sessão | O profissional é pago por cada sessão cujo status esteja marcado no filtro do relatório (ver "Quais sessões entram no pagamento"). Se o agendamento tem 5 sessões previstas e 3 estão com um status marcado, contam 3 sessões pagáveis. |
| Paciente | O profissional é pago no máximo 1 vez por agendamento/paciente naquele período, não importa quantas sessões (1 a 5) ele teve — é um valor "por pacote", não por sessão avulsa. O campo "Considera Marcação" do relatório define se o pacote exige ao menos uma sessão num status marcado. |

Exemplo numérico: Especialidade "Fisioterapia" com Valor = R$ 50,00 e um agendamento com 5 sessões previstas no mês, das quais 3 foram confirmadas como realizadas. Se o Tipo de Cobrança da especialidade for Por Sessão, o valor total é 3 × R$ 50 = R$ 150,00. Se for Paciente, o valor total é 1 × R$ 50 = R$ 50,00 — paga uma única vez pelo pacote do mês, mesmo que várias sessões tenham ocorrido.

## Quando criar uma nova Tabela de Valores

Seria natural imaginar que, ao reajustar valores, bastaria criar uma nova Tabela de Valores e vincular só os meses futuros a ela, preservando os valores antigos dos meses já vinculados à tabela anterior. É importante entender como o sistema realmente se comporta hoje antes de fazer isso:

> ⚠️ O cálculo do relatório usa sempre a Tabela de Valores mais recentemente cadastrada que estiver marcada como "Ativo = Sim" para toda a clínica — e não, especificamente, a tabela vinculada àquele mês na aba Agenda. A aba Agenda só controla se aquele mês pode ou não entrar no cálculo (precisa estar vinculado a alguma tabela), mas os valores aplicados vêm sempre da tabela ativa mais nova. Ou seja: editar um Valor numa tabela existente, ou ativar uma tabela nova, pode alterar o cálculo de meses antigos que ainda não tiveram o pagamento gerado — a única coisa que realmente fica "congelada" é a Conta a Pagar já gerada; uma vez gerada, ela não é recalculada.

Na prática, para reajustar valores com segurança: gere e confira a Conta a Pagar dos meses fechados antes de alterar valores ou ativar uma tabela nova, já que o sistema recalcula pelo valor mais recente ativo no momento em que o relatório é rodado — não pelo valor vigente na época do atendimento. Se notar valores de meses antigos mudando ao reajustar uma tabela nova, isso é o comportamento atual do sistema, e vale reportar à equipe de desenvolvimento para avaliar se é assim que deveria funcionar.

## Relatório de Pagamento de Profissionais (sintético)

Rota /relatorio/pagamento/profissional/agrupado. Clique em Filtros, escolha a Agenda (mês/ano) que quer calcular, e clique em Filtrar. O relatório mostra, por Profissional e Especialidade, quantas sessões foram realizadas, quantas entram no cálculo do pagamento, e o Valor Total a repassar.


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Agenda (filtro) | Mês/ano que será calculado — precisa estar vinculado a uma Tabela de Valores. *(obrigatório)* |
| Profissional (filtro) | Restringe o relatório a um profissional específico. |
| Status (filtro) | Quais situações de sessão são pagas (Presente, Ausente, Remarcação etc.). É este filtro que define o quantitativo de sessões a pagar — veja a seção seguinte. Vem com todos os status marcados. *(obrigatório)* |
| Considera Marcação (filtro) | Só tem efeito em especialidades com Tipo de Cobrança "Paciente": "Sim" (padrão) paga o agendamento se ao menos uma sessão estiver num status marcado; "Não" paga todo agendamento do mês, independentemente da marcação. |
| Qtd. Horários | Quantos agendamentos (paciente + horário) entraram no cálculo — só entram os que têm ao menos uma sessão num status marcado. |
| Sessões / Sessões Pagamento | Sessões: total de sessões previstas nesses agendamentos. Sessões Pagamento: quantas delas estão num dos Status marcados no filtro (e já com a data registrada). |
| Valor Total | Sessões Pagamento × Valor da sessão (da aba Profissionais ou Especialidades da Tabela de Valores). Só fica com checkbox pra selecionar se for maior que zero. |

## Quais sessões entram no pagamento: o filtro de Status

O quantitativo de Sessões Pagamento não é fixo: ele depende dos Status marcados no filtro do relatório. Cada agendamento do mês tem até 5 sessões, e cada sessão recebe na Agenda uma situação (Presente, Ausente, Ausente - Justificativa, Remarcação, Pac. Desmarcou, Pro. Desmarcou). Ao calcular, o sistema olha sessão por sessão e só conta as que estão num dos status marcados. Por isso, o mesmo mês pode dar valores diferentes dependendo do que foi marcado no filtro.


| Status da sessão | Se estiver marcado no filtro, a sessão é paga? |
|---|---|
| PRESENTE | Sim. |
| AUSENTE | Sim — a falta do paciente é paga ao profissional como se fosse uma sessão. Desmarque se a clínica não paga faltas. |
| AUSENTE - JUSTIFICATIVA | Sim — mesma regra do Ausente. |
| REMARCAÇÃO | Sim. |
| PAC. DESMARCOU / PRO. DESMARCOU | Normalmente não. Ao marcar uma sessão como desmarcada, o sistema não registra a data dela, e o cálculo só conta sessões com data registrada. A exceção é a sessão que já tinha sido marcada antes com outro status (ex.: Presente) e depois foi trocada para desmarcação: ela mantém a data anterior e passa a contar. |
| Sessão ainda sem marcação | Nunca — nem com todos os status marcados. Sessões com data futura também só contam depois que a data chegar. |

Exemplo real (Setembro/2026, ambiente de testes). Na linha do profissional "PSICANALISTA", especialidade Terapeuta Ocupacional, com valor de R$ 3,88 por sessão, há no mês 2 sessões marcadas como Presente e 3 marcadas como Ausente (as demais sessões previstas ainda não foram marcadas). Rodando o mesmo relatório com três combinações de Status:

| Status marcados no filtro | Qtd. Horários | Sessões | Sessões Pagamento | Valor Total (PSICANALISTA / T.O.) | Total do relatório |
|---|---|---|---|---|---|
| Todos (padrão da tela) | 4 | 17 | 5 | R$ 19,40 (5 × 3,88) | R$ 93,93 |
| Somente PRESENTE | 2 | 8 | 2 | R$ 7,76 (2 × 3,88) | R$ 82,29 |
| Somente AUSENTE + AUSENTE - JUSTIFICATIVA | 2 | 9 | 3 | R$ 11,64 (3 × 3,88) | R$ 11,64 |

Repare que as 5 sessões pagas com "Todos" são exatamente as 2 presenças + as 3 faltas. As colunas "Qtd. Horários" e "Sessões" também mudam, porque um agendamento só aparece se tiver ao menos uma sessão num status marcado.






> ⚠️ O botão Gerar Contas a Pagar usa os Status que estão marcados no filtro naquele momento: o valor gravado na conta é exatamente o que aparece na tela. Por isso, confira o filtro de Status antes de gerar, de acordo com a regra da clínica (ex.: pagar faltas ou não). Depois de gerada, a conta não muda se o filtro for alterado, e a linha continua marcada como "Conta a pagar gerada" com qualquer combinação de status.

Tipo de Cobrança "Paciente". Nessas especialidades o profissional recebe no máximo 1 vez por agendamento. Com "Considera Marcação = Sim" (padrão), o agendamento só é pago se ao menos uma sessão estiver num status marcado — ex.: com somente PRESENTE marcado, um paciente que faltou a todas as sessões do mês não gera pagamento. Com "Considera Marcação = Não", todo agendamento do mês é pago 1 vez, independentemente dos status. Para especialidades "Por Sessão", o campo Considera Marcação não muda nada.

## Relatório de Pagamento de Profissionais (analítico)

Rota /relatorio/pagamento/profissional (sem "/agrupado"). É a versão detalhada do mesmo cálculo do relatório sintético: em vez de uma linha por Profissional + Especialidade, mostra uma linha por Paciente + Profissional + Especialidade, com os mesmos totais de sessões e valor. Os filtros são os mesmos (Agenda, Profissional, Status, Sessões Cobrar, Valor de Pagamento, Considera Marcação), mas essa tela não tem botão para gerar Conta a Pagar — só "Filtros" e "Exportar".



Serve como tela de conferência/auditoria antes de gerar o pagamento em lote pelo relatório sintético: permite ver, paciente por paciente, exatamente quais sessões estão entrando no valor total de cada profissional — útil para investigar uma diferença inesperada (por exemplo, uma sessão que não deveria contar, ou um paciente que faltou e foi contabilizado por engano) antes de confirmar a geração da conta, ou para exportar e conferir com uma agenda física.

## Gerando a Conta a Pagar

Marque o checkbox das linhas desejadas (ou use o botão no canto superior direito da tabela pra marcar todas) e clique em Gerar Contas a Pagar. Preencha Plano de Contas, Centro de Custo e Data de Vencimento (os três são obrigatórios), e confirme em Sim / Gerar.



## Onde a conta gerada aparece — e por que ela nasce "Em Aberto"

A conta criada aparece normalmente na tela de Contas a Pagar, com o Favorecido (o profissional), o Plano de Contas (ex.: "Honorário Médico"), o Centro de Custo e o valor calculado. Ela nasce com Situação "1 - Aberto" e Valor Pago R$ 0,00 — ou seja, o Pagamento de Profissionais só calcula e registra a dívida com o profissional; ele não marca como pago sozinho. O pagamento em si só é registrado depois, manualmente, quando a clínica realmente faz o repasse: usando o botão de Pagamento/Acerto dessa conta (o mesmo botão "$" já visto na rotina de Contas a Pagar) para dar baixa quando o dinheiro sair de fato.


## Quando o mês não está vinculado a nenhuma tabela de valores

Se a Agenda (mês/ano) escolhida no filtro ainda não foi vinculada a nenhuma Tabela de Valores (aba Agenda, tela de configuração), o sistema recusa com o aviso "Agenda não vinculada a uma conf. Pagamento" — é preciso voltar em Tabelas Aux. → Tab. Pagamento e vincular aquele mês antes de tentar gerar o pagamento dele.


> ⚠️ Esta é uma das rotinas que geram Conta a Pagar automaticamente: em vez de lançar manualmente uma conta para cada profissional todo mês, o sistema calcula e gera tudo de uma vez a partir dos atendimentos realizados e da Tabela de Valores configurada — o Plano de Contas usado costuma ser algo como "Honorário Médico" e o Tipo de Documento fica marcado como "Pag. Profissional" na Conta a Pagar gerada. Diferente do Checkin (que já gera a conta paga), aqui a conta nasce em aberto: a baixa/pagamento em si é um passo manual separado, feito quando a clínica realmente repassa o valor ao profissional.
