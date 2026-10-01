#!/bin/bash
# Uso: rodar_rotina.sh <pasta> <NomeBase> <slug> "<Título da abertura>"   (usa GCP_TTS_KEY)
cd "$1/scripts" || exit 1
python -X utf8 doc.py >/dev/null || { echo "FALHA doc.py em $1"; exit 1; }
python -X utf8 ../../_scripts-comuns/pipeline-video/gerar_narracao_google.py . >/dev/null || { echo "FALHA narração em $1"; exit 1; }
python -X utf8 ../../_scripts-comuns/refazer_video.py . "$4" "$3" >/dev/null 2>&1 || { echo "FALHA vídeo em $1"; exit 1; }
cd ../.. && _scripts-comuns/fechar_rotina.sh "$1" >/dev/null && echo "OK $1"
