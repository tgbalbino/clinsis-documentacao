const { abrir } = require('./cap_common.js');
const path = require('path');
const OUT = 'C:/Projetos/W_Clinica/Controle-Tarefas/capturas/previa-menu';
const CSS1 = `.nav-treeview a{padding-left:14px !important;} .nav-sidebar .nav-treeview .nav-link .nav-icon{width:1.1rem !important;margin-right:.3rem !important;} .nav-sidebar .nav-treeview .nav-link{font-size:15px !important;}`;
const CSS2 = CSS1 + `.main-sidebar{width:230px !important;} body:not(.sidebar-mini-md):not(.sidebar-mini-xs):not(.layout-top-nav) .content-wrapper, body:not(.sidebar-mini-md):not(.sidebar-mini-xs):not(.layout-top-nav) .main-footer, body:not(.sidebar-mini-md):not(.sidebar-mini-xs):not(.layout-top-nav) .main-header{margin-left:230px !important;} .sidebar-mini .main-sidebar .nav-link{width:calc(230px - 1rem) !important;}`;
const CSS1B = CSS1 + `.nav-sidebar .nav-treeview .nav-link{font-size:14px !important;padding-right:6px !important;}`;
(async () => {
  const { browser, page, ir } = await abrir(__dirname, { viewport: { width: 1400, height: 2100 } });
  await ir('/financeiro/movimentos');
  await page.locator('.main-sidebar').getByText('Tabelas Aux.', { exact: true }).click(); await page.waitForTimeout(700);
  await page.locator('.main-sidebar').getByText('Cadastros', { exact: true }).nth(1).click().catch(() => {}); await page.waitForTimeout(700);
  const tirar = async (nome, css) => {
    let h;
    if (css) h = await page.addStyleTag({ content: css });
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(OUT, nome), clip: { x: 0, y: 0, width: 640, height: 2100 } });
    console.log(await page.evaluate(() => { const l=[...document.querySelectorAll('.nav-treeview .nav-link')].find(a=>a.innerText.includes('Formas de Pagamento')); const cs=getComputedStyle(l); const ic=l.querySelector('.nav-icon'); const ics=getComputedStyle(ic); const pp=l.querySelector('p'); return JSON.stringify({padL:cs.paddingLeft,padR:cs.paddingRight,fs:cs.fontSize,iconW:ics.width,iconM:ics.marginRight,linkW:l.getBoundingClientRect().width,pW:pp.getBoundingClientRect().width,pMargin:getComputedStyle(pp).marginLeft, disp:cs.display}); }));
    const quebras = await page.evaluate(() => [...document.querySelectorAll('.nav-treeview .nav-link p')].filter(p => p.getBoundingClientRect().height > 30).map(p => p.innerText.trim()));
    console.log(nome, 'itens que quebram:', quebras.length, quebras.join(' | '));
    if (h) await h.evaluate(e => e.remove());
    // menu
  };
  await tirar('0-atual.png');
  await tirar('1-opcao1.png', CSS1);
  await tirar('1b-opcao1-mais-compacta.png', CSS1B);
  await tirar('2-opcao2.png', CSS2);
  await browser.close();
})().catch(e => { console.error('FALHA', e.message.slice(0, 300)); process.exit(1); });
