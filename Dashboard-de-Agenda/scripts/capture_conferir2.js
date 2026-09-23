const path = require('path');
const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';
const outDir = path.join(__dirname, 'screenshots');
const shot = (page, name, fullPage = true) => page.screenshot({ path: path.join(outDir, `${name}.png`), fullPage });
const ID_AGENDA = 33;

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

  // 1) Agenda do mes: filtrar coluna "Sessão 1" = PRESENTE
  await page.goto(`${APP}/agendamento?idAgenda=${ID_AGENDA}`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(1000);
  await shot(page, '22-agendamento-grade-mes');

  // Abrir modal de Filtros e marcar "Sessão 1" = PRESENTE
  await page.click('button:has-text("Filtros")');
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(600);
  const modalFiltro = page.locator('.modal.show').last();
  const selS1 = modalFiltro.locator('select[ng-reflect-model]', { hasText: '' }).first();
  const labelS1 = modalFiltro.locator('label', { hasText: 'Sessão 1' }).first();
  const selectS1 = labelS1.locator('xpath=following-sibling::select').first();
  const opts = await selectS1.locator('option').all();
  for (const o of opts) {
    const t = (await o.textContent() || '').trim();
    if (t === 'PRESENTE') { await selectS1.selectOption(await o.getAttribute('value')); break; }
  }
  await page.waitForTimeout(300);
  await shot(page, '23a-modal-filtro-sessao1-presente');
  await modalFiltro.locator('button:has-text("Filtrar")').first().click();
  await page.waitForTimeout(1000);
  await page.locator('.modal.show button:has-text("Fechar")').click().catch(() => {});
  await page.waitForTimeout(500);
  await esconderMenuTestes();
  await shot(page, '23-agendamento-filtro-sessao1-presente');

  // 2) Relatorio Agenda - Qtd Marcacao
  await page.goto(`${APP}/relatorio/agenda/qtdmarcacao`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(1000);
  const modalQtd = page.locator('.modal.show').last();
  if (await modalQtd.count() > 0) {
    const selAgenda = modalQtd.locator('select').first();
    const optsA = await selAgenda.locator('option').all();
    for (const o of optsA) {
      const t = (await o.textContent() || '').trim();
      if (t.includes('2026') && t.toUpperCase().includes('SETEMBRO')) { await selAgenda.selectOption(await o.getAttribute('value')); break; }
    }
    await page.waitForTimeout(300);
    await modalQtd.locator('button:has-text("Buscar"), button:has-text("Pesquisar"), button:has-text("Filtrar")').first().click();
    await page.waitForTimeout(1200);
  }
  await esconderMenuTestes();
  await shot(page, '24-relatorio-qtd-marcacao');

  // 3) Relatorio Guia Faturamento
  await page.goto(`${APP}/relatorio/guiafaturamento`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(800);
  await shot(page, '25-relatorio-guia-faturamento');

  // 4) Relatorio Contas a Receber - Recebimentos
  await page.goto(`${APP}/relatorio/conta-receber/recebimentos`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(800);
  await shot(page, '26-relatorio-recebimentos');

  // 5) Agenda Profissional (grade de horarios / capacidade)
  await page.goto(`${APP}/agenda/profissional?idAgenda=${ID_AGENDA}`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(800);
  const selProf = page.locator('select').first();
  if (await selProf.count() > 0) {
    const opts = await selProf.locator('option').all();
    if (opts.length > 1) await selProf.selectOption(await opts[1].getAttribute('value'));
    await page.waitForTimeout(800);
  }
  await esconderMenuTestes();
  await shot(page, '27-agenda-profissional-horarios');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
