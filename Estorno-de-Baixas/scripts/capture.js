// Captura das telas da documentação "Estorno de Baixas (Contas a Receber e a Pagar)" (Playwright).
// Pré-requisitos: node setup_dados.js preparar; API em :49041 e front em :4222 (cap_common redireciona a API fixa do front);
// usuário administrador (E2E_LOGIN / E2E_SENHA). Banco local de teste; nunca produção.
// Lê os totais do dashboard antes e depois e grava em output/valores.json (a narração e o PDF citam esses valores).
const fs = require('fs');
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

const { receberEstornar, pagarEstornar } = JSON.parse(fs.readFileSync(path.join(__dirname, 'output', 'estado_demo.json'), 'utf8'));
const VALORES = path.join(__dirname, 'output', 'valores.json');

(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const valores = fs.existsSync(VALORES) ? JSON.parse(fs.readFileSync(VALORES, 'utf8')) : {};
  const passo = async (nome, fn) => {
    try { await fn(); console.log('ok  ', nome); }
    catch (e) { console.log('FALHA', nome, '-', e.message.split('\n')[0]); await shot('ZZ-erro-' + nome).catch(() => {}); throw e; }
  };
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };
  const pausa = (ms = 500) => page.waitForTimeout(ms);

  const dashboard = async (rotulo, nome) => {
    await ir('/financeiro/dashboard'); await fecharAviso();
    await page.locator('button:has-text("Buscar")').first().click(); await pausa(2500);
    const cards = await page.locator('h3').allTextContents();
    valores[rotulo] = cards.slice(0, 12).map(s => s.trim());
    fs.writeFileSync(VALORES, JSON.stringify(valores, null, 2));
    await shot(nome, false);
  };
  const relatorio = async (rota, nome, situacao) => {
    await ir(rota); await fecharAviso();
    await page.locator('button:has-text("Filtros")').first().click(); await pausa(700);
    if (situacao) await page.locator('select:has(option:text-matches("Somente (excluídas|cancelados)"))').selectOption({ label: situacao });
    await page.locator('button:has-text("Filtrar")').first().click(); await pausa(2500);
    await shot(nome, false);
  };
  const abrirLinha = async (rota, textoLinha) => {
    await ir(rota); await fecharAviso();
    const linha = page.locator('tr', { hasText: textoLinha }).first();
    await linha.waitFor({ timeout: 15000 });
    return linha;
  };

  // ---------- ANTES: o que os totais mostram com as 4 baixas ativas ----------
  await passo('01-dashboard-antes', () => dashboard('antes', '01-dashboard-antes'));
  await passo('02-rel-recebimentos-antes', () => relatorio('/relatorio/conta-receber/recebimentos', '02-rel-recebimentos-antes', 'Todas'));
  await passo('03-rel-pagamentos-antes', () => relatorio('/relatorio/conta-pagar/pagamentos', '03-rel-pagamentos-antes', 'Todas'));
  await passo('04-movimentos-antes', async () => {
    await ir('/financeiro/movimentos'); await fecharAviso();
    await page.locator('button:has-text("Buscar")').first().click(); await pausa(2000);
    await shot('04-movimentos-antes');
  });

  // ---------- ESTORNO DE UMA BAIXA A RECEBER ----------
  await passo('05-lista-receber-quitado', async () => {
    await abrirLinha('/financeiro/contareceber', String(receberEstornar));
    await shot('05-lista-receber-quitado', false);
  });
  await passo('06-receber-historico', async () => {
    const linha = await abrirLinha('/financeiro/contareceber', String(receberEstornar));
    await linha.locator('button[title="Pagamento / Acerto"]').click();
    const modal = page.locator('#modalReceberBaixa'); await modal.waitFor({ state: 'visible' }); await pausa();
    await modal.locator('button:has-text("Histórico / Estornos")').click(); await pausa(900);
    await shot('06-receber-historico', false);
    await modal.locator('tbody tr button.btn-danger').first().click();
    const motivo = page.locator('#modalConfirmarBaixaRemover'); await motivo.waitFor({ state: 'visible' });
    await motivo.locator('select').selectOption({ index: 1 }); await pausa();
    await shot('07-receber-motivo', false);
    await motivo.locator('button:has-text("Confirmar cancelamento")').click(); await pausa(2500);
    await modal.locator('button:has-text("Lançar recebimento")').click(); await pausa(500);
    await modal.locator('button:has-text("Histórico / Estornos")').click(); await pausa(1500);
    await shot('08-receber-estornado', false);
  });
  await passo('09-receber-reaberto', async () => {
    await abrirLinha('/financeiro/contareceber', String(receberEstornar));
    await shot('09-receber-reaberto', false);
  });

  // ---------- ESTORNO DE UMA BAIXA A PAGAR ----------
  await passo('10-pagar-historico', async () => {
    const linha = await abrirLinha('/financeiro/contapagar', 'ENERGIA ELETRICA');
    await shot('10-lista-pagar-quitado', false);
    await linha.locator('button[title="Pagamento / Acerto"]').click();
    const modal = page.locator('#modalContaPagarBaixa'); await modal.waitFor({ state: 'visible' }); await pausa();
    await modal.locator('button:has-text("Histórico / Estornos")').click(); await pausa(900);
    await shot('11-pagar-historico', false);
    await modal.locator('tbody tr button.btn-danger').first().click();
    const motivo = page.locator('.modal.show', { hasText: 'Cancelar Acerto de Pagamento' }); await motivo.waitFor({ state: 'visible' });
    await motivo.locator('select').selectOption({ index: 1 }); await pausa();
    await shot('12-pagar-motivo', false);
    await motivo.locator('button:has-text("Confirmar Cancelamento")').click(); await pausa(2500);
    await shot('13-pagar-estornado', false);
  });
  await passo('14-pagar-reaberto', async () => {
    await abrirLinha('/financeiro/contapagar', 'ENERGIA ELETRICA');
    await shot('14-pagar-reaberto', false);
  });

  // ---------- DEPOIS: conferência no dashboard, relatórios e movimentos ----------
  await passo('15-dashboard-depois', () => dashboard('depois', '15-dashboard-depois'));
  await passo('16-rel-recebimentos-todas', () => relatorio('/relatorio/conta-receber/recebimentos', '16-rel-recebimentos-todas', 'Todas'));
  await passo('17-rel-recebimentos-ativas', () => relatorio('/relatorio/conta-receber/recebimentos', '17-rel-recebimentos-ativas', 'Somente ativas'));
  await passo('18-rel-pagamentos-depois', () => relatorio('/relatorio/conta-pagar/pagamentos', '18-rel-pagamentos-depois', 'Todas'));
  await passo('19-movimentos-depois', async () => {
    await ir('/financeiro/movimentos'); await fecharAviso();
    await page.locator('button:has-text("Buscar")').first().click(); await pausa(2000);
    await shot('19-movimentos-depois');
  });

  await browser.close();
  console.log('captura concluída');
})().catch(e => { console.error(e.message); process.exit(1); });
