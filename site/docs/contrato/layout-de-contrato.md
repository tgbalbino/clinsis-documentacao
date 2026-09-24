# Layout de Contrato

_O modelo (template) usado para gerar o PDF de todos os contratos da clínica_

## Documentação em PDF

- [📄 Manual em PDF](../assets/Layout-de-Contrato/Documentacao_Layout_Contrato_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/w-cCTVEKQng?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/w-cCTVEKQng)

## Conteúdo completo do manual

---


_O modelo (template) usado para gerar o PDF de todos os contratos da clínica_

Versão 1.0 — 18/09/2026

Esta tela define o texto/modelo que vira o PDF de qualquer contrato da clínica — tanto o PDF baixado para impressão quanto o PDF enviado para assinatura eletrônica pela D4Sign. É um pré-requisito compartilhado pelas rotinas Contrato (sem assinatura digital) e Contrato (com assinatura digital D4Sign): sem um layout ativo configurado, nenhuma delas consegue gerar ou enviar um contrato.

---

## Onde fica e o que é

Em Tabelas Aux. → Layout Contrato (rota /aux/contratolaiout), a clínica escreve o texto do contrato em Markdown (um formato de texto simples com marcações como **negrito** e # Título), usando "variáveis" entre chaves duplas que o sistema troca automaticamente pelos dados reais de cada contrato na hora de gerar o PDF (nome do paciente, valor, datas, etc.).


> ⚠️ Só existe um layout ativo por clínica — não há como ter um modelo diferente por tipo de contrato, convênio ou especialidade. Ativar um novo layout muda o conteúdo do PDF de todos os contratos gerados a partir daquele momento (contratos já fechados/já enviados antes não são afetados, pois o PDF deles já foi gerado).

## Editando o layout

Ao clicar em "Editar" (ou "Novo layout"), aparece uma caixa de texto grande para o conteúdo em Markdown, e a lista de todas as variáveis disponíveis logo abaixo dela.



| Campo / Label na tela | O que é / de onde vem |
|---|---|
| Dados da clínica | {{ClinicaNomeFantasia}}, {{ClinicaRazaoSocial}}, {{ClinicaCnpj}}, {{ClinicaEndereco}}, {{ClinicaCidade}}, {{ClinicaUf}}, {{ClinicaTelefone}}, {{ClinicaEmail}}, {{ClinicaResponsavelNome}}, {{ClinicaResponsavelCPF}} |
| Dados do contrato | {{ContratoId}}, {{ContratoDataEmissao}}, {{ContratoDataVencimento}}, {{ContratoValorTotal}}, {{ContratoObservacao}}, {{DataAtual}} (data em que o PDF foi gerado) |
| Dados do paciente | {{PacienteNome}}, {{PacienteCPF}}, {{PacienteDataNascimento}}, {{PacienteEndereco}} |
| Dados do responsável | {{ResponsavelNome}}, {{ResponsavelCPF}}, {{ResponsavelEndereco}} (se não houver responsável cadastrado, usam os dados do próprio paciente), e {{RelacaoResponsavelLinha}} (linha "Relação com o paciente" — só aparece quando há responsável com relação preenchida) |
| Tabelas prontas | {{TabelaServicos}} (lista os serviços contratados: nome, quantidade, valor unitário e total) e {{TabelaPagamentos}} (lista as condições de pagamento: forma, valor, parcelas, 1ª e última parcela) — cada uma vira uma tabela pronta no PDF |

> ⚠️ A substituição é por texto exato — {{PacienteNome}}, sem espaços e com a grafia exatamente como na lista. Copiar o código da própria lista de variáveis evita erro de digitação.

## Modelo padrão pronto

Quem está criando um layout do zero não precisa escrever um contrato inteiro na mão: o botão "Usar modelo padrão" preenche o campo com um contrato de prestação de serviços completo e pronto (objeto, vigência, condições de pagamento, obrigações das partes, LGPD, cláusula de assinatura eletrônica, foro), já usando as variáveis corretas — só ajustar o que for necessário para a realidade da clínica.



## Pré-visualizando antes de ativar

O botão "Visualizar PDF de exemplo" gera um PDF de verdade a partir do texto que está no campo naquele momento — mesmo sem salvar — substituindo as variáveis por dados fictícios de exemplo (paciente, responsável, serviços e pagamento inventados). É a forma certa de conferir como o contrato vai ficar (formatação, quebras de linha, tabelas) antes de salvar e ativar o layout para valer.


> ⚠️ Sempre use "Visualizar PDF de exemplo" antes de marcar "Deixar ativo" e salvar. Um erro de digitação nas chaves de uma variável (ex.: colar um texto com acentuação de outra origem/codificação) pode corromper a acentuação de todo o contrato gerado a partir dali — inclusive dos contratos enviados para assinatura na D4Sign — e isso só aparece visualmente no PDF, não no texto do editor.

## Ativando um layout

Ao salvar um layout com a caixa "Deixar ativo" marcada (ou clicar em "Ativar" na listagem, para um layout já existente), ele passa a ser o único usado para gerar contratos daquele momento em diante — o layout que estava ativo antes é automaticamente desativado, mas continua salvo no histórico, podendo ser reativado depois se necessário.
