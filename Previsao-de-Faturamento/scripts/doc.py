# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_scripts-comuns'))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = '1.0'
DATA = '29/09/2026'
TITULO = 'Previsão de Faturamento da Agenda'
SUBTITULO = 'Quanto a clínica deve faturar no mês: para que serve, como configurar, de onde vêm os valores e como conferir'
VIDEO_NOME = "https://youtu.be/Aft3I2vvkLk"
INTRO = ('A <b>Previsão de Faturamento da Agenda</b> estima, semana a semana, quanto a clínica vai faturar com a '
         'agenda de um mês: soma o que já foi realizado e projeta o que ainda está agendado. Cada estimativa é '
         'guardada como uma "foto" da semana, então dá para acompanhar a evolução, ver o que mudou, conferir com '
         'o financeiro e, no fim do mês, medir o quanto a previsão acertou.')
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = [
    ('h2', 'Para que serve'),
    ('p', 'Responde à pergunta "quanto vamos faturar neste mês?" antes de o mês terminar. Em vez de esperar o '
          'fechamento, a direção acompanha uma previsão que se atualiza toda semana e mostra: quanto já está '
          'realizado, quanto ainda vem pela agenda, quanto mudou em relação à semana anterior e desde o '
          'início do mês, e se há divergência entre o que a agenda mostra e o que o financeiro gerou.'),
    ('aviso', 'Só o perfil <b>Administrador</b> acessa esta funcionalidade. As previsões são calculadas '
              'apenas para agendas de mês já criadas.'),

    ('h2', 'Onde fica'),
    ('tabela', [
        ('Relatórios → Cobrança → "Acessar Previsão de Faturamento da Agenda"', 'Tela principal: escolher a agenda, gerar a previsão, ver a evolução semanal e abrir as conferências.', 'Perfil Administrador'),
        ('Tabelas Aux. → Prev. Faturamento', 'Configuração da regra: quais status de sessão contam como faturáveis. Também aberta pelo botão "Configurar status" da tela principal.', 'Perfil Administrador'),
    ]),
    ('img', '01-menu-relatorios.png', 'Relatórios: o primeiro link da coluna Cobrança abre a Previsão de Faturamento da Agenda.'),

    ('h2', '1. Configuração: quais sessões contam como faturáveis'),
    ('p', 'Antes de gerar a primeira previsão é preciso dizer ao sistema <b>quais status de sessão geram '
          'faturamento</b>. Em <b>Tabelas Aux. → Prev. Faturamento</b> aparece a lista de status da agenda '
          '(Presente, Ausente, Ausente - Justificativa, Desmarcações, Remarcação…). Marque os que a clínica '
          'fatura e clique em <b>Salvar configuração</b>. O quadro azul confirma a regra escolhida.'),
    ('img', '00-config-status.png', 'Configuração: status marcados são considerados faturáveis; o número da versão sobe a cada salvamento.'),
    ('aviso', 'Cada vez que a regra é salva, ganha uma <b>nova versão</b>. Cada previsão gerada registra o '
              'critério usado (por exemplo, "Status faturáveis: PRESENTE, ...") e o mantém congelado — mudar a regra '
              'depois <b>não altera</b> as previsões antigas. Sem ao menos um status marcado, o sistema não gera '
              'previsão ("Configure ao menos um status faturável antes de gerar a previsão"). Escolha com cuidado: '
              'a maioria das clínicas marca só <b>Presente</b> (e, se cobra a falta, <b>Ausente</b>).'),

    ('h2', '2. Como a previsão é gerada'),
    ('p', 'Há duas formas, e as duas produzem a mesma "foto":'),
    ('tabelagen', ['Forma', 'Como funciona'], [
        ['Automática', 'Todos os dias de madrugada o sistema verifica as agendas do mês. Se a agenda ainda não tem previsão, cria a <b>Inicial</b>. Nas <b>segundas-feiras</b> cria a <b>Semanal</b>. Só roda para clínicas que já configuraram os status faturáveis.'],
        ['Manual', 'Na tela principal escolha a <b>Agenda</b> (mês/ano), a <b>Data de referência</b> e o <b>Tipo</b> (Inicial, Semanal ou Fechamento) e clique em <b>Gerar previsão</b>. Use o tipo <b>Fechamento</b> ao terminar o mês para registrar o resultado final.'],
    ], [3.2, 14.3]),
    ('p', 'Existe <b>uma previsão de cada tipo por semana</b> e por agenda: se ela já existe, gerar de novo apenas '
          'mostra a existente. A <b>data de referência</b> define até que dia as sessões contam como realizadas.'),

    ('h2', '3. Como o valor é calculado'),
    ('p', 'O sistema analisa cada <b>marcação</b> da agenda (um paciente, com um profissional e uma especialidade, '
          'com de 1 a 5 sessões no mês) e classifica cada sessão:'),
    ('tabelagen', ['Classificação', 'O que é', 'Entra na previsão?'], [
        ['Realizada faturável', 'Sessão com status marcado como faturável, com data até a data de referência.', 'Sim, com o valor cheio.'],
        ['Encerrada não faturável', 'Sessão já encerrada com status que não é faturável (ex.: ausência não cobrada).', 'Não.'],
        ['Futura', 'Sessões contratadas que ainda não foram encerradas (total de sessões menos as encerradas).', 'Sim, mas ponderadas pela probabilidade (abaixo).'],
    ], [3.8, 9.2, 4.5]),
    ('p', '<b>Previsão da marcação = (sessões realizadas faturáveis × valor) + (sessões futuras × valor × '
          'probabilidade)</b>. Vagas vazias na agenda <b>não entram</b> na previsão. O sistema calcula também o '
          '<b>potencial máximo</b> (se todas as sessões fossem faturadas) e o <b>desconto previsto</b> (diferença '
          'entre valor bruto e líquido).'),
    ('h2', 'A probabilidade histórica'),
    ('p', 'Nem toda sessão futura acontece, por isso ela entra na previsão multiplicada por uma probabilidade '
          'calculada com o <b>histórico dos 6 meses anteriores</b>: a proporção de sessões que acabaram em status '
          'faturável, com um pequeno ajuste para não oscilar demais. Se a clínica tem pouco histórico (menos de '
          '20 sessões classificadas), usa-se o padrão de <b>85%</b>. A taxa usada aparece na tela de cada '
          'previsão (no exemplo, 54,5%).'),

    ('h2', '4. De onde vêm os valores (preço de cada sessão)'),
    ('p', 'O preço vem das tabelas de <b>Tab. Cobrança</b> (Tabelas Aux. → Tab. Cobrança), na seguinte ordem de '
          'prioridade — a primeira que existir é usada:'),
    ('tabelagen', ['Atendimento', 'Ordem de busca do valor', 'Aparece como "Origem do preço"'], [
        ['Particular', '1º valor do <b>Profissional + Especialidade</b>; 2º valor da <b>Especialidade</b>.', 'Profissional/especialidade ou Especialidade'],
        ['Convênio', '1º valor da <b>Operadora + Especialidade</b>; 2º valor da <b>Especialidade</b>.', 'Operadora/especialidade ou Especialidade'],
    ], [3, 9.5, 5]),
    ('p', 'Se a tabela tiver valores por <b>Tipo de Marcação</b> (por exemplo, Avaliação e Consulta), vale o valor do '
          'tipo da marcação; se não houver específico, usa o valor "para todos os tipos". O <b>valor bruto</b> é o '
          'valor cobrado; o <b>valor líquido</b> é o valor com desconto, quando a tabela tem um valor com desconto '
          'preenchido — caso contrário, líquido = bruto.'),
    ('aviso', 'Marcação sem nenhum preço configurado fica com valor zero e aparece em <b>amarelo</b> no detalhamento e na '
              'lista de <b>Pendências</b> ("Sem preço"). Cadastre o valor em Tab. Cobrança e gere a previsão de novo.'),

    ('h2', '5. A tela principal'),
    ('img', '02-tela-previsao.png', 'Previsão de faturamento da agenda: filtros no alto, quatro cartões-resumo, o critério usado e a evolução semanal.'),
    ('tabela', [
        ('Previsão líquida atual', 'Valor líquido da previsão mais recente, com o bruto logo abaixo.', 'Última previsão da agenda'),
        ('Desde a primeira previsão', 'Diferença entre a previsão atual e a primeira do mês (valor e %). Verde sobe, vermelho cai.', 'Última − Primeira'),
        ('Financeiro gerado', 'Total líquido dos títulos de Contas a Receber já gerados para esta agenda (Cobrança de Paciente) e quanto já foi recebido.', 'Contas a Receber da agenda'),
        ('Agenda atual', 'Quantidade de pacientes, de sessões e de marcações sem preço.', 'Marcações da agenda'),
        ('Critério e probabilidade', 'Faixa de informação com os status faturáveis usados e a probabilidade histórica aplicada.', 'Regra congelada da previsão'),
        ('Evolução semanal', 'Uma linha por previsão: previsão bruta, descontos, líquida, variação em relação à semana anterior e desde o início, e financeiro gerado. Botões: Detalhes, Conciliação, Movimentações e Pendências.', 'Todas as previsões da agenda'),
    ]),

    ('h2', '6. Como conferir'),
    ('p', 'Cada linha da evolução tem quatro botões de conferência. Use esta ordem:'),
    ('h2', 'Detalhes: conferir marcação por marcação'),
    ('p', 'Lista cada marcação da previsão, com paciente, profissional, especialidade, modalidade (Particular ou '
          'Convênio), quantidade de <b>sessões</b>, <b>realizadas</b> e <b>futuras</b>, valor bruto e líquido, '
          'a <b>origem do preço</b>, a probabilidade e a previsão líquida. No topo: previsão filtrada, realizado '
          'operacional e futuro agendado "cheio" (sem ponderar). Dá para pesquisar e mostrar só os itens sem preço; '
          'o botão "Ver sessões" abre cada sessão com data, status e classificação.'),
    ('img', '03-detalhes.png', 'Detalhamento: cada marcação com sessões, valores, origem do preço, probabilidade e previsão.'),
    ('aviso', 'Exemplo para conferir a conta: PACIENTE 41 (Psicólogo, valor R$ 25,00) tem 4 sessões, 1 realizada e 3 futuras. '
              'Previsão = 1 × 25,00 + 3 × 25,00 × 54,5% = 25,00 + 40,91 = <b>R$ 65,91</b>, exatamente o valor da linha.'),

    ('h2', 'Conciliação: agenda × financeiro'),
    ('p', 'Compara, paciente a paciente, o <b>realizado operacional</b> (o que a agenda diz que foi realizado) com o '
          '<b>financeiro líquido</b> (o que já virou título em Contas a Receber para esta agenda), além do desconto, '
          'do valor recebido, da diferença e da quantidade de títulos. A coluna Situação indica o resultado:'),
    ('tabelagen', ['Situação', 'O que significa'], [
        ['Conciliado', 'Agenda e financeiro batem (diferença de até 1 centavo).'],
        ['Sem conta a receber', 'Há realizado na agenda, mas nenhum título financeiro: falta gerar a cobrança do paciente.'],
        ['Sem realização na agenda', 'Há título financeiro sem sessão realizada correspondente.'],
        ['Divergência de valor', 'Os dois têm valor, mas diferentes.'],
        ['Recebimento parcial', 'Bate, mas só parte do valor foi recebida.'],
    ], [5, 12.5]),
    ('img', '04-conciliacao.png', 'Conciliação: no exemplo, o PACIENTE 41 tem R$ 89,00 realizados na agenda e nenhum título a receber.'),

    ('h2', 'Movimentações: o que mudou desde a semana anterior'),
    ('p', 'Compara a previsão com a anterior e lista o que fez o valor subir ou cair, com totais de <b>aumentos</b>, '
          '<b>reduções</b> e <b>variação líquida</b>. Os motivos possíveis: Paciente incluído, Paciente removido, '
          'Preço/desconto, Status/realização, Sessões, Alteração cadastral (profissional, especialidade ou operadora) '
          'e Recálculo da probabilidade.'),
    ('img', '05-movimentacoes.png', 'Movimentações: no exemplo, o PACIENTE 41 subiu R$ 11,36 porque uma sessão foi realizada.'),

    ('h2', 'Pendências: o que precisa de correção'),
    ('p', 'Reúne as inconsistências que distorcem a previsão: <b>Sem conta a receber</b>, <b>Sem realização na '
          'agenda</b>, <b>Divergência de valor</b>, <b>Sem preço</b> (marcação sem valor em Tab. Cobrança) e '
          '<b>Quantidade inconsistente</b> (mais sessões classificadas do que as contratadas). Resolva as '
          'pendências e gere a previsão da semana seguinte.'),
    ('img', '06-pendencias.png', 'Pendências: total encontrado, valor envolvido e a lista com o tipo e a descrição de cada uma.'),

    ('h2', 'Fechamento e precisão: a previsão acertou?'),
    ('p', 'Ao clicar em <b>Fechamento e precisão</b>, o sistema compara cada previsão do mês com o <b>resultado '
          'final</b> (o financeiro líquido gerado no fechamento, ou o da última previsão se não houver fechamento) '
          'e mostra o <b>erro</b> em valor e em porcentagem, além da variação desde a primeira previsão. É a forma de '
          'saber se a estimativa é confiável. Enquanto não houver faturamento financeiro no fechamento, o erro '
          'percentual aparece como "N/A".'),
    ('img', '07-precisao.png', 'Fechamento e precisão: primeira e última previsão, resultado final e erro de cada semana.'),

    ('h2', 'Passo a passo para a conferência semanal'),
    ('tabelagen', ['Passo', 'O que fazer'], [
        ['1', 'Abra Relatórios → Previsão de Faturamento da Agenda e escolha a agenda do mês.'],
        ['2', 'Confira o critério (status faturáveis) e a probabilidade na faixa de informação.'],
        ['3', 'Abra <b>Pendências</b>: corrija preços faltantes e quantidades inconsistentes.'],
        ['4', 'Abra <b>Conciliação</b> com "Somente divergências" marcado e gere as cobranças que faltam (Cobrança de Paciente).'],
        ['5', 'Abra <b>Movimentações</b> para entender o que explica a variação da semana.'],
        ['6', 'No fim do mês, gere a previsão <b>Fechamento</b> e veja a <b>precisão</b>.'],
    ], [1.6, 15.9]),

    ('h2', 'Pontos de atenção'),
    ('aviso', 'Cada previsão é uma <b>foto</b>: o que muda na agenda depois de gerada não altera aquela previsão — gere a '
              'próxima semana para refletir a mudança. Previsões geradas antes da etapa de conciliação podem não '
              'ter os títulos financeiros nem as sessões detalhadas, e aparecem vazias nessas telas.'),
    ('aviso', 'O <b>financeiro gerado</b> considera apenas os títulos de Contas a Receber criados pela Cobrança de '
              'Paciente para a agenda; recebimentos de Contrato, Checkin e lançamentos manuais não entram nessa '
              'comparação.'),
]

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Previsao_de_Faturamento.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_Previsao_de_Faturamento_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_Previsao_de_Faturamento.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
