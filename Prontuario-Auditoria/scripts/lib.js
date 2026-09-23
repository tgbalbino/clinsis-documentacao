const path = require('path');
const { chromium } = require('playwright');
const API = 'http://localhost:49020/api', APP = 'http://localhost:4222';
const outDir = path.join(__dirname, 'screenshots');
exports.shot = (page, name, fullPage = false) => page.screenshot({ path: path.join(outDir, `${name}.png`), fullPage });
exports.open = async (login, senha) => {
  const r1 = await (await fetch(`${API}/usuario/login`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ Login: login, Senha: senha }) })).json();
  const j2 = await (await fetch(`${API}/clinicausuario/SelecionarClinica`, { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${r1.data.token}` }, body: JSON.stringify({ IdUsuario: r1.data.id, IdClinica: 1, IdPerfilEscolha: 0 }) })).json();
  const a = j2.data;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
  page.setDefaultTimeout(20000);
  await page.goto(APP);
  await page.evaluate((a) => {
    localStorage.setItem('_clTk', a.token); localStorage.setItem('_clNm', JSON.stringify(a.nome));
    localStorage.setItem('_clId', JSON.stringify(String(a.id))); localStorage.setItem('_clType', JSON.stringify(a.papel));
    localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig || []));
  }, { token: a.token, nome: a.nome, id: a.id, papel: a.papel, clinicaConfig: a.clinicaConfig });
  await page.addStyleTag({ content: '#li_testes { display: none !important; }' });
  return { browser, page };
};
exports.go = async (page, url) => { await page.goto(APP + url); await page.waitForLoadState('load'); await page.waitForTimeout(1800); await page.addStyleTag({ content: '#li_testes { display: none !important; }' }); };
