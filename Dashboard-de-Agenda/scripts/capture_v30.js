// v3.0 (30/09/2026): refaz todos os prints do Dashboard de Agenda no banco a3_cli_hoje e acrescenta a lista de Ausentes (Absenteísmo/Antecedência).
const { abrir } = require('../../_scripts-comuns/cap_common.js');
const ID_AGENDA = process.env.ID_AGENDA || '31'; // Setembro/2026
(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  const periodo = async (ini, fim) => {
    const a = page.locator('input[bsdatepicker]').first(), b = page.locator('input[bsdatepicker]').nth(1);
    await a.fill(ini); await page.keyboard.press('Escape'); await b.fill(fim); await page.keyboard.press('Escape');
    await page.click('button:has-text("Buscar")'); await page.waitForTimeout(3000);
  };
  const fechar = async () => { await page.locator('.modal.show button:has-text("Fechar")').last().click().catch(() => page.keyboard.press('Escape')); await page.waitForTimeout(700); };
  const modalTxt = async () => (await page.locator('.modal.show').last().innerText()).replace(/\s+/g, ' ').slice(0, 260);

  // ---- Dashboard de Setembro
  await ir('/agenda/dashboard'); await page.waitForTimeout(1500);
  await periodo('01/09/2026', '30/09/2026');
  await page.evaluate(() => window.scrollTo(0, 0)); await shot('40-dashboard-setembro-cards', false);
  await page.locator('.card-header:has-text("Sessões Registradas por Status")').scrollIntoViewIfNeeded(); await page.waitForTimeout(500); await shot('11-graficos', false);
  await page.locator('.card-header:has-text("Por Profissional")').scrollIntoViewIfNeeded(); await page.waitForTimeout(500); await shot('12-tabelas-profissional-especialidade', false);
  await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(300);
  const prev = page.locator('text=Sessões Previstas').first();
  if (await prev.count()) { await prev.scrollIntoViewIfNeeded(); await page.waitForTimeout(400); await shot('48-dashboard-previstas', false); }

  // ---- listas dos cards (drill-down)
  for (const [card, arq] of [['Taxa de Presença', '44-dashboard-drilldown'], ['Taxa de Absenteísmo', '49-drilldown-ausentes'], ['Pacientes Novos', '45-drilldown-novos'], ['Taxa de Ocupação', '46-drilldown-capacidade']]) {
    await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(300);
    await page.locator('.small-box', { hasText: card }).first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(1800);
    console.log(card, '=>', await modalTxt());
    await shot(arq, false); await fechar();
  }

  // ---- Faturamento por convênio (01/01 a 30/09)
  await page.evaluate(() => window.scrollTo(0, 0));
  await periodo('01/01/2026', '30/09/2026');
  await page.locator('.card-header:has-text("Faturamento por Convênio")').scrollIntoViewIfNeeded(); await page.waitForTimeout(600);
  await shot('43-faturamento-corrigido', false);
  const linhaFat = page.locator('.card:has(.card-header:has-text("Faturamento por Convênio")) tbody tr').first();
  console.log('faturamento linhas:', await page.locator('.card:has(.card-header:has-text("Faturamento por Convênio")) tbody tr').count());
  if (await linhaFat.count()) { await linhaFat.click().catch(() => {}); await page.waitForTimeout(1800); if (await page.locator('.modal.show').count()) { console.log('fat =>', await modalTxt()); await shot('47-drilldown-faturamento', false); await fechar(); } }

  // ---- Agenda de Setembro: grade e filtro Sessão 1 = PRESENTE
  await ir(`/agendamento?idAgenda=${ID_AGENDA}`); await page.waitForTimeout(5000);
  await shot('22-agendamento-grade-mes', false);
  console.log('rodape grade:', (await page.locator('body').innerText()).match(/Total de registros: \d+/)?.[0]);
  await page.locator('button:has-text("Filtros"):visible').first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(600);
  const modalF = page.locator('.modal.show').last();
  const selS1 = modalF.locator('label', { hasText: 'Sessão 1' }).first().locator('xpath=following-sibling::select').first();
  for (const o of await selS1.locator('option').all()) { if ((await o.textContent() || '').trim() === 'PRESENTE') { await selS1.selectOption(await o.getAttribute('value')); break; } }
  await shot('23a-modal-filtro-sessao1-presente', false);
  await modalF.locator('button:has-text("Filtrar")').first().click(); await page.waitForTimeout(1500);
  await page.locator('.modal.show button:has-text("Fechar")').click().catch(() => {}); await page.waitForTimeout(600);
  await shot('23-agendamento-filtro-sessao1-presente', false);
  console.log('rodape filtro:', (await page.locator('body').innerText()).match(/Total de registros: \d+/)?.[0]);

  // ---- Relatório Agenda - Qtd Marcação
  await ir('/relatorio/agenda/qtdmarcacao'); await page.waitForTimeout(1000);
  const mq = page.locator('.modal.show').last();
  if (await mq.count()) {
    const sel = mq.locator('select').first();
    for (const o of await sel.locator('option').all()) { const t = (await o.textContent() || '').trim(); if (t.includes('2026') && t.toUpperCase().includes('SETEMBRO')) { await sel.selectOption(await o.getAttribute('value')); break; } }
    await mq.locator('button:has-text("Buscar"), button:has-text("Pesquisar"), button:has-text("Filtrar")').first().click(); await page.waitForTimeout(2000);
  }
  await shot('24-relatorio-qtd-marcacao', false);
  console.log('qtd marcacao:', (await page.locator('.content-wrapper').innerText()).replace(/\s+/g, ' ').slice(0, 700));

  // ---- Horários do profissional
  await ir(`/agenda/profissional?idAgenda=${ID_AGENDA}`); await page.waitForTimeout(1000);
  await page.evaluate(() => localStorage.setItem('agendaProfissional.apresentacao.1', 'vista'));
  const sp = page.locator('#apnProfissional');
  if (await sp.count()) { const alvo = (await sp.locator('option').allTextContents()).find(o => o.trim().startsWith('Profissional 01')); if (alvo) await sp.selectOption({ label: alvo }); await page.waitForTimeout(1800); }
  await shot('42-prof-horarios', false);

  // ---- Financeiro - Recebimentos (01/01 a 30/09)
  await ir('/relatorio/conta-receber/recebimentos'); await page.waitForTimeout(800);
  await page.locator('button:has-text("Filtros"):visible').first().click(); await page.waitForSelector('.modal.show'); await page.waitForTimeout(500);
  const mr = page.locator('.modal.show').last();
  const datas = mr.locator('input[bsdatepicker]');
  await datas.nth(0).fill('01/01/2026'); await page.keyboard.press('Escape'); await datas.nth(1).fill('30/09/2026'); await page.keyboard.press('Escape');
  await mr.locator('button:has-text("Buscar"), button:has-text("Pesquisar"), button:has-text("Filtrar")').first().click(); await page.waitForTimeout(2000);
  await page.locator('.modal.show button:has-text("Fechar")').click().catch(() => {}); await page.waitForTimeout(600);
  await shot('32-relatorio-recebimentos-periodo', false);
  await browser.close(); console.log('OK');
})().catch(e => { console.error('FALHA:', e.message.slice(0, 600)); process.exit(1); });
