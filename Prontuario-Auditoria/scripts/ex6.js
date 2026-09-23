const { open, go, shot } = require('./lib');
(async () => {
  const { browser, page } = await open('99999999999', 'Cli99999');
  const sel = (i) => page.locator('select').nth(i);
  await go(page, '/relatorio/prontuario/auditoria');
  await sel(0).selectOption({ label: '2026 - SETEMBRO' });
  await sel(1).selectOption({ label: 'Evolução diária' });
  await page.locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await shot(page, '10-sintetico-evolucao');
  console.log('evol:', (await page.locator('tbody tr, tfoot tr').allInnerTexts()).map(s=>s.replace(/\s+/g,' ')).join(' || '));
  await browser.close();
})();
