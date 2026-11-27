"""joint_system.py —— 专家的 (B)+(C)：把 $(5a)$ 用**列空间包含**编码，与 Bézout 条件并成一个多项式系统

专家 2026-11-03 §2.2–§2.3 的建议：

* $(5a)$ 用辅助矩阵 $T$ 编码成**线性**方程（对 $T$ 线性），**不需要**对 $r=\\operatorname{rank}B_a$ 分层：
  $$A^{\\mathsf T}X_c(\\theta)=B_a(\\theta)\\,T,\\qquad B_a=[X_c\\mid W],\\ X_c=\\mathcal Z^{\\perp}\\text{ 的基};$$
* 谱条件用 Bézout 恒等式（对 $u$ 线性）：
  $$\\sum_{i}\\sum_{k<D}u_{i,k}\\,\\lambda^k m_i^{(\\rho)}(\\theta,\\lambda)=1;$$
* 于是对固定 $\\rho$，"该层存在可行 $\\theta$" ⟺ 系统
  $$S_\\rho=\\{(5a)\\text{ 的 }T\\text{-方程}\\}\\cup\\{\\text{Bézout 系数方程}\\}$$
  在 $(\\theta,T,u)$ 上有解。**注意**：若 $\\operatorname{rank}[V|Z]<\\rho$，则所有 $\\rho$-子式为零 ⟹
  Bézout 方程无解 ⟹ 该 $\\theta$ 自动被排除，所以**不需要**额外的"层"条件。

本模块：对每个 $\\rho$ 建 $S_\\rho$ 并判可满足性（Gröbner 基 $=[1]$ ⟹ 无解）；若有解则尝试取有理点并核验。

用法：python -u tools/verification/joint_system.py
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

F = Fraction
CAP_MINORS = 24


def build_chart(A, C, L0, q, rows, tam):
    """返回 (Xc, Ba, Wsym)：$X_c=\\mathcal Z^{\\perp}$（$n\\times(n-d)$）、$B_a=[X_c|W]$、$W$。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    Ksym = CGA.to_sym(Kc)
    W = sp.zeros(d, k)
    rest = [i for i in range(k) if i not in rows]
    for a, r0 in enumerate(rows):
        W[a, r0] = 1
    idx = 0
    for a in range(d):
        for c in rest:
            W[a, c] = tam[idx]
            idx += 1
    Kp = [list(x) for x in C] + [list(x) for x in L0]
    Kpsym = CGA.to_sym(Kp).T
    Msym = sp.zeros(k, k - d)
    for j in range(k - d):
        for a in range(d):
            Msym[rows[a], j] = -tam[a * (k - d) + j]
        Msym[rest[j], j] = 1
    Xc = Kpsym.row_join(Ksym * Msym)                    # Z^perp 的基（列）
    Wrows = CGA.to_sym([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)]).T
    Ba = Xc.row_join(Wrows)
    return Xc, Ba, Wrows


def five_a_equations(A, Xc, Ba, tam, T):
    """$A^{\\mathsf T}X_c-B_a T=0$（对 $T$ 线性）。"""
    Asym = CGA.to_sym(A)
    lhs = Asym.T * Xc
    eqs = []
    for i in range(lhs.rows):
        for j in range(lhs.cols):
            eqs.append(sp.expand(lhs[i, j] - (Ba * T)[i, j]))
    return eqs


def bezout_equations(mins, lam, D, u):
    """$\\sum_{i,k}u_{i,k}\\lambda^k m_i-1=0$ 的系数方程。"""
    total = sp.Integer(0)
    idx = 0
    for m in mins:
        poly = sp.Poly(sp.expand(m), lam)
        cdict = poly.as_dict()
        for kk in range(D):
            coef = sp.Integer(0)
            for (j,), c in cdict.items():
                if j + kk < 2 * D:
                    coef += c * lam ** (j + kk)
            total += u[idx] * coef
            idx += 1
    total = sp.expand(total - 1)
    poly = sp.Poly(sp.expand(total), lam)
    cdict = poly.as_dict()
    return [sp.expand(cdict.get((j,), sp.Integer(0))) for j in range(2 * D)]


def decide_chart(A, C, L0, q, rows, budget=60):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    tam = CGA.chart_symbols(d, k)
    if not tam:
        return 'UNKNOWN', '常数图卡', None
    Xc, Ba, Wrows = build_chart(A, C, L0, q, rows, tam)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    full = len(V[0]) + d
    results = []
    for rho in range(min(n, full), 0, -1):
        mins, lam = RS.pen_minors(A, C, L0, q, rows, tam, rho)
        if not mins or len(mins) > CAP_MINORS:
            continue
        D = max(sp.degree(m, lam) for m in mins)
        if D == 0:
            continue
        nu = len(mins) * D
        if nu > budget:
            continue
        u = sp.symbols(f'u0:{nu}')
        nb = Ba.cols
        T = sp.Matrix(nb, Xc.cols, lambda i, j: sp.Symbol(f'T_{i}_{j}'))
        eqs = five_a_equations(A, Xc, Ba, tam, T) + bezout_equations(mins, lam, D, u)
        vars_ = list(tam) + [T[i, j] for i in range(nb) for j in range(Ba.cols and Xc.cols)] + list(u)
        try:
            G = sp.groebner([sp.expand(e) for e in eqs], *vars_, order='grevlex')
            els = list(G.exprs)
        except Exception as e:                        # noqa: BLE001
            results.append((rho, 'groebner-fail'))
            continue
        if els == [sp.Integer(1)]:
            results.append((rho, 'empty'))
            continue
        # 非空：尝试取有理点
        pts = []
        try:
            for sol in sp.solve([sp.expand(e) for e in eqs], list(tam), dict=True):
                if all(s in sol for s in tam) and all(sp.simplify(sol[s]).is_rational for s in tam):
                    pts.append([sol[s] for s in tam])
        except Exception:                             # noqa: BLE001
            pass
        for pt in pts:
            th = [F(int(sp.Rational(v).p), int(sp.Rational(v).q)) for v in pt]
            Zt = DS.Z_from_theta(A, C, L0, q, rows, th)
            if ZG.bool_rank(ZG.cols_to_rows(Zt)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Zt, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            if TC.analyse(A, C, L)['five_b']:
                CC.check_candidate(A, C, L0, L, tag=f'q={q} rho={rho} theta={th}', verbose=False)
                return 'FEASIBLE', f'ρ={rho}、θ={th}（联合系统 + 七条检查）', L
        results.append((rho, 'nonempty-no-rational-point'))
    if results and all(x[1] == 'empty' for x in results):
        return 'INFEASIBLE', f'所有 ρ 层联合系统皆空（{results}）', None
    return 'UNKNOWN', f'{results}', None


def decide(A, C, L0, q):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'UNKNOWN', 'd 越界', None
    for rows in itertools.combinations(range(k), d):
        v, why, w = decide_chart(A, C, L0, q, rows)
        if v in ('FEASIBLE', 'INFEASIBLE'):
            return v, f'图卡 {rows}：{why}', w
    return 'UNKNOWN', '未定', None


def main():
    import importlib.util as iu
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    print(f'C4 q0={q04}：')
    v, why, w = decide(A4, C4m, L04, q04)
    print(f'  → {v}：{why[:200]}')
    for (n, p, r, seed) in [(5, 2, 1, 3023)]:
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
        if made is None:
            continue
        A, C, L0 = made
        O = QR.observability_matrix(A, C)
        if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        print(f'n={n} p={p} r={r} seed={seed} q0={q0}：')
        v, why, w = decide(A, C, L0, q0)
        print(f'  → {v}：{why[:200]}')


if __name__ == '__main__':
    main()
