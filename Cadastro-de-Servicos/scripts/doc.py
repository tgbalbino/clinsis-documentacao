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
TITULO = "Cadastro de Serviços"
SUBTITULO = "Para que serve e onde é utilizado (Tabelas Aux. → Serviços)"
VIDEO_NOME = "https://youtu.be/uotROr-rj6s"
INTRO = ('Um <b>Serviço</b> é um item simples de "nome + valor" — como um item de tabela de valores — '
         'usado como base para montar os itens de um <b>Contrato</b>. Este manual explica o cadastro e, '
         'principalmente, onde ele entra em uso dentro do sistema.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'O que é um Serviço'),
    ('p', 'Pense num Serviço como um <b>item de catálogo</b>: um nome ("Sessão de Fisioterapia", '
          '"Avaliação Inicial", "Pacote 10 sessões") e um valor sugerido. Ao montar um Contrato, em vez '
          'de digitar manualmente a descrição e o valor de cada item, o usuário busca um Serviço já '
          'cadastrado e usa isso como ponto de partida.'),
    ('p', 'O cadastro é bem enxuto: só <b>Descrição</b> e <b>Preço</b>. Não existe ativo/inativo, '
          'categoria, nem vínculo com convênio — e não há como excluir um Serviço já cadastrado pela '
          'tela, ele permanece disponível permanentemente na lista.'),
    ('img', '00-lista-servicos.png', 'Lista de Serviços (Tabelas Aux. → Serviços), com Nome e Preço de cada um.'),
    ('img', '01-cadastro-servico-vazio.png', 'Tela de cadastro: só dois campos, Serviço (nome) e Preço.'),

    ('h2', 'Onde é utilizado: exclusivamente no módulo Contrato'),
    ('aviso', 'Apesar do nome "Serviço" sugerir algo amplo (faturamento, convênio, guias), na prática '
              'ele é usado em <b>um único lugar do sistema</b>: a aba "Serviços" dentro do cadastro de '
              'Contrato. Guia de Faturamento, Cobrança de Paciente e Tabela de Valores de convênio usam '
              'outro conceito (Especialidade), sem nenhuma relação com este cadastro.'),
    ('p', 'Dentro de um Contrato, cada linha de serviço contratado (Serviço + Quantidade de sessões + '
          'Valor da sessão) fica registrada, e o <b>Valor Total do Contrato é a soma de todas essas '
          'linhas</b> — calculado automaticamente pelo sistema, sem que o usuário precise somar nada '
          'manualmente.'),
    ('img', '02-contrato-aba-servicos.png',
     'Aba "Serviços" dentro do cadastro de Contrato: lista os itens já adicionados (Serviço, Qtd, Valor Sessão, Valor Total) e o botão "Novo".'),
    ('img', '04-modal-buscar-servico-resultado.png',
     'Ao clicar em "Novo", abre a busca de Serviço: mostra nome e preço de cada um cadastrado, com um botão verde para selecionar.'),
    ('img', '06-contrato-servico-qtd-preenchida.png',
     'Depois de escolher o Serviço, o valor sugerido já vem preenchido; falta só informar a Quantidade de sessões. O Valor Total é calculado automaticamente (Quantidade × Valor).'),
    ('img', '07-contrato-servico-adicionado.png',
     'Serviço adicionado: a linha aparece na tabela do contrato, e o "Total Serviços" do contrato é atualizado.'),

    ('h2', 'Outros pontos onde o Serviço aparece'),
    ('tabela', [
        ('Cálculo do Valor Total do Contrato', 'A soma de todas as linhas de serviço do contrato define o valor total dele, usado depois para comparar com os pagamentos/acertos lançados ("Falta Acertar").', 'ContratoServicoRepository.cs'),
        ('Renovação de Contrato', 'Ao renovar um contrato, o sistema copia automaticamente os mesmos Serviços/quantidades/valores para o contrato novo. Se o contrato antigo não tiver nenhum serviço, a renovação é bloqueada.', 'ContratoRenovacaoService.cs'),
        ('Impressão do Contrato', 'No layout de impressão do contrato (Tabelas Aux. → Layout Contrato), existe um placeholder "TabelaServicos" que renderiza a lista de serviços contratados no PDF/documento impresso.', 'contrato-laiout-config.component.ts'),
    ]),
    ('aviso', 'Um Serviço só pode ser adicionado, alterado ou removido de um contrato enquanto ele '
              'estiver <b>ativo e ainda não assinado</b> (nem com uma solicitação de assinatura '
              'eletrônica em andamento) — depois de assinado, o contrato fica travado.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Servicos.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Servicos_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Cadastro_Servicos.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
