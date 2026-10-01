// Checkin de Paciente (v2.0, 30/09/2026): usa o agendamento de teste de hoje (Daniel, TO, 20:30, particular/PROPRIO).
// ATENÇÃO: confirma um check-in de verdade (gera Conta a Receber baixada). Rode uma vez.
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot, chamar } = await abrir(__dirname);
  const toasts = async () => (await page.locator('.toast-message').allInnerTexts()).join(' | ');
  const modal = () => page.locator('.modal.show').last();

  await ir('/paciente/checkin'); await page.waitForTimeout(1500);
  await shot('00-lista-inicial', false);
  await page.click('button:has-text("Realizar Check-In")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(1000);
  await shot('01-modal-codigo-barras', false);
  await page.click('button:has-text("Pesquisa Manual")'); await page.waitForTimeout(1200);
  const inp = modal().locator('input[placeholder="pesquisar paciente"]');
  await inp.fill('Daniel'); await inp.press('Enter'); await page.waitForTimeout(1800);
  await shot('02-pesquisa-resultado', false);
  await modal().locator('tbody tr').first().locator('button').last().click(); await page.waitForTimeout(3000);
  console.log('toast1:', await toasts());
  await shot('03-paciente-com-agenda-hoje', false);

  await modal().locator('tbody input[type=checkbox]').first().check(); await page.waitForTimeout(600);
  // tipo de preço
  const tipo = modal().locator('select').filter({ has: page.locator('option', { hasText: 'Valor normal' }) }).first();
  await tipo.selectOption({ label: 'Valor normal' }); await page.waitForTimeout(800);
  await shot('04-horarios-marcados-com-valor', false);

  // forma de pagamento: Dinheiro + valor restante
  const forma = modal().locator('select').filter({ has: page.locator('option', { hasText: 'Dinheiro' }) }).first();
  console.log('formas:', (await forma.locator('option').allInnerTexts()).join('|'));
  await forma.selectOption({ label: 'Dinheiro' }); await page.waitForTimeout(400);
  await modal().locator('button[title="Usar valor restante"]').click(); await page.waitForTimeout(500);
  await shot('05-pagamento-preenchido', false);
  await modal().locator('button:has-text("Adicionar")').first().click(); await page.waitForTimeout(800);
  await shot('06-pagamento-adicionado', false);

  // cartão de crédito com parcelas (apenas mostra o campo; não adiciona)
  const forma2 = modal().locator('select').filter({ has: page.locator('option', { hasText: 'Dinheiro' }) }).first();
  await forma2.selectOption({ label: 'Car. Crédito' }).catch(() => {}); await page.waitForTimeout(600);
  await shot('06b-cartao-credito-parcelas', false);
  await forma2.selectOption({ label: 'Dinheiro' }).catch(() => {}); await page.waitForTimeout(300);

  await modal().locator('button:has-text("Confirmar Check-In")').click(); await page.waitForTimeout(3500);
  console.log('toast2:', await toasts());
  await shot('07-apos-confirmar-checkin', false);

  // Contas a Receber gerada
  await ir('/financeiro/contareceber'); await page.waitForTimeout(2500);
  await shot('08-conta-a-receber-gerada-pelo-checkin', false);
  console.log('linhas CR:', (await page.locator('tbody tr').first().innerText().catch(() => '')).replace(/\s+/g, ' ').slice(0, 300));
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
