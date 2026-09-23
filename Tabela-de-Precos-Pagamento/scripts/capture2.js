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
  page.setDefaultTimeout(20000);
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

  // Lista de tabelas (vigencias)
  await page.goto(`${APP}/aux/tabpagamento`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '00-lista-vigencias');


  // Gerenciar a primeira tabela ativa
  const linhaAtiva = page.locator('tr').filter({ hasText: 'Sim' }).first();
  const linhaAlvo = (await linhaAtiva.count()) > 0 ? linhaAtiva : page.locator('table tbody tr').first();
  await linhaAlvo.locator('button[title*="Gerenciar" i], a[title*="Gerenciar" i], button.btn-info, a.btn-info').first().click();
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(800);

  await page.click('a:has-text("Profissionais"), button:has-text("Profissionais")');
  await page.waitForTimeout(700);
  await shot(page, '07b-debug-aba-profissionais');

  const primeiroProf = page.locator('tr').filter({ hasText: 'Profissional 01' }).first();
  await primeiroProf.locator('button').click();
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(700);
  await shot(page, '08-modal-valores-profissional');

  const modal = page.locator('.modal.show').last();
  const temReajuste = await modal.locator('button:has-text("Reajustar preços")').count();
  if (temReajuste > 0) {
    await modal.locator('button:has-text("Reajustar preços")').click();
    await page.waitForTimeout(400);
    await shot(page, '09-reajuste-profissional-formulario');
  }

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
