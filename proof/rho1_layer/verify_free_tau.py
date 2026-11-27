"""验证定理 2（rho3c1_free_tau.md）：U ⊆ B、w ≠ 0、(3,1) 层，tau 自由时可取 C 对角互异，使 (5b) 成立。

抽象层模型（忠实）：
  * U = span{u1,u2,u3} ⊂ Q^3（这里直接取 U = Q^3，即所有行都在 3 维空间内）；
  * T(u_i) = t_i ∈ U；B ⊇ U（tau 自由）；w ∈ U, w ≠ 0；
  * 行：lam*u_i - (t_i + beta tau_i)（i=1..3），再加 w（常数行）；
  * (5b) <=> 所有 3x3 子式的 gcd 为非零常数。

构造（定理 2 的证明）：把 u 取成标准基（U = I），C = diag(c1,c2,c3)，c 互异，且 w ≠ 0。
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
        t = pmul(M[0][j], det_poly(sub))
        if j % 2:
            t = [-c for c in t]
        acc = padd(acc, t)
    return ptrim(acc)


def cond_5b(rows):
    polys = []
    for rs in itertools.combinations(range(len(rows)), 3):
        for cs in itertools.combinations(range(3), 3):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            v = det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
    return len(g) == 1 and g[0] != 0


def main():
    rng = random.Random(555)
    ok = 0
    total = 0
    for _ in range(200):
        # U = I（标准基），C = diag(c)，c 互异；w ≠ 0
        cs = rng.sample([Fr(x) for x in range(-4, 5)], 3)
        C = [[cs[i] if i == j else Fr(0) for j in range(3)] for i in range(3)]
        w = [Fr(rng.choice([-2, -1, 1, 2])) for _ in range(3)]
        if not any(w):
            continue
        rows = [(C[i], [cs[i] if i == j else Fr(0) for j in range(3)]) for i in range(3)]
        # 注意：行 = lam*u_i - C_i，其中 u_i = e_i（标准基），C_i = C 的第 i 行
        rows = [([Fr(1) if i == j else Fr(0) for j in range(3)], [C[i][j] for j in range(3)]) for i in range(3)]
        rows.append(([Fr(0)] * 3, list(w)))
        total += 1
        if cond_5b(rows):
            ok += 1
    print(f"定理 2 构造验证：{ok}/{total} 通过（预期全部通过）")


if __name__ == '__main__':
    main()
