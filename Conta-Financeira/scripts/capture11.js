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




  await page.goto(`${APP}/cadastro/contasfinanceiras`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  // Reabilitar Cartao de Credito no CAIXA
  const linhaCaixa = page.locator('tr', { has: page.locator('td:first-child', { hasText: /^CAIXA$/ }) });
  await linhaCaixa.locator('button[title="Formas de pagamento desta conta"]').click();
  await page.waitForTimeout(700);
  const linhaCartao = page.locator('.modal.show tr').filter({ hasText: 'Cartão de Crédito' });
  if (await linhaCartao.locator('button:has-text("Habilitar")').count() > 0) {
    await linhaCartao.locator('button:has-text("Habilitar")').click();
    await page.waitForTimeout(400);
    await page.locator('button:visible', { hasText: 'Sim' }).click().catch(() => {});
    await page.waitForTimeout(800);
  }
  await page.click('.modal.show button:has-text("Fechar")');
  await page.waitForTimeout(500);
  // Excluir SICOOB (conta demo sem movimentos)
  const linhaSicoob = page.locator('tr', { has: page.locator('td:first-child', { hasText: /^SICOOB/ }) });
  await linhaSicoob.locator('button.btn-danger').click();
  await page.waitForTimeout(600);
  await shot(page, '16-confirmar-exclusao-conta-sem-movimentos');
  await page.locator('button:visible', { hasText: 'Sim' }).click();
  await page.waitForTimeout(1500);
  await shot(page, '17-exclusao-conta-sem-movimentos-ok');
  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message); process.exit(1); });
