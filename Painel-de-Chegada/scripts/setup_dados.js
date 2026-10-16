// Prepara (e depois restaura) os dados da documentação "Painel de Chegada (TV)".
// Uso: node setup_dados.js preparar | limpar     (banco local de teste; nunca produção)
// preparar: guarda a configuração do painel da clínica 1 e deixa 1 TV no máximo, 10 min de aviso e 15 s por cartão.
// limpar: devolve a configuração, apaga as TVs e os avisos criados pela captura.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'localhost';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ESTADO = path.join(__dirname, 'output', 'estado_demo.json');
const sql = (q) => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();

function preparar() {
  if (fs.existsSync(ESTADO)) throw new Error('Já existe output/estado_demo.json: rode "limpar" antes.');
  const ultimoAviso = sql(`SELECT ISNULL(MAX(Id),0) FROM PainelChegadaAviso`);
  const ultimaSessao = sql(`SELECT ISNULL(MAX(Id),0) FROM PainelChegadaTvSessao`);
  const cfg = sql(`SELECT CAST(Ativo AS VARCHAR)+'|'+CAST(DuracaoCartaoSegundos AS VARCHAR)+'|'+CAST(MaximoTvs AS VARCHAR)+'|'+CAST(DuracaoAvisoMinutos AS VARCHAR) FROM PainelChegadaConfiguracao WHERE IdClinica=1`);
  fs.writeFileSync(ESTADO, JSON.stringify({ ultimoAviso, ultimaSessao, cfg }, null, 2));
  sql(`UPDATE PainelChegadaConfiguracao SET Ativo=1, DuracaoCartaoSegundos=15, MaximoTvs=1, DuracaoAvisoMinutos=10 WHERE IdClinica=1`);
  console.log('Preparado.');
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('Nada a limpar.'); return; }
  const { ultimoAviso, ultimaSessao, cfg } = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  const [a, c, m, d] = cfg.split('|');
  sql(`DELETE FROM PainelChegadaAvisoEntrega WHERE IdAviso IN (SELECT Id FROM PainelChegadaAviso WHERE Id>${ultimoAviso});
       DELETE FROM PainelChegadaAviso WHERE Id>${ultimoAviso};
       DELETE FROM PainelChegadaTvSessao WHERE Id>${ultimaSessao};
       UPDATE PainelChegadaConfiguracao SET Ativo=${a}, DuracaoCartaoSegundos=${c}, MaximoTvs=${m}, DuracaoAvisoMinutos=${d} WHERE IdClinica=1;`);
  fs.unlinkSync(ESTADO);
  console.log('Restaurado.');
}
const modo = process.argv[2];
if (modo === 'preparar') preparar(); else if (modo === 'limpar') limpar(); else { console.error('Uso: node setup_dados.js preparar | limpar'); process.exit(1); }
