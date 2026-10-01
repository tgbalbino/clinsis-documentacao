// v1.5 (01/10/2026): lista de Agenda (Mais ações), Relatório Agenda sem botão duplicado
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/agenda'); await page.waitForTimeout(1200);
  await page.locator('button:has-text("Mais ações")').first().click(); await page.waitForTimeout(600);
  await shot('b00b-agenda-mais-acoes', false);
  await ir('/relatorio/agenda?idAgenda=31'); await page.waitForTimeout(2500); await shot('e05-relatorio-agenda', false);
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 300)); process.exit(1); });
