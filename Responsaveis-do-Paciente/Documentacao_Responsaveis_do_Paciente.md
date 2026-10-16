# Responsáveis do Paciente

_Quantos responsáveis forem necessários por paciente, com parentesco, contato e situação_

Versão 1.0 — 16/10/2026

Crianças, adolescentes e pacientes que dependem de alguém para vir à clínica costumam ter mais de um responsável: pai, mãe, avó, babá. No ClinSis, cada paciente pode ter quantos responsáveis forem necessários. Cada responsável é uma Pessoa (do tipo Responsável) ligada ao paciente pelo grau de parentesco e pela situação ativo ou inativo. A clínica pode exigir pelo menos um responsável ativo para pacientes menores de 18 anos, e os responsáveis são os que usam o Totem de check-in com os próprios dados.

Vídeo narrado desta rotina: `video-responsaveis-do-paciente-com-legenda.mp4`

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

![Paciente menor de idade, com a exigência ligada: asterisco vermelho em Responsáveis e a lista vazia.](02-paciente-sem-responsavel.png)

_Paciente menor de idade, com a exigência ligada: asterisco vermelho em Responsáveis e a lista vazia._

## Cadastrar um responsável no paciente

No cadastro do paciente, no bloco Responsáveis, a tabela mostra Nome, Parentesco, CPF e Situação. Clique em Adicionar responsável para abrir o formulário.

![Paciente com um responsável cadastrado. O selo amarelo "sem nascimento" avisa que ele ainda não poderá usar o totem.](03-paciente-com-responsavel.png)

_Paciente com um responsável cadastrado. O selo amarelo "sem nascimento" avisa que ele ainda não poderá usar o totem._

![Novo responsável: CPF, nome, grau de parentesco, celular, data de nascimento e endereço.](04-modal-novo.png)

_Novo responsável: CPF, nome, grau de parentesco, celular, data de nascimento e endereço._

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

![Dois responsáveis na lista do paciente. Nada é gravado até clicar em Salvar.](05-tabela-com-responsavel.png)

_Dois responsáveis na lista do paciente. Nada é gravado até clicar em Salvar._

![Cadastro salvo: o responsável passa a existir como Pessoa e fica ligado ao paciente.](06-salvo.png)

_Cadastro salvo: o responsável passa a existir como Pessoa e fica ligado ao paciente._

## Editar, inativar e remover

| Ação | Quando usar |
|---|---|
| Editar (lápis) | Corrigir telefone, endereço, parentesco ou data de nascimento do responsável. |
| Ativar / Inativar (chave) | Quando alguém deixa de ser responsável pelo paciente. O responsável inativo continua no histórico e não conta para a exigência de menor, nem usa o totem. |
| Remover (lixeira) | Só aparece para o responsável que acabou de ser incluído e ainda não foi salvo. Depois de salvo, use Inativar. |

## Responsável na tela de Pessoa

Em Cadastros → Pessoa, a lista tem a coluna Responsável, e o filtro Responsável mostra só essas pessoas. O filtro Sem data de nascimento ajuda a achar quem ainda não consegue usar o totem. Ao cadastrar uma Pessoa, a marca Responsável classifica a pessoa; o vínculo com o paciente é feito no cadastro do paciente.

![Filtros da tela de Pessoa: Responsável e Sem data de nascimento.](01-pessoa-filtro.png)

_Filtros da tela de Pessoa: Responsável e Sem data de nascimento._

![Pessoas do tipo Responsável, incluindo o responsável criado neste exemplo.](07-pessoa-responsavel.png)

_Pessoas do tipo Responsável, incluindo o responsável criado neste exemplo._

> ⚠️ Uma pessoa que é só responsável não conta como CPF duplicado de paciente. Isso permite cadastrar a criança com o CPF do pai ou da mãe, quando ela ainda não tem CPF próprio.

## Cuidados e regras

| Assunto | Como funciona |
|---|---|
| Paciente adulto | Também pode ter responsáveis (por exemplo, um cuidador). A exigência da clínica só vale para menores de 18 anos. |
| Mesmo responsável, vários pacientes | O responsável é uma única Pessoa. Alterar o celular dele vale para todos os pacientes ligados a ele. |
| CPF repetido na lista | O sistema não deixa informar o mesmo CPF duas vezes no mesmo paciente. |
| Quem pode editar | Quem pode alterar o cadastro do paciente. Os demais perfis apenas veem a lista. |
| Campo antigo de responsável | O campo único de responsável do cadastro antigo foi migrado para esta lista. Suporte: rodar o script 207 antes de publicar a API e o 208 só depois. |
