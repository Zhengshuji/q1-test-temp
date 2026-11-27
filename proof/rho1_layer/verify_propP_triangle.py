"""验证命题 P（mu=2）的专家构造（rho3c1_spectral.md §16）。

构造（专家）：坐标取 E = span(e1^T, e2^T)、w^T = e1^T；C = [[x,y,a],[0,u,b],[0,0,c]]，
其中 T 的第三列 = (a,b,c)，(a,b) != (0,0)；取 s=0、u != c、x ∉ {u,c}、y != 0 且（若 a != 0）a - yb/(u-c) != 0。
坏条件（存在第一坐标为零的特征向量）等价于二次式 p = a^2 s + a(u-c)y - b y^2 = 0。

本脚本：随机实例 -> 按配方构造 C -> 精确测 (5b)（[lam I - C; w^T] 的 3x3 子式 gcd = 1）。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util
spec = importlib.util.spec_from_file_location('V', 'proof/rho1_layer/verify_mu1_criterion.py')
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)


def b5_holds(C, w):
    rows = [[[-C[i][j], Fr(1) if i == j else Fr(0)] for j in range(3)] for i in range(3)]
    rows.append([[w[j]] for j in range(3)])
    polys = []
    for rs in itertools.combinations(range(4), 3):
        for cs in itertools.combinations(range(3), 3):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = V.pgcd(g, q)
    return len(g) == 1 and g[0] != 0


def main():
    rng = random.Random(2468)
    ok = tot = qbad = 0
    for _ in range(300):
        a = Fr(rng.randint(-3, 3)); b = Fr(rng.randint(-3, 3)); c = Fr(rng.randint(-3, 3))
        if a == 0 and b == 0:
            continue
        T = [[Fr(rng.randint(-3, 3)) for _ in range(2)] + [a],
             [Fr(rng.randint(-3, 3)) for _ in range(2)] + [b],
             [Fr(rng.randint(-3, 3)) for _ in range(2)] + [c]]
        while True:
            u = Fr(rng.randint(-4, 4))
            if u != c:
                break
        while True:
            y = Fr(rng.randint(-4, 4))
            if y != 0 and a * (u - c) - y * b != 0:
                break
        x = None
        for cand in range(-6, 7):
            if Fr(cand) not in (u, c):
                x = Fr(cand)
                break
        C = [[x, y, a], [Fr(0), u, b], [Fr(0), Fr(0), c]]
        w = [Fr(1), Fr(0), Fr(0)]
        tot += 1
        assert all(C[i][2] - T[i][2] == 0 for i in range(3))
        if b5_holds(C, w):
            ok += 1
        if a * a * Fr(0) + a * (u - c) * y - b * y * y == 0:
            qbad += 1
    print(f"专家构造验证：{tot} 个实例中 (5b) 成立 {ok} 个（预期全部）")
    print(f"  其中 p=0 的实例数：{qbad}（预期 0）")


if __name__ == '__main__':
    main()
