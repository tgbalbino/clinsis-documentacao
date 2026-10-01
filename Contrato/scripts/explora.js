const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/contrato');
  await page.locator('tr').filter({ has: page.locator('td', { hasText: /^13$/ }) }).locator('button[title="Baixar ou Marcar como assinado"]').click();
  await page.waitForSelector('.modal.show'); await page.waitForTimeout(900);
  await shot('11-modal-download-assinar');
  console.log((await page.locator('.modal.show button:visible').allInnerTexts()).join('|'));
  await browser.close();
})().catch(e => console.log('FALHA', e.message.slice(0,300)));
