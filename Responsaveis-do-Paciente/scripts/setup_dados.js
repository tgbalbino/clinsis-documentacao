// Prepara (e depois restaura) os dados da documentação "Responsáveis do Paciente".
// Uso: node setup_dados.js preparar | limpar     (banco local de teste; nunca produção)
// preparar: liga "Exigir responsável para menor de 18 anos" na clínica 1 (guarda o valor original).
// limpar: devolve a opção e os dados do Paciente 33 e apaga o responsável criado pela captura (CPF 52998224725) e o vínculo com o Paciente 18.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'localhost';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ESTADO = path.join(__dirname, 'output', 'estado_demo.json');
const CPF = '52998224725';
const sql = (q) => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();

function preparar() {
  if (fs.existsSync(ESTADO)) throw new Error('Já existe output/estado_demo.json: rode "limpar" antes.');
  const exige = sql(`SELECT CAST(ExigeResponsavelMenor18 AS VARCHAR) FROM Clinica WHERE IdClinica=1`);
  const q = (c) => sql(`SELECT ISNULL(CONVERT(NVARCHAR(40), ${c}, 121),'<<NULL>>') FROM Pessoa WHERE IdClinica=1 AND IdPessoa=33`);
  const p33 = { cpf: q('CPF_CNPJ'), celular: q('Celular'), revisao: q('DataRevisaoCadastro') };
  fs.writeFileSync(ESTADO, JSON.stringify({ exige, p33 }, null, 2));
  // Paciente 33 (menor, 2015): sem aviso de revisão cadastral na tela
  sql(`UPDATE Clinica SET ExigeResponsavelMenor18=1 WHERE IdClinica=1;
       UPDATE Pessoa SET DataRevisaoCadastro=GETDATE() WHERE IdClinica=1 AND IdPessoa=33;`);
  console.log('Preparado (exigência ligada).');
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('Nada a limpar.'); return; }
  const { exige, p33 } = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  const lit = (v) => (v === '<<NULL>>' ? 'NULL' : `'${v}'`);
  sql(`DELETE FROM PessoaPacienteResponsavel WHERE IdClinica=1 AND IdPessoaResponsavel IN (SELECT IdPessoa FROM Pessoa WHERE IdClinica=1 AND CPF_CNPJ='${CPF}' AND EhResponsavel=1);
       DELETE FROM Pessoa WHERE IdClinica=1 AND CPF_CNPJ='${CPF}' AND EhResponsavel=1;
       UPDATE Pessoa SET DataRevisaoCadastro=${lit(p33.revisao)} WHERE IdClinica=1 AND IdPessoa=33;
       UPDATE Clinica SET ExigeResponsavelMenor18=${exige} WHERE IdClinica=1;`);
  fs.unlinkSync(ESTADO);
  console.log('Restaurado.');
}
const modo = process.argv[2];
if (modo === 'preparar') preparar(); else if (modo === 'limpar') limpar(); else { console.error('Uso: node setup_dados.js preparar | limpar'); process.exit(1); }
