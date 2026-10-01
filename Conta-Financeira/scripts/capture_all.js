// Captura consolidada (substitui capture*.js antigos, mantidos como histórico)
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot, chamar } = await abrir(__dirname);
  const sel = async (select, txt) => { for (const o of await select.locator('option').all()) { if (((await o.textContent()) || '').toLowerCase().includes(txt)) { await select.selectOption(await o.getAttribute('value')); return true; } } return false; };
  const buscarReceber = async () => {
    await ir('/financeiro/contareceber');
    await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(450);
    await page.click('.modal.show button:has-text("Buscar")'); await page.waitForTimeout(1500);
    await page.click('.modal.show button:has-text("Fechar")').catch(() => {}); await page.waitForTimeout(500);
  };
  const formasCaixa = async () => {
    const l = page.locator('tr', { has: page.locator('td:first-child', { hasText: /^CAIXA$/ }) });
    await l.locator('button[title="Formas de pagamento desta conta"]').click(); await page.waitForTimeout(800);
  };

  // limpa SICOOB de execuções anteriores
  const cf = await chamar('POST', 'contafinanceira/listar', {});
  for (const c of (cf.data || [])) if (/^SICOOB/.test(c.descricao || c.nome || '')) console.log('del SICOOB', JSON.stringify(await chamar('DELETE', `contafinanceira/${c.idContaFinanceira}`)).slice(0, 60));

  // ---- Lista e cadastro
  await ir('/cadastro/contasfinanceiras');
  await shot('00-lista-contas-financeiras');
  await page.click('button:has-text("Novo")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(500);
  await page.fill('.modal.show input[maxlength="100"]', 'SICOOB CONTA CORRENTE');
  const selBanco = page.locator('.modal.show select').first();
  await selBanco.selectOption(await (await selBanco.locator('option').all())[1].getAttribute('value'));
  await page.fill('.modal.show input[maxlength="20"]', '0001');
  await page.fill('.modal.show input[maxlength="30"]', '12345-6');
  await page.locator('.modal.show input[type="text"]').last().fill('clinica@exemplo.com.br');
  await shot('10-novo-cadastro-completo');
  await page.click('.modal.show button:has-text("Salvar")'); await page.waitForTimeout(1800);
  await shot('11-lista-com-conta-nova');
  const nova = page.locator('tr').filter({ hasText: 'SICOOB' }).first();
  await nova.locator('button[title="Formas de pagamento desta conta"]').click(); await page.waitForTimeout(800);
  await shot('12-formas-conta-nova');
  await page.click('.modal.show button:has-text("Fechar")'); await page.waitForTimeout(500);
  await nova.locator('button.btn-warning').click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(700);
  await shot('13-editar-conta');
  await page.click('.modal.show button:has-text("Fechar")'); await page.waitForTimeout(500);

  // ---- Formas de pagamento da CAIXA: garante Cartão habilitado (antes) e desabilita (depois)
  await formasCaixa();
  let cartao = page.locator('.modal.show tr').filter({ hasText: 'Cartão de Crédito' });
  if (await cartao.locator('button:has-text("Habilitar")').count() > 0) { await cartao.locator('button:has-text("Habilitar")').click(); await page.waitForTimeout(400); await page.locator('button:visible', { hasText: 'Sim' }).click().catch(() => {}); await page.waitForTimeout(900); }
  await shot('02-formas-pagamento-antes');
  await cartao.locator('button:has-text("Desabilitar")').click(); await page.waitForTimeout(400);
  await page.locator('button:visible', { hasText: 'Sim' }).click(); await page.waitForTimeout(900);
  await shot('03-formas-pagamento-depois');
  await page.click('.modal.show button:has-text("Fechar")'); await page.waitForTimeout(500);

  // ---- Caixa fechado: baixa de Dinheiro na CAIXA recusada
  await buscarReceber();
  let modal;
  const abrirBaixa = async () => {
    await page.locator('tr').filter({ hasText: 'Aberto' }).first().locator('button.btn-success').first().click();
    await page.waitForSelector('.modal.show'); await page.waitForTimeout(800); modal = page.locator('.modal.show').last();
  };
  await abrirBaixa();
  await sel(modal.locator('select').first(), 'dinheiro'); await page.waitForTimeout(700);
  await modal.locator('input[mask="separator.2"]').first().fill('1,00');
  await sel(modal.locator('select', { hasText: 'CAIXA' }), 'caixa'); await page.waitForTimeout(500);
  console.log('conta sel:', await modal.locator('select', { hasText: 'CAIXA' }).inputValue());
  await modal.locator('button:has-text("Lançar")').click(); await page.waitForTimeout(700);
  await page.locator('button:visible', { hasText: 'Sim' }).click(); await page.waitForTimeout(1500);
  await shot('09-erro-caixa-fechado');

  // ---- Abre o caixa
  await ir('/caixa');
  await page.click('button:has-text("Abrir Caixa")'); await page.waitForTimeout(700);
  const inp = page.locator('.meuModalTotal input[mask="separator.2"]'); await inp.click(); await inp.pressSequentially('10000', { delay: 40 });
  await page.locator('.meuModalTotal button:has-text("Confirmar")').click(); await page.waitForTimeout(1800);

  // ---- Cartão na CAIXA (desabilitado) recusado; depois Dinheiro grava
  await buscarReceber(); await abrirBaixa();
  await sel(modal.locator('select').first(), 'cartão de crédito'); await page.waitForTimeout(300);
  await modal.locator('input[mask="separator.2"]').first().fill('1,00');
  await sel(modal.locator('select', { hasText: 'CAIXA' }), 'caixa'); await page.waitForTimeout(300);
  await modal.locator('button:has-text("Lançar")').click(); await page.waitForTimeout(700);
  await page.locator('button:visible', { hasText: 'Sim' }).click().catch(() => {}); await page.waitForTimeout(1200);
  await shot('05-erro-forma-nao-habilitada');
  await page.waitForTimeout(7000);
  await sel(modal.locator('select').first(), 'dinheiro'); await page.waitForTimeout(700);
  await sel(modal.locator('select', { hasText: 'CAIXA' }), 'caixa'); await page.waitForTimeout(500);
  await modal.locator('button:has-text("Lançar")').click(); await page.waitForTimeout(700);
  await page.locator('button:visible', { hasText: 'Sim' }).click().catch(() => {}); await page.waitForTimeout(500);
  await shot('07-baixa-com-sucesso');

  // ---- Contas a Pagar: cartão na CAIXA recusado
  await ir('/financeiro/contapagar');
  await page.locator('button[title="Pagamento / Acerto"]').first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  modal = page.locator('.modal.show').last();
  await sel(modal.locator('select').first(), 'cartão de crédito');
  await modal.locator('input[mask="separator.2"]').first().fill('1,00');
  await sel(modal.locator('select', { hasText: 'CAIXA' }), 'caixa'); await page.waitForTimeout(300);
  await modal.locator('button:has-text("Lançar")').click(); await page.waitForTimeout(700);
  await page.locator('button:visible', { hasText: 'Sim' }).click().catch(() => {}); await page.waitForTimeout(600);
  await shot('26-contapagar-erro-forma-nao-habilitada', false);

  // ---- Onde é usada
  await ir('/financeiro/movimentos');
  await sel(page.locator('select').first(), 'caixa');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(1500);
  await shot('22-movimentos-filtrado-caixa');
  await ir('/financeiro/fluxocaixa'); await page.waitForTimeout(1200);
  await shot('21-fluxo-caixa');
  await ir('/aux/pagamentoforma'); await shot('23-formas-pagamento-clinica');
  await ir('/aux/parametro');
  const busca = page.locator('input[type="text"]').first(); await busca.fill('ContaFinanceira').catch(() => {}); await page.keyboard.press('Enter'); await page.waitForTimeout(1200);
  await shot('24-parametro-conta-financeira-checkin');

  // ---- Reabilita Cartão na CAIXA, exclusões
  await ir('/cadastro/contasfinanceiras');
  await formasCaixa();
  cartao = page.locator('.modal.show tr').filter({ hasText: 'Cartão de Crédito' });
  if (await cartao.locator('button:has-text("Habilitar")').count() > 0) { await cartao.locator('button:has-text("Habilitar")').click(); await page.waitForTimeout(400); await page.locator('button:visible', { hasText: 'Sim' }).click().catch(() => {}); await page.waitForTimeout(900); }
  await page.click('.modal.show button:has-text("Fechar")'); await page.waitForTimeout(500);
  await page.locator('tr', { has: page.locator('td:first-child', { hasText: /^CAIXA$/ }) }).locator('button.btn-danger').click(); await page.waitForTimeout(700);
  await page.locator('button:visible', { hasText: 'Sim' }).click(); await page.waitForTimeout(1000);
  await shot('15-resultado-exclusao-caixa');
  await page.waitForTimeout(6000);
  await page.locator('tr', { has: page.locator('td:first-child', { hasText: /^SICOOB/ }) }).locator('button.btn-danger').click(); await page.waitForTimeout(700);
  await page.locator('button:visible', { hasText: 'Sim' }).click(); await page.waitForTimeout(1500);
  await shot('17-exclusao-conta-sem-movimentos-ok');

  // ---- Fecha o caixa (estado padrão do ambiente de teste: fechado)
  await ir('/caixa');
  await page.click('button:has-text("Fechar Caixa")'); await page.waitForTimeout(900);
  await page.locator('.meuModalTotal button:has-text("Confirmar")').click(); await page.waitForTimeout(1800);
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 600)); process.exit(1); });
