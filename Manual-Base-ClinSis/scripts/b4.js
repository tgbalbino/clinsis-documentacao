const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  await go('/agendamento?idAgenda=33'); await page.waitForTimeout(4000);
  const cancel = async () => { await page.locator('.modal.show button:has-text("Cancelar"), .modal.show button:has-text("Fechar")').last().click().catch(()=>{}); await page.waitForTimeout(800); };
  await page.locator('tbody tr button.btn-success:visible').first().click(); await modal();
  await page.locator('.modal.show input[type=text]').first().fill('Paciente 000'); await page.keyboard.press('Enter'); await page.waitForTimeout(1500);
  await page.locator('.modal.show tbody tr').first().locator('button').first().click(); await page.waitForTimeout(1500);
  const sels = page.locator('.modal.show select');
  const n = await sels.count();
  for (let i = 0; i < n; i++) {
    const o = await sels.nth(i).locator('option').allTextContents();
    console.log(i, o.slice(0, 6).join(' | '));
    if (o.length > 1) await sels.nth(i).selectOption({ index: 1 }).catch(()=>{});
  }
  await page.locator('.modal.show input[type=number]').first().fill('4');
  await page.waitForTimeout(500); await shot('d06-agendar-form-preenchido');
  await cancel();
  // Sessao
  await page.locator('tbody tr').nth(2).locator('button.dropdown-toggle').click(); await page.waitForTimeout(400);
  await page.locator('.dropdown-menu button:has-text("Sessão")').first().click(); await modal(); await shot('d07-sessao'); await cancel();
  // Filtros
  await page.locator('button:has-text("Filtros")').first().click(); await modal(); await shot('d08-filtros'); await cancel();
  // Relatorios
  await page.locator('button:has-text("Relatórios")').first().click(); await modal(); await shot('d09-relatorios');
  await page.locator('.modal.show select').selectOption('2'); await page.waitForTimeout(300); await shot('d09b-relatorios-presenca'); await cancel();
  // Colunas
  await page.locator('button:has-text("Colunas")').first().click(); await modal(); await shot('d10-colunas'); await cancel();
  await page.locator('button:has-text("Exportar")').first().click(); await modal(); await shot('d11-exportar'); await cancel();
  await page.locator('button:has-text("Pesquisa rápida")').first().click(); await modal(); await shot('d12-pesquisa-rapida'); await cancel();
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
