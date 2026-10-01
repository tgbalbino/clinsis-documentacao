const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/whatsapp/manual'); await page.waitForTimeout(2000);
  await shot('d13-whatsapp-do-dia', false);
  await page.locator('button:has-text("Definir mensagem"), a:has-text("Definir mensagem")').first().click(); await page.waitForTimeout(2500);
  console.log(page.url());
  console.log((await page.locator('.content-wrapper').innerText()).replace(/\s+/g, ' ').slice(0, 900));
  const pre = page.locator('button:has-text("Pré-visualizar")');
  if (await pre.count()) { await pre.first().click(); await page.waitForTimeout(1500); }
  await shot('d14-whatsapp-definir-mensagem', false);
  await ir('/relatorios'); await shot('d15-relatorios-painel', false);
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
