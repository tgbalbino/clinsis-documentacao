// Capturas da revisão v1.1 (26/09/2026): como o filtro de Status muda o quantitativo de sessões.
// Gera prints para Pagamento de Profissionais E para Cobrança de Paciente (mesma regra de contagem).
// Uso: NODE_PATH=<FrontClinica>/node_modules node capture_status.js
const path = require('path');
const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4200';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';
const PAG_DIR = path.join(__dirname, 'screenshots');
const COB_DIR = path.join(__dirname, '..', '..', 'Cobranca-de-Paciente', 'scripts', 'screenshots');
const IDAGENDA = '33'; // 2026 - Setembro

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
  const esconderMenuTestes = () => page.addStyleTag({ content: '#li_testes { display: none !important; }' });
  const shot = async (dir, name, fullPage = true) => { await page.mouse.move(5, 995); return page.screenshot({ path: path.join(dir, `${name}.png`), fullPage }); };

  await page.goto(APP);
  await page.evaluate((a) => {
    localStorage.setItem('_clTk', a.token);
    localStorage.setItem('_clNm', JSON.stringify(a.nome));
    localStorage.setItem('_clId', JSON.stringify(String(a.id)));
    localStorage.setItem('_clType', JSON.stringify(a.papel));
    localStorage.setItem('_clcfAux', JSON.stringify(a.clinicaConfig));
  }, auth);

  async function abrir(rota) {
    await page.goto(`${APP}${rota}`);
    await page.waitForLoadState('networkidle');
    await esconderMenuTestes();
    await page.waitForTimeout(600);
  }

  async function abrirFiltros() {
    await page.click('button:has-text("Filtros")');
    await page.waitForSelector('.modal.show', { timeout: 5000 });
    await page.waitForTimeout(500);
    await page.locator('.modal.show select').first().selectOption(IDAGENDA);
  }

  // Marca exatamente os status pedidos (ids do checkbox: <prefixo><valor>)
  async function definirStatus(prefixo, valores) {
    await page.evaluate(({ prefixo, valores }) => {
      for (let v = 1; v <= 6; v++) {
        const el = document.getElementById(prefixo + v);
        if (el && el.checked !== valores.includes(v)) el.click();
      }
    }, { prefixo, valores });
    await page.waitForTimeout(200);
  }

  async function abrirDropdownStatus() {
    await page.locator('.modal.show button.dropdown-toggle').first().click();
    await page.waitForTimeout(400);
  }

  async function filtrar() {
    // fecha o dropdown (se aberto) antes de filtrar
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(200);
    if (!(await page.locator('.modal.show').count())) return;
    await page.click('.modal.show button:has-text("Filtrar")');
    await page.waitForTimeout(1500);
  }

  async function rodar(rota, prefixo, valores, dir, nomeResultado, nomeFiltro) {
    await abrir(rota);
    await abrirFiltros();
    await definirStatus(prefixo, valores);
    if (nomeFiltro) {
      await abrirDropdownStatus();
      await shot(dir, nomeFiltro, false);
      await page.locator('.modal.show label:has-text("Agenda")').first().click(); // fecha dropdown
      await page.waitForTimeout(300);
    }
    await page.click('.modal.show button:has-text("Filtrar")');
    await page.waitForTimeout(1500);
    await shot(dir, nomeResultado);
  }

  const TODOS = [1, 2, 3, 4, 5, 6], PRESENTE = [3], AUSENTES = [4, 5];

  // ---------- Pagamento de Profissionais ----------
  const PAG_SINT = '/relatorio/pagamento/profissional/agrupado', PAG_ANAL = '/relatorio/pagamento/profissional';
  await rodar(PAG_SINT, 'statusPagtoSintetico', TODOS, PAG_DIR, '18-sintetico-todos-status', '17-filtro-status-todos');
  await rodar(PAG_SINT, 'statusPagtoSintetico', PRESENTE, PAG_DIR, '20-sintetico-somente-presente', '19-filtro-status-somente-presente');
  await rodar(PAG_SINT, 'statusPagtoSintetico', AUSENTES, PAG_DIR, '21-sintetico-somente-ausentes');
  await rodar(PAG_ANAL, 'statusPagtoAnalitico', AUSENTES, PAG_DIR, '22-analitico-somente-ausentes');

  // ---------- Cobrança de Paciente ----------
  const COB_SINT = '/relatorio/valorreceber/agrupado', COB_ANAL = '/relatorio/valorreceber';
  await rodar(COB_SINT, 'statusAgrupado', TODOS, COB_DIR, '14-sintetico-todos-status', '13-filtro-status-todos');
  await rodar(COB_SINT, 'statusAgrupado', PRESENTE, COB_DIR, '16-sintetico-somente-presente', '15-filtro-status-somente-presente');
  await rodar(COB_SINT, 'statusAgrupado', AUSENTES, COB_DIR, '17-sintetico-somente-ausentes');
  await rodar(COB_ANAL, 'status', AUSENTES, COB_DIR, '18-analitico-somente-ausentes');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
