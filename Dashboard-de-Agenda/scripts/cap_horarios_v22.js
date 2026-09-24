// v2.2 (24/09/2026): print 42 com o novo layout da tela Agenda -> Horarios (grade da semana)
const { chromium } = require('playwright');
const API='http://localhost:49020/api', APP='http://localhost:4222';
(async () => {
  const j1 = await (await fetch(`${API}/usuario/login`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({Login:'99999999999',Senha:'Cli99999'})})).json();
  const j2 = await (await fetch(`${API}/clinicausuario/SelecionarClinica`, {method:'POST',headers:{'Content-Type':'application/json',Authorization:`Bearer ${j1.data.token}`},body:JSON.stringify({IdUsuario:j1.data.id,IdClinica:1,IdPerfilEscolha:0})})).json();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
  const hide = () => page.addStyleTag({ content: '#li_testes { display: none !important; }' });
  await page.goto(APP);
  await page.evaluate((a)=>{localStorage.setItem('_clTk',a.token);localStorage.setItem('_clNm',JSON.stringify(a.nome));localStorage.setItem('_clId',JSON.stringify(String(a.id)));localStorage.setItem('_clType',JSON.stringify(a.papel));localStorage.setItem('_clcfAux',JSON.stringify(a.clinicaConfig||[]));
    localStorage.setItem('agendaProfissional.apresentacao.'+a.id,'vista');}, {token:j2.data.token,nome:j2.data.nome,id:j2.data.id,papel:j2.data.papel,clinicaConfig:j2.data.clinicaConfig});
  await page.goto(`${APP}/agenda/profissional?idAgenda=33`);
  await page.waitForLoadState('networkidle'); await hide(); await page.waitForTimeout(800);
  const sel = page.locator('#apnProfissional');
  const alvo = (await sel.locator('option').allTextContents()).find(o => o.trim().startsWith('Profissional 01'));
  await sel.selectOption({ label: alvo }); await page.waitForTimeout(1800); await hide();
  await page.screenshot({ path: 'screenshots/42-prof-horarios.png' });
  await browser.close(); console.log('ok');
})().catch(e=>{console.error(e.message);process.exit(1)});
