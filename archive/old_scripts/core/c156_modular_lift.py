r"""
c156_modular_lift.py -- 模素数版 lift 检验器（快速；用于大 n 的 (p,d) 覆盖）

有理数精确运算在 n=11 时太慢（>10 分钟）。本脚本改在 F_p 上做：

  * 秩 / 零空间 / 线性求解：Gauss 消元（模 p）
  * (a)：F = ΛM（解线性方程组）
  * (b)：$\operatorname{rank}(\lambda M-F)=\rho$ 对**随机 50 个** $\lambda\in\mathbb{F}_p$ 检查
        （(b) 只在有限个 λ 失败，故"全过"是强证据）

**注意**：(b) 在 F_p 上通过 ⟹ 有理数上很可能通过（gcd 恒为常数在模 p 下仍为常数）；
但反过来，F_p 上失败**不能**断言有理数上失败。故本脚本只用于**找正例**。

跑法：python scripts/core/c156_modular_lift.py [n] [p_out] [d]
"""
import sys, os, random, secrets
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

P = 2147483647          # 2^31 - 1（素数）


def inv(a):
    return pow(a % P, P - 2, P)


def rref(M):
    A = [[x % P for x in row] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    piv = []
    r = 0
    for c in range(n):
        pr = None
        for i in range(r, m):
            if A[i][c] % P:
                pr = i
                break
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
    if not M or not M[0]:
        return 0
    return len(rref(M)[1])


def solve(M, b):
    """解 M x = b；返回 (x0, ker) 或 None"""
    m = len(M)
    n = len(M[0])
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


def rand_mat(rng, m, n, lo=-1, hi=1):
    return [[rng.randint(lo, hi) % P for _ in range(n)] for _ in range(m)]


def mul(X, Y):
    assert len(X[0]) == len(Y)
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) % P
             for j in range(len(Y[0]))] for i in range(len(X))]


def trans(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


def nullspace(X):
    """返回 X v = 0 的基（v 为列）"""
    m, n = len(X), len(X[0])
    sol = solve(X, [0] * m)
    if sol is None:
        return []
    return sol[1]


def build(A_, C):
    """N = ker[C;CA] 的基（n×d），R0, S, alpha0, beta0"""
    n = len(A_)
    CA = mul(C, A_)
    st = C + CA
    Ncols = nullspace(st)              # 每个是长度 n 的向量
    N = [[Ncols[j][i] % P for j in range(len(Ncols))] for i in range(n)]
    d = len(Ncols)
    if d == 0:
        return None
    NtN = mul(trans(N), N)
    invNtN = None
    # 广义逆：(N^T N)^{-1} N^T
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


def lift(Ar, A_, C, L0, D, q, rng, trials=10, nlams=30):
    """尝试 q 行 lift（rank rho = len(Ar)）"""
    n, d = D["n"], D["d"]
    N, AN = D["N"], D["AN"]
    rho = len(Ar)
    # A 的零化子：{w : a·w = 0 对所有行 a} ⟺ w ∈ nullspace(Ar)
    ann = nullspace(Ar) if Ar else [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    m = q - 1
    rows = []
    for w in ann:
        for i in range(m):
            for Mx in (N, AN):
                e = [0] * (m * n)
                for j in range(n):
                    e[i * n + j] = sum(Mx[j][k] * w[k] for k in range(d)) % P
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
        # (a): F = Lambda M
        cols = []
        for i in range(q):
            for j in range(rho):
                e = [0] * (q * q)
                for k in range(q):
                    e[i * q + k] = M[k][j]
                cols.append(e)
        # 解 Lambda M = F
        rhs = [Fm[i][j] for i in range(q) for j in range(rho)]
        ok = True
        for lam in [rng.randint(0, P - 1) for _ in range(nlams)]:
            pen = [[(lam * M[i][j] - Fm[i][j]) % P for j in range(d)] for i in range(q)]
            if rank(pen) != rho:
                ok = False
                break
        if ok:
            # 精确确认 (a)
            solA = solve(cols, rhs)
            if solA is not None:
                return L
    return None


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    p_out = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    d_t = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    rng = random.Random(0)
    print(f"模素数版：n={n}, p_out={p_out}, d={d_t}（预测 q = max(3, d+2-p) = {max(3, d_t + 2 - p_out)}）")
    found = 0
    for seed in range(6):
        r = random.Random(seed)
        A_ = rand_mat(r, n, n)
        C = rand_mat(r, p_out, n)
        if rank(C) != p_out:
            continue
        if rank(C + mul(C, A_)) != n - d_t:
            continue
        D = build(A_, C)
        if D is None:
            continue
        L0 = [rand_mat(r, 1, n)[0]]
        AN = D["AN"]
        al = mul(L0, D["N"])[0]
        be = mul(L0, AN)[0]
        if not any(al):
            continue
        S = D["S"]
        rho = d_t + 1 - p_out              # 定律预测的 rho
        if rho < 2:
            rho = 2
        # 显式构造 |A∩S|=1 的 A：A = span{al, be} + L（L ⊆ S 一条线）
        best = None
        for k in range(len(S)):
            for t in (-1, 0, 1, 2):
                l = [(S[k][j] + t * S[(k + 1) % len(S)][j]) % P for j in range(D["d"])]
                Ar = [row for row in rref([al, be, l])[0] if any(row)]
                if len(Ar) != rho:
                    continue
                inter = len(Ar) + len(S) - rank(Ar + S)
                if inter != 1:
                    continue
                w = lift(Ar, A_, C, L0, D, rho + 1, r)
                if w is not None:
                    best = w
                    break
            if best:
                break
        print(f"   seed{seed}: dimS={len(S)} rho={rho} q={rho+1} → {'✓' if best else '✗'}")
        found += bool(best)
    print(f"合计命中 {found}")


if __name__ == "__main__":
    main()
