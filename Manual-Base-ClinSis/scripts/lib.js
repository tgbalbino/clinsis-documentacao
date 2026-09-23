const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const API = 'http://localhost:49020/api', APP = 'http://localhost:4222';
const OUT = path.join(__dirname, 'screenshots');
fs.mkdirSync(OUT, { recursive: true });
async function start() {
  const j = async (u, b, t) => (await fetch(API + u, { method: 'POST', headers: { 'Content-Type': 'application/json', ...(t ? { Authorization: 'Bearer ' + t } : {}) }, body: JSON.stringify(b) })).json();
  const l = await j('/usuario/login', { Login: '99999999999', Senha: 'Cli99999' });
  const s = await j('/clinicausuario/SelecionarClinica', { IdUsuario: l.data.id, IdClinica: 1, IdPerfilEscolha: 0 }, l.data.token);
  const a = s.data;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
  page.setDefaultTimeout(20000);
  await page.goto(APP);
  await page.evaluate(a => { localStorage.setItem('_clTk', a.token); localStorage.setItem('_clNm', JSON.stringify(a.nome)); localStorage.setItem('_clId', JSON.stringify(String(a.id))); localStorage.setItem('_clType', JSON.stringify(a.papel)); localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig || [])); }, a);
  await page.goto(APP + '/home'); await page.waitForLoadState('networkidle').catch(() => {});
  const hide = () => page.addStyleTag({ content: '#li_testes{display:none!important;}' });
  const go = async (u) => { await page.goto(APP + u); await page.waitForLoadState('networkidle').catch(() => {}); await hide(); await page.waitForTimeout(900); };
  const shot = (n, full = false) => page.screenshot({ path: path.join(OUT, n + '.png'), fullPage: full });
  const modal = async () => { await page.waitForSelector('.modal.show'); await page.waitForTimeout(500); };
  return { browser, page, go, shot, modal, hide, token: a.token };
}
module.exports = { start };
