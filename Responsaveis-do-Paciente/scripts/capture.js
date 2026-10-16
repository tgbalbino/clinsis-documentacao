// Captura das telas da documentação "Responsáveis do Paciente" (Playwright).
// Pré-requisitos: node setup_dados.js preparar; API em :49041 e front em :4222 (proxy para 49041); administrador (E2E_LOGIN / E2E_SENHA).
// Banco local de teste; nunca produção. Se falhar no meio, rode "limpar" + "preparar" antes de repetir.
const fs = require('fs');
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const valores = {};
  page.on('dialog', (d) => d.accept().catch(() => {}));
  const passo = async (nome, fn) => {
    try { await fn(); console.log('ok  ', nome); }
    catch (e) { console.log('FALHA', nome, '-', e.message.split('\n')[0]); await shot('ZZ-erro-' + nome).catch(() => {}); throw e; }
  };
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };
  const pausa = (ms = 500) => page.waitForTimeout(ms);
  const fieldset = () => page.locator('app-paciente-responsaveis fieldset');

  await passo('01-pessoa-filtro', async () => {
    await ir('/cadastro/pessoa'); await fecharAviso();
    await page.getByRole('button', { name: /Filtros/ }).first().click(); await pausa(800);
    await page.locator('.modal.show').getByLabel('Responsável', { exact: true }).check();
    await shot('01-pessoa-filtro', false);
    await page.getByRole('button', { name: 'Aplicar' }).click(); await pausa(2000);
    await shot('01b-pessoa-lista', false);
  });

  await passo('02-paciente-sem-responsavel', async () => {
    await ir('/paciente/cadastro?id=33'); await fecharAviso(); await pausa(2500);
    await fieldset().scrollIntoViewIfNeeded(); await pausa(500);
    await shot('02-paciente-sem-responsavel', false);
  });

  await passo('03-paciente-com-responsavel', async () => {
    await ir('/paciente/cadastro?id=18'); await fecharAviso(); await pausa(2500);
    await fieldset().scrollIntoViewIfNeeded(); await pausa(500);
    await shot('03-paciente-com-responsavel', false);
  });

  await passo('04-modal-novo', async () => {
    await page.getByRole('button', { name: /Adicionar responsável/ }).click(); await pausa(1000);
    await page.locator('#respCpf').pressSequentially('52998224725', { delay: 40 });
    await page.locator('#respNome').fill('João Responsável Demonstração');
    await page.locator('#respParentesco').selectOption({ label: 'Pai' });
    await page.locator('#respCelular').pressSequentially('31999990000', { delay: 30 });
    await page.locator('#respNasc').fill('1982-06-21');
    await pausa(500);
    await shot('04-modal-novo', false);
  });

  await passo('05-tabela-com-responsavel', async () => {
    await page.getByRole('button', { name: 'Confirmar', exact: true }).click(); await pausa(1200);
    await fieldset().scrollIntoViewIfNeeded(); await pausa(400);
    await shot('05-tabela-com-responsavel', false);
  });

  await passo('06-salvo', async () => {
    await page.getByRole('button', { name: /Salvar/ }).first().click(); await pausa(2500);
    valores.salvo = (await page.locator('.toast-message').first().innerText().catch(() => '')).trim();
    await shot('06-salvo', false);
  });

  await passo('07-pessoa-responsavel', async () => {
    await ir('/cadastro/pessoa'); await fecharAviso();
    await page.getByRole('button', { name: /Filtros/ }).first().click(); await pausa(800);
    await page.locator('.modal.show').getByLabel('Responsável', { exact: true }).check();
    await page.getByRole('button', { name: 'Aplicar' }).click(); await pausa(2000);
    await shot('07-pessoa-responsavel', false);
  });

  fs.writeFileSync(path.join(__dirname, 'output', 'valores.json'), JSON.stringify(valores, null, 2));
  console.log('valores:', JSON.stringify(valores));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
