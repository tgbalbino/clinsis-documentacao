// Captura das telas da documentação "Revisão cadastral de pacientes" (Playwright).
// Pré-requisitos: node setup_dados.js preparar; API em :49041 e front em :4222 (cap_common redireciona a API fixa do front);
// usuário administrador (E2E_LOGIN / E2E_SENHA). Banco local de teste; nunca produção.
// A captura marca um paciente como revisado (salvando o cadastro): se falhar no meio, rode "limpar" + "preparar" antes de repetir.
const fs = require('fs');
const path = require('path');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

const { pacientes } = JSON.parse(fs.readFileSync(path.join(__dirname, 'output', 'estado_demo.json'), 'utf8'));
const VALORES = path.join(__dirname, 'output', 'valores.json');

(async () => {
  const { browser, page, ir, shot, chamar } = await abrir(__dirname);
  const valores = {};
  page.on('dialog', (d) => d.accept().catch(() => {}));
  const passo = async (nome, fn) => {
    try { await fn(); console.log('ok  ', nome); }
    catch (e) { console.log('FALHA', nome, '-', e.message.split('\n')[0]); await shot('ZZ-erro-' + nome).catch(() => {}); throw e; }
  };
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };
  const pausa = (ms = 500) => page.waitForTimeout(ms);

  await passo('01-menu', async () => {
    await ir('/paciente/revisao-cadastral'); await fecharAviso();
    await page.waitForSelector('table tbody tr');
    await shot('01-menu', false);
  });

  await passo('02-lista', async () => {
    await page.selectOption('#rc-motivo', 'todos'); await pausa(1500);
    valores.total = (await page.locator('span.ml-auto.text-muted').innerText()).trim();
    await shot('02-lista', false);
  });

  await passo('03-filtro-endereco', async () => {
    await page.selectOption('#rc-motivo', 'endereco'); await pausa(1500);
    await shot('03-filtro-endereco', false);
    await page.selectOption('#rc-motivo', 'contato'); await pausa(1500);
    await shot('03b-filtro-contato', false);
    await page.selectOption('#rc-motivo', 'todos'); await pausa(1500);
  });

  await passo('04-confirmar-lote', async () => {
    const linha = page.locator('tr', { hasText: 'Paciente 0011' }).first();
    await linha.locator('input[type=checkbox]').check();
    await page.getByRole('button', { name: /Marcar como revisado/ }).click(); await pausa(800);
    await shot('04-confirmar-lote', false);
    await page.getByRole('button', { name: /^(Não|Cancelar|Fechar)/ }).first().click().catch(() => {}); await pausa(600);
  });

  await passo('05-parametro', async () => {
    await ir('/aux/parametro'); await fecharAviso(); await pausa(1500);
    await shot('05-parametro', false);
  });

  await passo('06-agenda-selo', async () => {
    await ir('/agenda'); await fecharAviso();
    await page.getByText('Acessar').first().click();
    await page.waitForLoadState('networkidle'); await pausa(4000);
    await page.locator('a.agenda-revisar-cadastro').first().waitFor({ timeout: 15000 });
    const pular = page.getByRole('button', { name: 'Pular' }); if (await pular.count()) { await pular.first().click(); await pausa(600); }
    await page.locator('a.agenda-revisar-cadastro').first().scrollIntoViewIfNeeded();
    await shot('06-agenda-selo', false);
  });

  await passo('07-checkin-aviso', async () => {
    const op = (await chamar('GET', 'operadora/listar') || {}).data;
    let idOperadora = 5;
    if (Array.isArray(op)) { const p = op.find(o => o.PlanoProprio || o.planoProprio); if (p) idOperadora = p.IdOperadora || p.idOperadora; }
    const r = await chamar('GET', `paciente/codigocartao/gerar/${pacientes.vencido}/${idOperadora}`);
    await ir('/paciente/checkin'); await fecharAviso();
    await page.getByRole('button', { name: 'Realizar Check-In' }).click(); await pausa(800);
    await page.locator('#txtCodBar').fill(r.data); await page.keyboard.press('Enter'); await pausa(3000);
    await page.locator('.alert-warning', { hasText: 'precisa de revis' }).waitFor({ timeout: 10000 });
    await shot('07-checkin-aviso', false);
  });

  await passo('08-cadastro-aviso', async () => {
    await ir('/paciente/cadastro?id=' + pacientes.vencido); await fecharAviso();
    await page.locator('.alert-warning', { hasText: 'precisa de revis' }).waitFor({ timeout: 10000 });
    await pausa(800);
    await shot('08-cadastro-aviso', false);
  });

  await passo('09-cadastro-confirmado', async () => {
    await page.getByRole('button', { name: 'Confirmar dados atualizados' }).click(); await pausa(2000);
    await shot('09-cadastro-confirmado', false);
  });

  await passo('10-lista-depois', async () => {
    await ir('/paciente/revisao-cadastral'); await fecharAviso(); await pausa(1500);
    valores.totalDepois = (await page.locator('span.ml-auto.text-muted').innerText()).trim();
    await shot('10-lista-depois', false);
  });

  fs.writeFileSync(VALORES, JSON.stringify(valores, null, 2));
  console.log('valores:', JSON.stringify(valores));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
