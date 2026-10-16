// Captura das telas novas do manual "Prontuário - Uso" (v1.1): preenchimento e visualização da alínea de Marcação.
// Pré-requisitos: na pasta Prontuario-Configuracao/scripts: node setup_marcacao.js preparar e node capture_marcacao.js
// (cria o tipo "Anamnese (modelo)" com a alínea de Marcação); API em :49041 e front em :4222 (proxy para 49041).
// Usuário profissional de teste (E2E_LOGIN / E2E_SENHA, padrão 55555555555 / Cli55555). Banco local; nunca produção.
// Cria um prontuário de teste no tipo clonado; o "limpar" do setup_marcacao apaga o tipo (e o prontuário precisa ser apagado antes: ver passo final).
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { abrir } = require('../../_scripts-comuns/cap_common.js');

// apaga prontuários de execuções anteriores no tipo clonado (rascunho impede criar outro para o mesmo paciente)
const sql = (q) => execFileSync('sqlcmd', ['-S', 'localhost', '-d', process.env.E2E_SQL_DB || 'a3_cli_hoje', '-E', '-C', '-I', '-f', '65001', '-h', '-1', '-W', '-Q', `SET NOCOUNT ON; ${q}`], { encoding: 'utf8' }).trim();
const TIPO = `(SELECT IdProntuarioTipo FROM ProntuarioTipo WHERE IdClinica=1 AND Prontuario='Anamnese (modelo)')`;
sql(`DELETE FROM ProntuarioTag WHERE IdProntuario IN (SELECT IdProntuario FROM Prontuario WHERE IdProntuarioTipo=${TIPO});
     DELETE FROM ProntuarioAlinea WHERE IdProntuario IN (SELECT IdProntuario FROM Prontuario WHERE IdProntuarioTipo=${TIPO});
     DELETE FROM Prontuario WHERE IdProntuarioTipo=${TIPO};`);

(async () => {
  const { browser, page, ir, shot, chamar } = await abrir(__dirname, { login: process.env.E2E_LOGIN || '55555555555', senha: process.env.E2E_SENHA || 'Cli55555' });
  const valores = {};
  page.on('dialog', (d) => d.accept().catch(() => {}));
  const passo = async (nome, fn) => {
    try { await fn(); console.log('ok  ', nome); }
    catch (e) { console.log('FALHA', nome, '-', e.message.split('\n')[0]); await shot('ZZ-erro-' + nome).catch(() => {}); throw e; }
  };
  const fecharAviso = async () => { const a = page.getByRole('button', { name: /Obrigado/i }); if (await a.count()) await a.first().click(); };
  const pausa = (ms = 500) => page.waitForTimeout(ms);
  const modal = () => page.locator('.modal.show').last();

  await passo('U01-novo', async () => {
    await ir('/prontuario/profissional'); await fecharAviso(); await pausa(2000);
    await modal().locator('select').filter({ has: page.locator('option', { hasText: 'Anamnese (modelo)' }) }).first().selectOption({ label: 'Anamnese (modelo)' }); await pausa(500);
    await modal().getByRole('button', { name: /Pesquisar/ }).click(); await pausa(2000);
    await page.getByRole('button', { name: /Novo/ }).first().click(); await pausa(1500);
    await shot('U01-novo', false);
  });

  await passo('U02-selecionar-paciente', async () => {
    const m = modal();
    await m.getByText(/Listar Pacientes da agenda/).first().click(); await pausa(2500);
    await shot('U02-pacientes-agenda', false);
  });

  await passo('U03-adicionar', async () => {
    const m = modal();
    await m.locator('tr', { hasText: 'Paciente 0002' }).locator('input[type=checkbox]').check(); await pausa(400);
    const esp = m.locator('select').last();
    const opcoes = await esp.locator('option').allInnerTexts(); valores.especialidades = opcoes;
    await esp.selectOption({ index: 1 }); await pausa(500);
    await shot('U03-paciente-selecionado', false);
    await m.getByRole('button', { name: 'Adicionar' }).click(); await pausa(3500);
    await shot('U04-prontuario-novo', false);
  });

  await passo('U05-marcacao', async () => {
    await page.locator('textarea').first().fill('Paciente chegou com a mãe, calmo e colaborativo.'); await pausa(400);
    await page.getByRole('button', { name: 'Salvar', exact: true }).last().click(); await pausa(1800);
    await page.getByRole('button', { name: /Próxima/ }).first().click(); await pausa(1500);
    await shot('U05-marcacao-vazia', false);
    await page.getByText('Com acompanhante', { exact: true }).first().click(); await pausa(300);
    await page.getByText('Outros', { exact: true }).first().click(); await pausa(500);
    await shot('U06-marcacao-outros', false);
  });

  await passo('U07-salvar-finalizar', async () => {
    await page.locator('input[placeholder^="Descreva"]').fill('Indicado pela escola.'); await pausa(300);
    await page.getByRole('button', { name: 'Salvar', exact: true }).last().click(); await pausa(1800);
    valores.toastSalvar = (await page.locator('.toast-message').allInnerTexts()).join(' | ');
    await shot('U07-marcacao-salva', false);
    await page.getByRole('button', { name: /Finalizar/ }).first().click(); await pausa(1200);
    await shot('U08-finalizar-confirmar', false);
    await page.getByRole('button', { name: /^(Sim|Confirmar|Finalizar)$/ }).last().click(); await pausa(3000);
    await shot('U09-finalizado', false);
  });

  fs.writeFileSync(path.join(__dirname, 'output_marcacao.json'), JSON.stringify(valores, null, 2));
  console.log('valores:', JSON.stringify(valores));
  await browser.close();
})().catch((e) => { console.error('ERRO', e.message); process.exit(1); });
