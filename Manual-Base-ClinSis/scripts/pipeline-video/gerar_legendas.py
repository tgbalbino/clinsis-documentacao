# -*- coding: utf-8 -*-
"""Gera um arquivo .srt sincronizado com a narração de uma rotina, usando a
mesma linha do tempo (LEAD/TAIL) do montar_video.py.
Uso: python gerar_legendas.py <pasta_da_rotina>
"""
import json
import os
import re
import sys
import wave

ROTINA_DIR = os.path.abspath(sys.argv[1])
AUDIO_DIR = os.path.join(ROTINA_DIR, "output", "audio")

LEAD = 0.4
TAIL = 0.7
MAX_CHARS_LINHA = 84  # quebra frases longas em blocos menores de legenda

with open(os.path.join(ROTINA_DIR, "narracoes.json"), "r", encoding="utf-8") as f:
    itens = json.load(f)


def dividir_em_blocos(texto):
    """Quebra o texto em frases e, se ainda ficarem longas, em blocos por vírgula."""
    frases = re.split(r'(?<=[.!?])\s+', texto.strip())
    blocos = []
    for frase in frases:
        if len(frase) <= MAX_CHARS_LINHA:
            blocos.append(frase)
            continue
        partes = re.split(r'(?<=,)\s+', frase)
        atual = ''
        for p in partes:
            candidato = (atual + ' ' + p).strip() if atual else p
            if len(candidato) > MAX_CHARS_LINHA and atual:
                blocos.append(atual)
                atual = p
            else:
                atual = candidato
        if atual:
            blocos.append(atual)
    return blocos


def fmt_srt(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


linhas_srt = []
idx = 1
cursor = 0.0  # tempo acumulado (início de cada clipe) na linha do tempo final

for item in itens:
    audio_path = os.path.join(AUDIO_DIR, item["audio"])
    with wave.open(audio_path, "rb") as w:
        dur_audio = w.getnframes() / w.getframerate()
    total_clip = dur_audio + LEAD + TAIL

    blocos = dividir_em_blocos(item["texto"])
    total_chars = sum(len(b) for b in blocos) or 1
    t0 = cursor + LEAD
    for bloco in blocos:
        dur_bloco = dur_audio * (len(bloco) / total_chars)
        t1 = t0 + dur_bloco
        linhas_srt.append(f"{idx}\n{fmt_srt(t0)} --> {fmt_srt(t1)}\n{bloco.strip()}\n")
        idx += 1
        t0 = t1

    cursor += total_clip

out_path = os.path.join(ROTINA_DIR, "output", "legendas.srt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(linhas_srt))
print("Legendas geradas em", out_path)
