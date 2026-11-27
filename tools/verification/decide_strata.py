"""decide_strata.py —— 双重秩分层 + $(*)$：**可行给见证、不可行给逐层证书**

**状态：不可用（见 attempts/51：双重分层 + Rabinowitsch 的 Gröbner 代价过高）**

把专家指出的两处"有限析取"都实现：

* $\\rho=\\operatorname{rank}[V|Z]$（决定 $P_{\\mathcal Z}$ 的极大子式尺寸）；
* $r=\\operatorname{rank}B_a$，$B_a=[\\mathcal Z^{\\perp}\\,|\\,W]$（决定 $(5a)$ 的秩条件）；
* $(*)$：$M_\\rho$ 的左零空间 $C_j^{(\\rho)}$，$e_0\\in\\operatorname{col}M_\\rho\\Rightarrow C_j=0$。

对每个 $\\rho$、每个 $r$、每对"见证子式" $(f_\\rho,g_r)$（$f_\\rho$ 是 $[V|Z]$ 的 $\\rho$-子式、$g_r$ 是 $B_a$ 的 $r$-子式），
用 Rabinowitsch（$z f-1=0$）取系统
$$S(\\rho,r,f,g)=\\{(\\rho+1)\\text{-子式 of }[V|Z]=0\\}\\cup\\{(r+1)\\text{-子式 of }M_a=0\\}\\cup\\{C_j^{(\\rho)}=0\\}\\cup\\{zf_\\rho-1=0\\}\\cup\\{zg_r-1=0\\}.$$
$S$ 的 Gröbner 基 $=[1]$ ⟹ 该 (层, 见证) 组合没有点；**所有**组合都空 ⟹ 该图卡无可行点（证书）。
若某组合非空，尝试取有理点并核 $(5a)$、$(5b)$、七条检查 ⟹ 见证。

用法：python -u tools/verification/decide_strata.py [n p r seed]
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
CALL_CAP = 24


def Ma_matrix(A, C, L0, q, rows, tam):
    """$M_a=[(\\mathcal Z^{\\perp})A^{\\mathsf T}\\ |\\ \\mathcal Z^{\\perp}\\ |\\ W]$ 与 $B_a=[\\mathcal Z^{\\perp}|W]$。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    Ksym = CGA.to_sym(Kc)
    Asym = CGA.to_sym(A)
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
    Zperp = Kpsym.row_join(Ksym * Msym)
    Wsym = CGA.to_sym([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)]).T
    Ba = Zperp.row_join(Wsym)
    Ma = (Asym.T * Zperp).row_join(Ba)
    return Ma, Ba


def point_ok(A, C, L0, q, rows, tam, th):
    d = len(A) - len(C) - q
    Zt = DS.Z_from_theta(A, C, L0, q, rows, th)
    if ZG.bool_rank(ZG.cols_to_rows(Zt)) != d:
        return None
    L = ZG.L_from_Z(A, C, L0, Zt, q)
    if L is None or not LQ.condA(A, C, L):
        return None
    if TC.analyse(A, C, L)['five_b']:
        CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={th}', verbose=False)
        return L
    return None


def solve_points(gens, tam, limit=60):
    """尝试从理想 gens 中取有理点（逐个变量的一元/多变量 solve）。"""
    out = []
    try:
        if len(tam) == 1:
            g = None
            for p0 in gens:
                p0 = sp.expand(p0)
                if p0 == 0:
                    continue
                g = p0 if g is None else sp.gcd(g, p0)
            if g is not None and sp.degree(g, tam[0]) > 0:
                for r0 in sp.roots(sp.Poly(g, tam[0])).keys():
                    if sp.simplify(r0).is_rational:
                        out.append([r0])
        else:
            for sol in sp.solve(gens, tam, dict=True):
                if all(s in sol for s in tam) and all(sp.simplify(sol[s]).is_rational for s in tam):
                    out.append([sol[s] for s in tam])
    except Exception:                                # noqa: BLE001
        pass
    return out[:limit]


def decide_chart(A, C, L0, q, rows, calls, verbose=False):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    tam = CGA.chart_symbols(d, k)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    full = len(V[0]) + d
    VZ, Z, Vsym = RS.VZ_matrix(A, C, L0, q, rows, tam)
    Ma, Ba = Ma_matrix(A, C, L0, q, rows, tam)
    z1, z2 = sp.symbols('z1_sat z2_sat')
    strata = []
    for rho in range(min(VZ.rows, full), 0, -1):
        f_rho = RS.minors_poly(VZ, rho)
        g_rho = RS.minors_poly(VZ, rho + 1) if rho + 1 <= min(VZ.rows, VZ.cols) else []
        if not f_rho:
            continue
        mins, lam = RS.pen_minors(A, C, L0, q, rows, tam, rho)
        if not mins:
            continue
        D = max(sp.degree(m, lam) for m in mins)
        if D == 0:
            continue
        try:
            M, e0 = RS.coeff_matrix_from_minors(mins, lam, D)
            ns = M.T.nullspace()
        except Exception:                        # noqa: BLE001
            continue
        Cs = []
        for yv in ns:
            dens = [sp.denom(sp.together(e)) for e in list(yv)]
            lcmden = sp.Integer(1)
            for dnm in dens:
                lcmden = sp.lcm(sp.expand(lcmden), sp.expand(dnm))
            poly = [sp.expand(sp.together(e * lcmden)) for e in list(yv)]
            Cs.append(sp.expand(sum(pp * qq for pp, qq in zip(poly, list(e0)))))
        for rr in range(min(Ba.rows, Ba.cols), 0, -1):
            g_r = RS.minors_poly(Ba, rr)
            h_r = RS.minors_poly(Ma, rr + 1) if rr + 1 <= min(Ma.rows, Ma.cols) else []
            if not g_r:
                continue
            base = [sp.expand(x) for x in (g_rho + h_r + Cs) if sp.expand(x) != 0]
            cand_pts = []
            all_empty = True
            for fk in f_rho[:2]:
                for gl in g_r[:2]:
                    if calls[0] >= CALL_CAP:
                        strata.append((rho, rr, 'budget'))
                        return 'UNKNOWN', f'图卡 {rows}：预算用尽（{CALL_CAP} 次）', None
                    calls[0] += 1
                    sysm = base + [sp.expand(z1 * fk - 1), sp.expand(z2 * gl - 1)]
                    try:
                        G = sp.groebner(sysm, *(list(tam) + [z1, z2]), order='grevlex')
                        els = list(G.exprs)
                    except Exception:            # noqa: BLE001
                        continue
                    if els != [sp.Integer(1)]:
                        all_empty = False
                        pts = solve_points(base, tam)
                        for pt in pts:
                            th = [F(int(sp.Rational(v).p), int(sp.Rational(v).q)) for v in pt]
                            L = point_ok(A, C, L0, q, rows, tam, th)
                            if L is not None:
                                return 'FEASIBLE', f'图卡 {rows}、ρ={rho}、r={rr}、θ={th}', L
                        break
                if not all_empty:
                    break
            strata.append((rho, rr, 'empty' if all_empty else 'nonempty'))
    if strata and all(s[2] == 'empty' for s in strata):
        return 'INFEASIBLE', f'图卡 {rows}：所有 (ρ,r,见证) 组合皆空（{len(strata)} 组）', None
    return 'UNKNOWN', f'图卡 {rows}：{strata}', None


def decide(A, C, L0, q, verbose=False):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'UNKNOWN', 'd 越界', None
    calls = [0]
    outs = []
    for rows in itertools.combinations(range(k), d):
        v, why, w = decide_chart(A, C, L0, q, rows, calls, verbose=verbose)
        if verbose:
            print(f'    [chart {rows}] {v}（累计 Gröbner {calls[0]} 次）')
        outs.append((v, why))
        if v == 'FEASIBLE':
            return v, why, w
        if v == 'UNKNOWN':
            return 'UNKNOWN', why, None
    if outs and all(v == 'INFEASIBLE' for v, _ in outs):
        return 'INFEASIBLE', '；'.join(w for _, w in outs), None
    return 'UNKNOWN', '；'.join(w for _, w in outs), None


def main():
    import importlib.util as iu
    cases = []
    if len(sys.argv) >= 5:
        cases = [tuple(int(x) for x in sys.argv[1:5])]
    else:
        cases = [(5, 1, 2, 3003), (6, 2, 2, 3027), (5, 2, 1, 3023)]
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    print(f'C4 q0={q04}：')
    v, why, w = decide(A4, C4m, L04, q04, verbose=True)
    print(f'  → {v}：{why[:160]}')
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
        v, why, w = decide(A, C, L0, q0, verbose=True)
        print(f'  → {v}：{why[:160]}')
        if w:
            print('   见证首行：', [str(x) for x in w[0]])


if __name__ == '__main__':
    main()
