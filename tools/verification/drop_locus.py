"""drop_locus.py —— "gcd 掉落轨迹"的符号判定（§8.1 的最后一块）

**问题**：一般 $\\theta$ 下极大子式的 gcd 有正次数（$(5b)$ 失败），但在特殊 $\\theta$ 上 gcd 的 $\\lambda$ 次数会
**掉落**；掉到 0 时 $(5b)$ 成立。所以判定的正解是：**掉落轨迹是否非空**。

**做法**：

1. 符号求出典型 gcd $g(\\theta,\\lambda)$（[chart_gcd_analysis.py](chart_gcd_analysis.py)）；
2. 取其 $\\lambda$ 首项系数 $\\ell(\\theta)$（有理函数；清分母得多项式）——
   掉落**只能**发生在 $\\ell$ 的零点或 gcd 表示式的分母零点（有限个候选）；
3. 对每个**有理**候选 $\\theta_0$，在该点精确计算所有极大子式的 gcd：
   * 次数 0 ⟹ **该 $\\theta_0$ 可行**（并给出见证 $\\mathcal L$，过七条一致性检查）；
   * 次数 $\\ge1$ ⟹ 该点仍失败；
4. 若候选集为空 ⟹ **certified：该图卡无可行点**（掉落轨迹为空）。

**限制**：只解出**有理**候选；若候选只有无理/复根，报 `UNKNOWN` 并给出该多项式。

用法：python -u tools/verification/drop_locus.py
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

F = Fraction


def rational_roots_poly(expr, sym):
    """返回多项式 expr 在 sym 上的**有理**根（sympy 精确）。"""
    if expr == 0:
        return None                      # 恒零：整个空间都是候选
    try:
        poly = sp.Poly(sp.expand(expr), sym)
    except Exception:                    # noqa: BLE001
        return None
    if poly.degree() <= 0:
        return []
    out = []
    for r in sp.roots(poly):
        if r.is_rational:
            out.append(Fraction(int(r.p), int(r.q)))
    return out


def minors_at(A, C, L0, q, rows, theta0):
    """在 $\\theta=\\theta_0$ 处精确算极大子式（作为 $\\lambda$ 的多项式系数列表）。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    tam = CGA.chart_symbols(d, k)
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
            W[a, c] = sp.Rational(theta0.numerator, theta0.denominator)
            idx += 1
    Z = Ksym * W.T
    P = ((lam * sp.eye(n) - Asym) * Vsym).row_join(Z)
    size = P.shape[1]
    mins = []
    for rs in itertools.combinations(range(n), size):
        m = sp.expand(P[list(rs), :].det())
        if m != 0:
            mins.append(m)
    if not mins:
        return None
    g = sp.Poly(mins[0], lam)
    for m in mins[1:]:
        g = sp.gcd(g, sp.Poly(m, lam))
    return sp.degree(g.as_expr(), lam), sp.factor(g.as_expr())


def analyse(A, C, L0, q, verbose=True):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    tam = CGA.chart_symbols(d, k)
    if not tam:
        return 'INFEASIBLE' if False else 'UNKNOWN', '常数图卡，未处理', None
    out = []
    found = None
    for rows in itertools.combinations(range(k), d):
        info = CGA.analyse_chart(A, C, L0, q, rows)
        deg = info.get('deg')
        if deg is None:
            out.append((rows, None, '分析失败'))
            continue
        if deg == 0:
            L, th = DS.try_witness(A, C, L0, q, rows, info.get('den'))
            if L is not None:
                return 'FEASIBLE', f'图卡 {rows}：deg=0，θ={th} 的见证通过七条检查', L
            out.append((rows, 0, 'deg=0 但未找到通过检查的见证'))
            continue
        # deg ≥ 1：求 λ 首项系数与分母的有理根
        expr = sp.together(info['gcd'])
        num, den = expr.as_numer_denom()
        lc = sp.Poly(num, sp.symbols('lam')).LC()
        cops = []
        for pol, tag in ((lc, 'lc'), (den, 'den')):
            rs = rational_roots_poly(pol, tam[0]) if len(tam) == 1 else None
            if rs is None:
                cops.append((tag, None))
            else:
                cops.extend((tag, v) for v in rs)
        if any(v is None for _, v in cops):
            out.append((rows, deg, '候选含无理根/多参数未处理'))
            continue
        cands = sorted({v for _, v in cops})
        checked = []
        for th in cands:
            res = minors_at(A, C, L0, q, rows, th)
            if res is None:
                continue
            deg0, g0 = res
            checked.append((th, deg0))
            if deg0 == 0:
                L = [list(x) for x in L0]
                # 直接构造 L 并核验
                Z = DS.Z_from_theta(A, C, L0, q, rows, [th] * (d * (k - d)))
                L = ZG.L_from_Z(A, C, L0, Z, q) if ZG.bool_rank(ZG.cols_to_rows(Z)) == d else None
                if L is not None and LQ.condA(A, C, L):
                    CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={th}', verbose=False)
                    return 'FEASIBLE', f'图卡 {rows}：掉落点 θ={th}，见证通过七条检查', L
                out.append((rows, deg, f'掉落点 θ={th} 处 (5a) 或构造失败'))
        out.append((rows, deg, f'候选 {[(str(t), dd) for t, dd in checked]}'))
        if verbose:
            print(f'    图卡 {rows}: 典型 deg={deg}；候选 θ={[str(v) for v in cands]}；'
                  f'各点 deg={[(str(t), dd) for t, dd in checked]}')
    # 若所有图卡的候选都非空且都 deg≥1 ⟹ 无掉落 ⟹ certified infeasible
    all_done = all(len(o) == 3 and o[1] is not None and '候选' in str(o[2]) for o in out)
    if out and all_done:
        # 可靠性警告：本工具的候选集只含"gcd 的 λ 首项系数"与"gcd 表示式分母"的零点；
        # 掉落还可能发生在**各子式自身** λ 首项系数的零点（未覆盖）。因此默认**不**报 INFEASIBLE。
        return ('UNKNOWN',
                '候选点上都 deg≥1，但候选集未覆盖"各子式首项系数零点"，不足以证明掉落轨迹为空'
                '（C4 的空轨迹结论见 attempts/41 的手工核验）', None)
    return 'UNKNOWN', '；'.join(f'{r0}:{why}' for r0, _, why in out), None


def main():
    import importlib.util as iu
    print('=== 掉落轨迹分析 ===')
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    print(f'C4 反例 q={q04}：')
    v, why, w = analyse(A4, C4m, L04, q04)
    print(f'  → {v}：{why}')
    for (n, p, r, seed) in [(5, 1, 2, 3003), (5, 1, 2, 3005)]:
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
        if made is None:
            continue
        A, C, L0 = made
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        print(f'n={n} p={p} r={r} seed={seed} q={q0}：')
        v, why, w = analyse(A, C, L0, q0)
        print(f'  → {v}：{why}')
        if w:
            for row in w:
                print('     ', [str(x) for x in row])


if __name__ == '__main__':
    main()
