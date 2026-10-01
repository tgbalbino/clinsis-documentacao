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

function hojeDigitos() {
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

  // ---- Novo contrato para "Teste Contrato D4SIGN" (email real cadastrado) ----
  await page.goto(`${APP}/contrato`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);

  await page.click('button:has-text("Novo")');
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(500);

  await page.click('.modal.show button:has(.fa-search)');
  await page.waitForSelector('#modalPesquisaPacienteContrato.show', { timeout: 5000 });
  await page.waitForTimeout(500);
  const modalPaciente = page.locator('#modalPesquisaPacienteContrato');
  await modalPaciente.locator('input').first().fill('Teste Contrato D4SIGN');
  await modalPaciente.locator('input').first().press('Enter');
  await page.waitForTimeout(900);
  await modalPaciente.locator('table tbody tr').first().locator('button[title="selecionar"]').click();
  await page.waitForTimeout(600);
  await shot(page, '00-paciente-selecionado');

  await page.locator('.modal.show input').nth(3).fill(hojeDigitos());
  await page.waitForTimeout(300);
  await page.click('.modal.show button:has-text("Salvar")');
  await page.waitForTimeout(1200);

  if (await page.locator('.modal.show').count() === 0) {
    await page.locator('tr').first().locator('button[title="Alterar contrato / serviços"]').click();
    await page.waitForSelector('.modal.show', { timeout: 5000 });
    await page.waitForTimeout(600);
  }

  const idContratoCriado = await page.evaluate(() => {
    const match = document.querySelector('.modal.show .modal-title')?.textContent?.match(/Nº\s*(\d+)/);
    return match ? Number(match[1]) : null;
  });
  console.log('Contrato criado:', idContratoCriado);

  // ---- Adicionar servico ----
  const secaoServicos = page.locator('.modal.show .space-between').filter({ hasText: 'Serviços' });
  await secaoServicos.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await secaoServicos.locator('button').click();
  await page.waitForTimeout(600);
  const modalServico = page.locator('#modalServico, .modal.show').last();
  await modalServico.locator('input').first().fill('Serviço 001');
  await modalServico.locator('input').first().press('Enter');
  await page.waitForTimeout(900);
  await modalServico.locator('table tbody tr').first().locator('button').click();
  await page.waitForTimeout(500);
  await modalServico.locator('input[mask="separator.0"]').fill('1');
  await modalServico.locator('input[mask="separator.2"]').fill('25,00');
  await page.waitForTimeout(300);
  await modalServico.locator('button:has-text("Salvar")').click();
  await page.waitForTimeout(700);

  // ---- Pagamento (via API direta - mascara de data nao propaga por automacao, ver nota tecnica) ----
  await page.evaluate(async ({ idContrato, apiUrl }) => {
    const token = localStorage.getItem('_clTk');
    await fetch(`${apiUrl}/ContratoPagamento/inserir`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body: JSON.stringify({
        IdContrato: idContrato, IdPagamentoForma: 2, Valor: 25.00, QuantidadeParcelas: 1,
        DataPrimeiraParcela: new Date().toISOString(), DataUltimaParcela: new Date().toISOString(),
        TaxaJurosMensal: 0, Observacao: ''
      })
    });
  }, { idContrato: idContratoCriado, apiUrl: API });
  await page.waitForTimeout(500);
  await page.click('.modal.show button.btn-secondary:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(500);
  await page.reload();
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);

  const linhaNova = page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp(`^${idContratoCriado}$`) }) });
  await linhaNova.locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(600);
  await shot(page, '01-contrato-pronto-enviar-assinatura');

  // ---- Enviar para assinatura (D4Sign real) ----
  await page.click('.modal.show button:has-text("Enviar para assinatura")');
  await page.waitForTimeout(600);
  await shot(page, '02-confirmar-enviar-assinatura');
  await page.click('.modal.show .btn-primary:has-text("Sim")').catch(async () => {
    await page.click('app-modal-confirmacao .btn-primary');
  });
  await page.waitForTimeout(6000); // chamadas reais a D4Sign (upload PDF, criar signatario, enviar)
  await shot(page, '03-apos-enviar-assinatura');

  await browser.close();
  console.log('OK - contrato enviado para assinatura:', idContratoCriado);
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
