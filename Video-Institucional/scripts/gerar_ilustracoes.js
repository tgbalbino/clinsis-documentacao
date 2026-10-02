// Gera as ilustrações do vídeo institucional (SVG -> PNG 1600x900), sem rostos realistas.
// Uso: node gerar_ilustracoes.js   (saída em ilustracoes/)
const path = require('path');
const fs = require('fs');
const { chromium } = require('C:/Projetos/W_Clinica/FrontClinica/node_modules/playwright');
const LOGO = 'data:image/png;base64,' + fs.readFileSync('C:/Projetos/W_Clinica/Documentacao-Entrega/_scripts-comuns/pipeline-video/marca/logo_horizontal_branco.png').toString('base64');
const F = "font-family:'Segoe UI',Arial,sans-serif";

// pessoa estilizada (sem traços de rosto, só um sorriso quando indicado)
const pessoa = (x, y, { pele, cabelo, roupa, sorriso = false, esc = 1, cabeloLongo = false }) => `
<g transform="translate(${x},${y}) scale(${esc})">
  <rect x="-70" y="60" width="140" height="170" rx="46" fill="${roupa}"/>
  <rect x="-16" y="40" width="32" height="30" rx="12" fill="${pele}"/>
  ${cabeloLongo ? `<rect x="-52" y="-48" width="104" height="120" rx="48" fill="${cabelo}"/>` : ''}
  <circle cx="0" cy="0" r="46" fill="${pele}"/>
  <path d="M-48 -6 Q-40 -58 0 -58 Q42 -58 48 -6 Q20 -30 -48 -6Z" fill="${cabelo}"/>
  ${sorriso ? `<path d="M-14 14 Q0 28 14 14" stroke="#7a3b2e" stroke-width="5" fill="none" stroke-linecap="round"/>` : ''}
</g>`;

const linhas = (n, x1, x2, y0, passo, cor, larg) =>
  Array.from({ length: n }, (_, i) => `<line x1="${x1}" y1="${y0 + i * passo}" x2="${x2}" y2="${y0 + i * passo}" stroke="${cor}" stroke-width="${larg}"/>`).join('');

const cartoes02 = [
  { x: 130, titulo: 'Faltas', sub: 'horários perdidos', cor: '#e57373', icone: `
    <rect x="70" y="70" width="190" height="170" rx="14" fill="#fff"/><rect x="70" y="70" width="190" height="40" rx="14" fill="#e57373"/>
    ${[0, 1, 2].map(r => [0, 1, 2].map(c => `<rect x="${88 + c * 56}" y="${126 + r * 36}" width="42" height="26" rx="5" fill="${(r * 3 + c) % 4 === 1 ? '#ffd0d0' : '#e6eef5'}"/>`).join('')).join('')}
    <path d="M200 150 L238 188 M238 150 L200 188" stroke="#c62828" stroke-width="10" stroke-linecap="round"/>` },
  { x: 590, titulo: 'Planilhas paralelas', sub: 'chance de erro', cor: '#f0b35a', icone: `
    <rect x="60" y="80" width="150" height="150" rx="10" fill="#fff"/><rect x="100" y="60" width="150" height="150" rx="10" fill="#f6fbf6" stroke="#9ccc9c" stroke-width="5"/>
    ${linhas(4, 100, 250, 95, 30, '#bcd9bc', 4)}
    ${[0, 1, 2].map(i => `<line x1="${135 + i * 38}" y1="60" x2="${135 + i * 38}" y2="210" stroke="#bcd9bc" stroke-width="4"/>`).join('')}
    <text x="205" y="200" font-size="80" font-weight="800" fill="#e08a00" style="${F}">?</text>` },
  { x: 1050, titulo: 'Resultado no escuro', sub: 'sem visão do mês', cor: '#7aa7c7', icone: `
    <rect x="60" y="70" width="190" height="170" rx="14" fill="#fff"/>
    <rect x="90" y="170" width="28" height="50" fill="#b8cfe0"/><rect x="132" y="140" width="28" height="80" fill="#b8cfe0"/><rect x="174" y="110" width="28" height="110" fill="#b8cfe0"/>
    <path d="M80 190 Q130 120 230 100" stroke="#5285ad" stroke-width="6" fill="none" stroke-dasharray="14 12" stroke-linecap="round"/>
    <text x="210" y="95" font-size="70" font-weight="800" fill="#5285ad" style="${F}">?</text>` }
];

const barras = [30, 50, 40, 70, 60, 85];

const cena = {
  '01-recepcao-segunda-feira': `
  <rect width="1600" height="900" fill="#efe6d8"/>
  <rect y="640" width="1600" height="260" fill="#d8cdbd"/>
  <g><rect x="90" y="90" width="220" height="150" rx="10" fill="#fff" stroke="#c9bba5" stroke-width="6"/>
     <circle cx="200" cy="165" r="52" fill="#fff" stroke="#8a7a62" stroke-width="6"/>
     <path d="M200 165 L200 128 M200 165 L228 180" stroke="#8a7a62" stroke-width="7" stroke-linecap="round"/></g>
  <rect x="120" y="560" width="1360" height="60" rx="14" fill="#8f6b4a"/>
  <rect x="140" y="620" width="1320" height="280" fill="#a37b57"/>
  <g transform="rotate(-6 560 470)"><rect x="380" y="380" width="360" height="190" rx="8" fill="#fffdf6" stroke="#b9ab92" stroke-width="5"/>
    ${linhas(6, 400, 720, 410, 28, '#d7cfbd', 3)}
    <path d="M410 425 L690 430 M415 470 L650 462 M420 500 Q470 480 520 505 T640 500" stroke="#c0392b" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M440 535 L520 535" stroke="#2c3e50" stroke-width="5" stroke-linecap="round"/></g>
  <rect x="800" y="420" width="90" height="90" fill="#ffe27a" transform="rotate(5 845 465)"/>
  <rect x="905" y="440" width="90" height="90" fill="#ffb3b3" transform="rotate(-7 950 485)"/>
  <rect x="1010" y="410" width="90" height="90" fill="#b7e4c7" transform="rotate(4 1055 455)"/>
  <text x="845" y="475" text-anchor="middle" font-size="40" font-weight="800" fill="#8a5a3c" style="${F}" transform="rotate(5 845 465)">?</text>
  <text x="950" y="495" text-anchor="middle" font-size="40" font-weight="800" fill="#b03a3a" style="${F}" transform="rotate(-7 950 485)">!</text>
  <g transform="translate(1250,470)"><rect x="-90" y="20" width="180" height="80" rx="20" fill="#34495e"/>
    <rect x="-110" y="-12" width="220" height="42" rx="21" fill="#2c3e50"/>
    <path d="M-150 -40 Q-170 -10 -150 20 M-185 -60 Q-220 -10 -185 40" stroke="#e67e22" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M150 -40 Q170 -10 150 20 M185 -60 Q220 -10 185 40" stroke="#e67e22" stroke-width="8" fill="none" stroke-linecap="round"/></g>
  ${pessoa(1040, 300, { pele: '#e0ac8b', cabelo: '#3b2a20', roupa: '#5285ad', cabeloLongo: true })}
  <text x="800" y="840" text-anchor="middle" font-size="46" font-weight="700" fill="#5a4630" style="${F}">Segunda-feira, 7h40</text>`,

  '02-custo-da-desorganizacao': `
  <rect width="1600" height="900" fill="#14263a"/>
  <text x="800" y="120" text-anchor="middle" font-size="52" font-weight="700" fill="#e8eef3" style="${F}">Quando a rotina não se organiza</text>
  ${cartoes02.map(c => `<g transform="translate(${c.x},230)"><rect width="380" height="440" rx="26" fill="#1d3550" stroke="${c.cor}" stroke-width="4"/>
      <g transform="translate(30,20)">${c.icone}</g>
      <text x="190" y="340" text-anchor="middle" font-size="36" font-weight="700" fill="#fff" style="${F}">${c.titulo}</text>
      <text x="190" y="388" text-anchor="middle" font-size="26" fill="${c.cor}" style="${F}">${c.sub}</text></g>`).join('')}
  <text x="800" y="800" text-anchor="middle" font-size="34" fill="#9fb4c6" style="${F}">No fim do mês, ninguém sabe ao certo como a clínica ou o consultório foi.</text>`,

  '05-clinica-organizada': `
  <rect width="1600" height="900" fill="#e8f3f1"/>
  <rect y="650" width="1600" height="250" fill="#cfe5e1"/>
  <circle cx="1440" cy="190" r="110" fill="#fff6d6" opacity="0.9"/>
  <rect x="80" y="590" width="1440" height="60" rx="14" fill="#7aa7a0"/>
  <rect x="100" y="650" width="1400" height="250" fill="#8fb8b1"/>
  <g transform="translate(250,270) scale(0.93)"><rect width="560" height="330" rx="18" fill="#0d1b2a"/><rect x="14" y="14" width="532" height="302" rx="10" fill="#fff"/>
    <rect x="14" y="14" width="532" height="46" rx="10" fill="#137a72"/><text x="40" y="46" font-size="26" font-weight="700" fill="#fff" style="${F}">Agenda do dia</text>
    ${[0, 1, 2, 3].map(i => `<rect x="34" y="${78 + i * 58}" width="492" height="46" rx="10" fill="#eef6f5"/><circle cx="62" cy="${101 + i * 58}" r="14" fill="#2a9d8f"/><path d="M55 ${101 + i * 58} l6 7 l10 -13" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><rect x="92" y="${92 + i * 58}" width="${230 - i * 20}" height="12" rx="6" fill="#b9d3cf"/><rect x="92" y="${110 + i * 58}" width="${150 - i * 10}" height="10" rx="5" fill="#d5e6e3"/><rect x="430" y="${90 + i * 58}" width="80" height="24" rx="12" fill="#c8ece5"/>`).join('')}
  </g>
  <g transform="translate(830,310) scale(0.92)"><rect width="520" height="280" rx="18" fill="#0d1b2a"/><rect x="14" y="14" width="492" height="252" rx="10" fill="#f7fafc"/>
    <rect x="34" y="34" width="140" height="70" rx="10" fill="#e4f1ef"/><rect x="190" y="34" width="140" height="70" rx="10" fill="#e4eef7"/><rect x="346" y="34" width="140" height="70" rx="10" fill="#fdf0dc"/>
    <rect x="34" y="124" width="452" height="124" rx="10" fill="#fff" stroke="#e1e8ee" stroke-width="3"/>
    ${barras.map((h, i) => `<rect x="${64 + i * 68}" y="${220 - h}" width="40" height="${h}" rx="6" fill="#137a72" opacity="0.85"/>`).join('')}
    <path d="M70 200 L130 175 L200 185 L270 150 L340 160 L420 135" stroke="#5285ad" stroke-width="5" fill="none" stroke-linecap="round"/></g>
  ${pessoa(135, 200, { pele: '#e0ac8b', cabelo: '#3b2a20', roupa: '#137a72', cabeloLongo: true, sorriso: true, esc: 0.9 })}
  ${pessoa(1455, 200, { pele: '#c68e6a', cabelo: '#2a2a2a', roupa: '#34495e', sorriso: true, esc: 0.9 })}
  <text x="800" y="840" text-anchor="middle" font-size="50" font-weight="700" fill="#0d4a44" style="${F}">Menos burocracia. Mais tempo para cuidar.</text>`
};

const finalHtml = `<div style="width:1600px;height:900px;background:linear-gradient(180deg,#0d1b2a,#172f44);display:flex;flex-direction:column;align-items:center;justify-content:center;${F};color:#fff">
  <img src="${LOGO}" style="width:760px">
  <div style="font-size:46px;margin-top:50px;font-weight:600">Gestão para clínicas e consultórios</div>
  <div style="font-size:40px;margin-top:36px;color:#7fd1c8;font-weight:600">www.clinsis.com.br/sobre</div></div>`;

(async () => {
  const out = path.join(__dirname, 'ilustracoes');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
  const render = async (nome, html) => {
    await page.setContent(`<html><body style="margin:0">${html}</body></html>`);
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(out, nome + '.png') });
    console.log('ok', nome);
  };
  for (const [nome, svg] of Object.entries(cena))
    await render(nome, `<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">${svg}</svg>`);
  await render('06-tela-final-clinsis', finalHtml);
  await browser.close();
})().catch(e => { console.error('FALHA', e.message); process.exit(1); });
