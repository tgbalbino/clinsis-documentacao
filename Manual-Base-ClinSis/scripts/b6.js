const { start } = require('./lib');
const path = require('path');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  const dl = path.join(__dirname, 'pdfs');
  await go('/agendamento?idAgenda=33'); await page.waitForTimeout(4000);
  await page.locator('tbody tr').nth(2).locator('button.dropdown-toggle').click(); await page.waitForTimeout(400);
  const [d] = await Promise.all([page.waitForEvent('download', { timeout: 30000 }).catch(() => null), page.locator('.dropdown-menu button:has-text("Horarios Pac.")').click()]);
  await page.waitForTimeout(1500);
  if (d) { await d.saveAs(path.join(dl, 'horarios-paciente.pdf')); console.log('pdf horarios'); }
  else { await page.locator('.modal.show button:has-text("Sim")').click().catch(()=>{}); const d2 = await page.waitForEvent('download', { timeout: 20000 }).catch(()=>null); if (d2) { await d2.saveAs(path.join(dl, 'horarios-paciente.pdf')); console.log('pdf horarios (2)'); } else console.log('sem download'); }
  await go('/relatorio/agenda?idAgenda=33'); await page.waitForTimeout(2500); await shot('e05-relatorio-agenda');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
