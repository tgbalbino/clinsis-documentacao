// Captura das telas "Cancelar documento" do manual "Contas a Receber" (v1.2).
// Pré-requisitos: node setup_atrasos.js preparar (cria o título em aberto de R$ 100,00 do Paciente 0002 vencido em 20/09/2026);
// API em :49041 e front em :4222 (proxy para 49041); administrador (E2E_LOGIN / E2E_SENHA). O "limpar" do setup apaga o título.
const fs = require('fs');
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const valores = {};
  page.on('dialog', (d) => d.accept().catch(() => {}));
  const passo = async (nome, fn) => {
    try { await fn(); console.log('ok  ', nome); }
    catch (e) { console.log('FALHA', nome, '-', e.message.split('\n')[0]); await shot('ZZ-erro-' + nome).catch(() => {}); throw e; }
  };
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };
  const pausa = (ms = 500) => page.waitForTimeout(ms);

  await passo('C01-abrir-cadastro', async () => {
    await ir('/financeiro/contareceber'); await fecharAviso(); await pausa(1500);
    const linha = page.locator('tr').filter({ hasText: 'Paciente 0002' }).filter({ hasText: 'Aberto' }).filter({ hasText: '20/09/2026' }).first();
    await linha.locator('button.btn-warning').click(); await page.waitForSelector('.modal.show'); await pausa(1500);
    await shot('C01-cadastro-cancelar', false);
  });

  await passo('C02-modal-cancelar', async () => {
    await page.locator('.modal.show').last().getByRole('button', { name: /Cancelar documento/ }).click(); await pausa(1000);
    const sel = page.locator('#modalCancelarContaReceber select');
    valores.motivos = await sel.locator('option').allInnerTexts();
    if (valores.motivos.length > 1) await sel.selectOption({ index: 1 });
    await shot('C02-modal-cancelar', false);
    await page.locator('#modalCancelarContaReceber').getByRole('button', { name: 'Confirmar cancelamento' }).click(); await pausa(2500);
    valores.toast = (await page.locator('.toast-message').allInnerTexts()).join(' | ');
    await shot('C03-cancelado', false);
  });

  fs.writeFileSync(path.join(__dirname, 'output', 'valores_cancelar.json'), JSON.stringify(valores, null, 2));
  console.log(JSON.stringify(valores));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
