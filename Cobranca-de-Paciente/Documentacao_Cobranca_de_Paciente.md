# Cobrança de Paciente

_Calcular e gerar, de uma vez, a cobrança de todos os pacientes particulares do mês_

Versão 1.0 — 18/09/2026

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
