# -*- coding: utf-8 -*-
"""Gera narracoes.json (texto de cada trecho do vídeo "Totem de Check-in"). Rode: python gerar_narracoes.py"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

itens = [
    ("04-totem-inicio.png",
     "Este treinamento mostra o Totem de check-in do ClinSis. É a tela da portaria onde o paciente, ou o responsável por "
     "ele, registra a chegada sozinho, sem usuário e senha, informando o CPF e a data de nascimento. A recepção vê o aviso "
     "na agenda. O totem só avisa a chegada: o check-in com pagamento continua sendo feito pela recepção."),
    ("01-configuracao.png",
     "O recurso vem desligado. O administrador abre Tabelas Auxiliares, Totem de check-in, marca Ativar o totem nesta "
     "clínica e ajusta, se precisar, a janela de horário: por padrão, o paciente pode registrar a chegada até sessenta "
     "minutos antes e até trinta minutos depois do horário marcado. Também dá para definir a inatividade, a validade da "
     "autorização, as tentativas erradas antes do bloqueio e a mensagem para Plano Próprio. Depois, é só salvar."),
    ("02-totem-qr.png",
     "Na portaria, abra o endereço do sistema acrescido de barra totem. O equipamento mostra Autorize este totem, com um "
     "código de resposta rápida e um código de seis dígitos."),
    ("03-autorizar.png",
     "Com o administrador logado, leia o código com o celular. Dê um nome ao totem, por exemplo, Totem da recepção, e "
     "clique em Autorizar totem. O código vale por cinco minutos."),
    ("03b-autorizado.png",
     "Pronto, o totem foi autorizado e essa página já pode ser fechada. Em poucos segundos o equipamento troca para a "
     "tela de boas-vindas."),
    ("05-totem-cpf.png",
     "O paciente toca em Registrar chegada e digita o CPF no teclado da tela. Atenção: o CPF e a data de nascimento são "
     "sempre da pessoa que está diante do totem. Se quem chegou é o responsável pelo paciente, ele digita os próprios "
     "dados, não os do paciente."),
    ("06-totem-nascimento.png",
     "Em seguida, a data de nascimento, com oito números: dia, mês e ano. Na tela, nunca aparece o CPF, e os dados "
     "digitados são apagados depois da identificação."),
    ("07-totem-itens.png",
     "O totem mostra os atendimentos de hoje. O paciente confere o horário e toca em Confirmar chegada. O responsável "
     "com mais de um dependente vê o nome de cada paciente."),
    ("08-totem-resultado.png",
     "Chegada registrada. Aguarde ser chamado. A tela volta ao início sozinha. Se o paciente chegar cedo demais, ou depois "
     "da janela, o totem avisa e orienta procurar a recepção. Paciente de Plano Próprio recebe a mensagem configurada "
     "para seguir à recepção."),
    ("09-agenda-chegou.png",
     "Na agenda do dia, antes do nome do paciente, aparece um selo verde com o horário da chegada. Assim a recepção sabe "
     "quem já está na clínica. A tela se atualiza sozinha a cada trinta segundos."),
    ("10-configuracao-totens.png",
     "Na tela do totem, a lista Totens autorizados mostra cada equipamento, a validade e o último acesso. O botão "
     "Revogar desliga um equipamento na hora. Para parar de usar o totem na clínica inteira, desmarque Ativar o totem "
     "nesta clínica e salve. Para o responsável ser reconhecido, ele precisa estar cadastrado no paciente, com CPF, "
     "data de nascimento e vínculo ativo."),
]

saida = [{"audio": f"{i:02d}.wav", "imagem": img, "texto": txt} for i, (img, txt) in enumerate(itens, 1)]
with open(os.path.join(BASE, "narracoes.json"), "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=1)
print(len(saida), "trechos")
