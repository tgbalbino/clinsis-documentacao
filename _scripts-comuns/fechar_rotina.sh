#!/bin/bash
# Copia PDFs/MD/vídeos de <rotina>/scripts/entrega para <rotina>/ e limpa temporários.
R="$1"; cp "$R"/scripts/entrega/*.{pdf,md,mp4} "$R"/ && rm -rf "$R"/scripts/output/clips "$R"/scripts/__pycache__; ls "$R"
