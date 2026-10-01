// Ver sessões (todas as sessões registradas do período) -> 50-ver-sessoes-todas.png
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/agenda/dashboard'); await page.waitForTimeout(1500);
  await page.locator('input[bsdatepicker]').first().fill('01/09/2026'); await page.keyboard.press('Escape');
  await page.locator('input[bsdatepicker]').nth(1).fill('30/09/2026'); await page.keyboard.press('Escape');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(2500);
  await page.click('button:has-text("Ver sessões")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(1800);
  await shot('50-ver-sessoes-todas', false);
  console.log((await page.locator('.modal.show').last().innerText()).replace(/\s+/g, ' ').slice(0, 200));
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
