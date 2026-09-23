const { start } = require('./lib');
(async () => {
  const { browser, page, go, shot, modal } = await start();
  await go('/clinica/dados'); await shot('c01-clinica-dados');
  await go('/clinica/setores'); await shot('c02-setores');
  await go('/aux/especialidade'); await shot('c03-especialidades');
  await go('/profissional/lista'); await shot('c04-profissionais-lista');
  await go('/profissional/cadastro'); await shot('c05-profissional-cadastro', true);
  await go('/paciente/lista'); await shot('c06-pacientes-lista');
  await go('/paciente/cadastro'); await shot('c07-paciente-cadastro', true);
  await go('/operadora/lista'); await shot('c08-operadoras');
  await go('/acessos');
  await page.locator('button:visible:has-text("Novo"), a:visible:has-text("Novo")').first().click();
  await page.waitForTimeout(1500); await shot('c09-acesso-novo', true);
  console.log(page.url());
  await go('/acessos');
  await page.locator('tbody tr').nth(2).locator('button:visible').first().click(); await page.waitForTimeout(600); await shot('c10-acesso-menu');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
