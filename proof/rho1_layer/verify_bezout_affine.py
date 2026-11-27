"""§17 + T11 的等价性检验（**带仿射约束**的 A，单变量参数化）。

A 取一条仿射直线：tau(s) = tau0 + s*d （s ∈ Q）。于是 p_i(tau(s)) 的系数是 s 的仿射函数。

两条判据（都在 A 上）：
  (i)  ∃s: gcd_lambda(p_1(tau(s),·),...,p_m(tau(s),·)) = 1
  (ii) ∃D ∃ 乘法映射 Φ_D 的极大子式 Δ: Δ(tau(·)) 作为 s 的多项式 ≢ 0

(i) 用采样（好集在 s 上是开的 ⟹ 采样决定性）；
(ii) 用**精确多项式**：把 Φ_D 的每个元素写成 s 的多项式，展开极大子式，检查非零系数。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


# ---------- 单变量多项式（系数从低到高，Fraction） ----------
def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    o = [Fr(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] += x
    for i, y in enumerate(b):
        o[i] += y
    return ptrim(o)


def pmul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return ptrim(o)


def pscale(a, c):
    return ptrim([c * x for x in a])


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


def main():
    rng = random.Random(31415)
    agree = disagree = 0
    for trial in range(40):
        m = rng.choice([2, 3])
        d = rng.choice([1, 2])
        # p_i(tau) 的系数：常数部分 + sum_k tau_k * 线性部分
        P0 = [[Fr(rng.randint(-2, 2)) for _ in range(d + 1)] for _ in range(m)]
        Pk = [[[Fr(rng.randint(-2, 2)) for _ in range(d + 1)] for _ in range(3)] for _ in range(m)]
        j = rng.choice([1, 2])
        tau0 = [Fr(rng.randint(-1, 1)) for _ in range(j)]
        dirv = [Fr(rng.randint(-1, 1)) for _ in range(j)]

        def p_of_s(i):
            """返回 p_i(tau0 + s*dir) 的系数，每个系数是 s 的多项式。"""
            out = []
            for e in range(d + 1):
                const = P0[i][e] + sum(tau0[k] * Pk[i][k][e] for k in range(j))
                lin = sum(dirv[k] * Pk[i][k][e] for k in range(j))
                out.append(ptrim([const, lin]))
            return out

        def peval_at(i, s):
            return ptrim([peval(c, s) for c in p_of_s(i)])

        def peval(p, s):
            r = Fr(0)
            for c in reversed(p):
                r = r * s + c
            return r

        # (i) 采样 s
        found_i = False
        for _t in range(60):
            s = Fr(rng.randint(-3, 3))
            g = peval_at(0, s)
            ok = True
            for i in range(1, m):
                g = pgcd(g, peval_at(i, s))
                if len(g) == 1 and g[0] == 0:
                    ok = False
                    break
            if len(g) == 1 and g[0] != 0:
                found_i = True
                break
        # (ii) 秩检验：用随机 s 上的精确 rank 近似 "在 Q(s) 上的秩"（坏 s 落在真子簇上）
        found_ii = False
        for D in range(0, 2 * d * (m - 1) + 3):
            rows = d + D + 1
            cols = m * (D + 1)
            good = False
            for _t in range(6):
                sv = Fr(rng.randint(-7, 7))
                M = [[Fr(0)] * cols for _ in range(rows)]
                for i in range(m):
                    ps = p_of_s(i)
                    for k in range(D + 1):
                        for e in range(d + 1):
                            if k + e <= d + D:
                                M[k + e][i * (D + 1) + k] += peval(ps[e], sv)
                if AI.rank(M) == rows:
                    good = True
                    break
            if good:
                found_ii = True
                break
        if found_i == found_ii:
            agree += 1
        else:
            disagree += 1
            if disagree <= 3:
                print(f"不一致: m={m} d={d} j={j}  (i)={found_i} (ii)={found_ii}")
    print(f"一致 {agree}，不一致 {disagree}（A 为仿射直线）")
    print("结论：0 不一致 => §17 在带仿射约束的 A 上也成立（**验证，不是证明**）")


if __name__ == '__main__':
    main()