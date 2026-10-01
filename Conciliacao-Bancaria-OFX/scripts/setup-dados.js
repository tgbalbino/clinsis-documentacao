// Prepara os movimentos da conta BANCO BRASIL (id 9) para a demonstração da conciliação OFX.
const { loginApi, API } = require('../../_scripts-comuns/cap_common.js');
(async () => {
  const a = await loginApi(); const h = { 'Content-Type': 'application/json', Authorization: 'Bearer ' + a.token };
  const post = async (r, b) => (await fetch(API + '/' + r, { method: 'POST', headers: h, body: JSON.stringify(b) })).json();
  const novos = [
    [1, 220, '2026-09-21', 'Recebimento consulta Ana Paula', 2, 2],
    [1, 350, '2026-09-22', 'Recebimento consulta Maria Souza', 2, 2],
    [1, 180, '2026-09-23', 'Recebimento sessão João Lima', 2, 2],
    [2, 1200, '2026-09-24', 'Aluguel da sala - setembro', 8, 4],
    [2, 89.9, '2026-09-25', 'Material de escritório - papelaria', 12, 4],
    [2, 60, '2026-09-26', 'Lanche da equipe', 12, 4],
  ];
  const ids = [];
  for (const [t, v, d, hist, pc, cc] of novos) {
    const r = await post('movimentofinanceiro', { idContaFinanceira: 9, tipoMovimento: t, valor: v, dataMovimento: d + 'T00:00:00', historico: hist, idPlanoConta: pc, idCentroCusto: cc });
    ids.push((r.data ?? r).idMovimentoFinanceiro);
  }
  console.log('criados', ids);
  // a 1ª linha do extrato (Ana Paula, 21/09) já fica conciliada para mostrar a situação "Já conciliado"
  const c = await post('movimentofinanceiro/conciliacao/ofx/conciliar', { idContaFinanceira: 9, pares: [{ idMovimentoFinanceiro: ids[0], fitId: '20260921001' }] });
  console.log('conciliado', JSON.stringify(c).slice(0, 200));
})();
