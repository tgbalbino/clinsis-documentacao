const { open, go, shot } = require('./lib');
(async () => {
  const { browser, page } = await open('99999999999', 'Cli99999');
  const sel = (i) => page.locator('select').nth(i);
  // sequenciais
  await go(page, '/relatorio/agenda/atendimentos-sequenciais');
  await sel(0).selectOption({ label: '2026 - SETEMBRO' });
  await page.locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await shot(page, '06-sequenciais-resultado');
  console.log('seq:', (await page.locator('thead tr').first().innerText().catch(()=>'')).replace(/\s+/g,' '), '||', (await page.locator('tbody tr').allInnerTexts()).map(s=>s.replace(/\s+/g,' ')).slice(0,6).join(' || '));
  // producao
  await go(page, '/relatorio/prontuario/producao');
  console.log('prod opts rel:', (await sel(0).locator('option').allInnerTexts()).join(','));
  await sel(1).selectOption({ label: 'Anamnese' });
  const ins = page.locator('input[bsdatepicker]');
  await ins.nth(0).fill('01/09/2026'); await page.keyboard.press('Escape');
  await ins.nth(1).fill('30/09/2026'); await page.keyboard.press('Escape');
  await page.locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await shot(page, '07-producao-resultado');
  console.log('prod:', (await page.locator('tbody tr, tfoot tr').allInnerTexts()).map(s=>s.replace(/\s+/g,' ')).join(' || '));
  await browser.close();
})();
