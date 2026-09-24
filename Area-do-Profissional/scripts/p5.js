const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot } = await start();
  await go('/paciente/lista'); await page.waitForSelector('tbody tr td'); await page.addStyleTag({ content: 'tbody td{filter:blur(6px)}' }); await page.waitForTimeout(500); await shot('p04-pacientes');
  await go('/perfil'); await page.waitForTimeout(1200); await page.addStyleTag({ content: 'input[type=email], input[type=text], .form-control{filter:blur(6px)} ' }); await shot('p10-perfil');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
