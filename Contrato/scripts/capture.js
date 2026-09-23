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

function hoje() {
  const d = new Date();
  const dd = String(d.getDate()).padStart(2, '0');
  const mm = String(d.getMonth() + 1).padStart(2, '0');
  return `${dd}${mm}${d.getFullYear()}`;
}

(async () => {
  const auth = await loginApi();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1100 } });
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

  // ---- Lista de contratos ----
  await page.goto(`${APP}/contrato`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '00-lista-contratos');

  // ---- Abrir contrato 14 (Paciente 000, Ativo, nao assinado, nao fechado) ----
  const linha14 = page.locator('tr').filter({ has: page.locator('td', { hasText: /^14$/ }) });
  await linha14.locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(600);
  await shot(page, '01-cadastro-dados-contrato');

  // ---- Aba Serviços ja mostrada na propria aba Dados do Contrato (rolar pra ver) ----
  await page.locator('.modal.show').getByRole('heading', { name: 'Serviços' }).scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await shot(page, '02-servicos-cadastrados');

  // ---- Aba Acertos / Pagamentos ----
  await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]');
  await page.waitForTimeout(500);
  await shot(page, '03-pagamentos-antes');

  // remover condicao de pagamento existente (sem data de 1a parcela) e recriar com data de hoje
  const modal = page.locator('.modal.show');
  const linhaPgto = modal.locator('table').last().locator('tbody tr').first();
  const temPgto = await linhaPgto.locator('button.btn-danger').count();
  if (temPgto > 0) {
    await linhaPgto.locator('button.btn-danger').click();
    await page.waitForTimeout(400);
  }

  const tabPgto = page.locator('#tabContratoPagamentos');
  const selectForma = tabPgto.locator('select').first();
  const opcoesForma = await selectForma.locator('option').all();
  let valorForma = null;
  for (const o of opcoesForma) {
    const t = (await o.textContent() || '').toLowerCase();
    if (t.includes('cart')) { valorForma = await o.getAttribute('value'); break; }
  }
  await selectForma.selectOption(valorForma || (await opcoesForma[1]?.getAttribute('value')));
  await tabPgto.locator('input[mask="separator.2"]').first().fill('40,00');
  await tabPgto.locator('input[mask="separator.0"]').first().fill('1');
  await tabPgto.locator('input[mask="00/00/0000"]').first().fill(hoje());
  await page.waitForTimeout(300);
  await shot(page, '04-pagamento-preenchido');
  await tabPgto.locator('button[title="Adicionar"]').click();
  await page.waitForTimeout(500);
  await shot(page, '05-pagamento-adicionado');

  // ---- Assinar (fora do modal principal, na listagem) ----
  await modal.locator('button:has-text("Fechar")').last().click();
  await page.waitForTimeout(500);
  await esconderMenuTestes();
  await linha14.locator('button[title="Baixar ou Marcar como assinado"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(400);
  await shot(page, '06-modal-download-assinar');
  await page.click('.modal.show button:has-text("Marcar como assinado")');
  await page.waitForTimeout(800);
  await page.click('.modal.show button:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(400);
  await shot(page, '07-lista-apos-assinar');

  // ---- Reabrir contrato e Fechar Contrato ----
  await linha14.locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(600);
  await shot(page, '08-cadastro-assinado-pronto-fechar');

  await page.click('.modal.show button:has-text("Fechar Contrato")');
  await page.waitForSelector('.modal-confirmacao, .modal.show:has-text("Deseja fechar este contrato")', { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(500);
  await shot(page, '09-confirmar-fechar-contrato');
  await page.click('.modal.show button:has-text("Sim")');
  await page.waitForTimeout(1200);
  await shot(page, '10-apos-fechar-contrato');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
