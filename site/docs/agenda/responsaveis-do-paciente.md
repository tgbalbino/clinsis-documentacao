# Responsáveis do Paciente

Cada paciente pode ter quantos responsáveis forem necessários, com parentesco e situação. Explica como cadastrar, a opção de exigir responsável para menores de 18 anos e o uso do responsável no totem.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Responsaveis-do-Paciente/Documentacao_Responsaveis_do_Paciente_Simplificado.pdf)

## Vídeo narrado

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;"><iframe src="https://www.youtube.com/embed/6df6y0tUt8o?rel=0" title="Vídeo narrado" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>

[Abrir no YouTube](https://youtu.be/6df6y0tUt8o)

## Conteúdo completo do manual

---


_Quantos responsáveis forem necessários por paciente, com parentesco, contato e situação_

Versão 1.0 — 16/10/2026

Crianças, adolescentes e pacientes que dependem de alguém para vir à clínica costumam ter mais de um responsável: pai, mãe, avó, babá. No ClinSis, cada paciente pode ter quantos responsáveis forem necessários. Cada responsável é uma Pessoa (do tipo Responsável) ligada ao paciente pelo grau de parentesco e pela situação ativo ou inativo. A clínica pode exigir pelo menos um responsável ativo para pacientes menores de 18 anos, e os responsáveis são os que usam o Totem de check-in com os próprios dados.


---

## Como funciona

| Assunto | Como funciona |
|---|---|
| Quantos responsáveis | Quantos forem necessários, cada um com grau de parentesco (Mãe, Pai, Avô, Avó, Tio, Babá, Irmão(ã) ou Outros) e situação Ativo ou Inativo. |
| O responsável é uma Pessoa | Fica no cadastro de Pessoa com a marca Responsável, e o mesmo responsável pode estar ligado a mais de um paciente (irmãos, por exemplo). |
| Onde se cadastra | No cadastro do paciente, aba Dados principais, bloco Responsáveis. Os responsáveis são gravados junto com o paciente, no botão Salvar. |
| Exigir responsável de menor | Opção da clínica: com ela ligada, não se salva paciente menor de 18 anos sem ao menos 1 responsável ativo. Vem desligada. |
| Totem de check-in | O responsável registra a chegada dos dependentes com o seu próprio CPF e data de nascimento. Por isso, com o totem ativo, a data de nascimento do responsável é obrigatória. |

## Como ligar a exigência de responsável para menores

Na Área do Administrador (endereço /area), abra Clínicas, entre no cadastro da clínica e marque Exigir responsável para menor de 18 anos. Salve. Depois disso, o título Responsáveis do cadastro de paciente menor ganha um asterisco vermelho, e o sistema avisa quando não há nenhum responsável ativo: "Paciente menor de 18 anos: informe ao menos 1 responsável ativo."


## Cadastrar um responsável no paciente

No cadastro do paciente, no bloco Responsáveis, a tabela mostra Nome, Parentesco, CPF e Situação. Clique em Adicionar responsável para abrir o formulário.



| Campo | Como preencher |
|---|---|
| CPF (obrigatório) | Precisa ser um CPF válido e não repetir na lista do paciente. Se o CPF já existir como responsável em outro paciente, o sistema avisa "Responsável já cadastrado: os dados foram carregados" e só falta informar o parentesco. |
| Nome (obrigatório) | Nome completo do responsável. |
| Grau de parentesco (obrigatório) | Escolha na lista: Mãe, Pai, Avô, Avó, Tio, Babá, Irmão(ã) ou Outros. |
| Celular | Contato do responsável. |
| Data de nascimento | Obrigatória quando o totem de check-in está ativo na clínica: é com ela e o CPF que o responsável se identifica no totem. |
| Responsável ativo | Marcado por padrão. Desmarque para manter o registro sem usá-lo (por exemplo, quando alguém deixa de ser responsável). |
| Endereço | Já vem preenchido com o endereço do paciente; altere se o responsável mora em outro lugar. |

Clique em Confirmar para incluir o responsável na lista e depois em Salvar, no cadastro do paciente, para gravar.



## Editar, inativar e remover

| Ação | Quando usar |
|---|---|
| Editar (lápis) | Corrigir telefone, endereço, parentesco ou data de nascimento do responsável. |
| Ativar / Inativar (chave) | Quando alguém deixa de ser responsável pelo paciente. O responsável inativo continua no histórico e não conta para a exigência de menor, nem usa o totem. |
| Remover (lixeira) | Só aparece para o responsável que acabou de ser incluído e ainda não foi salvo. Depois de salvo, use Inativar. |

## Responsável na tela de Pessoa

Em Cadastros → Pessoa, a lista tem a coluna Responsável, e o filtro Responsável mostra só essas pessoas. O filtro Sem data de nascimento ajuda a achar quem ainda não consegue usar o totem. Ao cadastrar uma Pessoa, a marca Responsável classifica a pessoa; o vínculo com o paciente é feito no cadastro do paciente.



> ⚠️ Uma pessoa que é só responsável não conta como CPF duplicado de paciente. Isso permite cadastrar a criança com o CPF do pai ou da mãe, quando ela ainda não tem CPF próprio.

## Cuidados e regras

| Assunto | Como funciona |
|---|---|
| Paciente adulto | Também pode ter responsáveis (por exemplo, um cuidador). A exigência da clínica só vale para menores de 18 anos. |
| Mesmo responsável, vários pacientes | O responsável é uma única Pessoa. Alterar o celular dele vale para todos os pacientes ligados a ele. |
| CPF repetido na lista | O sistema não deixa informar o mesmo CPF duas vezes no mesmo paciente. |
| Quem pode editar | Quem pode alterar o cadastro do paciente. Os demais perfis apenas veem a lista. |
| Campo antigo de responsável | O campo único de responsável do cadastro antigo foi migrado para esta lista. Suporte: rodar o script 207 antes de publicar a API e o 208 só depois. |
