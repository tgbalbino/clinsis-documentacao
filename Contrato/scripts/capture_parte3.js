// Parte 3: título gerado em Contas a Receber, renovação, "Não vai renovar", vencendo, parâmetro e sino.
// Uso: CONTRATO=15 NAOVAI=14 node capture_parte3.js
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const N = process.env.CONTRATO || '15';
  const M = process.env.NAOVAI || '14';
  const { browser, page, ir, shot } = await abrir(__dirname);
  const sim = () => page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click();
  const abrirContrato = async (n) => {
    await ir('/contrato');
    await page.locator('tr').filter({ has: page.locator('td', { hasText: new RegExp('^' + n + '$') }) }).locator('button[title="Alterar contrato / serviços"]').click();
    await page.waitForSelector('.modal.show'); await page.waitForTimeout(1500);
  };

  // Títulos gerados em Contas a Receber (com a origem)
  await ir('/financeiro/contareceber');
  await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(450);
  await page.click('.modal.show button:has-text("Buscar")'); await page.waitForTimeout(1800);
  await page.click('.modal.show button:has-text("Fechar")').catch(() => {}); await page.waitForTimeout(600);
  await shot('16-conta-a-receber-gerada-pelo-contrato');

  // Renovar
  await abrirContrato(N);
  if (await page.locator('.modal.show button:has-text("Renovar")').count() > 0) {
    await page.click('.modal.show button:has-text("Renovar")'); await page.waitForTimeout(700);
    await shot('19-confirmar-renovar');
    await sim(); await page.waitForTimeout(2500);
    await shot('20-apos-renovar-lista');
  }

  // Não vai renovar
  await abrirContrato(M);
  await shot('21-contrato-fechado-antes-nao-renovar');
  if (await page.locator('.modal.show button:has-text("Não vai renovar")').count() > 0) {
    await page.click('.modal.show button:has-text("Não vai renovar")'); await page.waitForTimeout(700);
    await shot('22-confirmar-nao-vai-renovar');
    await sim(); await page.waitForTimeout(1800);
    await shot('23-apos-nao-vai-renovar');
  }

  // Vencendo
  await ir('/contrato?vencendo=1');
  await shot('17-contratos-vencendo');

  // Parâmetro do aviso
  await ir('/aux/parametro');
  await shot('24-parametros-lista');
  const linha = page.locator('tr').filter({ hasText: /o Contrato está vencendo/i });
  if (await linha.count() > 0) {
    await linha.first().locator('button').first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(600);
    await shot('25-parametro-dias-aviso-editar');
  }

  // Sino
  await ir('/contrato');
  const sino = page.locator('i.fa-bell').first();
  if (await sino.count() > 0) { await sino.click(); await page.waitForTimeout(800); await shot('26-sino-notificacoes'); }
  await browser.close(); console.log('OK parte 3');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
