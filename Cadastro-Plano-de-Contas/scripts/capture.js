const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot, chamar } = await abrir(__dirname);
  // limpa restos de execuções anteriores
  const lst = await chamar('POST', 'planoconta/listar', {});
  for (const c of (lst.data || [])) if (/MATERIAL DE (LIMPEZA|ESCRITORIO)/.test(c.descricao || '')) console.log('del', c.descricao, JSON.stringify(await chamar('DELETE', `planoconta/${c.idPlanoConta}`)).slice(0,80));
  await ir('/cadastro/planocontas');
  await shot('00-arvore-inicial');
  await page.click('button:has-text("Lista")'); await page.waitForTimeout(800);
  await shot('01-lista');
  await page.click('button:has-text("Árvore")'); await page.waitForTimeout(500);

  // Novo (conta filha de "2 - Despesas")
  await page.click('button:has-text("Novo")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(500);
  const m = page.locator('.modal.show');
  await m.locator('select').first().selectOption({ value: 'D' });
  await page.waitForTimeout(500);
  await m.locator('input[type=text]').last().fill('MATERIAL DE ESCRITORIO');
  await m.locator('select').nth(1).selectOption({ label: '2 - Despesas' }).catch(() => {});
  await page.waitForTimeout(400);
  await shot('02-novo-modal-preenchido');
  await m.locator('button:has-text("Salvar")').click(); await page.waitForTimeout(1500);
  await page.waitForSelector('.modal.show', { state: 'detached' }).catch(() => {});
  await shot('03-apos-salvar');

  // Filtro
  await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show, .offcanvas.show'); await page.waitForTimeout(600);
  const f = page.locator('.modal.show, .offcanvas.show').first();
  await f.locator('input[type=text]').nth(1).fill('MATERIAL').catch(() => f.locator('input[type=text]').first().fill('MATERIAL'));
  await shot('04-filtro-preenchido');
  await f.locator('button:has-text("Aplicar")').first().click();
  await page.waitForTimeout(1200);
  await shot('05-resultado-filtro');
  await browser.close();
  console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
