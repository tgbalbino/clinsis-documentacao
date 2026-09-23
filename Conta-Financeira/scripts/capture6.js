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
  page.setDefaultTimeout(30000);
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


  await page.goto(`${APP}/cadastro/contasfinanceiras`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);

  // Novo cadastro completo
  await page.click('button:has-text("Novo")');
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(500);
  await page.fill('.modal.show input[maxlength="100"]', 'SICOOB CONTA CORRENTE');
  const selBanco = page.locator('.modal.show select').first();
  const opts = await selBanco.locator('option').all();
  await selBanco.selectOption(await opts[1].getAttribute('value'));
  await page.fill('.modal.show input[maxlength="20"]', '0001');
  await page.fill('.modal.show input[maxlength="30"]', '12345-6');
  await page.locator('.modal.show input[type="text"]').last().fill('clinica@exemplo.com.br');
  await page.waitForTimeout(300);
  await shot(page, '10-novo-cadastro-completo');
  await page.click('.modal.show button:has-text("Salvar")');
  await page.waitForTimeout(1500);
  await esconderMenuTestes();
  await shot(page, '11-lista-com-conta-nova');

  // Formas de pagamento da conta nova (sugestao inicial)
  const linhaNova = page.locator('tr').filter({ hasText: 'SICOOB' }).first();
  await linhaNova.locator('button[title="Formas de pagamento desta conta"]').click();
  await page.waitForTimeout(700);
  await shot(page, '12-formas-conta-nova');
  await page.click('.modal.show button:has-text("Fechar")');
  await page.waitForTimeout(500);

  // Editar (mostra campo Ativo)
  await linhaNova.locator('button.btn-warning').click();
  await page.waitForSelector('.modal.show');
  await page.waitForTimeout(600);
  await shot(page, '13-editar-conta');
  await page.click('.modal.show button:has-text("Fechar")');
  await page.waitForTimeout(500);

  // Tentar excluir CAIXA (tem movimentos)
  const linhaCaixa = page.locator('tr').filter({ hasText: /^\s*CAIXA\s/ }).first();
  await linhaCaixa.locator('button.btn-danger').click();
  await page.waitForTimeout(600);
  await shot(page, '14-confirmar-exclusao-caixa');
  await page.locator('#modalConfirmarExcluirContaFinanceira button:visible', { hasText: 'Sim' }).click();
  await page.waitForTimeout(1500);
  await shot(page, '15-resultado-exclusao-caixa');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
