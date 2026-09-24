const { start } = require('./lib');
const path = require('path'); const fs = require('fs');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  const dl = path.join(__dirname, 'pdfs'); fs.mkdirSync(dl, { recursive: true });
  await go('/agendamento?idAgenda=33'); await page.waitForTimeout(4000);
  const cancel = async () => { await page.locator('.modal.show button:has-text("Cancelar"), .modal.show button:has-text("Fechar"), .modal.show button:has-text("Não")').last().click().catch(()=>{}); await page.waitForTimeout(800); };
  const baixar = async (opt, nome) => {
    await page.locator('button:has-text("Relatórios")').first().click(); await modal();
    await page.locator('.modal.show select').selectOption(opt);
    const [d] = await Promise.all([page.waitForEvent('download', { timeout: 30000 }), page.locator('.modal.show button:has-text("Baixar documento")').click()]);
    await d.saveAs(path.join(dl, nome)); console.log('pdf', nome, d.suggestedFilename());
    await page.waitForTimeout(1000);
  };
  await baixar('1', 'atendimento-diario.pdf');
  await baixar('2', 'presenca-ausencia.pdf');
  // marcacao sessao dia
  await page.locator('button:has-text("Relatórios")').first().click(); await modal();
  await page.locator('.modal.show select').selectOption('3');
  await page.locator('.modal.show button:has-text("Visualizar")').click(); await page.waitForTimeout(3000);
  await shot('e03-marcacao-sessao-dia'); console.log('modals', await page.locator('.modal.show').count());
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
