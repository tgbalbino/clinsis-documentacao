// Prepara (e depois remove) os dados de demonstração da documentação "Controle de Cheques e Liquidação Financeira (Cheque e Cartão)".
// Uso: node setup_dados.js preparar | limpar     (banco local de teste; nunca produção)
// Variáveis: E2E_SQL_SERVER / E2E_SQL_DB (default DESKTOP-LI7EROU / a3_cli_hoje)
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'DESKTOP-LI7EROU';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ID_CLINICA = 1;
const ESTADO = path.join(__dirname, 'output', 'estado_demo.json');

const sql = q => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();

function preparar() {
  const original = {};
  for (const forma of [2, 6]) {
    original[forma] = sql(`SELECT CAST(PoliticaLiquidacao AS VARCHAR) + '|' + ISNULL(CAST(MaximoParcelasRecebimento AS VARCHAR), 'NULL') + '|' + ISNULL(CAST(PrazoLiquidacaoDiasPadrao AS VARCHAR), 'NULL') + '|' + ISNULL(CAST(IntervaloRepasseDias AS VARCHAR), 'NULL') + '|' + ISNULL(CAST(TaxaPercentualPadrao AS VARCHAR), 'NULL') FROM ConfigClinicaPagamentoForma WHERE IdClinica = ${ID_CLINICA} AND IdPagamentoForma = ${forma}`);
  }
  // Cartão de Crédito: repasse programado, 1º repasse em 30 dias, a cada 30 dias, taxa de 2,99%.
  sql(`UPDATE ConfigClinicaPagamentoForma SET PoliticaLiquidacao = 3, MaximoParcelasRecebimento = 6, PrazoLiquidacaoDiasPadrao = 30, IntervaloRepasseDias = 30, TaxaPercentualPadrao = 2.99 WHERE IdClinica = ${ID_CLINICA} AND IdPagamentoForma = 2`);
  // Cheque: compensação manual, previsão padrão de 3 dias.
  sql(`UPDATE ConfigClinicaPagamentoForma SET PoliticaLiquidacao = 2, PrazoLiquidacaoDiasPadrao = 3 WHERE IdClinica = ${ID_CLINICA} AND IdPagamentoForma = 6`);

  const receber = (pessoa, valor) => Number(sql(`
    DECLARE @plano INT = (SELECT TOP 1 IdPlanoConta FROM PlanoConta WHERE IdClinica = ${ID_CLINICA} AND Descricao = 'Consulta Particular');
    DECLARE @centro INT = (SELECT TOP 1 IdCentroCusto FROM CentroCusto WHERE IdClinica = ${ID_CLINICA} AND Descricao LIKE 'Consult%rio 1');
    INSERT INTO ContaReceber (IdClinica, IdItem, DataEmissao, DataVencimento, ValorOriginal, Saldo, Status, IdUsuario,
                              Modo, IdGrupoReceber, NParcela, TParcela, IdPlanoConta, IdCentroCusto, IdPessoa)
    VALUES (${ID_CLINICA}, 1, CAST(GETDATE() AS DATE), CAST(GETDATE() AS DATE), ${valor}, ${valor}, 1, 1,
            'M', 2000000000 + ABS(CHECKSUM(NEWID())) % 100000000, 1, 1, @plano, @centro, ${pessoa});
    SELECT CAST(SCOPE_IDENTITY() AS BIGINT);`));
  const cheque1 = receber(19, '450.00');   // Paciente 0002 - 1º título, pago com o cheque novo (cheque de R$ 700,00)
  const cheque2 = receber(19, '250.00');   // Paciente 0002 - 2º título, pago com o mesmo cheque já cadastrado
  const cartao = receber(20, '900.00');    // Paciente 0003 - cartão em 3x
  const pagar = Number(sql(`
    DECLARE @plano INT = (SELECT TOP 1 IdPlanoConta FROM PlanoConta WHERE IdClinica = ${ID_CLINICA} ORDER BY IdPlanoConta);
    DECLARE @centro INT = (SELECT TOP 1 IdCentroCusto FROM CentroCusto WHERE IdClinica = ${ID_CLINICA} ORDER BY IdCentroCusto);
    INSERT INTO ContaPagar (IdClinica, IdPlanoConta, IdCentroCusto, IdPessoa, Descricao, ValorOriginal, ValorPago, Saldo,
                            DataCompetencia, DataVencimento, Situacao, Recorrente, Cancelado, DataInclusao, IdUsuarioInclusao, Origem)
    VALUES (${ID_CLINICA}, @plano, @centro, 1, 'ALUGUEL DA SALA - IMOBILIARIA CENTRO', 1200.00, 0, 1200.00,
            CAST(GETDATE() AS DATE), CAST(GETDATE() AS DATE), 1, 0, 0, GETDATE(), 1, 1);
    SELECT CAST(SCOPE_IDENTITY() AS BIGINT);`));

  fs.mkdirSync(path.dirname(ESTADO), { recursive: true });
  fs.writeFileSync(ESTADO, JSON.stringify({ original, cheque1, cheque2, cartao, pagar }, null, 2));
  console.log(JSON.stringify({ cheque1, cheque2, cartao, pagar }));
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('nada a limpar'); return; }
  const { original, cheque1, cheque2, cartao, pagar } = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  const nul = v => (v === 'NULL' ? 'NULL' : v);
  sql(`
    DECLARE @recebers TABLE (Id BIGINT); INSERT @recebers VALUES (${cheque1}), (${cheque2}), (${cartao});
    DECLARE @baixas TABLE (Id INT); INSERT @baixas SELECT IdBaixa FROM ContaReceberBaixa WHERE IdReceber IN (SELECT Id FROM @recebers);
    DECLARE @baixasPagar TABLE (Id INT); INSERT @baixasPagar SELECT IdContaPagarBaixa FROM ContaPagarBaixa WHERE IdContaPagar = ${pagar};
    DECLARE @liq TABLE (Id BIGINT);
    INSERT @liq SELECT IdLiquidacaoFinanceira FROM LiquidacaoFinanceira WHERE (Origem = 2 AND IdOrigem IN (SELECT Id FROM @baixas)) OR (Origem = 1 AND IdOrigem IN (SELECT Id FROM @baixasPagar));
    DECLARE @chq TABLE (Id BIGINT); INSERT @chq SELECT DISTINCT IdCheque FROM LiquidacaoFinanceira WHERE IdLiquidacaoFinanceira IN (SELECT Id FROM @liq) AND IdCheque IS NOT NULL;
    DECLARE @cobr TABLE (Id BIGINT); INSERT @cobr SELECT IdReceberNovaCobranca FROM LiquidacaoFinanceira WHERE IdLiquidacaoFinanceira IN (SELECT Id FROM @liq) AND IdReceberNovaCobranca IS NOT NULL;
    DECLARE @mov TABLE (Id BIGINT);
    INSERT @mov SELECT IdMovimentoFinanceiro FROM Cheque WHERE IdCheque IN (SELECT Id FROM @chq) AND IdMovimentoFinanceiro IS NOT NULL;
    INSERT @mov SELECT IdMovimentoEstorno FROM Cheque WHERE IdCheque IN (SELECT Id FROM @chq) AND IdMovimentoEstorno IS NOT NULL;
    INSERT @mov SELECT IdMovimentoFinanceiro FROM LiquidacaoFinanceira WHERE IdLiquidacaoFinanceira IN (SELECT Id FROM @liq) AND IdMovimentoFinanceiro IS NOT NULL;
    INSERT @mov SELECT IdMovimentoEstorno FROM LiquidacaoFinanceira WHERE IdLiquidacaoFinanceira IN (SELECT Id FROM @liq) AND IdMovimentoEstorno IS NOT NULL;
    INSERT @mov SELECT IdMovimentoFinanceiro FROM MovimentoFinanceiro WHERE (Origem = 2 AND IdOrigem IN (SELECT Id FROM @baixas)) OR (Origem = 1 AND IdOrigem IN (SELECT Id FROM @baixasPagar));
    UPDATE Cheque SET IdMovimentoFinanceiro = NULL, IdMovimentoEstorno = NULL WHERE IdCheque IN (SELECT Id FROM @chq);
    UPDATE LiquidacaoFinanceira SET IdMovimentoFinanceiro = NULL, IdMovimentoEstorno = NULL, IdReceberNovaCobranca = NULL WHERE IdLiquidacaoFinanceira IN (SELECT Id FROM @liq);
    DELETE FROM MovimentoFinanceiro WHERE IdMovimentoFinanceiro IN (SELECT Id FROM @mov);
    DELETE FROM LiquidacaoFinanceira WHERE IdLiquidacaoFinanceira IN (SELECT Id FROM @liq);
    DELETE FROM Cheque WHERE IdCheque IN (SELECT Id FROM @chq);
    DELETE FROM ContaReceber WHERE IdReceber IN (SELECT Id FROM @cobr);
    DELETE FROM ContaReceberBaixa WHERE IdReceber IN (SELECT Id FROM @recebers);
    DELETE FROM ContaReceber WHERE IdReceber IN (SELECT Id FROM @recebers);
    DELETE FROM ContaPagarBaixa WHERE IdContaPagar = ${pagar};
    DELETE FROM ContaPagar WHERE IdContaPagar = ${pagar};`);
  for (const forma of [2, 6]) {
    const o = original[forma].split('|');
    sql(`UPDATE ConfigClinicaPagamentoForma SET PoliticaLiquidacao = ${o[0]}, MaximoParcelasRecebimento = ${nul(o[1])}, PrazoLiquidacaoDiasPadrao = ${nul(o[2])}, IntervaloRepasseDias = ${nul(o[3])}, TaxaPercentualPadrao = ${nul(o[4])} WHERE IdClinica = ${ID_CLINICA} AND IdPagamentoForma = ${forma}`);
  }
  fs.unlinkSync(ESTADO);
  console.log('dados de demonstração removidos e configuração das formas restaurada');
}

const acao = { preparar, limpar }[process.argv[2]];
if (acao) acao(); else console.log('uso: node setup_dados.js preparar|limpar');
