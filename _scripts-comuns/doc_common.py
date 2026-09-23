# -*- coding: utf-8 -*-
"""
Módulo comum para gerar documentação de rotinas (PDF completo, PDF simplificado
e Markdown-base) a partir de uma única lista de "blocos", usado por todos os
scripts doc_<rotina>.py.

Tipos de bloco (tuplas):
  ('h1', texto)
  ('h2', texto)
  ('p', texto)                          -- texto pode usar <b>negrito</b>
  ('aviso', texto)
  ('img', nome_arquivo, legenda)        -- nome_arquivo relativo a screenshots_dir
  ('tabela', [(campo, origem, calculado), ...])
  ('tabelagen', [cabecalhos], [linhas], [larguras_cm])
  ('pagebreak',)
"""
import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from PIL import Image as PILImage

COR_HEADER_TABELA = '#2E6DA4'
COR_TITULO_SECAO = '#1B5E8C'

_styles = getSampleStyleSheet()
_styles.add(ParagraphStyle(name='TituloCapa', fontSize=24, leading=28, alignment=TA_CENTER, textColor=colors.HexColor('#1a1a2e'), spaceAfter=10))
_styles.add(ParagraphStyle(name='SubtituloCapa', fontSize=13, leading=18, alignment=TA_CENTER, textColor=colors.HexColor('#555'), spaceAfter=6))
_styles.add(ParagraphStyle(name='H1', fontSize=18, leading=22, textColor=colors.HexColor('#1a1a2e'), spaceBefore=6, spaceAfter=10, fontName='Helvetica-Bold'))
_styles.add(ParagraphStyle(name='H2', fontSize=13, leading=16, textColor=colors.HexColor(COR_TITULO_SECAO), spaceBefore=14, spaceAfter=6, fontName='Helvetica-Bold', keepWithNext=1))
_styles.add(ParagraphStyle(name='Corpo', fontSize=9.5, leading=13, alignment=TA_LEFT, spaceAfter=6))
_styles.add(ParagraphStyle(name='Legenda', fontSize=8.5, leading=11, textColor=colors.HexColor('#666'), alignment=TA_CENTER, spaceBefore=4, spaceAfter=14, fontName='Helvetica-Oblique'))
_styles.add(ParagraphStyle(name='Aviso', fontSize=9.5, leading=13, textColor=colors.HexColor('#8a4b00'), backColor=colors.HexColor('#fff3cd'), borderPadding=8, spaceBefore=6, spaceAfter=10))
_CELL = ParagraphStyle(name='Cell', fontSize=8.3, leading=10.5, fontName='Helvetica')
_CELL_B = ParagraphStyle(name='CellB', fontSize=8.3, leading=10.5, fontName='Helvetica-Bold')


def _cell(txt, bold=False):
    return Paragraph(txt, _CELL_B if bold else _CELL)


def _img_flowable(path, width=16.5 * cm):
    with PILImage.open(path) as im:
        w, h = im.size
    ratio = h / w
    return Image(path, width=width, height=width * ratio)


def render_pdf(blocks, out_path, titulo, subtitulo, versao, data, screenshots_dir,
                video_nome=None, simples=False, intro_texto=None, rodape_texto=None):
    story = []
    story.append(Spacer(1, 4.5 * cm))
    story.append(Paragraph('ClinSis', _styles['SubtituloCapa']))
    story.append(Paragraph(titulo, _styles['TituloCapa']))
    if subtitulo:
        story.append(Spacer(1, 0.4 * cm))
        story.append(Paragraph(subtitulo, _styles['SubtituloCapa']))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(f'Versão {versao} — {data}', _styles['SubtituloCapa']))
    story.append(Spacer(1, 2.4 * cm))
    if intro_texto:
        story.append(Paragraph(intro_texto, _styles['Corpo']))
    if video_nome:
        story.append(Spacer(1, 0.3 * cm))
        story.append(Paragraph(f'Vídeo narrado explicando esta rotina (arquivo separado, '
                                f'entregue junto com este PDF): <b>{video_nome}</b>', _styles['Corpo']))
    story.append(PageBreak())

    for b in blocks:
        tipo = b[0]
        if tipo == 'h1':
            story.append(Paragraph(b[1], _styles['H1']))
        elif tipo == 'h2':
            story.append(Paragraph(b[1], _styles['H2']))
        elif tipo == 'p':
            story.append(Paragraph(b[1], _styles['Corpo']))
        elif tipo == 'aviso':
            story.append(KeepTogether([Paragraph(b[1], _styles['Aviso'])]))
        elif tipo == 'img':
            _, nome, legenda = b
            story.append(KeepTogether([
                _img_flowable(os.path.join(screenshots_dir, nome)),
                Paragraph(legenda, _styles['Legenda']),
            ]))
        elif tipo == 'tabela':
            rows = b[1]
            if simples:
                header = ['Campo / Label na tela', 'De onde vem essa informação']
                data_rows = [[_cell(h, True) for h in header]]
                for campo, origem, _calc in rows:
                    data_rows.append([_cell(campo), _cell(origem)])
                widths = [4 * cm, 13.5 * cm]
            else:
                header = ['Campo / Label na tela', 'Origem no banco de dados (fórmula)', 'Onde é calculado']
                data_rows = [[_cell(h, True) for h in header]]
                for campo, origem, calc in rows:
                    data_rows.append([_cell(campo), _cell(origem), _cell(calc)])
                widths = [4 * cm, 9.5 * cm, 4 * cm]
            t = Table(data_rows, colWidths=widths, repeatRows=1)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(COR_HEADER_TABELA)),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f4f7fb')]),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 5),
                ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            # Tabelas curtas (poucas linhas) ficam inteiras numa página; tabelas
            # longas continuam podendo quebrar (repeatRows=1 repete o cabeçalho).
            # O Spacer depois da tabela viaja junto no KeepTogether para garantir
            # uma folga real antes do próximo bloco (ex.: uma caixa de aviso opaca
            # logo em seguida) — sem isso, o próximo flowable é desenhado colado
            # na tabela e pode visualmente cobrir a última linha dela.
            if len(data_rows) <= 8:
                story.append(KeepTogether([t, Spacer(1, 0.35 * cm)]))
            else:
                story.append(t)
                story.append(Spacer(1, 0.35 * cm))
        elif tipo == 'tabelagen':
            _, headers, rows_g, widths_cm = b
            data_g = [[_cell(h, True) for h in headers]]
            for r in rows_g:
                data_g.append([_cell(c) for c in r])
            tg = Table(data_g, colWidths=[w * cm for w in widths_cm], repeatRows=1)
            tg.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(COR_HEADER_TABELA)),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f4f7fb')]),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 5),
                ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            if len(data_g) <= 8:
                story.append(KeepTogether([tg, Spacer(1, 0.35 * cm)]))
            else:
                story.append(tg)
                story.append(Spacer(1, 0.35 * cm))
        elif tipo == 'pagebreak':
            story.append(PageBreak())

    if not simples and rodape_texto:
        story.append(Spacer(1, 1 * cm))
        story.append(Paragraph(rodape_texto, _styles['Legenda']))

    def rodape(canvas, doc_):
        canvas.saveState()
        canvas.setFont('Helvetica', 7.5)
        canvas.setFillColor(colors.HexColor('#888888'))
        canvas.drawString(1.6 * cm, 1.2 * cm, f'Versão {versao} — {data}')
        canvas.drawRightString(A4[0] - 1.6 * cm, 1.2 * cm, f'Página {doc_.page}')
        canvas.restoreState()

    doc = SimpleDocTemplate(out_path, pagesize=A4,
                             topMargin=1.8 * cm, bottomMargin=1.8 * cm,
                             leftMargin=1.6 * cm, rightMargin=1.6 * cm,
                             title=titulo)
    doc.build(story, onFirstPage=rodape, onLaterPages=rodape)
    print('PDF gerado em', out_path)


def _strip_tags(txt):
    return re.sub(r'<[^>]+>', '', txt)


def render_md(blocks, out_path, titulo, subtitulo, versao, data, video_nome=None, intro_texto=None):
    lines = [f'# {titulo}', '']
    if subtitulo:
        lines += [f'_{subtitulo}_', '']
    lines += [f'Versão {versao} — {data}', '']
    if intro_texto:
        lines += [_strip_tags(intro_texto), '']
    if video_nome:
        lines += [f'Vídeo narrado desta rotina: `{video_nome}`', '']
    lines.append('---')

    for b in blocks:
        tipo = b[0]
        if tipo == 'h1':
            lines += ['', f'# {_strip_tags(b[1])}']
        elif tipo == 'h2':
            lines += ['', f'## {_strip_tags(b[1])}']
        elif tipo == 'p':
            lines += ['', _strip_tags(b[1])]
        elif tipo == 'aviso':
            lines += ['', f'> ⚠️ {_strip_tags(b[1])}']
        elif tipo == 'img':
            _, nome, legenda = b
            lines += ['', f'![{_strip_tags(legenda)}]({nome})', '', f'_{_strip_tags(legenda)}_']
        elif tipo == 'tabela':
            rows = b[1]
            lines += ['', '| Campo / Label na tela | Origem no banco de dados (fórmula) | Onde é calculado |',
                      '|---|---|---|']
            for campo, origem, calc in rows:
                campo_l = _strip_tags(campo).replace('\n', ' ').replace('|', '\\|')
                origem_l = _strip_tags(origem).replace('\n', ' ').replace('|', '\\|')
                calc_l = _strip_tags(calc).replace('\n', ' ').replace('|', '\\|')
                lines.append(f'| {campo_l} | {origem_l} | {calc_l} |')
        elif tipo == 'tabelagen':
            _, headers, rows_g, _w = b
            lines += ['', '| ' + ' | '.join(headers) + ' |', '|' + '---|' * len(headers)]
            for r in rows_g:
                cel = [_strip_tags(c).replace('\n', ' ').replace('|', '\\|') for c in r]
                lines.append('| ' + ' | '.join(cel) + ' |')
        elif tipo == 'pagebreak':
            pass

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print('Markdown gerado em', out_path)
