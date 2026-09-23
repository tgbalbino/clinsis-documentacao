const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';

const outDir = path.join(__dirname, 'screenshots');
fs.mkdirSync(outDir, { recursive: true });
const shot = (page, name, fullPage = true) => page.screenshot({ path: path.join(outDir, `${name}.png`), fullPage });

async function loginApi() {
  const r1 = await fetch(`${API}/usuario/login`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ Login: LOGIN, Senha: SENHA })
  });
  const j1 = await r1.json();
  if (!j1.success) throw new Error('Login falhou: ' + JSON.stringify(j1));
  const r2 = await fetch(`${API}/clinicausuario/SelecionarClinica`, {
    method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${j1.data.token}` },
    body: JSON.stringify({ IdUsuario: j1.data.id, IdClinica: 1, IdPerfilEscolha: 0 })
  });
  const j2 = await r2.json();
  if (!j2.success) throw new Error('SelecionarClinica falhou: ' + JSON.stringify(j2));
  return {
    token: j2.data.token, nome: j2.data.nome, id: j2.data.id, papel: j2.data.papel,
    clinicaConfig: j2.data.clinicaConfig || [],
  };
}

(async () => {
  const auth = await loginApi();
  console.log('Login OK:', auth.nome);

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
  page.on('console', msg => { if (msg.type() === 'error') console.log('[console error]', msg.text()); });

  const esconderMenuTestes = () => page.addStyleTag({ content: '#li_testes { display: none !important; }' });

  await page.goto(APP);
  await page.evaluate(({ token, nome, id, papel, clinicaConfig }) => {
    localStorage.setItem('_clTk', token);
    localStorage.setItem('_clNm', JSON.stringify(nome));
    localStorage.setItem('_clId', JSON.stringify(String(id)));
    localStorage.setItem('_clType', JSON.stringify(papel));
    localStorage.setItem('_clcfAux', JSON.stringify(clinicaConfig));
  }, auth);
  await esconderMenuTestes();

  // ---------- Tela de configuração da vigência ----------
  console.log('Abrindo config de Vigência de Pagamento...');
  await page.goto(`${APP}/aux/vigenciaprofpagto`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(600);
  await shot(page, '00-vigencia-lista');

  await page.goto(`${APP}/aux/vigenciaprofpagto/gerenciar?IdConfig=2`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(800);
  await shot(page, '01-vigencia-gerenciar-agenda');

  const abaProfissionais = page.locator('a, button').filter({ hasText: 'Profissionais' }).first();
  if (await abaProfissionais.count() > 0) {
    await abaProfissionais.click();
    await page.waitForTimeout(600);
    await shot(page, '02-vigencia-gerenciar-profissionais');
  }

  // ---------- Relatório de Pagamento de Profissionais (sintético) ----------
  console.log('Abrindo Pagamento de Profissionais (relatório sintético)...');
  await page.goto(`${APP}/relatorio/pagamento/profissional/agrupado`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(600);
  await shot(page, '03-relatorio-inicial');

  console.log('Abrindo Filtros e escolhendo agenda vinculada (2026 - Setembro)...');
  await page.click('button:has-text("Filtros")');
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(450);
  const modalFiltro = page.locator('.modal.show');
  await modalFiltro.locator('select').first().selectOption('33'); // IdAgenda 33 = 2026/9, já vinculada
  await shot(page, '04-filtro-agenda-vinculada', false);
  await page.click('.modal.show button:has-text("Filtrar")');
  await page.waitForTimeout(1200);
  await shot(page, '05-resultado-agenda-vinculada');

  console.log('Selecionando uma linha com valor > 0...');
  const checkboxes = page.locator('table tbody tr input[type=checkbox]');
  const qtd = await checkboxes.count();
  console.log('Checkboxes disponíveis:', qtd);
  if (qtd > 0) {
    await checkboxes.first().check();
    await page.waitForTimeout(400);
    await shot(page, '06-linha-selecionada');

    console.log('Abrindo modal Gerar Contas a Pagar...');
    await page.click('button:has-text("Gerar Contas a Pagar")');
    await page.waitForSelector('.modal.show', { timeout: 5000 });
    await page.waitForTimeout(450);

    const modalGerar = page.locator('.modal.show');
    await modalGerar.locator('input[list="pgtoProfPlanoContaList"]').click();
    const opcoesPlano = await page.locator('#pgtoProfPlanoContaList option').all();
    let opPlano = await opcoesPlano[0]?.getAttribute('value');
    for (const o of opcoesPlano) {
      const v = await o.getAttribute('value');
      if (v && v.toLowerCase().includes('honor')) { opPlano = v; break; }
    }
    if (opPlano) {
      await modalGerar.locator('input[list="pgtoProfPlanoContaList"]').fill(opPlano);
      await modalGerar.locator('input[list="pgtoProfPlanoContaList"]').blur();
    }

    await modalGerar.locator('input[list="pgtoProfCentroCustoList"]').click();
    const opCentro = await page.locator('#pgtoProfCentroCustoList option').first().getAttribute('value');
    await modalGerar.locator('input[list="pgtoProfCentroCustoList"]').fill(opCentro);
    await modalGerar.locator('input[list="pgtoProfCentroCustoList"]').blur();

    const hoje = new Date();
    const dataStr = `${String(hoje.getDate()).padStart(2, '0')}/${String(hoje.getMonth() + 1).padStart(2, '0')}/${hoje.getFullYear()}`;
    await modalGerar.locator('input[bsdatepicker]').fill(dataStr);
    await page.keyboard.press('Escape');
    await shot(page, '07-modal-gerar-preenchido', false);

    console.log('Confirmando geração...');
    await page.click('.modal.show button:has-text("Sim / Gerar")');
    await page.waitForTimeout(1500);
    await shot(page, '08-apos-gerar');
  }

  // ---------- Demonstrar erro: agenda NÃO vinculada ----------
  console.log('Testando com uma agenda NÃO vinculada (2026 - Abril, IdAgenda 30)...');
  await page.click('button:has-text("Filtros")');
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(450);
  await page.locator('.modal.show select').first().selectOption('30');
  await page.click('.modal.show button:has-text("Filtrar")');
  await page.waitForTimeout(1200);
  const checkboxes2 = page.locator('table tbody tr input[type=checkbox]');
  const qtd2 = await checkboxes2.count();
  console.log('Checkboxes na agenda não vinculada:', qtd2);
  if (qtd2 > 0) {
    await checkboxes2.first().check();
    await page.waitForTimeout(400);
    await page.click('button:has-text("Gerar Contas a Pagar")');
    await page.waitForSelector('.modal.show', { timeout: 5000 });
    await page.waitForTimeout(450);
    const modalGerar2 = page.locator('.modal.show');
    await modalGerar2.locator('input[list="pgtoProfPlanoContaList"]').click();
    const opcoesPlano2 = await page.locator('#pgtoProfPlanoContaList option').first().getAttribute('value');
    await modalGerar2.locator('input[list="pgtoProfPlanoContaList"]').fill(opcoesPlano2);
    await modalGerar2.locator('input[list="pgtoProfPlanoContaList"]').blur();
    const opcoesCentro2 = await page.locator('#pgtoProfCentroCustoList option').first().getAttribute('value');
    await modalGerar2.locator('input[list="pgtoProfCentroCustoList"]').fill(opcoesCentro2);
    await modalGerar2.locator('input[list="pgtoProfCentroCustoList"]').blur();
    const hoje2 = new Date();
    const dataStr2 = `${String(hoje2.getDate()).padStart(2, '0')}/${String(hoje2.getMonth() + 1).padStart(2, '0')}/${hoje2.getFullYear()}`;
    await modalGerar2.locator('input[bsdatepicker]').fill(dataStr2);
    await page.keyboard.press('Escape');
    await page.click('.modal.show button:has-text("Sim / Gerar")');
    await page.waitForTimeout(1200);
    await shot(page, '09-erro-agenda-nao-vinculada');
  } else {
    await shot(page, '09-agenda-nao-vinculada-sem-linhas');
  }

  await browser.close();
  console.log('OK — screenshots em', outDir);
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
