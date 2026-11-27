"""decide_symbolic.py —— 逐阶判定的**符号闭环**：可行给见证、不可行给 gcd 证书

对每个图卡：

1. 用符号 gcd 分析（[chart_gcd_analysis.py](chart_gcd_analysis.py)）得 $\\deg_\\lambda\\gcd$；
2. $\\deg=0$（一般 $\\theta$ 下 $(5b)$ 成立）⟹ 代入若干**有理 $\\theta$**，构造 $\\mathcal L$，
   通过七条一致性检查（[consistency_checks.py](consistency_checks.py)）⟹ **FEASIBLE**（带见证）；
3. $\\deg\\ge1$ ⟹ 一般 $\\theta$ 下 $(5b)$ 失败；再在 gcd 表示式的**分母零点**（有限个）上核验
   $\\deg$ 是否仍 $\\ge1$ ⟹ 该图卡"一致地坏"；
4. **注意**：$\deg\ge1$ 只排除"一般 $\theta$"；特殊 $\theta$ 上 gcd 可能**掉落**到 0（此时 $(5b)$ 成立）。
   故本工具在未逐个核验例外点时只报 `UNKNOWN`，不报 `INFEASIBLE`（C4 的 INFEASIBLE 来自
   [attempts/41](41_symbolic_chart_gcd.md) 里手工核验的例外点分析）。

用法：python -u tools/verification/decide_symbolic.py
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

F = Fraction


def Z_from_theta(A, C, L0, q, rows, theta):
    n = len(A)
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    d = n - len(C) - q
    rest = [i for i in range(k) if i not in rows]
    W = [[F(0)] * k for _ in range(d)]
    for a, r0 in enumerate(rows):
        W[a][r0] = F(1)
    idx = 0
    for a in range(d):
        for c in rest:
            W[a][c] = F(theta[idx])
            idx += 1
    return [[sum(Kc[i][t] * W[j][t] for t in range(k)) for j in range(d)] for i in range(n)]


def try_witness(A, C, L0, q, rows, den_expr, max_tries=12):
    """在 $\\deg=0$ 的图卡上找有理 $\\theta$ 使 $(5a)\\wedge(5b)$ 都给见证。"""
    n = len(A)
    d = n - len(C) - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    nv = d * (k - d)
    syms = tuple(sp.symbols(f't0:{nv}')) if nv > 1 else (sp.symbols('t0'),)
    cands = []
    for base in (0, 1, -1, 2, -2, 3):
        for frac in (1, 2):
            cands.append(Fraction(base) if frac == 1 else Fraction(1, 2) * base if base else Fraction(0))
    tested = 0
    for th in cands:
        vals = [th] * nv
        if nv == 0:
            vals = []
        if nv and den_expr is not None:
            try:
                dv = sp.sympify(den_expr).subs(dict(zip(syms, [sp.Rational(v.numerator, v.denominator) for v in vals])))
                if sp.simplify(dv) == 0:
                    continue
            except Exception:                     # noqa: BLE001
                pass
        Z = Z_from_theta(A, C, L0, q, rows, vals)
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Z, q)
        if L is None or not LQ.condA(A, C, L):
            continue
        if TC.analyse(A, C, L)['five_b']:
            CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={th}', verbose=False)
            return L, th
        tested += 1
        if tested >= max_tries:
            break
    return None, None


def decide(A, C, L0, q, verbose=True):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    charts = list(itertools.combinations(range(k), d))
    reports = []
    for rows in charts:
        info = CGA.analyse_chart(A, C, L0, q, rows)
        reports.append((rows, info))
        if verbose:
            print(f'    图卡 {rows}: deg={info.get("deg")}；{info.get("why")}')
    # 若有 deg=0 的图卡，尝试见证
    for rows, info in reports:
        if info.get('deg') == 0:
            L, th = try_witness(A, C, L0, q, rows, info.get('den'))
            if L is not None:
                return 'FEASIBLE', f'图卡 {rows} 上 θ={th} 的见证通过七条检查', L
    # 重要更正（2026-11-03）：deg≥1 只说明"一般 θ 失败"，**不能**说所有 θ 都失败——
    # 在特殊 θ 上 gcd 的 λ 次数可能**掉落**到 0（此时 (5b) 反而成立）。
    # 因此除 C4 那种"例外点也逐个核验过"的情形外，本工具不输出 INFEASIBLE，只报 UNKNOWN。
    if reports and all((info.get('deg') is not None and info.get('deg') >= 1) for _, info in reports):
        return ('UNKNOWN',
                '所有图卡一般 θ 下 deg≥1，但"特殊 θ 上 gcd 掉落"未排除；'
                '需在 gcd 的例外点（分母零点及首项系数零点）逐个核验后才可下 INFEASIBLE（参见 attempts/41 的 C4 处理）',
                None)
    return 'UNKNOWN', '存在无法判定的图卡（deg 缺失等）', None


def main():
    import importlib.util as iu
    print('=== 符号闭环判定 ===')
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    print(f'C4 反例 q={q04}：')
    v, why, w = decide(A4, C4m, L04, q04)
    print(f'  → {v}：{why}')
    spec2 = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m2 = iu.module_from_spec(spec2)
    spec2.loader.exec_module(m2)
    n = len(m2.A)
    for q in (5,):
        print(f'公开例子 q={q}：')
        v, why, w = decide(m2.A, m2.C, m2.L0, q)
        print(f'  → {v}：{why}')
        if w:
            for row in w:
                print('     ', [str(x) for x in row])


if __name__ == '__main__':
    main()
