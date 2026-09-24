"""Envia os vídeos de documentação (Documentacao-Entrega) para o YouTube.

Uso:
    python upload_youtube.py --listar                  # mostra o que seria enviado
    python upload_youtube.py                           # envia (não listado, com legenda)
    python upload_youtube.py --privacidade private
    python upload_youtube.py --variante sem-legenda
    python upload_youtube.py --pasta Contas-a-Pagar    # só uma rotina
    python upload_youtube.py --playlist "Documentação ClinSis"

Requisitos:
    pip install google-api-python-client google-auth-oauthlib
    client_secret.json (OAuth "App para computador") nesta pasta.
    NÃO versionar client_secret.json nem token.json.

Cota: cada upload custa ~1600 unidades; o limite padrão é 10.000/dia
(~6 vídeos/dia). O script para ao estourar a cota e retoma no dia seguinte
(vídeos já enviados ficam registrados em enviados.json).
"""
import argparse
import json
import re
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
CLIENT_SECRET = AQUI / "client_secret.json"
TOKEN = AQUI / "token.json"
REGISTRO = AQUI / "enviados.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtube"]
PASTAS_IGNORADAS = {"Marca-ClinSis", "youtube_upload"}


def autenticar():
    cred = None
    if TOKEN.exists():
        cred = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            if not CLIENT_SECRET.exists():
                sys.exit(f"Falta {CLIENT_SECRET.name} (credencial OAuth do Google Cloud).")
            cred = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_SECRET), SCOPES).run_local_server(port=0)
        TOKEN.write_text(cred.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=cred)


def carregar_registro():
    if REGISTRO.exists():
        return json.loads(REGISTRO.read_text(encoding="utf-8"))
    return {}


def salvar_registro(reg):
    REGISTRO.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")


def descobrir_videos(variante, pasta):
    videos = []
    for d in sorted(p for p in RAIZ.iterdir() if p.is_dir()):
        if d.name in PASTAS_IGNORADAS or (pasta and d.name != pasta):
            continue
        for mp4 in sorted(d.glob(f"*-{variante}.mp4")):
            videos.append((d.name, mp4))
    return videos


def titulo_de(nome_pasta):
    return f"ClinSis - {nome_pasta.replace('-', ' ')}"[:100]


def descricao_de(nome_pasta):
    rotina = nome_pasta.replace("-", " ")
    return (f"Documentação em vídeo da rotina \"{rotina}\" do sistema ClinSis.\n"
            "Passo a passo de uso para o usuário final.")


def playlist_id(yt, nome, privacidade):
    if not nome:
        return None
    pl = yt.playlists().list(part="snippet", mine=True, maxResults=50).execute()
    for item in pl.get("items", []):
        if item["snippet"]["title"] == nome:
            return item["id"]
    novo = yt.playlists().insert(
        part="snippet,status",
        body={"snippet": {"title": nome},
              "status": {"privacyStatus": privacidade}}).execute()
    return novo["id"]


def enviar(yt, caminho, titulo, descricao, privacidade):
    body = {
        "snippet": {"title": titulo, "description": descricao,
                    "categoryId": "27", "defaultLanguage": "pt-BR",
                    "defaultAudioLanguage": "pt-BR"},
        "status": {"privacyStatus": privacidade,
                   "selfDeclaredMadeForKids": False},
    }
    media = MediaFileUpload(str(caminho), chunksize=8 * 1024 * 1024, resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"   {int(status.progress() * 100)}%", end="\r")
    return resp["id"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variante", choices=["com-legenda", "sem-legenda"], default="com-legenda")
    ap.add_argument("--privacidade", choices=["private", "unlisted", "public"], default="unlisted")
    ap.add_argument("--pasta", help="nome da pasta da rotina (ex.: Contas-a-Pagar)")
    ap.add_argument("--playlist", help="nome da playlist (criada se não existir)")
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()

    videos = descobrir_videos(a.variante, a.pasta)
    reg = carregar_registro()

    if a.listar:
        for pasta, mp4 in videos:
            marca = "ENVIADO" if str(mp4) in reg else "pendente"
            print(f"[{marca}] {titulo_de(pasta)}  <-  {mp4.name}")
        return

    yt = autenticar()
    pl_id = playlist_id(yt, a.playlist, a.privacidade)

    for pasta, mp4 in videos:
        chave = str(mp4)
        if chave in reg:
            continue
        print(f"Enviando: {titulo_de(pasta)}")
        try:
            vid = enviar(yt, mp4, titulo_de(pasta), descricao_de(pasta), a.privacidade)
        except HttpError as e:
            if e.resp.status == 403 and "quota" in str(e).lower():
                print("Cota diária esgotada. Rode novamente amanhã.")
                break
            raise
        reg[chave] = {"video_id": vid, "url": f"https://youtu.be/{vid}"}
        salvar_registro(reg)
        if pl_id:
            yt.playlistItems().insert(part="snippet", body={"snippet": {
                "playlistId": pl_id,
                "resourceId": {"kind": "youtube#video", "videoId": vid}}}).execute()
        print(f"   ok: https://youtu.be/{vid}")


if __name__ == "__main__":
    main()
