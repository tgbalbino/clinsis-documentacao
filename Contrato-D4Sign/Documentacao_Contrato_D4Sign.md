# Contrato com Assinatura Digital (D4Sign)

_Envio para assinatura eletrônica, acompanhamento e fechamento automático_

Versão 1.1 — 29/09/2026

Este manual complementa o de Contrato (sem assinatura digital), cobrindo o que muda quando a clínica usa a integração com a D4Sign para colher a assinatura do paciente eletronicamente, em vez de assinar manualmente no sistema. O ciclo de vida do contrato (Criado → Assinado → Fechado, com geração automática de Conta a Receber) continua o mesmo — o que muda é como a assinatura acontece: em vez de um clique interno, o paciente assina de verdade, remotamente, e o próprio sistema fecha o contrato sozinho assim que a assinatura é confirmada.

Assista ao vídeo narrado desta rotina: [https://youtu.be/eg7ABN_eNyo](https://youtu.be/eg7ABN_eNyo)

---

> ⚠️ Para o contrato poder ser fechado/enviado para assinatura, a clínica também precisa ter um Layout de Contrato ativo configurado (o modelo/template que vira o PDF enviado à D4Sign) — veja o manual separado "Layout de Contrato" para essa configuração.

## Configuração prévia (feita uma vez pela equipe técnica)

Antes de qualquer contrato poder ser enviado para assinatura, a integração precisa estar configurada em Tabelas Aux. → D4Sign (rota /aux/d4sign): token de acesso da conta D4Sign, UUID do cofre onde os documentos são guardados, ambiente (Sandbox para testes ou Produção) e a URL pública do webhook — o endereço que a D4Sign chama de volta para avisar o ClinSis quando algo acontece com a assinatura (documento visualizado, assinado, finalizado, cancelado).

![Tela de Configuração D4Sign: no topo o resumo (Integração Ativa, Conexão Homologada, Ativação Pronta), abas Configuração/Status/Auditoria e, na aba Configuração, ambiente Sandbox/Produção, credenciais salvas (campos em branco mantêm o valor salvo), cofre de documentos e webhook.](00-config-d4sign.png)

_Tela de Configuração D4Sign: no topo o resumo (Integração Ativa, Conexão Homologada, Ativação Pronta), abas Configuração/Status/Auditoria e, na aba Configuração, ambiente Sandbox/Produção, credenciais salvas (campos em branco mantêm o valor salvo), cofre de documentos e webhook._

> ⚠️ A URL do webhook precisa ser um endereço público (HTTPS) que realmente chegue até a API do ClinSis. Em produção, é o domínio real do servidor; em ambiente de desenvolvimento, é comum usar um túnel temporário (ex.: Cloudflare Tunnel) apontando para a máquina local — só funciona enquanto esse túnel estiver rodando.

## Enviando o contrato para assinatura eletrônica

No topo do contrato salvo há a opção Assinatura eletrônica (D4Sign): "Assinar pela D4Sign" (padrão da clínica) ou "Não assinar". Dispensar a assinatura exige liberação administrativa e é explicado no manual de Contrato. Com "Assinar pela D4Sign" selecionado, o contrato só pode ser fechado depois que a assinatura for concluída.

Com o contrato criado, serviços e condição de pagamento preenchidos (igual à versão sem D4Sign), em vez de marcar "assinado" manualmente, clique em "Enviar para assinatura". O sistema avisa que, após o envio, os dados do contrato ficam bloqueados — ele deixa de poder ser editado a partir daqui.

![Contrato pronto (serviços e acerto batendo): no topo a opção "Assinar pela D4Sign / Não assinar" e, no rodapé, o botão "Enviar para assinatura". O aviso amarelo lembra que a assinatura eletrônica é obrigatória antes do fechamento.](01-contrato-pronto-enviar-assinatura.png)

_Contrato pronto (serviços e acerto batendo): no topo a opção "Assinar pela D4Sign / Não assinar" e, no rodapé, o botão "Enviar para assinatura". O aviso amarelo lembra que a assinatura eletrônica é obrigatória antes do fechamento._

![Confirmação: "Deseja enviar este contrato para assinatura eletrônica? Após o envio, os dados ficarão bloqueados."](02-confirmar-enviar-assinatura.png)

_Confirmação: "Deseja enviar este contrato para assinatura eletrônica? Após o envio, os dados ficarão bloqueados."_

Ao confirmar, o sistema, em sequência: gera o PDF do contrato, envia esse PDF para a D4Sign, cadastra o(s) signatário(s) e dispara o convite de assinatura por e-mail. O signatário é o responsável do contrato, se houver um cadastrado, ou o próprio paciente quando não há responsável — o e-mail usado é sempre o que está no cadastro da pessoa no ClinSis.

## Acompanhando a assinatura

A assinatura em si acontece fora do ClinSis, na página da D4Sign — o paciente/responsável recebe o e-mail, abre o link, confere e assina o documento eletronicamente. Dentro do ClinSis, a aba "Histórico da assinatura" do contrato registra cada evento recebido (documento enviado, visualizado, assinado, finalizado), com data e situação (Processado/Pendente).

![Contrato com a assinatura finalizada: a aba Histórico da assinatura lista cada evento recebido (aqui "Finalizado", capturado por sincronização). O alerta amarelo mostra que o fechamento automático falhou e o botão "Fechar Contrato" reprocessa.](05-historico-assinatura.png)

_Contrato com a assinatura finalizada: a aba Histórico da assinatura lista cada evento recebido (aqui "Finalizado", capturado por sincronização). O alerta amarelo mostra que o fechamento automático falhou e o botão "Fechar Contrato" reprocessa._

> ⚠️ Normalmente, o ClinSis fica sabendo que a assinatura avançou automaticamente, via webhook: assim que a D4Sign confirma um evento, ela avisa o ClinSis na hora, sem precisar de nenhuma ação da equipe. Se por algum motivo esse aviso automático não chegar (problema de rede, webhook temporariamente fora do ar), existe o botão Sincronizar com a D4Sign (ícone circular) para consultar o status manualmente a qualquer momento — foi exatamente esse botão que capturou o "Finalizado" no exemplo acima.

## Fechamento automático após a assinatura

Assim que a assinatura é confirmada (via webhook ou via Sincronizar), o ClinSis marca o contrato como Assinado e tenta fechá-lo automaticamente — o mesmo processo do botão manual "Fechar Contrato": gera as parcelas em Contas a Receber e trava o contrato definitivamente. Tudo isso acontece sem qualquer clique da equipe.

![Contrato com os selos "Assinatura finalizada" e "Contrato fechado", e o botão "PDF assinado", que baixa o documento assinado eletronicamente. Aparecem também Renovar e Não vai renovar.](04-contrato-fechado-automaticamente.png)

_Contrato com os selos "Assinatura finalizada" e "Contrato fechado", e o botão "PDF assinado", que baixa o documento assinado eletronicamente. Aparecem também Renovar e Não vai renovar._

![Conferindo em Contas a Receber: a parcela gerada pelo fechamento automático deste contrato aparece normalmente, com Situação "Aberto" — igual à versão sem D4Sign.](06-conta-a-receber-gerada.png)

_Conferindo em Contas a Receber: a parcela gerada pelo fechamento automático deste contrato aparece normalmente, com Situação "Aberto" — igual à versão sem D4Sign._

> ⚠️ Se o fechamento automático falhar por algum motivo (ex.: parâmetro de Plano de Conta ou Centro de Custo do Contrato não configurado), o contrato fica assinado mas não fechado, e um alerta amarelo aparece na tela do próprio contrato explicando o motivo da falha — basta corrigir a causa e clicar em "Fechar Contrato" manualmente para reprocessar. Não existe hoje uma lista/relatório central de contratos com falha de fechamento; a conferência é feita contrato por contrato.

## Cancelando uma solicitação de assinatura

Enquanto a assinatura ainda não foi concluída, é possível clicar no ícone de cancelar solicitação (proibido, vermelho) para desistir do envio. O sistema cancela o documento na D4Sign e o contrato volta a ficar liberado para edição — os serviços e a condição de pagamento podem ser revisados e o contrato pode ser reenviado para assinatura depois. Se o documento já tiver sido finalizado (assinado por todos) no momento do cancelamento, o sistema não cancela — em vez disso, apenas atualiza o status para refletir que já foi assinado.
