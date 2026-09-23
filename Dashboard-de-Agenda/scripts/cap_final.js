const { chromium } = require('playwright');
const API='http://localhost:49020/api', APP='http://localhost:4222';
(async () => {
  const r1 = await fetch(`${API}/usuario/login`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({Login:'99999999999',Senha:'Cli99999'})});
  const j1 = await r1.json();
  const r2 = await fetch(`${API}/clinicausuario/SelecionarClinica`, {method:'POST',headers:{'Content-Type':'application/json',Authorization:`Bearer ${j1.data.token}`},body:JSON.stringify({IdUsuario:j1.data.id,IdClinica:1,IdPerfilEscolha:0})});
  const j2 = await r2.json();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1100 } });
  const hide = () => page.addStyleTag({ content: '#li_testes { display: none !important; }' });
  await page.goto(APP);
  await page.evaluate((a)=>{localStorage.setItem('_clTk',a.token);localStorage.setItem('_clNm',JSON.stringify(a.nome));localStorage.setItem('_clId',JSON.stringify(String(a.id)));localStorage.setItem('_clType',JSON.stringify(a.papel));localStorage.setItem('_clcfAux',JSON.stringify(a.clinicaConfig||[]));}, {token:j2.data.token,nome:j2.data.nome,id:j2.data.id,papel:j2.data.papel,clinicaConfig:j2.data.clinicaConfig});
  // Dashboard mes de Setembro (numeros usados como exemplo de conferencia)
  await page.goto(`${APP}/agenda/dashboard`);
  await page.waitForLoadState('networkidle'); await hide(); await page.waitForTimeout(500);
  await page.locator('input[bsdatepicker]').first().fill('01/09/2026'); await page.keyboard.press('Escape');
  await page.locator('input[bsdatepicker]').nth(1).fill('30/09/2026'); await page.keyboard.press('Escape');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(2500); await hide();
  await page.screenshot({ path: 'screenshots/40-dashboard-setembro-cards.png', clip: { x: 0, y: 0, width: 1600, height: 430 } });
  // Dashboard Jan-Set (faturamento corrigido)
  await page.locator('input[bsdatepicker]').first().fill('01/01/2026'); await page.keyboard.press('Escape');
  await page.click('button:has-text("Buscar")'); await page.waitForTimeout(2500); await hide();
  await page.screenshot({ path: 'screenshots/41-dashboard-janset-full.png', fullPage: true });
  // Prof. horarios
  await page.goto(`${APP}/agenda/profissional?idAgenda=33`);
  await page.waitForLoadState('networkidle'); await hide(); await page.waitForTimeout(800);
  const sel = page.locator('select:visible').first();
  const opts = await sel.locator('option').all();
  for (const o of opts) { if ((await o.textContent()||'').includes('Profissional 01')) { await sel.selectOption(await o.getAttribute('value')); break; } }
  await page.waitForTimeout(1500); await hide();
  await page.screenshot({ path: 'screenshots/42-prof-horarios.png', fullPage: true });
  await browser.close();
  console.log('ok');
})().catch(e=>{console.error(e.message);process.exit(1)});
