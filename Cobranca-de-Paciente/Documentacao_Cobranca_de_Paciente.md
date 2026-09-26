# Cobrança de Paciente

_Calcular e gerar, de uma vez, a cobrança de todos os pacientes particulares do mês_

Versão 1.1 — 26/09/2026

Cobrança de Paciente calcula, a partir dos atendimentos particulares realizados no mês, quanto cada paciente deve pagar pelas sessões que teve — e gera a Conta a Receber correspondente com um clique, em vez de lançar uma conta manual pra cada paciente. Para isso funcionar, é preciso configurar ANTES uma Tabela de Valores para Cobrança (Tabelas Aux. → Tab. Cobrança), com o valor cobrado por sessão/atendimento particular.

Assista ao vídeo narrado desta rotina: [https://youtu.be/AdzPSoJ7_4I](https://youtu.be/AdzPSoJ7_4I)

---

## Configuração prévia: Tabela de Valores para Cobrança

Em Tabelas Aux. → Tab. Cobrança (rota /aux/cobranca/gerenciar) fica a configuração dos valores cobrados de cada paciente particular, organizada em três abas:

![Aba Especialidade: valor cobrado por sessão de cada especialidade, aplicado a qualquer profissional que não tenha um valor específico cadastrado (ex.: Fisioterapeuta R$ 2,00, Terapeuta Ocupacional R$ 1,99).](00-cobranca-config-especialidade.png)

_Aba Especialidade: valor cobrado por sessão de cada especialidade, aplicado a qualquer profissional que não tenha um valor específico cadastrado (ex.: Fisioterapeuta R$ 2,00, Terapeuta Ocupacional R$ 1,99)._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Aba Especialidade | Valor padrão cobrado por sessão de cada especialidade, aplicado a todos os profissionais que não tiverem um valor específico. | ConfigCobrancaEspecPagtoController.cs |
| Aba Profissional | Valor específico por Profissional + Especialidade, que sobrepõe o valor padrão da aba Especialidade quando presente. | ConfigCobrancaProfEspecPagtoController.cs |
| Aba Operadora | Valores específicos por Operadora de convênio (colunas Valor e Valor Social), usados quando o relatório de cobrança de convênio for aplicável. | ConfigCobrancaRepository.cs |

![Aba Profissional: lista de profissionais da clínica com os valores específicos por especialidade.](01-cobranca-config-profissional.png)

_Aba Profissional: lista de profissionais da clínica com os valores específicos por especialidade._

![Aba Operadora: valores de cobrança específicos por convênio (colunas Valor e Valor Social).](02-cobranca-config-operadora.png)

_Aba Operadora: valores de cobrança específicos por convênio (colunas Valor e Valor Social)._

> ⚠️ Assim como acontece no Pagamento de Profissionais, o campo Valor Social (nas abas Especialidade e Operadora) fica salvo no cadastro, mas não é usado hoje no cálculo da cobrança — o relatório sempre soma pelo campo "Valor" normal. Não conte com uma diferenciação automática de valor social nesta tela.

## Relatório de Cobrança de Paciente (sintético)

Rota /relatorio/valorreceber/agrupado. Clique em Filtros, escolha a Agenda (mês/ano) que quer calcular, marque os Status de sessão que devem entrar na cobrança e clique em Filtrar. O relatório considera apenas agendamentos Particulares (convênio não entra aqui) e soma, por paciente, quanto ele deve pagar.

![Tela inicial do relatório sintético, antes de aplicar o filtro.](03-sintetico-inicial.png)

_Tela inicial do relatório sintético, antes de aplicar o filtro._

![Filtro preenchido: Agenda de Setembro/2026 e todos os Status de sessão marcados.](04-sintetico-filtro-preenchido.png)

_Filtro preenchido: Agenda de Setembro/2026 e todos os Status de sessão marcados._

![Resultado: uma linha por paciente com o total de sessões e o Valor a Receber calculado — no exemplo, 9 pacientes somando R$ 22,97.](05-sintetico-resultado.png)

_Resultado: uma linha por paciente com o total de sessões e o Valor a Receber calculado — no exemplo, 9 pacientes somando R$ 22,97._

## Quais sessões entram na cobrança: o filtro de Status

A quantidade de sessões cobradas de cada paciente não é fixa: ela depende dos Status marcados no filtro do relatório — a mesma regra do Pagamento de Profissionais. Cada agendamento do mês tem até 5 sessões, e cada sessão recebe na Agenda uma situação (Presente, Ausente, Ausente - Justificativa, Remarcação, Pac. Desmarcou, Pro. Desmarcou). O sistema olha sessão por sessão e só cobra as que estão num dos status marcados. Por isso, o mesmo mês pode dar valores diferentes conforme o filtro.

![Filtros do relatório com a lista de Status aberta. Ao abrir a tela, todos os status já vêm marcados — ou seja, por padrão as faltas (Ausente e Ausente - Justificativa) e as remarcações também são cobradas do paciente.](13-filtro-status-todos.png)

_Filtros do relatório com a lista de Status aberta. Ao abrir a tela, todos os status já vêm marcados — ou seja, por padrão as faltas (Ausente e Ausente - Justificativa) e as remarcações também são cobradas do paciente._

| Status da sessão | Se estiver marcado no filtro, a sessão é cobrada? |
|---|---|
| PRESENTE | Sim. |
| AUSENTE | Sim — a falta é cobrada do paciente como uma sessão. Desmarque se a clínica não cobra faltas. |
| AUSENTE - JUSTIFICATIVA | Sim — mesma regra do Ausente. Desmarque se a falta justificada não deve ser cobrada. |
| REMARCAÇÃO | Sim. |
| PAC. DESMARCOU / PRO. DESMARCOU | Normalmente não. Ao marcar uma sessão como desmarcada, o sistema não registra a data dela, e o cálculo só conta sessões com data registrada. A exceção é a sessão que já tinha sido marcada antes com outro status (ex.: Presente) e depois foi trocada para desmarcação: ela mantém a data anterior e passa a contar. |
| Sessão ainda sem marcação | Nunca — nem com todos os status marcados. Sessões com data futura também só contam depois que a data chegar. |

Exemplo real (Setembro/2026, ambiente de testes). O "Paciente 0005" (Terapeuta Ocupacional, R$ 2,51 por sessão) tem 4 sessões previstas no mês, e a única já marcada foi uma falta (Ausente). Rodando o mesmo relatório com três combinações de Status:

| Status marcados no filtro | Paciente 0005 | Sessões (total) | Valor a Receber (total) |
|---|---|---|---|
| Todos (padrão da tela) | Aparece: 1 sessão, R$ 2,51 (a falta é cobrada) | 11 | R$ 27,39 |
| Somente PRESENTE | Não aparece — nada a cobrar | 10 | R$ 24,87 |
| Somente AUSENTE + AUSENTE - JUSTIFICATIVA | Único paciente da lista: 1 sessão, R$ 2,51 | 1 | R$ 2,51 |

Repare que a diferença entre "Todos" e "Somente PRESENTE" (11 − 10 = 1 sessão; R$ 27,39 − R$ 24,87 = R$ 2,51) é exatamente a falta do Paciente 0005.

![Todos os status marcados: 11 sessões, R$ 27,39. O Paciente 0005 aparece com 1 sessão (a falta) e, neste ambiente de testes, já teve a Conta a Receber gerada — ou seja, a falta foi cobrada.](14-sintetico-todos-status.png)

_Todos os status marcados: 11 sessões, R$ 27,39. O Paciente 0005 aparece com 1 sessão (a falta) e, neste ambiente de testes, já teve a Conta a Receber gerada — ou seja, a falta foi cobrada._

![Para cobrar só atendimentos realizados: clique em "Limpar" e marque apenas PRESENTE.](15-filtro-status-somente-presente.png)

_Para cobrar só atendimentos realizados: clique em "Limpar" e marque apenas PRESENTE._

![Somente PRESENTE: o Paciente 0005 sai da lista e o total cai para 10 sessões e R$ 24,87.](16-sintetico-somente-presente.png)

_Somente PRESENTE: o Paciente 0005 sai da lista e o total cai para 10 sessões e R$ 24,87._

![Somente AUSENTE e AUSENTE - JUSTIFICATIVA: aparece só quem tem falta no mês — útil para conferir quanto das faltas está sendo cobrado.](17-sintetico-somente-ausentes.png)

_Somente AUSENTE e AUSENTE - JUSTIFICATIVA: aparece só quem tem falta no mês — útil para conferir quanto das faltas está sendo cobrado._

![O relatório analítico com o mesmo filtro mostra o detalhe: Paciente 0005, profissional PSICANALISTA, TO, 4 sessões previstas e 1 a receber.](18-analitico-somente-ausentes.png)

_O relatório analítico com o mesmo filtro mostra o detalhe: Paciente 0005, profissional PSICANALISTA, TO, 4 sessões previstas e 1 a receber._

> ⚠️ O botão Gerar Conta a Receber gera a conta com o Valor a Receber que está na tela, ou seja, calculado com os Status marcados naquele momento. Por isso, confira o filtro de Status antes de gerar, de acordo com a regra da clínica (ex.: cobrar faltas ou não). Depois de gerada, a conta não muda se o filtro for alterado.

Diferente do Pagamento de Profissionais, a cobrança de paciente é sempre por sessão: o campo "Tipo de Cobrança" da Especialidade não é usado aqui, e esta tela não tem o filtro "Considera Marcação".

## Gerando a Conta a Receber

Marque o checkbox dos pacientes desejados (só aparece para quem tem Valor a Receber maior que zero) e clique em Gerar Conta a Receber. Preencha Data de Vencimento (mínimo hoje + 5 dias), Plano de Contas e Centro de Custo, todos obrigatórios, e confirme em Sim / Gerar.

![Paciente selecionado (Paciente 000, R$ 2,00) antes de abrir o modal de geração.](06-sintetico-linha-selecionada.png)

_Paciente selecionado (Paciente 000, R$ 2,00) antes de abrir o modal de geração._

![Modal "Gerar conta a receber" preenchido: Data de Vencimento 30/09/2026, Plano de Contas "Consulta Particular" e Centro de Custo "Administrativo / Financeiro".](07-sintetico-modal-gerar-preenchido.png)

_Modal "Gerar conta a receber" preenchido: Data de Vencimento 30/09/2026, Plano de Contas "Consulta Particular" e Centro de Custo "Administrativo / Financeiro"._

![Depois de gerar: aviso "Contas a receber geradas com sucesso" no canto superior direito.](08-sintetico-apos-gerar.png)

_Depois de gerar: aviso "Contas a receber geradas com sucesso" no canto superior direito._

## Onde a conta gerada aparece — e por que ela nasce "Em Aberto"

A conta criada aparece na tela de Contas a Receber, com o nome do paciente, o Plano de Contas, o Centro de Custo e o valor calculado. Assim como no Pagamento de Profissionais, ela nasce com Situação "Aberto" e Saldo Restante igual ao valor total — o relatório só calcula e registra a cobrança; o recebimento em si (o paciente efetivamente pagando) é lançado depois, manualmente, dando baixa nessa conta quando o dinheiro entrar de fato.

![Conferindo em Contas a Receber: a conta do "Paciente 000" (Plano de Contas "Consulta Particular", R$ 2,00) aparece com Situação "Aberto" e Saldo Restante R$ 2,00 — pendente do recebimento.](09-conta-a-receber-gerada-pela-cobranca.png)

_Conferindo em Contas a Receber: a conta do "Paciente 000" (Plano de Contas "Consulta Particular", R$ 2,00) aparece com Situação "Aberto" e Saldo Restante R$ 2,00 — pendente do recebimento._

## Relatório de Cobrança de Paciente (analítico)

Rota /relatorio/valorreceber (sem "/agrupado"). É a versão detalhada do mesmo cálculo do relatório sintético: em vez de uma linha por paciente, mostra uma linha por Paciente + Profissional + Especialidade, com Sessões, Sessões a Receber, Valor da Sessão e Valor a Receber. Os filtros são os mesmos (Agenda, Especialidade, Paciente, Status), mas esta tela não tem botão para gerar Conta a Receber — só "Filtros" e "Exportar".

![Tela inicial do relatório analítico, antes de aplicar o filtro.](10-analitico-inicial.png)

_Tela inicial do relatório analítico, antes de aplicar o filtro._

![Mesma Agenda (Setembro/2026) do exemplo do sintético, agora aberta por Paciente + Profissional + Especialidade: o total geral (R$ 22,97) bate exatamente com o sintético.](11-analitico-resultado.png)

_Mesma Agenda (Setembro/2026) do exemplo do sintético, agora aberta por Paciente + Profissional + Especialidade: o total geral (R$ 22,97) bate exatamente com o sintético._

Serve como tela de conferência/auditoria antes de gerar a cobrança em lote pelo relatório sintético: permite ver exatamente quais sessões, de qual profissional, estão compondo o valor total de cada paciente antes de confirmar a geração.

## Proteção contra cobrança em duplicidade

Rodar o relatório sintético mais de uma vez para o mesmo mês não gera cobrança duplicada: assim que uma Conta a Receber é gerada para um paciente naquela Agenda, o relatório passa a marcar esse paciente como "Conta a receber gerada" e esconde o checkbox de seleção dele — só volta a aparecer selecionável se essa conta for cancelada. Isso evita cobrar o mesmo paciente duas vezes pelas mesmas sessões.

![Depois de gerado, o paciente já cobrado (ex.: "Paciente 0005") aparece com o aviso "Conta a receber gerada" no lugar do checkbox, impedindo nova seleção para aquele mesmo mês.](12-sintetico-com-cobrancas-ja-geradas.png)

_Depois de gerado, o paciente já cobrado (ex.: "Paciente 0005") aparece com o aviso "Conta a receber gerada" no lugar do checkbox, impedindo nova seleção para aquele mesmo mês._

> ⚠️ Esta é uma das rotinas que geram Conta a Receber automaticamente: em vez de lançar manualmente uma conta para cada paciente todo mês, o sistema calcula e gera tudo de uma vez a partir dos atendimentos particulares realizados e da Tabela de Valores configurada — o Plano de Contas usado costuma ser algo como "Consulta Particular". Assim como no Pagamento de Profissionais, a conta nasce em aberto: a baixa/recebimento em si é um passo manual separado, feito quando o paciente realmente paga.
