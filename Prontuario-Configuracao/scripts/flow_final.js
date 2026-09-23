const { open, go, shot } = require('./lib');
const NOME = 'Relatório de Alta';
(async () => {
  let { browser, page } = await open('99999999999', 'Cli99999');
  const modal = () => page.locator('.modal.show').last();
  const espera = (ms = 1500) => page.waitForTimeout(ms);
  // ---- Tipos
  await go(page, '/prontuario/tipos'); await shot(page, '01-tipos');
  await page.locator('.btn-primary:has-text("Novo")').first().click(); await espera(1200);
  await modal().locator('input').first().fill(NOME); await shot(page, '02-tipo-novo');
  await modal().locator('button:has-text("Salvar")').click(); await espera(2500); await shot(page, '03-tipo-criado');
  await page.locator('tr', { hasText: NOME }).locator('button.btn-warning').click(); await espera(1500);
  await modal().locator('input.form-control').first().fill('30');
  await modal().locator('input[type=checkbox]').check(); await shot(page, '04-tipo-alterar');
  await modal().locator('button:has-text("Salvar")').click(); await espera(2500);
  await shot(page, '05-tipo-alterado');
  // ---- Alíneas
  await go(page, '/prontuario/alineas');
  await page.locator('select').first().selectOption({ label: NOME }); await espera(1200);
  await shot(page, '06-alineas-tipo-vazio');
  await page.locator('.btn-primary:has-text("Novo")').first().click(); await espera(1500);
  const add = async (campo, texto, nomeShot) => {
    await modal().locator('select').nth(0).selectOption({ label: NOME });
    await modal().locator('select').nth(1).selectOption(campo);
    await modal().locator('input').last().fill(texto);
    if (nomeShot) await shot(page, nomeShot);
    await modal().locator('button:has-text("Salvar")').click(); await espera(1800);
  };
  await add('T', 'Resumo do atendimento', '07-alinea-nova');
  await add('T', 'Conduta e orientações');
  await add('A', 'Anexar laudo (arquivo)');
  await modal().locator('button:has-text("Fechar")').click(); await espera(1200);
  await page.locator('select').first().selectOption({ label: NOME }); await espera(1500);
  await shot(page, '08-alineas-do-tipo');
  await page.locator('button:has(i.fa-arrow-down)').first().click(); await espera(700);
  await shot(page, '09-alineas-ordenar');
  await page.locator('button.btn-warning:has-text("Salvar")').click(); await espera(2000);
  await shot(page, '10-alineas-ordem-salva');
  console.log('alineas:', JSON.stringify(await page.locator('tbody tr').allInnerTexts()));
  await browser.close();

  // ---- Texto padrão (profissional)
  ({ browser, page } = await open('55555555555', 'Cli55555'));
  const modal2 = () => page.locator('.modal.show').last();
  await go(page, '/prontuario/textopadrao');
  await page.locator('.btn-primary:has-text("Novo")').first().click(); await espera(1500);
  await modal2().locator('select').selectOption({ label: 'Anamnese' });
  await modal2().locator('input.form-control').fill('Queixa inicial');
  await modal2().locator('textarea').fill('Paciente refere ... (texto padrão para agilizar o preenchimento).');
  await shot(page, '11-texto-padrao-novo');
  await modal2().locator('button:has-text("Salvar")').click(); await espera(2000);
  await shot(page, '12-texto-padrao-lista');
  console.log('textos:', JSON.stringify(await page.locator('tbody tr').allInnerTexts()));
  await browser.close();
})();
