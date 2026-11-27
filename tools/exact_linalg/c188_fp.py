"""c188_fp.py — F_p 上的 (5a)/(5b) 快速判定（供大样本搜索用）

多项式用系数列表表示（mod p，低次在前）。提供：
  rank_fp(M, p)             —— F_p 上的秩
  cond5a_fp(L, A, C, p)     —— (5a)
  cond5b_fp(L, A, C, p)     —— (5b)：子式 gcd 为常数

用法：from c188_fp import cond5a_fp, cond5b_fp
"""
import itertools


def rref_fp(M, p):
    basis = []
    for v in M:
        v = [x % p for x in v]
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x != 0)
            if v[piv] != 0:
                c = v[piv]
                v = [(v[j] - c * b[j]) % p for j in range(len(v))]
        if any(v):
            piv = next(i for i, x in enumerate(v) if x != 0)
            inv = pow(v[piv], p - 2, p)
            v = [(x * inv) % p for x in v]
            basis.append(v)
            basis.sort(key=lambda r: next(i for i, x in enumerate(r) if x != 0))
    return basis


def rank_fp(M, p):
    return len(rref_fp(M, p))


def mul_fp(X, Y, p):
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) % p for j in range(m)] for i in range(n)]


# ---------- 多项式（mod p，低次在前） ----------
def pnorm(a, p):
    while a and a[-1] % p == 0:
        a = a[:-1]
    return [x % p for x in a]


def padd(a, b, p):
    n = max(len(a), len(b))
    return pnorm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)], p)


def psub(a, b, p):
    n = max(len(a), len(b))
    return pnorm([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)], p)


def pmul(a, b, p):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return pnorm(out, p)


def pdivmod(a, b, p):
    a = pnorm(list(a), p)
    b = pnorm(list(b), p)
    if not b:
        raise ZeroDivisionError
    q = [0] * max(0, len(a) - len(b) + 1)
    inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and a:
        d = len(a) - len(b)
        coef = a[-1] * inv % p
        q[d] = coef
        for i in range(len(b)):
            a[d + i] = (a[d + i] - coef * b[i]) % p
        a = pnorm(a, p)
        if not a:
            break
    return pnorm(q, p), a


def pgcd_fp(a, b, p):
    a = pnorm(list(a), p)
    b = pnorm(list(b), p)
    while b:
        _, r = pdivmod(a, b, p)
        a, b = b, r
    if a:
        inv = pow(a[-1], p - 2, p)
        a = [(x * inv) % p for x in a]
    return a


def det_poly(M, p):
    """M: h×h，元素为多项式（列表）"""
    h = len(M)
    out = [0]
    for perm in itertools.permutations(range(h)):
        # 符号
        inv = 0
        for i in range(h):
            for j in range(i + 1, h):
                if perm[i] > perm[j]:
                    inv += 1
        term = [1]
        for i in range(h):
            term = pmul(term, M[i][perm[i]], p)
            if not term:
                break
        if inv % 2:
            out = psub(out, term, p)
        else:
            out = padd(out, term, p)
    return pnorm(out, p)


def cond5a_fp(L, A, C, p):
    n = len(A)
    CA = mul_fp(C, A, p)
    LA = mul_fp(L, A, p)
    rhs = rank_fp([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C], p)
    lhs = rank_fp([list(x) for x in LA] + [list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C], p)
    return lhs == rhs


def cond5b_fp(L, A, C, p):
    n = len(A)
    CA = mul_fp(C, A, p)
    LA = mul_fp(L, A, p)
    rows = []
    for i in range(len(L)):
        rows.append([[-LA[i][j] % p, L[i][j] % p] for j in range(n)])
    for r in CA:
        rows.append([[r[j] % p, 0] for j in range(n)])
    for r in C:
        rows.append([[r[j] % p, 0] for j in range(n)])
    h = rank_fp([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C], p)
    if h == 0:
        return True
    g = None
    for rr in itertools.combinations(range(len(rows)), h):
        for cc in itertools.combinations(range(n), h):
            M = [[rows[r][c] for c in cc] for r in rr]
            d = det_poly(M, p)
            if not d:
                continue
            g = d if g is None else pgcd_fp(g, d, p)
            if len(g) <= 1:
                break
        if g is not None and len(g) <= 1:
            break
    # g is None 意味着所有极大子式恒为零 —— 秩处处不足，必须返回 False
    return g is not None and len(g) <= 1


def nullspace_fp(M, p, n):
    """M 的行生成的矩阵的零空间（列向量），返回基（每个是长度 n 的列表）"""
    R = rref_fp(M, p)
    piv = [next(i for i, x in enumerate(r) if x) for r in R]
    free = [j for j in range(n) if j not in piv]
    out = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for idx, r in enumerate(R):
            v[piv[idx]] = (-r[f]) % p
        out.append(v)
    return out


if __name__ == "__main__":
    # 与 Q 上的 c162 对比一个小例子
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "exact_linalg"))
    from fractions import Fraction as Fr
    import c162_dimV_formula as M
    p = 3
    A = [[1, 0, 0], [0, 2, 0], [0, 0, 0]]
    C = [[0, 1, 1]]
    L = [[1, 0, 0], [0, 1, 0]]
    print("fp5a", cond5a_fp(L, A, C, p), "q5a", M.cond5a([[Fr(x) for x in r] for r in L],
                                                        [[Fr(x) for x in r] for r in A],
                                                        [[Fr(x) for x in r] for r in C]))
    print("fp5b", cond5b_fp(L, A, C, p))
