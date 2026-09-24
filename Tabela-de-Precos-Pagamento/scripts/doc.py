# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = "1.0"
DATA = "22/09/2026"
TITULO = "Tabela de Valores para Pagamento"
SUBTITULO = "Cadastro, valores por Especialidade/Profissional e reajuste de preço em massa"
VIDEO_NOME = "https://youtu.be/B5Jlz0kweIM"
INTRO = ('A <b>Tabela de Valores para Pagamento</b> (Tabelas Aux. → Tab. Pagamento) define quanto a '
         'clínica paga a cada profissional por sessão atendida. É essa tabela que o relatório de '
         '<b>Pagamento de Profissionais</b> usa para calcular o valor a pagar todo mês. Este manual '
         'cobre o cadastro completo e a ferramenta de <b>reajuste de preço em massa</b>, que aplica um '
         'percentual a vários valores de uma vez, sem precisar editar linha por linha.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'O conceito de "Tabela de Valores"'),
    ('p', 'Cada linha da lista principal é uma <b>Tabela de Valores</b>, com uma Descrição e um status Ativo/Inativo. O botão de engrenagem '
          '("Gerenciar") abre a tabela para cadastrar os valores propriamente ditos.'),
    ('img', '00-lista-vigencias.png', 'Lista de tabelas de pagamento cadastradas, com o status Ativo de cada uma.'),
    ('aviso', 'O cálculo do Pagamento de Profissionais sempre usa a tabela marcada como '
              '<b>Ativo = Sim</b> — e o sistema não garante que exista só uma. <b>Nunca deixe duas '
              'tabelas ativas ao mesmo tempo</b>: como não há uma ordem confiável entre elas, o '
              'resultado do cálculo fica imprevisível.'),

    ('h2', 'Dentro de "Gerenciar": três abas'),
    ('tabela', [
        ('Agenda', 'Vincula quais meses/anos de agenda usam esta tabela de valores (não define preço, só habilita o mês para entrar no cálculo).', 'AgendaVigenciaProfPagto'),
        ('Especialidades', 'Valor padrão por Especialidade × Tipo de Marcação, aplicado a todo profissional que não tiver um valor específico.', 'ConfigEspecPagto'),
        ('Profissionais', 'Valor específico por Profissional × Especialidade × Tipo de Marcação, que sobrepõe o valor padrão da aba Especialidades só para aquele profissional.', 'ConfigProfissionalEspecialidadePagto'),
    ]),
    ('img', '02-aba-especialidades.png', 'Aba "Especialidades": valor padrão (Valor e Valor Convênio) por Especialidade e Tipo de Marcação.'),
    ('img', '08-modal-valores-profissional.png',
     'Aba "Profissionais": ao clicar no ícone "$" de um profissional, abre a grade de valores específicos dele — sobrepõe o valor padrão só para esse profissional.'),

    ('h2', 'Reajuste de preço em massa'),
    ('p', 'O card <b>"Manutenção rápida de preços"</b> aparece tanto na aba Especialidades (reajusta '
          '<b>toda a tabela</b>) quanto dentro do modal de valores de um profissional (reajusta '
          '<b>só aquele profissional</b>). O funcionamento é o mesmo nos dois casos.'),
    ('img', '03-reajuste-formulario-aberto.png', 'Botão "Reajustar preços" expande o formulário: percentual e quais campos reajustar (Valor e/ou Valor Convênio).'),
    ('p', '<b>Passo a passo:</b>'),
    ('tabela', [
        ('1. Percentual de reajuste', 'Número positivo (aumento) ou negativo (desconto). Limite: maior que -100% e até 1000%.', 'ReajustePrecoController.cs'),
        ('2. Campos a reajustar', 'Marque "Valor", "Valor convênio", ou os dois.', 'reajuste-preco.component.html'),
        ('3. Calcular prévia', 'Mostra uma tabela comparando o valor atual com o valor novo, linha por linha — sem gravar nada ainda.', 'ReajustePreco/pagamento/simular'),
        ('4. Confirmar reajuste', 'Só depois de conferir a prévia, grava de fato. Pede uma confirmação extra ("Confirma o reajuste de X valor(es) em Y registro(s)?").', 'ReajustePreco/pagamento/confirmar'),
    ]),
    ('img', '04-reajuste-previa.png',
     'Prévia de um reajuste de 10%: mostra valor atual e valor novo (em verde) de cada linha, sem alterar nada até a confirmação.'),
    ('img', '05-reajuste-modal-confirmar.png', 'Confirmação final antes de gravar as alterações.'),
    ('img', '06-reajuste-confirmado.png', '"9 valor(es) reajustado(s) com sucesso" — os valores já aparecem atualizados na grade.'),
    ('img', '09-reajuste-profissional-formulario.png',
     'O mesmo recurso, dentro do modal de um profissional específico: reajusta só os valores daquele profissional, sem afetar a tabela padrão.'),
    ('aviso', 'A simulação (prévia) <b>não grava nada</b> — só depois de clicar em "Confirmar reajuste" '
              'os valores mudam de fato. Se algum valor for alterado por outra pessoa entre a prévia e a '
              'confirmação, o sistema recusa e pede para gerar uma nova prévia (evita reajustar em cima '
              'de dados já desatualizados). Linhas com Valor Convênio vazio não são alteradas, mesmo com '
              'o campo marcado. Toda confirmação de reajuste fica registrada no log do sistema.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Tabela_Preco_Pagamento.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Tabela_Preco_Pagamento_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Tabela_Preco_Pagamento.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
