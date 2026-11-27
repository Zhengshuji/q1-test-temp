"""专家优先级 3 的第一步：把内层问题(b)写成"按子式对 lam 的实际次数分层 + 每层秩退化条件"，
并**实验核对**它与直接 gcd 判定一致。

核对内容（对每个样本）：
  * degpat = 每个 rho x rho 子式对 lam 的实际次数（升序）；
  * gdeg   = 全部子式的 gcd 的次数；
  * (5b)   = gcd 为非零常数（gdeg == 0 且 gcd != 0）；
  * rk_gen = 在随机 lam0 处铅笔的秩（应 = rho 当且仅当 (5b)）。
预期恒等式： (5b)  <=>  (gdeg == 0)  <=>  (rk_gen == rho 且 gdeg == 0)

同时统计：不同的 degpat 有多少种（说明分层是**真的**会发生、不是空的）。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdivmod(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        c = r[-1] / b[-1]
        dd = len(r) - len(b)
        q[dd] = c
        for i, bi in enumerate(b):
            r[i + dd] -= c * bi
        r = ptrim(r)
    return q, r


def pgcd(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    while not (len(b) == 1 and b[0] == 0):
        _, r = pdivmod(a, b)
        a, b = b, r
    return a


def pmul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return ptrim(o)


def padd(a, b):
    o = [Fr(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] += x
    for i, y in enumerate(b):
        o[i] += y
    return ptrim(o)


def det_poly(M):
    n = len(M)
    if n == 1:
        return ptrim(list(M[0][0]))
    acc = [Fr(0)]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = pmul(M[0][j], det_poly(sub))
        if j % 2:
            term = [-c for c in term]
        acc = padd(acc, term)
    return ptrim(acc)


def minors(rows, rho, d):
    """返回全部 rho x rho 子式（多项式，系数升序）。rows[i] = (vec, vecA)。"""
    out = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(d), rho):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            val = det_poly(M)
            if not (len(val) == 1 and val[0] == 0):
                out.append(val)
    return out


def rank_at(rows, lam, rho, d):
    M = [[rows[i][0][j] * lam - rows[i][1][j] for j in range(d)] for i in range(len(rows))]
    return AI.rank(M)


def main():
    rng = random.Random(31415)
    strata = {}
    checks = 0
    agree = 0
    for trial in range(300):
        d = rng.choice([4, 5, 6])
        rho = rng.choice([2, 3])
        c = 1
        # U（dim rho）、T 保 U、B（dim m）、w ∈ U∩B
        U = AI.row_basis([[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(rho + 2)])[:rho]
        if len(U) < rho:
            continue
        m = rng.choice([1, 2, 3])
        B = AI.row_basis([[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(m + 2)])[:m]
        if len(B) < m:
            continue
        BU = [b for b in B if AI.rank([r[:] for r in U] + [b]) == len(U)]
        if not BU:
            continue
        w = BU[0]
        # T 保 U：T(u_i) = sum C_ij u_j
        Cc = [[Fr(rng.randint(-2, 2)) for _ in range(rho)] for _ in range(rho)]
        Tu = [[sum(Cc[i][j] * U[j][k] for j in range(rho)) for k in range(d)] for i in range(rho)]
        rows = [(U[i], Tu[i]) for i in range(rho)] + [([Fr(0)] * d, list(w))]
        # tau：给 U 行加 B∩U 的元素
        for _t in range(6):
            rr = []
            for i in range(rho):
                tv = [sum(Fr(rng.randint(-2, 2)) * b[k] for b in BU) for k in range(d)]
                rr.append((U[i], [Tu[i][k] + tv[k] for k in range(d)]))
            rr.append(([Fr(0)] * d, list(w)))
            ms = minors(rr, rho, d)
            if not ms:
                continue
            g = ms[0]
            for mm2 in ms[1:]:
                g = pgcd(g, mm2)
            gdeg = len(g) - 1
            degpat = tuple(sorted(len(m) - 1 for m in ms))
            rk = max(rank_at(rr, Fr(rng.randint(-5, 5)), rho, d) for _ in range(3))
            b5 = (gdeg == 0 and not (len(g) == 1 and g[0] == 0))
            strata[degpat] = strata.get(degpat, 0) + 1
            checks += 1
            if b5 == (gdeg == 0) and b5 == (rk == rho and gdeg == 0):
                agree += 1
    print(f"样本数 {checks}；degpat 种类 {len(strata)}")
    print("degpat 分布（前 8 个）:")
    for k, v in sorted(strata.items(), key=lambda kv: -kv[1])[:8]:
        print(f"   {k}: {v}")
    print(f"(5b) 与 [gdeg==0] 与 [gen-rank==rho 且 gdeg==0] 三者一致: {agree}/{checks}")


if __name__ == '__main__':
    main()
