// v1.1 (24/09/2026): lista de agendas com os botões renomeados (Horários/Acessar) e o novo layout de Horários do profissional
const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot } = await start();
  await go('/agenda'); await shot('b00-agenda-lista');

  // Primeiro acesso: apresentação do novo layout
  await go('/agenda/profissional?idAgenda=33');
  await page.waitForSelector('.ap-boasvindas'); await page.waitForTimeout(500);
  await shot('b04-prof-horarios-apresentacao');
  await page.locator('.ap-boasvindas button:has-text("Próximo")').click(); await page.waitForTimeout(500);
  await shot('b04b-prof-horarios-trocar-layout');
  await page.locator('.ap-balao button:has-text("Pular")').click(); await page.waitForTimeout(500);

  // Profissional 01, Seg e Qua, período da manhã marcado
  const sel = page.locator('#apnProfissional');
  const opts = await sel.locator('option').allTextContents();
  const alvo = opts.find(o => o.trim().startsWith('Profissional 01'));
  await sel.selectOption({ label: alvo }); await page.waitForTimeout(2000);
  for (const d of ['Seg', 'Qua']) await page.locator('.apn-dia', { hasText: d }).first().click();
  const manha = page.locator('.apn-periodo', { hasText: 'Manhã' });
  await manha.locator('button:has-text("marcar período")').click(); await page.waitForTimeout(400);
  await page.setViewportSize({ width: 1600, height: 1480 }); await page.waitForTimeout(400);
  await shot('b05-prof-horarios-selecionado');
  await page.setViewportSize({ width: 1600, height: 900 }); await page.evaluate(() => window.scrollTo(0, 0));

  // Mais ações
  await page.locator('button:has-text("Mais ações")').click(); await page.waitForTimeout(400);
  await page.locator('.apn-menu-lista').scrollIntoViewIfNeeded();
  await shot('b06-prof-horarios-mais-acoes');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
