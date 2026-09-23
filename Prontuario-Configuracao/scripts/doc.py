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
DATA = "23/09/2026"
TITULO = "Prontuário — Configuração"
SUBTITULO = "Tipos de prontuário, Alíneas e Textos padrão: o que são, como cadastrar e para que servem"
VIDEO_NOME = "video-prontuario-configuracao-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('Antes de um profissional preencher um prontuário, a clínica precisa definir <b>quais tipos de prontuário existem</b> '
         '(Anamnese, Evolução, Relatório...) e <b>quais campos cada tipo tem</b> (as alíneas). Este manual explica essas duas '
         'configurações, feitas pelo administrador, e os <b>Textos padrão</b>, que cada profissional cria para agilizar o '
         'preenchimento. O uso do dia a dia (criar, preencher, finalizar) e a auditoria estão em manuais próprios.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de homologação, clínica de '
          'testes "Homologação" (Clínica 1), com usuário administrador e usuário profissional de teste. Nenhum dado de '
          'produção foi acessado. Os registros criados para o teste foram excluídos ao final.')

blocks = [
    ('h2', 'Visão geral: o que configurar e quem faz'),
    ('tabelagen', ['Configuração', 'Quem faz', 'Onde'],
     [
         ['Tipo de prontuário', 'Administrador', 'Menu Prontuário → Tipos'],
         ['Alíneas do tipo (os campos)', 'Administrador', 'Menu Prontuário → Alíneas'],
         ['Texto padrão', 'Cada profissional (são pessoais)', 'Menu Prontuário → Textos padrão (área do profissional)'],
     ], [5.0, 5.0, 7.5]),
    ('p', 'A ordem natural é: <b>1)</b> criar o Tipo, <b>2)</b> cadastrar as Alíneas dele, <b>3)</b> cada profissional cria '
          'seus Textos padrão. Só depois o profissional consegue criar e preencher prontuários daquele tipo. '
          'As telas só aparecem se o módulo Prontuário estiver ligado para a clínica.'),

    ('h2', '1. Tipos de prontuário'),
    ('p', 'Um <b>Tipo</b> é uma categoria de documento clínico. Exemplos da clínica de teste: Anamnese, Evolução diária, '
          'Rel. Acompanhamento Mensal, Declaração, Relatório técnico. Acesso: <b>Prontuário → Tipos</b> (perfil administrador).'),
    ('img', '01-tipos.png', 'Lista de tipos da clínica: nome do tipo, se é visível na agenda e as ações (editar, Modelo, excluir).'),
    ('p', '<b>Novo:</b> informe apenas o nome do tipo e clique em Salvar. O tipo nasce sem nenhuma alínea, então ainda não '
          'serve para preencher: o próximo passo é cadastrar as alíneas.'),
    ('img', '02-tipo-novo.png', 'Novo tipo: só o nome é pedido.'),
    ('p', '<b>Editar</b> (botão amarelo): permite ajustar dois campos.'),
    ('tabela', [
        ('Dias', 'Número gravado no tipo e copiado para cada prontuário criado. Hoje nenhuma tela usa esse número, então preenchê-lo não muda o comportamento do sistema.', 'ProntuarioTipo.Dias'),
        ('Visível na agenda para preenchimento dos profissionais?', 'Quando marcado, o tipo aparece na lista de tipos da tela <b>Agenda resumida</b>, permitindo criar o prontuário direto a partir da agenda. Na lista de Tipos aparece como "Sim" ou "Não".', 'ProntuarioTipo.VisivelNaAgenda'),
    ]),
    ('img', '04-tipo-alterar.png', 'Editar tipo: Dias e "Visível na agenda". Ao salvar, a tela mostra "Salvo!" e a lista atualiza a coluna "Visível na agenda".'),
    ('p', '<b>Modelo</b> (botão azul ou verde): serve para anexar ao tipo um arquivo de modelo (por exemplo, um formulário em Word) '
          'que os profissionais podem baixar na tela Prontuário. O botão fica verde quando o tipo já tem modelo. '
          'O arquivo é guardado no armazenamento de arquivos da clínica (S3); nesta demonstração o envio não foi testado, pois o '
          'ambiente de teste não tem esse armazenamento configurado.'),
    ('p', '<b>Excluir</b> (botão vermelho): pede confirmação. <b>Não é possível excluir um tipo que já tenha prontuários</b> — o sistema '
          'avisa "Este tipo está vinculado a prontuário, não pode ser removido". Quando o tipo nunca foi usado, ele é excluído junto '
          'com suas alíneas, textos padrão, modelo e vínculos De-Para.'),
    ('img', '15-tipo-excluir.png', 'Confirmação ao excluir um tipo.'),
    ('aviso', '<b>Correção feita nesta documentação:</b> antes, excluir um tipo deixava suas alíneas "órfãs" no banco. Como o próximo tipo '
              'criado reaproveita o mesmo número interno, ele aparecia já com alíneas que ninguém cadastrou (foi assim que uma alínea '
              '"Descritiva" apareceu num tipo novo durante o teste). Agora a exclusão remove tudo junto. Para limpar registros órfãos '
              'antigos existe o script <b>139_Limpar_Orfaos_De_Prontuario_Tipo_Removido.sql</b>, que precisa ser executado no banco '
              'de cada ambiente.'),

    ('h2', '2. Alíneas'),
    ('p', 'A <b>Alínea</b> é cada campo (ou seção) do prontuário: "Queixa principal", "Conduta", "Resumo do atendimento"... '
          'O profissional preenche uma alínea por vez. Acesso: <b>Prontuário → Alíneas</b> (administrador). A lista mostra as alíneas '
          'de todos os tipos, ou só as do tipo escolhido no filtro do topo.'),
    ('img', '07-alinea-nova.png', 'Nova alínea: escolha o tipo de prontuário, o tipo de campo e digite o nome da alínea.'),
    ('tabelagen', ['Tipo de campo', 'Como o profissional preenche'],
     [
         ['Texto', 'Caixa de texto livre (aceita os Textos padrão).'],
         ['Sim ou Não', 'Lista com as opções Sim/Não.'],
         ['Arquivo - Upload', 'Anexo de um arquivo (por exemplo, um laudo em PDF ou imagem).'],
     ], [5.0, 12.5]),
    ('p', 'Depois de Salvar, a janela <b>continua aberta</b> para você cadastrar várias alíneas seguidas; use Fechar ao terminar. '
          'O sistema não impede duas alíneas com o mesmo nome no mesmo tipo, então confira para não duplicar.'),
    ('img', '08-alineas-do-tipo.png', 'Filtrando pelo tipo, a lista mostra o tipo de campo e o nome de cada alínea, na ordem em que aparecerão para o profissional.'),
    ('p', '<b>Ordem:</b> quando um tipo específico está filtrado, aparecem as setas para subir e descer cada alínea. Depois de reordenar, '
          'clique em <b>Salvar</b> (botão amarelo) para gravar a nova ordem.'),
    ('img', '09-alineas-ordenar.png', 'Após mover uma alínea, aparece o botão Salvar para gravar a ordem.'),
    ('img', '10-alineas-ordem-salva.png', 'Ordem salva ("Salvo!"): "Conduta e orientações" passou a ser a primeira.'),
    ('p', '<b>Excluir uma alínea</b> (botão vermelho) pede confirmação. Se a clínica tiver a configuração auxiliar '
          '<b>BLOCK_ADD_PRONT</b> (bloqueio de novos lançamentos de prontuário), os botões <b>Novo</b> e <b>excluir</b> desta tela '
          'deixam de aparecer, e o cadastro de alíneas fica somente para consulta.'),
    ('img', '14-alinea-excluir.png', 'Confirmação ao excluir uma alínea.'),

    ('h2', '3. Textos padrão'),
    ('p', 'Um <b>Texto padrão</b> é um trecho pronto que o profissional insere numa alínea de texto com um clique, em vez de digitar '
          'tudo de novo. Cada profissional cria os seus, por tipo de prontuário. Acesso: <b>Prontuário → Textos padrão</b>, '
          'na área do profissional.'),
    ('img', '11-texto-padrao-novo.png', 'Novo texto padrão: tipo de prontuário, título (máximo 20 caracteres) e o texto.'),
    ('img', '12-texto-padrao-lista.png', 'Lista dos textos do profissional, com o título e os botões Visualizar/Alterar e excluir.'),
    ('tabela', [
        ('Prontuário tipo', 'Em quais prontuários este texto estará disponível. Não pode ser trocado depois de salvo.', 'ProntuarioTextoPadrao.IdProntuarioTipo'),
        ('Título', 'Nome curto que o profissional vê na lista ao inserir (máximo 20 caracteres).', 'ProntuarioTextoPadrao.Titulo'),
        ('Texto', 'O conteúdo que será inserido na alínea.', 'ProntuarioTextoPadrao.Texto'),
    ]),
    ('img', '13-texto-padrao-excluir.png', 'Confirmação ao excluir um texto padrão.'),

    ('h2', 'Itens ligados a esta configuração'),
    ('tabelagen', ['Item', 'O que é', 'Onde está'],
     [
         ['Relatório Compartilhado(Prontuários)', 'Define se um profissional vê o prontuário finalizado de outro.', 'Cadastro de Especialidades (manual próprio)'],
         ['De-Para de prontuário', 'Forma antiga de autorizar um profissional a ver prontuários de outro. Está oculta do menu e sendo substituída pelo Relatório Compartilhado.', 'Rota /prontuario/depara (não aparece no menu)'],
         ['Tags do prontuário', 'Rótulos por método de atendimento; ligadas por configuração da clínica (PRONTUARIO_TAGS).', 'Manuais "Uso do Prontuário" e "Auditoria de Prontuário"'],
     ], [5.0, 7.5, 5.0]),
    ('aviso', '<b>Resumo dos cuidados:</b> (1) crie primeiro o tipo e as alíneas; (2) evite excluir ou reordenar alíneas de um tipo já em uso, pois isso muda o formulário dos '
              'prontuários em andamento; (3) tipo com prontuários não pode ser excluído; (4) textos padrão são pessoais de cada profissional.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Configuracao.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Configuracao_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Configuracao.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
