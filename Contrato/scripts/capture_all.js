// Captura consolidada do Contrato (sem D4Sign). Usa o paciente "Paciente 0005".
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot, chamar } = await abrir(__dirname);
  const hoje = new Date();
  const dd = String(hoje.getDate()).padStart(2, '0') + '/' + String(hoje.getMonth() + 1).padStart(2, '0') + '/' + hoje.getFullYear();
  const modal = () => page.locator('.modal.show').last();
  const sim = () => page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click();

  // Contratos abertos de Paciente 0005 de execuções anteriores são cancelados via API? (não há rota segura) -> reutiliza se existir
  await ir('/contrato');
  await shot('00-lista-contratos');
  await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(700);
  await shot('00b-filtros');
  await page.locator('.modal.show button:has-text("Fechar")').first().click(); await page.waitForTimeout(500);

  // Novo contrato
  await page.click('button:has-text("Novo")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  await shot('01-novo-contrato-vazio');
  let criado = false;
  for (let tent = 0; tent < 8 && !criado; tent++) {
    await page.click('.modal.show button:has(.fa-search)'); await page.waitForSelector('#modalPesquisaPacienteContrato.show'); await page.waitForTimeout(500);
    const mp = page.locator('#modalPesquisaPacienteContrato');
    await mp.locator('input').first().fill('Paciente 00'); await mp.locator('input').first().press('Enter'); await page.waitForTimeout(1500);
    await mp.locator('table tbody tr').nth(tent).locator('button[title="selecionar"]').click(); await page.waitForTimeout(800);
    await page.locator('.modal.show input[bsdatepicker]').first().fill(dd); await page.keyboard.press('Escape'); await page.waitForTimeout(300);
    if (tent === 0) await shot('02-paciente-selecionado');
    await page.click('.modal.show button:has-text("Salvar")'); await page.waitForTimeout(2500);
    criado = /N[ºo°]\s*\d+/.test(await page.locator('.modal.show .modal-title').first().innerText());
    console.log('tentativa', tent, 'criado', criado); await shot('_t' + tent);
  }
  await page.waitForTimeout(3000);
  await shot('03-contrato-criado');

  // Serviço
  const secao = page.locator('.modal.show .space-between').filter({ hasText: 'Serviços' });
  await secao.locator('button').click(); await page.waitForTimeout(800);
  await shot('04-buscar-servico');
  const ms = page.locator('#modalServico, .modal.show').last();
  await ms.locator('input').first().fill('Serviço 001'); await ms.locator('input').first().press('Enter'); await page.waitForTimeout(1200);
  await ms.locator('table tbody tr').first().locator('button').click(); await page.waitForTimeout(600);
  await ms.locator('input[mask="separator.0"]').fill('2');
  await ms.locator('input[mask="separator.2"]').fill('20,00'); await page.waitForTimeout(300);
  await shot('06-servico-preenchido');
  await ms.locator('button:has-text("Salvar")').click(); await page.waitForTimeout(1000);
  await shot('07-servico-adicionado');

  // Pagamento
  await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]'); await page.waitForTimeout(700);
  const tp = page.locator('#tabContratoPagamentos');
  await page.waitForFunction(() => { const s = document.querySelector('#tabContratoPagamentos select'); return s && s.options.length > 1; }, { timeout: 10000 });
  console.log('tab pagamento botoes:', (await tp.locator('button:visible').evaluateAll(a => a.map(e => (e.title || e.innerText).trim()))).join('|'));
  await shot('08-pagamento-tab');
  await browser.close(); console.log('OK parte 1');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
