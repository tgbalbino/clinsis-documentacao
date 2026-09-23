const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  await go('/agendamento?idAgenda=33'); await page.waitForTimeout(4000);
  await page.locator('tbody tr button.btn-success:visible').first().click(); await modal();
  await page.locator('.modal.show input[type=text]').first().fill('Paciente 000'); await page.keyboard.press('Enter'); await page.waitForTimeout(1500);
  await shot('d04-vincular-busca');
  await page.locator('.modal.show tbody tr').first().locator('button').first().click(); await page.waitForTimeout(1500);
  await shot('d05-agendar-form', true);
  console.log(await page.locator('.modal.show').count());
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
