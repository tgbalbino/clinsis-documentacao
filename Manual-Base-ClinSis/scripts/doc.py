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

VERSAO = "1.0"
DATA = "23/09/2026"
TITULO = "Manual Base do ClinSis"
SUBTITULO = "O que é o sistema, o fluxo geral, os cadastros, a criação da agenda e as impressões"
VIDEO_NOME = "https://youtu.be/r7iJc03azkw"
INTRO = ('Este é o <b>manual de entrada</b> do ClinSis. Ele explica, em linguagem simples, o que o sistema '
         'faz, como as partes se encaixam (Cadastros → Agenda → Atendimento/Prontuário → Financeiro), quais '
         'cadastros precisam existir antes de agendar, como criar a agenda do mês, como configurar os '
         'horários e agendar pacientes, e para que serve cada impressão da agenda.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocos = [
    # ------------------------------------------------------------------ 1
    ('h1', '1. O que é o ClinSis'),
    ('p', 'O <b>ClinSis</b> é um sistema web de gestão para clínicas de atendimento em saúde '
          '(fisioterapia, fonoaudiologia, psicologia, nutrição, terapia ocupacional e outras). Ele reúne, '
          'num só lugar, o que a clínica faz todos os dias: cadastrar pacientes e profissionais, montar a '
          'agenda mensal, registrar o atendimento e o prontuário, faturar convênios e controlar o '
          'dinheiro que entra e sai.'),
    ('p', 'Funciona pelo navegador (computador, tablet ou celular), sem instalar nada. Cada clínica tem os '
          'seus próprios dados, e cada pessoa da equipe entra com o seu login e enxerga só o que o seu '
          '<b>perfil</b> permite.'),
    ('img', 'a01-home.png',
     'Tela inicial (Home) do administrador: atalhos para Agenda, Doc Faturamento, Prontuário, Caixa, Protocolo e Check-In. '
     'O menu lateral dá acesso a todos os módulos.'),

    ('h2', 'Objetivos do sistema'),
    ('tabelagen', ['Objetivo', 'Como o ClinSis ajuda'], [
        ['Organizar a agenda', 'Agenda mensal por profissional, com horários, pacientes vinculados e controle de presença sessão a sessão.'],
        ['Centralizar o cadastro', 'Um só cadastro de pacientes, profissionais, convênios (operadoras) e usuários, sem planilhas paralelas.'],
        ['Registrar o atendimento', 'Prontuário do paciente feito pelo profissional, com modelos (tipos e alíneas) definidos pela clínica.'],
        ['Controlar o financeiro', 'Contas a Receber (pacientes e convênios), Contas a Pagar (profissionais e despesas), Caixa, Fluxo de Caixa e Dashboard.'],
        ['Dar visibilidade', 'Relatórios e dashboards de agenda, presença, produção e faturamento para a gestão decidir com números.'],
        ['Controlar quem faz o quê', 'Perfis de acesso (Administrador, Atendente, Profissional), setores e permissões extras por usuário.'],
    ], [4.2, 13.3]),

    ('h2', 'Funcionalidades base (menu lateral)'),
    ('tabelagen', ['Menu', 'Para que serve'], [
        ['Cadastros', 'Acessos, Clínica, Setores, Medicação, Exame, Paciente, Profissional, Operadora, Fornecedor e Pessoa.'],
        ['Agenda', 'Criar a agenda do mês, definir os horários dos profissionais e agendar pacientes.'],
        ['Dashboard Agenda', 'Painel gerencial com cartões, gráficos e tabelas da agenda (ocupação, presença, faturamento por convênio).'],
        ['Atendimento', 'Lista dos atendimentos realizados pelos profissionais.'],
        ['Prontuário', 'Tipos e alíneas (modelos), prontuário do profissional e prontuários por paciente.'],
        ['Contrato', 'Contratos de atendimento com pacientes, inclusive com assinatura eletrônica (D4Sign).'],
        ['Doc. Faturamento', 'Guias/documentos de faturamento de convênios e relatório de faturamento.'],
        ['Caixa', 'Abertura e fechamento de caixa, solicitações de cancelamento e histórico.'],
        ['Protocolo', 'Protocolos de atendimento (módulo opcional da clínica).'],
        ['Tabelas Aux.', 'Configurações: Horários, Especialidade, Feriados, Formas de Pagamento, Tabelas de Valores, Parâmetros, Layout de Contrato, entre outras.'],
        ['Relatórios', 'Relatórios de Cobrança, Paciente, Agenda, Prontuário, Pagamentos e Contratos.'],
        ['Financeiro', 'Contas a Pagar, Contas a Receber, Movimentos Financeiros, Plano de Contas, Centro de Custos, Contas Financeiras, Dashboard e Fluxo de Caixa.'],
    ], [3.6, 13.9]),
    ('aviso', 'Alguns módulos (Contrato, Doc. Faturamento, Caixa, Protocolo, Check-In) são <b>opcionais</b> e só '
              'aparecem para clínicas que os contrataram/ativaram.'),

    ('h2', 'Perfis de acesso'),
    ('p', 'Cada usuário tem um <b>perfil principal</b> e, se necessário, um <b>perfil secundário</b>:'),
    ('tabelagen', ['Perfil', 'O que faz'], [
        ['Administrador', 'Acesso total: cadastros, configurações, acessos, agenda, financeiro e relatórios.'],
        ['Atendente', 'Rotina da recepção: cadastros de pacientes, agenda e agendamentos, guias/faturamento e caixa.'],
        ['Profissional', 'Vê a própria agenda e pacientes do dia, registra sessões e faz os prontuários.'],
    ], [3.6, 13.9]),
    ('aviso', 'Regra do sistema: um usuário <b>não pode</b> ter Administrador + Atendente ao mesmo tempo. '
              'Combinações com Profissional (ex.: Atendente + Profissional) são permitidas.'),

    # ------------------------------------------------------------------ 2
    ('h1', '2. Fluxo geral do sistema'),
    ('p', 'Tudo no ClinSis segue uma ordem natural. Cada etapa depende da anterior:'),
    ('img', 'h01-fluxo.png', 'Fluxo geral: Cadastros → Agenda → Atendimento e Prontuário → Financeiro.'),
    ('tabelagen', ['Etapa', 'O que acontece', 'Onde fazer'], [
        ['1. Cadastros', 'Cadastra-se a clínica, os setores, as especialidades, os profissionais, os pacientes, os convênios e os acessos (logins) da equipe.', 'Menu Cadastros e Tabelas Aux.'],
        ['2. Agenda', 'Cria-se a agenda do mês, definem-se os horários de cada profissional e vinculam-se os pacientes aos horários.', 'Menu Agenda'],
        ['3. Atendimento e Prontuário', 'A cada sessão marca-se presença ou ausência; o profissional registra o prontuário do paciente.', 'Agenda (sessões), menus Atendimento e Prontuário'],
        ['4. Contas a Receber', 'O atendimento gera cobrança: pelo Check-in (particular), pela Cobrança de Paciente ou pelo faturamento de convênio. Cada cobrança vira uma <b>Conta a Receber</b>, que é baixada quando o pagamento entra.', 'Financeiro → Contas a Receber'],
        ['4. Contas a Pagar', 'O que a clínica deve pagar — despesas, fornecedores e o <b>pagamento dos profissionais</b> calculado a partir das sessões realizadas — vira <b>Conta a Pagar</b>, baixada quando é paga.', 'Financeiro → Contas a Pagar'],
    ], [3.4, 9.6, 4.5]),
    ('img', 'f05-contas-receber.png',
     'Contas a Receber: cartões de resumo (Em Aberto, Vencido, Vence Hoje, A Vencer, Recebido no Mês) e a lista de cobranças. '
     'Contas a Pagar segue o mesmo modelo.'),
    ('img', 'f03-prontuario.png',
     'Prontuário: o profissional (ou o administrador) filtra e abre os prontuários por tipo, profissional, paciente e período.'),
    ('p', 'Cada uma dessas rotinas financeiras e clínicas tem manual próprio nesta mesma biblioteca de documentação '
          '(Contas a Receber, Contas a Pagar, Checkin, Pagamento de Profissionais, Módulo de Caixa e outros). '
          'Este manual foca na base: <b>Cadastros → Agenda</b>.'),

    # ------------------------------------------------------------------ 3
    ('h1', '3. Cadastros principais para a agenda'),
    ('p', 'Antes de criar qualquer agenda, é preciso que estes cadastros existam. A ordem abaixo evita '
          'retrabalho, pois um depende do outro:'),
    ('tabelagen', ['Ordem', 'Cadastro', 'Menu', 'Por que é necessário'], [
        ['1', 'Clínica', 'Cadastros → Clínica', 'Dados da clínica (endereço, contato, responsável) e contadores de pacientes, profissionais e acessos.'],
        ['2', 'Setores', 'Cadastros → Setores', 'Áreas da equipe (ex.: Recepção, Contabilidade). Usado ao criar o acesso de cada usuário.'],
        ['3', 'Especialidades', 'Tabelas Aux. → Especialidade', 'Tipos de atendimento (Fisioterapia, Psicologia…). Cada agendamento tem uma especialidade.'],
        ['4', 'Operadoras (convênios)', 'Cadastros → Operadora', 'Convênios/planos atendidos. Um atendimento é Particular ou vinculado a um plano.'],
        ['5', 'Profissionais', 'Cadastros → Profissional', 'Quem atende. Só profissionais cadastrados podem ter horários na agenda.'],
        ['6', 'Pacientes', 'Cadastros → Paciente', 'Quem é atendido. Só pacientes cadastrados podem ser vinculados a um horário.'],
        ['7', 'Horários', 'Tabelas Aux. → Horários', 'Lista de horários que a clínica trabalha (07:00, 07:30…). Base para os horários de cada profissional.'],
        ['8', 'Acessos', 'Cadastros → Acessos', 'Logins da equipe (Atendente, Profissional), com perfil e setor.'],
    ], [1.4, 3.4, 4.3, 8.4]),

    ('h2', 'Clínica'),
    ('p', 'Mostra os totais da clínica — pacientes, profissionais e acessos, ativos e inativos — e permite '
          'editar endereço, contato e o <b>responsável</b> (usado na geração de contratos). Também há o '
          'atalho <b>Gerenciar</b> imagens da clínica.'),
    ('img', 'c01b-clinica-topo.png', 'Cadastros → Clínica: cartões com totais de Pacientes, Profissionais e Acessos (ativos/inativos).'),

    ('h2', 'Setores'),
    ('p', 'Lista simples de setores (Financeiro, Contabilidade, Recepção…). Um setor pode ser ativado ou '
          'desativado. Ele é escolhido ao dar acesso a um usuário.'),
    ('img', 'c02-setores.png', 'Cadastros → Setores: nome e situação (ativo/inativo) de cada setor.'),

    ('h2', 'Especialidades'),
    ('p', 'Define os tipos de atendimento da clínica. Cada especialidade tem descrição, abreviação (que aparece '
          'na agenda, ex.: FONO), <b>Tipo de Cobrança</b> (Por Sessão ou Paciente) e '
          '<b>Relatório Compartilhado (Prontuários)</b>, que controla se um profissional enxerga o '
          'prontuário finalizado de um colega. Os detalhes estão no manual "Cadastro de Especialidades".'),
    ('img', 'c03-especialidades.png', 'Tabelas Aux. → Especialidade: descrição, abreviação, tipo de cobrança, compartilhamento de relatório e situação.'),

    ('h2', 'Profissionais'),
    ('p', 'O cadastro do profissional reúne CPF, nome, data de nascimento, <b>Locação</b>, <b>Nome Agenda</b> '
          '(o nome curto que aparece na grade da agenda), registro profissional (conselho), endereço, '
          'contatos e se é estagiário. Os campos marcados com <font color="red">*</font> são obrigatórios. '
          'O profissional pode ser ativado ou inativado (menu Profissional → Inativação).'),
    ('img', 'c05-profissional-cadastro.png', 'Cadastros → Profissional → Cadastro: dados pessoais, endereço e contato.'),

    ('h2', 'Pacientes'),
    ('p', 'O cadastro do paciente pede CPF, titular, nome, data de nascimento, sexo, mãe, pai, estado civil, '
          'endereço e celular (campos com <font color="red">*</font>), além de dados opcionais como RG, '
          'CPS (carteira do convênio), indicação médica, doença/alergia e responsável, com anexo de laudo. '
          'Depois de cadastrado, o paciente pode ser vinculado a horários da agenda. No menu Paciente '
          'também existem <b>Entrada</b> e <b>Saída</b> (registro do tipo, data e motivo da entrada ou saída '
          'do paciente no tratamento) e <b>Inativação</b>.'),
    ('img', 'c07-paciente-cadastro.png', 'Cadastros → Paciente → Cadastro: dados pessoais, endereço, outras informações, responsável e laudo.'),

    ('h2', 'Operadoras (convênios)'),
    ('p', 'Cadastro dos convênios/planos atendidos pela clínica. No agendamento, o paciente atendido por '
          'convênio (Atendimento Particular = Não) é vinculado a uma operadora; o atendimento '
          '"PROPRIO" representa o particular. O submenu tem Listar, Cadastro e a relação de pacientes por operadora.'),
    ('img', 'c08-operadoras.png', 'Cadastros → Operadora → Listar: convênios cadastrados.'),

    # ------------------------------------------------------------------ 4
    ('h1', '4. Cadastro de Acesso (usuários do sistema)'),
    ('p', 'O acesso é o <b>login</b> de quem usa o sistema. Fica em <b>Cadastros → Acessos</b> e só é '
          'visível para o Administrador. A lista mostra, para cada usuário: se está ativo, nome, e-mail, '
          'data de cadastro, perfil, perfil secundário, setor e se <b>controla caixa</b>.'),
    ('img', 'c08b-acessos-lista.png', 'Cadastros → Acessos: lista de usuários da clínica (e-mails ocultados neste manual).'),

    ('h2', 'Criando um novo acesso'),
    ('p', 'Clique em <b>Novo</b> e informe o <b>CPF</b> da pessoa:'),
    ('img', 'c09b-acesso-novo.png', 'Novo Acesso: o primeiro passo é pesquisar pelo CPF.'),
    ('tabelagen', ['Situação', 'O que o sistema faz'], [
        ['A pessoa já tem usuário no ClinSis', 'Pergunta "Deseja permitir acesso a <nome>?". Escolha o <b>Perfil</b> (Atendente ou Profissional) e o <b>Setor</b> e confirme em "Sim, Permitir acesso". O login existente passa a valer também para esta clínica.'],
        ['A pessoa ainda não tem usuário', 'Abre o formulário de criação: <b>Login</b>, <b>E-mail</b>, <b>Nome</b>, <b>Perfil</b> (Atendente ou Profissional) e <b>Setor</b>. Ao salvar, o usuário é criado com a senha padrão do sistema.'],
    ], [5, 12.5]),
    ('aviso', 'O perfil <b>Administrador</b> não é escolhido na criação; ele é definido depois, pela opção Editar do usuário.'),

    ('h2', 'Gerenciando um acesso existente'),
    ('p', 'Na coluna de ações (botão de engrenagem) de cada usuário há:'),
    ('img', 'c10-acesso-menu.png', 'Menu de ações do usuário: Editar, Desativar, Permissões, bloquear dias e Resetar para senha padrão.'),
    ('tabelagen', ['Opção', 'Para que serve'], [
        ['Editar', 'Altera <b>Perfil</b>, <b>Perfil Secundário</b>, <b>Setor</b> e liga/desliga <b>Controla Caixa</b> (exige caixa aberto para o usuário lançar baixas).'],
        ['Desativar / Ativar', 'Bloqueia ou libera o acesso do usuário à clínica, sem apagar o histórico.'],
        ['Permissões', 'Permissões extras por usuário. Hoje existe "Permite gerenciar acessos", que libera a tela de Acessos para quem não é administrador.'],
        ['bloquear dias', 'Define em quais dias da semana o usuário pode entrar (marque só os dias permitidos).'],
        ['Resetar para senha padrão', 'Devolve a senha ao padrão do sistema, útil quando o usuário esquece a própria.'],
        ['Log de acessos (botão no topo)', 'Histórico de quando cada usuário entrou no sistema.'],
    ], [4.2, 13.3]),
    ('img', 'c11-acesso-editar.png', 'Editar: perfil, perfil secundário, setor e a chave "Controla Caixa".'),
    ('img', 'c12-acesso-permissoes.png', 'Permissões do usuário: adicionar permissões extras.'),
    ('img', 'c13-acesso-bloqueio-dias.png', 'Bloqueio de dias: marque os dias da semana em que o usuário pode acessar.'),

    # ------------------------------------------------------------------ 5
    ('h1', '5. Criação da agenda'),
    ('p', 'A agenda do ClinSis é <b>mensal</b>: existe uma agenda para cada mês/ano. Ela fica em <b>Agenda</b> '
          'no menu. A lista mostra todas as agendas criadas, da mais recente para a mais antiga, e cada uma '
          'tem os botões abaixo.'),
    ('img', 'b00-agenda-lista.png', 'Menu Agenda: lista de agendas por Ano/Mês, com os botões de cada uma.'),
    ('tabelagen', ['Botão', 'Função'], [
        ['Relatório', 'Resumo do mês: quantidade de agendamentos, pacientes, sessões, presentes, ausentes e desmarcações.'],
        ['Prof. horários', 'Define os horários de cada profissional naquele mês.'],
        ['Ver Agenda', 'Abre a grade de agendamento (onde os pacientes são vinculados e as sessões marcadas).'],
        ['Divergência Sessões', 'Lista os agendamentos cuja quantidade de <b>Sessões</b> difere das <b>Sessões Esperadas</b> do mês (quantas vezes o dia da semana acontece) e permite <b>Ajustar</b>, um a um ou em lote.'],
        ['Lixeira (vermelho)', 'Remove a agenda do mês.'],
        ['Remoção Rápida de Pacientes (link no topo)', 'Atalho para remover pacientes da agenda em lote.'],
    ], [5, 12.5]),

    ('h2', 'Passo a passo: criar a agenda do mês'),
    ('p', '1. Clique em <b>Novo</b>. 2. Escolha o <b>Mês</b> e o <b>Ano</b>. 3. Se quiser aproveitar o mês '
          'anterior, marque <b>Copiar agenda anterior</b> e escolha qual agenda será clonada. '
          '4. Clique em <b>Salvar</b>.'),
    ('img', 'b01-nova-agenda.png', 'Nova Agenda: mês, ano e a opção de copiar uma agenda anterior.'),
    ('aviso', 'Se a agenda escolhida não for a do mês corrente, o sistema pede uma confirmação extra. '
              'E só pode existir <b>uma agenda por mês/ano</b>: tentar criar de novo mostra a mensagem '
              '"Já existe uma agenda criada para (mês/ano)".'),

    ('h2', 'Criar do zero ou copiar a anterior?'),
    ('tabelagen', ['Opção', 'O que acontece'], [
        ['Sem copiar', 'A agenda nasce vazia: é preciso definir os horários dos profissionais e vincular os pacientes.'],
        ['Copiar agenda anterior', 'O sistema copia para o novo mês os <b>horários dos profissionais</b> e os <b>pacientes já vinculados</b> a eles. Os status das sessões (presente/ausente…) e as datas das sessões são <b>zerados</b>, pois o mês novo ainda não aconteceu.'],
    ], [4.2, 13.3]),
    ('aviso', 'Copiar a agenda anterior é o caminho mais rápido na rotina: os pacientes fixos continuam nos '
              'mesmos dias e horários, e você só ajusta as exceções.'),

    # ------------------------------------------------------------------ 6
    ('h1', '6. Parametrização de horários'),
    ('p', 'Há dois níveis de horários, e é importante não confundir:'),
    ('tabelagen', ['Nível', 'Onde', 'O que define'], [
        ['Horários da clínica', 'Tabelas Aux. → Horários', 'A lista geral de horários que a clínica trabalha (ex.: 07:00, 07:30, 08:00…). É o "cardápio" de horários.'],
        ['Horários do profissional', 'Agenda → Prof. horários', 'Quais desses horários cada profissional atende, em cada dia da semana (ou em datas específicas), naquele mês.'],
    ], [3.8, 4.6, 9.1]),

    ('h2', 'Horários da clínica (Tabelas Aux. → Horários)'),
    ('p', 'Cada horário tem uma <b>Situação</b> (Ativo/Inativo) e um botão para ativar ou desativar. '
          'Só horários <b>ativos</b> aparecem na hora de montar a agenda do profissional. Há duas formas '
          'de cadastrar:'),
    ('img', 'b02-horarios.png', 'Configuração de Horários: lista com situação, botão Ativar/Desativar, campo para novo horário e "Gerar Horários".'),
    ('tabelagen', ['Forma', 'Como usar'], [
        ['Novo (um a um)', 'Digite o horário no formato 00:00 (ex.: 08:30) e clique em <b>Novo</b>.'],
        ['Gerar Horários (em lote)', 'Informe <b>Horário Início</b>, <b>Horário Fim</b> e o <b>Intervalo</b> (de 5 em 5 até de 50 em 50 minutos). O sistema cria todos os horários do período.'],
    ], [5, 12.5]),
    ('img', 'b03-gerar-horarios.png', 'Gerar Horários: exemplo de 08:00 às 18:00 de 30 em 30 minutos.'),

    ('h2', 'Horários do profissional (Agenda → Prof. horários)'),
    ('p', 'Depois de criada a agenda do mês, clique em <b>Prof. horários</b> nela. A tela "Profissional Agenda" '
          'permite montar a grade de cada profissional.'),
    ('p', '1. Escolha o profissional (pela lista ou em "buscar profissional"). '
          '2. Se a clínica trabalha com os dois formatos, escolha o <b>Formato</b>: <b>SEMANAL</b> (um dia da semana, que se repete o mês inteiro) '
          'ou <b>DATA</b> (um dia específico). '
          '3. Marque o <b>Dia</b> (ou a <b>Data</b>). '
          '4. Marque os <b>Horários</b> desejados (ou "Marcar todos"). '
          '5. Clique em <b>Incluir</b>. Repita para os outros dias.'),
    ('img', 'b05-prof-horarios-selecionado.png', 'Prof. horários: escolha do profissional, formato, dia, marcação dos horários e a tabela dos horários já incluídos.'),
    ('tabelagen', ['Recurso', 'Para que serve'], [
        ['Manter Marcação', 'Ao incluir, mantém os horários marcados na tela, para repetir a mesma seleção em outro dia sem remarcar tudo.'],
        ['Transferir horários/agenda para outro profissional', 'Passa a agenda deste profissional (horários e pacientes) para outro. Útil quando um profissional sai.'],
        ['Clonar horários para outro profissional', 'Copia os horários deste profissional para outro, sem tirar do original.'],
        ['Remover Todos os Horários deste profissional', 'Limpa toda a grade do profissional no mês.'],
        ['Remover (caixas + lixeira)', 'Marque as linhas da tabela e use a lixeira para remover horários específicos.'],
    ], [6.4, 11.1]),
    ('aviso', 'Sem horários de profissional definidos, a grade de agendamento fica vazia: não há onde vincular pacientes.'),

    # ------------------------------------------------------------------ 7
    ('h1', '7. Agendamento de pacientes'),
    ('p', 'Com a agenda criada e os horários dos profissionais definidos, o agendamento é feito em '
          '<b>Agenda → Ver Agenda</b> (ou pelo botão Agendamento dentro de Prof. horários). A tela é uma '
          'grade: <b>cada linha é um horário de um profissional</b> em um dia da semana ou data.'),
    ('img', 'd01-agendamento.png', 'Grade de agendamento: horários dos profissionais, pacientes vinculados, plano, sessões e status de cada sessão.'),
    ('p', 'As linhas em <b>branco</b> com o botão verde (+) são <b>horários vagos</b>. As linhas com o botão '
          'azul de engrenagem já têm paciente. A cor da linha pode indicar a situação da guia de faturamento. '
          'Use "Somente vagos" para listar apenas os horários livres.'),

    ('h2', 'Como agendar um paciente'),
    ('p', '1. Na linha vaga, clique no botão verde <b>(+)</b>. '
          '2. Em "Vincular Paciente" pesquise pelo nome e selecione o paciente. '
          '3. Preencha o formulário e clique em <b>Salvar</b>.'),
    ('img', 'd04-vincular-busca.png', 'Vincular Paciente: busca do paciente cadastrado (nome, data de nascimento, mãe, pai e município).'),
    ('img', 'd06-agendar-form-preenchido.png', 'Formulário do agendamento preenchido: dados do horário, do paciente e as informações do atendimento.'),
    ('tabelagen', ['Campo', 'O que informar'], [
        ['Atendimento Particular? *', '<b>Sim</b> = paciente particular. <b>Não</b> = atendido por convênio; nesse caso aparecem também <b>Plano</b> (operadora), <b>Cooparticipativo</b> e <b>Nº Doc Faturamento</b> (guia).'],
        ['Sessões *', 'Quantas sessões o paciente tem naquele horário no mês (a agenda tem até 5 colunas de sessão: Sessão 1 a Sessão 5, uma por ocorrência do dia da semana no mês).'],
        ['Forma Atendimento *', 'Presencial ou Online.'],
        ['Especialidade *', 'A especialidade do atendimento (ex.: FONO, PSICO).'],
        ['Tipo Marcação *', 'NI (não informado), Avaliação ou Consulta/Sessão.'],
        ['Método * e Programa *', 'Método terapêutico e programa/agrupamento definidos nas tabelas auxiliares da clínica.'],
        ['Data Entrada', 'Data em que o paciente começou nesse horário.'],
        ['Observação', 'Texto livre. Uma linha com observação mostra um ícone de comentário para leitura rápida.'],
    ], [4.6, 12.9]),
    ('aviso', 'Os campos marcados com * são obrigatórios. Para vincular mais de um paciente ao mesmo '
              'horário (por exemplo, atendimento em grupo), use <b>Adicionar mais</b> na linha.'),

    ('h2', 'Ações sobre um agendamento existente'),
    ('p', 'O botão de engrenagem de cada linha abre o menu de ações:'),
    ('img', 'd02-agendamento-menu-linha.png', 'Menu de ações da linha: Editar, Sessão, Adicionar mais, Desmarcar, Entrada, Saída, Trocar Profissional e Horários Pac.'),
    ('tabelagen', ['Ação', 'Para que serve'], [
        ['Editar', 'Corrige os dados do agendamento (sessões, plano, especialidade, observação…).'],
        ['Sessão', 'Marca o resultado de uma sessão (ex.: Presente, Ausente) no dia em que ela acontece. Abre a janela "Marcar Sessão" para escolher qual sessão (1 a 5).'],
        ['Adicionar mais', 'Vincula outro paciente ao mesmo horário do profissional.'],
        ['Desmarcar', 'Remove o paciente daquele horário (pede confirmação antes).'],
        ['Entrada / Saída', 'Registra a entrada ou a saída do paciente no tratamento (tipo, data e motivo).'],
        ['Trocar Profissional', 'Passa o paciente para outro profissional.'],
        ['Horários Pac.', 'Gera o PDF com todos os horários do paciente no mês (veja a seção de impressões).'],
    ], [4, 13.5]),
    ('img', 'd07-sessao.png', 'Marcar Sessão: identifica profissional, paciente, dia e hora e pede a sessão a marcar.'),
    ('aviso', 'Também é possível marcar a sessão com <b>duplo clique</b> na célula da coluna Sessão 1…5 da linha do paciente.'),

    ('h2', 'Ferramentas da tela de agendamento'),
    ('tabelagen', ['Botão', 'Função'], [
        ['Filtros', 'Filtra a grade por data, paciente, dias, profissionais, quantidade de sessões, método, cooparticipativo, particular e pelo status de cada sessão.'],
        ['Relatórios', 'Abre a janela das impressões do dia (veja a seção 8).'],
        ['Exportar', 'Exporta a agenda para arquivo CSV (planilha): com os filtros aplicados ou a agenda inteira.'],
        ['Pesquisa rápida', 'Encontra rapidamente um profissional ou paciente na agenda.'],
        ['Colunas', 'Escolhe quais colunas ficam visíveis na grade; a escolha fica salva para o usuário.'],
        ['Somente vagos', 'Mostra só os horários sem paciente.'],
        ['Anterior / Próxima agenda', 'Setas para navegar entre os meses.'],
    ], [4, 13.5]),
    ('img', 'd08-filtros.png', 'Filtros da grade de agendamento.'),

    # ------------------------------------------------------------------ 8
    ('h1', '8. Impressões da agenda e seus objetivos'),
    ('p', 'O ClinSis oferece impressões/relatórios da agenda para situações diferentes do dia a dia. '
          'A tabela resume qual usar em cada caso:'),
    ('tabelagen', ['Impressão', 'Onde encontrar', 'Objetivo'], [
        ['Atendimento Diário (PDF)', 'Ver Agenda → Relatórios', 'Lista do dia, por profissional, com horário, paciente e campos de assinatura do responsável e convênio. Serve para a recepção conferir e colher assinaturas.'],
        ['Marcação - Presença/Ausência (PDF)', 'Ver Agenda → Relatórios', 'Lista de presença do dia: sessão, profissional, paciente, mãe e o status marcado. Serve para conferência de quem veio e quem faltou.'],
        ['Marcação sessão dia (tela)', 'Ver Agenda → Relatórios', 'Mostra na tela as sessões marcadas naquele dia: quem marcou, status, data da sessão e totais por status. Serve para auditar as marcações.'],
        ['Horários do paciente (PDF)', 'Ver Agenda → engrenagem da linha → Horários Pac.', 'Folha do paciente com os dias, horários e profissionais do mês. Serve para entregar ao paciente ou responsável.'],
        ['Exportar agenda (CSV)', 'Ver Agenda → Exportar', 'Leva a agenda para planilha, com filtros ou completa, para análises próprias.'],
        ['Relatório da Agenda (tela)', 'Agenda → Relatório (na linha do mês)', 'Resumo do mês: agendamentos, pacientes, sessões, presentes, ausentes e desmarcações, por profissional ou todos.'],
        ['Relatórios de Agenda (menu Relatórios)', 'Relatórios → Agenda', 'Marcação Sessão Dia, Sessões Faturamento, Qtd. Marcação Agenda, Presença Diária e Atendimentos Sequenciais, com filtros próprios.'],
    ], [4.4, 4.6, 8.5]),

    ('h2', 'Relatórios do dia (Ver Agenda → Relatórios)'),
    ('p', 'Escolha a <b>data</b> (dentro do mês da agenda) e o <b>tipo</b>: "Atendimento Diário", '
          '"Marcação - Presença/Ausência" ou "Marcação sessão dia". Os dois primeiros baixam um PDF; o '
          'terceiro abre na tela (botão <b>Visualizar</b>).'),
    ('img', 'd09b-relatorios-presenca.png', 'Janela Relatórios: data da agenda e tipo de relatório.'),

    ('h2', 'Atendimento Diário'),
    ('p', 'Mostra o dia da semana escolhido (ex.: QUARTA-FEIRA 23/09/2026) e, para cada profissional, os '
          'pacientes por horário, com colunas para <b>assinatura do responsável</b> e <b>convênio</b> e uma '
          'linha final <b>ASSINATURA DO PROFISSIONAL</b>. É a folha de presença impressa da recepção.'),
    ('img', 'e-atendimento-diario.png', 'PDF do Atendimento Diário.'),

    ('h2', 'Marcação - Presença/Ausência'),
    ('p', 'Lista as sessões marcadas na data escolhida, com sessão, profissional, paciente, mãe e o status '
          '(PRESENTE, AUSENTE…).'),
    ('img', 'e-presenca-ausencia.png', 'PDF da Lista de presença do dia.'),

    ('h2', 'Marcação sessão dia (na tela)'),
    ('p', 'Mostra data/hora em que cada marcação foi feita, profissional, paciente, <b>usuário</b> que marcou, '
          'status e data da sessão, com o total por status no rodapé. Ajuda a saber quem registrou o quê.'),
    ('img', 'e03-marcacao-sessao-dia.png', 'Marcação do mês/dia: usuário responsável, status e totais.'),

    ('h2', 'Horários do paciente'),
    ('p', 'Impressão individual: mês/ano, clínica, nome do paciente, usuário que gerou e a lista de dias da '
          'semana com horário e profissional. É o "comprovante" dos dias e horários do paciente.'),
    ('img', 'e-horarios-paciente.png', 'PDF Horários do paciente (trecho superior).'),

    ('h2', 'Relatório da Agenda e relatórios no menu Relatórios'),
    ('img', 'e05-relatorio-agenda.png', 'Agenda → Relatório: cartões-resumo do mês, com filtro por profissional.'),
    ('img', 'f01-relatorios.png', 'Menu Relatórios: o bloco "Agenda" reúne os relatórios de acompanhamento.'),
    ('img', 'g01-presenca-diaria.png', 'Exemplo: Relatório - Presença Diária, com filtros de usuário, profissional, paciente, data, particular e método.'),
    ('aviso', 'A Lista simples de pacientes do dia (link na tela Agenda) existe para o perfil <b>Profissional</b> '
              'e mostra somente os pacientes do próprio profissional naquele dia.'),

    # ------------------------------------------------------------------ 9
    ('h1', '9. Resumo: da implantação ao primeiro agendamento'),
    ('tabelagen', ['Passo', 'Ação', 'Onde'], [
        ['1', 'Conferir os dados da clínica', 'Cadastros → Clínica'],
        ['2', 'Cadastrar setores', 'Cadastros → Setores'],
        ['3', 'Cadastrar especialidades e operadoras', 'Tabelas Aux. → Especialidade; Cadastros → Operadora'],
        ['4', 'Cadastrar profissionais e pacientes', 'Cadastros → Profissional / Paciente'],
        ['5', 'Cadastrar os horários da clínica', 'Tabelas Aux. → Horários (Gerar Horários)'],
        ['6', 'Criar os acessos da equipe', 'Cadastros → Acessos'],
        ['7', 'Criar a agenda do mês', 'Agenda → Novo'],
        ['8', 'Definir os horários de cada profissional', 'Agenda → Prof. horários'],
        ['9', 'Vincular os pacientes aos horários', 'Agenda → Ver Agenda → (+)'],
        ['10', 'Marcar presença/ausência a cada sessão', 'Ver Agenda → engrenagem → Sessão'],
        ['11', 'Imprimir/conferir', 'Ver Agenda → Relatórios; Relatórios → Agenda'],
    ], [1.6, 8.2, 7.7]),
    ('aviso', 'A partir do segundo mês, o caminho é bem mais curto: <b>criar a agenda copiando a anterior</b> '
              '(passo 7 com "Copiar agenda anterior") já traz horários e pacientes. Só é preciso ajustar as exceções.'),
]

blocos_tecnico = blocos + [
    ('pagebreak',),
    ('h1', 'Anexo técnico (somente versão completa)'),
    ('tabelagen', ['Assunto', 'Detalhe técnico'], [
        ['Cópia da agenda', 'Ao criar com "Copiar agenda anterior", a API chama a stored procedure <b>AgendaAbertura</b>, que cria a linha em <b>Agenda</b> (com IdAgendaCopy apontando para a origem), copia <b>AgendaProfissionalDia</b> (horários) e <b>AgendaProfissionalDiaPac</b> (pacientes vinculados) e, nesta última, zera IDSTATUS_S1..S5 (-1) e DATAS1..S5 (nulas).'],
        ['Modo de cópia', 'O campo <b>Clinica.CopiaAgenda</b> define o que é copiado: T = tudo, S = só horários semanais (Data = 1900-01-01), D = só horários por data específica.'],
        ['Unicidade', 'A API impede duas agendas no mesmo mês/ano da clínica (mensagem "Já existe uma agenda criada para...").'],
        ['Horários da clínica', 'Tabela de horários ativos consultada na montagem da grade de Prof. horários (tela Tabelas Aux. → Horários, rota /aux/horarios).'],
        ['Perfis (IdPerfil)', 'Profissional = 10, Atendente = 20, Administrador = 50. Não é permitido 50 + 20 (nem 20 + 50) como principal + secundário.'],
        ['Rotas do front', '/agenda, /agenda/profissional, /agendamento, /aux/horarios, /acessos, /acessos/permissoes, /acessos/bloqueiodias, /acessos/logs, /relatorio/agenda, /relatorios.'],
        ['Impressões', 'Atendimento Diário: RelatorioController.PdfAgendaAtendimentoDia; Presença/Ausência: pdf/agenda/presentesAusentes (PresentesAusentesPDF); Horários do paciente: AgendaPacienteHorariosPDF.'],
    ], [4, 13.5]),
]

render_pdf(blocos_tecnico, os.path.join(ENTREGA, 'Documentacao_Manual_Base_ClinSis.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocos, os.path.join(ENTREGA, 'Documentacao_Manual_Base_ClinSis_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocos_tecnico, os.path.join(ENTREGA, 'Documentacao_Manual_Base_ClinSis.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
