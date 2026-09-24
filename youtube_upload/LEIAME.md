# Envio dos vídeos para o YouTube

1. Google Cloud Console → criar projeto → ativar **YouTube Data API v3**.
2. Tela de consentimento OAuth (tipo Externo; adicione seu e-mail como usuário de teste).
3. Credenciais → **ID do cliente OAuth → App para computador** → baixar como `client_secret.json` nesta pasta.
4. `pip install google-api-python-client google-auth-oauthlib`
5. `python upload_youtube.py --listar` para conferir; depois `python upload_youtube.py --playlist "Documentação ClinSis"`.

Notas:
- Padrão: vídeos **não listados**, variante **com-legenda**.
- Cota: ~6 vídeos/dia (1600 unidades cada, limite 10.000). O script retoma de onde parou (`enviados.json`).
- Vídeos de projetos de API não auditados podem ser forçados a privado pelo YouTube; solicite auditoria de conformidade para publicar como não listado/público.
- Nunca versionar `client_secret.json` nem `token.json`.
