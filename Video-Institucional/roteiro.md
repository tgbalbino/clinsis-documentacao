# Vídeo institucional ClinSis (aprox. 105 s) - roteiro aprovado em 02/10/2026

Público: gestores de clínicas e consultórios (nunca usar o termo "pequenas").
Tom: calmo e acolhedor; o nome ClinSis só aparece nos blocos 4 e 6.
Voz: Google Cloud TTS pt-BR-Neural2-C (mesma dos outros vídeos). Endereço final: https://www.clinsis.com.br/sobre

Personagens fictícias (ilustração, não depoimento): Marina (recepcionista) e Dr. Paulo (gestor).
Telas: SOMENTE dados fictícios de demonstração (LGPD). Sem números de ganho/redução (não há dado real).

| # | Tempo | Narração (ver scripts/narracoes.json) | Imagem |
|---|---|---|---|
| 1 | 0:00-0:15 | Segunda-feira, 7h40... | Ilustração: recepção, agenda de papel, telefone |
| 2 | 0:15-0:30 | Cada falta é um horário perdido... | Ilustração/colagem: planilhas, Dr. Paulo pensativo |
| 3 | 0:30-0:52 | E se a clínica soubesse... | Tela: confirmação do paciente (celular) |
| 4 | 0:52-1:30 | Agenda, faturamento, financeiro, relatórios | Telas: agenda, faturamento, financeiro, dashboard |
| 5 | 1:30-1:52 | A recepção respira... | Ilustração: Marina e Dr. Paulo, clínica organizada |
| 6 | 1:52-2:00 | ClinSis. Gestão para clínicas e consultórios... | Logo + endereço |

## Imagens a produzir
- scripts/ilustracoes/01-recepcao-segunda-feira.png
- scripts/ilustracoes/02-custo-da-desorganizacao.png
- scripts/ilustracoes/05-clinica-organizada.png
- scripts/ilustracoes/06-tela-final-clinsis.png (logo + clinsis.com.br/sobre; usar Marca-ClinSis)
- scripts/screenshots/10 a 14 (capturas do sistema com dados fictícios)
Estilo das ilustrações: desenho vetorial limpo, cores da marca, sem rostos fotorrealistas.

## Pipeline (igual aos outros vídeos)
1. Capturas: node scripts/capture.js (modelo: WhatsApp/scripts/capture.js, usa _scripts-comuns/cap_common.js)
2. Voz: python _scripts-comuns/pipeline-video/gerar_narracao_google.py Video-Institucional/scripts  (precisa de GCP_TTS_KEY)
3. Montagem: montar_video.py, aplicar_intro_outro.py, legendas (gerar_legendas.py / queimar_legendas.py)
4. Publicar no YouTube (youtube_upload) e trocar o link em FrontClinica/.../sobre-clinsis.component.ts
