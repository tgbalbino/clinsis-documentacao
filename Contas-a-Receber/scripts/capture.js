const { abrir, datalistSelecionar } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  // abre o caixa (usuário controla caixa)
  await ir('/caixa');
  if (await page.locator('button:has-text("Abrir Caixa")').count() > 0) {
    await page.click('button:has-text("Abrir Caixa")'); await page.waitForTimeout(800);
    await page.locator('.meuModalTotal input[mask="separator.2"]').fill('100,00');
    await page.locator('.meuModalTotal button:has-text("Confirmar")').click(); await page.waitForTimeout(1800);
  }
  await ir('/financeiro/contareceber');
  await shot('00-lista-inicial');
  await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  await shot('01-filtros');
  console.log('botoes filtro:', (await page.locator('.modal.show button').allInnerTexts()).join('|'));
  await page.locator('.modal.show button:has(.fa-search)').first().click(); await page.waitForTimeout(900);
  const pf = page.locator('.modal.show').last();
  await pf.locator('input[placeholder="pesquisar paciente"]').fill('Paciente 0007'); await pf.locator('input[placeholder="pesquisar paciente"]').press('Enter'); await page.waitForTimeout(1500);
  await pf.locator('tbody tr').first().locator('button').last().click(); await page.waitForTimeout(800);
  await shot('01b-filtros-paciente');
  await page.locator('.modal.show button:has-text("Buscar")').first().click(); await page.waitForTimeout(2000);
  await page.locator('.modal.show button:has-text("Fechar")').first().click().catch(() => {}); await page.waitForTimeout(900);
  await shot('02-resultado-busca');
  await page.waitForTimeout(6000);
  await page.click('button:has-text("Filtro rápido")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(700);
  await shot('03-filtro-rapido');
  await page.locator('.modal.show button:has-text("Fechar")').first().click().catch(() => page.keyboard.press('Escape')); await page.waitForTimeout(700);

  await page.click('button:has-text("Novo")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  let m = page.locator('.modal.show').last();
  await m.locator('input[type=text]').first().locator('xpath=following::button[1]').click(); await page.waitForTimeout(1000);
  const pac = page.locator('.modal.show').last();
  await pac.locator('input[placeholder="pesquisar paciente"]').fill('Paciente 0007'); await pac.locator('input[placeholder="pesquisar paciente"]').press('Enter'); await page.waitForTimeout(1500);
  await pac.locator('tbody tr').first().locator('button').last().click(); await page.waitForTimeout(800);
  m = page.locator('.modal.show').last();
  const ins = m.locator('input[placeholder="Digite e selecione"]');
  await datalistSelecionar(page, ins.nth(0), 'Consulta Particular');
  await datalistSelecionar(page, ins.nth(1), 'Administrativo');
  const qtd = m.locator('input[type=text]').nth(3); await qtd.click(); await qtd.fill('2');
  const vl = m.locator('input[type=text]').last(); await vl.click(); await vl.fill('150,00'); await vl.press('Tab');
  await m.locator('input[bsdatepicker]').first().fill('10/10/2026'); await page.keyboard.press('Escape'); await page.waitForTimeout(300);
  await shot('04-parcela-preenchida');
  await m.locator('button:has-text("Gerar Parcelas")').click(); await page.waitForTimeout(1200);
  await shot('05-preview-parcelas');
  console.log('botoes:', (await m.locator('button').allInnerTexts()).join('|'));
  await m.locator('button:has-text("Confirmar")').click(); await page.waitForTimeout(2000);
  await shot('06-apos-confirmar');
  const hoje = new Date(); const dd = String(hoje.getDate()).padStart(2, '0') + '/' + String(hoje.getMonth() + 1).padStart(2, '0') + '/' + hoje.getFullYear();
  await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(500);
  await page.locator('.modal.show button:has-text("Buscar")').first().click(); await page.waitForTimeout(1800);
  await page.locator('.modal.show button:has-text("Fechar")').first().click(); await page.waitForTimeout(700);
  const linha = page.locator('tr').filter({ hasText: 'Paciente 0007' }).filter({ hasText: 'Aberto' }).filter({ hasText: dd + ' ' }).first();
  await linha.locator('button.btn-success').click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(1200);
  const b = page.locator('.modal.show').last();
  const vb = b.locator('input[type=text]').nth(9); await vb.click(); await vb.fill('150,00'); await vb.press('Tab');
  await b.locator('select').nth(0).selectOption({ label: 'Cartão de Crédito' });
  await page.waitForTimeout(500);
  await b.locator('select', { hasText: 'BANCO BRASIL' }).selectOption({ label: 'BANCO BRASIL' });
  await page.waitForTimeout(600);
  await shot('09-baixa-preenchida');
  await b.locator('button:has-text("Lançar")').click(); await page.waitForTimeout(1000);
  await shot('09b-confirmacao');
  await page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click().catch(() => {}); await page.waitForTimeout(2000);
  await shot('10-apos-lancar-baixa');
  // fecha o caixa
  await ir('/caixa');
  if (await page.locator('button:has-text("Fechar Caixa")').count() > 0) {
    await page.click('button:has-text("Fechar Caixa")'); await page.waitForTimeout(900);
    await page.locator('.meuModalTotal button:has-text("Confirmar")').click(); await page.waitForTimeout(1800);
  }
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
