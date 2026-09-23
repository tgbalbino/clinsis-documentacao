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

  // Dashboard filtrado para Setembro/2026 (mesmo periodo do relatorio Qtd Marcacao)
  await page.goto(`${APP}/agenda/dashboard`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(500);
  const campoInicio = page.locator('input[bsdatepicker]').first();
  const campoFim = page.locator('input[bsdatepicker]').nth(1);
  await campoInicio.fill('01/09/2026');
  await page.keyboard.press('Escape');
  await campoFim.fill('30/09/2026');
  await page.keyboard.press('Escape');
  await page.click('button:has-text("Buscar")');
  await page.waitForTimeout(2500);
  await esconderMenuTestes();
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(300);
  await shot(page, '30-dashboard-setembro', false);

  // Guardar os numeros lidos dos cards, pra usar na documentacao
  const cards = await page.$$eval('.small-box', els => els.map(e => ({
    valor: (e.querySelector('h3') || {}).innerText,
    label: (e.querySelector('p') || {}).innerText
  })));
  console.log(JSON.stringify(cards, null, 2));
  require('fs').writeFileSync(path.join(__dirname, 'cards_setembro.json'), JSON.stringify(cards, null, 2));

  // Relatorio Guia Faturamento: escolher tipo de filtro "Data de Recebimento", datas 01/01/2026 a 30/09/2026
  await page.goto(`${APP}/relatorio/guiafaturamento`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(600);
  const selTipo = page.locator('select').first();
  const optsT = await selTipo.locator('option').all();
  for (const o of optsT) {
    const t = (await o.textContent() || '').trim();
    if (t.toLowerCase().includes('recebimento')) { await selTipo.selectOption(await o.getAttribute('value')); break; }
  }
  await page.waitForTimeout(500);
  const inputsData = page.locator('input[bsdatepicker], input[type="text"][placeholder*="/"]');
  if (await inputsData.count() >= 2) {
    await inputsData.nth(0).fill('01/01/2026');
    await page.keyboard.press('Escape');
    await inputsData.nth(1).fill('30/09/2026');
    await page.keyboard.press('Escape');
  }
  const btnBuscar = page.locator('button:has-text("Buscar"), button:has-text("Pesquisar")').first();
  if (await btnBuscar.count() > 0) await btnBuscar.click();
  await page.waitForTimeout(1500);
  await esconderMenuTestes();
  await shot(page, '31-relatorio-guia-faturamento-recebimento');

  // Relatorio Recebimentos: filtros Data 01/01/2026 a 30/09/2026
  await page.goto(`${APP}/relatorio/conta-receber/recebimentos`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(600);
  await page.click('button:has-text("Filtros")');
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(500);
  const modalRec = page.locator('.modal.show').last();
  const inputsRec = modalRec.locator('input[bsdatepicker]');
  if (await inputsRec.count() >= 2) {
    await inputsRec.nth(0).fill('01/01/2026');
    await page.keyboard.press('Escape');
    await inputsRec.nth(1).fill('30/09/2026');
    await page.keyboard.press('Escape');
  }
  await modalRec.locator('button:has-text("Buscar"), button:has-text("Pesquisar"), button:has-text("Filtrar")').first().click();
  await page.waitForTimeout(1500);
  await page.locator('.modal.show button:has-text("Fechar")').click().catch(() => {});
  await page.waitForTimeout(500);
  await esconderMenuTestes();
  await shot(page, '32-relatorio-recebimentos-periodo');

  // Agenda Profissional (grade de horarios): descobrir o select real de profissional dentro do modal/tela
  await page.goto(`${APP}/agenda/profissional?idAgenda=33`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(800);
  await shot(page, '33-agenda-profissional-inicial');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
