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
  await shot(page, '01-gerenciar-aba-agenda');

  // Aba Especialidades
  await page.click('a:has-text("Especialidades"), button:has-text("Especialidades")');
  await page.waitForTimeout(700);
  await shot(page, '02-aba-especialidades');

  // Expandir Reajustar precos
  await page.click('button:has-text("Reajustar preços")');
  await page.waitForTimeout(500);
  await shot(page, '03-reajuste-formulario-aberto');

  // Preencher percentual e calcular previa
  const campoPercentual = page.locator('input[type="number"]').first();
  await campoPercentual.fill('10');
  await page.waitForTimeout(300);
  await page.click('button:has-text("Calcular prévia")');
  await page.waitForTimeout(1200);
  await shot(page, '04-reajuste-previa');

  // Confirmar
  await page.click('button:has-text("Confirmar reajuste")');
  await page.waitForTimeout(500);
  await shot(page, '05-reajuste-modal-confirmar');
  await page.locator('button:visible', { hasText: 'Sim' }).click();
  await page.waitForTimeout(1200);
  await shot(page, '06-reajuste-confirmado');

  // Aba Profissionais
  await page.click('a:has-text("Profissionais"), button:has-text("Profissionais")');
  await page.waitForTimeout(700);
  await shot(page, '07-aba-profissionais');

  const primeiroProf = page.locator('table tbody tr').first();
  await primeiroProf.locator('button').first().click();
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(700);
  await shot(page, '08-modal-valores-profissional');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
