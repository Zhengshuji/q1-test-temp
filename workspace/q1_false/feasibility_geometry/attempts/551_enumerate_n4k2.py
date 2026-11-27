"""551：n=4,k=2,m=1 的系统枚举：A e1,A e2 取小向量，L0=[e1;e2]，r 符号。
打印 (5b) 的 gcd（作为 r 的多项式），找非退化例子。"""
import itertools
import sympy as sp

r1, r2, r3, r4, lam = sp.symbols('r1 r2 r3 r4 lam')
r = sp.Matrix([[r1, r2, r3, r4]])

basis = {
    '0': sp.Matrix([[0, 0, 0, 0]]),
    'e1': sp.Matrix([[1, 0, 0, 0]]),
    'e2': sp.Matrix([[0, 1, 0, 0]]),
    'e3': sp.Matrix([[0, 0, 1, 0]]),
    'e4': sp.Matrix([[0, 0, 0, 1]]),
}

out = []
for n1, v1 in basis.items():
    for n2, v2 in basis.items():
        AN = sp.Matrix.hstack(v1.T, v2.T)          # 4x2, columns A e1, A e2
        H = sp.Matrix.vstack(sp.Matrix([[1, 0], [0, 1]]), r[:, 0:2])
        HA = sp.Matrix.vstack(sp.Matrix([[1, 0], [0, 1]]),
                              r * AN)  # 2 fixed rows: e1,e2 -> (e1·AN, e2·AN)
        # 固定行 H_A: e1 N = (1,0) -> H_0 row; H_A row = e1 * AN
        HA = sp.Matrix.vstack(sp.Matrix([list((sp.Matrix([[1, 0, 0, 0]]) * AN)[0, :]),
                                         list((sp.Matrix([[0, 1, 0, 0]]) * AN)[0, :])]),
                              r * AN)
        P = lam * H - HA
        ms = []
        for i in range(3):
            for j in range(i + 1, 3):
                ms.append(sp.expand(P[i, 0] * P[j, 1] - P[i, 1] * P[j, 0]))
        ms = [m for m in ms if sp.expand(m) != 0]
        if not ms:
            continue
        g = sp.factor(sp.gcd_list(ms))
        deg = sp.degree(sp.expand(g), lam)
        out.append((n1, n2, deg, g))
        if len(out) >= 12:
            break
    if len(out) >= 12:
        break

for n1, n2, deg, g in out:
    print(n1, n2, 'deg', deg, 'gcd=', g)
