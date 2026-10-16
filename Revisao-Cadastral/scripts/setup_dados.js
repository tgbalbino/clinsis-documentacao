// Prepara (e depois restaura) os dados de demonstração da documentação "Revisão cadastral de pacientes".
// Uso: node setup_dados.js preparar | limpar     (banco local de teste; nunca produção)
// preparar: liga o módulo na clínica 1 e deixa 4 pacientes com situações diferentes (guarda os valores originais em output/estado_demo.json).
// limpar: devolve os valores originais e desliga o módulo.
// Variáveis: E2E_SQL_SERVER / E2E_SQL_DB (default localhost / a3_cli_hoje)
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const SQL_SERVER = process.env.E2E_SQL_SERVER || 'localhost';
const SQL_DB = process.env.E2E_SQL_DB || 'a3_cli_hoje';
const ID_CLINICA = 1;
const ESTADO = path.join(__dirname, 'output', 'estado_demo.json');

const sql = (q) => execFileSync('sqlcmd', ['-S', SQL_SERVER, '-d', SQL_DB, '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();

// Pacientes de teste e o que cada um demonstra
const PACIENTES = {
  vencido: 20,    // agenda toda sexta 16:30: revisão vencida (aparece na agenda e no check-in)
  endereco: 28,   // endereço incompleto (sem bairro)
  contato: 26,    // sem celular, telefone e e-mail
  vencido2: 23    // segundo paciente com revisão vencida
};

function preparar() {
  if (fs.existsSync(ESTADO)) throw new Error('Já existe output/estado_demo.json: rode "limpar" antes de preparar de novo.');
  const ids = Object.values(PACIENTES).join(',');
  const linhas = sql(`SELECT CONVERT(VARCHAR(30), ISNULL(DataRevisaoCadastro,'1900-01-01'), 121), IdUsuarioRevisaoCadastro, ISNULL(Bairro,''), ISNULL(Celular,''), ISNULL(Telefone,''), ISNULL(Email,''), IdPessoa
                      FROM Pessoa WHERE IdClinica=${ID_CLINICA} AND IdPessoa IN (${ids})`);
  const originais = {};
  // sqlcmd separa colunas por espaço com -W; usa um SELECT por campo para não depender do separador
  for (const id of Object.values(PACIENTES)) {
    const q = (c) => sql(`SELECT ISNULL(CAST(${c} AS NVARCHAR(100)),'<<NULL>>') FROM Pessoa WHERE IdClinica=${ID_CLINICA} AND IdPessoa=${id}`);
    originais[id] = {
      DataRevisaoCadastro: sql(`SELECT ISNULL(CONVERT(VARCHAR(30), DataRevisaoCadastro, 121),'<<NULL>>') FROM Pessoa WHERE IdClinica=${ID_CLINICA} AND IdPessoa=${id}`),
      IdUsuarioRevisaoCadastro: q('IdUsuarioRevisaoCadastro'), Bairro: q('Bairro'), Celular: q('Celular'), Telefone: q('Telefone'), Email: q('Email')
    };
  }
  const modulo = sql(`SELECT CAST(ModRevisaoCadastral AS VARCHAR) FROM Clinica WHERE IdClinica=${ID_CLINICA}`);
  const parametro = sql(`SELECT ISNULL(Valor,'<<NULL>>') FROM Parametro WHERE IdClinica=${ID_CLINICA} AND Nome='RevisaoCadastralDias'`);
  fs.writeFileSync(ESTADO, JSON.stringify({ originais, modulo, parametro, pacientes: PACIENTES }, null, 2));

  sql(`UPDATE Clinica SET ModRevisaoCadastral=1 WHERE IdClinica=${ID_CLINICA};
       UPDATE Parametro SET Valor='365' WHERE IdClinica=${ID_CLINICA} AND Nome='RevisaoCadastralDias';
       UPDATE Pessoa SET DataRevisaoCadastro=DATEADD(DAY,-420,GETDATE()), IdUsuarioRevisaoCadastro=NULL WHERE IdClinica=${ID_CLINICA} AND IdPessoa=${PACIENTES.vencido};
       UPDATE Pessoa SET DataRevisaoCadastro=DATEADD(DAY,-30,GETDATE()), Bairro='' WHERE IdClinica=${ID_CLINICA} AND IdPessoa=${PACIENTES.endereco};
       UPDATE Pessoa SET DataRevisaoCadastro=DATEADD(DAY,-10,GETDATE()), Celular='', Telefone='', Email='' WHERE IdClinica=${ID_CLINICA} AND IdPessoa=${PACIENTES.contato};
       UPDATE Pessoa SET DataRevisaoCadastro=DATEADD(DAY,-700,GETDATE()), IdUsuarioRevisaoCadastro=NULL WHERE IdClinica=${ID_CLINICA} AND IdPessoa=${PACIENTES.vencido2};`);
  console.log('Dados de demonstração preparados:', JSON.stringify(PACIENTES));
}

function limpar() {
  if (!fs.existsSync(ESTADO)) { console.log('Nada a limpar.'); return; }
  const { originais, modulo, parametro } = JSON.parse(fs.readFileSync(ESTADO, 'utf8'));
  const lit = (v) => (v === '<<NULL>>' ? 'NULL' : `N'${String(v).replace(/'/g, "''")}'`);
  for (const [id, o] of Object.entries(originais)) {
    sql(`UPDATE Pessoa SET DataRevisaoCadastro=${o.DataRevisaoCadastro === '<<NULL>>' ? 'NULL' : `CONVERT(DATETIME, '${o.DataRevisaoCadastro}', 121)`},
         IdUsuarioRevisaoCadastro=${o.IdUsuarioRevisaoCadastro === '<<NULL>>' ? 'NULL' : o.IdUsuarioRevisaoCadastro},
         Bairro=${lit(o.Bairro)}, Celular=${lit(o.Celular)}, Telefone=${lit(o.Telefone)}, Email=${lit(o.Email)}
         WHERE IdClinica=${ID_CLINICA} AND IdPessoa=${id}`);
  }
  sql(`UPDATE Clinica SET ModRevisaoCadastral=${modulo} WHERE IdClinica=${ID_CLINICA};
       ${parametro === '<<NULL>>' ? '' : `UPDATE Parametro SET Valor='${parametro}' WHERE IdClinica=${ID_CLINICA} AND Nome='RevisaoCadastralDias';`}`);
  fs.unlinkSync(ESTADO);
  console.log('Dados de demonstração restaurados.');
}

const modo = process.argv[2];
if (modo === 'preparar') preparar();
else if (modo === 'limpar') limpar();
else { console.error('Uso: node setup_dados.js preparar | limpar'); process.exit(1); }
