"""核对 rho3c1_spectral.md 的推论 2：

  (5b)  <=>  w^T v_k != 0 对所有特征向量 v_k 成立   （C 有单谱时）

做法：随机取 C（3x3，有理，单谱），随机取 w != 0，用精确有理算术：
  * 直接算 p_0 = det(lam I - C) 与 p_i（第 i 行换成 w），求 gcd 是否非零常数；
  * 求 C 的特征多项式在 Q 上的有理根（只看有理特征值 —— 若 C 的特征值不全是有理数，
    则 p_0 在 Q[lam] 上不可完全分解，此时只比较"有理特征值处的公共根"与"对应特征向量的正交性"）。
  * 对每个**有理**特征值 lam_k：算 v_k（核空间）与 eta_k，检查 (w^T v_k == 0) 与
    "lam_k 是 p_1,p_2,p_3 的公共根" 是否一致（引理 1）。
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


def ev_idx(polys):
    """几个多项式在给定点的值（用 Horner）。"""
    raise NotImplementedError


def main():
    rng = random.Random(424242)
    ok_lemma = 0
    total_lemma = 0
    ok_cor = 0
    total_cor = 0
    for _ in range(120):
        while True:
            C = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
            M = [[ptrim([-C[i][j], Fr(1) if i == j else Fr(0)]) for j in range(3)] for i in range(3)]
            cp = det_poly(M)
            # 有理根
            import math
            L = 1
            for cc in cp:
                L = L * cc.denominator // math.gcd(L, cc.denominator)
            ints = [int(cc * L) for cc in cp]
            def divs(v):
                v = abs(v)
                return [i for i in range(1, v + 1) if v % i == 0] or [1]
            cands = set()
            for p in divs(ints[0]):
                for q in divs(ints[-1]):
                    cands.add(Fr(p, q)); cands.add(-Fr(p, q))
            roots = []
            for lam in sorted(cands):
                val = Fr(0)
                for cc in reversed(cp):
                    val = val * lam + cc
                if val == 0:
                    roots.append(lam)
            # 只保留**单**根（cp'(lam) != 0）—— 引理 1 的假设
            dcp = [Fr(k) * cp[k] for k in range(1, len(cp))]
            simple = []
            for lam in roots:
                val = Fr(0)
                for cc in reversed(dcp):
                    val = val * lam + cc
                if val != 0:
                    simple.append(lam)
            roots = simple
            if len(roots) >= 2:          # 至少两个单有理特征根，才有意义
                break
        w = [Fr(rng.randint(-2, 2)) for _ in range(3)]
        if not any(w):
            continue
        # p_i：第 i 行换成 w
        def p_i(A, w, i):
            MM = [[ptrim([-A[r][c], Fr(1) if r == c else Fr(0)]) for c in range(3)] for r in range(3)]
            MM[i] = [[x] for x in w]
            return det_poly(MM)
        ps = [p_i(C, w, i) for i in range(3)]
        for lam in roots:
            total_lemma += 1
            # 公共根？
            allzero = all((lambda p: sum(p[k] * lam ** k for k in range(len(p))))(p) == 0 for p in ps)
            # 特征向量（核空间）
            Mk = [[C[i][j] - (lam if i == j else Fr(0)) for j in range(3)] for i in range(3)]
            ker = AI.nullspace(Mk)
            if not ker:
                continue
            dot = [sum(w[k] * v[k] for k in range(3)) for v in ker]
            orth = any(d == 0 for d in dot) and all(d == 0 for d in dot) if False else all(d == 0 for d in dot)
            if allzero == orth:
                ok_lemma += 1
        # 推论 2 只在"全部特征值有理"时可直接比
        if len(roots) == 3:
            total_cor += 1
            vals = []
            for lam in roots:
                Mk = [[C[i][j] - (lam if i == j else Fr(0)) for j in range(3)] for i in range(3)]
                ker = AI.nullspace(Mk)
                vals.append(all(sum(w[k] * v[k] for k in range(3)) == 0 for v in ker))
            g = ps[0]
            for q in ps[1:]:
                g = pgcd(g, q)
            g = pgcd(g, cp)
            gcd_one = (len(g) == 1 and g[0] != 0)
            if gcd_one == (not any(vals)):
                ok_cor += 1
    print(f"引理 1（单特征值处）：{ok_lemma}/{total_lemma} 一致")
    print(f"推论 2（全部特征值有理时）：{ok_cor}/{total_cor} 一致")


if __name__ == '__main__':
    main()
