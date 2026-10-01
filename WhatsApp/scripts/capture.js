// Prints do WhatsApp (painel, Meta, paciente, agenda). Não envia mensagens nem testa conexão.
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/aux/whatsapp'); await shot('00-painel-whatsapp', false);
  await ir('/aux/whatsapp-meta'); await page.waitForTimeout(2500);
  await shot('03-meta-configuracao');
  await page.locator('button:has-text("Ver texto")').first().click(); await page.waitForTimeout(1500);
  await shot('04-meta-ver-texto', false);
  console.log('texto:', (await page.locator('.modal.show').last().innerText().catch(() => '')).replace(/\s+/g, ' ').slice(0, 600));
  await page.locator('.modal.show button:has-text("Fechar"), .modal.show .btn-close, .modal.show button:has-text("OK")').first().click().catch(() => page.keyboard.press('Escape')); await page.waitForTimeout(700);
  // abre um filtro (Atendimento particular)
  await page.locator('text=Atendimento particular?').first().click().catch(() => {}); await page.waitForTimeout(800);
  await shot('05-meta-filtros', false);
  await page.locator('button:has-text("Simular próximos envios")').click(); await page.waitForTimeout(4000);
  await shot('06-meta-simulacao');
  for (const [aba, arq] of [['Templates', '07-meta-templates'], ['Disparos', '08-meta-disparos'], ['Mensagens', '09-meta-mensagens']]) {
    await page.locator('.nav-link, button', { hasText: aba }).first().click(); await page.waitForTimeout(2500); await shot(arq, false);
  }
  // Paciente: aba WhatsApp e lista
  await ir('/paciente'); await page.waitForTimeout(1500);
  await shot('10-pacientes-lista', false);
  console.log('botoes paciente:', (await page.locator('.content-wrapper button:visible, .content-wrapper a:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).slice(0, 14).join('|'));
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
