// Exportação CSV (tarefa 0107): sintético (agrupado) e analítico
const { abrir } = require('../../_scripts-comuns/cap_common.js');
const fs = require('fs');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const rodar = async (rota, nomeShot) => {
    await ir(rota);
    await page.click('button:has-text("Filtros")'); await page.waitForSelector('.modal.show'); await page.waitForTimeout(600);
    const sel = page.locator('.modal.show select').first();
    const opts = await sel.locator('option').all();
    console.log('opcoes:', (await sel.locator('option').allInnerTexts()).slice(0, 6).join('|'));
    await sel.selectOption(await opts[1].getAttribute('value'));
    await page.click('.modal.show button:has-text("Filtrar")'); await page.waitForTimeout(2500);
    await shot(nomeShot);
    const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 20000 }).catch(() => null), page.locator('button:has-text("Exportar"), a:has-text("Exportar")').first().click()]);
    if (dl) { const f = 'output_' + nomeShot + '.csv'; await dl.saveAs(f); const t = fs.readFileSync(f, 'utf8'); console.log(nomeShot, 'CSV:', dl.suggestedFilename(), '\n' + t.split('\n').slice(0, 4).join('\n')); fs.unlinkSync(f); }
    else console.log(nomeShot, 'sem download');
    await page.waitForTimeout(800);
  };
  await rodar('/relatorio/pagamento/profissional/agrupado', '24-sintetico-exportar');
  await rodar('/relatorio/pagamento/profissional', '25-analitico-exportar');
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
