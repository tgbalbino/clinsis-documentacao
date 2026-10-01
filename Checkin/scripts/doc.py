# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '2.0'
DATA = '30/09/2026'
TITULO = 'Checkin de Paciente'
SUBTITULO = 'Registrar a chegada do paciente e, se houver cobrança, já receber na hora'
VIDEO_NOME = "https://youtu.be/MKW8mdKnfTg"
INTRO = ('O <b>Checkin</b> registra a chegada do paciente na clínica no dia da consulta ou sessão. Quando o paciente tem um horário '
         '<b>agendado para hoje</b> que é cobrado na hora (por exemplo, atendimento particular), o Checkin também mostra a cobrança e permite '
         'lançar o pagamento: nesse caso, o sistema gera automaticamente uma <b>Conta a Receber já paga</b>. Para o pagamento funcionar, a clínica '
         'precisa ter configurado, em Parâmetros, o Plano de Conta, o Centro de Custo e a Conta Financeira do Checkin, e o usuário precisa ter o '
         '<b>caixa aberto</b>.')
RODAPE = ('Documento gerado por teste manual guiado em ambiente local de homologação, clínica de testes "Homologação" (Clínica 1), '
          'usuário administrador de teste. O agendamento e o pagamento usados no exemplo são fictícios.')

blocks = [
    ('h2', 'Tela inicial'),
    ('p', 'Na <b>Home</b>, clique no cartão <b>Check-in</b> (perfil administrador; endereço <b>/paciente/checkin</b>). A tela mostra os check-ins já feitos na data escolhida, com Paciente, '
          'Data/Hora do check-in, Horário da Agenda e quem atendeu. O botão <b>Realizar Check-In</b> abre o lançamento de um novo.'),
    ('img', '00-lista-inicial.png', 'Paciente Check-In: check-ins do dia e o botão Realizar Check-In.'),

    ('h2', 'Antes de usar'),
    ('tabelagen', ['O que precisa existir', 'Onde configurar / como conferir'], [
        ['Parâmetros do Checkin', 'Em <b>Tabelas Aux. → Parâmetros</b>, configure <b>IdPlanoContaCheckin</b> (Plano de Conta), <b>IdCentroCustoCheckin</b> (Centro de Custo) e <b>IdContaFinanceiraCheckin</b> (Conta Financeira que recebe o valor). Cada um deve apontar para um cadastro que exista e esteja ativo; se o cadastro for excluído depois, o Checkin com pagamento passa a falhar até o parâmetro ser corrigido. A mensagem de erro diz qual dos três está errado.'],
        ['Caixa aberto', 'Se o usuário controla caixa, é preciso <b>abrir o caixa</b> antes (menu Caixa). Sem isso, o sistema avisa: "Nenhum caixa aberto para o usuário. Abra o caixa antes de registrar o recebimento."'],
        ['Plano Próprio', 'O Checkin trabalha com pacientes de <b>Plano Próprio</b> (por exemplo, operadora PROPRIO). Se nem o cadastro do paciente nem o agendamento forem de plano próprio, o sistema avisa e não confirma. Se só o agendamento for, ele pergunta se deseja atualizar o cadastro do paciente.'],
        ['Horário de hoje e valor', 'O paciente precisa ter um horário marcado <b>hoje</b>, com uma especialidade que tenha valor em <b>Config → Cobrança</b>.'],
    ], [4.2, 13.3]),

    ('h2', 'Identificando o paciente'),
    ('p', 'O campo principal lê o <b>código de barras</b> da carteirinha ou pulseira do paciente e confirma o paciente assim que o código é lido. '
          'Sem o código à mão, use <b>Pesquisa Manual</b>: digite o nome ou CPF, pressione Enter e clique em selecionar na linha do paciente.'),
    ('img', '01-modal-codigo-barras.png', 'Check-In: campo para leitura do código de barras, ou os botões Ler Código e Pesquisa Manual.'),
    ('img', '02-pesquisa-resultado.png', 'Resultado da Pesquisa Manual por nome.'),

    ('h2', 'Quando o paciente tem um horário cobrável hoje'),
    ('p', 'Identificado o paciente, o sistema busca os horários de hoje dele e mostra, para cada um, o dia, a data, a hora, o profissional, a especialidade, '
          'o <b>Valor</b> e o <b>Valor Social</b>. Marque a caixa do horário que está sendo confirmado; pode marcar mais de um.'),
    ('img', '03-paciente-com-agenda-hoje.png', 'Horário de hoje do paciente (20:30, especialidade TO), com Valor e Valor Social.'),
    ('p', 'Depois de marcar, escolha o <b>Tipo de preço</b> (Valor normal ou Valor social). O campo <b>Valor Receber</b> mostra o total a cobrar.'),
    ('img', '04-horarios-marcados-com-valor.png', 'Horário marcado, Tipo de preço e Valor Receber (R$ 36,56) preenchidos, com a área Adicionar pagamento.'),
    ('aviso', 'Se aparecer "* Verificar pendência de pagamento" em vermelho, o paciente tem valor em aberto em Contas a Receber. Confira antes de finalizar.'),

    ('h2', 'Lançando o pagamento'),
    ('p', 'Em <b>Adicionar pagamento</b>, escolha a forma (Dinheiro, Pix, Cheque, Car. Débito ou Car. Crédito), informe o valor, ou use o botão da calculadora '
          'para preencher o <b>valor restante</b>, e clique em <b>Adicionar</b>. É possível combinar mais de uma forma de pagamento até o Restante chegar a zero.'),
    ('img', '05-pagamento-preenchido.png', 'Forma Dinheiro com o valor da sessão preenchido, antes de clicar em Adicionar.'),
    ('img', '06-pagamento-adicionado.png', 'Depois de Adicionar: o pagamento aparece na lista, Total pago R$ 36,56 e Restante R$ 0,00.'),
    ('p', 'No <b>Cartão de Crédito</b> aparece o campo de <b>Parcelas</b>, limitado ao máximo de parcelas de recebimento configurado para a clínica; as parcelas seguem para a Conta a Receber.'),
    ('img', '06b-cartao-credito-parcelas.png', 'Car. Crédito: campo de parcelas ao lado da forma de pagamento.'),

    ('h2', 'Confirmando o Check-In'),
    ('p', 'Com o Restante em zero, clique em <b>Confirmar Check-In</b>. O sistema registra a chegada e, como houve pagamento, gera e baixa a Conta a Receber na hora, '
          'lançando o valor na Conta Financeira configurada e no caixa aberto do usuário.'),
    ('img', '07-apos-confirmar-checkin.png', 'Check-in confirmado: aparece na lista com a data/hora, o horário da agenda (20:30:00) e o atendente.'),
    ('img', '08-conta-a-receber-gerada-pelo-checkin.png', 'Contas a Receber: a linha do paciente, R$ 36,56, Plano de Conta "Consulta Particular", Situação "Baixada", gerada e paga automaticamente pelo Checkin.'),
    ('aviso', 'Esta rotina gera Conta a Receber automaticamente: não é preciso lançar nada à mão em Contas a Receber.'),

    ('h2', 'Mensagens que você pode encontrar'),
    ('tabelagen', ['Mensagem', 'Causa', 'O que fazer'], [
        ['Nenhuma marcação existente na agenda para o dia', 'O paciente não tem horário marcado hoje.', 'Confira a data e a agenda. O Checkin confirma presença em algo já agendado; não cria atendimento novo.'],
        ['Existe 1 marcação na agenda para o dia e 1 check-in realizado', 'Todos os horários de hoje já tiveram check-in.', 'Nada a fazer.'],
        ['Selecione ao menos um horário e informe o valor', 'Nenhum horário marcado ou sem valor a receber.', 'Marque o horário e confira o Tipo de preço.'],
        ['Nenhum caixa aberto para o usuário...', 'O usuário controla caixa e ainda não abriu.', 'Abra o caixa e confirme de novo.'],
        ['Paciente não está vinculado a um Plano Próprio...', 'Nem o cadastro nem o agendamento são de plano próprio.', 'Ajuste a operadora do agendamento ou do cadastro do paciente.'],
        ['Erro citando Plano de Conta, Centro de Custo ou Conta Financeira', 'Parâmetro do Checkin vazio ou apontando para cadastro excluído.', 'Corrija em Tabelas Aux. → Parâmetros.'],
    ], [5.4, 5.6, 6.5]),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Checkin.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Checkin_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Checkin.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
