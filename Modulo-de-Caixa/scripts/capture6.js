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

  // ---- Tentativa de fechar com solicitacao pendente (mostra o bloqueio) ----
  await page.goto(`${APP}/caixa`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await page.click('button:has-text("Fechar Caixa")');
  await page.waitForTimeout(1500);
  await shot(page, '17-bloqueio-fechar-com-solicitacao-pendente');

  // ---- Tela de Solicitacoes: aprovar o cancelamento ----
  await page.goto(`${APP}/caixas/solicitacoes`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '18-solicitacoes-pendentes');

  await page.locator('tr').filter({ hasText: 'Suprimento' }).locator('button:has-text("Cancelar")').click();
  await page.waitForTimeout(600);
  await shot(page, '19-solicitacoes-confirmar-cancelamento');
  await page.locator('button:visible', { hasText: 'Sim' }).click();
  await page.waitForTimeout(1200);
  await shot(page, '20-solicitacoes-apos-aprovar');

  // ---- Voltar pro caixa e fechar de verdade ----
  await page.goto(`${APP}/caixa`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '21-extrato-apos-cancelamento-aprovado');

  await page.click('button:has-text("Fechar Caixa")');
  await page.waitForTimeout(800);
  await shot(page, '14-modal-fechar-caixa-resumo');
  await page.click('.meuModalContainer button:has-text("Confirmar")');
  await page.waitForTimeout(1200);
  await shot(page, '15-apos-fechar-caixa');

  // ---- Meus Caixas ----
  await page.waitForTimeout(500);
  await shot(page, '16-meus-caixas-lista');

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
