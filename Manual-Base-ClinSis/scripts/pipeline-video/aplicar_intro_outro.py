# -*- coding: utf-8 -*-
"""Junta intro.mp4 + vídeo principal + outro.mp4 num único arquivo final,
escalando tudo para a resolução do vídeo principal.
Uso: python aplicar_intro_outro.py <intro.mp4> <principal.mp4> <outro.mp4> <saida.mp4>
"""
import re
import subprocess
import sys
import imageio_ffmpeg

INTRO, PRINCIPAL, OUTRO, SAIDA = sys.argv[1:5]
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def resolucao(path):
    r = subprocess.run([FFMPEG, "-i", path], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    m = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", r.stderr)
    return int(m.group(1)), int(m.group(2))


W, H = resolucao(PRINCIPAL)
print(f"Resolução do vídeo principal: {W}x{H}")

filtro = (
    f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps=15,format=yuv420p,setsar=1[v0];"
    f"[1:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps=15,format=yuv420p,setsar=1[v1];"
    f"[2:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps=15,format=yuv420p,setsar=1[v2];"
    f"[0:a]aresample=44100,aformat=channel_layouts=stereo[a0];"
    f"[1:a]aresample=44100,aformat=channel_layouts=stereo[a1];"
    f"[2:a]aresample=44100,aformat=channel_layouts=stereo[a2];"
    f"[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]"
)

cmd = [
    FFMPEG, "-y",
    "-i", INTRO, "-i", PRINCIPAL, "-i", OUTRO,
    "-filter_complex", filtro,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-c:a", "aac", "-b:a", "160k",
    SAIDA,
]
subprocess.run(cmd, check=True)
print("Gerado:", SAIDA)
