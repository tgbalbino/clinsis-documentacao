const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  const t = async (n, f) => { try { await f(); console.log('ok', n); } catch (e) { console.log('FALHA', n, e.message.split('\n')[0]); } };
  const lista = async () => { await go('/prontuario/profissional'); await modal(); await page.locator('.modal.show select').first().selectOption({ label: 'Evolução diária' }); await page.locator('.modal.show button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500); };
  await t('visualizar', async () => { await lista(); const row = page.locator('tbody tr', { hasText: '0000107' }); const bs0 = await row.locator('a,button').evaluateAll(b => b.map(x => x.tagName+'|'+x.className+'|'+(x.getAttribute('title')||''))); console.log(bs0); await row.locator('a').first().click(); await page.waitForLoadState('networkidle'); await page.waitForTimeout(2500); console.log(page.url()); await shot('p06-prontuario-visualizar', true); });
  await t('preencher', async () => { await lista(); const row = page.locator('tbody tr', { hasText: '0000108' }); const bs = await row.locator('a,button').evaluateAll(b => b.map(x => x.tagName+'|'+x.className+'|'+(x.getAttribute('title')||'')+'|'+(x.getAttribute('href')||''))); console.log(bs);
    await row.locator('a.btn-warning, a:has(.fa-edit), a:has(.fa-sticky-note)').first().click(); await page.waitForLoadState('networkidle'); await page.waitForTimeout(2500); console.log(page.url()); await shot('p06c-prontuario-preencher', true); });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
