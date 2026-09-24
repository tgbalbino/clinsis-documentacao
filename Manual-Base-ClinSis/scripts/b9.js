const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot } = await start();
  await go('/relatorios');
  const links = await page.evaluate(() => [...document.querySelectorAll('a')].filter(a=>/Sessões Faturamento|Marcação Sessão Dia|Qtd\. Marcação|Presença Diária|Sequenciais/.test(a.textContent)).map(a=>a.textContent.trim()+' '+a.getAttribute('href')));
  console.log(links);
  for (const [u, n] of [['/relatorio/agenda/presencadiaria','g01-presenca-diaria'],['/relatorio/agenda/qtdmarcacao','g02-qtd-marcacao'],['/relatorio/agenda/atendimentos-sequenciais','g03-sequenciais']]) { await go(u); await page.waitForTimeout(1500); await shot(n); }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
