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

  await page.goto(`${APP}/aux/tabcobranca`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '00-aba-especialidade');

  // Reajuste em massa (aba Especialidade)
  await page.click('button:has-text("Reajustar preços")');
  await page.waitForTimeout(500);
  await shot(page, '01-reajuste-formulario-aberto');

  const campoPercentual = page.locator('input[type="number"]').first();
  await campoPercentual.fill('8');
  await page.waitForTimeout(300);
  await page.click('button:has-text("Calcular prévia")');
  await page.waitForTimeout(1200);
  await shot(page, '02-reajuste-previa');

  await page.click('button:has-text("Confirmar reajuste")');
  await page.waitForTimeout(500);
  await page.locator('button:visible', { hasText: 'Sim' }).click();
  await page.waitForTimeout(1200);
  await esconderMenuTestes();
  await shot(page, '03-reajuste-confirmado');

  // Aba Profissional
  await page.click('#nav-tab button:has-text("Profissional")');
  await page.waitForTimeout(700);
  await shot(page, '04-aba-profissional');

  const primeiroProf = page.locator('#profissionais table tbody tr').first();
  if (await primeiroProf.count() > 0) {
    await primeiroProf.locator('button').first().click();
    await page.waitForSelector('.modal.show');
    await page.waitForTimeout(700);
    await shot(page, '05-modal-valores-profissional');
    await page.click('.modal.show button:has-text("Fechar")').catch(() => {});
    await page.waitForTimeout(400);
  }

  // Aba Operadora
  await page.click('#nav-tab button:has-text("Operadora")');
  await page.waitForTimeout(700);
  const selOperadora = page.locator('select').first();
  if (await selOperadora.count() > 0) {
    const opcoes = await selOperadora.locator('option').all();
    if (opcoes.length > 1) await selOperadora.selectOption(await opcoes[1].getAttribute('value'));
    await page.waitForTimeout(700);
  }
  await shot(page, '06-aba-operadora');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
