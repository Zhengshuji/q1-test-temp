"""rank_stratified.py —— 秩分层：在"$\\operatorname{rank}[V|Z]=\\rho$"的层上跑 $(*)$ 判据

**问题**（见 [attempts/48](48_rank_stratification_needed.md)）：$\\operatorname{rank}[V|Z]$ 在特殊 $\\theta$ 处跌落，
极大子式的尺寸随之从 $\\dim V+d$ 掉到 $\\rho$，用固定尺寸会误判。

**做法**（单参数图卡，$\\theta\\in\\mathbb C$）：对每个 $\\rho$：

1. 层条件：$\\{g_i(\\theta)=0\\}$（$[V|Z]$ 的 $(\\rho+1)$-子式）与 $\\{f_k(\\theta)\\ne0\\}$（某个 $\\rho$-子式）；
2. 在 $\\rho$ 层上，$(5b)\\iff e_0\\in\\operatorname{col}M_\\rho(\\theta)$，$M_\\rho$ 由 $P_{\\mathcal Z}(\\lambda)$ 的 $\\rho$-子式构成；
3. 由左零空间得 $C_j^{(\\rho)}(\\theta)$，$e_0\\in\\operatorname{col}M_\\rho\\Rightarrow C_j=0$；
4. 于是候选 $\\theta$ = $\\{g_i\\}\\cup\\{C_j\\}$ 的公共零点（单参数：一元 gcd 的根）；再核验 $f_k\\ne0$、
   $(5a)$、以及 $\\theta$ 处的 $(5b)$（Toeplitz + gcd 双路）。

用法：python -u tools/verification/rank_stratified.py [n p r seed]
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
import spectral_gcd as SG                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import consistency_checks as CC           # noqa: E402
import chart_gcd_analysis as CGA          # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def VZ_matrix(A, C, L0, q, rows, tam):
    """$[V\\ |\\ Z(\\theta)]$ 与 $[V|Z]$ 的各类子式。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    Ksym = CGA.to_sym(Kc)
    Vsym = CGA.to_sym(V)
    W = sp.zeros(d, k)
    rest = [i for i in range(k) if i not in rows]
    for a, r0 in enumerate(rows):
        W[a, r0] = 1
    idx = 0
    for a in range(d):
        for c in rest:
            W[a, c] = tam[idx]
            idx += 1
    Z = Ksym * W.T
    return Vsym.row_join(Z), Z, Vsym


def minors_poly(M, size):
    out = []
    for rs in itertools.combinations(range(M.rows), size):
        for cs in itertools.combinations(range(M.cols), size):
            d0 = sp.expand(M[list(rs), list(cs)].det())
            if d0 != 0:
                out.append(d0)
    return out


def pen_minors(A, C, L0, q, rows, tam, size):
    """$P_{\\mathcal Z}(\\lambda)$ 的 size×size 子式（含 $\\lambda$）。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    lam = sp.symbols('lam')
    Ksym = CGA.to_sym(Kc)
    Asym = CGA.to_sym(A)
    Vsym = CGA.to_sym(V)
    W = sp.zeros(d, k)
    rest = [i for i in range(k) if i not in rows]
    for a, r0 in enumerate(rows):
        W[a, r0] = 1
    idx = 0
    for a in range(d):
        for c in rest:
            W[a, c] = tam[idx]
            idx += 1
    Z = Ksym * W.T
    P = ((lam * sp.eye(n) - Asym) * Vsym).row_join(Z)
    out = []
    for rs in itertools.combinations(range(P.rows), size):
        for cs in itertools.combinations(range(P.cols), size):
            d0 = sp.expand(P[list(rs), list(cs)].det())
            if d0 != 0:
                out.append(d0)
    return out, lam


def coeff_matrix_from_minors(mins, lam, D):
    rows_n = 2 * D
    cols = []
    for m in mins:
        poly = sp.Poly(sp.expand(m), lam)
        cdict = poly.as_dict()
        cm = [sp.expand(cdict.get((j,), sp.Integer(0))) for j in range(poly.degree() + 1)]
        for kk in range(D):
            col = [sp.Integer(0)] * rows_n
            for j, c in enumerate(cm):
                if j + kk < rows_n:
                    col[j + kk] = c
            cols.append(sp.Matrix(col))
    M = sp.Matrix.hstack(*cols) if cols else sp.zeros(rows_n, 0)
    e0 = sp.Matrix([1] + [0] * (rows_n - 1))
    return M, e0


def roots_of(gens, sym):
    """单参数：{g_i} 与 {C_j} 的公共零点（一元 gcd 的有理/代数根）。"""
    g = None
    for p0 in gens:
        p0 = sp.expand(p0)
        if p0 == 0:
            continue
        g = p0 if g is None else sp.gcd(g, p0)
    if g is None:
        return None, '所有条件恒零（整条线都是候选）'
    if sp.degree(g, sym) == 0:
        return [], f'公共零点为空（gcd 为非零常数）'
    try:
        rs = list(sp.roots(sp.Poly(g, sym)).keys())
    except Exception:                            # noqa: BLE001
        rs = []
    return rs, f'gcd = {sp.factor(g)}'


def analyse(A, C, L0, q, verbose=True):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d * (k - d) != 1:
        return 'UNKNOWN', '只实现单参数图卡', None
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    full = len(V[0]) + d
    found = []
    for rows in itertools.combinations(range(k), d):
        tam = CGA.chart_symbols(d, k)
        VZ, Z, Vsym = VZ_matrix(A, C, L0, q, rows, tam)
        for rho in range(min(VZ.rows, full), d - 1, -1):
            if rho == 0:
                continue
            g = minors_poly(VZ, rho + 1) if rho + 1 <= min(VZ.rows, VZ.cols) else []
            f = minors_poly(VZ, rho)
            if not f:
                continue
            mins, lam = pen_minors(A, C, L0, q, rows, tam, rho)
            if not mins:
                continue
            D = max(sp.degree(m, lam) for m in mins)
            if D == 0 or len(mins) * D > 400:
                continue
            M, e0 = coeff_matrix_from_minors(mins, lam, D)
            # 左零空间
            try:
                ns = M.T.nullspace()
            except Exception:                    # noqa: BLE001
                continue
            Cs = []
            for yv in ns:
                dens = [sp.denom(sp.together(e)) for e in list(yv)]
                lcmden = sp.Integer(1)
                for dnm in dens:
                    lcmden = sp.lcm(sp.expand(lcmden), sp.expand(dnm))
                poly = [sp.expand(sp.together(e * lcmden)) for e in list(yv)]
                Cs.append(sp.expand(sum(pp * qq for pp, qq in zip(poly, list(e0)))))
            if not Cs:
                # 左零空间为空 ⟹ M 满行秩 ⟹ e_0 自动在列空间 ⟹ 该层处处 (5b) 成立
                why = '左零空间为空 ⟹ 该层处处可行（取层内一点验证）'
                cands = [sp.Rational(v) for v in (0, 1, -1, 2, -2, sp.Rational(1, 2), sp.Rational(3, 2))]
            else:
                cands, why = roots_of(g + Cs, tam[0])
                if cands is None:
                    continue
            if verbose:
                print(f'  图卡 {rows}，ρ={rho}：(ρ+1)-子式 {len(g)}，(ρ)-子式 {len(f)}，'
                      f'M {M.shape}，C {len(Cs)}；{why}')
            for th in cands:
                sub = {tam[0]: th}
                if not any(sp.simplify(fk.subs(sub)) != 0 for fk in f):
                    continue                       # 不在该层
                thr = th if th.is_real else None
                if thr is None:
                    continue
                thq = F(int(sp.Rational(thr).p), int(sp.Rational(thr).q)) if thr.is_rational else None
                if thq is None:
                    continue
                Zt = DS.Z_from_theta(A, C, L0, q, rows, [thq])
                if ZG.bool_rank(ZG.cols_to_rows(Zt)) != d:
                    continue
                L = ZG.L_from_Z(A, C, L0, Zt, q)
                if L is None or not LQ.condA(A, C, L):
                    continue
                if TC.analyse(A, C, L)['five_b']:
                    CC.check_candidate(A, C, L0, L, tag=f'q={q} rho={rho} theta={thq}', verbose=False)
                    found.append((rows, rho, thq))
                    return 'FEASIBLE', f'图卡 {rows}、层 ρ={rho}、θ={thq}（见证通过七条检查）', L
    return 'UNKNOWN', f'未找到可行层（候选 {found}）', None


def main():
    cases = []
    if len(sys.argv) >= 5:
        cases.append(tuple(int(x) for x in sys.argv[1:5]))
    else:
        cases = [(5, 1, 2, 3003), (5, 1, 2, 3005), (5, 1, 1, 3006), (5, 2, 1, 3023), (6, 2, 2, 3027)]
    for (n, p, r, seed) in cases:
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
        if made is None:
            continue
        A, C, L0 = made
        O = QR.observability_matrix(A, C)
        if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        print(f'n={n} p={p} r={r} seed={seed} q0={q0}：')
        v, why, w = analyse(A, C, L0, q0)
        print(f'  → {v}：{why}')
        if w:
            print('   见证首行：', [str(x) for x in w[0]])


if __name__ == '__main__':
    main()
