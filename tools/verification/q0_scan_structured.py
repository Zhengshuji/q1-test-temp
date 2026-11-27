"""q0_scan_structured.py —— 专家 §Q5 建议的数据表：结构化实例上的零阶差 vs 正阶差

专家 2026-11-03 §Q5 要求为每个实例记录：

| 类别 | 量 |
|---|---|
| 动力学 | 特征值、几何重数、（可得时）Jordan 结构 |
| 可观测性 | $n_0$、$r_1$、相关不变子空间维数 |
| 代数最小 | $q_0$、功能指标 $\\eta_j$ |
| 代数族 | 图卡维数、可行样本数（本脚本用"$q_0$ 阶 $Z$-参数化抽样命中数"近似）|
| 谱条件 | 可达 $h$、$d_{\\rm fin}$、坏 $\\lambda$（有理扫描）|

然后比较"$q_{\\min}=q_0$"与"$q_{\\min}>q_0$"的实例，看是否有结构差异。

用法：python -u tools/verification/q0_scan_structured.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402

F = Fraction


def det_int(M):
    """整数/有理矩阵的行列式（递归展开，矩阵很小）。"""
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    total = F(0)
    for j in range(n):
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        total += ((-1) ** j) * M[0][j] * det_int(minor)
    return total


def charpoly(A):
    """$\\det(\\lambda I-A)$ 的系数（降幂），Faddeev–LeVerrier 的初等实现。"""
    n = len(A)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    M = [row[:] for row in I]
    coeffs = [F(1)]
    for k in range(1, n + 1):
        AM = LQ.mul(A, M)
        c = -sum(AM[i][i] for i in range(n)) / k
        coeffs.append(c)
        M = [[AM[i][j] + (c if i == j else F(0)) for j in range(n)] for i in range(n)]
    return coeffs


def divisors(n):
    n = abs(int(n))
    if n == 0:
        return [0]
    return [d for d in range(1, n + 1) if n % d == 0]


def rational_roots(coeffs):
    from math import lcm
    cs = [F(c) for c in coeffs]
    while cs and cs[0] == 0:
        cs = cs[1:]
    if len(cs) <= 1:
        return []
    m = 1
    for c in cs:
        m = lcm(m, c.denominator)
    ip = [int(c * m) for c in cs]
    an, a0 = abs(ip[0]), abs(ip[-1])
    roots = []
    for p in divisors(a0) or [0]:
        for q_ in divisors(an):
            for s in (1, -1):
                x = F(s * p, q_)
                acc = F(0)
                for c in ip:
                    acc = acc * x + c
                if acc == 0 and x not in roots:
                    roots.append(x)
    return sorted(roots)


def spectrum_note(A):
    coeffs = charpoly(A)
    rr = rational_roots(coeffs)
    n = len(A)
    return f'{len(rr)}/{n} 个特征值有理: {[str(x) for x in rr]}'


def bad_lambdas(A, C, L, h):
    CA = LQ.mul(C, A)
    LA = LQ.mul(L, A)
    vals = [F(k) for k in range(-5, 6)] + [F(a, b) for a in range(-6, 7) for b in (2, 3, 4, 5)]
    out = []
    for lam in sorted(set(vals)):
        Qm = [[lam * L[i][j] - LA[i][j] for j in range(len(A))] for i in range(len(L))]
        Qm = Qm + [list(r) for r in CA] + [list(r) for r in C]
        if LQ.rank(Qm) < h:
            out.append(lam)
    return out


def main():
    families = []
    for n in (5, 6, 7):
        families.append((f'diag-distinct-n{n}', T3.diag_family(n, [0, 1, 2, 3])))
        families.append((f'diag-repeat-n{n}', T3.diag_family(n, [1, 1, 2])))
        families.append((f'jordan-n{n}', T3.jordan_family(n, [1, 2])))
    rows = []
    for name, A in families:
        n = len(A)
        for p in (2, 3):
            if p >= n:
                continue
            seed_c = sum(ord(ch) for ch in name) * 13 + p * 17
            import random
            rngC = random.Random(seed_c)
            C = None
            for _try in range(60):
                cand = [[F(rngC.randrange(2)) for _ in range(n)] for _ in range(p)]
                if LQ.rank(cand) != p:
                    continue
                if LQ.rank(T3.obs_matrix(A, cand)) != n:
                    continue
                C = cand
                break
            if C is None:
                continue
            for r in (1, 2):
                if p + r > n:
                    continue
                L0 = T3.pick_L0(A, C, r, seed=sum(ord(ch) for ch in name) * 7 + p * 31 + r)
                if L0 is None:
                    continue
                O = T3.obs_matrix(A, C)
                if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                    continue
                q0 = Q0.eta_and_q0(A, C, L0)[0]
                CA = LQ.mul(C, A)
                r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
                seed_L = sum(ord(ch) for ch in name) * 11 + q0 * 29
                cands = ZG.sample_L_at_order(A, C, L0, q0, 60, seed=seed_L)
                hs, dfs, bad, feas = set(), set(), set(), 0
                for L in cands:
                    h, s, m, d_fin = T3.fast_dfin(A, C, L)
                    hs.add(h)
                    dfs.add(d_fin)
                    if d_fin == 0:
                        feas += 1
                    else:
                        for lam in bad_lambdas(A, C, L, h)[:3]:
                            bad.add(lam)
                rows.append(dict(family=name, n=n, p=p, r=r, q0=q0, r1=r1,
                                 spec=spectrum_note(A), adm=len(cands),
                                 hs=sorted(hs), dfs=sorted(dfs), feas=feas,
                                 bad=sorted(bad)))
    print(f"{'family':18s} {'n':>2s} {'p':>2s} {'r':>2s} {'q0':>3s} {'r1':>3s} "
          f"{'adm':>4s} {'(5b)':>4s} {'h 取值':>12s} {'d_fin 取值':>12s}  谱")
    for x in rows:
        print(f"{x['family']:18s} {x['n']:>2d} {x['p']:>2d} {x['r']:>2d} {x['q0']:>3d} {x['r1']:>3d} "
              f"{x['adm']:>4d} {x['feas']:>4d} {str(x['hs']):>12s} {str(x['dfs']):>12s}  {x['spec']}")
    eq = [x for x in rows if x['feas'] > 0]
    gt = [x for x in rows if x['adm'] > 0 and x['feas'] == 0]
    print(f'\nq0 阶可行（q_min=q0）{len(eq)} 个；q0 阶不可行（q_min>q0 或未知）{len(gt)} 个；'
          f'无代数样本 {len(rows) - len(eq) - len(gt)} 个')
    print('\n正阶差实例的 h 取值：', [x['hs'] for x in gt])
    print('零阶差实例的 h 取值：', [x['hs'] for x in eq[:12]])


if __name__ == '__main__':
    main()
