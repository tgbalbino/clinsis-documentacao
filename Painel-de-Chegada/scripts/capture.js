// Captura das telas da documentação "Painel de Chegada (TV)" (Playwright).
// Pré-requisitos: node setup_dados.js preparar; API em :49041 e front em :4222 (proxy para 49041); administrador (E2E_LOGIN / E2E_SENHA).
// Banco local de teste; nunca produção. Se falhar no meio, rode "limpar" + "preparar" antes de repetir.
const fs = require('fs');
const path = require('path');
const { abrir, APP } = require('../../_scripts-comuns/cap_common.js');

const SHOTS = path.join(__dirname, 'screenshots');

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
  const abrirAgenda = async () => {
    await ir('/agenda'); await fecharAviso();
    await page.getByText('Acessar').first().click();
    await page.waitForLoadState('networkidle'); await pausa(4000);
    const pular = page.getByRole('button', { name: 'Pular' }); if (await pular.count()) { await pular.first().click(); await pausa(600); }
  };

  await passo('01-configuracao', async () => {
    await ir('/painel-chegada/configuracao'); await fecharAviso(); await pausa(1500);
    await shot('01-configuracao', false);
  });

  await passo('02-agenda-sem-tv', async () => {
    await abrirAgenda();
    await page.locator('.agenda-painel-aviso').first().waitFor({ timeout: 15000 });
    await shot('02-agenda-sem-tv', false);
  });

  const ctxTv = await browser.newContext({ viewport: { width: 1600, height: 900 } });
  const tv = await ctxTv.newPage();
  tv.setDefaultTimeout(20000);
  const shotTv = async (nome) => { await tv.waitForTimeout(600); await tv.screenshot({ path: path.join(SHOTS, nome + '.png') }); };
  let qrUrl = '';
  tv.on('response', async (r) => {
    if (/painelchegada\/tv\/desafio$/i.test(r.url()) && r.request().method() === 'POST') {
      try { const j = await r.json(); const d = j.data || j; qrUrl = d.qrUrl || d.QrUrl || ''; } catch { /* ignora */ }
    }
  });

  await passo('03-tv-qr', async () => {
    await tv.goto(`${APP}/painel-chegada`); await tv.waitForSelector('.painel-pareamento img', { timeout: 20000 });
    await shotTv('03-tv-qr');
  });

  await passo('04-autorizar', async () => {
    if (!qrUrl) throw new Error('qrUrl não capturada');
    await page.goto(new URL(qrUrl, APP).toString()); await page.waitForLoadState('networkidle'); await fecharAviso(); await pausa(800);
    await shot('04-autorizar', false);
    await page.getByRole('button', { name: /Autorizar/ }).click();
    await page.waitForSelector('.alert-success'); await pausa(600);
    await shot('04b-autorizado', false);
  });

  await passo('05-tv-aguardando', async () => {
    await tv.waitForSelector('.painel-vazio', { timeout: 30000 });
    await shotTv('05-tv-aguardando');
  });

  await passo('06-agenda-avisar', async () => {
    await abrirAgenda();
    const linha = page.locator('tr', { hasText: 'Paciente 0003' }).first();
    await linha.getByRole('button').first().click(); await pausa(800);
    await page.locator('.agenda-acao-painel-chegada').first().waitFor({ timeout: 10000 });
    await shot('06-agenda-avisar', false);
    await page.locator('.agenda-acao-painel-chegada').first().click(); await pausa(1800);
    valores.toast = (await page.locator('.toast-message').first().innerText().catch(() => '')).trim();
    await shot('06b-aviso-enviado', false);
  });

  await passo('07-tv-nova-chegada', async () => {
    await tv.waitForSelector('.painel-aviso', { timeout: 20000 });
    valores.tv = (await tv.locator('.painel-aviso').innerText()).replace(/\s+/g, ' ');
    await shotTv('07-tv-nova-chegada');
  });

  await passo('08-chamadas', async () => {
    await page.keyboard.press('Escape'); await pausa(500);
    await page.getByRole('button', { name: /Mais opções/ }).first().click(); await pausa(600);
    await page.getByText('Ver chamadas do painel').first().click(); await pausa(1800);
    await shot('08-chamadas', false);
  });

  fs.writeFileSync(path.join(__dirname, 'output', 'valores.json'), JSON.stringify(valores, null, 2));
  console.log('valores:', JSON.stringify(valores));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
