"""验证定理 12：mu=0 通道恒不可行（det(lam U - C) = det U * p_T(lam)，是恒零或非零三次）。

精确有理算术；不抽样推断结论 —— 这里只是核对"构造出的铅笔确实失败"。
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


def b5_holds(rows, d):
    polys = []
    for rs in itertools.combinations(range(len(rows)), 3):
        for cs in itertools.combinations(range(d), 3):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
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
    rng = random.Random(86420)
    tot = fails = deg_check = 0
    for _ in range(400):
        d = 4
        U = AI.row_basis([[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(4)])
        if len(U) != 3:
            continue
        Tm = [[Fr(rng.randint(-2, 2)) for _ in range(3)] for _ in range(3)]
        rows = []
        for i in range(3):
            Ti = [sum(Tm[i][j] * U[j][k] for j in range(3)) for k in range(d)]
            rows.append((U[i], Ti))
        rows.append(([Fr(0)] * d, [Fr(0)] * d))
        tot += 1
        if not b5_holds(rows, d):
            fails += 1
        M3 = [[[-rows[i][1][j], rows[i][0][j]] for j in range(3)] for i in range(3)]
        p = V.det_poly(M3)
        if (len(p) == 4) or (len(p) == 1 and p[0] == 0):
            deg_check += 1
    print(f"mu=0：{tot} 个实例；(5b) 不成立: {fails}")
    print(f"  det(lam U - C) 为'非零三次'或'恒零': {deg_check}/{tot}")


if __name__ == '__main__':
    main()
