// Captura das telas novas do manual "Dashboard de Agenda" (v3.2): evolução de presenças e ausências e indicador de retornos.
// Pré-requisitos: API em :49041 e front em :4222 (proxy para 49041); administrador (E2E_LOGIN / E2E_SENHA). Somente leitura.
const fs = require('fs');
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const valores = {};
  const pausa = (ms = 500) => page.waitForTimeout(ms);
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };

  await ir('/agenda/dashboard'); await fecharAviso(); await pausa(1500);
  const a = page.locator('input[bsdatepicker]').first(), b = page.locator('input[bsdatepicker]').nth(1);
  await a.fill('01/09/2026'); await page.keyboard.press('Escape'); await b.fill('30/09/2026'); await page.keyboard.press('Escape');
  await page.click('button:has-text("Buscar")'); await pausa(3500);

  const card = page.locator('.card', { hasText: 'Evolução de Presenças e Ausências por Agenda' }).first();
  await card.scrollIntoViewIfNeeded(); await pausa(1500);
  valores.opcoes = {
    periodicidade: await card.locator('select').nth(0).locator('option').allInnerTexts(),
    quantidade: await card.locator('select').nth(1).locator('option').allInnerTexts(),
    agrupar: await card.locator('select').nth(2).locator('option').allInnerTexts(),
    indicador: await card.locator('select').nth(3).locator('option').allInnerTexts()
  };
  await shot('E01-evolucao-geral', false);

  await card.locator('select').nth(2).selectOption({ label: 'Especialidade' }); await pausa(2500);
  await card.scrollIntoViewIfNeeded(); await pausa(500);
  await shot('E02-evolucao-especialidade', false);

  await card.locator('select').nth(0).selectOption({ label: 'Semanal' }); await pausa(2500);
  await card.locator('select').nth(2).selectOption({ label: 'Geral' }); await pausa(2500);
  await card.scrollIntoViewIfNeeded(); await pausa(500);
  valores.tabelaSemanal = (await card.locator('table').first().innerText().catch(() => '')).replace(/\s+/g, ' ').slice(0, 400);
  await shot('E03-evolucao-semanal', false);

  await page.evaluate(() => window.scrollTo(0, 0)); await pausa(400);
  valores.cardsRetorno = await page.locator('.small-box', { hasText: /Retorno/i }).allInnerTexts();
  await shot('E04-topo', false);

  fs.writeFileSync(path.join(__dirname, 'output', 'valores_evolucao.json'), JSON.stringify(valores, null, 2));
  console.log(JSON.stringify(valores, null, 1));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
