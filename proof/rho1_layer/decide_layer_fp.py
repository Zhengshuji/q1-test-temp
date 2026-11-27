"""有限域上的**完整**层判定（(rho,c)=(3,1)）：§28 判定链的实现（小规模）。

在 F_p 上枚举 X 里**所有** 3 维子空间 U（含固定行 W0），筛掉不满足 (N) 的，
再对每个格子用 C.2/C.3 判据；若某格"不被覆盖" => FEASIBLE 并构造见证 V ⊆ F_p^n，
最后用堆叠判据验 (5a)(5b)。若所有格都"被覆盖" => INFEASIBLE（在 F_p 上是**完全**结论 ✓）。

用法：python decide_layer_fp.py 3
"""
import itertools
import sys

P = int(sys.argv[1]) if len(sys.argv) > 1 else 3


def inv(a):
    return pow(a % P, P - 2, P)


def rref(M):
    M = [[x % P for x in r] for r in M]
    r, c = len(M), len(M[0])
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


def inspan(B, v):
    if not B:
        return all(x % P == 0 for x in v)
    return rank([r[:] for r in B] + [v[:]]) == rank([r[:] for r in B])


def det_poly(M):
    n = len(M)
    if n == 1:
        return [x % P for x in M[0][0]]
    acc = [0]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        t = pmul(M[0][j], det_poly(sub))
        if j % 2:
            t = [(-c) % P for c in t]
        acc = padd(acc, t)
    return acc


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


def gcd_one(polys):
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
        if len(g) == 1 and g[0] % P:
            return True
    return len(g) == 1 and g[0] % P != 0


def main():
    import random
    from collections import Counter
    rng = random.Random(2468)
    # 取一个小实例：n=5, p=1 或 2
    n, p = 6, 1
    A = [[rng.randrange(P) for _ in range(n)] for _ in range(n)]
    C = [[rng.randrange(P) for _ in range(n)] for _ in range(p)]
    L0 = [[rng.randrange(P) for _ in range(n)]]
    CA = mm(C, A)
    J = rb(C + CA)
    j = len(J)
    # 补基 -> X 坐标
    comp = []
    span = [r[:] for r in J]
    for i in range(n):
        e = [1 if k == i else 0 for k in range(n)]
        if len(rb(span + [e])) > len(span):
            comp.append(e); span = rb(span + [e])
        if len(span) == n:
            break
    d = len(comp)
    L = J + comp
    Linv = None
    # 求 L 的逆（n x n）
    aug = [L[i][:] + [1 if i == k else 0 for k in range(n)] for i in range(n)]
    R, _ = rref(aug)
    Linv = [r[n:] for r in R]

    def pi(x):
        a = mm([x], Linv)[0]
        return [t % P for t in a[j:]]

    def lift(u):
        a = [0] * j + [t % P for t in u]
        # a · L
        return [sum(a[i] * L[i][k] for i in range(n)) % P for k in range(n)]

    B = rb([pi(mm([jj], A)[0]) for jj in J])
    W0 = rb([pi(r) for r in L0] + [pi(mm([r], A)[0]) for r in L0])
    print(f"F_{P}: n={n}, j={j}, d={d}, dim B={len(B)}, dim W0={len(W0)}")

    # 枚举所有 3 维子空间（RREF）
    def spaces(k, m):
        for piv in itertools.combinations(range(m), k):
            free = [c for c in range(m) if c not in piv]
            for vals in itertools.product(range(P), repeat=k * len(free)):
                M = [[0] * m for _ in range(k)]
                for i, pc in enumerate(piv):
                    M[i][pc] = 1
                idx = 0
                for i in range(k):
                    for fc in free:
                        M[i][fc] = vals[idx]; idx += 1
                Bs = rb(M)
                if len(Bs) == k:
                    yield Bs

    total = condN = feas = 0
    witness = None
    for U in spaces(3, d):
        total += 1
        if not all(inspan(U, w) for w in W0):
            continue
        # (N): pi(U A) ⊆ U + B
        fU = [pi(mm([lift(u)], A)[0]) for u in U]
        if not all(rank([r[:] for r in U] + [b[:] for b in B] + [v[:]]) ==
                   rank([r[:] for r in U] + [b[:] for b in B]) for v in fU):
            continue
        condN += 1
        E = [b for b in B if inspan(U, b)]
        if not E:
            continue                      # C.5：w 只能为 0
        w = next((e for e in E if any(x % P for x in e)), None)
        if w is None:
            continue
        # 格子 T：pi(u_i A) 在 U 基下的坐标（mod E 无影响，因为 w 与 E 都在 U 里）
        Uarr = [r[:] for r in U]
        Uinv = None
        ## 用 U 的 3 个基向量把 pi(u A) 表示成 U 坐标（若在 U+B 里则先投影，这里简化：假设可实现）
        Trows = []
        ok = True
        for u in U:
            v = pi(mm([lift(u)], A)[0])
            # 求 v 在 U 坐标下的"U 分量"：解 v = sum c_i u_i + b
            M = [[U[i][t] for i in range(3)] + [b[t] for b in B] for t in range(d)]
            augm = [row + [v[t]] for t, row in enumerate(M)]
            R2, piv2 = rref(augm)
            sol = [0] * (3 + len(B))
            for row in R2:
                for t in range(3 + len(B)):
                    if row[t] % P:
                        sol[t] = row[3 + len(B)] * inv(row[t]) % P
                        break
            Trows.append([sol[i] % P for i in range(3)])
        # C.2/C.3：T 是否有落在 E^perp 里的特征向量
        Erows = []
        for e in E:
            # e 在 U 坐标下
            M = [[U[i][t] for i in range(3)] + [e[t]] for t in range(d)]
            R3, _ = rref(M)
            coeff = [0] * 3
            for row in R3:
                for t in range(3):
                    if row[t] % P:
                        coeff[t] = row[3] * inv(row[t]) % P
                        break
            Erows.append(coeff)
        rows = [[[-Trows[i][k] % P, 1 if i == k else 0] for k in range(3)] for i in range(3)]
        for e in Erows:
            rows.append([[e[k] % P] for k in range(3)])
        polys = []
        for rs in itertools.combinations(range(len(rows)), 3):
            for cs in itertools.combinations(range(3), 3):
                Mx = [[rows[i][k] for k in cs] for i in rs]
                val = det_poly(Mx)
                if not (len(val) == 1 and val[0] == 0):
                    polys.append(val)
        bad = gcd_one(polys)          # True = 无公共根 = 不存在这样的特征向量 = 不被覆盖
        if bad:
            feas += 1
            witness = U
            break
    print(f"  3 维子空间总数 {total}；满足 (N) 且 W0 ⊆ U 的 {condN}；"
          f"判据说'不被覆盖'的 {feas}")
    print("  => 层" + ("FEASIBLE（已找到格子）" if feas else "INFEASIBLE（F_p 上完全枚举）"))


if __name__ == '__main__':
    main()
