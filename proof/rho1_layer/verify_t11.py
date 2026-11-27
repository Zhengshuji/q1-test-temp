"""T11（定理 27.2 / 推论 27.3）的精确验证（验证 ≠ 证明）。

命题：若 p_1..p_m ∈ Q[lam]、deg <= d、gcd = 1，则存在 D0 <= 2d(m-1) 使
      Phi_D: (a_1..a_m) (deg a_j <= D) |-> sum a_j p_j   (deg <= d+D)
是**满射**（rank = d+D+1）。

做法：精确有理数算术，直接算 rank Phi_D，找最小的满射 D，与界 2d(m-1) 比较。
gcd=1 的构造：让其中一个多项式为常数 1，或令 p_m = p_1 + p_2 + 1 之类；并用 Euclid 实际核验 gcd。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def pmul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o


def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pdivmod(a, b):
    a, b = ptrim(a), ptrim(b)
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


def pgcd_all(ps):
    g = ps[0]
    for q in ps[1:]:
        a, b = ptrim(g), ptrim(q)
        while not (len(b) == 1 and b[0] == 0):
            _, r = pdivmod(a, b)
            a, b = b, r
        g = a
    # 归一化成首一
    if g[-1] != 0:
        g = [x / g[-1] for x in g]
    return ptrim(g)


def phi_rank(ps, D):
    d = max(len(p) - 1 for p in ps)
    m = len(ps)
    rows = d + D + 1
    cols = m * (D + 1)
    M = [[Fr(0)] * cols for _ in range(rows)]
    for j, p in enumerate(ps):
        for k in range(D + 1):
            col = j * (D + 1) + k
            for e, c in enumerate(p):
                if k + e <= d + D:
                    M[k + e][col] += c
    return AI.rank(M), rows


def main():
    rng = random.Random(20261028)
    worst = 0
    checked = 0
    fails = 0
    for trial in range(200):
        m = rng.choice([2, 3, 4, 5])
        d = rng.choice([1, 2, 3])
        ps = []
        for _j in range(m):
            p = [Fr(rng.randint(-3, 3)) for _ in range(d + 1)]
            if p[-1] == 0:
                p[-1] = Fr(1)
            ps.append(ptrim(p))
        # 强制 gcd = 1：把最后一个换成 p_1 + p_2 + ... + 1（gcd 仍可能 >1），再用 Euclid 核验
        ps[-1] = ptrim([ps[0][i] + (ps[1][i] if len(ps) > 1 else Fr(0)) + (Fr(1) if i == 0 else Fr(0))
                        for i in range(d + 1)])
        g = pgcd_all(ps)
        if len(g) != 1 or g[0] != 1:
            continue                          # 只测 gcd = 1 的样本
        bound = 2 * d * (m - 1)
        # 找最小的满射 D
        found = None
        for D in range(0, bound + 3):
            r, rows = phi_rank(ps, D)
            if r == rows:
                found = D
                break
        checked += 1
        if found is None:
            fails += 1
            if fails <= 3:
                print(f"  未找到满射 D（m={m}, d={d}, bound={bound}）: {ps}")
        else:
            if found > bound:
                fails += 1
                if fails <= 3:
                    print(f"  超出界: m={m} d={d} 最小 D={found} > bound={bound}")
            worst = max(worst, found)
    print(f"gcd=1 样本 {checked} 例，失败 {fails}；观测到的最大最小-D = {worst}")
    print("结论：0 失败 => 定理 27.2 的界在样本上成立（**验证，不是证明**）")


if __name__ == '__main__':
    main()
