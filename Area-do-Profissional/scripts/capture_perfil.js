const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname, { login: '55555555555', senha: 'Cli55555' });
  await ir('/perfil'); await page.waitForTimeout(1500);
  console.log(page.url());
  await shot('p10-perfil', false);
  console.log((await page.locator('.content-wrapper').innerText()).replace(/\s+/g, ' ').slice(0, 500));
  await browser.close();
})().catch(e => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
