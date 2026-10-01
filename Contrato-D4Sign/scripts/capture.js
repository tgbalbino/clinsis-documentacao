// Contrato com D4Sign SEM enviar nada de verdade (sem e-mail/assinatura reais).
// Parte A: contrato novo pronto para enviar + janela de confirmação (cancelada).
// Parte B: contrato 8 (assinatura já finalizada em teste anterior na D4Sign Sandbox): histórico, PDF assinado e fechamento.
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const hoje = new Date();
  const dd = String(hoje.getDate()).padStart(2, '0') + '/' + String(hoje.getMonth() + 1).padStart(2, '0') + '/' + hoje.getFullYear();
  const nao = () => page.locator('button:visible', { hasText: /^\s*N[ãa]o\s*$/ }).first().click();

  await ir('/aux/d4sign'); await shot('00-config-d4sign');

  // Parte A
  await ir('/contrato');
  let idc = process.env.CONTRATO;
  if (!idc) {
  await page.click('button:has-text("Novo")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  let criado = false;
  for (let tent = 0; tent < 12 && !criado; tent++) {
    await page.click('.modal.show button:has(.fa-search)'); await page.waitForSelector('#modalPesquisaPacienteContrato.show'); await page.waitForTimeout(500);
    const mp = page.locator('#modalPesquisaPacienteContrato');
    await mp.locator('input').first().fill('Paciente 00'); await mp.locator('input').first().press('Enter'); await page.waitForTimeout(1500);
    await mp.locator('table tbody tr').nth(tent).locator('button[title="selecionar"]').click(); await page.waitForTimeout(800);
    await page.locator('.modal.show input[bsdatepicker]').first().fill(dd); await page.keyboard.press('Escape'); await page.waitForTimeout(300);
    await page.click('.modal.show button:has-text("Salvar")'); await page.waitForTimeout(2500);
    criado = /N[ºo°]\s*\d+/.test(await page.locator('.modal.show .modal-title').first().innerText());
  }
  await page.waitForTimeout(3000);
  const secao = page.locator('.modal.show .space-between').filter({ hasText: 'Serviços' });
  await secao.locator('button').click(); await page.waitForTimeout(800);
  const ms = page.locator('#modalServico, .modal.show').last();
  await ms.locator('input').first().fill('Serviço 001'); await ms.locator('input').first().press('Enter'); await page.waitForTimeout(1200);
  await ms.locator('table tbody tr').first().locator('button').click(); await page.waitForTimeout(600);
  await ms.locator('input[mask="separator.0"]').fill('1');
  await ms.locator('input[mask="separator.2"]').fill('20,00'); await page.waitForTimeout(300);
  await ms.locator('button:has-text("Salvar")').click(); await page.waitForTimeout(1200);
  await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]'); await page.waitForTimeout(800);
  const tp = page.locator('#tabContratoPagamentos');
  await tp.locator('select').first().selectOption({ label: 'Pix' }); await page.waitForTimeout(500);
  await tp.locator('button[title^="Preencher"]').click();
  await tp.locator('button[type="submit"], button[title="Adicionar"]').first().click(); await page.waitForTimeout(1200);
  await page.locator('.modal.show button:has-text("Salvar")').last().click(); await page.waitForTimeout(2500);
  idc = (await page.locator('.modal.show .modal-title').first().innerText()).match(/\d+/)[0];
  console.log('contrato criado', idc);
  await page.locator('.modal.show button:has-text("Salvar")').last().click(); await page.waitForTimeout(2500);
  }
  if (await page.locator('.modal.show').count() === 0) {
    await ir('/contrato');
    await page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp('^' + idc + '$') }) }).locator('button[title="Alterar contrato / serviços"]').click();
    await page.waitForSelector('.modal.show'); await page.waitForTimeout(2500);
  }
  console.log('botoes:', (await page.locator('.modal.show button:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).join('|'));
  await shot('01-contrato-pronto-enviar-assinatura');
  if (await page.locator('.modal.show button:has-text("Enviar para assinatura")').count() > 0) {
    await page.click('.modal.show button:has-text("Enviar para assinatura")'); await page.waitForTimeout(900);
    await shot('02-confirmar-enviar-assinatura');
    await nao(); await page.waitForTimeout(600);   // NÃO envia
  }

  // Parte B: contrato 8
  await ir('/contrato');
  await page.locator('tr').filter({ has: page.locator('td', { hasText: /^8$/ }) }).locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show'); await page.waitForTimeout(2500);
  await shot('03-assinatura-finalizada');
  await page.click('.modal.show button[data-bs-target="#tabContratoAssinatura"]'); await page.waitForTimeout(800);
  await shot('05-historico-assinatura');
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
