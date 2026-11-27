"""chart_gcd_analysis.py —— 逐图卡的**符号 gcd 分析**（§8.1 的谱层，替代网格）

对每个图卡（参数 $\\theta$），把 $P_{\\mathcal Z}(\\lambda)=[(\\lambda I-A)V\\ |\\ Z(\\theta)]$ 的极大子式看作
$\\mathbb Q(\\theta)[\\lambda]$ 中的多项式，算它们的**符号 gcd**：

* $\\deg_\\lambda \\gcd=0$ ⟹ 对一般 $\\theta$，$(5b)$ 成立（该图卡"好"）——代入有理 $\\theta$ 得见证；
* $\\deg_\\lambda \\gcd\\ge1$ ⟹ 对一般 $\\theta$，$(5b)$ **失败**（该图卡"坏"），且给出**显式公共因子**。

于是整阶判定变成"逐图卡看 gcd 的 $\\lambda$ 次数"——**不采样**、可读、可复核。
注意事项（诚实）：$\\deg=0$ 只对一般 $\\theta$ 成立；$\\deg\\ge1$ 的图卡仍需排除
"使首项系数消失的有限个 $\\theta$"（本脚本报告这些 $\\theta$ 的分母，供进一步核验）。

用法：python -u tools/verification/chart_gcd_analysis.py
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

F = Fraction


def to_sym(M):
    return sp.Matrix([[sp.Rational(v.numerator, v.denominator) for v in row] for row in M])


def chart_symbols(d, k):
    n = d * (k - d)
    if n == 0:
        return ()
    return tuple(sp.symbols(f't0:{n}')) if n > 1 else (sp.symbols('t0'),)


def analyse_chart(A, C, L0, q, rows, max_minors=60):
    """返回 dict：gcd 的 λ 次数、公共因子、非零子式数、说明。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    tam = chart_symbols(d, k)
    lam = sp.symbols('lam')
    Ksym = to_sym(Kc)
    Asym = to_sym(A)
    Vsym = to_sym(V)
    # Z(θ) = K·W
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
    P = (lam * sp.eye(n) - Asym) * Vsym
    P = P.row_join(Z)
    size = P.shape[1]
    if size == 0:
        return {'deg': None, 'why': '无列'}
    mins = []
    for rs in itertools.combinations(range(n), size):
        m = sp.expand(P[list(rs), :].det())
        if m != 0:
            mins.append(m)
        if len(mins) >= max_minors:
            break
    if not mins:
        return {'deg': None, 'why': '所有极大子式恒零'}
    if not tam:
        polys = [sp.Poly(m, lam) for m in mins]
        g = polys[0]
        for h in polys[1:]:
            g = sp.gcd(g, h)
        return {'deg': sp.degree(g.as_expr(), lam), 'gcd': sp.factor(g.as_expr()),
                'nminors': len(mins), 'why': f'常数图卡；子式 {len(mins)} 个'}
    dom = sp.QQ.frac_field(*tam)
    try:
        polys = [sp.Poly(m, lam, domain=dom) for m in mins]
    except Exception as e:                        # noqa: BLE001
        return {'deg': None, 'why': f'域转换失败：{e}'}
    g = polys[0]
    for h in polys[1:]:
        g = sp.gcd(g, h)
    expr = sp.factor(sp.simplify(g.as_expr()))
    deg = sp.degree(sp.together(expr).as_numer_denom()[0], lam)
    den = sp.together(expr).as_numer_denom()[1]
    return {'deg': deg, 'gcd': expr, 'den': den, 'nminors': len(mins),
            'why': f'子式 {len(mins)} 个；分母（例外的 θ）= {den}'}


def main():
    import importlib.util as iu
    print('=== 逐图卡符号 gcd 分析 ===')
    targets = []
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    targets.append(('C4 反例', A4, C4m, L04, q04))
    spec2 = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m2 = iu.module_from_spec(spec2)
    spec2.loader.exec_module(m2)
    targets.append(('公开例子', m2.A, m2.C, m2.L0, 5))
    for tag, A, C, L0, q in targets:
        n, p, r = len(A), len(C), len(L0)
        d = n - p - q
        Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        k = len(Kc[0])
        print(f'{tag}：n={n} p={p} r={r} q={q} d={d} k={k}（参数 {d * (k - d)}）')
        if d < 0 or d > k:
            print('  d 越界，跳过')
            continue
        verdicts = []
        for rows in itertools.combinations(range(k), d):
            if d * (k - d) > 3:
                print('  （参数 >3，跳过该实例）')
                break
            info = analyse_chart(A, C, L0, q, rows)
            print(f'  图卡 {rows}: λ次数={info["deg"]}；{info["why"]}'
                  + (f'\n      gcd = {info["gcd"]}' if info.get('gcd') else ''))
            verdicts.append(info['deg'])
        if verdicts and all(v is not None and v >= 1 for v in verdicts):
            print('  ⟹ 各图卡对一般 θ 都**失败** ⟹ 该阶（一般位置下）不可行')
        elif any(v == 0 for v in verdicts):
            print('  ⟹ 某图卡对一般 θ **成立** ⟹ 该阶可行（可代入有理 θ 取见证）')


if __name__ == '__main__':
    main()
