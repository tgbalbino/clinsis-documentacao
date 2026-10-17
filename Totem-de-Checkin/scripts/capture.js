// Captura das telas da documentação "Totem de Check-in" (Playwright).
// Pré-requisitos: node setup_dados.js preparar; API em :49041 e front em :4222; usuário administrador (E2E_LOGIN / E2E_SENHA).
// Banco local de teste; nunca produção. Se falhar no meio, rode "limpar" + "preparar" antes de repetir.
const fs = require('fs');
const path = require('path');
const { abrir, APP } = require('../../_scripts-comuns/cap_common.js');

const SHOTS = path.join(__dirname, 'screenshots');
const CPF = '31666387096', NASC = '02101997';

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

  // revoga totens de execuções anteriores
  const lista = await chamar('GET', 'totem/configuracao');
  console.log('config atual:', JSON.stringify(lista).slice(0, 200));

  await passo('01-configuracao', async () => {
    await ir('/totem/configuracao'); await fecharAviso(); await pausa(1500);
    await shot('01-configuracao', false);
  });

  // Totem: contexto separado, sem login
  const ctxTotem = await browser.newContext({ viewport: { width: 1100, height: 780 } });
  const totem = await ctxTotem.newPage();
  totem.setDefaultTimeout(20000);
  await totem.route('http://localhost:49020/**', (route) => route.continue({ url: route.request().url().replace('localhost:49020', 'localhost:49041') }));
  const shotT = async (nome) => { await totem.waitForTimeout(500); await totem.screenshot({ path: path.join(SHOTS, nome + '.png') }); };
  let qrUrl = '';
  totem.on('response', async (r) => { if (/totem\/identificar/i.test(r.url())) { try { console.log('IDENTIFICAR', r.status(), (await r.text()).slice(0, 600)); } catch {} } });
  totem.on('response', async (r) => { if (/totem\/desafio$/i.test(r.url()) && r.request().method() === 'POST') { try { const j = await r.json(); qrUrl = (j.data || j).qrUrl || ''; } catch {} } });

  await passo('02-totem-qr', async () => {
    await totem.goto(`${APP}/totem`); await totem.waitForSelector('.totem-qr', { timeout: 20000 });
    await shotT('02-totem-qr');
  });

  await passo('03-autorizar', async () => {
    if (!qrUrl) throw new Error('qrUrl não capturada');
    await page.goto(new URL(qrUrl, APP).toString()); await page.waitForLoadState('networkidle'); await fecharAviso(); await pausa(800);
    await page.locator('#nomeTotem').fill('Totem da recepção');
    await shot('03-autorizar', false);
    await page.getByRole('button', { name: 'Autorizar totem' }).click();
    await page.waitForSelector('.alert-success'); await pausa(600);
    await shot('03b-autorizado', false);
  });

  await passo('04-totem-inicio', async () => {
    await totem.waitForSelector('text=Bem-vindo', { timeout: 30000 });
    await shotT('04-totem-inicio');
  });

  await passo('05-totem-cpf', async () => {
    await totem.getByRole('button', { name: 'Registrar chegada' }).click();
    for (const d of CPF.slice(0, 7)) await totem.locator('.totem-tecla', { hasText: new RegExp('^' + d + '$') }).first().click();
    await shotT('05-totem-cpf');
    for (const d of CPF.slice(7)) await totem.locator('.totem-tecla', { hasText: new RegExp('^' + d + '$') }).first().click();
    await totem.getByRole('button', { name: 'Continuar' }).click();
  });

  await passo('06-totem-nascimento', async () => {
    for (const d of NASC) await totem.locator('.totem-tecla', { hasText: new RegExp('^' + d + '$') }).first().click();
    await shotT('06-totem-nascimento');
    await totem.getByRole('button', { name: 'Confirmar', exact: true }).click();
  });

  await passo('07-totem-itens', async () => {
    await totem.waitForSelector('.totem-itens li', { timeout: 20000 }).catch(async (e) => { await shotT('ZZ-totem'); valores.erroTotem = (await totem.locator('main').innerText()).replace(/\s+/g, ' '); console.log(valores.erroTotem); throw e; });
    valores.itemTexto = (await totem.locator('.totem-itens li').first().innerText()).replace(/\s+/g, ' ');
    await shotT('07-totem-itens');
    await totem.getByRole('button', { name: 'Confirmar chegada' }).click();
  });

  await passo('08-totem-resultado', async () => {
    await totem.waitForSelector('.totem-selo', { timeout: 20000 });
    valores.resultado = (await totem.locator('h1').innerText()).trim();
    await shotT('08-totem-resultado');
  });

  await passo('09-agenda-chegou', async () => {
    await ir('/agenda'); await fecharAviso();
    await page.getByText('Acessar').first().click();
    await page.waitForLoadState('networkidle'); await pausa(4000);
    const pular = page.getByRole('button', { name: 'Pular' }); if (await pular.count()) { await pular.first().click(); await pausa(600); }
    const selo = page.locator('span.agenda-chegou-totem').first();
    await selo.waitFor({ timeout: 20000 });
    valores.selo = ((await selo.getAttribute('title')) || '').trim();
    await selo.scrollIntoViewIfNeeded();
    await shot('09-agenda-chegou', false);
  });

  await passo('10-configuracao-totens', async () => {
    await ir('/totem/configuracao'); await fecharAviso(); await pausa(1500);
    await shot('10-configuracao-totens', false);
  });

  fs.writeFileSync(path.join(__dirname, 'output', 'valores.json'), JSON.stringify(valores, null, 2));
  console.log('valores:', JSON.stringify(valores));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
