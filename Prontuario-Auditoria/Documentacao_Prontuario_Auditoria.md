# Prontuário — Auditoria e Relatórios

_Como conferir se cada atendimento gerou prontuário: Auditoria, Produção e Atendimentos Sequenciais_

Versão 1.0 — 23/09/2026

Este manual é para o administrador. Ele explica como conferir, mês a mês, se os atendimentos realizados (presenças) geraram prontuários finalizados, quais ficaram em digitação e quais estão sem tag. São três relatórios em Relatórios: Auditoria de Prontuários, Produção de Prontuários e Atendimentos Sequenciais, além das configurações da clínica que mudam a contagem.

Vídeo narrado desta rotina: `video-prontuario-auditoria-com-legenda.mp4 (ou -sem-legenda.mp4)`

---

## Para que serve cada relatório

| Relatório | Pergunta que responde | Onde |
|---|---|---|
| Auditoria de Prontuários | Cada profissional fez prontuário dos atendimentos que realizou no mês? | Relatórios (painel) → Auditoria |
| Produção de Prontuários | Quantos prontuários foram finalizados, estão em digitação ou foram excluídos por profissional e tipo, em um período? | Relatórios (painel) → Produção de Prontuários |
| Atendimentos Sequenciais | Quais atendimentos em horários seguidos o sistema junta como um só na auditoria? | Relatórios (painel) → Atendimentos Sequenciais |

## 1. Auditoria de Prontuários

![Filtros da auditoria: Agenda e Tipo são obrigatórios; Profissional, Método e Tag são opcionais.](01-auditoria.png)

_Filtros da auditoria: Agenda e Tipo são obrigatórios; Profissional, Método e Tag são opcionais._

| Filtro | Para que serve |
|---|---|
| Agenda * | O mês da agenda a auditar (ex.: 2026 - SETEMBRO). É obrigatório. |
| Tipo de Prontuário * | Qual tipo conferir (Anamnese, Evolução diária...). Obrigatório: cada consulta olha um tipo por vez. |
| Profissional | Restringe a um profissional. |
| Método | Restringe aos atendimentos desse método de atendimento (e, se a clínica usa tags, aos prontuários com essa tag). |
| Tag | Só prontuários que tenham essa tag. |
| Tipo de Relatório | Sintético (uma linha por profissional) ou Analítico (uma linha por profissional e paciente). |

![Auditoria sintética de Setembro/2026, tipo Anamnese.](04-sintetico.png)

_Auditoria sintética de Setembro/2026, tipo Anamnese._

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Presenças | Quantidade de sessões marcadas como Presente na agenda do mês (data da sessão registrada). É o número de atendimentos realizados. | AgendaProfissionalDiaPac (status 3) |
| Finalizado | Prontuários do tipo escolhido com situação Finalizada e data de emissão dentro do mês. Prontuários excluídos não contam. | Prontuario.Situacao = F |
| Não Finalizado | Prontuários em Digitação (rascunho). Rascunhos sem data de emissão entram pelo mês da criação. | Prontuario.Situacao = D |
| Sem Tag | Prontuários sem nenhuma tag (relevante nas clínicas que usam tags). | ProntuarioTag |

A linha do profissional fica em vermelho quando o número de Finalizado é diferente de Presenças. Em regra, cada presença deveria ter um prontuário finalizado. No exemplo, o PSICANALISTA tem 5 presenças, mas só 2 prontuários finalizados, então merece conferência.

![Analítico: mostra por paciente onde falta prontuário (por exemplo, paciente com presença e nenhum prontuário finalizado).](05-analitico.png)

_Analítico: mostra por paciente onde falta prontuário (por exemplo, paciente com presença e nenhum prontuário finalizado)._

Use Exportar (depois de pesquisar) para baixar o resultado em CSV (arquivo "AuditoriaProntuario.csv", com o tipo e a agenda no topo).

![Tipo Evolução diária em Setembro/2026: 4 prontuários em digitação e 14 finalizados para o PSICANALISTA.](10-sintetico-evolucao.png)

_Tipo Evolução diária em Setembro/2026: 4 prontuários em digitação e 14 finalizados para o PSICANALISTA._

> ⚠️ Correções feitas nesta documentação: (1) rascunhos sem data de emissão não entravam no mês e por isso "Não Finalizado" ficava menor do que o real (em Setembro havia 4 rascunhos de Evolução diária e o relatório mostrava só 1); agora usam a data de criação. (2) O relatório de Produção contava prontuários excluídos também como Finalizado/Digitação; agora conta só os ativos e mostra os excluídos à parte.

> ⚠️ Limites a saber: o relatório conta prontuários pela data de emissão; e existe uma coluna "Fora da Agenda" (prontuário de paciente sem marcação no mês) que está oculta temporariamente na tela, em revisão.

## 2. Produção de Prontuários

![Produção de Anamnese entre 01/09 e 30/09/2026: por profissional e tipo.](07-producao-resultado.png)

_Produção de Anamnese entre 01/09 e 30/09/2026: por profissional e tipo._

Escolha o Tipo de Relatório (Total do Período ou Diário), o tipo de prontuário, o período de emissão, e opcionalmente profissional e tag. As colunas são Finalizado, Digitação e Excluído. O modo Diário abre uma linha por dia de emissão. Ao contrário da auditoria, este relatório não olha as presenças da agenda: mede apenas a produção de prontuários.

## 3. Configurações da clínica que mudam a auditoria

Três opções da Configuração Auxiliar (ativadas por clínica pelos scripts 137 e 138) alteram a contagem e o comportamento do prontuário:

| Opção | O que muda |
|---|---|
| PRONTUARIO_TAGS | Liga as tags no prontuário e o filtro de Método/Tag na auditoria. O profissional precisa ter ao menos 1 tag para finalizar. |
| PRONT_TAG_AUTO | Ao criar o prontuário, aplica a tag do método da agenda quando o paciente tem um único método no mês com o profissional. |
| AUD_PRONT_DUPLO_1 | Atendimento duplo conta como 1 nas Presenças da auditoria: dois horários consecutivos (mesma agenda, profissional, paciente, método e dia da semana) contam uma presença só, pois gera-se um único prontuário. |

As três estão ligadas na Clínica 1 (Homologação). Os scripts 137 (clínica 6, com métodos e preenchimento de tags) e 138 (clínicas 1 e 6) só cadastram e habilitam essas opções, e podem ser executados mais de uma vez.

## 4. Atendimentos Sequenciais

Este relatório mostra os pares (ou cadeias) de horários que o sistema trata como um atendimento único quando AUD_PRONT_DUPLO_1 está ligada. Escolha a Agenda (obrigatória), e opcionalmente Profissional e Método.

![Atendimentos sequenciais de Setembro/2026: paciente, método, dia, horários e as presenças de cada horário.](06-sequenciais-resultado.png)

_Atendimentos sequenciais de Setembro/2026: paciente, método, dia, horários e as presenças de cada horário._

| Coluna | Significado |
|---|---|
| Dia / Horários | Dia da semana e os dois horários seguidos (ex.: Segunda, 12:20 - 12:30). |
| Presenças 1º horário / 2º horário | Quantas vezes o paciente esteve presente em cada um dos dois horários no mês. |
| Atendimento Sequencial | Em quantas datas os dois horários tiveram presença ao mesmo tempo. Cada uma dessas datas conta como 1 na auditoria. |

> ⚠️ Como conferir: para cada par listado, a Auditoria conta 1 atendimento por data em que houve presença nos dois horários, e não 2. Assim, um paciente com dois horários seguidos e presença nos dois gera um só prontuário esperado.

## Roteiro de conferência mensal

| Passo | O que fazer |
|---|---|
| 1 | Abra a Auditoria (sintético) do mês e do tipo principal (ex.: Evolução diária). |
| 2 | Procure as linhas em vermelho (Finalizado diferente de Presenças). |
| 3 | Veja o analítico dessas linhas para achar o paciente sem prontuário. |
| 4 | Confira a coluna Não Finalizado e cobre os rascunhos; confira Sem Tag, se a clínica usa tags. |
| 5 | Se a diferença vier de atendimentos em horários seguidos, confira no relatório de Atendimentos Sequenciais. |
| 6 | Use a Produção para acompanhar o total finalizado no período e exporte em CSV quando precisar. |
