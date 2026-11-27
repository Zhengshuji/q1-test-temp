#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rp_k_omega_check.py -- k=omega 的 RP 判定的算例核验（验证 != 证明）

两件事：
  (1) 可行情形（k=omega=2, q=3, K∩AK=0）：随机取样点上的行列式因子判据（Smith 路径）
      与"枚举 2-子式 + gcd"路径一致，且样本绝大多数为好；
  (2) 不可行情形（k=omega=2, q=3, K=AK，A|_K 为 swap）：H_A = H M 恒成立，
      铅笔 = H(λI-M)，gcd = det(λI-M) = λ^2-1；所有样本都坏。

定理本身（RP 上界）见 workspace/augmentation_family/attempts/101_rp_k_omega.md；
本脚本只核验：判据实现、两情形的判决、以及"不可行 => 永不接受"的单侧性。
"""
import os
import sys
import random
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for _p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, _p))

import linalg_q as LQ                 # noqa: E402
import poly_smith as PS               # noqa: E402

F = Fraction


def rand_mat(r, c, rng, lo=-3, hi=3):
    return [[F(rng.randint(lo, hi)) for _ in range(c)] for _ in range(r)]


def minor2_poly(H, HA, rows, cols):
    """2x2 minor of lambda H - H_A, 返回系数列表（低次在前）."""
    e = [[[-HA[i][j], H[i][j]] for j in cols] for i in rows]
    # (a0 + a1 λ)(d0 + d1 λ) - (b0 + b1 λ)(c0 + c1 λ)
    a, b, c, d = e[0][0], e[0][1], e[1][0], e[1][1]
    p = [a[0] * d[0], a[0] * d[1] + a[1] * d[0], a[1] * d[1]]
    q = [b[0] * c[0], b[0] * c[1] + b[1] * c[0], b[1] * c[1]]
    out = [p[i] - q[i] for i in range(3)]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pgcd(a, b):
    a, b = list(a), list(b)
    def trim(x):
        while len(x) > 1 and x[-1] == 0:
            x.pop()
        return x
    a, b = trim(a), trim(b)
    while not (len(b) == 1 and b[0] == 0):
        # a mod b
        r = list(a)
        while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
            d = r[-1] / b[-1]
            sh = len(r) - len(b)
            for i in range(len(b)):
                r[sh + i] -= d * b[i]
            r = trim(r)
        a, b = b, r
    if not (len(a) == 1 and a[0] == 0):
        lead = a[-1]
        a = [x / lead for x in a]
    return a


def gcd_degree_by_minors(H, HA):
    import itertools
    q, k = len(H), len(H[0])
    g = None
    for rows in itertools.combinations(range(q), 2):
        for cols in itertools.combinations(range(k), 2):
            m = minor2_poly(H, HA, rows, cols)
            if not (len(m) == 1 and m[0] == 0):
                g = m if g is None else pgcd(g, m)
    if g is None:
        return -1
    while len(g) > 1 and g[-1] == 0:
        g.pop()
    return len(g) - 1 if not (len(g) == 1 and g[0] == 0) else -1


def smith_verdict(H, HA):
    Q = [[[-HA[i][j], H[i][j]] for j in range(len(H[0]))] for i in range(len(H))]
    ok, delta, info = PS.full_col_rank_constant(Q)
    return ok, info


def build_feasible():
    """n=6, p=2, q=3, r=1, k=2, K∩AK=0（自由区）."""
    n = 6
    C = [[F(1) if j == i else F(0) for j in range(n)] for i in range(2)]
    A = [[F(0)] * n for _ in range(n)]
    A[0][2] = F(1)   # 列 3 = e1
    A[1][3] = F(1)   # 列 4 = e2
    A[2][4] = F(1)   # 列 5 = e3
    A[3][5] = F(1)   # 列 6 = e4
    L0 = [[F(1) if j == 4 else F(0) for j in range(n)]]  # e5^T
    NK = [[F(0)] * 2 for _ in range(n)]
    NK[4][0] = F(1)
    NK[5][1] = F(1)
    return A, C, L0, NK


def build_infeasible():
    """n=4, p=1, q=3, r=1, k=2, K=AK（A|_K = swap）."""
    n = 4
    C = [[F(1) if j == 0 else F(0) for j in range(n)]]
    A = [[F(0)] * n for _ in range(n)]
    A[0][3] = F(1)   # 行 1 = e4^T (CA=e4^T)
    A[2][1] = F(1)   # 列 2 = e3
    A[1][2] = F(1)   # 列 3 = e2
    A[3][3] = F(0)
    # A e4 = e1: 列 4 = e1
    A[0][3] = F(1)   # 同时满足行 1 = e4^T? 行 1 的列 4 = 1, 即 CA=e4^T ✓；列 4 = e1 也是 A[0][3]=1 ✓
    L0 = [[F(1) if j == 1 else F(0) for j in range(n)]]  # e2^T
    NK = [[F(0)] * 2 for _ in range(n)]
    NK[1][0] = F(1)  # e2
    NK[2][1] = F(1)  # e3
    return A, C, L0, NK


def sample_H(A, C, L0, NK, rng):
    n = len(A)
    m = 3 - len(L0)          # q=3
    R = rand_mat(m, n, rng)
    L = [r[:] for r in L0] + R
    H = LQ.mul(L, NK)
    HA = LQ.mul(LQ.mul(L, A), NK)
    return L, H, HA


def run(tag, build, rng, trials=20):
    A, C, L0, NK = build()
    n = len(A)
    m = 3 - len(L0)
    good = bad = skipped = 0
    agree = 0
    for _ in range(trials):
        R = rand_mat(m, n, rng)
        L = [r[:] for r in L0] + R
        if LQ.rank([r[:] for r in L]) != 3:
            skipped += 1
            continue
        H = LQ.mul(L, NK)
        HA = LQ.mul(LQ.mul(L, A), NK)
        if LQ.rank([r[:] for r in H]) != 2:
            skipped += 1
            continue
        d = gcd_degree_by_minors(H, HA)
        ok, info = smith_verdict(H, HA)
        if (d == 0) == ok:
            agree += 1
        good += 1 if d == 0 else 0
        bad += 0 if d == 0 else 1
    print(f'[{tag}] tested {good + bad} (skipped {skipped}); good {good}, bad {bad}; '
          f'Smith vs minors agree {agree}/{good + bad}')
    return good, bad, agree


def main():
    rng = random.Random(20261108)
    print('=== k=omega=2, q=3 ===')
    g1, b1, a1 = run('feasible (K∩AK=0)', build_feasible, rng, 20)
    g2, b2, a2 = run('infeasible (K=AK)', build_infeasible, rng, 20)
    assert a1 == g1 + b1 and a2 == g2 + b2, 'Smith 与枚举子式不一致'
    assert g1 > 0, '可行情形没有好样本（取样失败）'
    assert b2 == g2 + b2 and g2 == 0, '不可行情形出现了好样本（判据有问题）'
    print('\n单侧性检查：不可行情形 20 个样本全部为坏 => 算法永不接受 ✓')
    print('可行情形：好样本 > 0 => 随机取样可命中（RP 的 yes 侧）✓')


if __name__ == '__main__':
    main()
