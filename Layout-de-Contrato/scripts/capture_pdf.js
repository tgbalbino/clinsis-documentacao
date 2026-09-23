const path = require('path');
const { chromium } = require('playwright');

const API = process.env.E2E_API_URL || 'http://localhost:49020/api';
const APP = process.env.E2E_APP_URL || 'http://localhost:4222';
const LOGIN = process.env.E2E_LOGIN || '99999999999';
const SENHA = process.env.E2E_SENHA || 'Cli99999';
const outDir = path.join(__dirname, 'screenshots');

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
  return { token: j2.data.token };
}

(async () => {
  const auth = await loginApi();
  const r = await fetch(`${API}/contratolaiout/obterativo`, { headers: { Authorization: `Bearer ${auth.token}` } });
  const layout = (await r.json()).data;

  const rp = await fetch(`${API}/contratolaiout/previsualizar`, {
    method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${auth.token}` },
    body: JSON.stringify({ LaioutMD: layout.laioutMD })
  });
  console.log('previsualizar status:', rp.status);
  const buf = Buffer.from(await rp.arrayBuffer());
  const fs = require('fs');
  fs.writeFileSync(path.join(outDir, 'exemplo.pdf'), buf);
  console.log('PDF salvo, bytes:', buf.length);

  // renderizar a primeira pagina do PDF como imagem via chromium
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 1300 } });
  await page.goto('file:///' + path.join(outDir, 'exemplo.pdf').replace(/\\/g, '/'));
  await page.waitForTimeout(2500);
  await page.screenshot({ path: path.join(outDir, '05-pdf-exemplo-gerado.png') });
  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
