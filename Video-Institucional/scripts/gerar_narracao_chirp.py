# -*- coding: utf-8 -*-
"""Gera os áudios do vídeo institucional com a voz Chirp 3 HD (Google). Uso: GCP_TTS_KEY=... python gerar_narracao_chirp.py [Voz]"""
import base64, json, os, sys, urllib.request
VOZ = sys.argv[1] if len(sys.argv) > 1 else 'Charon'
KEY = os.environ['GCP_TTS_KEY']
AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, 'output', 'audio')
os.makedirs(SAIDA, exist_ok=True)
itens = json.load(open(os.path.join(AQUI, 'narracoes.json'), encoding='utf-8'))
total = 0
for it in itens:
    body = json.dumps({"input": {"text": it["texto"]},
                       "voice": {"languageCode": "pt-BR", "name": f"pt-BR-Chirp3-HD-{VOZ}"},
                       "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": 24000}}).encode()
    req = urllib.request.Request(f"https://texttospeech.googleapis.com/v1/text:synthesize?key={KEY}", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    r = json.load(urllib.request.urlopen(req))
    open(os.path.join(SAIDA, it["audio"]), "wb").write(base64.b64decode(r["audioContent"]))
    total += len(it["texto"])
    print("Gerado", it["audio"])
print("Voz:", VOZ, "| caracteres:", total)
