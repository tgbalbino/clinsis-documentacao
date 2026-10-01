# -*- coding: utf-8 -*-
"""Cria scripts/doc.py de uma rotina a partir do .md já entregue (uso: md_para_doc.py <pasta_rotina> <NomeArquivoBase> <slug-video>)
Ex.: md_para_doc.py Cadastro-Plano-de-Contas Cadastro_Plano_de_Contas cadastro-plano-de-contas
"""
import os, re, sys, pprint
pasta, base, slug = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3]
md = open(os.path.join(pasta, f'Documentacao_{base}.md'), encoding='utf-8').read().split('\n')
titulo = md[0][2:].strip(); sub = md[2].strip('_ '); versao_data = md[4]
m = re.match(r'Versão (\S+) — (\S+)', versao_data)
i = 6; intro = ''
while md[i].strip() and not md[i].startswith('Assista') and not md[i].startswith('Vídeo narrado'):
    intro += md[i] + ' '; i += 1
while md[i] != '---': i += 1
blocks = []; i += 1
while i < len(md):
    l = md[i]
    if not l.strip(): i += 1; continue
    if l.startswith('## '): blocks.append(('h2', l[3:].strip()))
    elif l.startswith('# '): blocks.append(('h1', l[2:].strip()))
    elif l.startswith('> ⚠️'): blocks.append(('aviso', l[4:].strip()))
    elif l.startswith('!['):
        mm = re.match(r'!\[(.*)\]\((.*)\)$', l); blocks.append(('img', mm.group(2), mm.group(1)))
        i += 1
        while i < len(md) and (not md[i].strip() or md[i].startswith('_')): 
            if md[i].startswith('_'): break
            i += 1
    elif l.startswith('|'):
        rows = []
        while i < len(md) and md[i].startswith('|'):
            rows.append([c.strip().replace(chr(92)+'|', '|') for c in re.split('(?<!'+chr(92)+chr(92)+')'+chr(92)+'|', md[i])[1:-1]]); i += 1
        hdr, body = rows[0], rows[2:]
        if len(hdr) == 3 and hdr[0].startswith('Campo'): blocks.append(('tabela', [tuple(r) for r in body]))
        else: blocks.append(('tabelagen', hdr, body, [17.5 / len(hdr)] * len(hdr)))
        continue
    elif l.startswith('_') and l.endswith('_'): pass
    else: blocks.append(('p', l.strip()))
    i += 1
out = f'''# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/_scripts-comuns"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts-comuns"))
from doc_common import render_pdf, render_md

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "screenshots")
ENTREGA = os.path.join(BASE, "entrega")
os.makedirs(ENTREGA, exist_ok=True)

VERSAO = {m.group(1)!r}
DATA = {m.group(2)!r}
TITULO = {titulo!r}
SUBTITULO = {sub!r}
VIDEO_NOME = "video-{slug}-com-legenda.mp4 (ou -sem-legenda.mp4)"
INTRO = {intro.strip()!r}
RODAPE = ('Documento gerado por teste manual guiado (navegador automatizado) em ambiente local de '
          'homologação, clínica de testes "Homologação" (Clínica 1), usuário administrador de teste. '
          'Nenhum dado de produção foi acessado.')

blocks = {pprint.pformat(blocks, width=110)}

render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_{base}.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=False, intro_texto=INTRO, rodape_texto=RODAPE)
render_pdf(blocks, os.path.join(ENTREGA, 'Documentacao_{base}_Simplificado.pdf'),
           TITULO, SUBTITULO, VERSAO, DATA, SHOTS, video_nome=VIDEO_NOME,
           simples=True, intro_texto=INTRO)
render_md(blocks, os.path.join(ENTREGA, 'Documentacao_{base}.md'),
          TITULO, SUBTITULO, VERSAO, DATA, video_nome=VIDEO_NOME, intro_texto=INTRO)
'''
open(os.path.join(pasta, 'scripts', 'doc.py'), 'w', encoding='utf-8').write(out)
print('doc.py criado com', len(blocks), 'blocos')
