const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  const blur = () => page.addStyleTag({ content: 'tbody td:not(:first-child):not(:last-child){filter:blur(6px)}' });
  const t = async (n, f) => { try { await f(); console.log('ok', n); } catch (e) { console.log('FALHA', n, e.message.split('\n')[0]); } };
  await t('home', async () => { await go('/home'); await shot('p01-home', true); });
  await t('agenda', async () => { await go('/agenda'); await shot('p02-agenda'); });
  await t('resumida', async () => {
    await page.locator('a:has-text("Acessar")').first().click(); await page.waitForLoadState('networkidle'); await page.waitForTimeout(2500);
    console.log(page.url()); await blur(); await shot('p03-agenda-resumida'); });
  await t('pacientes-dia', async () => { await go('/agenda/pacientesdodia'); await blur(); await page.locator('button:has-text("Pesquisar")').first().click().catch(()=>{}); await page.waitForTimeout(1500); await shot('p03b-pacientes-dia'); });
  await t('pacientes', async () => { await go('/paciente/lista'); await blur(); await page.waitForTimeout(500); await shot('p04-pacientes'); });
  await t('prontuarios', async () => {
    await go('/prontuario/profissional'); await modal(); await shot('p05-prontuarios-filtro');
    const sel = page.locator('.modal.show select').first(); const ops = await sel.locator('option').allTextContents(); console.log(ops);
    await sel.selectOption({ index: 1 }); await page.locator('.modal.show button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
    await blur(); await shot('p05b-prontuarios-lista'); });
  await t('textopadrao', async () => { await go('/prontuario/textopadrao'); await page.waitForTimeout(800); await shot('p07-textos-padrao');
    await page.locator('button:visible:has-text("Novo"), a:visible:has-text("Novo")').first().click(); await page.waitForTimeout(1200); await shot('p07b-texto-padrao-novo'); });
  await t('atendimento', async () => { await go('/atendimento'); await page.waitForTimeout(800); await shot('p08-atendimento'); });
  await t('protocolo', async () => { await go('/protocolo'); await page.waitForTimeout(1500); await shot('p09-protocolo'); });
  await t('perfil', async () => { await go('/perfil'); await page.waitForTimeout(1000); await shot('p10-perfil'); });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
