// Prints 0112/0128/0129: Enviar lembretes (manual), Definir mensagem, Respostas WhatsApp (agenda), aba WhatsApp do paciente
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/aux/whatsapp'); await shot('00-painel-whatsapp', false);
  await ir('/whatsapp/manual'); await page.waitForTimeout(2500);
  console.log('manual: ', (await page.locator('.content-wrapper').innerText()).replace(/\s+/g, ' ').slice(0, 500));
  await shot('01a-manual-hoje-sem-agendamentos', false);
  // procura um dia com agendamentos (somente consulta, pois já passou)
  for (let d = 29; d >= 14; d--) {
    await page.locator('input[type=date]').fill(`2026-09-${d}`); await page.locator('input[type=date]').dispatchEvent('change'); await page.waitForTimeout(1500);
    const t = await page.locator('.content-wrapper p.mb-5').first().innerText().catch(() => '');
    if (!t.startsWith('0 ')) { console.log('dia com dados:', d, t.slice(0, 40)); break; }
  }
  await shot('01-manual-lembretes-do-dia', false);
  await ir('/whatsapp/manual/msg'); await page.waitForTimeout(1500); await shot('02-manual-definir-mensagem', false);
  await ir('/agendamento?idAgenda=31'); await page.waitForTimeout(6000);
  await shot('12a-agenda-botoes', false);
  console.log('botoes agenda:', (await page.locator('.content-wrapper button:visible, .content-wrapper a:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).slice(0, 30).join('|'));
  const resp = page.locator('button[title^="Respostas dos pacientes"]').first();
  console.log('respostas:', await resp.count());
  if (await resp.count()) { await resp.click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(2500); await shot('12-agenda-respostas-whatsapp', false); console.log((await page.locator('.modal.show').innerText()).replace(/\s+/g, ' ').slice(0, 800)); }
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
