const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/paciente/checkin');
  await page.click('button:has-text("Realizar Check-In")'); await page.waitForTimeout(1000);
  await page.click('button:has-text("Pesquisa Manual")'); await page.waitForTimeout(1200);
  const m = page.locator('.modal.show').last();
  await m.locator('input[placeholder="pesquisar paciente"]').fill('Daniel'); await m.locator('input[placeholder="pesquisar paciente"]').press('Enter'); await page.waitForTimeout(1500);
  await m.locator('tbody tr').first().locator('button').last().click(); await page.waitForTimeout(3000);
  await shot('_ck1', false);
  console.log((await page.locator('.modal.show').last().innerText().catch(()=>'')).replace(/\s+/g,' ').slice(0,700));
  console.log((await page.locator('.modal.show button:visible').allInnerTexts()).map(x=>x.trim()).join('|'));
  await browser.close();
})().catch(e => console.log('FALHA', e.message.slice(0,300)));
