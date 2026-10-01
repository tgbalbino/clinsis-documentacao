// Helper comum das capturas (Playwright): login via API + token no localStorage.
const path = require('path');
const { chromium } = require('C:/Projetos/W_Clinica/FrontClinica/node_modules/playwright');
const API = process.env.E2E_API_URL || 'http://localhost:49041/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '43660781045';
const SENHA = process.env.E2E_SENHA || 'Cli43660';

async function loginApi(login = LOGIN, senha = SENHA, idClinica = 1) {
  const r1 = await fetch(`${API}/usuario/login`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ Login: login, Senha: senha }) });
  const j1 = await r1.json();
  const r2 = await fetch(`${API}/clinicausuario/SelecionarClinica`, { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${j1.data.token}` }, body: JSON.stringify({ IdUsuario: j1.data.id, IdClinica: idClinica, IdPerfilEscolha: 0 }) });
  const j2 = await r2.json();
  return { token: j2.data.token, nome: j2.data.nome, id: j2.data.id, papel: j2.data.papel, clinicaConfig: j2.data.clinicaConfig || [], permissoes: j2.data.permissoes || j2.data.Permissoes || [] };
}

async function abrir(dirScripts, opts = {}) {
  const outDir = path.join(dirScripts, 'screenshots');
  const auth = await loginApi(opts.login, opts.senha);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: opts.viewport || { width: 1600, height: 1000 } });
  page.setDefaultTimeout(20000);
  // o front tem a API fixa em 49020 (usada pelo Visual Studio do usuário); aqui redireciona para a API isolada de documentação
  await page.route('http://localhost:49020/**', (route) => route.continue({ url: route.request().url().replace('localhost:49020', 'localhost:49041') }));
  const esconder = () => page.addStyleTag({ content: '#li_testes { display: none !important; }' }).catch(() => {});
  await page.goto(APP);
  await page.evaluate((a) => {
    localStorage.setItem('_clTk', a.token);
    localStorage.setItem('_clNm', JSON.stringify(a.nome));
    localStorage.setItem('_clId', JSON.stringify(String(a.id)));
    localStorage.setItem('_clType', JSON.stringify(a.papel));
    localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig));
    localStorage.setItem('_clk', JSON.stringify(a.permissoes || []));
  }, auth);
  const ir = async (rota) => { await page.goto(`${APP}${rota}`); await page.waitForLoadState('networkidle'); await esconder(); await page.waitForTimeout(700); };
  const shot = async (name, fullPage = true) => { await esconder(); await page.mouse.move(1000, 990); await page.waitForTimeout(200); await page.screenshot({ path: path.join(outDir, `${name}.png`), fullPage }); };
  const chamar = async (metodo, rota, corpo) => {
    const r = await fetch(`${API}/${rota}`, { method: metodo, headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${auth.token}` }, body: corpo === undefined ? undefined : JSON.stringify(corpo) });
    const t = await r.text(); try { return JSON.parse(t); } catch { return t; }
  };
  return { browser, page, auth, ir, shot, esconder, chamar };
}
module.exports = { abrir, loginApi, API, APP };

// ng-select: abre, digita e escolhe a primeira opção que contém o texto
async function ngSelecionar(page, locator, texto) {
  await locator.click();
  await locator.locator('input').first().pressSequentially(texto, { delay: 60 }).catch(async () => { await page.keyboard.type(texto, { delay: 60 }); });
  await page.waitForSelector('.ng-dropdown-panel .ng-option', { timeout: 8000 });
  await page.waitForTimeout(500);
  await page.locator('.ng-dropdown-panel .ng-option').first().click();
  await page.waitForTimeout(300);
}
module.exports.ngSelecionar = ngSelecionar;

// input com <datalist>: escolhe a primeira opção que contém o trecho (ou a n-ésima se trecho vazio)
async function datalistSelecionar(page, input, trecho = '', idx = 0) {
  const lista = await input.getAttribute('list');
  const valores = await page.evaluate((id) => [...document.querySelectorAll(`#${id} option`)].map(o => o.value), lista);
  const t = trecho.toLowerCase();
  const v = typeof idx === 'function' ? valores.find(idx) : (t ? valores.find(x => x.toLowerCase().includes(t)) : valores[idx]);
  if (!v) throw new Error(`datalist ${lista}: sem opção para "${trecho}" (${valores.length} opções)`);
  await input.click(); await input.fill(v); await input.press('Tab'); await page.waitForTimeout(400);
  return v;
}
module.exports.datalistSelecionar = datalistSelecionar;
