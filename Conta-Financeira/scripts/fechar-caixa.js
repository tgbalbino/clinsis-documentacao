const { chromium } = require('playwright');
const API = 'http://localhost:49020/api';
const APP = 'http://localhost:4222';
const LOGIN = '99999999999';
const SENHA = 'Cli99999';

async function loginApi() {
  const r1 = await fetch(`${API}/usuario/login`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ Login: LOGIN, Senha: SENHA }) });
  const j1 = await r1.json();
  const r2 = await fetch(`${API}/clinicausuario/SelecionarClinica`, { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${j1.data.token}` }, body: JSON.stringify({ IdUsuario: j1.data.id, IdClinica: 1, IdPerfilEscolha: 0 }) });
  const j2 = await r2.json();
  return { token: j2.data.token, nome: j2.data.nome, id: j2.data.id, papel: j2.data.papel, clinicaConfig: j2.data.clinicaConfig || [] };
}

(async () => {
  const auth = await loginApi();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
  page.setDefaultTimeout(20000);
  await page.goto(APP);
  await page.evaluate((a) => {
    localStorage.setItem('_clTk', a.token);
    localStorage.setItem('_clNm', JSON.stringify(a.nome));
    localStorage.setItem('_clId', JSON.stringify(String(a.id)));
    localStorage.setItem('_clType', JSON.stringify(a.papel));
    localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig));
  }, auth);

  await page.goto(`${APP}/caixa`);
  await page.waitForLoadState('networkidle');
  await page.click('button:has-text("Fechar Caixa")');
  await page.waitForTimeout(800);
  await page.locator('.meuModalTotal button:has-text("Confirmar")').click();
  await page.waitForTimeout(1500);
  await page.screenshot({ path: 'screenshots/fechar-caixa-final.png' });
  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message); process.exit(1); });
