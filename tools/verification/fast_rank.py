"""fast_rank.py —— 用 $\\mathbb Q(\\theta)$ 上的**秩比较**替代子式 Gröbner（专攻可行方向）

观察（本模块的依据）：

* $(5a)$：$A^{\\mathsf T}X_c=B_aT$ 可解 $\\iff \\operatorname{rank}_{\\mathbb Q(\\theta)}M_a=\\operatorname{rank}_{\\mathbb Q(\\theta)}B_a$
  —— 一个**布尔**，一次符号秩，**不需要**算 $(r_a+1)$-子式、更不需要 Gröbner；
* $(5b)$：$e_0\\in\\operatorname{col}M_\\rho$ $\\iff \\operatorname{rank}M_\\rho=\\operatorname{rank}[M_\\rho\\mid e_0]$（同样一个布尔）。

若两个等式在**典型层**都成立，则两个"好集"都是稠密开集，其交非空 ⟹ **存在**可行 $\\theta$；
再取若干有理 $\\theta$（避开有限个例外值）逐一核验 $(5a)$、$(5b)$ 与七条检查 ⟹ 见证。

若 $(5b)$ 的等式**不**成立（典型层谱不可行），则该阶的可行性只可能落在"gcd 跌落"轨迹上——
需要另一套工具（见 [attempts/43](43_drop_locus.md)），本模块报 `INFEASIBLE_GENERIC`。

用法：python -u tools/verification/fast_rank.py [--sweep N]
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
import chart_gcd_analysis as CGA          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import rank_stratified as RS              # noqa: E402
import joint_system as JS                 # noqa: E402

F = Fraction
CAND = [F(0), F(1), F(-1), F(2), F(-2), F(3), F(-3), F(1, 2), F(-1, 2), F(3, 2), F(5, 2), F(1, 3)]


def sym_rank(M):
    """$\\mathbb Q(\\theta)$ 上的秩（sympy 精确）。"""
    if M.rows == 0 or M.cols == 0:
        return 0
    return M.rank()


def constant_chart(A, C, L0, q, rows):
    """常数图卡：$Z$ 唯一，直接核验。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d == k:
        Z = [list(x) for x in Kc]
    elif d == 0:
        Z = [[] for _ in range(n)]
    else:
        return 'UNKNOWN', f'常数图卡（d={d}, k={k}）', None
    if d > 0 and ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
        return 'INFEASIBLE', '常数图卡：Z 秩不足', None
    L = ZG.L_from_Z(A, C, L0, Z, q)
    if L is None or not LQ.condA(A, C, L):
        return 'INFEASIBLE', '常数图卡：(5a) 失败', None
    if TC.analyse(A, C, L)['five_b']:
        CC.check_candidate(A, C, L0, L, tag=f'q={q} 常数图卡', verbose=False)
        return 'FEASIBLE', '常数图卡：唯一 Z 通过全部检查', L
    return 'INFEASIBLE', '常数图卡：(5b) 失败', None


def analyse_chart(A, C, L0, q, rows):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    tam = CGA.chart_symbols(d, k)
    if not tam:
        return constant_chart(A, C, L0, q, rows)
    Xc, Ba, Wrows = JS.build_chart(A, C, L0, q, rows, tam)
    Asym = CGA.to_sym(A)
    M_a = (Asym.T * Xc).row_join(Ba)
    VZ, Z, Vsym = RS.VZ_matrix(A, C, L0, q, rows, tam)
    try:
        rho = sym_rank(VZ)                      # 该图卡上 rank[V|Z] 的真实值（$\mathbb Q(\theta)$ 上）
    except Exception:                            # noqa: BLE001
        return 'UNKNOWN', 'rank[V|Z] 符号计算失败', None
    if rho < 1 or rho > min(VZ.rows, VZ.cols):
        return 'UNKNOWN', f'ρ={rho} 越界', None
    mins, lam = RS.pen_minors(A, C, L0, q, rows, tam, rho)
    if not mins:
        return 'UNKNOWN', f'无 {rho} 阶子式', None
    D = max(sp.degree(m, lam) for m in mins)
    if D == 0:
        return 'UNKNOWN', 'D=0', None
    M, e0 = RS.coeff_matrix_from_minors(mins, lam, D)
    try:
        r_a = sym_rank(M_a) == sym_rank(Ba)
    except Exception:                              # noqa: BLE001
        r_a = None
    try:
        r_b = sym_rank(M) == sym_rank(M.row_join(e0))
    except Exception:                              # noqa: BLE001
        r_b = None
    info = f'ρ={rho}, (5a) 典型可解={r_a}, (5b) 典型成立={r_b}, 子式 {len(mins)} 个'
    if r_b is False:
        return 'INFEASIBLE_GENERIC', f'{info}（谱条件在典型层失败 ⟹ 只能靠跌落轨迹）', None
    if r_a is False:
        return 'INFEASIBLE_GENERIC', f'{info}（(5a) 在典型层失败）', None
    if r_a is None or r_b is None:
        return 'UNKNOWN', f'{info}（秩比较失败）', None
    # 两者都在典型层成立 ⟹ 稠密开集之交非空 ⟹ 取有理点核验
    for th in CAND:
        ths = [th] * (d * (k - d))
        Zt = DS.Z_from_theta(A, C, L0, q, rows, ths)
        if ZG.bool_rank(ZG.cols_to_rows(Zt)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Zt, q)
        if L is None or not LQ.condA(A, C, L):
            continue
        if TC.analyse(A, C, L)['five_b']:
            CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={ths}', verbose=False)
            return 'FEASIBLE', f'{info}，θ={ths}', L
    return 'UNKNOWN', f'{info}：典型层成立但未取到见证', None


def decide(A, C, L0, q):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'UNKNOWN', 'd 越界', None
    outs = []
    for rows in itertools.combinations(range(k), d):
        v, why, w = analyse_chart(A, C, L0, q, rows)
        outs.append((rows, v, why))
        if v == 'FEASIBLE':
            return v, f'图卡 {rows}：{why}', w
    if outs and all(v == 'INFEASIBLE' for _, v, _ in outs):
        return 'INFEASIBLE', '；'.join(f'{rr}:{yy}' for rr, _, yy in outs), None
    if outs and all(v in ('INFEASIBLE', 'INFEASIBLE_GENERIC') for _, v, _ in outs):
        return 'INFEASIBLE_GENERIC', '；'.join(f'{rr}:{yy[:70]}' for rr, _, yy in outs), None
    return 'UNKNOWN', '；'.join(f'{rr}:{vv}:{yy[:60]}' for rr, vv, yy in outs), None


def main():
    import importlib.util as iu
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    print(f'C4 q0={q04}：', flush=True)
    v, why, w = decide(A4, C4m, L04, q04)
    print(f'  → {v}：{why[:160]}', flush=True)
    if '--sweep' in sys.argv:
        maxn = int(sys.argv[sys.argv.index('--sweep') + 1])
        from collections import Counter
        stats = Counter()
        done = 0
        for n in (5, 6, 7):
            for p in (1, 2):
                for r in (1, 2):
                    if p + r > n:
                        continue
                    for seed in range(3000, 3010):
                        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                        if made is None:
                            continue
                        A, C, L0 = made
                        O = QR.observability_matrix(A, C)
                        if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                            continue
                        q0 = Q0.eta_and_q0(A, C, L0)[0]
                        v, why, w = decide(A, C, L0, q0)
                        stats[v] += 1
                        done += 1
                        print(f'n={n} p={p} r={r} seed={seed} q0={q0}: {v}', flush=True)
                        if done >= maxn:
                            print('统计：', dict(stats))
                            return
        print('统计：', dict(stats))


if __name__ == '__main__':
    main()
