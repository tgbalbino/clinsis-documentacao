// Captura das telas novas do manual "Contas a Receber" (v1.2): aviso de pagamento em atraso na baixa e relatório de recebimentos.
// Pré-requisitos: node setup_atrasos.js preparar; API em :49041 e front em :4222 (proxy para 49041); administrador (E2E_LOGIN / E2E_SENHA).
// Banco local de teste; nunca produção. Não confirma a baixa do título em aberto (responde Não ao aviso).
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

  await passo('R01-baixa-em-atraso', async () => {
    await ir('/financeiro/contareceber'); await fecharAviso(); await pausa(1500);
    await shot('R00-lista-paciente', false);
    const linha = page.locator('tr').filter({ hasText: 'Paciente 0002' }).filter({ hasText: 'Aberto' }).filter({ hasText: '20/09/2026' }).first();
    await linha.locator('button.btn-success').click(); await page.waitForSelector('.modal.show'); await pausa(1200);
    const b = page.locator('.modal.show').last();
    const vb = b.locator('input[type=text]').nth(9); await vb.click(); await vb.fill('100,00'); await vb.press('Tab');
    await b.locator('select').nth(0).selectOption({ label: 'Pix' }); await pausa(500);
    await b.locator('select').filter({ hasText: 'Selecione' }).last().selectOption({ index: 1 }); await pausa(500);
    await shot('R01-baixa-preenchida', false);
    await b.locator('button.btn-lancar').click(); await pausa(1200);
    valores.aviso = (await page.locator('.modal.show').last().innerText()).replace(/\s+/g, ' ').slice(0, 500);
    await shot('R02-aviso-atraso', false);
    await page.locator('button:visible', { hasText: /^\s*N[aã]o\s*$/ }).first().click().catch(() => {}); await pausa(800);
  });

  await passo('R03-relatorio', async () => {
    await ir('/relatorio/conta-receber/recebimentos'); await fecharAviso(); await pausa(1500);
    const hoje = new Date(); const dd = String(hoje.getDate()).padStart(2, '0') + '/' + String(hoje.getMonth() + 1).padStart(2, '0') + '/' + hoje.getFullYear();
    const campos = page.locator('.modal.show input[bsdatepicker]');
    if (await campos.count() === 0) { await page.getByRole('button', { name: /Filtros/ }).first().click(); await pausa(800); }
    await page.locator('.modal.show input[bsdatepicker]').nth(0).fill(dd); await page.keyboard.press('Escape');
    await page.locator('.modal.show input[bsdatepicker]').nth(1).fill(dd); await page.keyboard.press('Escape');
    await pausa(300);
    await page.locator('.modal.show button:has-text("Filtrar")').first().click(); await pausa(2500);
    valores.relatorio = (await page.locator('table').first().innerText()).replace(/\s+/g, ' ').slice(0, 600);
    await shot('R03-relatorio-recebimentos', false);
  });

  fs.writeFileSync(path.join(__dirname, 'output', 'valores_atrasos.json'), JSON.stringify(valores, null, 2));
  console.log(JSON.stringify(valores, null, 1));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
