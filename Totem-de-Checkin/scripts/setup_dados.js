// Prepara (e depois restaura) os dados da documentação "Totem de Check-in".
// Uso: node setup_dados.js preparar | limpar     (banco local de teste; nunca produção)
// preparar: grava a configuração padrão do totem na clínica 1 e altera o horário 52 (16:30) para
//   perto da hora atual, para o paciente estar dentro da janela do totem.
// limpar: devolve a configuração e o horário 52 originais e apaga as chegadas de demonstração.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'localhost';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ESTADO = path.join(__dirname, 'output', 'estado_demo.json');
const GUID = '3fd44cb5550443c'; // Paciente 0003, sexta, 16:30 (agenda 32)
const sql = (q) => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();

function preparar() {
  if (fs.existsSync(ESTADO)) throw new Error('Já existe output/estado_demo.json: rode "limpar" antes.');
  const cfg = sql(`SELECT CAST(Ativo AS VARCHAR)+'|'+CAST(MinutosAntes AS VARCHAR)+'|'+CAST(MinutosDepois AS VARCHAR) FROM TotemConfiguracao WHERE IdClinica=1`);
  const hora = sql(`SELECT CONVERT(VARCHAR(8), Hora, 108) FROM Hora WHERE IdClinica=1 AND IdHora=52`);
  const agora = new Date(Date.now() + 20 * 60000);
  const m = agora.getMinutes() < 30 ? '00' : '30';
  const hhmm = `${String(agora.getHours()).padStart(2, '0')}:${m}`;
  fs.writeFileSync(ESTADO, JSON.stringify({ cfg, hora, hhmm }, null, 2));
  sql(`UPDATE Hora SET Hora='${hhmm}' WHERE IdClinica=1 AND IdHora=52;
       UPDATE TotemConfiguracao SET Ativo=1, MinutosAntes=60, MinutosDepois=30 WHERE IdClinica=1;`);
  console.log('Preparado. Horário do Paciente 0003 hoje:', hhmm);
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('Nada a limpar.'); return; }
  const { cfg, hora } = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  const [a, b, d] = cfg.split('|');
  sql(`UPDATE Hora SET Hora='${hora}' WHERE IdClinica=1 AND IdHora=52;
       DELETE FROM ChegadaPaciente WHERE IdClinica=1 AND GuidAgendamento='${GUID}';
       UPDATE TotemConfiguracao SET Ativo=${a}, MinutosAntes=${b}, MinutosDepois=${d} WHERE IdClinica=1;`);
  fs.unlinkSync(ESTADO);
  console.log('Restaurado.');
}
const modo = process.argv[2];
if (modo === 'preparar') preparar(); else if (modo === 'limpar') limpar(); else { console.error('Uso: node setup_dados.js preparar | limpar'); process.exit(1); }
