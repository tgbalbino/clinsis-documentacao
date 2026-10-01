# -*- coding: utf-8 -*-
"""Uso: patch_doc.py <pasta> <versao> <img|-> <legenda|-> <texto_barra|-> [titulo_h2_antes]
Atualiza versão/data (hoje), garante o sys.path de _scripts-comuns e insere a seção
'Barra de ações' (se texto != '-') antes do h2 informado (ou no início dos blocos)."""
import sys, os, re, datetime

pasta, versao, img, leg, texto = sys.argv[1:6]
antes = sys.argv[6] if len(sys.argv) > 6 else None
p = os.path.join(pasta, 'scripts', 'doc.py')
s = open(p, encoding='utf-8').read()
s = re.sub(r"VERSAO = ['\"][^'\"]*['\"]", f"VERSAO = '{versao}'", s)
s = re.sub(r"DATA = ['\"][^'\"]*['\"]", "DATA = '" + datetime.date.today().strftime('%d/%m/%Y') + "'", s)

if '_scripts-comuns' not in s:
    linha = ("sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname("
             "os.path.abspath(__file__)))), '_scripts-comuns'))\n")
    s = s.replace('from doc_common import', linha + 'from doc_common import', 1)

if texto != '-' and "('h2', 'Barra de ações')" not in s:
    bl = f" ('h2', 'Barra de ações'),\n ('p', {texto!r}),\n"
    if img != '-':
        bl += f" ('img', {img!r}, {leg!r}),\n"
    if antes:
        k = s.index(f"('h2', {antes!r})")
        s = s[:k] + bl.lstrip() + ' ' + s[k:]
    else:
        s = s.replace('blocks = [', 'blocks = [' + bl.lstrip(), 1)
open(p, 'w', encoding='utf-8').write(s)
print('doc.py atualizado:', p)
