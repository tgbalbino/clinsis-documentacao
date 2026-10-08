// Prepara (e depois remove) os dados de demonstração da documentação "Estorno de Baixas (Contas a Receber e a Pagar)".
// Uso: node setup_dados.js preparar | limpar     (banco local de teste; nunca produção)
// Cria 2 títulos a receber e 2 a pagar JÁ BAIXADOS (via API, como a tela faz). Depois a captura estorna um de cada.
// Variáveis: E2E_SQL_SERVER / E2E_SQL_DB (default localhost / a3_cli_hoje)
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { loginApi, API } = require('../../_scripts-comuns/cap_common.js');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'localhost';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ID_CLINICA = 1;
const ESTADO = path.join(__dirname, 'output', 'estado_demo.json');

const sql = q => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();
const hoje = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };

async function post(token, rota, corpo) {
  const r = await fetch(`${API}/${rota}`, { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` }, body: JSON.stringify(corpo) });
  const t = await r.text();
  if (!r.ok) throw new Error(`${rota}: HTTP ${r.status} ${t.slice(0, 300)}`);
  return t;
}

async function preparar() {
  const obsCaixa = sql(`SELECT CAST(IdCaixa AS VARCHAR) + '|' + ISNULL(Observacao, '<<NULL>>') FROM Caixa WHERE IdClinica = ${ID_CLINICA} AND IdCaixa = 4`);
  const receber = (pessoa, valor) => Number(sql(`
    DECLARE @plano INT = (SELECT TOP 1 IdPlanoConta FROM PlanoConta WHERE IdClinica = ${ID_CLINICA} AND Descricao = 'Consulta Particular');
    DECLARE @centro INT = (SELECT TOP 1 IdCentroCusto FROM CentroCusto WHERE IdClinica = ${ID_CLINICA} AND Descricao LIKE 'Consult%rio 1');
    INSERT INTO ContaReceber (IdClinica, IdItem, DataEmissao, DataVencimento, ValorOriginal, Saldo, Status, IdUsuario,
                              Modo, IdGrupoReceber, NParcela, TParcela, IdPlanoConta, IdCentroCusto, IdPessoa)
    VALUES (${ID_CLINICA}, 1, CAST(GETDATE() AS DATE), CAST(GETDATE() AS DATE), ${valor}, ${valor}, 1, 1,
            'M', 2000000000 + ABS(CHECKSUM(NEWID())) % 100000000, 1, 1, @plano, @centro, ${pessoa});
    SELECT CAST(SCOPE_IDENTITY() AS BIGINT);`));
  const pagar = (descricao, valor) => Number(sql(`
    DECLARE @plano INT = (SELECT TOP 1 IdPlanoConta FROM PlanoConta WHERE IdClinica = ${ID_CLINICA} ORDER BY IdPlanoConta);
    DECLARE @centro INT = (SELECT TOP 1 IdCentroCusto FROM CentroCusto WHERE IdClinica = ${ID_CLINICA} ORDER BY IdCentroCusto);
    INSERT INTO ContaPagar (IdClinica, IdPlanoConta, IdCentroCusto, IdPessoa, Descricao, ValorOriginal, ValorPago, Saldo,
                            DataCompetencia, DataVencimento, Situacao, Recorrente, Cancelado, DataInclusao, IdUsuarioInclusao, Origem)
    VALUES (${ID_CLINICA}, @plano, @centro, 1, '${descricao}', ${valor}, 0, ${valor},
            CAST(GETDATE() AS DATE), CAST(GETDATE() AS DATE), 1, 0, 0, GETDATE(), 1, 1);
    SELECT CAST(SCOPE_IDENTITY() AS BIGINT);`));

  const estado = { obsCaixa, receberEstornar: receber(19, '400.00'), receberManter: receber(20, '250.00'),
                   pagarEstornar: pagar('ENERGIA ELETRICA - CONCESSIONARIA', '350.00'), pagarManter: pagar('MATERIAL DE LIMPEZA - DISTRIBUIDORA', '120.00') };
  fs.mkdirSync(path.dirname(ESTADO), { recursive: true });
  fs.writeFileSync(ESTADO, JSON.stringify(estado, null, 2));

  const auth = await loginApi();
  const data = `${hoje()}T00:00:00`;
  for (const [id, v] of [[estado.receberEstornar, 400], [estado.receberManter, 250]])
    await post(auth.token, 'ContaReceberBaixa/inserir', { IdReceber: id, IdItem: 1, ValorPago: v, JurosPago: 0, Desconto: 0, DataPagamento: data, IdFormaPagamento: 1, EstaPago: true, IdContaFinanceira: 8 });
  for (const [id, v] of [[estado.pagarEstornar, 350], [estado.pagarManter, 120]])
    await post(auth.token, 'ContaPagarBaixa', { IdContaPagar: id, DataPagamento: data, ValorPago: v, JurosPago: 0, Desconto: 0, IdFormaPagamento: 1, IdContaFinanceira: 8 });
  console.log(JSON.stringify(estado));
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('nada a limpar'); return; }
  const e = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  sql(`
    DECLARE @baixasR TABLE (Id INT); INSERT @baixasR SELECT IdBaixa FROM ContaReceberBaixa WHERE IdReceber IN (${e.receberEstornar}, ${e.receberManter});
    DECLARE @baixasP TABLE (Id INT); INSERT @baixasP SELECT IdContaPagarBaixa FROM ContaPagarBaixa WHERE IdContaPagar IN (${e.pagarEstornar}, ${e.pagarManter});
    DELETE FROM MovimentoFinanceiro WHERE (Origem = 2 AND IdOrigem IN (SELECT Id FROM @baixasR)) OR (Origem = 1 AND IdOrigem IN (SELECT Id FROM @baixasP));
    DELETE FROM ContaReceberBaixa WHERE IdReceber IN (${e.receberEstornar}, ${e.receberManter});
    DELETE FROM ContaReceber WHERE IdReceber IN (${e.receberEstornar}, ${e.receberManter});
    DELETE FROM ContaPagarBaixa WHERE IdContaPagar IN (${e.pagarEstornar}, ${e.pagarManter});
    DELETE FROM ContaPagar WHERE IdContaPagar IN (${e.pagarEstornar}, ${e.pagarManter});`);
  const [idCaixa, obs] = [e.obsCaixa.split('|')[0], e.obsCaixa.slice(e.obsCaixa.indexOf('|') + 1)];
  sql(`UPDATE Caixa SET Observacao = ${obs === '<<NULL>>' ? 'NULL' : `'${obs.replace(/'/g, "''")}'`} WHERE IdClinica = ${ID_CLINICA} AND IdCaixa = ${idCaixa}`);
  fs.unlinkSync(ESTADO);
  console.log('dados de demonstração removidos');
}

const cmd = process.argv[2];
if (cmd === 'preparar') preparar().catch(e => { console.error(e.message); process.exit(1); });
else if (cmd === 'limpar') limpar();
else console.log('uso: node setup_dados.js preparar | limpar');
