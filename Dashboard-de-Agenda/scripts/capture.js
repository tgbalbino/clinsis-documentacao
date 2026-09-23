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
  const page = await browser.newPage({ viewport: { width: 1600, height: 1100 } });
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

  await page.goto(`${APP}/agenda/dashboard`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(500);

  // Ampliar período pra 01/01/2026 a 30/09/2026 pra garantir dados em todos os blocos
  const campoInicio = page.locator('input[bsdatepicker]').first();
  const campoFim = page.locator('input[bsdatepicker]').nth(1);
  await campoInicio.fill('01/01/2026');
  await page.keyboard.press('Escape');
  await campoFim.fill('30/09/2026');
  await page.keyboard.press('Escape');
  await page.click('button:has-text("Buscar")');
  await page.waitForTimeout(2500);
  await esconderMenuTestes();

  await shot(page, '00-topo-cards-1');

  // Scroll incremental para capturar tudo em partes
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(300);
  await shot(page, '01-cards-e-filtros');

  await page.locator('.card-header:has-text("Presença x Ausência")').scrollIntoViewIfNeeded();
  await page.waitForTimeout(500);
  await shot(page, '02-graficos-pizza-evolucao');

  await page.locator('.card-header:has-text("Por Profissional")').scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);
  await shot(page, '03-tabelas-profissional-especialidade-operadora');

  const temMetodoPrograma = await page.locator('.card-header:has-text("Por Método"), .card-header:has-text("Por Programa")').count();
  if (temMetodoPrograma > 0) {
    await page.locator('.card-header:has-text("Por Método"), .card-header:has-text("Por Programa")').first().scrollIntoViewIfNeeded();
    await page.waitForTimeout(400);
    await shot(page, '04-metodo-programa');
  }

  await page.locator('.card-header:has-text("Sessões por Faixa Etária")').scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);
  await shot(page, '05-faixa-etaria-dias-horarios');

  await page.locator('.card-header:has-text("Faturamento por Convênio")').scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);
  await shot(page, '06-faturamento-convenio');

  // Tooltip da Taxa de Ocupação
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(300);
  const cardOcupacao = page.locator('.small-box:has-text("Taxa de Ocupação")');
  await cardOcupacao.hover();
  await page.waitForTimeout(600);
  await shot(page, '07-tooltip-taxa-ocupacao', false);

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
