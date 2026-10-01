// Prints v1.4 do Manual Base (tarefas 0112, 0129-0131, 0135): lista de Profissional, cadastros com Novo no cabeçalho,
// lista de Agenda, Enviar lembretes e Definir mensagem.
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/profissional/lista'); await page.waitForTimeout(2500);
  await shot('c04-profissional-lista', false);
  console.log('prof lista botoes:', (await page.locator('.content-wrapper button:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).join('|'));
  await ir('/profissional/cadastro'); await shot('c05-profissional-cadastro', true);
  await ir('/paciente/cadastro'); await shot('c07-paciente-cadastro', true);
  await ir('/agenda'); await page.waitForTimeout(1500); await shot('b00-agenda-lista', false);
  console.log('agenda lista botoes:', (await page.locator('.content-wrapper button:visible, .content-wrapper a:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).slice(0, 20).join('|'));
  await ir('/agendamento?idAgenda=31'); await page.waitForTimeout(6000); await shot('d01-agendamento', false);
  await ir('/whatsapp/manual'); await page.waitForTimeout(1500);
  await page.locator('input[type=date]').fill('2026-09-29'); await page.locator('input[type=date]').dispatchEvent('change'); await page.waitForTimeout(1800);
  await shot('d13-whatsapp-do-dia', false);
  await page.locator('a:has-text("Definir mensagem")').first().click(); await page.waitForTimeout(2500);
  const pre = page.locator('button:has-text("Pré-visualizar")');
  if (await pre.count()) { await pre.first().click(); await page.waitForTimeout(1500); }
  await shot('d14-whatsapp-definir-mensagem', false);
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
