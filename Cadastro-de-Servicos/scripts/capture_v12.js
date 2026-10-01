// v1.2: lista, reajuste (com o limite de gravação) e cadastro com Novo no cabeçalho. Não grava nada.
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/aux/servicos');
  await shot('00-lista-servicos');
  await page.click('button:has-text("Reajustar preços")'); await page.waitForTimeout(1200);
  await shot('00b-reajuste-aberto');
  await page.locator('input[type=number]').first().fill('10');
  await page.click('button:has-text("Calcular prévia")'); await page.waitForTimeout(1500);
  await shot('00c-reajuste-previa');
  await page.locator('input[type=number]').first().fill('99999999');
  await page.click('button:has-text("Calcular prévia")'); await page.waitForTimeout(1200);
  await shot('00d-reajuste-acima-do-limite');
  console.log('alerta:', (await page.locator('.toast-message, .alert').allInnerTexts()).join(' | ').slice(0, 400));
  await ir('/aux/servicos');
  await page.locator('.content-wrapper').getByText('Novo', { exact: true }).first().click(); await page.waitForTimeout(1500);
  await shot('01-cadastro-servico-vazio');
  console.log('url:', page.url());
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
