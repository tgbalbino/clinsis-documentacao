# Progresso da documentação de rotinas do ClinSis

## Objetivo
Para cada rotina do sistema, gerar: PDF completo (com coluna técnica "origem no banco"), PDF simplificado (sem essa coluna), Markdown-base editável, e vídeo narrado em português com marca ClinSis (logo + música), em duas versões — com legenda (amarela, negrito, borda preta) e sem legenda.

Cada entrega fica em `C:\Projetos\W_Clinica\Documentacao-Entrega\<Nome-da-Rotina>\`, incluindo uma subpasta `scripts\` com os scripts-fonte (Playwright de captura, `doc.py`, `narracoes.json`) para permitir alterações futuras sem refazer tudo do zero.

## Ordem acordada com o usuário
1. ✅ Dashboard Financeiro e Fluxo de Caixa
2. ✅ Cadastro de Plano de Contas
3. ✅ Cadastro de Centro de Custo
4. ✅ Contas Recorrentes
5. ✅ Contas a Pagar
6. ✅ Contas a Receber
7. ✅ Checkin de Paciente (fluxo completo de pagamento)
8. ✅ Pagamento de Profissionais (com aprofundamento de Valor/Valor Convênio, Tipo de Marcação, Tipo de Cobrança, quando criar nova Tabela de Valores, e relatório analítico)
9. ✅ Cobrança de Paciente
10. ✅ Contrato (sem assinatura digital)
11. ✅ Contrato (com assinatura digital / D4Sign) — testado ponta a ponta com Sandbox real
12. ✅ Layout de Contrato — documento separado, com referência cruzada nos outros dois de Contrato
13. ✅ Módulo de Caixa
14. ✅ Cadastro de Conta Financeira (com a validação Conta Financeira × Forma de Pagamento)
15. ✅ Dashboard de Agenda (todos os cards, gráficos e tabelas explicados, com as ressalvas de cálculo)
16. ✅ Movimentos Financeiros (o que é, de onde vem, conciliação, exclusão e transferência entre contas)
17. ✅ Cadastro de Especialidades — campos "Tipo de Cobrança" e "Relatório Compartilhado(Prontuários)" explicados em detalhe
18. ✅ Cadastro de Serviços — para que serve e único uso real (aba Serviços do Contrato)
19. ✅ Tabela de Valores (Pagamento) — valores por Especialidade/Profissional, reajuste de preço em massa
20. ✅ Tabela de Valores (Cobrança) — valores por Especialidade/Profissional/Operadora, reajuste de preço em massa

## Bugs reais corrigidos durante a documentação (política: sempre corrigir, nunca só documentar)

Detalhe completo de cada um nas mensagens de commit (`git log` na branch `main` do ApiClinica e FrontClinica — a partir de 22/09/2026 o trabalho passou a ser direto na `main`, a `feat_09_26` não é mais usada; todos os commits já com `git push`) e nas memórias da sessão.

- **Checkin**: parâmetros de Plano de Conta/Centro de Custo/Conta Financeira apontando pra registros excluídos causavam erro genérico; mensagens específicas eram engolidas por um `catch` mal posicionado.
- **Pagamento de Profissionais**: gerar pagamento sem Centro de Custo estourava erro SQL cru.
- **Cobrança de Paciente**: filtro de Status vazio quebrava com erro genérico; relatório sintético permitia gerar Conta a Receber em duplicidade pro mesmo paciente/mês (corrigido com migration `118_Adicionar_IdAgenda_ContaReceber.sql`, já executada).
- **Conta Financeira**: (1) baixa de Conta a Receber sem caixa aberto lançava exceção crua e mostrava só "erro interno" — agora mostra a mensagem específica (o Checkin também passou a abortar/desfazer se a baixa não for gravada); (2) era impossível excluir qualquer Conta Financeira, pois o vínculo automático com Formas de Pagamento barrava por FK — agora exclui conta sem movimentos e explica o bloqueio quando há movimentos ou quando a conta é a do parâmetro do Checkin.
- **Layout de Contrato** (dado corrompido, não bug de código): o layout ativo da clínica de teste tinha acentuação corrompida (mojibake); reativei a versão anterior, que estava correta.
- **Movimentos Financeiros**: o botão "Nova Transferência" sempre falhava com erro interno genérico (INSERT em MovimentoFinanceiro sem IdPlanoConta/IdCentroCusto, colunas NOT NULL). Corrigido exigindo Plano de Contas e Centro de Custo na própria transferência, igual a qualquer outro lançamento financeiro (front + back).

## Notas de configuração do ambiente de teste (não são bugs)

- **Módulo de Caixa**: o usuário admin de teste (IdUsuario 212) estava com "Controla Caixa" desmarcado — habilitei via API pra poder demonstrar o fluxo ao vivo. Continua habilitado; o caixa dele está **fechado** — abra em `/caixa` antes de testar qualquer baixa.
- **Contrato/D4Sign**: testes usam o paciente "Teste Contrato D4SIGN" (IdPessoa 176), que tem o e-mail real do usuário cadastrado — útil pra qualquer teste futuro de assinatura eletrônica.

## Nota de automação (Playwright) — campo de data com máscara

Os campos de data com `mask="00/00/0000"` (ngx-mask) não propagam o valor pro `ngModel` de forma confiável via automação (`fill()`/`pressSequentially()`) — mostra a data certa na tela, mas salva nulo. Não confirmado se afeta usuários reais (não tratado como bug de produto). Contorno usado: gravar o dado direto via API (mesmo endpoint que o botão usaria) e recarregar a tela para os prints.

## Site índice de toda a documentação (MkDocs)

Em `Documentacao-Entrega/site/` existe um site estático (MkDocs + tema Material, grátis) que lista
todas as 20 rotinas documentadas, organizadas por categoria, com link pros PDFs (completo e
simplificado) de cada uma e um espaço reservado para o link do vídeo no YouTube. Ver
`site/README.md` para como regenerar, conferir localmente e publicar (GitHub Pages, IIS ou qualquer
host estático grátis).

**Pendente**: os vídeos ainda não foram subidos ao YouTube (não tenho acesso à conta do usuário
pra fazer isso) — assim que o usuário subir cada vídeo e passar os links, é só editar o dicionário
`YOUTUBE_LINKS` em `site/scripts/gerar_site_docs.py` e regenerar.

## Pipeline técnico (lembrete)

Detalhado nas memórias `documentacao-usuario-padrao-video-com-marca`, `documentacao-usuario-guardar-base-em-md`, `narracao-video-google-cloud-tts`, `documentacao-salvar-scripts-fonte-na-entrega`. Resumo do fluxo por rotina:
1. Investigar código (Explore/subagente) + testar ao vivo com Playwright, screenshots em `scratchpad/rotinas/<rotina>/screenshots/`.
2. Escrever `doc.py` (blocos de conteúdo) → gera PDF completo, PDF simplificado e `.md`.
3. Escrever `narracoes.json` → `gerar_narracao_google.py` (precisa da chave da API do Google Cloud TTS, que **não fica salva em disco** — pedir de novo a cada sessão, projeto "Clinsis" no Google Cloud Console).
4. `montar_video.py` → `gerar_legendas.py` → `queimar_legendas.py`.
5. `marca/gerar_frames.py "<Título da Rotina>"` → `marca/montar_intro_outro.py` → `marca/aplicar_intro_outro.py` (com legenda e sem legenda).
6. Copiar PDFs/MD/vídeos + pasta `scripts/` para `Documentacao-Entrega/<Rotina>/`.

## 21. Manual Base do ClinSis (23/09/2026)
PDF completo + simplificado + MD prontos em `Manual-Base-ClinSis/` e incluídos no site MkDocs (categoria "Introdução"). Vídeos (com/sem legenda, ~3m55s) entregues; pipeline reutilizável em `scripts/pipeline-video/` (usa a variável GCP_TTS_KEY, chave pedida a cada sessão).

## 22. Área do Profissional (24/09/2026)
PDF completo + simplificado + MD + vídeos (com/sem legenda, ~3m38s) em `Area-do-Profissional/`, feitos com usuário de perfil Profissional (login de teste 55555555555). Link do YouTube ainda pendente (a capa do PDF cita o nome do arquivo até o link existir).
Site: agora só o PDF simplificado é publicado e o texto é limpo de informação técnica (ver `limpar_para_usuario_final` em `site/scripts/gerar_site_docs.py`).
