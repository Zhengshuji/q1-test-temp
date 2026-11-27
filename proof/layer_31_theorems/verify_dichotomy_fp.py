"""专家 Step 3 的执行：在**完整枚举**（不是抽样 ✗）下检验"二分猜想"。

在一个具体实例上，枚举 X 里**所有** 3 维子空间（在 F_p 上 Grassmannian 有限 ✓），
筛出满足 A1–A3、A6 的那些（结构可允许），再看是否存在 mu >= 1 的、以及是否存在"未覆盖"的格子。

二分猜想：结构可允许的层要么没有 mu>=1 的格子，要么有未覆盖的格子。

实例：§55 的"好"实例（n=6、W 上是不约三次友矩阵、C=(-1,-2,0,0,0,-1)、V=<e1,e2,e3,e5>），
      模 p 后在 F_p 上做完整枚举。**结论只对 F_p 成立** ✗（不能直接推 Q ✗）。
"""
import itertools
import sys

P = int(sys.argv[1]) if len(sys.argv) > 1 else 3


def rref(M):
    M = [[x % P for x in r] for r in M]
    r, c = len(M), len(M[0]) if M else 0
    piv, i = [], 0
    for j in range(c):
        t = next((k for k in range(i, r) if M[k][j] % P), None)
        if t is None:
            continue
        M[i], M[t] = M[t], M[i]
        iv = pow(M[i][j] % P, P - 2, P)
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
    assert len(X[0]) == len(Y)
    return [[sum(X[i][t] * Y[t][j] for t in range(len(Y))) % P for j in range(len(Y[0]))]
            for i in range(len(X))]


def inv(A):
    n = len(A)
    aug = [A[i][:] + [1 if i == k else 0 for k in range(n)] for i in range(n)]
    R, piv = rref(aug)
    assert len(piv) == n and piv == list(range(n))
    return [r[n:] for r in R]


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
    return ptrim(acc)


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
    ib = pow(b[-1] % P, P - 2, P)
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


def gcd_is_one(polys):
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
        if len(g) == 1 and g[0] % P:
            return True
    return len(g) == 1 and g[0] % P != 0


def main():
    n = 6
    # §55 的"好"实例，模 P
    A = [[0] * n for _ in range(n)]
    A[0][1] = 1; A[1][2] = 1; A[2][0] = 3 % P; A[2][1] = 2 % P; A[2][2] = 1 % P   # 友矩阵 x^3 - x^2 - 2x - 3
    A[3][3] = 1
    A[4][5] = 1
    A[5][0] = 1; A[5][4] = 1
    C = [[(-1) % P, (-2) % P, 0, 0, 0, (-1) % P]]
    L0 = [[0, 0, 0, 0, 1, 0]]
    CA = mm(C, A)
    J = rb(C + CA)
    j = len(J)
    K = []
    span = [r[:] for r in J]
    for i in range(n):
        e = [1 if t == i else 0 for t in range(n)]
        if rank(span + [e]) > len(span):
            K.append(e); span = rb(span + [e])
        if len(span) == n:
            break
    d = len(K)
    Lmat = J + K
    Linv = inv(Lmat)

    def pi(x):
        c = mm([x], Linv)[0]
        return c[j:]

    def lift(u):
        a = [0] * j + list(u)
        return [sum(a[i] * Lmat[i][t] for i in range(n)) % P for t in range(n)]

    B = rb([pi(mm([jj], A)[0]) for jj in J])
    u0 = pi(L0[0])
    u0A = pi(mm([L0[0]], A)[0])
    print(f"F_{P}: n={n}, j={j}, d={d}, dim B={len(B)}, dim<u0,u0A>={rank([u0, u0A]) if any(u0) or any(u0A) else 0}")

    # 枚举 G(3,d)
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

    tot = adm = with_mu = not_cov = 0
    for U in spaces(3, d):
        tot += 1
        # A2、A3
        if any(rank(U + [x]) != 3 for x in [u0, u0A] if any(x)):
            continue
        # A6: (N)
        fU = [pi(mm([lift(u)], A)[0]) for u in U]
        if not all(rank(U + B + [v]) == rank(U + B) for v in fU):
            continue
        adm += 1
        # μ = dim(B ∩ U)：维数公式（§61 的教训：不能数"基向量里有多少个落在 U 里" ✗）
        mu_ = len(B) + 3 - rank([r[:] for r in B] + [r[:] for r in U])
        if mu_ == 0:
            continue
        # B ∩ U 的一组基（解 sum c_i B_i = sum a_j U_j）
        E = []
        _rows = [[B[i][k] for i in range(len(B))] + [(-U[j][k]) % P for j in range(len(U))]
                 for k in range(d)]
        _R, _ = rref(_rows)
        _free = [c for c in range(len(B) + 3) if c not in _R and False]
        # 用零空间：解 _rows · z = 0，取 z 的前 len(B) 部分作 B∩U 的元素
        _ns = []
        _piv = []
        _M = [r[:] for r in _rows]
        _MR, _pivs = rref(_M)
        _piv = _pivs
        _cols = len(B) + 3
        for _f in [c for c in range(_cols) if c not in _piv]:
            z = [0] * _cols
            z[_f] = 1
            for _i, _pc in enumerate(_piv):
                z[_pc] = (-_MR[_i][_f]) % P
            _ns.append(z)
        for z in _ns:
            v = [sum(z[i] * B[i][k] for i in range(len(B))) % P for k in range(d)]
            if any(v):
                E.append(v)
        E = rb(E)
        if len(E) != mu_:
            E = E[:mu_]
        with_mu += 1
        # 格子判据：解 T
        fU2 = [pi(mm([lift(u)], A)[0]) for u in U]
        nunk = 9 + 3 * len(B)
        eqs = []
        for i in range(3):
            for k in range(d):
                row = [0] * nunk + [fU2[i][k]]
                for jj in range(3):
                    row[jj * 3 + i] = U[jj][k]
                for t in range(len(B)):
                    row[9 + i * len(B) + t] = B[t][k]
                eqs.append(row)
        R, piv2 = rref(eqs)
        sol = [0] * nunk
        for row in R:
            p_ = next((jj for jj in range(nunk) if row[jj] != 0), None)
            if p_ is None:
                continue
            sol[p_] = row[nunk] * inv([[row[p_]]])[0][0] % P
        T = [[sol[jj * 3 + i] for jj in range(3)] for i in range(3)]
        # E 的生成元在 U 坐标下
        Erows = []
        for er in E:
            ER, _ = rref([[U[jj][k] for jj in range(3)] + [er[k]] for k in range(d)])
            a = [0] * 3
            for row in ER:
                p_ = next((jj for jj in range(3) if row[jj] != 0), None)
                if p_ is None:
                    continue
                a[p_] = row[3] * inv([[row[p_]]])[0][0] % P
            Erows.append(a)
        rows = [[[-T[i][k] % P, 1 if i == k else 0] for k in range(3)] for i in range(3)]
        for er in Erows:
            rows.append([[er[k] % P] for k in range(3)])
        polys = []
        for rs in itertools.combinations(range(len(rows)), 3):
            for cs in itertools.combinations(range(3), 3):
                Mx = [[rows[i][k] for k in cs] for i in rs]
                v = det_poly(Mx)
                if not (len(v) == 1 and v[0] == 0):
                    polys.append(v)
        if not gcd_is_one(polys):
            not_cov += 1
    print(f"  全部 3 维子空间 {tot}；结构可允许（A2,A3,A6）{adm}；其中有 mu>=1 的 {with_mu}；未覆盖的 {not_cov}")
    verdict = ("猜想一致 ✓（无 mu>=1，或存在未覆盖）" if (with_mu == 0 or not_cov > 0)
               else "**猜想被推翻** ✗（有 mu>=1 的格子，但全部被覆盖）")
    print("  =>", verdict)


if __name__ == '__main__':
    main()
