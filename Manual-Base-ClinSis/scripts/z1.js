const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  await go('/acessos'); await page.waitForSelector('tbody tr td');
  await page.addStyleTag({ content: 'tbody td:nth-child(3){filter:blur(7px)}' }); await page.waitForTimeout(400);
  await shot('c08b-acessos-lista');
  await page.locator('button:visible:has-text("Novo")').first().click(); await modal(); await shot('c09b-acesso-novo');
  await go('/home'); await shot('a01-home');
  await go('/agenda'); await shot('b00-agenda-lista');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
