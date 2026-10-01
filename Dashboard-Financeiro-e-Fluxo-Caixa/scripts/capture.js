const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const datas = async (ini, fim) => {
    const campos = page.locator('input[bsdatepicker]');
    await campos.nth(0).fill(ini); await page.keyboard.press('Escape');
    await campos.nth(1).fill(fim); await page.keyboard.press('Escape');
    await page.waitForTimeout(300);
  };

  // Dashboard Financeiro
  await ir('/financeiro/dashboard');
  await shot('00-dashboard-inicial');
  await datas('01/01/2026', '30/09/2026');
  await shot('01-dashboard-filtro-preenchido');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(3000);
  await shot('02-dashboard-resultado');

  // Fluxo de Caixa
  await ir('/financeiro/fluxocaixa');
  await shot('10-fluxo-inicial');
  await datas('01/09/2026', '30/09/2026');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(3000);
  await shot('11-fluxo-resultado');
  console.log('selects:', await page.locator('select').evaluateAll(a => a.map(e => [...e.options].map(o => o.text).join('/'))));
  const mostrar = page.locator('select', { hasText: 'Somente Realizado' });
  await mostrar.selectOption({ label: 'Somente Realizado' }); await page.waitForTimeout(500);
  const agr = page.locator('select', { hasText: 'Mês' }).last();
  await agr.selectOption({ label: 'Mês' }); await page.waitForTimeout(300);
  await datas('01/01/2026', '30/09/2026');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(3000);
  await shot('12-fluxo-agrupado-mes');
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
