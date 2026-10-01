// Captura consolidada do Módulo de Caixa (substitui capture*.js antigos, mantidos como histórico)
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const M = '.meuModalTotal, .meuModalContainer';
  const modal = () => page.locator(M).first();

  await ir('/caixa');
  if (await page.locator('button:has-text("Fechar Caixa")').count() > 0) {
    await page.click('button:has-text("Fechar Caixa")'); await page.waitForTimeout(900);
    await modal().locator('button:has-text("Confirmar")').click(); await page.waitForTimeout(2000);
    await ir('/caixa');
  }
  await shot('00-meu-caixa-inicial');
  await page.click('button:has-text("Abrir Caixa")'); await page.waitForTimeout(800);
  await shot('01-modal-abrir-caixa');
  await modal().locator('input[mask="separator.2"]').fill('100,00');
  await shot('02-abrir-caixa-preenchido');
  await modal().locator('button:has-text("Confirmar")').click(); await page.waitForTimeout(1800);
  await shot('03-caixa-aberto-extrato-vazio');

  // Suprimento
  await page.click('button:has-text("Novo Lançamento")'); await page.waitForTimeout(800);
  await modal().locator('select').first().selectOption('E'); await page.waitForTimeout(500);
  await shot('04-modal-lancamento-tipo-suprimento');
  await modal().locator('select').nth(1).selectOption({ label: 'Dinheiro' });
  await modal().locator('input[type="text"]').first().fill('Troco inicial adicional');
  const vs = modal().locator('input[mask="separator.2"]'); await vs.click(); await vs.fill('50,00');
  await page.waitForTimeout(300);
  await shot('05-lancamento-suprimento-preenchido');
  await modal().locator('button.btn-success').first().click(); await page.waitForTimeout(700);
  await shot('06-lancamento-adicionado-tabela');
  await modal().locator('button:has-text("Salvar")').click(); await page.waitForTimeout(600);
  await page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click().catch(() => {}); await page.waitForTimeout(1500);
  await shot('07-extrato-com-suprimento');

  // Baixa de Conta a Receber (reflete no caixa)
  await ir('/financeiro/contareceber');
  await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(450);
  await page.click('.modal.show button:has-text("Buscar")'); await page.waitForTimeout(1500);
  await page.click('.modal.show button:has-text("Fechar")').catch(() => {}); await page.waitForTimeout(500);
  await page.locator('tr').filter({ hasText: 'Aberto' }).first().locator('button.btn-success').first().click();
  await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  const b = page.locator('.modal.show').last();
  await shot('08-modal-baixa-contareceber');
  for (const o of await b.locator('select').first().locator('option').all()) { if (((await o.textContent()) || '').toLowerCase().includes('dinheiro')) { await b.locator('select').first().selectOption(await o.getAttribute('value')); break; } }
  await page.waitForTimeout(700);
  await b.locator('input[mask="separator.2"]').first().fill('1,00');
  const cs = b.locator('select', { hasText: 'CAIXA' });
  for (const o of await cs.locator('option').all()) { if (((await o.textContent()) || '').trim() === 'CAIXA') { await cs.selectOption(await o.getAttribute('value')); break; } }
  await page.waitForTimeout(500);
  await shot('08b-modal-baixa-preenchida');
  await b.locator('button:has-text("Lançar")').click(); await page.waitForTimeout(800);
  await page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click(); await page.waitForTimeout(1500);
  await shot('09-apos-baixar-contareceber');
  await b.locator('button:has-text("Fechar")').click().catch(() => {});
  await ir('/caixa');
  await shot('10-extrato-com-entrada-refletida');

  // Solicitar cancelamento do suprimento
  await shot('11-extrato-completo-antes-fechar');
  await page.locator('tr').filter({ hasText: 'Suprimento' }).locator('button:has-text("Cancelar")').first().click(); await page.waitForTimeout(600);
  await shot('12-confirmar-solicitar-cancelamento');
  await page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click(); await page.waitForTimeout(1200);
  await shot('13-apos-solicitar-cancelamento');

  // Fechar com solicitação pendente: bloqueado
  await page.waitForTimeout(6000);
  await page.click('button:has-text("Fechar Caixa")'); await page.waitForTimeout(900);
  await modal().locator('button:has-text("Confirmar")').click(); await page.waitForTimeout(1000);
  await shot('17-bloqueio-fechar-com-solicitacao-pendente');
  await page.waitForTimeout(5000);
  await modal().locator('button:has-text("Cancelar")').click().catch(() => {}); await page.waitForTimeout(600);

  // Aprovar em Solicitações
  await ir('/caixas/solicitacoes');
  await shot('18-solicitacoes-pendentes');
  await page.locator('tr').filter({ hasText: 'Suprimento' }).locator('button:has-text("Cancelar")').first().click(); await page.waitForTimeout(700);
  await shot('19-solicitacoes-confirmar-cancelamento');
  await page.locator('button:visible', { hasText: /^\s*Sim\s*$/ }).first().click(); await page.waitForTimeout(1500);
  await shot('20-solicitacoes-apos-aprovar');

  // Fechar de verdade
  await ir('/caixa');
  await shot('21-extrato-apos-cancelamento-aprovado');
  await page.click('button:has-text("Fechar Caixa")'); await page.waitForTimeout(900);
  await shot('14-modal-fechar-caixa-resumo');
  await modal().locator('button:has-text("Confirmar")').click(); await page.waitForTimeout(1800);
  await shot('15-apos-fechar-caixa');
  await shot('16-meus-caixas-lista');

  // Histórico geral e extrato do caixa fechado
  await ir('/caixas');
  await page.click('button:has(.fa-search)').catch(() => {}); await page.waitForTimeout(1500);
  await shot('23-listar-historico-caixas');
  const antes = page.context().pages().length;
  await page.locator('a:has-text("Extrato"), button:has-text("Extrato")').first().click(); await page.waitForTimeout(2500);
  const ps = page.context().pages(); const alvo = ps[ps.length - 1];
  await alvo.addStyleTag({ content: '#li_testes { display: none !important; }' }).catch(() => {});
  await alvo.screenshot({ path: path.join(__dirname, 'screenshots', '22-extrato-caixa-fechado.png'), fullPage: true });
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 600)); process.exit(1); });
