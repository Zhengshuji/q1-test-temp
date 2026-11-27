"""regress_bezout.py —— 用专家的 $(*)$ 判据做**全回归**

对一组已知/可判的（实例，阶）对，逐图卡跑 $(*)$ 判据：

* 理想 $(C_1,\\dots,C_k)=(1)$ ⟹ `INFEASIBLE`（证书）；
* 否则解该理想，取有理/实候选 $\\theta$，代入构造 $\\mathcal L$，
  通过 $(5a)$ + $(5b)$ + 七条一致性检查 ⟹ `FEASIBLE`（见证）；
* 图卡秩不恒定或候选非有理 ⟹ `UNKNOWN`（说明原因）。

用法：python -u tools/verification/regress_bezout.py
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import consistency_checks as CC           # noqa: E402
import bezout_rank_test as BR             # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def try_candidates(A, C, L0, q, rows, gens, tam):
    """由理想 $I=(C_j)$ 解出候选 $\\theta$，逐个代入验证。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    nv = d * (k - d)
    sols = []
    if len(gens) == 1:
        try:
            for r0 in sp.roots(sp.Poly(gens[0], tam[0])):
                sols.append([r0] * nv)
        except Exception:                          # noqa: BLE001
            pass
    else:
        try:
            for sol in sp.solve(gens, tam, dict=True):
                if len(sol) == len(tam):
                    sols.append([sol[s] for s in tam])
        except Exception:                          # noqa: BLE001
            pass
    for vals in sols:
        if any(not sp.simplify(v).is_rational for v in vals):
            continue
        th = [F(int(sp.Rational(v).p), int(sp.Rational(v).q)) for v in vals]
        Z = DS.Z_from_theta(A, C, L0, q, rows, th)
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Z, q)
        if L is None or not LQ.condA(A, C, L):
            continue
        if TC.analyse(A, C, L)['five_b']:
            CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={th}', verbose=False)
            return L, th
    return None, None


def decide(A, C, L0, q, verbose=False):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'UNKNOWN', 'd 越界', None
    verdicts = []
    for rows in itertools.combinations(range(k), d):
        mins, D, tam, lam = BR.build_minors(A, C, L0, q, rows)
        if not mins or D == 0 or not tam:
            verdicts.append(('unknown', rows, '退化/常数图卡'))
            continue
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
        size = len(V[0]) + d
        if not BR.rank_is_constant(A, C, L0, q, rows, size):
            verdicts.append(('unknown', rows, 'rank[V|Z] 不恒定（需按秩析取）'))
            continue
        if len(mins) * D > 48:
            verdicts.append(('unknown', rows, f'超预算（子式 {len(mins)}×D {D}；左零空间符号计算过慢）'))
            continue
        M, e0 = BR.coefficient_matrix(mins, D, tam, lam)
        Cs = BR.left_null_Cs(M, tam, e0)
        if not Cs:
            verdicts.append(('feasible?', rows, '左零空间为空 ⟹ 处处可行（需见证核验）'))
            L, th = DS.try_witness(A, C, L0, q, rows, None)
            if L is not None:
                return 'FEASIBLE', f'图卡 {rows}（左零空），θ={th}', L
            continue
        try:
            G = sp.groebner(Cs, *tam, order='grevlex')
            gens = list(G.exprs)
        except Exception as e:                      # noqa: BLE001
            verdicts.append(('unknown', rows, f'Gröbner 失败：{e}'))
            continue
        if gens == [sp.Integer(1)]:
            verdicts.append(('infeasible', rows, '理想 =(1)'))
            continue
        if verbose:
            print(f'    图卡 {rows}: 理想非 (1) = {gens}')
        L, th = try_candidates(A, C, L0, q, rows, gens, tam)
        if L is not None:
            return 'FEASIBLE', f'图卡 {rows}，θ={th}（理想解 + 七条检查）', L
        verdicts.append(('unknown', rows, f'理想非 (1) 但解不出有理/实见证（{gens}）'))
    if verdicts and all(v[0] == 'infeasible' for v in verdicts):
        return 'INFEASIBLE', '所有图卡理想 =(1)', None
    return 'UNKNOWN', '；'.join(f'{v[1]}:{v[2]}' for v in verdicts), None


def main():
    import importlib.util as iu
    print('=== $(*)$ 判据的全回归 ===')
    cases = []
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, cands4 = V4.build()
    cases.append(('C4 q0', A4, C4m, L04, q04))
    cases.append(('C4 q0+1', A4, C4m, L04, q04 + 1))
    spec2 = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m2 = iu.module_from_spec(spec2)
    spec2.loader.exec_module(m2)
    # 公开例子 q=4 已由**整数障碍**（$h=q+r_1=8$）排除，q=5 已由见证排除；
    # 其图卡的 $(*)$ 判据需 $8\\times224$ 的左零空间，当前实现超预算（见 docs/08 §4.7b 注）。
    cases.append(('公开例子 q=2', m2.A, m2.C, m2.L0, 2))
    for (n, p, r, seed) in [(5, 1, 2, 3003), (5, 1, 2, 3005), (5, 1, 1, 3000),
                            (5, 1, 1, 3006), (6, 1, 2, 3003)]:
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
        if made is None:
            continue
        A, C, L0 = made
        O = QR.observability_matrix(A, C)
        if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        cases.append((f'rand {n}/{p}/{r} seed{seed} q0={q0}', A, C, L0, q0))
    for tag, A, C, L0, q in cases:
        v, why, w = decide(A, C, L0, q)
        print(f'{tag}（q={q}）: {v} —— {why[:110]}')
        if w:
            print('   见证首行：', [str(x) for x in w[0]])


if __name__ == '__main__':
    main()
