# -*- coding: utf-8 -*-
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "_scripts-comuns"))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = "1.1"
DATA = "24/09/2026"
TITULO = "Área do Profissional"
SUBTITULO = "O que o profissional de saúde vê e pode fazer no ClinSis"
VIDEO_NOME = "video-area-do-profissional-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('Este manual mostra, passo a passo, o dia a dia do <b>profissional de saúde</b> no ClinSis: '
         'a Home, a agenda e os pacientes do dia, os pacientes, os prontuários e relatórios, os textos '
         'padrões, o atendimento, o protocolo e o perfil. O menu do profissional é menor que o do '
         'administrador, e algumas opções só aparecem se a clínica ativou o módulo correspondente.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), com um usuário de perfil Profissional. '
          'Nenhum dado de produção foi acessado.')

blocos = [
    ('h1', '1. Menu e Home do profissional'),
    ('p', 'O menu do profissional é menor que o do administrador. Algumas opções só aparecem se a clínica ativou o módulo ou a configuração correspondente.'),
    ('tabelagen', ['Opção do menu', 'Aparece quando'], [
        ['Agenda', 'Módulo Agenda ativo'],
        ['Pacientes', 'Configuração "Profissional pode ver pacientes" ativa'],
        ['Prontuário', 'Módulo Prontuário ativo'],
        ['Atendimento (Listar)', 'Módulo Receituário ativo'],
        ['Atendimento > Pacientes do dia', 'Módulo Receituário ativo e clínica no modelo consultório'],
        ['Protocolo', 'Módulo Protocolo ativo'],
        ['Perfil, Home e Sair', 'Sempre'],
    ], [6.5, 11]),
    ('aviso', 'Se falta uma opção no menu, o módulo ou a configuração não está ativo na sua clínica. Fale com o administrador. '
              'O profissional <b>não vê</b> os menus de Cadastros, Tabelas Auxiliares, Financeiro, Relatórios, Caixa e Doc. Faturamento.'),
    ('img', 'p01-home.png', 'Home do profissional: cartões de atalho (Agenda, Prontuário, Protocolo, Atendimentos), resumo do dia e pendências gerais.'),
    ('h2', 'Cartões de atalho'),
    ('tabelagen', ['Cartão', 'O que faz'], [
        ['Agenda', 'Lista os dois últimos meses de agenda, cada um com o botão <b>Agenda resumida</b>. O link <b>Agenda detalhada</b> abre a lista de pacientes do dia.'],
        ['Prontuário', 'Abre seus prontuários e tem o link <b>Textos padrões</b>. Só aparece com o módulo Prontuário ativo.'],
        ['Protocolo', 'Só aparece com o módulo Protocolo ativo.'],
        ['Atendimentos', 'Abre "Pacientes do dia" do consultório. Só aparece se a clínica for consultório.'],
        ['Alterar Perfil', 'Só aparece se o seu usuário tem um segundo perfil de acesso.'],
    ], [3.6, 13.9]),
    ('h2', 'Resumo do dia e pendências'),
    ('p', 'Logo abaixo aparece uma faixa com os números de hoje (disponível para todas as clínicas, sem configuração): <b>Total de Pacientes, Total de Presentes, '
          'Relatórios Finalizados, Relatórios Abertos, Evoluções Finalizadas e Evoluções Abertas</b>. Em <b>Pendências gerais</b> você vê as '
          'Evoluções Abertas e os Relatórios Abertos no geral. Pendência é algo que você começou e ainda não finalizou.'),

    ('h1', '2. Agenda'),
    ('p', 'Menu <b>Agenda</b>: lista de Ano/Mês. Em cada linha, o botão <b>Acessar</b> abre a Agenda resumida do mês. '
          'Se a clínica não for consultório, aparece também o link <b>Ver lista simples de pacientes do dia</b>.'),
    ('img', 'p02-agenda.png', 'Menu Agenda do profissional: só o botão Acessar por mês.'),
    ('aviso', 'O profissional não pode criar nem remover agendas, e não vê os botões Relatório, Horários, Acessar (grade de agendamento) e Divergência Sessões. Esses são do administrador e do atendente.'),
    ('h2', 'Agenda resumida'),
    ('p', 'Mostra os seus pacientes agendados no mês. Recursos:'),
    ('tabelagen', ['Recurso', 'Como usar'], [
        ['Ver Pacientes / Ver Planilha', 'Alterna entre a visão por paciente e a visão em tabela.'],
        ['Pacientes do dia', 'Marque a caixa, informe a data e clique em Carregar.'],
        ['Confirmação WhatsApp', 'Só aparece se o módulo WhatsApp estiver ativo.'],
        ['Filtros da tabela', 'Filtre por Dia, Data, Hora e Paciente.'],
        ['Ícone verde ao lado do paciente', 'Indica que o prontuário de evolução diária de hoje já foi finalizado.'],
    ], [5.6, 11.9]),
    ('img', 'p03-agenda-resumida.png', 'Agenda resumida do mês: dia, hora e paciente de cada horário.'),
    ('p', '<b>Criar prontuário a partir da agenda:</b> dê dois cliques no paciente (ou clique em Prontuários, na visão por paciente), '
          'escolha o <b>Tipo</b> de prontuário, a <b>Especialidade</b> e confirme a inclusão.'),
    ('aviso', 'Se a clínica bloqueou a criação de prontuários, nada acontece ao clicar. Para prontuário de evolução diária, não é permitido usar data futura.'),
    ('h2', 'Pacientes do dia (Agenda detalhada)'),
    ('p', 'Acesse pelo link <b>Agenda detalhada</b> da Home, ou <b>Ver lista simples de pacientes do dia</b> na Agenda. '
          'Escolha a data e clique em <b>Pesquisar</b>. A lista mostra dia, hora, paciente, celular, situação da guia, operadora, '
          'programa, observação e o status das sessões S1 a S5. Se a clínica permitir, aparece o botão <b>Marcar Presença</b> em cada linha.'),
    ('img', 'p03b-pacientes-dia.png', 'Pacientes por Dia: lista do dia com status das sessões e o botão Marcar Presença.'),

    ('h1', '3. Pacientes'),
    ('p', 'Menu <b>Pacientes</b>, só com a configuração "Profissional pode ver pacientes" ativa. Sem ela, o sistema volta para a Home. '
          'O profissional pode <b>ver a lista</b> e abrir o cadastro de um paciente existente.'),
    ('img', 'p04-pacientes.png', 'Lista de pacientes (dados ocultados neste manual).'),
    ('tabelagen', ['O profissional NÃO pode', 'Detalhe'], [
        ['Cadastrar paciente novo', 'O botão de cadastrar fica oculto.'],
        ['Baixar a ficha do paciente', 'O botão fica oculto.'],
        ['Alterar os dados adicionais', 'Os campos ficam bloqueados.'],
        ['Abrir o cadastro sem escolher paciente', 'É preciso abrir a partir da lista.'],
    ], [6.5, 11]),

    ('h1', '4. Prontuário'),
    ('p', 'Menu <b>Prontuário</b> (com o módulo Prontuário ativo): criar, preencher e finalizar prontuários e relatórios dos seus pacientes.'),
    ('h2', 'Lista de prontuários'),
    ('p', 'Para ver a lista, use <b>Pesquisa</b> e escolha o <b>Tipo</b> (obrigatório). Filtros: Nº do prontuário, nome do paciente, '
          'emissão e inclusão (data inicial e final), Finalizado (Todos, Finalizado ou Digitação), Ordenação e Tags (se ativas).'),
    ('img', 'p05-prontuarios-filtro.png', 'Filtro de prontuários: o Tipo é obrigatório.'),
    ('p', 'A lista mostra automaticamente o <b>seu</b> profissional, com as colunas Nº, Profissional, Paciente, Mãe, Situação, Início, '
          'Finalização e Emissão. Uma etiqueta <b>compartilhado</b> indica um relatório de outro profissional da mesma especialidade; linhas em cor '
          'diferente indicam prontuário atrasado.'),
    ('img', 'p05b-prontuarios-lista.png', 'Lista de prontuários do tipo Evolução diária, com Situação Finalizada ou Digitação.'),
    ('tabelagen', ['Botão', 'O que faz'], [
        ['Novo', 'Cria um prontuário (escolhe o paciente). Não aparece se a clínica bloqueou a criação.'],
        ['Olho', 'Visualiza o prontuário.'],
        ['Bloco amarelo', 'Abre para preencher. Só nos prontuários que são seus.'],
        ['Lixeira', 'Exclui. Só prontuário seu que ainda está em Digitação, com confirmação.'],
        ['tags', 'Mostra as tags do prontuário (se ativas).'],
        ['Impressora (rodapé)', 'Gera o PDF dos prontuários marcados. Só é possível marcar os finalizados.'],
    ], [4, 13.5]),
    ('img', 'p05c-prontuario-novo.png', 'Novo prontuário: escolha o paciente (da agenda atual ou por dados) e a especialidade.'),
    ('aviso', 'O profissional não pode excluir prontuário finalizado nem de outro profissional, e não exporta CSV (isso é do administrador).'),
    ('h2', 'Preencher o prontuário'),
    ('p', '1. Abra o prontuário no bloco amarelo. 2. Informe a <b>Data de emissão</b>. 3. Responda cada <b>Alínea</b> (pergunta), usando '
          '<b>Anterior</b> e <b>Próxima</b>. 4. Clique em <b>Salvar</b>. 5. Com todas as alíneas respondidas, clique em <b>Finalizar</b>.'),
    ('img', 'p06c-prontuario-preencher.png', 'Preenchimento do prontuário: data de emissão, tags, alínea, texto e os botões Salvar e Finalizar.'),
    ('tabelagen', ['Tipo de resposta', 'Como funciona'], [
        ['Texto livre', 'Até 50.000 caracteres.'],
        ['Sim ou Não', 'Marque a opção.'],
        ['Arquivo PDF', 'Envie o arquivo ou visualize o já salvo.'],
        ['Texto Padrão', 'Escolha o texto na lista para inserir.'],
    ], [4, 13.5]),
    ('aviso', 'Inserir um texto padrão apaga o que você já digitou no campo. E, depois de <b>Finalizar</b>, o prontuário não pode mais ser editado por você: somente o administrador pode reabrir.'),
    ('h2', 'Visualizar e imprimir'),
    ('p', 'A visualização mostra todas as alíneas. Com o prontuário finalizado, use <b>Página de impressão / Download</b>.'),
    ('img', 'p06-prontuario-visualizar.png', 'Prontuário finalizado em modo de visualização.'),
    ('h2', 'Textos padrões'),
    ('p', 'Na Home, no cartão Prontuário, o link <b>Textos padrões</b> guarda textos que você usa sempre. Clique em <b>Novo</b>, escolha o '
          '<b>Tipo de prontuário</b>, digite o <b>Título</b> (máximo de 20 caracteres) e o <b>Texto</b>, e clique em Salvar. Para mudar, '
          'use Visualizar/Alterar; para apagar, a lixeira. O tipo não pode ser trocado depois de salvo.'),
    ('img', 'p07-textos-padrao.png', 'Lista de textos padrões por tipo de prontuário.'),
    ('img', 'p07b-texto-padrao-novo.png', 'Novo texto padrão: tipo, título e texto.'),

    ('h1', '5. Atendimento (receituário)'),
    ('p', 'Menu <b>Atendimento</b>, com o módulo Receituário ativo: registra consultas com receita de medicamentos e pedido de exames. '
          'Em <b>Atendimento > Listar</b> aparecem os <b>seus</b> atendimentos, com filtros por paciente, data inicial e final e '
          '"Filtrar atendimentos do dia atual".'),
    ('img', 'p08-atendimento.png', 'Atendimentos: lista com Profissional, Paciente, Data, Horário e Finalizado.'),
    ('tabelagen', ['Botão por linha', 'O que faz'], [
        ['Finalizar Atendimento', 'Só aparece se o atendimento ainda não foi finalizado.'],
        ['Visualizar', 'Abre o atendimento.'],
        ['Imp. Completo, Imp. Exames e Imp. Medicamentos', 'Imprimem o atendimento inteiro ou só exames ou só medicamentos.'],
    ], [6.5, 11]),
    ('p', 'Na <b>ficha do atendimento</b> há Novo Medicamento, Novo Exame, Anamnese (preenchimento pelo prontuário) e Observação (opcional). '
          'Depois de finalizado, a ficha fica somente para leitura.'),
    ('p', '<b>Atendimento > Pacientes do dia</b> (clínica no modelo consultório): mostra Paciente, Data, Horário e se está Finalizado. '
          'Use <b>Atendimento</b> para abrir a ficha (ou dois cliques na linha), <b>Finalizar Atendimento</b> e <b>Ver últimos atendimentos</b>.'),

    ('h1', '6. Protocolo'),
    ('p', 'Menu <b>Protocolo</b> (com o módulo Protocolo ativo): registrar e acompanhar solicitações com prazo, entre pessoas da clínica.'),
    ('img', 'p09-protocolo.png', 'Lista de protocolos: datas, solicitante, destinatários, tipo, status, prazo e atendido.'),
    ('p', 'A lista tem protocolo, data de alteração, data limite, solicitante, usuário e profissional destinatários, tipo, status, prazo em dias, '
          'atendido e data de finalização. Filtre por tipo, status, solicitante, destinatário, atendido e período de inclusão. Para criar, '
          'clique em <b>Novo</b> e informe Tipo, Situação, Data Limite, Prazo de entrega (dias), Solicitante, Usuário destinatário, '
          'Profissional destinatário e Data do atendimento.'),

    ('h1', '7. Perfil'),
    ('p', 'Menu <b>Perfil</b>: cuidar dos dados da sua conta. Mostra nome, e-mail, situação (Ativo ou Inativo), perfil de acesso e data de cadastro.'),
    ('img', 'p10-perfil.png', 'Perfil: dados da conta (e-mail ocultado neste manual) e as opções Alterar Dados e Alterar Senha.'),
    ('tabelagen', ['Opção', 'Como usar'], [
        ['Alterar Dados', 'Altere Nome, E-mail e Data de nascimento. Digite sua senha para confirmar.'],
        ['Alterar Senha', 'Informe a senha atual, a nova senha e repita a nova senha.'],
    ], [4, 13.5]),

    ('h1', '8. Resumo: o que o profissional não faz'),
    ('tabelagen', ['Não faz', 'Quem faz'], [
        ['Criar ou remover agendas', 'Administrador / Atendente'],
        ['Cadastrar pacientes', 'Administrador / Atendente'],
        ['Excluir prontuário finalizado ou de outro profissional', 'Ninguém pelo profissional; só exclui o próprio prontuário em Digitação'],
        ['Reabrir prontuário finalizado', 'Administrador'],
        ['Acessar Financeiro, Relatórios, Caixa, Doc. Faturamento e Tabelas Auxiliares', 'Administrador / Atendente'],
    ], [9, 8.5]),
]

render_pdf(blocos, os.path.join(ENTREGA, 'Documentacao_Area_do_Profissional.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocos, os.path.join(ENTREGA, 'Documentacao_Area_do_Profissional_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocos, os.path.join(ENTREGA, 'Documentacao_Area_do_Profissional.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
