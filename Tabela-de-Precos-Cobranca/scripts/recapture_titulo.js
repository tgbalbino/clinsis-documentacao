// Recaptura (somente leitura, sem confirmar reajuste) as telas que mostram o titulo "Tabela de valores para ...".
const path = require('path');
const { chromium } = require('playwright');
const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';
const pasta = process.argv[2]; // cobranca | pagamento
const outDir = path.join(__dirname, 'screenshots');
const shot = (page, n) => page.screenshot({ path: path.join(outDir, n + '.png') });
async function login() {
  const p = (u, b, t) => fetch(API + u, { method: 'POST', headers: { 'Content-Type': 'application/json', ...(t ? { Authorization: 'Bearer ' + t } : {}) }, body: JSON.stringify(b) }).then(r => r.json());
  const l = await p('/usuario/login', { Login: LOGIN, Senha: SENHA });
  const s = await p('/clinicausuario/SelecionarClinica', { IdUsuario: l.data.id, IdClinica: 1, IdPerfilEscolha: 0 }, l.data.token);
  return s.data;
}
(async () => {
  const a = await login();
  const b = await chromium.launch(); const page = await b.newPage({ viewport: { width: 1600, height: 1000 } }); page.setDefaultTimeout(20000);
  const hide = () => page.addStyleTag({ content: '#li_testes { display: none !important; }' });
  await page.goto(APP);
  await page.evaluate(a => { localStorage.setItem('_clTk', a.token); localStorage.setItem('_clNm', JSON.stringify(a.nome)); localStorage.setItem('_clId', JSON.stringify(String(a.id))); localStorage.setItem('_clType', JSON.stringify(a.papel)); localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig || [])); }, a);
  await page.goto(APP + '/home'); await page.waitForLoadState('networkidle').catch(() => {});
  const go = async u => { await page.goto(APP + u); await page.waitForLoadState('networkidle'); await hide(); await page.waitForTimeout(900); };
  if (pasta === 'pagamento') {
    await go('/aux/tabpagamento'); await shot(page, '00-lista-vigencias');
  } else {
    await go('/aux/tabcobranca'); await shot(page, '00-aba-especialidade');
    await page.click('button:has-text("Reajustar preços")'); await page.waitForTimeout(500); await shot(page, '01-reajuste-formulario-aberto');
    await page.locator('input[type="number"]').first().fill('8'); await page.waitForTimeout(300);
    await page.click('button:has-text("Calcular prévia")'); await page.waitForTimeout(1200); await shot(page, '02-reajuste-previa');
    await go('/aux/tabcobranca');
    await page.click('#nav-tab button:has-text("Operadora")'); await page.waitForTimeout(700);
    const sel = page.locator('select').first();
    if (await sel.count() > 0) { const ops = await sel.locator('option').all(); if (ops.length > 1) await sel.selectOption(await ops[1].getAttribute('value')); await page.waitForTimeout(700); }
    await shot(page, '06-aba-operadora');
  }
  await b.close(); console.log('OK', pasta);
})().catch(e => { console.error('FALHA', e.message); process.exit(1); });
