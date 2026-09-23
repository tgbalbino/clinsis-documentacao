const { open, go, shot } = require('./lib');
(async () => {
  const { browser, page } = await open('99999999999', 'Cli99999');
  const sel = (i) => page.locator('select').nth(i);
  await go(page, '/relatorio/prontuario/auditoria');
  await sel(0).selectOption({ label: '2026 - SETEMBRO' });
  await sel(1).selectOption({ label: 'Anamnese' });
  await page.locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await shot(page, '04-sintetico');
  console.log('sint:', (await page.locator('tbody tr, tfoot tr').allInnerTexts()).map(s=>s.replace(/\s+/g,' ')).join(' || '));
  console.log('opts metodo:', (await sel(3).locator('option').allInnerTexts()).join(','), '| tags:', (await sel(4).locator('option').allInnerTexts()).join(','), '| rel:', (await sel(5).locator('option').allInnerTexts()).join(','));
  await sel(5).selectOption({ index: 1 }); await page.waitForTimeout(500);
  await page.locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await shot(page, '05-analitico');
  console.log('anal:', (await page.locator('tbody tr, tfoot tr').allInnerTexts()).map(s=>s.replace(/\s+/g,' ')).join(' || '));
  await browser.close();
})();
