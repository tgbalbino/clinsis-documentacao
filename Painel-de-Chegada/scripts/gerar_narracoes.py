# -*- coding: utf-8 -*-
"""Gera narracoes.json (texto de cada trecho do vídeo "Painel de Chegada"). Rode: python gerar_narracoes.py"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

itens = [
    ("07-tv-nova-chegada.png",
     "Este treinamento mostra o Painel de chegada do ClinSis. Ele mostra numa TV da clínica o nome do profissional e do "
     "paciente que acabou de chegar, com um aviso sonoro, e também avisa o profissional no próprio sistema. Quando não "
     "há chegada, a TV mostra a data, a hora, o clima e os aniversariantes do dia."),
    ("01-configuracao.png",
     "O módulo é liberado por clínica na Área do Administrador e vem desligado. Depois, o administrador abre Tabelas "
     "Auxiliares, Painel de chegada, ativa o módulo e ajusta a duração do aviso, o tempo de cada cartão, o som e o "
     "volume, se o nome do paciente aparece só com a inicial ou completo, e quantas TVs podem ser autorizadas. Embaixo, "
     "a presença da TV informa se há alguma conectada."),
    ("02-agenda-sem-tv.png",
     "Se o painel estiver ligado e nenhuma TV estiver conectada, a agenda mostra um aviso amarelo: Painel de chegada "
     "indisponível, os avisos não serão exibidos, com o link Como conectar a TV."),
    ("03-tv-qr.png",
     "Na TV, abra o endereço do sistema acrescido de barra painel hífen chegada, em tela cheia. A tela pede para "
     "autorizar o dispositivo, com um código de resposta rápida e um código de seis dígitos."),
    ("04-autorizar.png",
     "Com o celular da recepção, logado como administrador, leia o código e clique em Autorizar."),
    ("05-tv-aguardando.png",
     "A TV passa para Aguardando chegadas. Clique uma vez na tela da TV para liberar o som, porque o navegador só toca "
     "som depois de um clique."),
    ("06-agenda-avisar.png",
     "Para avisar uma chegada pela agenda, abra o menu de ações da linha do paciente e clique em Avisar chegada. O botão "
     "só aparece para atendimentos de hoje. Também é possível avisar pelo check-in: ao confirmar, o sistema pergunta se "
     "deseja avisar o profissional, e basta marcar os horários e clicar em Avisar agora."),
    ("07-tv-nova-chegada.png",
     "Na TV aparece Nova chegada, com o nome do profissional em destaque e o do paciente abaixo, uma barra de tempo e o "
     "som. A chamada anterior fica no canto da tela. O profissional logado também vê a mensagem de que o paciente foi "
     "chamado, e pode ativar as notificações do navegador para receber o aviso mesmo com o sistema minimizado."),
    ("08-chamadas.png",
     "Para conferir, na agenda, em Mais opções, Ver chamadas do painel. A lista mostra o profissional, o paciente, a "
     "hora da chamada, quando expira e a situação. Sem chamadas, o sistema mostra os aniversariantes do dia, e a TV "
     "também os exibe com a mensagem Parabéns."),
]

saida = [{"audio": f"{i:02d}.wav", "imagem": img, "texto": txt} for i, (img, txt) in enumerate(itens, 1)]
with open(os.path.join(BASE, "narracoes.json"), "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=1)
print(len(saida), "trechos")
