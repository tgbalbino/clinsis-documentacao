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
DATA = "18/09/2026"
TITULO = "Layout de Contrato"
SUBTITULO = "O modelo (template) usado para gerar o PDF de todos os contratos da clínica"
VIDEO_NOME = "video-layout-contrato-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = ('Esta tela define o <b>texto/modelo</b> que vira o PDF de qualquer contrato da clínica — '
         'tanto o PDF baixado para impressão quanto o PDF enviado para assinatura eletrônica pela '
         'D4Sign. É um pré-requisito compartilhado pelas rotinas <b>Contrato (sem assinatura '
         'digital)</b> e <b>Contrato (com assinatura digital D4Sign)</b>: sem um layout ativo '
         'configurado, nenhuma delas consegue gerar ou enviar um contrato.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Onde fica e o que é'),
    ('p', 'Em <b>Tabelas Aux. → Layout Contrato</b> (rota <font face="Courier">/aux/contratolaiout</font>), '
          'a clínica escreve o texto do contrato em <b>Markdown</b> (um formato de texto simples com '
          'marcações como <font face="Courier">**negrito**</font> e <font face="Courier"># Título</font>), '
          'usando "variáveis" entre chaves duplas que o sistema troca automaticamente pelos dados reais '
          'de cada contrato na hora de gerar o PDF (nome do paciente, valor, datas, etc.).'),
    ('img', '00-lista-layouts.png',
     'Listagem de layouts cadastrados: é possível manter vários (histórico de versões), mas só um fica '
     '"Ativo" por vez — é sempre esse único ativo que gera o PDF de qualquer contrato da clínica.'),
    ('aviso', 'Só existe <b>um</b> layout ativo por clínica — não há como ter um modelo diferente por '
              'tipo de contrato, convênio ou especialidade. Ativar um novo layout muda o conteúdo do '
              'PDF de todos os contratos gerados a partir daquele momento (contratos já fechados/já '
              'enviados antes não são afetados, pois o PDF deles já foi gerado).'),

    ('h2', 'Editando o layout'),
    ('p', 'Ao clicar em "Editar" (ou "Novo layout"), aparece uma caixa de texto grande para o conteúdo '
          'em Markdown, e a lista de todas as variáveis disponíveis logo abaixo dela.'),
    ('img', '01-editor-layout-ativo.png', 'Editor do layout ativo: texto em Markdown com títulos, negrito e as variáveis entre chaves duplas.'),
    ('img', '02-variaveis-disponiveis.png',
     'Lista completa de variáveis disponíveis, exibida abaixo do campo de texto — basta copiar o '
     'código exato (ex.: {{PacienteNome}}) para o texto do contrato.'),
    ('tabela', [
        ('Dados da clínica', '{{ClinicaNomeFantasia}}, {{ClinicaRazaoSocial}}, {{ClinicaCnpj}}, {{ClinicaEndereco}}, {{ClinicaCidade}}, {{ClinicaUf}}, {{ClinicaTelefone}}, {{ClinicaEmail}}, {{ClinicaResponsavelNome}}, {{ClinicaResponsavelCPF}}', 'PDFContratoService.cs'),
        ('Dados do contrato', '{{ContratoId}}, {{ContratoDataEmissao}}, {{ContratoDataVencimento}}, {{ContratoValorTotal}}, {{ContratoObservacao}}, {{DataAtual}} (data em que o PDF foi gerado)', 'PDFContratoService.cs'),
        ('Dados do paciente', '{{PacienteNome}}, {{PacienteCPF}}, {{PacienteDataNascimento}}, {{PacienteEndereco}}', 'PDFContratoService.cs'),
        ('Dados do responsável', '{{ResponsavelNome}}, {{ResponsavelCPF}}, {{ResponsavelEndereco}} (se não houver responsável cadastrado, usam os dados do próprio paciente), e {{RelacaoResponsavelLinha}} (linha "Relação com o paciente" — só aparece quando há responsável com relação preenchida)', 'PDFContratoService.cs'),
        ('Tabelas prontas', '{{TabelaServicos}} (lista os serviços contratados: nome, quantidade, valor unitário e total) e {{TabelaPagamentos}} (lista as condições de pagamento: forma, valor, parcelas, 1ª e última parcela) — cada uma vira uma tabela pronta no PDF', 'PDFContratoService.cs'),
    ]),
    ('aviso', 'A substituição é por texto exato — <font face="Courier">{{PacienteNome}}</font>, sem '
              'espaços e com a grafia exatamente como na lista. Copiar o código da própria lista de '
              'variáveis evita erro de digitação.'),

    ('h2', 'Modelo padrão pronto'),
    ('p', 'Quem está criando um layout do zero não precisa escrever um contrato inteiro na mão: o '
          'botão <b>"Usar modelo padrão"</b> preenche o campo com um contrato de prestação de serviços '
          'completo e pronto (objeto, vigência, condições de pagamento, obrigações das partes, LGPD, '
          'cláusula de assinatura eletrônica, foro), já usando as variáveis corretas — só ajustar o que '
          'for necessário para a realidade da clínica.'),
    ('img', '03-novo-layout-vazio.png', 'Tela de "Novo layout", vazia, antes de usar o modelo padrão.'),
    ('img', '04-modelo-padrao-preenchido.png', 'Depois de clicar em "Usar modelo padrão": o texto completo aparece pronto para revisão/edição.'),

    ('h2', 'Pré-visualizando antes de ativar'),
    ('p', 'O botão <b>"Visualizar PDF de exemplo"</b> gera um PDF de verdade a partir do texto que está '
          'no campo <b>naquele momento — mesmo sem salvar</b> — substituindo as variáveis por dados '
          'fictícios de exemplo (paciente, responsável, serviços e pagamento inventados). É a forma '
          'certa de conferir como o contrato vai ficar (formatação, quebras de linha, tabelas) antes de '
          'salvar e ativar o layout para valer.'),
    ('img', '05-pdf-exemplo-gerado.png',
     'PDF de exemplo gerado a partir do layout: dados fictícios (Paciente Exemplo da Silva, Sessão de '
     'Exemplo, etc.) já formatados em tabelas, título, negrito — exatamente como sairia num contrato real.'),
    ('aviso', 'Sempre use "Visualizar PDF de exemplo" antes de marcar "Deixar ativo" e salvar. Um erro '
              'de digitação nas chaves de uma variável (ex.: colar um texto com acentuação de outra '
              'origem/codificação) pode corromper a acentuação de todo o contrato gerado a partir '
              'dali — inclusive dos contratos enviados para assinatura na D4Sign — e isso só aparece '
              'visualmente no PDF, não no texto do editor.'),

    ('h2', 'Ativando um layout'),
    ('p', 'Ao salvar um layout com a caixa "Deixar ativo" marcada (ou clicar em "Ativar" na listagem, '
          'para um layout já existente), ele passa a ser o único usado para gerar contratos daquele '
          'momento em diante — o layout que estava ativo antes é automaticamente desativado, mas '
          'continua salvo no histórico, podendo ser reativado depois se necessário.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Layout_Contrato.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Layout_Contrato_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Layout_Contrato.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
