// uso: node dbg_modal.js <rota> "<texto botão que abre modal>" 
const { abrir } = require('./cap_common.js');
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await ir(process.argv[2]);
  console.log('BOTOES', (await page.locator('button:visible').allInnerTexts()).map(x=>x.trim()).filter(Boolean).join(' | '));
  if (process.argv[3]) {
    await page.click(`button:has-text("${process.argv[3]}")`); await page.waitForTimeout(1200);
    const m = page.locator('.modal.show').last();
    console.log(await m.evaluate(e => [...e.querySelectorAll('label,input,select,textarea,button')].map(x => x.tagName + ':' + (x.getAttribute('name')||x.getAttribute('formcontrolname')||x.getAttribute('id')||x.type||'') + ':' + (x.innerText||x.placeholder||'').trim().slice(0,25)).join('\n')));
    await shot('_dbg');
  }
  await browser.close();
})();
