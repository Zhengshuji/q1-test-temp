"""decide_full.py —— 秩分层 + $(*)$ 的**完整逐阶判定**（可行给见证、不可行给逐层证书）

**状态：不可用（见 attempts/50：子式集合/次数界约定与 bezout_rank_test 不一致）**

对图卡（任意参数个数）与每个 $\\rho$：

* 层条件：$g=\\{[V|Z]\\text{ 的 }(\\rho+1)\\text{-子式}\\}$（等式）、$f=\\{[V|Z]\\text{ 的 }\\rho\\text{-子式}\\}$（"某个 $\\ne0$"）；
* $(*)$ 条件：$M_\\rho$（$P_{\\mathcal Z}(\\lambda)$ 的 $\\rho$-子式构成）的左零空间 $C_j^{(\\rho)}$，
  $e_0\\in\\operatorname{col}M_\\rho\\Rightarrow C_j=0$（若左零为空 ⟹ 层内处处可行）；
* **层判定**：理想 $I_\\rho=(g,C_j)$ 的 Gröbner 基
  - $=[1]$ ⟹ 该层**空**（无可行点）；
  - 否则用 Rabinowitsch（$zf_k-1=0$）逐个 $f_k$ 判"层内是否存在 $f_k\\ne0$ 的点"；
    若能解出有理点，代入构造 $\\mathcal L$ 并核 $(5a)$、$(5b)$、七条检查 ⟹ **FEASIBLE**；
* **图卡判定**：所有层皆空 ⟹ 该图卡不可行；某层有实/有理点 ⟹ 可行；其余 `UNKNOWN`。

用法：python -u tools/verification/decide_full.py [n p r seed]
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
CAP_MINORS = 40


def try_point(A, C, L0, q, rows, tam, gens, fs):
    """在 $V(\\mathrm{gens})$ 上找有理点且某个 $f_k\\ne0$，再核验成见证。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    nv = d * (k - d)
    sols = []
    if not gens:
        # 无等式约束：抽样找层内点（某个 f_k ≠ 0 且图卡参数有效）
        grid = [sp.Rational(v) for v in (0, 1, -1, 2, -2, 3, -3, sp.Rational(1, 2),
                                         sp.Rational(-1, 2), sp.Rational(3, 2))]
        for combo in itertools.islice(itertools.product(grid, repeat=len(tam)), 400):
            if not any(sp.simplify(fk.subs(dict(zip(tam, combo)))) != 0 for fk in fs):
                continue
            th = [F(int(sp.Rational(v).p), int(sp.Rational(v).q)) for v in combo]
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
    try:
        if len(gens) == 1 and len(tam) == 1:
            for r0 in sp.roots(sp.Poly(gens[0], tam[0])).keys():
                sols.append([r0])
        else:
            for sol in sp.solve(gens, tam, dict=True):
                if all(s in sol for s in tam):
                    sols.append([sol[s] for s in tam])
    except Exception:                              # noqa: BLE001
        return None, None
    for vals in sols:
        if any(not sp.simplify(v).is_rational for v in vals):
            continue
        if not any(sp.simplify(fk.subs(dict(zip(tam, vals)))) != 0 for fk in fs):
            continue                                # 不在该层
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


def decide_chart(A, C, L0, q, rows, verbose=False):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    full = len(V[0]) + d
    tam = CGA.chart_symbols(d, k)
    VZ, Z, Vsym = RS.VZ_matrix(A, C, L0, q, rows, tam)
    strata = []
    for rho in range(min(VZ.rows, full), 0, -1):
        g = RS.minors_poly(VZ, rho + 1) if rho + 1 <= min(VZ.rows, VZ.cols) else []
        fs = RS.minors_poly(VZ, rho)
        if not fs:
            continue
        mins, lam = RS.pen_minors(A, C, L0, q, rows, tam, rho)
        if not mins:
            continue
        D = max(sp.degree(m, lam) for m in mins)
        if D == 0:
            continue
        if len(mins) * D > 400 or len(g) > CAP_MINORS or len(fs) > CAP_MINORS:
            strata.append((rho, 'budget'))
            continue
        M, e0 = RS.coeff_matrix_from_minors(mins, lam, D)
        try:
            ns = M.T.nullspace()
        except Exception:                          # noqa: BLE001
            strata.append((rho, 'nullspace-fail'))
            continue
        Cs = []
        for yv in ns:
            dens = [sp.denom(sp.together(e)) for e in list(yv)]
            lcmden = sp.Integer(1)
            for dnm in dens:
                lcmden = sp.lcm(sp.expand(lcmden), sp.expand(dnm))
            poly = [sp.expand(sp.together(e * lcmden)) for e in list(yv)]
            Cs.append(sp.expand(sum(pp * qq for pp, qq in zip(poly, list(e0)))))
        if verbose:
            print(f'      [dbg] rho={rho}: |g|={len(g)} |fs|={len(fs)} |mins|={len(mins)} D={D} |Cs|={len(Cs)} M={M.shape}')
        g_eq = [sp.expand(x) for x in g if sp.expand(x) != 0]
        # 先判层本身是否为空（不论 Cs 是否为空）
        if g_eq:
            try:
                G0 = sp.groebner(g_eq, *tam, order='grevlex')
                if list(G0.exprs) == [sp.Integer(1)]:
                    strata.append((rho, 'empty'))
                    continue
            except Exception:                      # noqa: BLE001
                strata.append((rho, 'layer-groebner-fail'))
                continue
        gens = [sp.expand(x) for x in (g + Cs) if sp.expand(x) != 0]
        if not Cs:
            # 层内处处可行：任取层内点验证
            L, th = try_point(A, C, L0, q, rows, tam, [], fs)
            strata.append((rho, 'good' if L is not None else 'auto-but-no-point'))
            if L is not None:
                return 'FEASIBLE', f'图卡 {rows}、ρ={rho}（左零为空）、θ={th}', L
            continue
        if not gens:
            L, th = try_point(A, C, L0, q, rows, tam, [], fs)
            strata.append((rho, 'good' if L is not None else 'no-gens'))
            if L is not None:
                return 'FEASIBLE', f'图卡 {rows}、ρ={rho}、θ={th}', L
            continue
        try:
            G = sp.groebner(gens, *tam, order='grevlex')
            els = list(G.exprs)
        except Exception:                          # noqa: BLE001
            strata.append((rho, 'groebner-fail'))
            continue
        if els == [sp.Integer(1)]:
            strata.append((rho, 'empty'))
            continue
        # 非空的层：试着取点
        L, th = try_point(A, C, L0, q, rows, tam, gens, fs)
        if L is not None:
            return 'FEASIBLE', f'图卡 {rows}、ρ={rho}、θ={th}', L
        strata.append((rho, 'nonempty-but-no-rational-point'))
    if verbose:
        print(f'    图卡 {rows}：层 {strata}')
    if strata and all(s[1] == 'empty' for s in strata):
        return 'INFEASIBLE', f'图卡 {rows}：所有层皆空（{len(strata)} 层）', None
    return 'UNKNOWN', f'图卡 {rows}：{strata}', None


def decide(A, C, L0, q, verbose=True):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'UNKNOWN', 'd 越界', None
    outs = []
    for rows in itertools.combinations(range(k), d):
        v, why, w = decide_chart(A, C, L0, q, rows, verbose=True)
        outs.append((v, why))
        if v == 'FEASIBLE':
            return v, why, w
    if outs and all(v == 'INFEASIBLE' for v, _ in outs):
        return 'INFEASIBLE', '；'.join(w for _, w in outs), None
    return 'UNKNOWN', '；'.join(f'{v}:{w}' for v, w in outs), None


def main():
    if len(sys.argv) >= 5:
        cases = [tuple(int(x) for x in sys.argv[1:5])]
    else:
        cases = [(6, 2, 2, 3000), (5, 1, 2, 3003), (5, 2, 1, 3023), (6, 2, 2, 3027), (5, 1, 1, 3006)]
    import importlib.util as iu
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    print(f'C4 q0={q04}：')
    v, why, w = decide(A4, C4m, L04, q04)
    print(f'  → {v}：{why[:140]}')
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
        v, why, w = decide(A, C, L0, q0)
        print(f'  → {v}：{why[:120]}')
        if w:
            print('   见证首行：', [str(x) for x in w[0]])


if __name__ == '__main__':
    main()
