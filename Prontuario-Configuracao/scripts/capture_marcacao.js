// Captura das telas novas do manual "Prontuário - Configuração" (v1.1): Clonar tipo, alínea de Marcação e pré-visualização.
// Pré-requisitos: node setup_marcacao.js preparar; API em :49041 e front em :4222 (proxy para 49041); administrador (E2E_LOGIN / E2E_SENHA).
// Banco local de teste; nunca produção. Cria o tipo "Anamnese (modelo)" por clonagem; o setup "limpar" apaga.
// As imagens vão para scripts/screenshots e depois são copiadas para scripts/ (o doc.py lê de lá).
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
  const modal = () => page.locator('.modal.show').last();

  await passo('M01-tipos-clonar', async () => {
    await ir('/prontuario/tipos'); await fecharAviso(); await pausa(1500);
    await shot('M01-tipos-clonar', false);
    await page.locator('tr', { hasText: 'Anamnese' }).first().locator('button[title^="Clonar"]').click(); await pausa(900);
    await modal().locator('input[type=text]').fill('Anamnese (modelo)');
    await shot('M02-clonar-modal', false);
    await modal().getByRole('button', { name: 'Clonar', exact: true }).click(); await pausa(2500);
    valores.clonar = (await page.locator('.toast-message').first().innerText().catch(() => '')).trim();
    await shot('M03-tipo-clonado', false);
  });

  await passo('M04-alinea-marcacao', async () => {
    await ir('/prontuario/alineas'); await fecharAviso(); await pausa(1500);
    await page.locator('select.form-control').first().selectOption({ label: 'Anamnese (modelo)' }); await pausa(1500);
    await shot('M04-alineas-do-clone', false);
    await page.getByRole('link', { name: /Novo/ }).first().click().catch(async () => { await page.getByText('Novo').first().click(); });
    await pausa(1000);
    await modal().locator('select').nth(1).selectOption('M'); await pausa(600);
    await modal().locator('input[placeholder^="Título que o profissional"]').fill('Como o paciente chegou');
    await modal().getByText('Várias opções').click(); await pausa(300);
    for (const op of ['Sozinho', 'Com acompanhante', 'Encaminhado por outro serviço']) {
      await modal().getByRole('button', { name: /Adicionar opção/ }).click(); await pausa(300);
      await modal().locator('input[placeholder="Descrição da opção"]').last().fill(op);
    }
    await modal().getByText('Permitir "Outros"').click(); await pausa(300);
    await modal().getByText(/^Obrigatória/).click(); await pausa(300);
    await shot('M05-modal-marcacao', false);
  });

  await passo('M06-preview-alinea', async () => {
    await modal().getByRole('button', { name: /Pré-visualizar/ }).click(); await pausa(1200);
    await shot('M06-preview-alinea', false);
    await page.locator('.al-preview-fundo').getByRole('button', { name: 'Fechar' }).click(); await pausa(900);
  });

  await passo('M07-salvar-alinea', async () => {
    await modal().getByRole('button', { name: /^Salvar/ }).click(); await pausa(2000);
    valores.salvar = (await page.locator('.toast-message').first().innerText().catch(() => '')).trim();
    await modal().getByRole('button', { name: 'Fechar' }).click().catch(() => {}); await pausa(1200);
    await shot('M07-alineas-com-marcacao', false);
  });

  await passo('M08-preview-prontuario', async () => {
    await page.getByRole('button', { name: /Pré-visualizar prontuário/ }).click(); await pausa(1500);
    valores.previewTodas = (await page.locator('.al-preview-fundo').innerText()).replace(/\s+/g, ' ').slice(0, 300);
    await shot('M08-preview-prontuario', false);
  });

  fs.writeFileSync(path.join(__dirname, 'output_marcacao.json'), JSON.stringify(valores, null, 2));
  console.log('valores:', JSON.stringify(valores));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
