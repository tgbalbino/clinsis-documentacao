const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  await go('/agendamento?idAgenda=33'); await page.waitForTimeout(4000);
  const close = async () => { await page.locator('.modal.show button:has-text("Fechar"), .modal.show button:has-text("Cancelar")').first().click().catch(()=>{}); await page.waitForTimeout(700); };
  await shot('d01-agendamento');
  // menu engrenagem
  await page.locator('tbody tr').nth(2).locator('button.dropdown-toggle').click(); await page.waitForTimeout(500);
  await shot('d02-agendamento-menu-linha');
  await page.keyboard.press('Escape'); await page.mouse.click(1000,60); await page.waitForTimeout(400);
  // verde +
  await page.locator('tbody tr button.btn-success:visible').first().click(); await page.waitForTimeout(1500);
  await shot('d03-agendar-paciente', true);
  console.log(page.url(), await page.locator('.modal.show').count());
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
