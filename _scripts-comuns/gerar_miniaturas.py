# -*- coding: utf-8 -*-
import json
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = r"C:\Projetos\W_Clinica\Documentacao-Entrega"
MARCA = r"C:\Users\Dev\AppData\Local\Temp\claude\c--Projetos-W-Clinica-ApiClinica\9f6f67c6-bb27-4e65-be84-5877a44fa848\scratchpad\marca"
DEST = r"C:\Projetos\W_Clinica\Videos-YouTube"
os.makedirs(DEST, exist_ok=True)
W, H = 1280, 720
FONTE_B = "C:/Windows/Fonts/segoeuib.ttf"
FONTE_S = "C:/Windows/Fonts/seguisb.ttf"
FUNDO_A, FUNDO_B = (10, 22, 36), (26, 62, 96)
DESTAQUE = (94, 168, 232)

# (n, arquivo do video sem prefixo, pasta, titulo curto, categoria)
ITENS = [
    (1, "video-manual-base-clinsis", "Manual-Base-ClinSis", "Manual Base do ClinSis", "PRIMEIROS PASSOS"),
    (2, "video-cadastro-plano-de-contas", "Cadastro-Plano-de-Contas", "Plano de Contas", "FINANCEIRO"),
    (3, "video-cadastro-centro-de-custo", "Cadastro-Centro-de-Custo", "Centro de Custo", "FINANCEIRO"),
    (4, "video-conta-financeira", "Conta-Financeira", "Conta Financeira", "FINANCEIRO"),
    (5, "video-especialidade", "Cadastro-de-Especialidades", "Especialidades", "CADASTROS"),
    (6, "video-cadastro-servicos", "Cadastro-de-Servicos", "Serviços", "CADASTROS"),
    (7, "video-tabela-preco-cobranca", "Tabela-de-Precos-Cobranca", "Tabela de Valores: Cobrança", "CADASTROS"),
    (8, "video-tabela-preco-pagamento", "Tabela-de-Precos-Pagamento", "Tabela de Valores: Pagamento", "CADASTROS"),
    (9, "video-prontuario-configuracao", "Prontuario-Configuracao", "Prontuário: Configuração", "PRONTUÁRIO"),
    (10, "video-layout-contrato", "Layout-de-Contrato", "Layout de Contrato", "CONTRATOS"),
    (11, "video-caixa", "Modulo-de-Caixa", "Módulo de Caixa", "FINANCEIRO"),
    (12, "video-contas-a-receber", "Contas-a-Receber", "Contas a Receber", "FINANCEIRO"),
    (13, "video-contas-a-pagar", "Contas-a-Pagar", "Contas a Pagar", "FINANCEIRO"),
    (14, "video-contas-recorrentes", "Contas-Recorrentes", "Contas Recorrentes", "FINANCEIRO"),
    (15, "video-movimentos-financeiros", "Movimentos-Financeiros", "Movimentos Financeiros", "FINANCEIRO"),
    (16, "video-checkin", "Checkin", "Checkin de Paciente", "ATENDIMENTO"),
    (17, "video-prontuario-uso", "Prontuario-Uso", "Prontuário: Uso pelo Profissional", "PRONTUÁRIO"),
    (18, "video-contrato", "Contrato", "Contrato", "CONTRATOS"),
    (19, "video-contrato-d4sign", "Contrato-D4Sign", "Contrato com Assinatura Digital", "CONTRATOS"),
    (20, "video-cobranca-de-paciente", "Cobranca-de-Paciente", "Cobrança de Paciente", "COBRANÇA E PAGAMENTO"),
    (21, "video-pagamento-profissionais", "Pagamento-de-Profissionais", "Pagamento de Profissionais", "COBRANÇA E PAGAMENTO"),
    (22, "video-dashboard-agenda", "Dashboard-de-Agenda", "Dashboard de Agenda", "PAINÉIS"),
    (23, "video-prontuario-auditoria", "Prontuario-Auditoria", "Prontuário: Auditoria", "PRONTUÁRIO"),
    (24, "video-dashboard-financeiro-e-fluxo-caixa", "Dashboard-Financeiro-e-Fluxo-Caixa", "Dashboard Financeiro e Fluxo de Caixa", "PAINÉIS"),
]
TOTAL = len(ITENS)


def fundo():
    y = np.linspace(0, 1, H)[:, None]
    x = np.linspace(0, 1, W)[None, :]
    t = np.clip(0.55 * y + 0.45 * x, 0, 1)
    a = np.array(FUNDO_A, dtype=float)
    b = np.array(FUNDO_B, dtype=float)
    arr = (a[None, None, :] * (1 - t[..., None]) + b[None, None, :] * t[..., None]).astype("uint8")
    return Image.fromarray(arr, "RGB").convert("RGBA")


def captura(pasta):
    cands = [os.path.join(RAIZ, pasta, "scripts", "narracoes.json"), os.path.join(RAIZ, pasta, "narracoes.json")]
    for c in cands:
        if os.path.exists(c):
            try:
                itens = json.load(open(c, encoding="utf-8"))
            except Exception:
                continue
            for it in itens[:3]:
                nome = it.get("imagem")
                if not nome:
                    continue
                for base in (os.path.join(RAIZ, pasta, "scripts"), os.path.join(RAIZ, pasta, "scripts", "screenshots"), os.path.join(RAIZ, pasta)):
                    p = os.path.join(base, nome)
                    if os.path.exists(p):
                        return p
    return None


def quebrar(draw, texto, fonte, largura):
    palavras, linhas, atual = texto.split(), [], ""
    for p in palavras:
        teste = (atual + " " + p).strip()
        if draw.textlength(teste, font=fonte) <= largura:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


def arredondar(img, raio):
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, img.size[0] - 1, img.size[1] - 1], raio, fill=255)
    img = img.convert("RGBA")
    img.putalpha(m)
    return img


for n, video, pasta, titulo, categoria in ITENS:
    img = fundo()
    d = ImageDraw.Draw(img)

    d = ImageDraw.Draw(img)

    # logo + "Treinamento" (topo esquerdo)
    logo = Image.open(os.path.join(MARCA, "logo_horizontal_branco.png")).convert("RGBA")
    lw = 250
    logo = logo.resize((lw, int(logo.size[1] * lw / logo.size[0])), Image.LANCZOS)
    img.paste(logo, (56, 44), logo)

    # numero gigante (lado direito)
    txt = f"{n:02d}"
    f_num = ImageFont.truetype(FONTE_B, 430)
    bb = d.textbbox((0, 0), txt, font=f_num)
    nx = 1240 - (bb[2] - bb[0]) - bb[0]
    ny = 170 - bb[1]
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(camada).text((nx + 6, ny + 8), txt, font=f_num, fill=(0, 0, 0, 120))
    camada = camada.filter(ImageFilter.GaussianBlur(10))
    img = Image.alpha_composite(img, camada)
    d = ImageDraw.Draw(img)
    d.text((nx, ny), txt, font=f_num, fill=DESTAQUE)

    # categoria (pill)
    f_cat = ImageFont.truetype(FONTE_S, 30)
    tw = d.textlength(categoria, font=f_cat)
    d.rounded_rectangle([58, 330, 58 + tw + 44, 384], 26, fill=(255, 255, 255, 235))
    d.text((80, 333), categoria, font=f_cat, fill=(16, 42, 68))

    # titulo (auto-ajuste)
    area_w = 610
    tam = 88
    while tam > 44:
        f_t = ImageFont.truetype(FONTE_B, tam)
        linhas = quebrar(d, titulo, f_t, area_w)
        if len(linhas) <= 3 and len(linhas) * int(tam * 1.12) <= 235 and all(d.textlength(l, font=f_t) <= area_w for l in linhas):
            break
        tam -= 4
    y = 405
    for l in linhas:
        d.text((56, y), l, font=f_t, fill=(255, 255, 255))
        y += int(tam * 1.12)

    # rodape
    f_r = ImageFont.truetype(FONTE_S, 28)
    d.text((58, H - 58), f"TREINAMENTO CLINSIS  •  {n} DE {TOTAL}", font=f_r, fill=(170, 200, 230))

    nome_saida = f"{n:02d}_{video}-miniatura.jpg"
    img.convert("RGB").save(os.path.join(DEST, nome_saida), "JPEG", quality=92)
    print("ok", nome_saida,)
