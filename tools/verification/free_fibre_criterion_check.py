#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""free_fibre_criterion_check.py -- 自由区 q=3, omega=2 的判据机器核验

自由区: ker T = 0（K∩A^{-1}K=0），故底部行 (B_1,B_2) 自由；等价地，给定固定的顶块
U_0 (r x k), V_0 (r x k) 与 m = q-r 个自由行，问题是矩阵补全：
  H = [U_0; B_1], H_A = [V_0; B_2],  rank H = 2, ker H ⊆ ker H_A, 铅笔好。

判据（见 attempts/102）:
  E = row(U_0), F_0 = row(V_0), EF = dim(E+F_0)
  (A) EF <= 2 且 m >= 2 - dim E;
  (B) EF=0 => m=3;  EF=1 => m>=2;
      EF=2 => 若 V_0 = λ U_0 则 m>=2；否则（固定铅笔好 或 m>=1）。

本脚本对随机 (U_0,V_0) 逐一核验：预测 FEAS 的实例构造出好点；预测 INFEAS 的实例
要么无 S、要么无 rank-2 H、要么所有可容许样本都坏（后者只是证据，不是证明）。
"""
import os
import sys
import random
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for _p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, _p))

import linalg_q as LQ                 # noqa: E402

F = Fraction


def rank(M):
    return LQ.rank([list(map(F, r)) for r in M]) if M else 0


def pgcd(a, b):
    def trim(x):
        x = list(x)
        while len(x) > 1 and x[-1] == 0:
            x.pop()
        return x
    a, b = trim(a), trim(b)
    while not (len(b) == 1 and b[0] == 0):
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


def minors2(H, HA):
    q, k = len(H), len(H[0])
    out = []
    for rows in itertools.combinations(range(q), 2):
        for cols in itertools.combinations(range(k), 2):
            e = [[[-HA[i][j], H[i][j]] for j in cols] for i in rows]
            p = [e[0][0][0] * e[1][1][0],
                 e[0][0][0] * e[1][1][1] + e[0][0][1] * e[1][1][0],
                 e[0][0][1] * e[1][1][1]]
            z = [e[0][1][0] * e[1][0][0],
                 e[0][1][0] * e[1][0][1] + e[0][1][1] * e[1][0][0],
                 e[0][1][1] * e[1][0][1]]
            m = [p[i] - z[i] for i in range(3)]
            if not (len(m) == 1 and m[0] == 0):
                out.append(m)
    return out


def good(H, HA):
    ms = minors2(H, HA)
    if not ms:
        return False
    g = ms[0]
    for m in ms[1:]:
        g = pgcd(g, m)
    while len(g) > 1 and g[-1] == 0:
        g.pop()
    return len(g) == 1 and g[0] != 0


def fixed_pencil_good(U, V):
    return good(U, V) if U else (rank(V) == 2)


def proportional(U, V, r, k):
    """V = lambda U for some lambda?"""
    lam = None
    for i in range(r):
        for j in range(k):
            if U[i][j] != 0:
                cand = V[i][j] / U[i][j]
                if lam is None:
                    lam = cand
                elif cand != lam:
                    return False
            elif V[i][j] != 0:
                return False
    return lam is not None


def pencil_rank_at(U, V, lam):
    M = [[lam * U[i][j] - V[i][j] for j in range(len(U[0]) if U else len(V[0]))] for i in range(len(U))]
    return rank(M) if M else 0


def normal_rank(U, V):
    if not U and not V:
        return 0
    k = len(U[0]) if U else len(V[0])
    best = 0
    for lam in (F(0), F(1), F(-1), F(2), F(-2), F(3), F(5), F(7)):
        best = max(best, pencil_rank_at(U, V, lam))
    return best


def predict(U, V, r, k):
    E = rank(U) if U else 0
    EF = rank(U + V) if (U or V) else 0
    m = 3 - r
    if EF > 2 or m < 2 - E:
        return False
    rho = normal_rank(U, V)
    if rho == 0:
        return m == 3
    if rho == 1:
        return m >= 2
    # rho == 2
    if proportional(U, V, r, k):
        return m >= 2
    if fixed_pencil_good(U, V):
        return True
    return m >= 1


def rv(k, rng):
    return [F(rng.randint(-2, 2)) for _ in range(k)]


def build_basis(U, V, k, rng):
    EF = rank(U + V) if (U or V) else 0
    if EF == 0:
        while True:
            a, b = rv(k, rng), rv(k, rng)
            if rank([a, b]) == 2:
                return [a, b]
    if EF == 1:
        u = LQ.rref([x[:] for x in U] + [x[:] for x in V])[0][0]
        while True:
            w = rv(k, rng)
            if rank([u, w]) == 2:
                return [u, w]
    if EF == 2:
        rk = LQ.rref([x[:] for x in U] + [x[:] for x in V])[0]
        return [rk[0], rk[1]]
    return None


def build_fibre(U, V, k, rng):
    """构造 S、H；返回 (H, basis, m) 或 None（无 S / 无 rank-2 H）."""
    r = len(U)
    m = 3 - r
    E = rank(U) if U else 0
    basis = build_basis(U, V, k, rng)
    if basis is None:
        return None
    need = max(0, 2 - E)
    if need > m:
        return None
    rows = [x[:] for x in U]
    for _ in range(need):
        while True:
            c = [F(rng.randint(-2, 2)) for _ in range(2)]
            cand = [sum(c[t] * basis[t][j] for t in range(2)) for j in range(k)]
            if rank(rows + [cand]) > rank(rows):
                break
        rows.append(cand)
    for _ in range(m - need):
        c = [F(rng.randint(-2, 2)) for _ in range(2)]
        rows.append([sum(c[t] * basis[t][j] for t in range(2)) for j in range(k)])
    if rank(rows) != 2:
        return None
    if rank(rows + [x[:] for x in V]) != 2:
        return None
    return rows, basis, m


def sample_good(U, V, k, rng, tries=80):
    built = build_fibre(U, V, k, rng)
    if built is None:
        return None  # 无 S 或无 rank-2 H
    H, basis, m = built
    for _ in range(tries):
        B2 = []
        for _ in range(m):
            c = [F(rng.randint(-2, 2)) for _ in range(2)]
            B2.append([sum(c[t] * basis[t][j] for t in range(2)) for j in range(k)])
        HA = [x[:] for x in V] + B2
        if rank(H + HA) != 2:
            continue
        if good(H, HA):
            return True
    return False


def main():
    rng = random.Random(20261108)
    print('=== 自由区 q=3, omega=2 判据核验 ===')
    ok = 0
    bad = 0
    for k in (2, 3):
        for r in (0, 1, 2):
            n_feas = n_inf = 0
            for _ in range(200):
                U = [rv(k, rng) for _ in range(r)]
                V = [rv(k, rng) for _ in range(r)]
                pred = predict(U, V, r, k)
                res = sample_good(U, V, k, rng)
                if pred:
                    assert res is True, f'predicted FEAS but no good point: k={k} r={r} U={U} V={V}'
                    n_feas += 1
                else:
                    # 无 S / 无 rank-2 H / 所有样本坏
                    assert res is not True, f'predicted INFEAS but found good: k={k} r={r} U={U} V={V}'
                    n_inf += 1
                ok += 1
            print(f'  k={k}, r={r}, m={3-r}: FEAS {n_feas}, INFEAS {n_inf}')
    print(f'ALL {ok} instances consistent with the criterion')


if __name__ == '__main__':
    main()
