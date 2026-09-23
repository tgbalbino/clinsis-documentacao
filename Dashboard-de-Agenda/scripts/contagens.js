const path = require('path');
const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = '99999999999', SENHA = 'Cli99999';

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
    localStorage.setItem('_clTk', a.token); localStorage.setItem('_clNm', JSON.stringify(a.nome));
    localStorage.setItem('_clId', JSON.stringify(String(a.id))); localStorage.setItem('_clType', JSON.stringify(a.papel));
    localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig));
  }, auth);

  const resultado = {};
  for (const status of ['PRESENTE', 'AUSENTE']) {
    for (let n = 1; n <= 5; n++) {
      await page.goto(`${APP}/agendamento?idAgenda=33`);
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(500);
      await page.click('button:has-text("Filtros")');
      await page.waitForSelector('.modal.show');
      await page.waitForTimeout(500);
      const modal = page.locator('.modal.show').last();
      const sel = modal.locator('label', { hasText: `Sessão ${n}` }).first().locator('xpath=following-sibling::select').first();
      const opts = await sel.locator('option').all();
      for (const o of opts) {
        if ((await o.textContent() || '').trim() === status) { await sel.selectOption(await o.getAttribute('value')); break; }
      }
      await modal.locator('button:has-text("Filtrar")').first().click();
      await page.waitForTimeout(1000);
      await page.locator('.modal.show button:has-text("Fechar")').click().catch(() => {});
      await page.waitForTimeout(400);
      const txt = await page.locator('text=/Total de registros/').first().innerText();
      const m = txt.match(/Total de registros:\s*(\d+)/);
      resultado[`S${n}_${status}`] = m ? Number(m[1]) : txt;
    }
  }
  console.log(JSON.stringify(resultado, null, 2));
  require('fs').writeFileSync(path.join(__dirname, 'contagens.json'), JSON.stringify(resultado, null, 2));
  await browser.close();
})().catch(e => { console.error('FALHA:', e.message); process.exit(1); });
