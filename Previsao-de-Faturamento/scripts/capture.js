const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/config/previsao-faturamento'); await page.waitForTimeout(1200);
  await shot('00-config-status');
  await ir('/relatorios'); await shot('01-menu-relatorios', false);
  await ir('/relatorio/previsao-faturamento'); await page.waitForTimeout(1500);
  const opts = await page.locator('select').first().locator('option').allInnerTexts();
  console.log('agendas:', opts.join('|'));
  await page.locator('select').first().selectOption({ label: '9/2026' }).catch(async () => page.locator('select').first().selectOption({ index: 1 }));
  await page.waitForTimeout(2000);
  await shot('02-tela-previsao');
  const ult = page.locator('tbody tr').last();
  const abrirBtn = async (nome, arq) => {
    await ult.locator(`button:has-text("${nome}")`).click(); await page.waitForTimeout(2500);
    await shot(arq); console.log(nome, page.url().replace('http://localhost:4222', ''));
    await page.goBack(); await page.waitForTimeout(2000);
    await page.locator('select').first().selectOption({ label: '9/2026' }).catch(() => {}); await page.waitForTimeout(1500);
  };
  await abrirBtn('Detalhes', '03-detalhes');
  await abrirBtn('Conciliação', '04-conciliacao');
  await abrirBtn('Movimentações', '05-movimentacoes');
  await abrirBtn('Pendências', '06-pendencias');
  await page.locator('button:has-text("Fechamento e precisão")').click(); await page.waitForTimeout(2500); await shot('07-precisao');
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
