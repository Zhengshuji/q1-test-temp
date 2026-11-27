# -*- coding: utf-8 -*-
"""
verify_witness_independent.py -- ⭐⭐⭐ 用**完全独立**的实现复核见证

独立性：
  · 不 import 项目的任何库（exact_count_thm7 / linalg_exact 都不用）
  · 自带 Fraction Gauss 消元求秩、自带矩阵乘法
  · 自带多项式算术 + 子式 gcd（(5b) 的充分必要判据）
  · 另外用 30 个随机有理 λ 直接算秩做交叉验证

判据 (5b)：rank[λL−LA; CA; C] ≡ r0 := rank[L;CA;C]
  ⟺ 全部 r0 阶子式的 gcd 是**非零常数**
"""
import json
import os
import random
from fractions import Fraction as Fr
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
WIT = os.path.join(HERE, "witness_caseII_parallel_YES.json")


# ---------- 独立线性代数 ----------
def rank(M):
    if not M:
        return 0
    A = [[Fr(x) for x in row] for row in M]
    R, C = len(A), len(A[0])
    r = 0
    for c in range(C):
        p = None
        for i in range(r, R):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(R):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(C)]
        r += 1
        if r == R:
            break
    return r


def matmul(X, Y):
    assert X and Y and len(X[0]) == len(Y), "维数不匹配"
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]


def vstack(*Ms):
    out = []
    for M in Ms:
        out.extend([list(r) for r in M])
    return out


# ---------- 独立多项式算术（系数列表，低次在前）----------
def P_trim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q


def P_add(a, b):
    n = max(len(a), len(b))
    return P_trim([(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0))
                   for i in range(n)])


def P_sub(a, b):
    n = max(len(a), len(b))
    return P_trim([(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0))
                   for i in range(n)])


def P_mul(a, b):
    if P_trim(a) == [Fr(0)] or P_trim(b) == [Fr(0)]:
        return [Fr(0)]
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return P_trim(r)


def P_divmod(a, b):
    a = P_trim(a)
    b = P_trim(b)
    if b == [Fr(0)]:
        raise ZeroDivisionError
    db = len(b) - 1
    q = [Fr(0)] * max(1, len(a) - db)
    while len(a) - 1 >= db and a != [Fr(0)]:
        d = len(a) - 1 - db
        co = a[-1] / b[-1]
        q[d] += co
        for i in range(len(b)):
            a[d + i] -= co * b[i]
        a = P_trim(a)
    return P_trim(q), a


def P_gcd(a, b):
    a, b = P_trim(a), P_trim(b)
    while b != [Fr(0)]:
        _, r = P_divmod(a, b)
        a, b = b, r
    if len(a) > 1:
        lc = a[-1]
        a = [x / lc for x in a]
    return a


def P_det(M, k):
    if k == 1:
        return [Fr(x) for x in M[0][0]]
    tot = [Fr(0)]
    for j in range(k):
        sub = [row[:j] + row[j + 1:] for row in M[1:]]
        d = P_det(sub, k - 1)
        pr = P_mul(M[0][j], d)
        tot = P_add(tot, pr) if j % 2 == 0 else P_sub(tot, pr)
    return P_trim(tot)


# ---------- 主验证 ----------
def main():
    with open(WIT, encoding="utf-8") as f:
        w = json.load(f)
    A = [[Fr(x) for x in r] for r in w["A"]]
    C = [[Fr(x) for x in r] for r in w["C"]]
    L = [[Fr(x) for x in r] for r in w["L0"]]
    n = w["n"]
    p = len(C)
    r = len(L)

    print("=== 独立复核（全新实现，不依赖项目库）===\n")
    print("n=%d p=%d r=%d  q0(记录)=%d  d_CA(记录)=%d"
          % (n, p, r, w["q0"], w["d_CA"]))
    print()

    CA = matmul(C, A)
    LA = matmul(L, A)
    W = vstack(C, CA)

    ok = {}
    ok["H1 rank C = p"] = (rank(C) == p)
    ok["H2 rank L0 = r"] = (rank(L) == r)
    ok["H3 rank [L0;C] = r+p"] = (rank(vstack(L, C)) == r + p)

    def obs(M, A, n):
        rows = [list(x) for x in M]
        cur = [list(x) for x in M]
        for _ in range(n - 1):
            cur = matmul(cur, A)
            rows.extend(cur)
        return rows

    OL, OC = obs(L, A, n), obs(C, A, n)
    ok["H4 row(O_L0) ⊆ row(O_C)"] = (rank(vstack(OL, OC)) == rank(OC))

    r0 = rank(vstack(L, CA, C))
    r5a = rank(vstack(LA, L, CA, C))
    ok["(5a)"] = (r5a == r0)

    # (5b)：全部 r0 阶子式的 gcd 必须是非零常数
    m, nc = len(vstack(L, CA, C)), n
    # 铅笔 P：前 r 行 = −LA + λL；其余 = 常数
    P = []
    for i in range(m):
        row = []
        for j in range(nc):
            if i < r:
                row.append([-LA[i][j], L[i][j]])
            else:
                base = vstack(L, CA, C)[i]
                row.append([base[j]])
        P.append(row)
    minors = []
    for rows in combinations(range(m), r0):
        for cols in combinations(range(nc), r0):
            sub = [[P[i][j] for j in cols] for i in rows]
            g = P_det(sub, r0)
            if g != [Fr(0)]:
                minors.append(g)
    G = minors[0]
    for q in minors[1:]:
        G = P_gcd(G, q)
        if len(G) == 1:
            break
    nz = any(x != 0 for x in G)
    ok["(5b) gcd 为常数"] = (len(P_trim(G)) == 1 and nz)

    # 交叉验证：30 个随机有理 λ 直接算秩
    rng = random.Random(7)
    bad = 0
    for _ in range(30):
        lam = Fr(rng.randint(-20, 20), rng.randint(1, 7))
        M = []
        for i in range(r):
            M.append([lam * L[i][j] - LA[i][j] for j in range(nc)])
        M = vstack(M, CA, C)
        if rank(M) != r0:
            bad += 1
    ok["(5b) 30 个随机 λ 均 = r0"] = (bad == 0)

    # 情形 II / 平行 / 非退化 / T5a
    N = None
    # 独立求 ker(W) 的基
    def ker_basis(M):
        A2 = [[Fr(x) for x in row] for row in M]
        R, C2 = len(A2), len(A2[0])
        piv = []
        r_ = 0
        for c in range(C2):
            p_ = None
            for i in range(r_, R):
                if A2[i][c] != 0:
                    p_ = i
                    break
            if p_ is None:
                continue
            A2[r_], A2[p_] = A2[p_], A2[r_]
            pv = A2[r_][c]
            A2[r_] = [x / pv for x in A2[r_]]
            for i in range(R):
                if i != r_ and A2[i][c] != 0:
                    f = A2[i][c]
                    A2[i] = [A2[i][j] - f * A2[r_][j] for j in range(C2)]
            piv.append(c)
            r_ += 1
            if r_ == R:
                break
        free = [c for c in range(C2) if c not in piv]
        basis = []
        for fc in free:
            v = [Fr(0)] * C2
            v[fc] = Fr(1)
            for i, pc in enumerate(piv):
                v[pc] = -A2[i][fc]
            basis.append(v)
        return basis

    W2 = vstack(C, CA)
    B = ker_basis(W2)
    dCA = len(B)
    ok["情形 II: d_CA ≥ q0"] = (dCA >= w["q0"])
    ok["d_CA 与记录一致"] = (dCA == w["d_CA"])

    Nb = [[B[j][i] for j in range(dCA)] for i in range(n)]   # n×d
    H = matmul(L, Nb)
    ok["T5a: rank H < q0"] = (rank(H) < w["q0"])
    ok["rank H 与记录一致"] = (rank(H) == w["rankH"])

    def pv(v):
        return [sum(v[i] * Nb[i][j] for i in range(n)) for j in range(dCA)]

    pL = [pv(L[i]) for i in range(r)]
    pLA = [pv(LA[i]) for i in range(r)]
    ok["平行: rank[π(L0);π(L0A)] ≤ 1"] = (rank(pL + pLA) <= 1)
    ok["非退化: π(L0) ≠ 0"] = any(any(x != 0 for x in w2) for w2 in pL)

    print("r0 = rank[L;CA;C] = %d ；rank[LA;L;CA;C] = %d" % (r0, r5a))
    print("(5b) 子式个数 = %d ；gcd 次数 = %d ；gcd = %s"
          % (len(minors), len(G) - 1, [str(x) for x in G]))
    print()
    allok = True
    for k, v in ok.items():
        print("  %-34s : %s" % (k, "✓" if v else "**✗**"))
        allok = allok and v
    print()
    if allok:
        print("⟹⟹⟹ **见证经完全独立实现复核通过** ⟹")
        print("    情形 II + 非退化平行 + H1–H4 ∧ (5a) ∧ (5b) 全部成立")
        print("    ⟹ **c6 / c6′ （平行 ⟹ NO）为假** ⟹ 情形 II 可为 YES")
    else:
        print("⟹ **复核未通过** —— 见证有误，需撤回")


if __name__ == "__main__":
    main()
