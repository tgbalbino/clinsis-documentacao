# Revisão Cadastral de Pacientes

Mantém endereço e contato dos pacientes atualizados: lista de pendentes, aviso na agenda, no check-in e no cadastro, e o prazo de revisão como parâmetro da clínica.

## Documentação em PDF

- [📄 Manual em PDF](../assets/Revisao-Cadastral/Documentacao_Revisao_Cadastral_Simplificado.pdf)

## Vídeo narrado

*Vídeo em processo de publicação — o link será adicionado aqui assim que estiver disponível no YouTube.*

## Conteúdo completo do manual

---


_Como manter endereço e contato dos pacientes atualizados: lista de pendentes, aviso na agenda e no check-in_

Versão 1.0 — 16/10/2026

Cadastro desatualizado atrapalha a clínica: telefone que não atende, lembrete que não chega, cobrança enviada para o endereço errado. O módulo Revisão cadastral ajuda a manter o cadastro do paciente em dia, com foco em endereço e contato. Ele mostra, numa lista, quem precisa de revisão, e avisa na agenda do dia, no check-in e no próprio cadastro do paciente. O prazo para sugerir uma nova revisão (em dias) é um parâmetro da clínica. O módulo vem desligado e é liberado por clínica pela Área do Administrador.


---

## Quando o cadastro precisa de revisão

O sistema considera que o cadastro de um paciente ativo precisa de revisão quando acontece pelo menos uma destas situações:

| Situação | Como aparece | Exemplo |
|---|---|---|
| Nunca revisado ou prazo vencido | Selo amarelo Vencido (ou Nunca revisado) | Última revisão há 420 dias e o prazo da clínica é de 365 dias |
| Endereço incompleto | Selo vermelho Endereço | Falta CEP, logradouro, número, bairro ou município |
| Sem contato | Selo vermelho Contato | Nenhum celular, telefone ou e-mail preenchido |

> ⚠️ Endereço incompleto e falta de contato valem mesmo dentro do prazo: um cadastro sem telefone precisa ser revisado hoje, não daqui a um ano.

## Como ativar o módulo (administrador do sistema)

O módulo é liberado por clínica, como os demais módulos do ClinSis. Na Área do Administrador (endereço /area), abra Clínicas, entre no cadastro da clínica e marque a opção Revisão cadastral de pacientes. Salve.

> ⚠️ Depois de ligar, os usuários da clínica precisam sair e entrar de novo no sistema: o módulo chega junto com o login. Desligado, nada do que está neste manual aparece.

## Como definir o prazo (parâmetro)

Em Tabelas Aux. → Parâmetros existe o parâmetro RevisaoCadastralDias, que define de quantos em quantos dias o cadastro deve ser revisado. O padrão é 365 dias. Aceita de 30 a 1.825 dias; um valor vazio, inválido ou fora dessa faixa volta ao padrão. Clique no lápis amarelo para alterar.


## Lista de pacientes para revisar

Com o módulo ligado, aparece o menu Paciente → Revisão cadastral (para atendente e administrador). A lista mostra os pacientes ativos pendentes, dos mais antigos para os mais recentes, com nome, CPF, contato, data da última revisão (e quantos dias faz) e o motivo. No canto direito ficam o prazo em vigor e o total de pacientes.


Para trabalhar um grupo de cada vez, use o filtro Motivo: Revisão vencida ou nunca feita, Endereço incompleto ou Sem celular, telefone ou e-mail. Também dá para buscar pelo nome.



O botão com o lápis, em cada linha, abre o cadastro do paciente para conferir e atualizar os dados.

## Confirmar que o cadastro está atualizado

A revisão é registrada (data e usuário) de duas formas:

| Forma | Quando usar |
|---|---|
| Salvar o cadastro do paciente | Você corrigiu endereço ou contato e salvou. Só conta como revisão se endereço e contato mínimos estiverem preenchidos; salvar com dado faltando não revisa. |
| Botão Confirmar dados atualizados (no cadastro) ou Marcar como revisado (na lista) | Você conferiu com o paciente e os dados já estavam corretos. Na lista, marque vários pacientes e confirme de uma vez. |



## Aviso na agenda do dia

Na agenda, o paciente que precisa de revisão ganha um pequeno cartão amarelo antes do nome. Ao passar o mouse aparece o motivo, e o clique leva direto ao cadastro. Assim a recepção percebe o aviso antes mesmo do paciente chegar.


## Aviso no check-in

No check-in, ao ler o cartão do paciente, uma faixa amarela informa o motivo. O aviso não bloqueia o check-in. O link Abrir cadastro em outra aba permite conferir os dados sem perder o atendimento em andamento.


## Aviso no cadastro do paciente

Ao abrir o cadastro de um paciente que precisa de revisão, aparece uma faixa amarela no topo com o motivo e o botão Confirmar dados atualizados.


Ao confirmar, o sistema grava a revisão, a faixa some e o paciente deixa de aparecer na lista, na agenda e no check-in. Se houver alterações ainda não salvas no formulário, o sistema pede para salvar antes de confirmar.


## Regras importantes

| Assunto | Como funciona |
|---|---|
| Quem entra na lista | Somente pacientes ativos. Paciente inativo não aparece. |
| Pacientes novos | Nascem com a data do cadastro como data da primeira revisão. |
| Quando o módulo é ligado | Os pacientes existentes partem da data da última alteração do cadastro, para ninguém aparecer como vencido de uma só vez. |
| Editar por outras telas | Alterar a pessoa pelo painel de Pessoa não conta como revisão; use o cadastro do paciente. |
| Menores de idade | A revisão olha os dados do próprio paciente. Os dados do responsável não são avaliados nesta versão. |
| Módulo desligado | Nenhuma tela, aviso ou menu do módulo aparece e as consultas retornam vazio. |

> ⚠️ Revisar é conferir com o paciente: pergunte se o telefone e o endereço continuam os mesmos antes de confirmar.
