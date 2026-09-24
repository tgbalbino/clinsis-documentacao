const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot } = await start();
  await go('/home');
  const t = await page.evaluate(() => { document.querySelectorAll('.nav-sidebar .has-treeview > a, .nav-sidebar .nav-item > a').forEach(()=>{}); return [...document.querySelectorAll('.nav-sidebar li')].map(li => { const a = li.querySelector(':scope > a'); const depth = (li.parentElement.closest('li')? (li.parentElement.closest('li').parentElement.closest('li')?2:1):0); return '  '.repeat(depth) + (a? a.textContent.trim().replace(/\s+/g,' '):'') + ' -> ' + (a? a.getAttribute('href')||'':''); }).join('\n'); });
  console.log(t);
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
