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
TITULO = "Tabela de Valores para Cobrança"
SUBTITULO = "Cadastro por Especialidade/Profissional/Operadora e reajuste de preço em massa"
VIDEO_NOME = "https://youtu.be/mFThg03z-RY"
INTRO = ('A <b>Tabela de Valores para Cobrança</b> (Tabelas Aux. → Tab. Cobrança) define quanto cobrar '
         'do paciente por sessão particular. É essa tabela que o relatório de <b>Cobrança de '
         'Paciente</b> usa para calcular o valor a receber todo mês. Este manual cobre as três formas '
         'de configurar o valor (Especialidade, Profissional e Operadora) e a ferramenta de '
         '<b>reajuste de preço em massa</b>.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Diferença em relação à Tabela de Pagamento'),
    ('p', 'Ao contrário da Tabela de Valores para Pagamento, aqui <b>não existe o conceito de várias '
          'tabelas de valores</b> — é uma configuração única e sempre "viva" por clínica, sem histórico '
          'de versões nem status Ativo/Inativo. A tela tem três abas, cada uma com um escopo diferente '
          'de valor.'),
    ('tabela', [
        ('Especialidade', 'Valor padrão por Especialidade, usado quando não há valor específico do profissional nem da operadora.', 'ConfigCobrancaEspecPagto'),
        ('Profissional', 'Valor específico por Profissional × Especialidade, que sobrepõe o valor padrão só para aquele profissional.', 'ConfigCobrancaProfEspecPagto'),
        ('Operadora', 'Valor específico por Operadora (convênio) × Especialidade, que sobrepõe o valor padrão para atendimentos daquela operadora.', 'ConfigCobrancaOperadoraEspecPagto'),
    ]),
    ('img', '00-aba-especialidade.png', 'Aba "Especialidade": valor padrão (Valor e Valor Social) por especialidade, com filtro e exportação em CSV.'),
    ('img', '05-modal-valores-profissional.png', 'Aba "Profissional": ao abrir um profissional, aparece a grade de valores específicos dele.'),
    ('img', '06-aba-operadora.png', 'Aba "Operadora": escolha a operadora no topo e configure o valor por especialidade específico para ela.'),

    ('h2', 'Reajuste de preço em massa'),
    ('p', 'O mesmo card <b>"Manutenção rápida de preços"</b> usado na Tabela de Pagamento aparece aqui '
          'também, nas três abas — reajustando sempre o escopo da aba em que está (Especialidade = '
          'valor padrão geral; Profissional = só daquele profissional; Operadora = só daquela '
          'operadora).'),
    ('img', '01-reajuste-formulario-aberto.png', 'Botão "Reajustar preços" expande o formulário: percentual e quais campos reajustar (Valor cobrado e/ou Valor social).'),
    ('tabela', [
        ('1. Percentual de reajuste', 'Número positivo (aumento) ou negativo (desconto). Limite: maior que -100% e até 1000%.', 'ReajustePrecoController.cs'),
        ('2. Campos a reajustar', 'Marque "Valor cobrado", "Valor social", ou os dois.', 'reajuste-preco.component.html'),
        ('3. Calcular prévia', 'Mostra o valor atual e o valor novo de cada especialidade — sem gravar nada ainda.', 'ReajustePreco/cobranca(/profissional|/operadora)/simular'),
        ('4. Confirmar reajuste', 'Só depois de conferir a prévia, grava de fato, com uma confirmação extra.', 'ReajustePreco/cobranca(/profissional|/operadora)/confirmar'),
    ]),
    ('img', '02-reajuste-previa.png',
     'Prévia de um reajuste de 8%: Valor atual/novo e Social atual/novo de cada especialidade, em verde os valores que mudam.'),
    ('img', '03-reajuste-confirmado.png', '"11 valor(es) reajustado(s) com sucesso" — grade já atualizada com os novos valores.'),
    ('aviso', 'A prévia <b>não altera nada</b> — só a confirmação grava de verdade. Se algum valor '
              'mudar entre a prévia e a confirmação (outra pessoa editando ao mesmo tempo), o sistema '
              'recusa e pede uma nova prévia. Linhas com Valor Social vazio não são alteradas, mesmo '
              'com o campo marcado, e cada confirmação fica registrada no log do sistema.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Tabela_Preco_Cobranca.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Tabela_Preco_Cobranca_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Tabela_Preco_Cobranca.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
