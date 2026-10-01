const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/aux/d4sign'); await shot('00-config-d4sign');
  await ir('/contrato');
  await page.locator('tr').filter({ has: page.locator('td', { hasText: /^8$/ }) }).locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show'); await page.waitForTimeout(2500);
  await shot('_c8');
  console.log((await page.locator('.modal.show button:visible').allInnerTexts()).map(x=>x.trim()).join('|'));
  await browser.close();
})().catch(e => console.log('FALHA', e.message.slice(0,300)));
