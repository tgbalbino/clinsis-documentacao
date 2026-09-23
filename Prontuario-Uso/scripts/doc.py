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
TITULO = "Prontuário — Uso pelo Profissional"
SUBTITULO = "Criar, preencher, finalizar, consultar e imprimir prontuários"
VIDEO_NOME = "video-prontuario-uso-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('Este manual mostra o dia a dia do prontuário para o <b>profissional</b>: como criar um prontuário para um paciente da '
         'agenda, preencher as alíneas, usar textos padrão e tags, <b>finalizar</b>, consultar, imprimir em PDF e excluir um '
         'rascunho. Os tipos e as alíneas (o formulário) são configurados antes, no manual "Prontuário — Configuração". '
         'A conferência gerencial (auditoria) tem manual próprio.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de homologação, clínica de '
          'testes "Homologação" (Clínica 1), com o usuário profissional de teste. Nenhum dado de produção foi acessado. '
          'Os prontuários criados para o teste foram excluídos ao final.')

blocks = [
    ('h2', 'Quem faz o quê'),
    ('tabelagen', ['Perfil', 'O que pode fazer'],
     [
         ['Profissional', 'Criar, preencher, finalizar, consultar, imprimir e excluir rascunhos dos <b>seus</b> prontuários; ver prontuários finalizados de outros, se a Especialidade compartilhar.'],
         ['Administrador', 'Consultar e imprimir; exportar a lista em CSV. Não cria prontuário pela tela do profissional.'],
         ['Atendente', 'Acessa a lista de prontuários (link "Prontuário" do menu), sem criar nem editar.'],
     ], [4.0, 13.5]),
    ('p', 'O acesso é por <b>Prontuário</b> no menu lateral (na área do profissional). O módulo Prontuário precisa estar ligado para a clínica.'),

    ('h2', '1. Encontrar prontuários (a lista)'),
    ('p', 'Ao abrir a tela, aparece a janela <b>Filtrar</b>. O <b>Tipo</b> é obrigatório (Anamnese, Evolução diária...). Os demais filtros são opcionais.'),
    ('img', '01-inbox.png', 'Filtros: número do prontuário, tipo (obrigatório), nome do paciente, datas de emissão e de inclusão, situação (Finalizado), ordenação e tags.'),
    ('tabelagen', ['Filtro', 'Para que serve'],
     [
         ['Nº Prontuário', 'Busca direto pelo número do prontuário (só o número, sem zeros à esquerda).'],
         ['Tipo *', 'Obrigatório. A lista mostra um tipo por vez.'],
         ['Nome do Paciente', 'Parte do nome.'],
         ['Emissão inicial / final', 'Data de emissão (a data do documento, informada ao finalizar).'],
         ['Inclusão inicial / final', 'Data em que o prontuário foi criado.'],
         ['Finalizado', 'Todos, só finalizados ou só em digitação.'],
         ['Ordenação', 'Mais recentes primeiro, entre outras.'],
         ['Tags', 'Só aparece se a clínica usa tags. Com nenhuma marcada, retorna todos.'],
     ], [4.5, 13.0]),
    ('img', '13-lista-filtrada.png', 'Resultado do filtro: número, profissional, paciente, mãe, situação, datas e as ações da linha.'),
    ('p', 'Situação: <b>Digitação</b> (rascunho, ainda editável) ou <b>Finalizada</b> (travada). Ações de cada linha: <b>olho</b> (visualizar), '
          '<b>tags</b> (ver as tags do prontuário, quando a clínica usa tags), <b>amarelo</b> (abrir para preencher, só nos seus prontuários) e '
          '<b>lixeira</b> (só nos seus rascunhos). A caixa de seleção existe só nos finalizados e serve para imprimir.'),

    ('h2', '2. Criar um prontuário'),
    ('p', 'Depois de filtrar por um tipo, clique em <b>Novo</b>. A janela "Selecionar Paciente" tem duas abas: <b>Buscar da agenda</b> e '
          '<b>Buscar por dados</b>.'),
    ('img', '05-novo-menu.png', 'Janela para selecionar o paciente e a especialidade.'),
    ('img', '06-pacientes-agenda.png', '"Listar Pacientes da agenda atual" mostra os pacientes do profissional na agenda do mês, para marcar um ou vários.'),
    ('p', 'Marque o(s) paciente(s), escolha a <b>Especialidade</b> (obrigatória: ela é gravada no prontuário e é ela que define o '
          '"Relatório Compartilhado") e clique em <b>Adicionar</b>. Pacientes que já têm um rascunho do mesmo tipo não aparecem para não criar '
          'duplicado. Quando se cria um só, o sistema já abre o prontuário para preenchimento.'),
    ('img', '07-selecionar-paciente.png', 'Paciente e especialidade selecionados, prontos para Adicionar.'),
    ('aviso', '<b>Regra da Evolução diária:</b> esse tipo não pode ser criado com data mais de 1 dia no futuro.'),

    ('h2', '3. Preencher o prontuário'),
    ('img', '08-apos-adicionar.png', 'Prontuário recém-criado: dados do paciente, data de emissão, tags e a primeira alínea.'),
    ('tabelagen', ['Área da tela', 'Como funciona'],
     [
         ['Cabeçalho', 'Tipo, paciente, mãe e o número do prontuário (N°).'],
         ['Data de emissão', 'Vem com a data de hoje. Ajuste se necessário e use o Salvar ao lado. É a data que aparece no documento.'],
         ['Tags', 'Escolha uma tag na lista e clique em Salvar; para remover, use a lixeira ao lado da tag. Só existe se a clínica usa tags.'],
         ['Alínea', 'Cada alínea é um campo do formulário. Use Anterior / Próxima para navegar; o "1/1" mostra a posição.'],
         ['Descrever', 'Caixa de texto da alínea, com contador de caracteres. Salvar grava só a alínea atual ("Texto Salvo.").'],
         ['Texto Padrão', 'Lista dos seus textos padrão do tipo. Ao escolher um, o sistema pergunta se deseja inserir.'],
     ], [4.0, 13.5]),
    ('img', '09-texto-padrao-confirmar.png', 'Ao escolher um texto padrão, a confirmação avisa que o texto já digitado no campo será apagado.'),
    ('aviso', '<b>Atenção:</b> inserir um texto padrão <b>substitui</b> o que já foi digitado na alínea. Insira o texto padrão primeiro e complemente depois.'),
    ('img', '10-alinea-salva.png', 'Alínea salva. O botão <b>Finalizar</b> só aparece depois que há texto salvo.'),
    ('p', 'Para alíneas do tipo <b>Sim ou Não</b> aparece uma lista de opções, e nas do tipo <b>Arquivo</b> há o envio de um anexo. '
          'Cada alínea é salva separadamente.'),

    ('h2', '4. Tags'),
    ('p', 'As tags identificam o <b>método de atendimento</b> (por exemplo, "Padrão" ou "Jedi") e são usadas na Auditoria de Prontuário. '
          'Só aparecem se a clínica tem a opção <b>PRONTUARIO_TAGS</b>. Como elas entram no prontuário:'),
    ('tabelagen', ['Quando', 'O que acontece'],
     [
         ['Ao criar o prontuário', 'Se a clínica tem a opção <b>PRONT_TAG_AUTO</b> e o paciente tem <b>um único método</b> na agenda do mês com esse profissional, a tag desse método é aplicada sozinha. Com mais de um método (ou nenhum), não marca.'],
         ['Ao abrir o prontuário', 'O sistema aplica as tags sugeridas pelos métodos da agenda do mês da emissão e por tags de outros prontuários do mesmo mês (no teste, um paciente com dois métodos recebeu as duas tags ao abrir).'],
         ['Manualmente', 'Escolha na lista e clique em Salvar. Só é possível mexer nas tags enquanto o prontuário não estiver finalizado.'],
         ['Ao finalizar', 'Se a clínica usa tags e existem tags cadastradas, é preciso ter <b>ao menos 1 tag</b>, senão a tela avisa "Informe ao menos 1 tag antes de finalizar o prontuário".'],
     ], [4.0, 13.5]),
    ('img', '14-tags-modal.png', 'Depois de finalizado, as tags são consultadas pelo botão "tags" da linha na lista.'),
    ('aviso', '<b>Correção feita nesta documentação:</b> a tag automática ao criar o prontuário não funcionava, porque o cálculo do mês '
              'dependia da data de emissão, que só existe ao finalizar. Agora usa a data de criação, e ela é aplicada corretamente '
              '(testado: paciente com método único recebeu a tag na criação).'),

    ('h2', '5. Finalizar'),
    ('p', 'Clique em <b>Finalizar</b>. A janela confirma a <b>data de emissão</b> que será usada; escolha Sim para concluir.'),
    ('img', '11-finalizar-confirmar.png', 'Confirmação de finalização com a data de emissão.'),
    ('img', '12-finalizado.png', 'Prontuário finalizado: os campos ficam bloqueados (cinza) e as tags saem da tela de edição.'),
    ('tabelagen', ['Depois de finalizar', 'Regra'],
     [
         ['Edição', 'Não é mais possível alterar textos. Se tentar (por exemplo, por outra tela), o servidor responde "Não é possível salvar. O prontuário está finalizado."'],
         ['Exclusão', 'Prontuário finalizado não é excluído (a tela não mostra a lixeira e agora o servidor também recusa).'],
         ['Reabrir', 'Não há botão de reabrir na tela do profissional; a reabertura é uma operação restrita (perfil 50) feita fora da tela de prontuário.'],
         ['Quem edita', 'Somente o profissional dono do prontuário. Outro profissional nunca altera, mesmo com Relatório Compartilhado (que é só leitura).'],
     ], [4.0, 13.5]),

    ('h2', '6. Consultar e imprimir'),
    ('p', 'O <b>olho</b> abre a visualização (só leitura), que também traz o botão <b>Página de impressão / Download</b>.'),
    ('img', '15-visualizar.png', 'Visualização do prontuário finalizado.'),
    ('p', 'Para gerar o <b>PDF</b> direto da lista, marque a caixa dos prontuários finalizados e clique no ícone da impressora. '
          'Só é possível imprimir de <b>um paciente por vez</b> ("Selecione documentos de apenas 1 paciente"). O arquivo baixa como '
          '"pac_&lt;nome do paciente&gt;_&lt;data e hora&gt;.pdf".'),
    ('img', '16-selecionar-imprimir.png', 'Prontuário finalizado marcado; o ícone da impressora gera o PDF.'),
    ('img', '18-pdf-prontuario.png', 'PDF gerado: cabeçalho com dados do paciente, as alíneas preenchidas, marca d\'água da clínica e linha de assinatura e carimbo.'),
    ('aviso', '<b>Correção feita nesta documentação:</b> o nome do arquivo saía como "pac__data.pdf", sem o nome do paciente. Agora inclui o nome '
              '(ex.: "pac_Paciente_0005_23-09-2026 17-49.pdf"). O modelo do PDF (1, 2 ou 3) é definido por tipo de prontuário na configuração da clínica.'),

    ('h2', '7. Excluir um rascunho'),
    ('p', 'A lixeira aparece só nos <b>seus rascunhos</b> (situação Digitação).'),
    ('img', '19-lista-rascunho.png', 'Rascunho na lista: aparecem olho, tags, abrir e lixeira; sem caixa de impressão.'),
    ('img', '20-excluir-rascunho.png', 'Confirmação da exclusão do rascunho.'),
    ('tabelagen', ['Situação do rascunho', 'O que a exclusão faz'],
     [
         ['Nenhuma alínea salva', 'Apaga o prontuário de vez (junto com as tags).'],
         ['Já tem texto salvo', 'Marca como excluído: some da lista, mas o registro é preservado no banco.'],
     ], [5.0, 12.5]),
    ('aviso', '<b>Correção feita nesta documentação:</b> excluir um rascunho que tinha tag (inclusive a automática) falhava em silêncio, porque a tag '
              'impedia a exclusão no banco. Agora as tags saem junto (testado com o rascunho criado durante o teste).'),

    ('h2', '8. Ver prontuários de outros profissionais'),
    ('p', 'Um profissional só vê o prontuário <b>finalizado</b> de outro se a <b>Especialidade</b> do prontuário estiver com '
          '"Relatório Compartilhado(Prontuários)" e o paciente já tiver prontuário com ele. Nível 1: só quem atende a mesma especialidade. '
          'Nível 2: qualquer profissional com paciente em comum. O compartilhamento é sempre <b>somente leitura</b>. '
          'Detalhes no manual "Cadastro de Especialidades".'),
    ('p', 'A tela <b>Prontuários por paciente</b> (menu Prontuário do administrador e do profissional) reúne o histórico de um paciente: escolha o '
          'paciente (só aparecem pacientes ativos), o tipo e, se quiser, o profissional, e pesquise. Esta consulta não foi demonstrada em vídeo.'),

    ('h2', 'Mensagens e cuidados'),
    ('tabelagen', ['Mensagem', 'O que significa'],
     [
         ['"Tipo não enviado" / "Paciente não encontrado"', 'Faltou escolher o tipo ou o paciente.'],
         ['"Operação não permitida"', 'O prontuário é de outro profissional (só o dono altera).'],
         ['"Não é possível salvar. O prontuário está finalizado."', 'Prontuário já finalizado.'],
         ['"Informe ao menos 1 tag antes de finalizar o prontuário"', 'A clínica exige tag e nenhuma foi marcada.'],
         ['"Selecione documentos de apenas 1 paciente"', 'Na impressão, marque prontuários de um único paciente.'],
         ['"Este tipo está vinculado a prontuário..."', 'Ao excluir um tipo que já tem prontuários (na Configuração).'],
     ], [7.0, 10.5]),
    ('aviso', '<b>Resumo:</b> (1) o profissional só edita o que é seu; (2) finalizar trava o prontuário; (3) inserir texto padrão apaga o texto da alínea; '
              '(4) imprima um paciente por vez; (5) o Relatório Compartilhado é só leitura.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Uso.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Uso_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Prontuario_Uso.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
