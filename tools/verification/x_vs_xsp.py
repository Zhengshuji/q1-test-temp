"""x_vs_xsp.py —— 在一个实例上算出 $X$（代数可容许簇）与 $X_{\\rm sp}$（谱可行子集），检验"跌落轨迹 = $X_{\\rm sp}$"

对单参数图卡（$d(k-d)=1$，$\\theta\\in\\mathbb C$）：

* $X=\\{\\theta:\\ (5a)\\}$：$(5a)$ 的多项式条件（$M_a=[(\\mathcal Z^{\\perp})A^{\\mathsf T}\\ |\\ \\mathcal Z^{\\perp}\\ |\\ W]$ 的 $(h_0+1)$-子式）；
* $X_{\\rm sp}=\\{\\theta:\\ e_0\\in\\operatorname{col}M(\\theta)\\}$：$[M(\\theta)\\mid e_0]$ 的 $(\\rho+1)$-子式的公共零点（$\\rho$ = $M$ 的典型秩），
  再逐点核验（排除"秩进一步掉落"造成的伪点）；
* 典型 gcd 的 $\\lambda$ 次数（判断"一般位置是否失败"）。

用法：python -u tools/verification/x_vs_xsp.py [n p r seed]
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
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import bezout_rank_test as BR             # noqa: E402
import chart_gcd_analysis as CGA          # noqa: E402

F = Fraction


def five_a_poly(A, C, L0, q, rows, tam):
    """$(5a)$ 的一元多项式条件（$h_0$ 层）。返回 (polys, h0)。"""
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
    Z = Ksym * W.T
    Kp = [list(x) for x in C] + [list(x) for x in L0]
    Kpsym = CGA.to_sym(Kp).T
    Msym = sp.zeros(k, k - d)
    for j in range(k - d):
        for a in range(d):
            Msym[rows[a], j] = -tam[a * (k - d) + j]
        Msym[rest[j], j] = 1
    Zperp = Kpsym.row_join(Ksym * Msym)
    Wsym = CGA.to_sym([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)]).T
    MA = (Asym.T * Zperp).row_join(Zperp).row_join(Wsym)
    MB = Zperp.row_join(Wsym)
    # h0 由采样
    hs = set()
    for t in (-2, -1, 0, 1, 2):
        sub = {tam[0]: t} if len(tam) == 1 else {}
        if not sub:
            continue
        rk = MB.subs(sub).rank()
        hs.add(rk)
    h0 = max(hs)
    polys = []
    size = h0 + 1
    if size <= MA.rows:
        for rs in itertools.combinations(range(MA.rows), size):
            for cs in itertools.combinations(range(MA.cols), size):
                d0 = sp.expand(MA[list(rs), list(cs)].det())
                if d0 != 0:
                    polys.append(d0)
    return polys, h0


def main():
    if len(sys.argv) >= 5:
        n, p, r, seed = (int(x) for x in sys.argv[1:5])
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
    else:
        # 找一个单参数、秩恒定的实例
        made = None
        for (nn, pp, rr, ss) in [(5, 1, 2, 3003), (5, 1, 1, 3006), (6, 1, 2, 3003), (5, 1, 1, 3000)]:
            cand = QR.make_instance(nn, pp, rr, ss * 17 + pp * 7 + rr)
            if cand is None:
                continue
            A0, C0, L00 = cand
            O = QR.observability_matrix(A0, C0)
            if LQ.rank(O + [x[:] for x in L00]) != LQ.rank(O):
                continue
            q0 = Q0.eta_and_q0(A0, C0, L00)[0]
            Kc = ZG.ker_cols([list(x) for x in C0] + [list(x) for x in L00])
            k = len(Kc[0])
            d = nn - pp - q0
            if d <= 0 or d >= k or d * (k - d) != 1:
                continue
            rows = tuple(range(d))
            V = ZG.ker_cols([list(x) for x in C0] + [list(x) for x in LQ.mul(C0, A0)])
            if not BR.rank_is_constant(A0, C0, L00, q0, rows, len(V[0]) + d):
                continue
            made = cand
            n, p, r, seed = nn, pp, rr, ss
            break
        if made is None:
            print('未找到"单参数 + 秩恒定"的实例')
            return
    A, C, L0 = made
    q = Q0.eta_and_q0(A, C, L0)[0]
    print(f'实例 n={n} p={p} r={r} seed={seed}；q={q}')
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    lam = sp.symbols('lam')
    for rows in itertools.combinations(range(k), d):
        tam = CGA.chart_symbols(d, k)
        print(f'  图卡 {rows}（参数 {d * (k - d)}）：')
        info = CGA.analyse_chart(A, C, L0, q, rows)
        print(f'    典型 gcd 的 λ 次数 = {info.get("deg")}；{info.get("why")}')
        polys, h0 = five_a_poly(A, C, L0, q, rows, tam)
        if polys:
            g5 = polys[0]
            for pp_ in polys[1:]:
                g5 = sp.gcd(g5, pp_)
            print(f'    X（(5a)）：h0={h0}，{len(polys)} 个子式；gcd = {sp.factor(g5)}')
        else:
            g5 = sp.Integer(0)
            print(f'    X（(5a)）：h0={h0}，无 (h0+1)-子式（h0=n ⟹ 自动成立）')
        # X_sp
        mins, D, tam2, lam2 = BR.build_minors(A, C, L0, q, rows)
        if not mins or D == 0 or len(tam2) != 1:
            print('    X_sp：退化/常数图卡，跳过')
            continue
        if len(mins) * D > 48:
            print(f'    X_sp：超预算（{len(mins)}×{D}）')
            continue
        M, e0 = BR.coefficient_matrix(mins, D, tam2, lam2)
        # 典型秩 ρ
        rho = max(M.subs({tam2[0]: t}).rank() for t in (-2, -1, 0, 1, 2))
        Aug = M.row_join(e0)
        if rho >= Aug.rows:
            # 满行秩 ⟹ e_0 自动在列空间 ⟹ $X_{sp}$ = 整个图卡（(5b) 处处成立）
            print(f'    X_sp：ρ={rho} = 行数 ⟹ e_0 自动在 col M ⟹ X_sp = 整个图卡（(5b) 处处成立）')
            continue
        size = rho + 1
        sp_polys = []
        for rs in itertools.combinations(range(Aug.rows), size):
            for cs in itertools.combinations(range(Aug.cols), size):
                d0 = sp.expand(Aug[list(rs), list(cs)].det())
                if d0 != 0:
                    sp_polys.append(d0)
        if not sp_polys:
            print(f'    X_sp：ρ={rho}，(ρ+1)-子式全为零 ⟹ 处处 e_0∈col M')
            continue
        gsp = sp_polys[0]
        for pp_ in sp_polys[1:]:
            gsp = sp.gcd(gsp, pp_)
        print(f'    X_sp：ρ={rho}，{len(sp_polys)} 个 (ρ+1)-子式；公共零点 gcd = {sp.factor(gsp)}')
        # 候选点逐点核验
        cands = []
        for r0 in sp.roots(sp.Poly(gsp, tam2[0])):
            cands.append(r0)
        print(f'    候选 θ = {[str(c) for c in cands]}')
        for th in cands:
            sub = {tam2[0]: th}
            ok = M.subs(sub).rank() == Aug.subs(sub).rank()
            print(f'      θ={sp.simplify(th)}：e_0∈col M = {ok}；在 X 中 = {sp.simplify(g5.subs(sub)) == 0 if g5 != 0 else True}')


if __name__ == '__main__':
    main()
