// Capturas extras do vídeo institucional: Nova Agenda (copiar agenda anterior) e Tipos de prontuário.
// Uso: E2E_API_URL=http://localhost:49020/api node capture2.js
// Só abre telas: NÃO salva a nova agenda nem altera dados. Nome da clínica trocado só na imagem.
const { abrir } = require('../../_scripts-comuns/cap_common.js');

const trocarNomes = (page) => page.evaluate(() => {
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n; while ((n = w.nextNode())) {
    const v = n.nodeValue.replace(/Homologa[cç][aã]o/g, 'Clínica Vida Plena').replace('Usuário: ADMIN', 'Usuário: Recepção');
    if (v !== n.nodeValue) n.nodeValue = v;
  }
});

(async () => {
  const { browser, page, ir, shot } = await abrir(__dirname);
  await page.unroute('http://localhost:49020/**').catch(() => {});

  // 15: Nova Agenda com "Copiar agenda anterior" marcada (não salva)
  await ir('/agenda'); await page.waitForTimeout(1500);
  await page.locator('button:has-text("Novo")').first().click();
  await page.waitForTimeout(1500);
  await page.locator('label:has-text("Copiar agenda anterior"), input[type="checkbox"]').first().click().catch(() => {});
  await page.waitForTimeout(1200);
  await trocarNomes(page);
  await shot('15-nova-agenda-copiar-anterior', false);
  console.log('ok 15');

  // 16: tipos de prontuário (Anamnese, Evolução diária...)
  await ir('/prontuario/tipos'); await page.waitForTimeout(3000);
  await trocarNomes(page);
  await page.evaluate(() => document.querySelectorAll('table tbody tr').forEach(tr => { if (tr.cells[0] && tr.cells[0].textContent.trim() === '...') tr.remove(); }));
  await shot('16-prontuario-tipos', false);
  console.log('ok 16 ->', page.url());
  await browser.close();
})().catch((e) => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
