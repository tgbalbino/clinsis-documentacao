const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/contrato');
  await page.locator('tr').filter({ has: page.locator('td', { hasText: /^8$/ }) }).locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show'); await page.waitForTimeout(2500);
  await page.click('.modal.show button:has-text("Fechar Contrato")'); await page.waitForTimeout(900);
  await shot('04a-confirmar-fechar');
  await page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click(); await page.waitForTimeout(3000);
  await shot('04-contrato-fechado-automaticamente');
  await page.locator('.modal.show button:has-text("Fechar")').last().click().catch(() => {}); await page.waitForTimeout(600);
  await ir('/financeiro/contareceber');
  await page.click('button:has-text("Filtro rápido")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(500);
  await page.locator('.modal.show input').first().fill('Ana'); await page.locator('.modal.show button:has-text("Filtrar")').click(); await page.waitForTimeout(1800);
  await shot('06-conta-a-receber-gerada');
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
