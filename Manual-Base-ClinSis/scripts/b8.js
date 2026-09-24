const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot } = await start();
  for (const [u, n] of [['/relatorios','f01-relatorios'],['/atendimento','f02-atendimento'],['/prontuario/profissional','f03-prontuario'],['/prontuario/paciente','f03b-prontuario-pacientes'],['/financeiro/contapagar','f04-contas-pagar'],['/financeiro/contareceber','f05-contas-receber'],['/aux/deparaprofissionalpac','f06-depara'],['/aux/feriados','f07-feriados']]) {
    await go(u); await page.waitForTimeout(1200); await shot(n); console.log(n);
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
