const path = require('path');
const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';
const outDir = path.join(__dirname, 'screenshots');
const shot = (page, name, fullPage = true) => page.screenshot({ path: path.join(outDir, `${name}.png`), fullPage });

async function loginApi() {
  const r1 = await fetch(`${API}/usuario/login`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ Login: LOGIN, Senha: SENHA })
  });
  const j1 = await r1.json();
  const r2 = await fetch(`${API}/clinicausuario/SelecionarClinica`, {
    method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${j1.data.token}` },
    body: JSON.stringify({ IdUsuario: j1.data.id, IdClinica: 1, IdPerfilEscolha: 0 })
  });
  const j2 = await r2.json();
  return { token: j2.data.token, nome: j2.data.nome, id: j2.data.id, papel: j2.data.papel, clinicaConfig: j2.data.clinicaConfig || [] };
}

(async () => {
  const auth = await loginApi();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
  page.setDefaultTimeout(30000);
  const esconderMenuTestes = () => page.addStyleTag({ content: '#li_testes { display: none !important; }' });

  await page.goto(APP);
  await page.evaluate((a) => {
    localStorage.setItem('_clTk', a.token);
    localStorage.setItem('_clNm', JSON.stringify(a.nome));
    localStorage.setItem('_clId', JSON.stringify(String(a.id)));
    localStorage.setItem('_clType', JSON.stringify(a.papel));
    localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig));
  }, auth);
  await esconderMenuTestes();





  // Movimentos filtrado por conta CAIXA
  await page.goto(`${APP}/financeiro/movimentos`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(1000);
  const selConta = page.locator('select').first();
  const optsC = await selConta.locator('option').all();
  for (const o of optsC) { if ((await o.textContent()).trim() === 'CAIXA') { await selConta.selectOption(await o.getAttribute('value')); break; } }
  await page.click('button:has-text("Buscar")');
  await page.waitForTimeout(1200);
  await shot(page, '22-movimentos-filtrado-caixa');

  // Formas de pagamento da clinica
  await page.goto(`${APP}/aux/pagamentoforma`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(1000);
  await shot(page, '23-formas-pagamento-clinica');

  // Parametros
  await page.goto(`${APP}/aux/parametro`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(1000);
  const busca = page.locator('input[type="text"]').first();
  await busca.fill('ContaFinanceira').catch(() => {});
  await page.keyboard.press('Enter');
  await page.waitForTimeout(1000);
  await shot(page, '24-parametro-conta-financeira-checkin');

  // Contas a Pagar - baixa com Conta Financeira obrigatoria
  await page.goto(`${APP}/financeiro/contapagar`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(600);
  await page.click('button:has-text("Filtros")');
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(450);
  await page.click('.modal.show button:has-text("Buscar")');
  await page.waitForTimeout(1000);
  await page.click('.modal.show button:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(400);
  const linha = page.locator('tr').filter({ hasText: 'Aberto' }).first();
  await linha.locator('button.btn-success').first().click();
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(700);
  await shot(page, '25-contapagar-baixa-conta-obrigatoria');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message); process.exit(1); });
