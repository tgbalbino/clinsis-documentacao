# Recortes usados só no vídeo (a partir dos prints inteiros de screenshots/)
from PIL import Image
S = 'screenshots/'
def rec(origem, destino, box):
    Image.open(S + origem).crop(box).save(S + destino)
rec('21-fluxo-caixa.png', '21v-fluxo-por-conta.png', (200, 1670, 1600, 1885))
rec('23-formas-pagamento-clinica.png', '23v-formas-pagamento-clinica.png', (200, 90, 1600, 340))
rec('24-parametro-conta-financeira-checkin.png', '24v-parametro-checkin.png', (200, 90, 1600, 420))
