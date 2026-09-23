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

function hojeComBarras() {
  const d = new Date();
  const dd = String(d.getDate()).padStart(2, '0');
  const mm = String(d.getMonth() + 1).padStart(2, '0');
  return `${dd}/${mm}/${d.getFullYear()}`;
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

  await page.goto(`${APP}/contrato`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '00-lista-contratos');

  // ---- Novo contrato ----
  await page.click('button:has-text("Novo")');
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(500);
  await shot(page, '01-novo-contrato-vazio');

  // precisa escolher paciente primeiro
  await page.click('.modal.show button:has(.fa-search)');
  await page.waitForSelector('#modalPesquisaPacienteContrato.show', { timeout: 5000 });
  await page.waitForTimeout(500);
  const modalPaciente = page.locator('#modalPesquisaPacienteContrato');
  await modalPaciente.locator('input').first().fill('Paciente 000');
  await modalPaciente.locator('input').first().press('Enter');
  await page.waitForTimeout(900);
  await modalPaciente.locator('table tbody tr').first().locator('button[title="selecionar"]').click();
  await page.waitForTimeout(600);
  await shot(page, '02-paciente-selecionado');

  await page.locator('.modal.show input').nth(3).fill(hojeDigitos());
  await page.waitForTimeout(300);
  await page.click('.modal.show button:has-text("Salvar")');
  await page.waitForTimeout(1200);
  await shot(page, '03-contrato-criado');

  if (await page.locator('.modal.show').count() === 0) {
    await page.locator('table tbody tr').first().locator('button[title="Alterar contrato / serviços"]').click();
    await page.waitForSelector('.modal.show', { timeout: 5000 });
    await page.waitForTimeout(600);
    await shot(page, '03b-contrato-reaberto');
  }

  // ---- Adicionar servico ----
  const secaoServicos = page.locator('.modal.show .space-between').filter({ hasText: 'Serviços' });
  await secaoServicos.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await shot(page, '03c-secao-servicos-vazia');
  await secaoServicos.locator('button').click();
  await page.waitForTimeout(600);
  await shot(page, '04-buscar-servico');

  const modalServico = page.locator('#modalServico, .modal.show').last();
  await modalServico.locator('input').first().fill('Serviço 001');
  await modalServico.locator('input').first().press('Enter');
  await page.waitForTimeout(900);
  await shot(page, '04b-servico-pesquisado');
  await modalServico.locator('table tbody tr').first().locator('button').click();
  await page.waitForTimeout(500);
  await shot(page, '05-servico-selecionado-form');
  await modalServico.locator('input[mask="separator.0"]').fill('2');
  await modalServico.locator('input[mask="separator.2"]').fill('20,00');
  await page.waitForTimeout(300);
  await shot(page, '06-servico-preenchido');
  await modalServico.locator('button:has-text("Salvar")').click();
  await page.waitForTimeout(700);
  await shot(page, '07-servico-adicionado');

  // ---- Aba Pagamentos ----
  await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]');
  await page.waitForTimeout(500);
  const tabPgto = page.locator('#tabContratoPagamentos');
  await page.waitForFunction(() => {
    const sel = document.querySelector('#tabContratoPagamentos select');
    return sel && sel.options.length > 1;
  }, { timeout: 10000 });
  const selectForma = tabPgto.locator('select').first();
  const opcoesForma = await selectForma.locator('option').all();
  let valorForma = null;
  for (const o of opcoesForma) {
    const t = (await o.textContent() || '').toLowerCase();
    if (t.includes('cart')) { valorForma = await o.getAttribute('value'); break; }
  }
  await selectForma.selectOption(valorForma);
  await tabPgto.locator('input[mask="separator.2"]').first().fill('40,00');
  await tabPgto.locator('input[mask="separator.0"]').first().fill('1');
  const campoParcela = tabPgto.locator('input[mask="00/00/0000"]').first();
  await campoParcela.click();
  await campoParcela.pressSequentially(hojeDigitos(), { delay: 150 });
  await page.waitForTimeout(500);
  await shot(page, '08-pagamento-preenchido');

  // A mascara dd/mm/aaaa nao propaga o ngModel de forma confiavel via automacao;
  // grava a condicao de pagamento direto pela API (mesmo endpoint que o botao usaria)
  // para garantir a data da 1a parcela, e recarrega a tela para os prints finais.
  const idContratoCriado = await page.evaluate(() => {
    const match = document.querySelector('.modal.show .modal-title')?.textContent?.match(/Nº\s*(\d+)/);
    return match ? Number(match[1]) : null;
  });
  await page.evaluate(async ({ idContrato, apiUrl }) => {
    const token = localStorage.getItem('_clTk');
    await fetch(`${apiUrl}/ContratoPagamento/inserir`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body: JSON.stringify({
        IdContrato: idContrato,
        IdPagamentoForma: 2,
        Valor: 40.00,
        QuantidadeParcelas: 1,
        DataPrimeiraParcela: new Date().toISOString(),
        TaxaJurosMensal: 0,
        Observacao: ''
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
  await page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp(`^${idContratoCriado}$`) }) })
    .locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(600);
  await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]');
  await page.waitForTimeout(500);
  await shot(page, '09-pagamento-adicionado');
  await page.click('.modal.show button.btn-secondary:has-text("Fechar")');
  await page.waitForTimeout(500);

  // ---- Assinar (manual) ----
  const linhaNova = page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp(`^${idContratoCriado}$`) }) });
  await linhaNova.locator('button[title="Baixar ou Marcar como assinado"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(400);
  await shot(page, '11-modal-download-assinar');
  await page.click('.modal.show button:has-text("Marcar como assinado")');
  await page.waitForTimeout(800);
  await page.click('.modal.show button:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(400);
  await shot(page, '12-lista-apos-assinar');

  // ---- Fechar Contrato (gera as parcelas em Contas a Receber) ----
  await linhaNova.locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(600);
  await shot(page, '13-cadastro-assinado-pronto-fechar');
  await page.click('.modal.show button:has-text("Fechar Contrato")');
  await page.waitForTimeout(600);
  await shot(page, '14-confirmar-fechar-contrato');
  await page.click('#modalFecharContrato button:has-text("Sim")');
  await page.waitForTimeout(1500);
  await shot(page, '15-apos-fechar-contrato');
  await page.click('.modal.show button.btn-secondary:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(400);

  // ---- Verificar parcela gerada em Contas a Receber ----
  await page.goto(`${APP}/financeiro/contareceber`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(500);
  await page.click('button:has-text("Filtros")');
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(450);
  await page.click('.modal.show button:has-text("Buscar")');
  await page.waitForTimeout(1000);
  await page.click('.modal.show button:has-text("Fechar")').catch(() => {});
  await page.waitForTimeout(400);
  await shot(page, '16-conta-a-receber-gerada-pelo-contrato');

  // ---- Contratos vencendo (a parcela gerada vence hoje, entra na janela padrao de 30 dias) ----
  await page.goto(`${APP}/contrato?vencendo=1`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await shot(page, '17-contratos-vencendo');

  // ---- Renovar o contrato recem fechado ----
  await page.goto(`${APP}/contrato`);
  await page.waitForLoadState('networkidle');
  await esconderMenuTestes();
  await page.waitForTimeout(700);
  await linhaNova.locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show', { timeout: 5000 });
  await page.waitForTimeout(600);
  await shot(page, '18-contrato-fechado-antes-renovar');
  await page.click('.modal.show button:has-text("Renovar")');
  await page.waitForTimeout(600);
  await shot(page, '19-confirmar-renovar');
  await page.click('#modalRenovarContrato button:has-text("Sim")');
  await page.waitForTimeout(1200);
  await shot(page, '20-apos-renovar-lista');

  await browser.close();
  console.log('OK - contrato criado:', idContratoCriado);
})().catch(e => { console.error('FALHA:', e.message, e.stack); process.exit(1); });
