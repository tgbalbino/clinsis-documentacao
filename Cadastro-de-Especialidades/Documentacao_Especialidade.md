# Cadastro de Especialidades

_"Tipo de Cobrança" e "Relatório Compartilhado(Prontuários)" explicados com exemplos_

Versão 1.0 — 22/09/2026

O cadastro de Especialidade (Psicologia, Fisioterapia, Fonoaudiologia, etc.) tem duas configurações que mudam o comportamento de outras partes do sistema, mas cujo efeito nem sempre é óbvio pelo nome: Tipo de Cobrança (usada só no Pagamento de Profissionais) e Relatório Compartilhado(Prontuários) (usada só no Prontuário). Este manual explica as duas em detalhe, com exemplos.

Assista ao vídeo narrado desta rotina: [https://youtu.be/9pTvpUSwb_g](https://youtu.be/9pTvpUSwb_g)
---

## Onde fica o cadastro

Acesso em Tabelas Aux. → Especialidade (rota aux/especialidade). Além de Descrição, Abreviação e Ativo, cada especialidade tem os dois campos explicados abaixo — que não afetam o cadastro em si, e sim como outras telas do sistema se comportam para os atendimentos daquela especialidade.

![Lista de Especialidades já mostra as colunas "Tipo de Cobrança" e "Relatório Compartilhado" — repare como cada uma tem uma combinação diferente.](00-lista-especialidades.png)

_Lista de Especialidades já mostra as colunas "Tipo de Cobrança" e "Relatório Compartilhado" — repare como cada uma tem uma combinação diferente._

![Modal de cadastro: os campos "Tipo de Cobrança" e "Relatório Compartilhado(Prontuários)", com a explicação já disponível na própria tela (texto pequeno abaixo do segundo campo).](01-cadastro-tipo-cobranca-rel-compartilhado.png)

_Modal de cadastro: os campos "Tipo de Cobrança" e "Relatório Compartilhado(Prontuários)", com a explicação já disponível na própria tela (texto pequeno abaixo do segundo campo)._

## Tipo de Cobrança — usado só no Pagamento de Profissionais

Essa opção só é lida em um único lugar do sistema: o cálculo do relatório de Pagamento de Profissionais (analítico e resumido). Ela não afeta a cobrança do paciente/convênio nem a geração de guias — só quanto o profissional recebe pelo atendimento.

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Por Sessão | Paga uma vez para CADA sessão realizada (presença confirmada) no mês, dentro daquele agendamento. | Relatorio_Query.cs |
| Paciente | Paga só 1 vez por paciente/agendamento no mês, não importa quantas sessões ele teve — é um valor "fechado" por paciente, não por sessão. | Relatorio_Query.cs |

> ⚠️ Exemplo: a especialidade "Fonoaudiologia" está configurada como Por Sessão. Se o paciente João teve 4 sessões confirmadas no mês com a profissional Maria, o relatório de Pagamento de Profissionais calcula 4 sessões a pagar (4 × valor da sessão) para Maria. Já a especialidade "Avaliação Neuropsicológica" está configurada como Paciente: mesmo que o paciente tenha tido 3 sessões marcadas naquele mês, o sistema conta apenas 1 unidade a pagar — o "pacote" é pago uma única vez, e não por sessão.

Faz sentido usar Paciente em especialidades que cobram um valor fechado por avaliação ou processo (mesmo que ele tome várias sessões), e Por Sessão nas especialidades onde o profissional é remunerado por atendimento individual.

## Relatório Compartilhado(Prontuários) — usado só no Prontuário

Controla se um profissional consegue ver o prontuário já finalizado de OUTRO profissional, quando os dois atendem o mesmo paciente. Um prontuário em rascunho/digitação nunca é compartilhado, não importa a configuração — só depois de finalizado.

| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |
|---|---|---|
| Não | Prontuários finalizados dessa especialidade nunca ficam visíveis para outro profissional (só quem escreveu, ou um administrador). | ProntuarioRepository.cs |
| Somente mesma especialidade | Outro profissional só vê o prontuário se ele também for da mesma especialidade E também atender aquele paciente. | ProntuarioRepository.cs |
| Qualquer profissional do mesmo paciente | Qualquer profissional que atenda aquele paciente pode ver o prontuário finalizado, mesmo sendo de outra especialidade. | ProntuarioRepository.cs |

> ⚠️ Exemplo: a especialidade "Psicologia" está configurada como Somente mesma especialidade. A psicóloga Ana atende o paciente Pedro e finaliza um prontuário. A psicóloga Beatriz, que também atende Pedro, consegue ver o prontuário finalizado de Ana. Mas o fisioterapeuta Carlos, que também atende Pedro, não consegue, pois não é da mesma especialidade. Se a especialidade fosse Qualquer profissional do mesmo paciente, Carlos também conseguiria ver.

Na tela de Prontuário (acesso do profissional), existe o campo "Emitente", que só aparece para o usuário logado como Profissional: ao escolher uma opção diferente de "Próprio", a lista passa a trazer também prontuários de outros profissionais — e é exatamente essa configuração da Especialidade que decide quais prontuários de terceiros aparecem nessa busca.
