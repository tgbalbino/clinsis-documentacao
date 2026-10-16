# -*- coding: utf-8 -*-
"""Gera narracoes.json (texto de cada trecho do vídeo "Revisão Cadastral de Pacientes"). Rode: python gerar_narracoes.py"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

itens = [
    ("02-lista.png",
     "Este treinamento mostra a Revisão cadastral de pacientes do ClinSis. O objetivo é manter o endereço e o contato "
     "dos pacientes atualizados. Primeiro, o administrador do sistema libera o módulo para a clínica, na Área do "
     "Administrador, no cadastro da clínica, e os usuários entram de novo no sistema. Com o módulo ligado, aparece no "
     "menu Paciente a opção Revisão cadastral. A lista mostra os pacientes ativos que precisam de revisão, do mais "
     "antigo para o mais recente, com o motivo de cada um. No canto, o prazo em vigor: trezentos e sessenta e cinco "
     "dias, e o total de pacientes pendentes."),
    ("03-filtro-endereco.png",
     "Um paciente precisa de revisão em três situações: quando a última revisão passou do prazo ou nunca foi feita, "
     "selo amarelo; quando o endereço está incompleto, selo vermelho; ou quando não tem nenhum celular, telefone ou "
     "e-mail, também em vermelho. Endereço incompleto e falta de contato valem mesmo dentro do prazo. Use o filtro "
     "Motivo para trabalhar um grupo de cada vez. Aqui, apenas o paciente com o endereço faltando."),
    ("03b-filtro-contato.png",
     "E aqui, os pacientes sem celular, telefone ou e-mail. Também é possível buscar pelo nome. O botão com o lápis, em "
     "cada linha, abre o cadastro do paciente."),
    ("05-parametro.png",
     "O prazo é um parâmetro da clínica. Em Tabelas Auxiliares, Parâmetros, o parâmetro Revisão Cadastral Dias define de "
     "quantos em quantos dias o cadastro deve ser revisado. O padrão é trezentos e sessenta e cinco dias, e aceita de "
     "trinta a mil oitocentos e vinte e cinco. Clique no lápis amarelo para alterar."),
    ("06-agenda-selo.png",
     "Na agenda, o paciente que precisa de revisão ganha um pequeno cartão amarelo antes do nome. Ao passar o mouse, "
     "aparece o motivo, e o clique leva direto ao cadastro. Assim a recepção percebe o aviso antes de o paciente chegar."),
    ("07-checkin-aviso.png",
     "No check-in, ao ler o cartão do paciente, uma faixa amarela informa o motivo da revisão. O aviso não bloqueia o "
     "check-in. O link Abrir cadastro em outra aba permite conferir os dados sem perder o atendimento em andamento."),
    ("08-cadastro-aviso.png",
     "No cadastro do paciente, a faixa amarela no topo mostra o motivo e o botão Confirmar dados atualizados. Confira o "
     "endereço e o contato com o paciente. Se corrigir algo, basta salvar o cadastro: salvar com endereço e contato "
     "completos já registra a revisão. Se estava tudo certo, clique em Confirmar dados atualizados."),
    ("09-cadastro-confirmado.png",
     "A revisão foi registrada, com a data e o usuário, e a faixa desapareceu. O paciente deixa de aparecer na lista, na "
     "agenda e no check-in até o próximo prazo."),
    ("04-confirmar-lote.png",
     "Na lista, também é possível confirmar vários pacientes de uma vez. Marque os pacientes que foram conferidos, clique "
     "em Marcar como revisado, e o sistema pede uma confirmação antes de gravar."),
    ("10-lista-depois.png",
     "Depois de confirmar, os pacientes saem da lista: o total caiu de onze para dez. Lembrando: revisar é conferir com "
     "o paciente se o telefone e o endereço continuam os mesmos. Salvar o cadastro com dado faltando não conta como "
     "revisão, e só aparecem na lista os pacientes ativos."),
]

saida = [{"audio": f"{i:02d}.wav", "imagem": img, "texto": txt} for i, (img, txt) in enumerate(itens, 1)]
with open(os.path.join(BASE, "narracoes.json"), "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=1)
print(len(saida), "trechos")
