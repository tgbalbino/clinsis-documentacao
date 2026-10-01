// uso: node controla_caixa.js on|off  — liga/desliga "Controla Caixa" do ADMIN TESTE AUTOMACAO (clínica 1)
const { abrir } = require('./cap_common.js');
(async () => {
  const quer = process.argv[2] !== 'off';
  const { browser, page, ir } = await abrir(__dirname);
  await ir('/acessos');
  await page.locator('tr').filter({ hasText: 'ADMIN TESTE' }).first().locator('button').first().click(); await page.waitForTimeout(500);
  await page.locator('.dropdown-menu.show a, .dropdown-menu.show button').filter({ hasText: /Editar/ }).first().click(); await page.waitForTimeout(1000);
  const chk = page.locator('#sw-ControlaCaixa');
  console.log('atual:', await chk.isChecked(), 'desejado:', quer);
  if ((await chk.isChecked()) !== quer) { await page.locator(`label[for="sw-ControlaCaixa"]`).click(); await page.waitForTimeout(300); { const st = page.locator('.modal.show select').nth(2); if ((await st.inputValue()) === '' || (await st.inputValue()) === '0') await st.selectOption({ index: 1 }); } console.log('btns', (await page.locator('button:visible').allInnerTexts()).map(x=>x.trim()).filter(Boolean).join('|')); await page.locator('button:visible', { hasText: /Salvar|Confirmar|Gravar/ }).last().click(); await page.waitForTimeout(1500); }
  await browser.close();
})().catch(e => { console.error('FALHA:', e.message.slice(0, 300)); process.exit(1); });
