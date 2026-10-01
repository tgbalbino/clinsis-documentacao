// Parte 2: acerto (Crediário), dispensa da assinatura (liberação administrativa) e fechamento. Uso: CONTRATO=15 node capture_parte2.js
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const N = process.env.CONTRATO || '15';
  const { browser, page, ir, shot } = await abrir(__dirname);
  const modal = () => page.locator('.modal.show').last();
  const sim = () => page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click();
  await ir('/contrato');
  await page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp('^' + N + '$') }) }).locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show'); await page.waitForTimeout(1500);
  await shot('05-contrato-com-servico');

  // Acerto
  await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]'); await page.waitForTimeout(800);
  const tp = page.locator('#tabContratoPagamentos');
  const jaTem = await tp.locator('tbody tr', { hasText: 'Crediário' }).count();
  if (!jaTem) {
  await tp.locator('select').first().selectOption({ label: 'Crediário' }); await page.waitForTimeout(600);
  await tp.locator('button[title^="Preencher"]').click();
  await tp.locator('input[mask="separator.0"]').first().fill('2');
  const datas = tp.locator('input[bsdatepicker]');
  await datas.first().fill('10/10/2026'); await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  await tp.locator('input[mask="separator.4"]').first().fill('1').catch(() => {});
  await page.waitForTimeout(300);
  await shot('09-pagamento-preenchido');
  await tp.locator('button[type="submit"], button[title="Adicionar"]').first().click(); await page.waitForTimeout(1000);
  }
  await shot('10-pagamento-adicionado');

  // Salvar o acerto e reabrir
  await page.locator('.modal.show button:has-text("Salvar")').last().click(); await page.waitForTimeout(2500);
  if (await page.locator('.modal.show').count() === 0) {
    await page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp('^' + N + '$') }) }).locator('button[title="Alterar contrato / serviços"]').click();
    await page.waitForSelector('.modal.show'); await page.waitForTimeout(1500);
  }
  await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]'); await page.waitForTimeout(600);

  // Dispensa da assinatura eletrônica (liberação administrativa)
  const dispensada = /Dispensada/.test(await page.locator('.contrato-opcao-assinatura').first().innerText().catch(() => ''));
  if (!dispensada) {
    await page.click('.modal.show button:has-text("Não assinar")'); await page.waitForTimeout(1200);
    await shot('11-liberacao-dispensa-assinatura');
    await modal().locator('select').selectOption({ index: 1 }); await page.waitForTimeout(400);
    await shot('11b-motivo-selecionado');
    await modal().locator('button:has-text("Dispensar assinatura")').click(); await page.waitForTimeout(1800);
    await page.click('.modal.show button[data-bs-target="#tabContratoPagamentos"]').catch(() => {}); await page.waitForTimeout(500);
    await shot('12-assinatura-dispensada');
  }

  // Fechar contrato
  await page.click('.modal.show button:has-text("Fechar Contrato")'); await page.waitForTimeout(800);
  await shot('14-confirmar-fechar-contrato');
  await sim(); await page.waitForTimeout(2500);
  await shot('15-apos-fechar-contrato');
  await browser.close(); console.log('OK parte 2 (parcial)');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
