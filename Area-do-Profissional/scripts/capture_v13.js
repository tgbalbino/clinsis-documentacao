// v1.3: menu Agenda do profissional (0135), Pacientes do dia com Respostas WhatsApp (0110/0112), Perfil (0122). Login de profissional.
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname, { login: '55555555555', senha: 'Cli55555' });
  const blur = () => page.addStyleTag({ content: 'tbody td:not(:first-child):not(:last-child){filter:blur(6px)}' });
  await ir('/agenda'); await shot('p02-agenda', false);
  console.log('botoes agenda:', (await page.locator('.content-wrapper a:visible, .content-wrapper button:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).slice(0, 8).join('|'));
  await page.locator('tr', { hasText: 'Atual' }).locator('a[title="Abrir a minha agenda deste mês"]').first().click(); await page.waitForLoadState('networkidle'); await page.waitForTimeout(2500);
  console.log(page.url()); console.log('resumida botoes:', (await page.locator('.content-wrapper button:visible, .content-wrapper a:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).slice(0, 14).join('|'));
  await blur(); await shot('p03-agenda-resumida', false);
  await ir('/agenda/pacientesdodia'); await blur();
  for (let d = 30; d >= 14; d--) {
    const dt = page.locator('input[bsdatepicker]').first();
    await dt.fill(`${d}/09/2026`); await dt.press('Tab');
    await page.locator('button:has-text("Pesquisar")').first().click().catch(() => {}); await page.waitForTimeout(1300);
    if (await page.locator('tbody tr', { hasText: /[0-9][0-9]:[0-9][0-9]/ }).count() > 0) { console.log('dia com dados', d); break; }
  }
  await blur(); await shot('p03b-pacientes-dia', false);
  const resp = page.locator('button:has-text("Respostas WhatsApp")').first();
  console.log('respostas:', await resp.count());
  if (await resp.count()) { await resp.click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(2200); await shot('p03c-respostas-whatsapp', false); }
  await ir('/perfil'); await page.waitForTimeout(1200);
  await page.addStyleTag({ content: 'input[type=email], input[type=text], .form-control{filter:blur(6px)}' }); await shot('p10-perfil', false);
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
