const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';
const NOVA_URL = process.argv[2];
if (!NOVA_URL) { console.error('Uso: node atualizar_webhook.js <url-tunel>'); process.exit(1); }

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

  await page.goto(`${APP}/aux/d4sign`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(800);

  await page.fill('#d4signWebhookUrl', `${NOVA_URL}/api/integracaod4sign/webhook`);
  await page.click('#d4signAmbiente'); // no-op, garante foco fora do campo
  await page.click('button:has-text("Testar conexão")');
  await page.waitForTimeout(2500);
  await page.screenshot({ path: 'webhook-testado.png', fullPage: true });

  await page.click('button:has-text("Salvar configuração")');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: 'webhook-salvo.png', fullPage: true });

  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
