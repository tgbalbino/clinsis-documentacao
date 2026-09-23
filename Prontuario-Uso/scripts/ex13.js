const { open, go, shot } = require('./lib');
(async () => {
  const { browser, page } = await open('55555555555', 'Cli55555');
  const modal = () => page.locator('.modal.show').last();
  await go(page, '/prontuario/profissional'); await modal().locator('select').first().selectOption({ label: 'Anamnese' }); await modal().locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await page.locator('.btn-primary:has-text("Novo")').first().click(); await page.waitForTimeout(1500);
  await modal().locator('button:has-text("Listar Pacientes da agenda atual")').click(); await page.waitForTimeout(2500);
  await modal().locator('tr', { hasText: 'Paciente 0003' }).locator('input[type=checkbox]').check();
  await modal().locator('select').selectOption({ label: 'NEUROPSICOLOGO' });
  await modal().locator('button:has-text("Adicionar")').click(); await page.waitForTimeout(3000);
  const id = new URL(page.url()).searchParams.get('idProntuario'); console.log('criado', id);
  await go(page, '/prontuario/profissional'); await modal().locator('select').first().selectOption({ label: 'Anamnese' }); await modal().locator('input').first().fill(id); await modal().locator('button:has-text("Pesquisar")').click(); await page.waitForTimeout(2500);
  await shot(page, '19-lista-rascunho');
  await page.locator('tbody tr').first().locator('button.btn-danger').click(); await page.waitForTimeout(1200);
  await shot(page, '20-excluir-rascunho');
  await page.getByRole('button', { name: 'Sim', exact: true }).click(); await page.waitForTimeout(2000);
  console.log('linhas apos excluir:', await page.locator('tbody tr').count());
  await browser.close();
})();
