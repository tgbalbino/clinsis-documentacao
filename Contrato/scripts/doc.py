# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/_scripts-comuns"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts-comuns"))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.1'
DATA = '29/09/2026'
TITULO = 'Contrato (sem assinatura digital)'
SUBTITULO = 'Ciclo de vida completo: criação, fechamento, geração de Conta a Receber, renovação e aviso de vencimento'
VIDEO_NOME = "https://youtu.be/szRnAwHrqI4"
INTRO = 'Contrato formaliza um pacote de sessões vendido ao paciente (ex.: "10 sessões de Fisioterapia"), com um valor total e uma ou mais condições de pagamento (à vista, parcelado no cartão, etc.). Diferente de um agendamento avulso, o Contrato tem um ciclo de vida com fases — criado, assinado, fechado — e, uma vez fechado, gera automaticamente as parcelas em Contas a Receber. Este manual cobre a versão sem assinatura digital (assinatura "no papel", marcada manualmente no sistema); a versão com assinatura eletrônica pela D4Sign é documentada à parte.'
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [('aviso', 'Para o contrato poder ser fechado/impresso, a clínica precisa ter um Layout de Contrato ativo configurado (o modelo/template que vira o PDF) — veja o manual separado "Layout de Contrato" para essa configuração.'),
 ('h2', 'As fases do Contrato'),
 ('p', 'O Contrato não tem um único campo de "status" — a fase em que ele está é resultado da combinação de algumas informações: se está Ativo, se já foi Assinado, se já foi Fechado e, depois de fechado, se está pendente de renovação. Na prática, um contrato passa pelas seguintes fases:'),
 ('tabela', [('Criado', 'Contrato recém-cadastrado. Serviços e condição de pagamento podem ser editados livremente.', 'Ativo=Sim, Assinado=Não, Fechado=Não'),
 ('Assinado', 'Marcado manualmente como assinado "no papel" (sem D4Sign). A partir daqui, os dados do contrato não podem mais ser alterados.', 'Assinado=Sim'),
 ('Fechado', 'Botão "Fechar Contrato" acionado: gera as parcelas em Contas a Receber e trava o contrato definitivamente.', 'Fechado=Sim, com data de fechamento'),
 ('Cancelado', 'Pode acontecer a qualquer momento antes de Fechado, desmarcando "Ativo" na edição do contrato. É definitivo — não existe botão para reativar.', 'Ativo=Não'),
 ('Vencendo / Renovado / Não vai renovar', 'Só depois de Fechado: controla se aquele contrato já venceu (ou está perto de vencer) e o que a clínica decidiu fazer a respeito.', 'Status de Renovação')]),
 ('aviso', 'Um contrato assinado não pode mais ser editado — nem os serviços, nem a condição de pagamento. Revise tudo com atenção antes de marcar como assinado.'),
 ('h2', 'Criando um contrato'),
 ('p', 'Em Contrato (menu lateral), clique em Novo, escolha o paciente pela lupa e preencha a Data de Emissão (obrigatória). Depois de salvar, o contrato passa a existir (fase Criado) e as seções de Serviços e Acertos/Pagamentos ficam disponíveis.'),
 ('img', '00-lista-contratos.png', 'Listagem de Contratos: número, paciente, datas, valor, situação (Ativo/Assinado) e os botões de ação de cada linha.'),
 ('p', 'O botão <b>Filtros</b> permite localizar contratos pelo <b>número do contrato</b>, além de paciente, período e situação.'),
 ('img', '00b-filtros.png', 'Janela de Filtros da listagem de Contratos, com o campo de número do contrato.'),
 ('img', '01-novo-contrato-vazio.png', 'Modal de novo contrato: só é possível adicionar serviços depois de salvar com um paciente e uma data de emissão.'),
 ('img', '02-paciente-selecionado.png', 'Paciente selecionado pela busca — e-mail e celular do paciente aparecem automaticamente (vêm do cadastro dele).'),
 ('h2', 'Adicionando Serviços'),
 ('p', 'Na aba "Dados do Contrato", a seção Serviços lista o que o paciente está contratando. Clique em Novo, pesquise o serviço, informe a quantidade de sessões e o valor por sessão — o Valor Total é calculado automaticamente.'),
 ('img', '04-buscar-servico.png', 'Pesquisa de serviço a adicionar ao contrato.'),
 ('img', '06-servico-preenchido.png', 'Serviço "Serviço 001", 2 sessões, R$ 20,00 cada — Valor Total R$ 40,00 calculado automaticamente.'),
 ('img', '07-servico-adicionado.png', 'Serviço salvo e listado na seção Serviços do contrato.'),
 ('h2', 'Condição de Pagamento (Acertos/Pagamentos)'),
 ('p', 'Na aba "Acertos / Pagamentos", cadastre como o paciente vai pagar. Você pode combinar mais de um acerto no mesmo contrato (por exemplo, parte em Pix e o restante no Crediário). Os campos mudam conforme a Forma de Pagamento escolhida:'),
 ('tabelagen', ['Forma', 'O que informar', 'Título gerado em Contas a Receber'], [['Crediário', 'Valor, número de parcelas, data da 1ª e da Última Parcela e, se houver, a Taxa de Juros Mensal.', 'Uma parcela por mês.'], ['Cartão de Crédito', 'Valor, quantas vezes foi passado no cartão (até o máximo aceito pela clínica) e a Data do Pagamento.', 'Um único título com o valor total.'], ['Dinheiro, Pix, Cartão de Débito e demais', 'Valor e Data do Pagamento (por padrão, hoje).', 'Um único título com o valor total.']], [5.833333333333333, 5.833333333333333, 5.833333333333333]),
 ('p', 'O Crediário é a única forma que parcela o pagamento do paciente. As demais são à vista. Para parcelar em Dinheiro ou Pix, use o Crediário.'),
 ('p', 'A soma de todas as condições de pagamento precisa bater exatamente com o total dos Serviços para o contrato poder ser fechado — o card "Falta Acertar" mostra a diferença em tempo real.'),
 ('p', '> ℹ️ O acerto é a condição combinada com o paciente, não o recebimento. O dinheiro só entra no caixa ou na conta financeira quando a parcela é baixada em Contas a Receber, informando como o paciente realmente pagou. O Crediário não aparece nas telas de baixa, porque ele é uma condição do contrato e não um meio de pagamento.'),
 ('img', '09-pagamento-preenchido.png', 'Acerto em Crediário preenchido: R$ 40,00 em 2 parcelas, 1ª parcela em 10/10/2026, com juros mensais (botão "=" preenche o valor que falta acertar).'),
 ('img', '10-pagamento-adicionado.png', 'Acerto salvo na lista; o card "Falta Acertar" zera e os botões "Fechar Contrato" e "Enviar para assinatura" ficam disponíveis.'),
 ('h2', 'Assinatura eletrônica, dispensa ou assinatura em papel'),
 ('p', 'Depois de salvar, o topo do contrato mostra a opção <b>Assinatura eletrônica (D4Sign)</b>, com dois botões: "Assinar pela D4Sign" e "Não assinar". O valor inicial segue o padrão da clínica (parâmetro de assinatura). Se a clínica assina pela D4Sign, o contrato é enviado pelo botão "Enviar para assinatura" e o fluxo segue como no manual de Contrato com D4Sign. Se este contrato não vai ser assinado eletronicamente, clique em <b>Não assinar</b>.'),
 ('img', '03-contrato-criado.png', 'Contrato salvo: no topo, a opção "Assinatura eletrônica (D4Sign)" com os botões "Assinar pela D4Sign" e "Não assinar".'),
 ('p', 'Dispensar a assinatura exige <b>liberação administrativa</b>: quem é Administrador escolhe apenas o <b>Motivo</b> (lista de motivos cadastrada); os demais usuários precisam informar também o login e a senha de um Administrador. A dispensa fica registrada no contrato (quem dispensou, quem liberou, quando e o motivo).'),
 ('img', '11-liberacao-dispensa-assinatura.png', 'Janela "Dispensar assinatura eletrônica": o Motivo é obrigatório.'),
 ('img', '12-assinatura-dispensada.png', 'Assinatura dispensada: o topo mostra quem dispensou, quando e o motivo; o próximo passo é fechar o contrato.'),
 ('p', 'Se a clínica prefere registrar a assinatura no papel, na listagem de Contratos clique no botão de caneta/download da linha e, no modal que abre, em "Marcar como assinado" (esse botão só aparece se o contrato ainda não estiver assinado). O mesmo modal permite baixar o PDF do contrato para impressão e assinatura física.'),
 ('img', '11-modal-download-assinar.png', 'Modal "Download contrato / Assinar", com os botões Baixar documento e Marcar como assinado.'),
 ('h2', 'Fechando o Contrato (gera a Conta a Receber)'),
 ('p', 'Com o contrato assinado (ou mesmo sem assinar, se a clínica não exigir isso), abra-o de novo e clique em Fechar Contrato. O botão só fica habilitado se houver pelo menos um Serviço, pelo menos uma condição de Pagamento, e a diferença entre os dois totais for zero. Ao confirmar, o sistema gera, de uma só vez, os títulos em Contas a Receber — uma parcela por mês para cada acerto em Crediário e um único título para cada acerto à vista ou no cartão — e o contrato fica travado definitivamente (nunca mais pode ser editado).'),
 ('img', '14-confirmar-fechar-contrato.png', 'Confirmação: "As parcelas serão geradas em Contas a Receber e os serviços/pagamento não poderão mais ser alterados."'),
 ('img', '15-apos-fechar-contrato.png', 'Contrato fechado: aviso "As parcelas foram geradas em Contas a Receber" e novos botões Renovar / Não vai renovar aparecem.'),
 ('img', '16-conta-a-receber-gerada-pelo-contrato.png', 'Contas a Receber: as parcelas do contrato aparecem com a coluna "Origem" (ex.: "Contrato 15 - Crediário 1/2"), Situação "Aberto".'),
 ('aviso', 'Só é possível fechar um contrato se dois parâmetros de sistema estiverem configurados para a clínica: Plano de Conta do Contrato e Centro de Custo do Contrato (tela de Parâmetros). São eles que definem em qual Plano de Conta/Centro de Custo as parcelas geradas vão cair em Contas a Receber.'),
 ('h2', 'Aviso de vencimento (contratos "vencendo")'),
 ('p', 'Uma vez por dia (de madrugada), o sistema verifica todos os contratos já fechados e ainda não renovados, e gera um aviso para a equipe administrativa quando a última parcela cadastrada estiver perto de vencer (por padrão, até 30 dias antes). Esse aviso aparece como uma notificação no sino no canto superior direito do sistema, com um balão mostrando o contrato e o paciente — clicar nele leva direto para a lista de contratos vencendo.'),
 ('img', '17-contratos-vencendo.png', 'Tela de Contratos filtrada em "modo vencendo" (acessível também diretamente pelo link /contrato?vencendo=1).'),
 ('h2', 'Configurando quantos dias de antecedência do aviso'),
 ('p', 'O prazo de antecedência do aviso é configurável por clínica, em Tabelas Aux. → Parâmetros, no parâmetro DiasAvisoVencContrato ("Quantos dias antes do vencimento do plano o sistema avisa o financeiro que o Contrato está vencendo") — se não for configurado, o sistema usa 30 dias como padrão. No exemplo abaixo, está configurado para 30 dias.'),
 ('img', '24-parametros-lista.png', 'Tela de Parâmetros: o parâmetro de dias de aviso aparece na lista, junto com os demais parâmetros do Contrato (Plano de Conta, Centro de Custo, exigência de assinatura D4Sign).'),
 ('img', '25-parametro-dias-aviso-editar.png', 'Editando o parâmetro DiasAvisoVencContrato: valor atual 30 dias.'),
 ('aviso', 'Este é um aviso interno, para a equipe agir — ligar para o paciente, mandar mensagem por fora do sistema, negociar a renovação. Nesta versão sem D4Sign, o sistema não envia nenhuma notificação automática (e-mail/WhatsApp) diretamente ao paciente ou responsável sobre o contrato.'),
 ('h2', 'Renovando um contrato'),
 ('p', 'Com o contrato fechado e ainda não renovado, o botão Renovar fica disponível. Ao confirmar, o sistema cria um contrato novo, copiando os mesmos Serviços e a mesma condição de Pagamento do contrato original — mas com as datas deslocadas: os acertos em Crediário continuam no mês seguinte ao da última parcela do contrato antigo, e os acertos à vista ou no cartão passam a ter a data de hoje. O contrato antigo não é alterado (continua fechado, com suas parcelas já geradas intactas); ele só ganha a marca "Renovado" e some da lista de vencendo. O novo contrato nasce na fase "Criado" — revise os dados e feche-o normalmente quando estiver pronto.'),
 ('img', '19-confirmar-renovar.png', 'Confirmação de renovação: "Um novo contrato será criado copiando os serviços e a condição de pagamento deste."'),
 ('img', '20-apos-renovar-lista.png', 'Aviso "Contrato renovado. Revise os dados do novo contrato antes de fechar." — o novo contrato aparece na listagem (linha destacada).'),
 ('h2', 'Quando o paciente não vai renovar'),
 ('p', 'Se a equipe já sabe que o paciente não vai continuar, em vez de Renovar, clique em Não vai renovar. Isso não cria contrato nenhum — apenas marca o contrato atual com esse status e para de gerar o aviso de vencimento para ele.'),
 ('img', '22-confirmar-nao-vai-renovar.png', 'Confirmação: "O aviso de vencimento deixará de ser gerado."'),
 ('img', '23-apos-nao-vai-renovar.png', 'Contrato marcado com o badge "Não vai renovar" e aviso de confirmação.')]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contrato.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Contrato_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Contrato.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
