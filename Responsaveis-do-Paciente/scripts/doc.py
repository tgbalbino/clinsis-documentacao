# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.0'
DATA = '16/10/2026'
NOME = 'Responsaveis_do_Paciente'
TITULO = "Responsáveis do Paciente"
SUBTITULO = "Quantos responsáveis forem necessários por paciente, com parentesco, contato e situação"
VIDEO_NOME = "https://youtu.be/6df6y0tUt8o"
INTRO = ('Crianças, adolescentes e pacientes que dependem de alguém para vir à clínica costumam ter <b>mais de um responsável</b>: '
         'pai, mãe, avó, babá. No ClinSis, cada paciente pode ter quantos <b>responsáveis</b> forem necessários. Cada responsável é uma '
         '<b>Pessoa</b> (do tipo <b>Responsável</b>) ligada ao paciente pelo <b>grau de parentesco</b> e pela situação <b>ativo ou inativo</b>. '
         'A clínica pode <b>exigir pelo menos um responsável ativo</b> para pacientes menores de 18 anos, e os responsáveis '
         'são os que usam o <b>Totem de check-in</b> com os próprios dados.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado. O responsável do exemplo foi criado só para este manual e removido depois.')

blocks = [
    ('h2', 'Como funciona'),
    ('tabelagen', ['Assunto', 'Como funciona'],
     [['Quantos responsáveis', 'Quantos forem necessários, cada um com <b>grau de parentesco</b> (Mãe, Pai, Avô, Avó, Tio, Babá, Irmão(ã) ou Outros) e situação <b>Ativo</b> ou <b>Inativo</b>.'],
      ['O responsável é uma Pessoa', 'Fica no cadastro de <b>Pessoa</b> com a marca <b>Responsável</b>, e o mesmo responsável pode estar ligado a <b>mais de um paciente</b> (irmãos, por exemplo).'],
      ['Onde se cadastra', 'No <b>cadastro do paciente</b>, aba <b>Dados principais</b>, bloco <b>Responsáveis</b>. Os responsáveis são gravados junto com o paciente, no botão <b>Salvar</b>.'],
      ['Exigir responsável de menor', 'Opção da clínica: com ela ligada, não se salva paciente menor de 18 anos sem ao menos <b>1 responsável ativo</b>. Vem <b>desligada</b>.'],
      ['Totem de check-in', 'O responsável registra a chegada dos dependentes com o <b>seu próprio CPF e data de nascimento</b>. Por isso, com o totem ativo, a data de nascimento do responsável é obrigatória.']],
     [5, 13]),

    ('h2', 'Como ligar a exigência de responsável para menores'),
    ('p', 'Na <b>Área do Administrador</b> (endereço <b>/area</b>), abra <b>Clínicas</b>, entre no cadastro da clínica e marque '
          '<b>Exigir responsável para menor de 18 anos</b>. Salve. Depois disso, o título <b>Responsáveis</b> do cadastro de paciente '
          'menor ganha um <b>asterisco vermelho</b>, e o sistema avisa quando não há nenhum responsável ativo: '
          '<b>"Paciente menor de 18 anos: informe ao menos 1 responsável ativo."</b>'),
    ('img', '02-paciente-sem-responsavel.png', 'Paciente menor de idade, com a exigência ligada: asterisco vermelho em Responsáveis e a lista vazia.'),

    ('h2', 'Cadastrar um responsável no paciente'),
    ('p', 'No cadastro do paciente, no bloco <b>Responsáveis</b>, a tabela mostra <b>Nome</b>, <b>Parentesco</b>, <b>CPF</b> e <b>Situação</b>. '
          'Clique em <b>Adicionar responsável</b> para abrir o formulário.'),
    ('img', '03-paciente-com-responsavel.png', 'Paciente com um responsável cadastrado. O selo amarelo "sem nascimento" avisa que ele ainda não poderá usar o totem.'),
    ('img', '04-modal-novo.png', 'Novo responsável: CPF, nome, grau de parentesco, celular, data de nascimento e endereço.'),
    ('tabelagen', ['Campo', 'Como preencher'],
     [['CPF (obrigatório)', 'Precisa ser um CPF válido e não repetir na lista do paciente. Se o CPF já existir como responsável em outro paciente, o sistema avisa <b>"Responsável já cadastrado: os dados foram carregados"</b> e só falta informar o parentesco.'],
      ['Nome (obrigatório)', 'Nome completo do responsável.'],
      ['Grau de parentesco (obrigatório)', 'Escolha na lista: Mãe, Pai, Avô, Avó, Tio, Babá, Irmão(ã) ou Outros.'],
      ['Celular', 'Contato do responsável.'],
      ['Data de nascimento', '<b>Obrigatória quando o totem de check-in está ativo</b> na clínica: é com ela e o CPF que o responsável se identifica no totem.'],
      ['Responsável ativo', 'Marcado por padrão. Desmarque para manter o registro sem usá-lo (por exemplo, quando alguém deixa de ser responsável).'],
      ['Endereço', 'Já vem preenchido com o endereço do paciente; altere se o responsável mora em outro lugar.']],
     [5, 13]),
    ('p', 'Clique em <b>Confirmar</b> para incluir o responsável na lista e depois em <b>Salvar</b>, no cadastro do paciente, para gravar.'),
    ('img', '05-tabela-com-responsavel.png', 'Dois responsáveis na lista do paciente. Nada é gravado até clicar em Salvar.'),
    ('img', '06-salvo.png', 'Cadastro salvo: o responsável passa a existir como Pessoa e fica ligado ao paciente.'),

    ('h2', 'Editar, inativar e remover'),
    ('tabelagen', ['Ação', 'Quando usar'],
     [['Editar (lápis)', 'Corrigir telefone, endereço, parentesco ou data de nascimento do responsável.'],
      ['Ativar / Inativar (chave)', 'Quando alguém deixa de ser responsável pelo paciente. O responsável <b>inativo</b> continua no histórico e <b>não conta</b> para a exigência de menor, nem usa o totem.'],
      ['Remover (lixeira)', 'Só aparece para o responsável que acabou de ser incluído e ainda não foi salvo. Depois de salvo, use <b>Inativar</b>.']],
     [5, 13]),

    ('h2', 'Responsável na tela de Pessoa'),
    ('p', 'Em <b>Cadastros → Pessoa</b>, a lista tem a coluna <b>Responsável</b>, e o filtro <b>Responsável</b> mostra só essas pessoas. '
          'O filtro <b>Sem data de nascimento</b> ajuda a achar quem ainda não consegue usar o totem. Ao cadastrar uma Pessoa, '
          'a marca <b>Responsável</b> classifica a pessoa; o vínculo com o paciente é feito no cadastro do paciente.'),
    ('img', '01-pessoa-filtro.png', 'Filtros da tela de Pessoa: Responsável e Sem data de nascimento.'),
    ('img', '07-pessoa-responsavel.png', 'Pessoas do tipo Responsável, incluindo o responsável criado neste exemplo.'),
    ('aviso', 'Uma pessoa que é <b>só responsável</b> não conta como CPF duplicado de paciente. Isso permite cadastrar a criança com o CPF do pai '
              'ou da mãe, quando ela ainda não tem CPF próprio.'),

    ('h2', 'Cuidados e regras'),
    ('tabelagen', ['Assunto', 'Como funciona'],
     [['Paciente adulto', 'Também pode ter responsáveis (por exemplo, um cuidador). A exigência da clínica só vale para menores de 18 anos.'],
      ['Mesmo responsável, vários pacientes', 'O responsável é uma única Pessoa. Alterar o celular dele vale para todos os pacientes ligados a ele.'],
      ['CPF repetido na lista', 'O sistema não deixa informar o mesmo CPF duas vezes no mesmo paciente.'],
      ['Quem pode editar', 'Quem pode alterar o cadastro do paciente. Os demais perfis apenas veem a lista.'],
      ['Campo antigo de responsável', 'O campo único de responsável do cadastro antigo foi migrado para esta lista. Suporte: rodar o script 207 antes de publicar a API e o 208 só depois.']],
     [6, 12]),
]

render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, f'Documentacao_{NOME}.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
print('ok')
