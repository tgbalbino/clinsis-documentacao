# -*- coding: utf-8 -*-
"""Remonta os dois vídeos de uma rotina (com e sem legenda) com abertura/encerramento da marca.
Usa os áudios que já estão em scripts/output/audio (gere antes os que mudaram com
pipeline-video/gerar_narracao_google.py) e os prints de scripts/screenshots.

Uso: python refazer_video.py <pasta_scripts_da_rotina> "<Título da abertura>" <slug>
Saída: <pasta_scripts>/entrega/video-<slug>-com-legenda.mp4 e video-<slug>-sem-legenda.mp4
"""
import os
import subprocess
import sys

SCRIPTS, TITULO, SLUG = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3]
PIPE = os.path.join(SCRIPTS, "pipeline-video")
MARCA = os.path.join(PIPE, "marca")
ENTREGA = os.path.join(SCRIPTS, "entrega")
PY = sys.executable


def run(*args, cwd=None):
    print(">", " ".join(os.path.basename(a) if os.path.isabs(a) else a for a in args))
    subprocess.run([PY, "-X", "utf8", *args], check=True, cwd=cwd)


# 1. Abertura com o título da rotina + encerramento
run(os.path.join(MARCA, "gerar_frames.py"), TITULO, cwd=MARCA)
run(os.path.join(MARCA, "montar_intro_outro.py"), cwd=MARCA)

# 2. Vídeo principal (prints + narração) e legendas sincronizadas
principal = f"_principal-{SLUG}.mp4"
run(os.path.join(PIPE, "montar_video.py"), SCRIPTS, principal)
run(os.path.join(PIPE, "gerar_legendas.py"), SCRIPTS)
principal = os.path.join(ENTREGA, principal)
principal_leg = principal.replace(".mp4", "-leg.mp4")
run(os.path.join(PIPE, "queimar_legendas.py"), principal, os.path.join(SCRIPTS, "output", "legendas.srt"), principal_leg)

# 3. Intro + principal + outro nas duas versões
intro, outro = os.path.join(MARCA, "intro.mp4"), os.path.join(MARCA, "outro.mp4")
run(os.path.join(PIPE, "aplicar_intro_outro.py"), intro, principal, outro, os.path.join(ENTREGA, f"video-{SLUG}-sem-legenda.mp4"))
run(os.path.join(PIPE, "aplicar_intro_outro.py"), intro, principal_leg, outro, os.path.join(ENTREGA, f"video-{SLUG}-com-legenda.mp4"))
for p in (principal, principal_leg):
    os.remove(p)
print("Vídeos prontos em", ENTREGA)
