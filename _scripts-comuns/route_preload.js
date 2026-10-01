// Uso: node -r route_preload.js script.js  — faz o front (API fixa em 49020) falar com a API isolada de documentação (49041)
const pw = require('C:/Projetos/W_Clinica/FrontClinica/node_modules/playwright');
const rota = (r) => r.continue({ url: r.request().url().replace('localhost:49020', 'localhost:49041') });
const orig = pw.chromium.launch.bind(pw.chromium);
pw.chromium.launch = async (o) => {
  const b = await orig(o);
  const np = b.newPage.bind(b); b.newPage = async (...a) => { const p = await np(...a); await p.route('http://localhost:49020/**', rota); return p; };
  const nc = b.newContext.bind(b); b.newContext = async (...a) => { const c = await nc(...a); await c.route('http://localhost:49020/**', rota); return c; };
  return b;
};
