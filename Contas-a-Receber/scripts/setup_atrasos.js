// Prepara (e depois remove) os dados de demonstração do trecho "Recebimento em atraso" (Contas a Receber v1.2).
// Uso: node setup_atrasos.js preparar | limpar     (banco local de teste; nunca produção)
// Cria 3 títulos a receber do Paciente 0002 (IdPessoa 19), vencidos em setembro/2026: dois já BAIXADOS hoje (via API, como a tela faz),
// que alimentam o relatório de recebimentos e o dashboard, e um EM ABERTO para a captura do aviso de pagamento em atraso.
// Variáveis: E2E_SQL_SERVER / E2E_SQL_DB (default localhost / a3_cli_hoje)
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { loginApi, API } = require('../../_scripts-comuns/cap_common.js');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'localhost';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ID_CLINICA = 1;
const ESTADO = path.join(__dirname, 'output', 'estado_atrasos.json');

const sql = (q) => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();
const hoje = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };

async function post(token, rota, corpo) {
  const r = await fetch(`${API}/${rota}`, { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` }, body: JSON.stringify(corpo) });
  const t = await r.text();
  if (!r.ok) throw new Error(`${rota}: HTTP ${r.status} ${t.slice(0, 300)}`);
  return t;
}

async function preparar() {
  if (fs.existsSync(ESTADO)) throw new Error('Já existe output/estado_atrasos.json: rode "limpar" antes.');
  const receber = (vencimento, valor) => Number(sql(`
    DECLARE @plano INT = (SELECT TOP 1 IdPlanoConta FROM PlanoConta WHERE IdClinica = ${ID_CLINICA} AND Descricao = 'Consulta Particular');
    DECLARE @centro INT = (SELECT TOP 1 IdCentroCusto FROM CentroCusto WHERE IdClinica = ${ID_CLINICA} AND Descricao LIKE 'Consult%rio 1');
    INSERT INTO ContaReceber (IdClinica, IdItem, DataEmissao, DataVencimento, ValorOriginal, Saldo, Status, IdUsuario,
                              Modo, IdGrupoReceber, NParcela, TParcela, IdPlanoConta, IdCentroCusto, IdPessoa)
    VALUES (${ID_CLINICA}, 1, '2026-09-01', '${vencimento}', ${valor}, ${valor}, 1, 1,
            'M', 2000000000 + ABS(CHECKSUM(NEWID())) % 100000000, 1, 1, @plano, @centro, 19);
    SELECT CAST(SCOPE_IDENTITY() AS BIGINT);`));
  const estado = { baixadoA: receber('2026-09-10', '120.00'), baixadoB: receber('2026-09-30', '80.00'), aberto: receber('2026-09-20', '100.00') };
  fs.mkdirSync(path.dirname(ESTADO), { recursive: true });
  fs.writeFileSync(ESTADO, JSON.stringify(estado, null, 2));
  const auth = await loginApi();
  const data = `${hoje()}T00:00:00`;
  for (const [id, v] of [[estado.baixadoA, 120], [estado.baixadoB, 80]])
    await post(auth.token, 'ContaReceberBaixa/inserir', { IdReceber: id, IdItem: 1, ValorPago: v, JurosPago: 0, Desconto: 0, DataPagamento: data, IdFormaPagamento: 1, EstaPago: true, IdContaFinanceira: 8 });
  console.log(JSON.stringify(estado));
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('nada a limpar'); return; }
  const e = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  const ids = `${e.baixadoA}, ${e.baixadoB}, ${e.aberto}`;
  sql(`
    DECLARE @baixasR TABLE (Id INT); INSERT @baixasR SELECT IdBaixa FROM ContaReceberBaixa WHERE IdReceber IN (${ids});
    DELETE FROM MovimentoFinanceiro WHERE Origem = 2 AND IdOrigem IN (SELECT Id FROM @baixasR);
    DELETE FROM ContaReceberBaixa WHERE IdReceber IN (${ids});
    DELETE FROM ContaReceber WHERE IdReceber IN (${ids});`);
  fs.unlinkSync(ESTADO);
  console.log('dados de demonstração removidos');
}

const cmd = process.argv[2];
if (cmd === 'preparar') preparar().catch((e) => { console.error(e.message); process.exit(1); });
else if (cmd === 'limpar') limpar();
else console.log('uso: node setup_atrasos.js preparar | limpar');
