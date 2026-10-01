# -*- coding: utf-8 -*-
"""Grava (hardsub) um arquivo .srt no vídeo.
Uso: python queimar_legendas.py <entrada.mp4> <legendas.srt> <saida.mp4>
"""
import subprocess
import sys
import imageio_ffmpeg

ENTRADA, SRT, SAIDA = sys.argv[1:4]
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

srt_ffmpeg = SRT.replace("\\", "/").replace(":", "\\:")
estilo = (
    "FontName=Segoe UI,Bold=1,FontSize=15,PrimaryColour=&H0000FFFF,"
    "OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=1,MarginV=28"
)

cmd = [
    FFMPEG, "-y", "-i", ENTRADA,
    "-vf", f"subtitles='{srt_ffmpeg}':force_style='{estilo}'",
    "-c:v", "libx264", "-c:a", "copy",
    SAIDA,
]
subprocess.run(cmd, check=True)
print("Gerado:", SAIDA)
