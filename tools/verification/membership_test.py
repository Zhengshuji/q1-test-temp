"""membership_test.py —— $z\\in\\operatorname{im}\\psi$ 的**精确**判定（B.18c 的实施）

**判据**：$z\\in\\operatorname{im}\\psi=\\bigcup_\\lambda(\\lambda I-A)V$ $\\iff$ $\\exists\\lambda$：线性系统
$(\\lambda B_V-A B_V)u=z$ 相容 $\\iff$ 增广铅笔 $[\\lambda B_V-A B_V\\mid z]$（$n\\times(d_V+1)$）的**全部**
$(d_V+1)$ 阶子式在某个 $\\lambda$ 同时为零 $\\iff$ 这些子式的 gcd 有**正次数**（或有子式恒为零且其余相容）。

**为什么必须这样做**：只在有理 $\\lambda$ 上取样会漏掉**代数** $\\lambda$（本项目已两次踩坑）。

本脚本：
1. 复检上一轮那个 $n=6$ 实例的 12 个候选——用精确判据看它们是否真的落在 $\\operatorname{im}\\psi$；
2. 在随机 $p=r=1$ 实例上，检验"$d=1$ 时 $(5b)$ 失败 $\\iff z\\in\\operatorname{im}\\psi$"（B.18c 第 2 条）。

用法：python -u tools/verification/membership_test.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def in_im_psi(A, C, z):
    """z ∈ ⋃_λ (λI−A)V ? 精确（子式 gcd）。返回 (成员?, gcd 次数)。"""
    n = len(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    dV = len(V[0]) if (V and V[0]) else 0
    if dV == 0:
        return False, None
    As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
    Bs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in V])
    zs = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in z])
    M = (lam * Bs - As * Bs).row_join(zs)      # n × (dV+1)
    k = dV + 1
    mins = []
    allzero = True
    for rs in itertools.combinations(range(n), k):
        m = sp.expand(M[list(rs), :].det())
        if m != 0:
            allzero = False
            mins.append(sp.Poly(m, lam))
    if allzero:
        return True, None
    g = mins[0]
    for mm in mins[1:]:
        g = sp.gcd(g, mm)
    deg = sp.degree(g.as_expr(), lam)
    return (deg > 0), deg


def main():
    rng = random.Random(20261104)
    st = Counter()
    # ===== 1) 复检上一轮的诊断实例（n=6，12 个候选）=====
    print('=== 1) 精确判据复检：d=1 时 (5b) 失败是否等于 z ∈ im ψ ===')
    for trial in range(60):
        n = rng.choice([4, 5, 6])
        p = r = 1
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        O = QR.observability_matrix(A, C)
        if LQ.rank(O) != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (V and V[0] and K and K[0]):
            continue
        dK = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        q = n - 2                       # d = 1
        if q < q0:
            continue
        d = 1
        for _ in range(4):
            coef = [F(rng.randrange(-3, 4)) for _ in range(dK)]
            z = [sum(K[i][t] * coef[t] for t in range(dK)) for i in range(n)]
            if all(x == 0 for x in z):
                continue
            Z = [[z[i]] for i in range(n)]
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                st['不可容许（跳过）'] += 1
                continue
            ok, _ = OT.observability_ok(A, C, L)
            fails = not ok
            member, deg = in_im_psi(A, C, z)
            st['样本'] += 1
            if fails == member:
                st['一致'] += 1
            else:
                st['不一致'] += 1
                if st['不一致'] <= 5:
                    print(f'  不一致：失败={fails}，z∈imψ={member}（gcd 次数 {deg}）')
    print('统计：', dict(st))
    print('  一致 = "(5b) 失败" ⟺ "z ∈ im ψ"（B.18c 第 2 条）')




def whole_family_d1():
    """d=1 的整族检验：K 中的随机 z 上，(5a) 可容许 与 z∈im ψ 的列联表。"""
    import collections
    rng = random.Random(4242)
    st = Counter()
    print('\n=== 2) d=1 的整族检验：可容许 vs 成员 ===')
    for trial in range(40):
        n = rng.choice([5, 6, 7])
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        O = QR.observability_matrix(A, C)
        if LQ.rank(O) != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        dK = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        q = n - 2
        if q < q0:
            continue
        for _ in range(6):
            coef = [F(rng.randrange(-3, 4)) for _ in range(dK)]
            z = [sum(K[i][t] * coef[t] for t in range(dK)) for i in range(n)]
            if all(x == 0 for x in z):
                continue
            Z = [[z[i]] for i in range(n)]
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None:
                continue
            admissible = LQ.condA(A, C, L)
            member, deg = in_im_psi(A, C, z)
            st[f'可容许={admissible}, 成员={member}'] += 1
    print('列联表：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')
    bad = st['可容许=True, 成员=False']
    print(f'\n可容许但**不**在 im ψ 中的候选数 = {bad}（若为 0，则 d=1 上没有可行候选）')


if __name__ == '__main__':
    main()
    whole_family_d1()
