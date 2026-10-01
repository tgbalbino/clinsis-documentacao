# Oculta identificadores reais (WABA, Phone Number ID, números de telefone) nos prints antes de gerar o manual.
from PIL import Image, ImageDraw, ImageFont
import os
S = 'screenshots/'
try: F = ImageFont.truetype('arial.ttf', 15)
except Exception: F = None
def cobrir(nome, caixas, rotulo='oculto'):
    p = S + nome
    if not os.path.exists(p): return
    im = Image.open(p).convert('RGB'); d = ImageDraw.Draw(im)
    for (x1, y1, x2, y2) in caixas:
        d.rectangle((x1, y1, x2, y2), fill=(226, 228, 232), outline=(190, 192, 198))
        d.text((x1 + 8, y1 + (y2 - y1 - 15) // 2), rotulo, fill=(110, 112, 120), font=F)
    im.save(p)
ids = [(272, 546, 688, 580), (707, 546, 1123, 580), (1142, 546, 1558, 580)]
cobrir('03-meta-configuracao.png', ids)
cobrir('05-meta-filtros.png', ids)
cobrir('06-meta-simulacao.png', ids + [(1050, 1480, 1195, 1545)])
cobrir('04-meta-ver-texto.png', [(866, 185, 1015, 207)])
cobrir('09-meta-mensagens.png', [(583, 283, 685, 760)])
cobrir('01-manual-lembretes-do-dia.png', [(800, 266, 925, 326)], '')
cobrir('04-meta-ver-texto.png', [(268, 546, 400, 582), (1200, 546, 1560, 582)], '')
