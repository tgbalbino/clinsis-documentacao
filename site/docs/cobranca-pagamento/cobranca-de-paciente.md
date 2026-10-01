# Cobrança de Paciente

Calcula e gera, de uma só vez, a cobrança de todos os pacientes particulares do mês a partir das sessões realizadas, criando as Contas a Receber correspondentes. Possui relatórios sintético e analítico para conferência e proteção contra cobrança em duplicidade. Depende da Tabela de Valores para Cobrança.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Cobranca-de-Paciente/Documentacao_Cobranca_de_Paciente_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/ViW55USFc6I?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/ViW55USFc6I)

## Conteúdo completo do manual

---


_Calcular e gerar, de uma vez, a cobrança de todos os pacientes particulares do mês_

Versão 1.1 — 26/09/2026

Cobrança de Paciente calcula, a partir dos atendimentos particulares realizados no mês, quanto cada paciente deve pagar pelas sessões que teve — e gera a Conta a Receber correspondente com um clique, em vez de lançar uma conta manual pra cada paciente. Para isso funcionar, é preciso configurar ANTES uma Tabela de Valores para Cobrança (Tabelas Aux. → Tab. Cobrança), com o valor cobrado por sessão/atendimento particular.


---

## Configuração prévia: Tabela de Valores para Cobrança

Em Tabelas Aux. → Tab. Cobrança (rota /aux/cobranca/gerenciar) fica a configuração dos valores cobrados de cada paciente particular, organizada em três abas:


| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Aba Especialidade | Valor padrão cobrado por sessão de cada especialidade, aplicado a todos os profissionais que não tiverem um valor específico. |
| Aba Profissional | Valor específico por Profissional + Especialidade, que sobrepõe o valor padrão da aba Especialidade quando presente. |
| Aba Operadora | Valores específicos por Operadora de convênio (colunas Valor e Valor Social), usados quando o relatório de cobrança de convênio for aplicável. |



> ⚠️ Assim como acontece no Pagamento de Profissionais, o campo Valor Social (nas abas Especialidade e Operadora) fica salvo no cadastro, mas não é usado hoje no cálculo da cobrança — o relatório sempre soma pelo campo "Valor" normal. Não conte com uma diferenciação automática de valor social nesta tela.

## Relatório de Cobrança de Paciente (sintético)

Rota /relatorio/valorreceber/agrupado. Clique em Filtros, escolha a Agenda (mês/ano) que quer calcular, marque os Status de sessão que devem entrar na cobrança e clique em Filtrar. O relatório considera apenas agendamentos Particulares (convênio não entra aqui) e soma, por paciente, quanto ele deve pagar.




## Quais sessões entram na cobrança: o filtro de Status

A quantidade de sessões cobradas de cada paciente não é fixa: ela depende dos Status marcados no filtro do relatório — a mesma regra do Pagamento de Profissionais. Cada agendamento do mês tem até 5 sessões, e cada sessão recebe na Agenda uma situação (Presente, Ausente, Ausente - Justificativa, Remarcação, Pac. Desmarcou, Pro. Desmarcou). O sistema olha sessão por sessão e só cobra as que estão num dos status marcados. Por isso, o mesmo mês pode dar valores diferentes conforme o filtro.


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






> ⚠️ O botão Gerar Conta a Receber gera a conta com o Valor a Receber que está na tela, ou seja, calculado com os Status marcados naquele momento. Por isso, confira o filtro de Status antes de gerar, de acordo com a regra da clínica (ex.: cobrar faltas ou não). Depois de gerada, a conta não muda se o filtro for alterado.

Diferente do Pagamento de Profissionais, a cobrança de paciente é sempre por sessão: o campo "Tipo de Cobrança" da Especialidade não é usado aqui, e esta tela não tem o filtro "Considera Marcação".

## Gerando a Conta a Receber

Marque o checkbox dos pacientes desejados (só aparece para quem tem Valor a Receber maior que zero) e clique em Gerar Conta a Receber. Preencha Data de Vencimento (mínimo hoje + 5 dias), Plano de Contas e Centro de Custo, todos obrigatórios, e confirme em Sim / Gerar.




## Onde a conta gerada aparece — e por que ela nasce "Em Aberto"

A conta criada aparece na tela de Contas a Receber, com o nome do paciente, o Plano de Contas, o Centro de Custo e o valor calculado. Assim como no Pagamento de Profissionais, ela nasce com Situação "Aberto" e Saldo Restante igual ao valor total — o relatório só calcula e registra a cobrança; o recebimento em si (o paciente efetivamente pagando) é lançado depois, manualmente, dando baixa nessa conta quando o dinheiro entrar de fato.


## Relatório de Cobrança de Paciente (analítico)

Rota /relatorio/valorreceber (sem "/agrupado"). É a versão detalhada do mesmo cálculo do relatório sintético: em vez de uma linha por paciente, mostra uma linha por Paciente + Profissional + Especialidade, com Sessões, Sessões a Receber, Valor da Sessão e Valor a Receber. Os filtros são os mesmos (Agenda, Especialidade, Paciente, Status), mas esta tela não tem botão para gerar Conta a Receber — só "Filtros" e "Exportar".



Serve como tela de conferência/auditoria antes de gerar a cobrança em lote pelo relatório sintético: permite ver exatamente quais sessões, de qual profissional, estão compondo o valor total de cada paciente antes de confirmar a geração.

## Proteção contra cobrança em duplicidade

Rodar o relatório sintético mais de uma vez para o mesmo mês não gera cobrança duplicada: assim que uma Conta a Receber é gerada para um paciente naquela Agenda, o relatório passa a marcar esse paciente como "Conta a receber gerada" e esconde o checkbox de seleção dele — só volta a aparecer selecionável se essa conta for cancelada. Isso evita cobrar o mesmo paciente duas vezes pelas mesmas sessões.


> ⚠️ Esta é uma das rotinas que geram Conta a Receber automaticamente: em vez de lançar manualmente uma conta para cada paciente todo mês, o sistema calcula e gera tudo de uma vez a partir dos atendimentos particulares realizados e da Tabela de Valores configurada — o Plano de Contas usado costuma ser algo como "Consulta Particular". Assim como no Pagamento de Profissionais, a conta nasce em aberto: a baixa/recebimento em si é um passo manual separado, feito quando o paciente realmente paga.
