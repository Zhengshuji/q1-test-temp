"""跨域稳健性检验（(a)）：在 F_p（p=3,5,7）上完全枚举候选实例的 (3,1) 型层，比较

  * 合法 V 的个数；
  * 每个 V 的 (5b) 状态与 gcd 次数；
  * 按"子式次数模式"分层的分布，以及每层是否被完全覆盖。

为了在 p 较大时也可行，先做一个坐标变换把 row L0 送到 e1，然后只需枚举
"包含 e1 的 4 维子空间" = { span{e1} (+) W : W 是 5 维空间里的 3 维子空间 }，
其个数是高斯二项式 [5 choose 3]_p（p=5 约 2e4，p=7 约 1.4e5）。

用法：python enum_31_fp.py 3 5 7
"""
import itertools
import json
import sys

P = int(sys.argv[1]) if len(sys.argv) > 1 else 3


# ---------- F_p 线性代数 ----------
def inv(a):
    return pow(a % P, P - 2, P)


def rref(M):
    M = [[x % P for x in row] for row in M]
    r, c = len(M), len(M[0])
    piv, i = [], 0
    for j in range(c):
        p = next((t for t in range(i, r) if M[t][j] % P), None)
        if p is None:
            continue
        M[i], M[p] = M[p], M[i]
        iv = inv(M[i][j])
        M[i] = [(x * iv) % P for x in M[i]]
        for t in range(r):
            if t != i and M[t][j] % P:
                f = M[t][j]
                M[t] = [(a - f * b) % P for a, b in zip(M[t], M[i])]
        piv.append(j)
        i += 1
        if i == r:
            break
    return M, piv


def rank(M):
    return len(rref(M)[1]) if M else 0


def row_basis(M):
    R, piv = rref(M)
    return [R[i] for i in range(len(piv))]


def mat_inv(M):
    n = len(M)
    A = [[M[i][j] % P for j in range(n)] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for j in range(n):
        p = next(t for t in range(j, n) if A[t][j] % P)
        A[j], A[p] = A[p], A[j]
        iv = inv(A[j][j])
        A[j] = [(x * iv) % P for x in A[j]]
        for t in range(n):
            if t != j and A[t][j] % P:
                f = A[t][j]
                A[t] = [(a - f * b) % P for a, b in zip(A[t], A[j])]
    return [row[n:] for row in A]


def mul_vec(x, M):          # 行向量 x 乘矩阵 M
    return [sum(x[i] * M[i][j] for i in range(len(x))) % P for j in range(len(M[0]))]


def mm(X, Y):
    return [[sum(X[i][t] * Y[t][j] for t in range(len(Y))) % P for j in range(len(Y[0]))] for i in range(len(X))]


# ---------- 多项式 F_p[lam] ----------
def ptrim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


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


def det_poly(M):
    n = len(M)
    if n == 1:
        return ptrim(list(M[0][0]))
    acc = [0]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        t = pmul(M[0][j], det_poly(sub))
        if j % 2:
            t = [(-c) % P for c in t]
        acc = padd(acc, t)
    return ptrim(acc)


# ---------- 判定 ----------
def cond_5a(L, A, C):
    CA = mm(C, A)
    LA = mm(L, A)
    return rank([*LA, *L, *CA, *C]) == rank([*L, *CA, *C])


def gcd_and_pattern(L, A, C, n):
    CA, LA = mm(C, A), mm(L, A)
    base = [*L, *CA, *C]
    r0 = rank(base)
    rows = [(L[i], LA[i]) for i in range(len(L))]
    for r in CA:
        rows.append(([0] * n, list(r)))
    for r in C:
        rows.append(([0] * n, list(r)))
    polys = []
    for rs in itertools.combinations(range(len(rows)), r0):
        for cs in itertools.combinations(range(n), r0):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            v = det_poly(M)
            if not (len(v) == 1 and v[0] % P == 0):
                polys.append(v)
    if not polys:
        return None, None, r0
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
    ok = (len(g) == 1 and g[0] % P != 0)
    return (len(g) - 1, ok, tuple(sorted(len(p) - 1 for p in polys)))


def main():
    d0 = json.load(open('proof/rho1_layer/candidate_c31_counterexample.json', encoding='utf-8'))[0]
    A = [[int(x) % P for x in r] for r in d0['A']]
    C = [[int(x) % P for x in r] for r in d0['C']]
    L0 = [int(x) % P for x in d0['L0'][0]]
    n = len(A)
    CA = mm(C, A)
    J = row_basis([*C, *CA])
    j = len(J)
    print(f"F_{P}: n={n}, dim J={j}, rank[C]=?, L0={L0}")

    # 坐标变换 M：L0 * M = e1
    cs = []
    for i in range(n):
        e = [1 if k == i else 0 for k in range(n)]
        if rank([L0] + cs + [e]) > rank([L0] + cs):
            cs.append(e)
        if len(cs) == n - 1:
            break
    if len(cs) != n - 1:
        print("L0 为零行，跳过")
        return
    M = [[L0[i]] + [cs[k][i] for k in range(n - 1)] for i in range(n)]   # 列向量拼
    Minv = mat_inv(M)

    # 枚举 3 维 W ⊆ span{e2..en}（用 5 个坐标的 RREF）
    def spaces(k, m):
        for piv in itertools.combinations(range(m), k):
            free = [c for c in range(m) if c not in piv]
            for vals in itertools.product(range(P), repeat=k * len(free)):
                Mx = [[0] * m for _ in range(k)]
                for i, pc in enumerate(piv):
                    Mx[i][pc] = 1
                idx = 0
                for i in range(k):
                    for fc in free:
                        Mx[i][fc] = vals[idx]
                        idx += 1
                B = row_basis(Mx)
                if len(B) == k:
                    yield B

    strata = {}
    total = 0
    n5 = 0
    for W in spaces(3, n - 1):
        # V' = span{e1} + W（e1 与 W 独立，因为 W ⊆ span{e2..en}）
        Vp = [[1] + [0] * (n - 1)] + [[0] + w for w in W]
        # V = V' * Minv
        V = row_basis([mul_vec(x, Minv) for x in Vp])
        if len(V) != 4:
            continue
        # V 必须含 L0：等价于 V' 含 e1（由构造保证）
        if rank([*V, *CA, *C]) - j != 3:
            continue
        if len(V) + j - rank([*V, *J]) != 1:
            continue
        if not cond_5a(V, A, C):
            continue
        total += 1
        gd, ok, pat = gcd_and_pattern(V, A, C, n)
        if ok:
            n5 += 1
        key = pat if pat is not None else ('EMPTY',)
        st = strata.setdefault(key, [0, 0])
        st[0] += 1
        if ok:
            st[1] += 1
    print(f"  合法 V: {total}；其中 (5b) 成立: {n5}")
    print("  按次数模式分层 [V 数, (5b) 成立数]:")
    for k in sorted(strata, key=lambda z: -strata[z][0])[:6]:
        print(f"    {str(k)[:70]}{'...' if len(str(k))>70 else ''}: {strata[k]}")


if __name__ == '__main__':
    main()
