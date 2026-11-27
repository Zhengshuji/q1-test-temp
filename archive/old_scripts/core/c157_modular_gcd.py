r"""
c157_modular_gcd.py -- 模素数版 lift 检验器（**正确版**：用多项式 gcd 判 (b)）

背景：`c156` 用"随机 λ 采样"判 (b)，而 (b) 的失败集是**有限个** λ
⟹ 采样几乎必然漏掉 ⟹ 系统性假阳性。本脚本改用**模 p 的多项式 gcd**：

$$(b)\iff \gcd\{\rho\text{ 阶子式 of }\lambda M-F\}\ \text{为（非零）常数}$$

组件：F_p 多项式（系数列表）/ 行列式（Laplace）/ gcd（Euclid + 首一化）。

跑法：python scripts/core/c157_modular_gcd.py <n> <p_out> <d> <rho>
校准：c157 8 2 4 2 应报 0（精确版亦然）；c157 8 2 4 3 应报 >0。
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

P = 2147483647


def inv(a):
    return pow(a % P, P - 2, P)


def rref(M):
    A = [[x % P for x in row] for row in M]
    m, n = len(A), (len(A[0]) if A else 0)
    piv, r = [], 0
    for c in range(n):
        pr = next((i for i in range(r, m) if A[i][c] % P), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = inv(A[r][c])
        A[r] = [x * iv % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    return A, piv


def rank(M):
    return len(rref(M)[1]) if M and M[0] else 0


def solve(M, b):
    m, n = len(M), len(M[0])
    A = [[M[i][j] % P for j in range(n)] + [b[i] % P] for i in range(m)]
    A, piv = rref(A)
    for i in range(m):
        if all(A[i][j] == 0 for j in range(n)) and A[i][n]:
            return None
    x = [0] * n
    for r, c in enumerate(piv):
        x[c] = A[r][n]
    free = [j for j in range(n) if j not in piv]
    ker = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for r, c in enumerate(piv):
            v[c] = (-A[r][f]) % P
        ker.append(v)
    return x, ker


def mul(X, Y):
    assert len(X[0]) == len(Y)
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) % P
             for j in range(len(Y[0]))] for i in range(len(X))]


def trans(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


# ---------- 多项式（系数列表，低次在前，模 P） ----------
def pnorm(a):
    while len(a) > 1 and a[-1] % P == 0:
        a = a[:-1]
    return [x % P for x in a]


def pdeg(a):
    a = pnorm(a)
    return len(a) - 1 if any(a) else -1


def pconst_nonzero(a):
    a = pnorm(a)
    return len(a) == 1 and a[0] % P != 0


def psub(a, b):
    n = max(len(a), len(b))
    return pnorm([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)])


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % P
    return pnorm(r)


def pdivmod(a, b):
    a = pnorm(list(a))
    b = pnorm(list(b))
    if not any(b):
        raise ZeroDivisionError
    ib = inv(b[-1])
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        d = len(a) - len(b)
        c = a[-1] * ib % P
        q[d] = c
        a = psub(a, [(c * b[i]) % P for i in range(len(b))] + [0] * d)
    return pnorm(q), pnorm(a if a else [0])


def pgcd(a, b):
    a, b = pnorm(list(a)), pnorm(list(b))
    while any(b):
        _, r = pdivmod(a, b)
        a, b = b, r
    if not any(a):
        return [0]
    return pnorm([x * inv(a[-1]) % P for x in a])


def pdet(mat):
    """Laplace 展开（多项式元素）；matrix 为 poly 的 list of list"""
    n = len(mat)
    if n == 0:
        return [1]
    if n == 1:
        return pnorm(mat[0][0])
    acc = [0]
    for j in range(n):
        sub = [[mat[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = pmul(mat[0][j], pdet(sub))
        sign = 1 if j % 2 == 0 else -1
        acc = psub(acc, term) if sign < 0 else [((acc[i] if i < len(acc) else 0) + (term[i] if i < len(term) else 0)) % P
                                               for i in range(max(len(acc), len(term)))]
        acc = pnorm(acc)
    return acc


def build(A_, C):
    n = len(A_)
    st = C + mul(C, A_)
    Ncols = solve(st, [0] * len(st))[1]
    N = [[Ncols[j][i] % P for j in range(len(Ncols))] for i in range(n)]
    d = len(Ncols)
    if d == 0:
        return None
    NtN = mul(trans(N), N)
    m = len(NtN)
    aug = [row[:] + [1 if i == j else 0 for j in range(m)] for i, row in enumerate(NtN)]
    aug, piv = rref(aug)
    if len(piv) < m or any(p >= m for p in piv):
        return None
    invNtN = [row[m:] for row in aug]
    Npinv = mul(invNtN, trans(N))
    AN = mul(A_, N)
    Ap = mul(Npinv, AN)
    R0 = [[(AN[i][j] - sum(N[i][k] * Ap[k][j] for k in range(d))) % P
           for j in range(d)] for i in range(n)]
    S = [row for row in rref(R0)[0] if any(x % P for x in row)]
    return {"N": N, "AN": AN, "Ap": Ap, "R0": R0, "S": S, "d": d, "n": n}


def b_holds(M, Fm, rho):
    """(b) ⟺ 所有 ρ 阶子式的 gcd 为非零常数"""
    q, d = len(M), len(M[0])
    import itertools
    pen = [[[(-Fm[i][j]) % P, M[i][j] % P] for j in range(d)] for i in range(q)]
    g = [0]
    for rs in itertools.combinations(range(q), rho):
        for cs in itertools.combinations(range(d), rho):
            v = pdet([[pen[r][c] for c in cs] for r in rs])
            if not any(x % P for x in v):
                continue
            g = pgcd(g, v) if any(g) else v
            if pconst_nonzero(g):
                return True
    return pconst_nonzero(g) if any(g) else False


def lift(Ar, A_, C, L0, D, q, rng, trials=30):
    n, d = D["n"], D["d"]
    N, AN = D["N"], D["AN"]
    rho = len(Ar)
    ann = solve(Ar, [0] * rho)[1] if Ar else []
    m = q - 1
    rows = []
    for wv in ann:
        for i in range(m):
            for Mx in (N, AN):
                e = [0] * (m * n)
                for j in range(n):
                    e[i * n + j] = sum(Mx[j][k] * wv[k] for k in range(d)) % P
                rows.append(e)
    if rows:
        sol = solve(rows, [0] * len(rows))
        if sol is None:
            return None
        x0, ker = sol
    else:
        x0, ker = [0] * (m * n), [[1 if t == s else 0 for s in range(m * n)] for t in range(m * n)]
    for _ in range(trials):
        x = [v % P for v in x0]
        for v in ker:
            c = rng.randint(-2, 2)
            x = [(x[j] + c * v[j]) % P for j in range(len(x))]
        L = [list(L0[0])] + [[x[i * n + j] for j in range(n)] for i in range(m)]
        M = mul(L, N)
        if rank(M) != rho:
            continue
        Fm = mul(L, AN)
        if b_holds(M, Fm, rho):
            return L
    return None


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    p_out = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    d_t = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    rho = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    trials = int(sys.argv[5]) if len(sys.argv) > 5 else 30
    seeds = int(sys.argv[6]) if len(sys.argv) > 6 else 4
    print(f"n={n}, p_out={p_out}, d={d_t}, rho={rho}, trials={trials}")
    ok = tot = 0
    for seed in range(seeds):
        r = random.Random(seed)
        A_ = [[r.randint(-1, 1) % P for _ in range(n)] for _ in range(n)]
        C = [[r.randint(-1, 1) % P for _ in range(n)] for _ in range(p_out)]
        if rank(C) != p_out:
            continue
        if rank(C + mul(C, A_)) != n - d_t:
            continue
        D = build(A_, C)
        if D is None:
            continue
        L0 = [[r.randint(-1, 1) % P for _ in range(n)]]
        al = mul(L0, D["N"])[0]
        be = mul(L0, D["AN"])[0]
        if not any(al):
            continue
        d = D["d"]
        Ar = [row for row in rref([al, be])[0] if any(row)]
        k = 0
        while len(Ar) < rho and k < d:
            e = [1 if j == k else 0 for j in range(d)]
            Ar = [row for row in rref(Ar + [e])[0] if any(row)]
            k += 1
        if len(Ar) != rho:
            continue
        tot += 1
        w = lift(Ar, A_, C, L0, D, rho + 1, r, trials=trials)
        ok += w is not None
        print(f"   seed{seed}: dimS={len(D['S'])} rho={rho} q={rho+1} → {'✓' if w else '✗'}")
    print(f"合计 {tot}，成功 {ok}")


if __name__ == "__main__":
    main()
