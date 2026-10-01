const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/aux/servicos');
  await shot('00-lista-servicos');
  // Reajuste em massa (só prévia; nada é gravado)
  await page.click('button:has-text("Reajustar preços")'); await page.waitForTimeout(1200);
  await shot('00b-reajuste-aberto');
  await page.locator('input[type=number]').first().fill('10');
  await page.click('button:has-text("Calcular prévia")'); await page.waitForTimeout(1500);
  await shot('00c-reajuste-previa');
  console.log('botoes:', (await page.locator('button:visible').allInnerTexts()).map(x => x.trim()).filter(Boolean).join('|'));
  await page.locator('button:has-text("Fechar")').first().click(); await page.waitForTimeout(800); await shot('_pos');
  // Cadastro
  await page.locator('.content-wrapper').getByText('Novo', { exact: true }).first().click(); await page.waitForTimeout(1500);
  await shot('01-cadastro-servico-vazio');
  // Uso em Contrato (contrato aberto)
  await ir('/contrato');
  const N = process.env.CONTRATO || '13';
  await page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp('^' + N + '$') }) }).locator('button[title="Alterar contrato / serviços"]').click();
  await page.waitForSelector('.modal.show'); await page.waitForTimeout(2500);
  await page.locator('.modal.show').getByRole('heading', { name: 'Serviços' }).scrollIntoViewIfNeeded(); await page.waitForTimeout(400);
  await shot('02-contrato-aba-servicos');
  await page.locator('.modal.show .space-between').filter({ hasText: 'Serviços' }).locator('button').click(); await page.waitForTimeout(900);
  const mb = page.locator('.modal.show').last();
  await mb.locator('input[type="text"]').first().fill('Serviço'); await mb.locator('input').first().press('Enter'); await page.waitForTimeout(1200);
  await shot('04-modal-buscar-servico-resultado');
  await mb.locator('table tbody tr').first().locator('button').first().click(); await page.waitForTimeout(700);
  await mb.locator('input[mask="separator.0"]').first().fill('3'); await page.waitForTimeout(400);
  await shot('06-contrato-servico-qtd-preenchida');
  await mb.locator('button:has-text("Salvar")').first().click(); await page.waitForTimeout(1200);
  await shot('07-contrato-servico-adicionado');
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
