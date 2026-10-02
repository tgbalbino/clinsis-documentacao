// Capturas do vídeo institucional (clínica 1 = demonstração, API local em 49020, front em 4222).
// Uso: E2E_API_URL=http://localhost:49020/api node capture.js <token-da-confirmacao>
// Só lê telas. Para a LGPD, nomes de pacientes e o nome da clínica são trocados por nomes
// FICTÍCIOS apenas na imagem (DOM), sem alterar o banco.
const path = require('path');
const { abrir, APP } = require('../../_scripts-comuns/cap_common.js');

const NOMES_FICTICIOS = ['Marina Oliveira', 'Carlos Nogueira', 'Fernanda Rocha', 'Rafael Castro', 'Beatriz Lima', 'Paulo Andrade',
  'Camila Souza', 'Renato Vieira', 'Julia Mendes', 'Tiago Ribeiro', 'Larissa Costa', 'Bruno Teixeira'];
const SUBSTITUICOES_FIXAS = { 'Homologação': 'Clínica Vida Plena', 'Homologacao': 'Clínica Vida Plena', 'Usuário: ADMIN': 'Usuário: Recepção' };

// Troca nomes no DOM: nomes de pessoas (1ª coluna de tabelas e textos conhecidos) e o nome da clínica.
const mascarar = (page, nomesReais = [], primeiraColuna = false) => page.evaluate(({ fixas, ficticios, reais, colunaNomes }) => {
  const mapa = new Map(Object.entries(fixas));
  reais.forEach((n, i) => mapa.set(n, ficticios[i % ficticios.length]));
  // 1ª coluna das tabelas: cada nome distinto vira um nome fictício (exceto "Paciente 0007" e similares)
  const vistos = new Map();
  if (colunaNomes) document.querySelectorAll('table tbody tr td:first-child').forEach((td) => {
    const t = td.textContent.trim();
    if (!t || /^paciente\s*\d+$/i.test(t) || /\d/.test(t.slice(0, 3))) return;
    if (!vistos.has(t)) vistos.set(t, ficticios[vistos.size % ficticios.length]);
    mapa.set(t, vistos.get(t));
  });
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n; while ((n = w.nextNode())) {
    let v = n.nodeValue;
    mapa.forEach((novo, velho) => { if (v.includes(velho)) v = v.split(velho).join(novo); });
    v = v.replace(/\(\d{2}\) \d \d{4}-\d{4}/g, '(11) 9 9999-0000');
    if (v !== n.nodeValue) n.nodeValue = v;
  }
}, { fixas: SUBSTITUICOES_FIXAS, ficticios: NOMES_FICTICIOS, reais: nomesReais, colunaNomes: primeiraColuna });

(async () => {
  const token = process.argv[2];
  const { browser, page, ir, shot } = await abrir(__dirname);
  // a API é a própria do VS (49020): desfaz o redirecionamento para a API isolada de documentação
  await page.unroute('http://localhost:49020/**').catch(() => {});

  // 10: link do paciente em celular (sem login)
  const ctx = await browser.newContext({ viewport: { width: 420, height: 860 }, deviceScaleFactor: 2 });
  const cel = await ctx.newPage();
  await cel.route('http://localhost:49020/**', (r) => r.continue());
  await cel.goto(`${APP}/externo/confirmar-agendamentos?t=${token}`);
  await cel.waitForLoadState('networkidle');
  await cel.waitForSelector('.confirmacao-card, .agendamento', { timeout: 20000 });
  await cel.waitForTimeout(800);
  await mascarar(cel, ['Ana Luísa da Silva']);
  await cel.screenshot({ path: path.join(__dirname, 'screenshots', '10-confirmacao-paciente-celular.png') });
  await ctx.close();

  // 11: agenda do mês atual (abre pelo "Acessar" da 1ª linha)
  await ir('/agenda'); await page.waitForTimeout(1500);
  await page.locator('button:has-text("Acessar"), a:has-text("Acessar")').first().click();
  await page.waitForLoadState('networkidle'); await page.waitForTimeout(3500);
  await mascarar(page, ['Ana Luísa da Silva', 'Daniel Silva da Conceicao Pessanha', 'Bob Singer', 'Uelitu', 'Jack Bauer']);
  await shot('11-agenda-do-dia', false);
  console.log('ok 11 ->', page.url());

  // 12: contas a receber (cobranças e recebimentos)
  await ir('/financeiro/contareceber'); await page.waitForTimeout(3000);
  await mascarar(page, [], true);
  await shot('12-contas-a-receber', false);
  console.log('ok 12');

  // 13: dashboard financeiro de setembro (mês com movimento)
  await ir('/financeiro/dashboard'); await page.waitForTimeout(1500);
  await page.locator('input:visible').nth(0).fill('01/09/2026');
  await page.locator('input:visible').nth(1).fill('30/09/2026');
  await page.locator('button:has-text("Buscar")').first().click();
  await page.waitForTimeout(3500);
  await page.waitForTimeout(500);
  await mascarar(page, ['Daniel Silva da Conceicao Pessanha', 'Ana Luísa da Silva']);
  await shot('13-financeiro-dashboard', false);
  console.log('ok 13');

  // 14: dashboard da agenda
  await ir('/agenda/dashboard'); await page.waitForTimeout(3500);
  await mascarar(page, ['Daniel Silva da Conceicao Pessanha', 'Ana Luísa da Silva']);
  await shot('14-dashboard', false);
  console.log('ok 14');
  await browser.close();
  console.log('OK');
})().catch((e) => { console.error('FALHA:', e.message.slice(0, 400)); process.exit(1); });
