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

  const linhaAberta = page.locator('tr').filter({ hasText: 'Aberto' }).first();
  await linhaAberta.locator('button.btn-success').first().click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(600);

  const modalBaixa = page.locator('.modal.show').last();
  const metodoSelect = modalBaixa.locator('select').first();
  const contaSelect = modalBaixa.locator('select').nth(1);

  async function selecionar(select, textoContem) {
    const opcoes = await select.locator('option').all();
    for (const o of opcoes) {
      const t = (await o.textContent() || '').toLowerCase();
      if (t.includes(textoContem)) { await select.selectOption(await o.getAttribute('value')); return true; }
    }
    return false;
  }

  await selecionar(metodoSelect, 'cartão de crédito');
  await page.waitForTimeout(300);
  const campoValor = modalBaixa.locator('input[mask="separator.2"]').first();
  await campoValor.fill('1,00');
  await page.waitForTimeout(200);
  await selecionar(contaSelect, 'caixa');
  await page.waitForTimeout(300);
  await shot(page, '04-baixa-combinacao-nao-habilitada');

  await modalBaixa.locator('button:has-text("Lançar")').click();
  await page.waitForSelector('div:has-text("Deseja realmente salvar este pagamento?")', { timeout: 5000 });
  await page.waitForTimeout(400);
  await page.locator('button:visible', { hasText: 'Sim' }).click();
  await page.waitForTimeout(1500);
  await shot(page, '05-erro-forma-nao-habilitada');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
