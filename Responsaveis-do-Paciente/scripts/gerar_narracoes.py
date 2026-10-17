# -*- coding: utf-8 -*-
"""Gera narracoes.json (texto de cada trecho do vídeo "Responsáveis do Paciente"). Rode: python gerar_narracoes.py"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

itens = [
    ("03-paciente-com-responsavel.png",
     "Este treinamento mostra os Responsáveis do paciente no ClinSis. Cada paciente pode ter quantos responsáveis forem "
     "necessários: pai, mãe, avó, babá. Eles ficam no cadastro do paciente, na aba Dados principais, no bloco "
     "Responsáveis, com nome, parentesco, CPF e situação. O selo amarelo, sem nascimento, avisa que aquele responsável "
     "ainda não poderá usar o totem de check-in."),
    ("02-paciente-sem-responsavel.png",
     "A clínica pode exigir pelo menos um responsável ativo para pacientes menores de dezoito anos. A opção fica na Área "
     "do Administrador, no cadastro da clínica, e vem desligada. Quando ligada, o título Responsáveis ganha um asterisco "
     "vermelho e o sistema não deixa salvar um menor sem responsável: informe ao menos um responsável ativo."),
    ("04-modal-novo.png",
     "Para cadastrar, clique em Adicionar responsável. Informe o CPF, o nome e o grau de parentesco. Se o CPF já existir "
     "como responsável de outro paciente, o sistema carrega os dados dele. O celular é opcional. A data de nascimento é "
     "obrigatória quando o totem está ativo, porque o responsável se identifica no totem com o próprio CPF e nascimento. "
     "O endereço já vem preenchido com o do paciente, e pode ser alterado."),
    ("05-tabela-com-responsavel.png",
     "Clique em Confirmar para incluir o responsável na lista. Nada é gravado ainda: o responsável só é salvo junto com o "
     "paciente, no botão Salvar. Antes de salvar, a lixeira permite remover quem acabou de ser incluído."),
    ("06-salvo.png",
     "Cadastro salvo. O responsável passou a existir como Pessoa e ficou ligado ao paciente. Depois de salvo, para tirar "
     "alguém da lista, use a chave Inativar: o responsável inativo continua no histórico, não conta para a exigência de "
     "menor e não usa o totem."),
    ("01-pessoa-filtro.png",
     "Na tela de Pessoa, em Cadastros, existe o filtro Responsável, que mostra só essas pessoas, e o filtro Sem data de "
     "nascimento, que ajuda a encontrar quem ainda não consegue usar o totem."),
    ("07-pessoa-responsavel.png",
     "Aqui estão os responsáveis, com a coluna Responsável marcada, incluindo o que acabamos de criar. O mesmo responsável "
     "pode estar ligado a vários pacientes, e alterar o celular dele vale para todos. Uma pessoa que é só responsável não "
     "conta como CPF duplicado de paciente, o que permite cadastrar a criança com o CPF do pai ou da mãe."),
]

saida = [{"audio": f"{i:02d}.wav", "imagem": img, "texto": txt} for i, (img, txt) in enumerate(itens, 1)]
with open(os.path.join(BASE, "narracoes.json"), "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=1)
print(len(saida), "trechos")
