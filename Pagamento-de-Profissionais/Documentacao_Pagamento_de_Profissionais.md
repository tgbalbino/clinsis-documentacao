# Pagamento de Profissionais

_Calcular e gerar, de uma vez, o repasse de todos os profissionais do mês_

Versão 1.0 — 17/09/2026

Pagamento de Profissionais calcula, a partir dos atendimentos realizados no mês, quanto a clínica deve repassar para cada profissional — e gera a Conta a Pagar correspondente com um clique, em vez de lançar uma conta manual pra cada profissional. Para isso funcionar, é preciso configurar ANTES uma Tabela de Valores para Pagamento (Tabelas Aux. → Tab. Pagamento), com o valor pago por sessão/atendimento e vinculando o mês (Agenda) que vai usar essa tabela.

Assista ao vídeo narrado desta rotina: [https://youtu.be/0dVv7ctVDPE](https://youtu.be/0dVv7ctVDPE)

---

## Configuração prévia: Tabela de Valores para Pagamento

Em Tabelas Aux. → Tab. Pagamento fica a lista de "tabelas de valores" — cada uma agrupa um conjunto de valores usados para calcular o repasse dos profissionais. Ao abrir uma tabela (botão da engrenagem), três abas organizam a configuração:

![Lista de tabelas de valores para pagamento. No exemplo, a "Tabela 2026" já está ativa.](00-vigencia-lista.png)

_Lista de tabelas de valores para pagamento. No exemplo, a "Tabela 2026" já está ativa._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Aba Agenda | Quais competências (mês/ano) usam esta tabela de valores. Sem vincular o mês aqui, o sistema recusa gerar o pagamento daquele mês. | ConfigAgendaProfEspecPagtoController.cs |
| Aba Especialidades | Valor padrão por Especialidade (ex.: Fisioterapeuta, Psicólogo), aplicado a todos os profissionais daquela especialidade que não tiverem um valor específico. | ConfigProfissionalEspecialidadePagtoController.cs |
| Aba Profissionais | Valor específico por Profissional + Especialidade, que sobrepõe o valor padrão da aba Especialidades quando presente. | ConfigProfissionalEspecialidadePagtoController.cs |

![Aba Agenda: lista de competências (2026/Setembro, 2026/Agosto, etc.) já vinculadas a esta tabela de valores.](01-vigencia-gerenciar-agenda.png)

_Aba Agenda: lista de competências (2026/Setembro, 2026/Agosto, etc.) já vinculadas a esta tabela de valores._

![Aba Profissionais: lista de profissionais; o botão "$" abre o cadastro dos valores daquele profissional por especialidade.](02-vigencia-gerenciar-profissionais.png)

_Aba Profissionais: lista de profissionais; o botão "$" abre o cadastro dos valores daquele profissional por especialidade._

## "Valor" e "Valor Convênio": qual dos dois é usado no cálculo

Tanto na aba Especialidades quanto na aba Profissionais, cada linha tem dois campos de valor: Valor e Valor Convênio. Pela lógica do nome, seria esperado que o sistema usasse automaticamente o Valor Convênio quando o atendimento foi feito por um paciente de convênio, e o Valor normal quando foi particular.

![Aba Especialidades: cada linha tem as colunas Tipo de Marcação, Valor e Valor Convênio — no exemplo, "Terapeuta Ocupacional / Todos os tipos" vale R$ 2,00 e "Fisioterapeuta" tem Valor R$ 3,00 e Valor Convênio R$ 2,00 preenchido.](13-vigencia-aba-especialidades.png)

_Aba Especialidades: cada linha tem as colunas Tipo de Marcação, Valor e Valor Convênio — no exemplo, "Terapeuta Ocupacional / Todos os tipos" vale R$ 2,00 e "Fisioterapeuta" tem Valor R$ 3,00 e Valor Convênio R$ 2,00 preenchido._

> ⚠️ Isso não acontece hoje. Conferindo o cálculo do relatório, o sistema sempre usa o campo Valor para calcular o repasse, independentemente do atendimento ser particular ou de convênio — o campo Valor Convênio fica salvo no cadastro, mas não entra em nenhuma conta. Na prática, preencher o Valor Convênio hoje não muda o valor pago ao profissional. Recomendamos não contar com uma diferenciação automática por convênio nesta tela e alinhar com a equipe de desenvolvimento se essa distinção deveria estar ativa.

## "Tipo de Marcação": valores diferentes por tipo de atendimento

O campo Tipo de Marcação (ex.: "Todos os tipos", "Avaliação", "Consulta/Sessão") permite cadastrar um valor de pagamento diferente conforme o tipo de marcação escolhido no agendamento do paciente. Por padrão existe uma linha "Todos os tipos", que serve de valor genérico; é possível clicar no botão "+" e adicionar uma linha específica para "Avaliação" ou "Consulta/Sessão" com um valor próprio.

Exemplo real do ambiente de testes: na aba Especialidades, "Terapeuta Ocupacional" tem duas linhas: "Todos os tipos" = R$ 2,00 e "Avaliação" = R$ 3,00 (ver print acima) — um agendamento de Avaliação paga R$ 3,00, e qualquer outro tipo (Consulta/Sessão) paga R$ 2,00 pela linha genérica.

![O mesmo vale na aba Profissionais: o "Profissional 01" tem valor específico para Psicólogo — "Todos os tipo" = R$ 10,00 e "Consulta/Ses[são]" = R$ 2,00 — sobrepondo, só para ele, o valor padrão de Psicólogo da aba Especialidades (R$ 80,00).](14-vigencia-modal-valores-profissional.png)

_O mesmo vale na aba Profissionais: o "Profissional 01" tem valor específico para Psicólogo — "Todos os tipo" = R$ 10,00 e "Consulta/Ses[são]" = R$ 2,00 — sobrepondo, só para ele, o valor padrão de Psicólogo da aba Especialidades (R$ 80,00)._

## "Tipo de Cobrança" da Especialidade: por sessão ou por paciente

Esse campo não fica na Tabela de Valores — ele é configurado no cadastro da própria Especialidade (Cadastros → Especialidades), no campo Tipo de Cobrança, com duas opções: Por Sessão ou Paciente. Mesmo estando em outra tela, ele afeta diretamente como o Pagamento de Profissionais conta as sessões:

![Cadastros → Especialidades: a lista já mostra a coluna Tipo de Cobrança de cada especialidade — no ambiente de testes, todas estão configuradas como "Por Sessão".](15-especialidade-lista-tipocobranca.png)

_Cadastros → Especialidades: a lista já mostra a coluna Tipo de Cobrança de cada especialidade — no ambiente de testes, todas estão configuradas como "Por Sessão"._

![Abrindo "Editar" numa especialidade (ex.: Fisioterapeuta), o campo Tipo de Cobrança aparece no cadastro, com as opções Por Sessão / Paciente.](16-especialidade-cadastro-tipocobranca.png)

_Abrindo "Editar" numa especialidade (ex.: Fisioterapeuta), o campo Tipo de Cobrança aparece no cadastro, com as opções Por Sessão / Paciente._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Por Sessão | O profissional é pago por cada sessão confirmada individualmente. Se o agendamento tem 5 sessões previstas e 3 foram confirmadas, contam 3 sessões pagáveis. | Especialidade.TipoCobranca = 1 |
| Paciente | O profissional é pago no máximo 1 vez por agendamento/paciente naquele período, não importa quantas sessões (1 a 5) ele teve — é um valor "por pacote", não por sessão avulsa. | Especialidade.TipoCobranca = 2 |

Exemplo numérico: Especialidade "Fisioterapia" com Valor = R$ 50,00 e um agendamento com 5 sessões previstas no mês, das quais 3 foram confirmadas como realizadas. Se o Tipo de Cobrança da especialidade for Por Sessão, o valor total é 3 × R$ 50 = R$ 150,00. Se for Paciente, o valor total é 1 × R$ 50 = R$ 50,00 — paga uma única vez pelo pacote do mês, mesmo que várias sessões tenham ocorrido.

## Quando criar uma nova Tabela de Valores

Seria natural imaginar que, ao reajustar valores, bastaria criar uma nova Tabela de Valores e vincular só os meses futuros a ela, preservando os valores antigos dos meses já vinculados à tabela anterior. É importante entender como o sistema realmente se comporta hoje antes de fazer isso:

> ⚠️ O cálculo do relatório usa sempre a Tabela de Valores mais recentemente cadastrada que estiver marcada como "Ativo = Sim" para toda a clínica — e não, especificamente, a tabela vinculada àquele mês na aba Agenda. A aba Agenda só controla se aquele mês pode ou não entrar no cálculo (precisa estar vinculado a alguma tabela), mas os valores aplicados vêm sempre da tabela ativa mais nova. Ou seja: editar um Valor numa tabela existente, ou ativar uma tabela nova, pode alterar o cálculo de meses antigos que ainda não tiveram o pagamento gerado — a única coisa que realmente fica "congelada" é a Conta a Pagar já gerada; uma vez gerada, ela não é recalculada.

Na prática, para reajustar valores com segurança: gere e confira a Conta a Pagar dos meses fechados antes de alterar valores ou ativar uma tabela nova, já que o sistema recalcula pelo valor mais recente ativo no momento em que o relatório é rodado — não pelo valor vigente na época do atendimento. Se notar valores de meses antigos mudando ao reajustar uma tabela nova, isso é o comportamento atual do sistema, e vale reportar à equipe de desenvolvimento para avaliar se é assim que deveria funcionar.

## Relatório de Pagamento de Profissionais (sintético)

Rota /relatorio/pagamento/profissional/agrupado. Clique em Filtros, escolha a Agenda (mês/ano) que quer calcular, e clique em Filtrar. O relatório mostra, por Profissional e Especialidade, quantas sessões foram realizadas, quantas entram no cálculo do pagamento, e o Valor Total a repassar.

![Resultado para Setembro/2026 (mês já vinculado à Tabela 2026): 4 linhas com Valor Total calculado, somando R$ 67,00.](05-resultado-agenda-vinculada.png)

_Resultado para Setembro/2026 (mês já vinculado à Tabela 2026): 4 linhas com Valor Total calculado, somando R$ 67,00._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Agenda (filtro) | Mês/ano que será calculado — precisa estar vinculado a uma Tabela de Valores. | Obrigatório |
| Profissional (filtro) | Restringe o relatório a um profissional específico. | Opcional |
| Status (filtro) | Quais status de agendamento entram no cálculo (Presente, Ausente, etc.). | Obrigatório ter ao menos 1 marcado |
| Sessões / Sessões Pagamento | Total de sessões no mês e quantas delas contam para pagamento (conforme os Status marcados). | RelatorioRepository.cs |
| Valor Total | Sessões Pagamento × Valor da sessão (da aba Profissionais ou Especialidades da Tabela de Valores). Só fica com checkbox pra selecionar se for maior que zero. | RelatorioRepository.cs |

## Relatório de Pagamento de Profissionais (analítico)

Rota /relatorio/pagamento/profissional (sem "/agrupado"). É a versão detalhada do mesmo cálculo do relatório sintético: em vez de uma linha por Profissional + Especialidade, mostra uma linha por Paciente + Profissional + Especialidade, com os mesmos totais de sessões e valor. Os filtros são os mesmos (Agenda, Profissional, Status, Sessões Cobrar, Valor de Pagamento, Considera Marcação), mas essa tela não tem botão para gerar Conta a Pagar — só "Filtros" e "Exportar".

![Tela inicial do relatório analítico, antes de aplicar o filtro de Agenda.](11-analitico-inicial.png)

_Tela inicial do relatório analítico, antes de aplicar o filtro de Agenda._

![Mesma Agenda (Setembro/2026) do exemplo do relatório sintético, agora aberta paciente a paciente: o total geral (R$ 67,00) bate exatamente com o valor do sintético, só que dividido em várias linhas.](12-analitico-resultado.png)

_Mesma Agenda (Setembro/2026) do exemplo do relatório sintético, agora aberta paciente a paciente: o total geral (R$ 67,00) bate exatamente com o valor do sintético, só que dividido em várias linhas._

Serve como tela de conferência/auditoria antes de gerar o pagamento em lote pelo relatório sintético: permite ver, paciente por paciente, exatamente quais sessões estão entrando no valor total de cada profissional — útil para investigar uma diferença inesperada (por exemplo, uma sessão que não deveria contar, ou um paciente que faltou e foi contabilizado por engano) antes de confirmar a geração da conta, ou para exportar e conferir com uma agenda física.

## Gerando a Conta a Pagar

Marque o checkbox das linhas desejadas (ou use o botão no canto superior direito da tabela pra marcar todas) e clique em Gerar Contas a Pagar. Preencha Plano de Contas, Centro de Custo e Data de Vencimento (os três são obrigatórios), e confirme em Sim / Gerar.

![Modal "Gerar contas a pagar" preenchido: Plano de Contas "Honorário Médico", Centro de Custo "Administrativo / Financeiro" e Data de Vencimento de hoje, para a linha do Profissional 01 selecionada.](07-modal-gerar-preenchido.png)

_Modal "Gerar contas a pagar" preenchido: Plano de Contas "Honorário Médico", Centro de Custo "Administrativo / Financeiro" e Data de Vencimento de hoje, para a linha do Profissional 01 selecionada._

![Depois de gerar: aviso "1 conta(s) a pagar gerada(s) com sucesso" e a linha marca "Conta a pagar gerada" (não pode mais ser selecionada de novo).](08-apos-gerar.png)

_Depois de gerar: aviso "1 conta(s) a pagar gerada(s) com sucesso" e a linha marca "Conta a pagar gerada" (não pode mais ser selecionada de novo)._

## Onde a conta gerada aparece — e por que ela nasce "Em Aberto"

A conta criada aparece normalmente na tela de Contas a Pagar, com o Favorecido (o profissional), o Plano de Contas (ex.: "Honorário Médico"), o Centro de Custo e o valor calculado. Ela nasce com Situação "1 - Aberto" e Valor Pago R$ 0,00 — ou seja, o Pagamento de Profissionais só calcula e registra a dívida com o profissional; ele não marca como pago sozinho. O pagamento em si só é registrado depois, manualmente, quando a clínica realmente faz o repasse: usando o botão de Pagamento/Acerto dessa conta (o mesmo botão "$" já visto na rotina de Contas a Pagar) para dar baixa quando o dinheiro sair de fato.

![Conferindo em Contas a Pagar: a conta do "Profissional 01" (Plano de Contas "Honorário Médico", R$ 40,00) aparece com Situação "1 - Aberto" e Valor Pago R$ 0,00 — pendente só da baixa quando o pagamento for efetivamente feito.](10-conta-a-pagar-gerada-pelo-pagamento-profissional.png)

_Conferindo em Contas a Pagar: a conta do "Profissional 01" (Plano de Contas "Honorário Médico", R$ 40,00) aparece com Situação "1 - Aberto" e Valor Pago R$ 0,00 — pendente só da baixa quando o pagamento for efetivamente feito._

## Quando o mês não está vinculado a nenhuma tabela de valores

Se a Agenda (mês/ano) escolhida no filtro ainda não foi vinculada a nenhuma Tabela de Valores (aba Agenda, tela de configuração), o sistema recusa com o aviso "Agenda não vinculada a uma conf. Pagamento" — é preciso voltar em Tabelas Aux. → Tab. Pagamento e vincular aquele mês antes de tentar gerar o pagamento dele.

![Exemplo real: ao filtrar por um mês (Abril/2026) que não está vinculado a nenhuma tabela, o relatório vem vazio e aparece o aviso de erro.](09-agenda-nao-vinculada-sem-linhas.png)

_Exemplo real: ao filtrar por um mês (Abril/2026) que não está vinculado a nenhuma tabela, o relatório vem vazio e aparece o aviso de erro._

> ⚠️ Esta é uma das rotinas que geram Conta a Pagar automaticamente: em vez de lançar manualmente uma conta para cada profissional todo mês, o sistema calcula e gera tudo de uma vez a partir dos atendimentos realizados e da Tabela de Valores configurada — o Plano de Contas usado costuma ser algo como "Honorário Médico" e o Tipo de Documento fica marcado como "Pag. Profissional" na Conta a Pagar gerada. Diferente do Checkin (que já gera a conta paga), aqui a conta nasce em aberto: a baixa/pagamento em si é um passo manual separado, feito quando a clínica realmente repassa o valor ao profissional.
