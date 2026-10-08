# -*- coding: utf-8 -*-
"""Gera narracoes.json (texto de cada trecho do vídeo "Estorno de Baixas"). Rode: python gerar_narracoes.py
Os valores citados (650/470/180 antes, 250/120/130 depois) vêm de output/valores.json, lidos pela captura."""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

itens = [
    ("01-dashboard-antes.png",
     "Este treinamento mostra como estornar uma baixa de conta a receber e de conta a pagar no ClinSis, e como conferir "
     "o resultado no Dashboard Financeiro, nos relatórios e nos Movimentos Financeiros. Estornar é cancelar um "
     "recebimento ou um pagamento lançado errado. Antes de começar, o Dashboard do mês mostra entradas de seiscentos e "
     "cinquenta reais, saídas de quatrocentos e setenta, e resultado de cento e oitenta. O saldo da conta Caixa é de "
     "cento e oitenta reais."),
    ("02-rel-recebimentos-antes.png",
     "No relatório de Recebimentos, em Relatórios, estão as duas baixas do mês: quatrocentos reais da Paciente zero zero "
     "zero dois, e duzentos e cinquenta da Paciente zero zero zero três. Ambas estão ativas."),
    ("03-rel-pagamentos-antes.png",
     "No relatório de Pagamentos, as duas contas pagas: energia elétrica, de trezentos e cinquenta reais, e material de "
     "limpeza, de cento e vinte."),
    ("04-movimentos-antes.png",
     "Em Movimentos Financeiros, cada baixa gerou um lançamento na conta Caixa: duas entradas e duas saídas, somando "
     "mil cento e vinte reais."),
    ("05-lista-receber-quitado.png",
     "Vamos estornar o recebimento de quatrocentos reais. Em Contas a Receber, o título aparece como Baixada, com saldo "
     "zerado. Clique no botão verde de pagamento, ao lado do título."),
    ("06-receber-historico.png",
     "Na janela de Acertos e Recebimentos, abra a aba Histórico e Estornos. Ela lista todas as baixas do título. Para "
     "estornar, clique na lixeira vermelha da linha."),
    ("07-receber-motivo.png",
     "O sistema pede o motivo do cancelamento, que é obrigatório: recebimento lançado em conta errada, valor ou data "
     "incorretos, recebimento em duplicidade ou recebimento não realizado. Escolha o motivo e clique em Confirmar "
     "cancelamento."),
    ("08-receber-estornado.png",
     "Pronto. A baixa não é apagada: ela continua no histórico, em vermelho, como Estornado, com a data, o usuário e o "
     "motivo. O Valor Restante volta a quatrocentos reais, e a lixeira desaparece, porque uma baixa estornada não pode "
     "ser estornada de novo."),
    ("09-receber-reaberto.png",
     "Na lista de Contas a Receber, o título voltou para Aberto, com saldo de quatrocentos reais, pronto para receber "
     "de novo. Se o valor ou a data estavam errados, basta lançar a baixa correta."),
    ("10-lista-pagar-quitado.png",
     "O estorno de um pagamento funciona do mesmo jeito. Em Contas a Pagar, a conta de energia elétrica, de trezentos e "
     "cinquenta reais, está quitada. Clique no botão verde de pagamento para abrir o Pagamento e Acerto da conta."),
    ("11-pagar-historico.png",
     "Na aba Histórico e Estornos ficam os pagamentos da conta. Para estornar, clique no botão vermelho de cancelar."),
    ("12-pagar-motivo.png",
     "Escolha o motivo do cancelamento, também obrigatório, e clique em Confirmar Cancelamento."),
    ("13-pagar-estornado.png",
     "O pagamento passa a aparecer como Cancelado, e o sistema informa o total cancelado: trezentos e cinquenta reais."),
    ("14-pagar-reaberto.png",
     "A conta de energia elétrica voltou para Aberto, com o saldo integral de trezentos e cinquenta reais."),
    ("15-dashboard-depois.png",
     "Agora a conferência. No Dashboard Financeiro, com o mesmo período, as entradas caíram de seiscentos e cinquenta "
     "para duzentos e cinquenta reais: exatamente os quatrocentos estornados. As saídas caíram de quatrocentos e setenta "
     "para cento e vinte: os trezentos e cinquenta do pagamento cancelado. O resultado do período passou de cento e "
     "oitenta para cento e trinta reais, e o saldo da conta Caixa também. As tabelas por plano de conta e os maiores "
     "recebimentos e pagamentos por pessoa foram atualizados."),
    ("16-rel-recebimentos-todas.png",
     "No relatório de Recebimentos, com a situação Todas, a baixa estornada continua aparecendo, com o selo vermelho "
     "Excluída, para consulta e auditoria. Mas o total do rodapé soma somente as baixas ativas: duzentos e cinquenta "
     "reais."),
    ("17-rel-recebimentos-ativas.png",
     "Com a situação Somente ativas, a baixa estornada sai da lista, e o total continua o mesmo."),
    ("18-rel-pagamentos-depois.png",
     "No relatório de Pagamentos vale a mesma regra. O pagamento cancelado aparece com o selo Cancelado, mas o total "
     "soma somente os pagamentos ativos: cento e vinte reais."),
    ("19-movimentos-depois.png",
     "Em Movimentos Financeiros, os lançamentos dos estornos deixaram de aparecer. Sobraram apenas a entrada de duzentos "
     "e cinquenta reais e a saída de cento e vinte. O lançamento original não é apagado do banco de dados: ele é marcado "
     "como excluído, com usuário, data e motivo. Por isso não entra mais em saldos, dashboard, extrato e conciliação."),
    ("08-receber-estornado.png",
     "Para terminar, três regras importantes. Primeira: o estorno exige motivo e fica registrado com usuário e data. "
     "Segunda: se a baixa foi feita com o caixa aberto, esse caixa precisa continuar aberto; se já foi fechado, peça a "
     "um administrador para reabri-lo. Terceira: baixa de cheque já compensado, ou de cartão com parcela já repassada, "
     "não pode ser estornada direto. Antes, é preciso devolver a liquidação financeira."),
]

saida = [{"audio": f"{i:02d}.wav", "imagem": img, "texto": txt} for i, (img, txt) in enumerate(itens, 1)]
with open(os.path.join(BASE, "narracoes.json"), "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=1)
print(len(saida), "trechos")
