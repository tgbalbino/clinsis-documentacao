# -*- coding: utf-8 -*-
"""Monta o vídeo narrado de uma rotina a partir de screenshots/ + narracoes.json + output/audio/.
Uso: python montar_video.py <pasta_da_rotina> <nome_arquivo_final.mp4>
"""
import json
import os
import sys
import subprocess
import wave
import imageio_ffmpeg

ROTINA_DIR = os.path.abspath(sys.argv[1])
NOME_FINAL = sys.argv[2] if len(sys.argv) > 2 else "video-narrado.mp4"

SHOTS = os.path.join(ROTINA_DIR, "screenshots")
AUDIO = os.path.join(ROTINA_DIR, "output", "audio")
CLIPS = os.path.join(ROTINA_DIR, "output", "clips")
ENTREGA = os.path.join(ROTINA_DIR, "entrega")
os.makedirs(CLIPS, exist_ok=True)
os.makedirs(ENTREGA, exist_ok=True)

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

with open(os.path.join(ROTINA_DIR, "narracoes.json"), "r", encoding="utf-8") as f:
    itens = json.load(f)

LEAD = 0.4
TAIL = 0.7

clip_paths = []
for item in itens:
    img_path = os.path.join(SHOTS, item["imagem"])
    audio_path = os.path.join(AUDIO, item["audio"])
    clip_path = os.path.join(CLIPS, item["audio"].replace(".wav", ".mp4"))

    with wave.open(audio_path, "rb") as w:
        dur = w.getnframes() / w.getframerate()
    total_dur = dur + LEAD + TAIL

    filtro_audio = f"adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad=pad_dur={TAIL}"
    cmd = [
        FFMPEG, "-y",
        "-loop", "1", "-i", img_path,
        "-i", audio_path,
        "-filter_complex", f"[1:a]{filtro_audio}[a]",
        "-map", "0:v", "-map", "[a]",
        "-vf", "scale=1600:1000:force_original_aspect_ratio=decrease,pad=1600:1000:(ow-iw)/2:(oh-ih)/2:color=0xF4F6F9,format=yuv420p",
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-t", f"{total_dur:.2f}",
        "-r", "15",
        clip_path,
    ]
    print("Gerando", os.path.basename(clip_path), f"({total_dur:.1f}s)")
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    clip_paths.append(clip_path)

concat_list = os.path.join(CLIPS, "concat.txt")
with open(concat_list, "w", encoding="utf-8") as f:
    for p in clip_paths:
        f.write(f"file '{p}'\n")

FINAL = os.path.join(ENTREGA, NOME_FINAL)
cmd_concat = [
    FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
    "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", "-r", "15",
    FINAL,
]
print("Concatenando clipes finais...")
subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Vídeo final:", FINAL)
