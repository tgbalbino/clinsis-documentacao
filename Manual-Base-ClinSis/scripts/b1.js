const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  // Nova agenda
  await go('/agenda');
  await page.locator('button:visible:has-text("Novo")').first().click(); await modal();
  await page.locator('.modal.show select').first().selectOption('10'); await page.locator('.modal.show input[type=checkbox]').first().check(); await page.waitForTimeout(300); await page.locator('.modal.show select').nth(2).selectOption({ index: 1 }); await page.waitForTimeout(300);
  await shot('b01-nova-agenda');
  await page.keyboard.press('Escape'); await page.locator('.modal.show button:has-text("Cancelar")').click().catch(()=>{}); await page.waitForTimeout(600);
  // Horarios
  await go('/aux/horarios'); await shot('b02-horarios');
  await page.locator('button:has-text("Gerar Horários")').click(); await modal();
  const ins = page.locator('.modal.show input[mask="00:00"]');
  await ins.nth(0).pressSequentially('0800'); await ins.nth(1).pressSequentially('1800');
  await page.locator('.modal.show select').selectOption('30'); await page.waitForTimeout(300);
  await shot('b03-gerar-horarios');
  await page.locator('.modal.show button:has-text("Cancelar")').click(); await page.waitForTimeout(600);
  // Prof horarios
  await go('/agenda/profissional?idAgenda=33'); await shot('b04-prof-horarios-vazio');
  const sel = page.locator('app-modal-add-profissional-agenda > .row select').first();
  const opts = await sel.locator('option').allTextContents(); console.log(opts.slice(0,8));
  await sel.selectOption({ label: 'Profissional 01' }); await page.waitForTimeout(1500); await shot('b05-prof-horarios-selecionado', true);
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
