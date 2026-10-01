const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/paciente/lista'); await page.waitForTimeout(2500);
  await shot('10-pacientes-lista', false);
  console.log('botoes:', (await page.locator('.content-wrapper button:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).slice(0, 14).join('|'));
  const linha = page.locator('tbody tr').filter({ hasText: 'Paciente 0006' }).first();
  await linha.locator('button, a').first().click(); await page.waitForTimeout(3000);
  console.log(page.url());
  const aba = page.locator('button.nav-link:has-text("WhatsApp")');
  console.log('aba whatsapp:', await aba.count());
  if (await aba.count()) { await aba.first().click(); await page.waitForTimeout(1500); await shot('11-paciente-aba-whatsapp', false); }
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
