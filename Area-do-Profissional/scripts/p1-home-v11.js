// v1.1 (24/09/2026): Home do profissional com os totalizadores (agora sempre visíveis, sem configuração da clínica)
const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot } = await start();
  await go('/home'); await page.waitForTimeout(1500); await shot('p01-home', true);
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
