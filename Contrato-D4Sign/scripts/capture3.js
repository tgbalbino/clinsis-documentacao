const path = require('path');
const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';
const outDir = path.join(__dirname, 'screenshots');
const shot = (page, name, fullPage = true) => page.screenshot({ path: path.join(outDir, `${name}.png`), fullPage });
const IDCONTRATO = 29;

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
  const page = await browser.newPage({ viewport: { width: 1600, height: 1100 } });
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

  await page.goto(`${APP}/contrato`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);

  const linha = page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp(`^${IDCONTRATO}$`) }) });
  await linha.locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(700);
  await shot(page, '04-contrato-fechado-automaticamente');

  await page.click('.modal.show button[data-bs-target="#tabContratoAssinatura"]');
  await page.waitForTimeout(500);
  await shot(page, '05-historico-assinatura');

  await page.click('.modal.show button.btn-secondary:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(400);

  // ---- Verificar Conta a Receber gerada ----
  await page.goto(`${APP}/financeiro/contareceber`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(500);
  await page.click('button:has-text("Filtros")');
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(450);
  await page.click('.modal.show button:has-text("Buscar")');
  await page.waitForTimeout(1000);
  await page.click('.modal.show button:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(400);
  await shot(page, '06-conta-a-receber-gerada');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
