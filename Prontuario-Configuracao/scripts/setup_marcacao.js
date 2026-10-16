// Prepara (e depois restaura) os dados para as capturas de Marcação do manual "Prontuário - Configuração".
// Uso: node setup_marcacao.js preparar | limpar     (banco local de teste; nunca produção)
// preparar: libera o Prontuário com marcação na clínica 1 (guarda o valor original).
// limpar: apaga o tipo "Anamnese (modelo)" criado pela captura (alíneas, opções e textos) e devolve a liberação.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'localhost';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ESTADO = path.join(__dirname, 'estado_marcacao.json');
const sql = (q) => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();

function preparar() {
  if (fs.existsSync(ESTADO)) throw new Error('Já existe estado_marcacao.json: rode "limpar" antes.');
  const lib = sql(`SELECT CAST(ModProntuarioMarcacao AS VARCHAR) FROM Clinica WHERE IdClinica=1`);
  const maxTipo = sql(`SELECT ISNULL(MAX(IdProntuarioTipo),0) FROM ProntuarioTipo WHERE IdClinica=1`);
  fs.writeFileSync(ESTADO, JSON.stringify({ lib, maxTipo }, null, 2));
  sql(`UPDATE Clinica SET ModProntuarioMarcacao=1 WHERE IdClinica=1`);
  console.log('Preparado (marcação liberada).');
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('Nada a limpar.'); return; }
  const { lib, maxTipo } = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  // filhas primeiro (a tabela de opções antes da de alíneas); todas filtradas pelo tipo criado na captura
  // prontuários de demonstração (criados pela captura do manual de uso) e suas respostas
  try { sql(`DELETE FROM ProntuarioTag WHERE IdProntuario IN (SELECT IdProntuario FROM Prontuario WHERE IdProntuarioTipo>${maxTipo})`); sql(`DELETE FROM ProntuarioAlinea WHERE IdProntuario IN (SELECT IdProntuario FROM Prontuario WHERE IdProntuarioTipo>${maxTipo})`); sql(`DELETE FROM Prontuario WHERE IdProntuarioTipo>${maxTipo}`); } catch (e) { console.log('  aviso prontuarios', e.message.split(String.fromCharCode(10))[0]); }
  const ordem = ['ProntuarioParamTipoAlineaOpcao', 'ProntuarioParamTipoAlinea', 'ProntuarioTextoPadrao', 'ProntuarioModeloDownload', 'ProntuarioDePara'];
  for (const t of ordem) {
    try { sql(`DELETE FROM ${t} WHERE IdProntuarioTipo>${maxTipo}`); } catch (e) { console.log('  aviso', t, e.message.split(String.fromCharCode(10))[0]); }
  }
  sql(`DELETE FROM ProntuarioTipo WHERE IdClinica=1 AND IdProntuarioTipo>${maxTipo}`);
  sql(`UPDATE Clinica SET ModProntuarioMarcacao=${lib} WHERE IdClinica=1`);
  fs.unlinkSync(ESTADO);
  console.log('Restaurado.');
}
const modo = process.argv[2];
if (modo === 'preparar') preparar(); else if (modo === 'limpar') limpar(); else { console.error('Uso: node setup_marcacao.js preparar | limpar'); process.exit(1); }
