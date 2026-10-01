// Prints novos (tarefas 0012/0033, 0086, 0090-0093) para o Manual Base; salvam em screenshots/
const { abrir } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir('/agendamento?idAgenda=31'); await page.waitForTimeout(6000);
  await shot('d01-agendamento', false);
  await page.locator('button:has-text("Colunas")').first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  await shot('d10-colunas', false);
  console.log('colunas:', (await page.locator('.modal.show').last().innerText()).replace(/\s+/g, ' ').slice(0, 400));
  await page.locator('.modal.show button:has-text("Fechar"), .modal.show button:has-text("Cancelar")').first().click().catch(() => {}); await page.waitForTimeout(600);
  await page.locator('button:has-text("Exportar")').first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(1200);
  await shot('d11-exportar', false);
  console.log('exportar:', (await page.locator('.modal.show').last().innerText()).replace(/\s+/g, ' ').slice(0, 400));
  await page.locator('.modal.show button:has-text("Fechar"), .modal.show button:has-text("Cancelar")').first().click().catch(() => {}); await page.waitForTimeout(600);
  await ir('/operadora/pacientes'); await shot('c08c-operadora-pacientes', false);
  await ir('/acessos');
  await page.locator('button:has-text("Filtros")').first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(800);
  await shot('c08d-acessos-filtros', false);
  console.log('filtros acessos:', (await page.locator('.modal.show').last().innerText()).replace(/\s+/g, ' ').slice(0, 300));
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 500)); process.exit(1); });
