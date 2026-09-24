# -*- coding: utf-8 -*-
"""Gera os áudios de narração (Google Cloud TTS) para uma rotina.
Uso: python gerar_narracao_google.py <pasta_da_rotina>
A pasta deve conter narracoes.json e vai receber output/audio/*.wav
"""
import base64
import json
import os
import sys
import urllib.request

ROTINA_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(ROTINA_DIR, "output", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

API_KEY = os.environ["GCP_TTS_KEY"]
URL = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"

VOICE = {"languageCode": "pt-BR", "name": "pt-BR-Neural2-C"}
AUDIO_CONFIG = {"audioEncoding": "LINEAR16", "sampleRateHertz": 24000, "speakingRate": 1.05}

with open(os.path.join(ROTINA_DIR, "narracoes.json"), "r", encoding="utf-8") as f:
    itens = json.load(f)

total_chars = 0
for item in itens:
    body = json.dumps({
        "input": {"text": item["texto"]},
        "voice": VOICE,
        "audioConfig": AUDIO_CONFIG,
    }).encode("utf-8")
    total_chars += len(item["texto"])

    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    audio_bytes = base64.b64decode(result["audioContent"])
    out_path = os.path.join(AUDIO_DIR, item["audio"])
    with open(out_path, "wb") as f:
        f.write(audio_bytes)
    print("Gerado:", out_path)

print(f"\nTotal de caracteres enviados nesta execução: {total_chars}")
