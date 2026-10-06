// Captura das telas da documentação "Controle de Cheques e Liquidação Financeira (Cheque e Cartão)" (Playwright).
// Pré-requisitos: node setup_dados.js preparar; API em :49041 e front em :4222 (cap_common redireciona a API fixa do front);
// usuário administrador (E2E_LOGIN / E2E_SENHA). Banco local de teste; nunca produção.
// Listas saem em página inteira (fullPage); modais, na janela (viewport), esperando a animação do modal terminar.
const fs = require('fs');
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

const { cheque1, cheque2, cartao, pagar } = JSON.parse(fs.readFileSync(path.join(__dirname, 'output', 'estado_demo.json'), 'utf8'));

const CPF_EMITENTE = '47685594099'; // Paciente 0002 (CPF de teste)
const br = d => `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}/${d.getFullYear()}`;
const mais = n => { const d = new Date(); d.setDate(d.getDate() + n); return d; };

(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const passo = async (nome, fn) => {
    try { await fn(); console.log('ok  ', nome); }
    catch (e) { console.log('FALHA', nome, '-', e.message.split('\n')[0]); await shot('ZZ-erro-' + nome).catch(() => {}); throw e; }
  };
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };
  const dataCampo = async (campo, data) => { await campo.fill(br(data)); await campo.press('Escape'); };
  const pausa = () => page.waitForTimeout(500);

  const abrirBaixaReceber = async (idReceber, valor) => {
    await ir('/financeiro/contareceber'); await fecharAviso();
    const linha = page.locator('tr', { hasText: valor }).filter({ hasText: String(idReceber) }).first();
    await linha.waitFor({ timeout: 15000 });
    await linha.locator('button[title="Pagamento / Acerto"]').click();
    const modal = page.locator('#modalReceberBaixa'); await modal.waitFor({ state: 'visible' }); await pausa();
    return modal;
  };
  const confirmarBaixa = async () => {
    await page.locator('#modalConfirmarBaixa').waitFor({ state: 'visible' }); await pausa();
    await page.locator('#modalConfirmarBaixa button:has-text("Sim")').click();
    await page.waitForTimeout(2500);
  };
  const liquidacoes = async (todas = true) => {
    await ir('/financeiro/liquidacoes'); await fecharAviso();
    if (todas) { await page.locator('select').first().selectOption({ label: 'Todas' }); await page.locator('button:has-text("Buscar")').click(); await page.waitForTimeout(1500); }
  };
  const cheques = async (situacao = 'Todas') => {
    await ir('/financeiro/cheques'); await fecharAviso();
    await page.locator('#filtroSituacao').selectOption({ label: situacao });
    await page.locator('#btnBuscarCheques').click(); await page.waitForTimeout(1500);
  };
  const preencherChequeRecebido = async (modal, numero) => {
    await modal.locator('#chequeBanco').selectOption('001');
    await modal.locator('#chequeAgencia').fill('0001');
    await modal.locator('#chequeConta').fill('12345-6');
    await modal.locator('#chequeSerie').fill('A');
    await modal.locator('#chequeNumero').fill(numero);
    await modal.locator('#chequeEmitenteCpf').fill(CPF_EMITENTE);
    await modal.locator('#chequeNumero').blur();
  };

  // 1) Configuração das formas
  await passo('01-config-formas', async () => {
    await ir('/aux/pagamentoforma'); await fecharAviso(); await page.waitForTimeout(800);
    await shot('01-config-formas', false);
  });

  // 2) Baixa com cheque novo (cheque de R$ 700,00 que vai pagar dois títulos)
  await passo('02-baixa-cheque-novo', async () => {
    const modal = await abrirBaixaReceber(cheque1, '450,00');
    await modal.locator('select').filter({ has: page.locator('option', { hasText: 'Cheque' }) }).first().selectOption({ label: 'Cheque' });
    await modal.locator('#blocoCheque').waitFor({ timeout: 5000 });
    await modal.locator('label:text-is("Valor") + input').fill('450,00');
    await preencherChequeRecebido(modal, '000482');
    await modal.locator('#chequeValor').fill('700');
    await dataCampo(modal.locator('#chequeBomPara'), mais(15));
    await modal.locator('#chequeEmitenteInfo i.fa-user-check').waitFor({ timeout: 8000 });
    await modal.locator('label:has-text("Conta Financeira") ~ select').first().selectOption({ label: 'CAIXA' });
    await pausa();
    await shot('02-baixa-cheque-novo', false);
    await modal.locator('button:has-text("Lançar")').first().click();
    await page.locator('#modalConfirmarBaixa').waitFor({ state: 'visible' }); await pausa();
    await shot('03-baixa-cheque-confirmacao', false);
    await page.locator('#modalConfirmarBaixa button:has-text("Sim")').click();
    await page.waitForTimeout(2500);
  });

  // 3) Segundo título: o mesmo cheque digitado de novo é reconhecido
  await passo('04-cheque-duplicado', async () => {
    const modal = await abrirBaixaReceber(cheque2, '250,00');
    await modal.locator('select').filter({ has: page.locator('option', { hasText: 'Cheque' }) }).first().selectOption({ label: 'Cheque' });
    await modal.locator('#blocoCheque').waitFor({ timeout: 5000 });
    await modal.locator('label:text-is("Valor") + input').fill('250,00');
    await preencherChequeRecebido(modal, '482');
    await modal.locator('#avisoChequeDuplicado').waitFor({ timeout: 8000 });
    await modal.locator('label:has-text("Conta Financeira") ~ select').first().selectOption({ label: 'CAIXA' });
    await pausa();
    await shot('04-cheque-duplicado', false);
    await modal.locator('#btnUsarChequeCadastrado').click();
    await pausa();
    await shot('05-cheque-da-carteira', false);
    await modal.locator('button:has-text("Lançar")').first().click();
    await confirmarBaixa();
  });

  // 4) Tela Cheques
  await passo('06-lista-cheques', async () => {
    await cheques('Em carteira');
    await shot('06-lista-cheques');
    const id = await page.locator('#tabelaCheques tbody tr button[id^="btnDetalhe"]').first().getAttribute('id');
    await page.locator('#' + id).click();
    await page.locator('#modalDetalheCheque').waitFor({ state: 'visible' });
    await page.waitForTimeout(900);
    await shot('07-detalhe-cheque', false);
    await page.locator('#modalDetalheCheque button:has-text("Fechar")').click();
    await pausa();
  });

  // 5) Liquidações mostram "Ver cheque"
  await passo('08-liquidacoes-cheque', async () => {
    await liquidacoes(true);
    await shot('08-liquidacoes-cheque');
  });

  // 6) Compensar o cheque no banco
  await passo('09-compensar-cheque', async () => {
    await cheques('Em carteira');
    await page.locator('#tabelaCheques tbody tr button[id^="btnCompensar"]').first().click();
    const modal = page.locator('#modalCompensarCheque'); await modal.waitFor({ state: 'visible' });
    await modal.locator('#contaCompensacao').selectOption({ label: 'BANCO BRASIL' });
    await pausa();
    await shot('09-compensar-cheque', false);
    await modal.locator('#btnConfirmarCompensacao').click();
    await page.waitForTimeout(2500);
    await cheques('Todas');
    await shot('10-cheque-compensado');
  });

  await passo('11-movimentos', async () => {
    await ir('/financeiro/movimentos'); await fecharAviso();
    await page.locator('select').filter({ has: page.locator('option', { hasText: 'Compensação de cheque' }) }).first().selectOption({ label: 'Compensação de cheque' });
    await page.locator('button:has-text("Buscar")').first().click(); await page.waitForTimeout(1800);
    await shot('11-movimentos');
  });

  // 7) Devolver o cheque (já compensado): estorno único e uma cobrança por título
  await passo('12-devolver-cheque', async () => {
    await cheques('Compensado');
    await page.locator('#tabelaCheques tbody tr button[id^="btnDevolver"]').first().click();
    const modal = page.locator('#modalDevolverCheque'); await modal.waitFor({ state: 'visible' });
    await modal.locator('#motivoDevolucaoCheque').fill('Cheque devolvido pelo banco: insuficiência de fundos');
    await modal.locator('#tarifaNovaCobrancaCheque').fill('15');
    await page.waitForTimeout(900);
    await shot('12-devolver-cheque', false);
    await modal.locator('#btnConfirmarDevolucaoCheque').click();
    await page.waitForTimeout(2500);
    await cheques('Todas');
    await shot('13-cheque-devolvido');
    await ir('/financeiro/contareceber'); await fecharAviso(); await page.waitForTimeout(800);
    await shot('14-cobrancas-devolucao');
  });

  // 8) Cartão de crédito em 3x
  await passo('15-baixa-cartao', async () => {
    const modal = await abrirBaixaReceber(cartao, '900,00');
    await modal.locator('select:has(option[value="2"])').first().selectOption('2');
    await modal.locator('label:has-text("Qtd. Parcelas") + select').selectOption({ label: '3x' });
    await modal.locator('#avisoRepasseParcelado').waitFor({ timeout: 5000 });
    await modal.locator('label:text-is("Valor") + input').fill('900,00');
    await modal.locator('label:has-text("Nº do documento (NSU/lote)") + input').fill('NSU 7731204');
    await modal.locator('label:has-text("Conta Financeira") ~ select').first().selectOption({ label: 'BANCO BRASIL' });
    await pausa();
    await shot('15-baixa-cartao', false);
    await modal.locator('button:has-text("Lançar")').first().click();
    await confirmarBaixa();
  });

  await passo('16-parcelas-repasse', async () => {
    await liquidacoes(true);
    await shot('16-parcelas-repasse');
  });

  await passo('17-liquidar-parcela', async () => {
    const linha = page.locator('tbody tr', { hasText: 'NSU 7731204' }).filter({ hasText: '1/3' }).first();
    await linha.locator('button:has-text("Liquidar")').click();
    const modal = page.locator('#modalLiquidarFinanceira'); await modal.waitFor({ state: 'visible' });
    await page.waitForTimeout(700);
    await shot('17-liquidar-parcela', false);
    await modal.locator('button:has-text("Confirmar liquidação")').click();
    await page.waitForTimeout(2500);
    await liquidacoes(true);
    await shot('18-parcela-liquidada');
  });

  // 9) Cancelar a baixa do cartão: bloqueado porque uma parcela já foi repassada
  await passo('19-cancelar-bloqueado', async () => {
    const modal = await abrirBaixaReceber(cartao, '900,00');
    await modal.locator('tbody tr button.btn-danger').first().click();
    const motivo = page.locator('#modalConfirmarBaixaRemover'); await motivo.waitFor({ state: 'visible' });
    await motivo.locator('select').selectOption({ index: 1 });
    await pausa();
    await shot('19-cancelar-baixa-motivo', false);
    await motivo.locator('button:has-text("Confirmar cancelamento")').click();
    await page.waitForTimeout(800);
    await shot('20-cancelar-bloqueado', false);
  });

  // 10) Pagamento com cheque emitido
  await passo('21-pagar-cheque-emitido', async () => {
    await ir('/financeiro/contapagar'); await fecharAviso();
    const linha = page.locator('tr', { hasText: 'ALUGUEL DA SALA' }).first();
    await linha.waitFor({ timeout: 15000 });
    await linha.locator('button[title="Pagamento / Acerto"]').click();
    const modal = page.locator('#modalContaPagarBaixa'); await modal.waitFor({ state: 'visible' }); await pausa();
    await modal.locator('select').filter({ has: page.locator('option', { hasText: 'Cheque' }) }).first().selectOption({ label: 'Cheque' });
    await modal.locator('#blocoCheque').waitFor({ timeout: 5000 });
    await modal.locator('label:has-text("Valor Pago") ~ input').first().fill('1.200,00');
    await modal.locator('#chequeContaSacada').selectOption({ index: 1 });
    await modal.locator('#chequeSerie').fill('B');
    await modal.locator('#chequeNumero').fill('000118');
    await dataCampo(modal.locator('#chequeBomPara'), mais(10));
    await modal.locator('label:has-text("Conta Financeira") ~ select').first().selectOption({ label: 'CAIXA' });
    await pausa();
    await shot('21-pagar-cheque-emitido', false);
    await modal.locator('button:has-text("Lançar")').first().click();
    await page.waitForTimeout(2500);
  });

  await passo('22-cheque-emitido', async () => {
    await ir('/financeiro/cheques'); await fecharAviso();
    await page.locator('#filtroTipo').selectOption({ label: 'Emitido' });
    await page.locator('#btnBuscarCheques').click(); await page.waitForTimeout(1500);
    await shot('22-lista-cheque-emitido');
    await page.locator('#tabelaCheques tbody tr button[id^="btnAlterar"]').first().click();
    const alterar = page.locator('#modalAlterarCheque'); await alterar.waitFor({ state: 'visible' }); await pausa();
    await shot('23-alterar-cheque', false);
    await alterar.locator('button:has-text("Fechar")').click(); await pausa();
    await page.locator('#tabelaCheques tbody tr button[id^="btnCompensar"]').first().click();
    const modal = page.locator('#modalCompensarCheque'); await modal.waitFor({ state: 'visible' }); await pausa();
    await shot('24-compensar-cheque-emitido', false);
    await modal.locator('#btnConfirmarCompensacao').click();
    await page.waitForTimeout(2500);
  });

  // 11) Filtros da lista de liquidações
  await passo('25-filtros', async () => {
    await liquidacoes(true);
    await page.locator('#filtroConta').selectOption({ label: 'BANCO BRASIL' });
    await dataCampo(page.locator('#filtroDataInicio'), mais(0));
    await dataCampo(page.locator('#filtroDataFim'), mais(70));
    await page.locator('button:has-text("Buscar")').click();
    await page.waitForTimeout(1500);
    await shot('25-filtros', false);
  });

  // 12) Fluxo de caixa projetado
  await passo('26-fluxo-projetado', async () => {
    await ir('/financeiro/fluxocaixa'); await fecharAviso();
    const botao = page.locator('button:has-text("Buscar")').first();
    if (await botao.count()) { await botao.click(); await page.waitForTimeout(2500); }
    await shot('26-fluxo-projetado');
  });

  await browser.close();
  console.log('captura concluída');
})().catch(e => { console.error(e.message); process.exit(1); });
