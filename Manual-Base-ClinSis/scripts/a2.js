const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  await go('/acessos');
  const row = () => page.locator('tbody tr').nth(2); await page.waitForSelector('tbody tr td');
  await row().locator('button:visible').first().click(); await page.waitForTimeout(400);
  await page.locator('button:visible:has-text("Editar")').first().click(); await modal(); await shot('c11-acesso-editar');
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  await go('/acessos'); await page.waitForSelector('tbody tr td'); await page.waitForTimeout(500);
  await row().locator('button:visible').first().click(); await page.waitForTimeout(400);
  await page.locator('a:visible:has-text("Permissões"), button:visible:has-text("Permissões")').first().click();
  await page.waitForLoadState('networkidle').catch(()=>{}); await page.waitForTimeout(1200); await shot('c12-acesso-permissoes');
  console.log(page.url());
  await go('/acessos'); await page.waitForSelector('tbody tr td'); await page.waitForTimeout(500);
  await row().locator('button:visible').first().click(); await page.waitForTimeout(400);
  await page.locator('a:visible:has-text("bloquear dias"), button:visible:has-text("bloquear dias")').first().click();
  await page.waitForLoadState('networkidle').catch(()=>{}); await page.waitForTimeout(1200); await shot('c13-acesso-bloqueio-dias');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
