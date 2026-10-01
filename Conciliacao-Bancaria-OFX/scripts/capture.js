// Prints da Conciliação Bancária (OFX). Usa extrato-exemplo.ofx e os movimentos criados por setup-dados.js.
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');
const f = (n) => path.join(__dirname, n);
(async () => {
  const { browser, page, ir, shot, chamar } = await abrir(__dirname, {});
  // volta ao estado inicial: só a linha da Ana Paula (21/09) fica conciliada
  const movs = await chamar('POST', 'movimentofinanceiro/listar', { idClinica: 1, idContaFinanceira: 9, rows: 100 });
  for (const m of (movs.data || [])) if (m.conciliado && m.fitId !== '20260921001') await chamar('POST', `movimentofinanceiro/${m.idMovimentoFinanceiro}/desconciliar`, {});

  const buscarMov = async (nome) => {
    await ir('/financeiro/movimentos');
    await page.locator('input[bsdatepicker]').first().fill('01/09/2026');
    await page.locator('input[bsdatepicker]').nth(1).fill('30/09/2026');
    await page.locator('select').filter({ has: page.locator('option', { hasText: 'BANCO BRASIL' }) }).first().selectOption({ label: 'BANCO BRASIL' });
    await page.locator('button:has-text("Buscar")').first().click(); await page.waitForTimeout(2000);
    await shot(nome, false);
  };

  // menu lateral
  await ir('/financeiro/conciliacao-ofx');
  await shot('00-tela-inicial', false);
  await buscarMov('01-movimentos-antes');

  await ir('/financeiro/conciliacao-ofx');
  await page.locator('select').first().selectOption({ label: 'BANCO BRASIL' });
  await page.locator('input[type=file]').setInputFiles(f('extrato-exemplo.ofx'));
  await page.waitForTimeout(400);
  await shot('02-arquivo-escolhido', false);
  await page.locator('button:has-text("Ler extrato")').click(); await page.waitForTimeout(3000);
  await shot('03-resultado', false);
  await page.locator('button:has-text("Conciliar marcados")').click(); await page.waitForTimeout(900);
  await shot('04-conciliando-aviso', false);
  await page.waitForTimeout(4500);
  await shot('05-depois-de-conciliar', false);

  await buscarMov('06-movimentos-depois');

  // arquivo de outra agência
  await ir('/financeiro/conciliacao-ofx');
  await page.locator('select').first().selectOption({ label: 'BANCO BRASIL' });
  await page.locator('input[type=file]').setInputFiles(f('extrato-agencia-diferente.ofx'));
  await page.locator('button:has-text("Ler extrato")').click(); await page.waitForTimeout(3000);
  await shot('07-aviso-conta-diferente', false);

  // arquivo inválido
  await ir('/financeiro/conciliacao-ofx');
  await page.locator('select').first().selectOption({ label: 'BANCO BRASIL' });
  await page.locator('input[type=file]').setInputFiles(f('arquivo-invalido.ofx'));
  await page.locator('button:has-text("Ler extrato")').click(); await page.waitForTimeout(1200);
  await shot('08-arquivo-invalido', false);
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
