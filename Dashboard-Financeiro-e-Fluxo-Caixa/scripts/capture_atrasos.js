// Captura das telas novas do manual "Dashboard Financeiro e Fluxo de Caixa" (v1.2): cards de recebimento em atraso e
// o aviso de baixas aguardando compensação no Fluxo de Caixa Projetado.
// Pré-requisitos: API em :49041 e front em :4222 (proxy para 49041); administrador (E2E_LOGIN / E2E_SENHA). Somente leitura.
const fs = require('fs');
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const valores = {};
  page.on('dialog', (d) => d.accept().catch(() => {}));
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };
  const datas = async (ini, fim) => {
    const campos = page.locator('input[bsdatepicker]');
    await campos.nth(0).fill(ini); await page.keyboard.press('Escape');
    await campos.nth(1).fill(fim); await page.keyboard.press('Escape');
    await page.waitForTimeout(300);
  };

  await ir('/financeiro/dashboard'); await fecharAviso();
  await datas('01/09/2026', '31/10/2026');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(3500);
  const card = page.locator('.small-box', { hasText: 'Recebido em atraso' }).first();
  await card.scrollIntoViewIfNeeded(); await page.waitForTimeout(500);
  valores.recebidoEmAtraso = (await card.innerText()).replace(/\s+/g, ' ');
  valores.mediaAtraso = (await page.locator('.small-box', { hasText: 'Atraso médio' }).first().innerText()).replace(/\s+/g, ' ');
  valores.mesPosterior = (await page.locator('.small-box', { hasText: 'mês posterior' }).first().innerText()).replace(/\s+/g, ' ');
  await shot('A01-dashboard-atraso', false);

  await ir('/financeiro/fluxocaixa'); await fecharAviso();
  await datas('01/10/2026', '30/11/2026');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(3500);
  const proj = page.locator('.card', { hasText: 'Fluxo de Caixa Projetado' }).first();
  await proj.scrollIntoViewIfNeeded(); await page.waitForTimeout(500);
  valores.projetado = (await proj.innerText()).replace(/\s+/g, ' ');
  await shot('A02-fluxo-projetado', false);

  fs.writeFileSync(path.join(__dirname, 'output', 'valores_atrasos.json'), JSON.stringify(valores, null, 2));
  console.log(JSON.stringify(valores, null, 1));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
