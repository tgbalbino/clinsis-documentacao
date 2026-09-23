# Site de documentação do ClinSis (MkDocs)

Site estático que indexa todas as rotinas documentadas (PDFs completo/simplificado e vídeo de cada
uma), organizado por área/categoria, com busca. Gerado com [MkDocs](https://www.mkdocs.org/) +
tema [Material](https://squidfunk.github.io/mkdocs-material/) — grátis, open source.

## Estrutura

- `docs/` — páginas em Markdown (uma por rotina) + os PDFs copiados em `docs/assets/<Rotina>/`.
  **Não edite `docs/` diretamente** — ele é gerado automaticamente por `scripts/gerar_site_docs.py`
  a partir das pastas em `Documentacao-Entrega/<Rotina>/`. Qualquer alteração manual em `docs/` se
  perde no próximo regeneramento.
- `mkdocs.yml` — configuração do site (também gerada automaticamente; o menu/nav é montado a partir
  da lista `ROTINAS` dentro do script).
- `publicado/` — o site já "compilado" em HTML puro, pronto para publicar em qualquer lugar (é o
  que se gera com `mkdocs build`).
- `scripts/gerar_site_docs.py` — script que gera tudo isso. Rode de novo sempre que uma rotina nova
  for documentada, ou um PDF for atualizado.

## Como regenerar o site depois de documentar uma rotina nova

1. Adicione a nova rotina na lista `ROTINAS` no topo de `scripts/gerar_site_docs.py`
   (pasta de origem, categoria, e título do menu).
2. Rode:
   ```
   python scripts/gerar_site_docs.py
   ```
3. Rebuilde o HTML final:
   ```
   python -m mkdocs build
   ```
   (dentro da pasta `site/`; instala com `pip install mkdocs mkdocs-material` se ainda não tiver).

## Como conferir localmente antes de publicar

```
python -m mkdocs serve
```
Abre em `http://127.0.0.1:8000` com recarregamento automático ao editar.

## Como adicionar os links do YouTube

Depois de subir cada vídeo no canal, edite o dicionário `YOUTUBE_LINKS` no topo de
`scripts/gerar_site_docs.py`:

```python
YOUTUBE_LINKS = {
    "Checkin": ("https://youtu.be/ID_COM_LEGENDA", "https://youtu.be/ID_SEM_LEGENDA"),
    ...
}
```

A chave é o nome da pasta da rotina (igual à pasta em `Documentacao-Entrega/`). Depois rode os dois
comandos do passo anterior para regenerar e rebuildar.

## Como publicar (colocar o link no sistema)

Três opções, todas gratuitas:

1. **GitHub Pages** (se o projeto já usa GitHub): rode `python -m mkdocs gh-deploy` dentro da pasta
   `site/` — publica o conteúdo de `publicado/` direto num link tipo
   `https://<usuario>.github.io/<repo>/`. É o caminho mais simples de manter.
2. **Servir pelo próprio IIS/servidor da clínica**: copie o conteúdo da pasta `publicado/` para
   qualquer pasta servida como site estático (ex.: um subcaminho do IIS, tipo `/docs`). Não precisa
   de banco de dados nem backend — é só HTML/CSS/JS puro.
3. **Qualquer host de arquivo estático grátis** (Netlify, Vercel, Cloudflare Pages): arrasta a pasta
   `publicado/` e pronto.

Depois de publicado, adicione um item de menu no FrontClinica (sidebar) apontando para a URL
pública — um link `<a href="URL" target="_blank">Documentação</a>` simples, sem precisar de rota
Angular nova.

## Observação sobre os screenshots

Cada página do site tem um resumo + os links de PDF (que já têm as capturas de tela reais,
formatadas). O texto completo do manual também aparece na página, mas sem as imagens (elas só
existem no PDF) — os arquivos de captura de tela originais não fazem parte da entrega final, só o
PDF já renderizado com elas.
