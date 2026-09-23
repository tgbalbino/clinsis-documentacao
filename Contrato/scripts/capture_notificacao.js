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
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
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

  // ---- Tela de Parametros: onde fica "Dias de Aviso de Vencimento do Contrato" ----
  await page.goto(`${APP}/aux/parametro`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '24-parametros-lista');

  const linhaParam = page.locator('tr').filter({ hasText: /o Contrato está vencendo/i });
  const existeLinha = await linhaParam.count();
  if (existeLinha > 0) {
    await linhaParam.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await shot(page, '24b-parametro-dias-aviso-destacado');
    await linhaParam.locator('button.btn-warning').click();
    await page.waitForSelector('.modal.show', { timeout: 5000 });
    await page.waitForTimeout(500);
    await shot(page, '25-parametro-dias-aviso-editar');
  }

  // ---- Sino de notificacoes ----
  await page.goto(`${APP}/contrato`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  const sino = page.locator('[class*="notif"], .fa-bell, i.fa-bell').first();
  const temSino = await sino.count();
  console.log('sino encontrado:', temSino);
  if (temSino > 0) {
    await sino.click();
    await page.waitForTimeout(600);
    await shot(page, '26-sino-notificacoes');
  }

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
