"""第 4 步的**交叉核对**：在 F_3 上**完全枚举** V（4 维），直接验 (5a)∧(5b)，
与"判定链"（decide_layer_fp.py，枚举 U 并用 C.2/C.3）的结论比较。

取 n=6, p=1：j <= 2 => d >= 4，4 维子空间总数为高斯二项式 [6 choose 4]_3 = 11011（RREF 计数）。
"""
import itertools
import random
import sys

P = 3


def inv(a):
    return pow(a % P, P - 2, P)


def rref(M):
    M = [[x % P for x in r] for r in M]
    r, c = len(M), len(M[0]) if M else 0
    piv, i = [], 0
    for j in range(c):
        t = next((k for k in range(i, r) if M[k][j] % P), None)
        if t is None:
            continue
        M[i], M[t] = M[t], M[i]
        iv = inv(M[i][j])
        M[i] = [(x * iv) % P for x in M[i]]
        for k in range(r):
            if k != i and M[k][j] % P:
                f = M[k][j]
                M[k] = [(a - f * b) % P for a, b in zip(M[k], M[i])]
        piv.append(j)
        i += 1
        if i == r:
            break
    return M, piv


def rank(M):
    return len(rref(M)[1]) if M else 0


def rb(M):
    R, piv = rref(M)
    return [R[i] for i in range(len(piv))]


def mm(X, Y):
    return [[sum(X[i][t] * Y[t][j] for t in range(len(Y))) % P for j in range(len(Y[0]))]
            for i in range(len(X))]


def ptrim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] % P == 0:
        a.pop()
    return a


def pmul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] = (o[i + j] + x * y) % P
    return ptrim(o)


def padd(a, b):
    o = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] = (o[i] + x) % P
    for i, y in enumerate(b):
        o[i] = (o[i] + y) % P
    return ptrim(o)


def pdivmod(a, b):
    a, b = ptrim(a), ptrim(b)
    ib = inv(b[-1])
    q = [0] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        c = (r[-1] * ib) % P
        dd = len(r) - len(b)
        q[dd] = c
        for i, bi in enumerate(b):
            r[i + dd] = (r[i + dd] - c * bi) % P
        r = ptrim(r)
    return q, r


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while not (len(b) == 1 and b[0] == 0):
        _, r = pdivmod(a, b)
        a, b = b, r
    return a


def det_poly(M):
    n = len(M)
    if n == 1:
        return ptrim(M[0][0])
    acc = [0]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        t = pmul(M[0][j], det_poly(sub))
        if j % 2:
            t = [(-c) % P for c in t]
        acc = padd(acc, t)
    return acc


def cond_5a(V, A, C):
    CA = mm(C, A); VA = mm(V, A)
    return rank(VA + V + CA + C) == rank(V + CA + C)


def cond_5b(V, A, C):
    CA = mm(C, A); VA = mm(V, A)
    base = V + CA + C
    r0 = rank(base)
    rows = [(V[i], VA[i]) for i in range(len(V))]
    for r in CA:
        rows.append(([0] * len(r), list(r)))
    for r in C:
        rows.append(([0] * len(r), list(r)))
    g = None
    for rs in itertools.combinations(range(len(rows)), r0):
        for cs in itertools.combinations(range(len(V[0])), r0):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            val = det_poly(M)
            if len(val) == 1 and val[0] == 0:
                continue
            g = val if g is None else pgcd(g, val)
            if len(g) == 1 and g[0] % P:
                return True
    return False if g is None else (len(g) == 1 and g[0] % P != 0)


def main():
    rng = random.Random(2468)
    n, p = 6, 1
    A = [[rng.randrange(P) for _ in range(n)] for _ in range(n)]
    C = [[rng.randrange(P) for _ in range(n)] for _ in range(p)]
    L0 = [[rng.randrange(P) for _ in range(n)]]
    CA = mm(C, A)
    J = rb(C + CA); j = len(J)
    print(f"F_{P}: n={n}, j={j}, rank[C;CA]={j}")
    found = None
    cnt = 0
    for piv in itertools.combinations(range(n), 4):
        free = [c for c in range(n) if c not in piv]
        for vals in itertools.product(range(P), repeat=4 * len(free)):
            M = [[0] * n for _ in range(4)]
            for i, pc in enumerate(piv):
                M[i][pc] = 1
            idx = 0
            for i in range(4):
                for fc in free:
                    M[i][fc] = vals[idx]; idx += 1
            V = rb(M)
            if len(V) != 4:
                continue
            if not all(rank(V + [r]) == 4 for r in L0):
                continue
            rho = rank(V + CA + C) - j
            c = len(V) + j - rank(V + J)
            if (rho, c) != (3, 1):
                continue
            if not cond_5a(V, A, C):
                continue
            cnt += 1
            if found is None and cond_5b(V, A, C):
                found = V
    print(f"  满足类型 (3,1) + (5a) 的 V 共 {cnt} 个；其中 (5b) 成立的：{'有' if found else '无'}")
    print("  => 直接枚举结论：" + ("FEASIBLE" if found else "INFEASIBLE（F_3 上完全）"))


if __name__ == '__main__':
    main()
