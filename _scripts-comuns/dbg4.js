const { abrir } = require('./cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  page.on('console', m => { if (m.type()==='error') console.log('ERR', m.text().slice(0,200)); });
  await ir('/acessos'); await page.waitForTimeout(2500);
  console.log(page.url());
  console.log((await page.locator('body').innerText()).slice(0,400).replace(/\s+/g,' '));
  await shot('_dbg');
  await browser.close();
})();
