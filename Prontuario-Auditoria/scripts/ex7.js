const { open, go, shot } = require('./lib');
const path = require('path');
(async () => {
  const { browser, page } = await open('99999999999', 'Cli99999');
  const sel = (i) => page.locator('select').nth(i);
  await go(page, '/relatorio/prontuario/auditoria');
  await sel(0).selectOption({ label: '2026 - SETEMBRO' }); await sel(1).selectOption({ label: 'Evolução diária' });
  await page.locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await shot(page, '11-exportar-botao');
  const dl = page.waitForEvent('download', { timeout: 20000 }).catch(() => null);
  await page.locator('button:has-text("Exportar")').click();
  const d = await dl; if (d) { const f = path.join(__dirname, 'auditoria.csv'); await d.saveAs(f); console.log('download', d.suggestedFilename()); console.log(require('fs').readFileSync(f, 'utf8').slice(0, 400)); } else console.log('sem download; toasts:', (await page.locator('.toast-message').allInnerTexts()).join('|'));
  await browser.close();
})();
