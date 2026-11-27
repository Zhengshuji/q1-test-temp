r"""函数域/显式点计算：$q=3$、$\omega=2$ 层上找一个**好点** ⟹ 该实例 $q_{\min}=3$。

实例：$n=4,p=1,r=1$，$C=e_1^{\mathsf T}$、$A$ 第一行 $e_4^{\mathsf T}$、列 2,3 = $e_3,e_2$；$L_0=e_3^{\mathsf T}$。
$K=\langle e_2,e_3\rangle$、$N_K=[e_2,e_3]$；$E=\operatorname{row}(L_0N_K)=(0,1)$、$F_0=\operatorname{row}(L_0AN_K)=(1,0)$；
$Z_1=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$、$Z_2=I_2$。

取 $B_1=\begin{pmatrix}1&0\\1&1\end{pmatrix}$（两行都不平行于 $E$）、$B_2=-B_1Z_1$（⟹ 可达性 $B_1Z_1+B_2Z_2=0$ ✓）。
构造 $H=[E;B_1]$、$H_A=[F_0;B_2]$；算 $P=\lambda H-H_A$ 的三个 2 阶子式的精确 gcd。
"""

from fractions import Fraction as Fr
import itertools

F = Fr


def pdeg(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return -1 if (len(p) == 1 and p[0] == 0) else len(p) - 1


def pdivmod(p, q):
    p = list(p); q = list(q)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    r = list(p)
    quot = [F(0)] * max(1, len(p) - len(q) + 1)
    while pdeg(r) >= pdeg(q):
        d = pdeg(r) - pdeg(q)
        f = r[pdeg(r)] / q[pdeg(q)]
        quot[d] = f
        for i in range(len(q)):
            r[i + d] -= f * q[i]
        while len(r) > 1 and r[-1] == 0:
            r.pop()
    return quot, r


def pgcd(p, q):
    p, q = list(p), list(q)
    while pdeg(q) >= 0:
        _, r = pdivmod(p, q)
        p, q = q, r
    return p


def matmul(X, Y):
    return [[sum(X[i][t] * Y[t][j] for t in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def rank(M):
    if not M:
        return 0
    A = [list(map(F, row)) for row in M]
    r, rows, cols = 0, len(A), len(A[0])
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        r += 1
    return r


def main():
    E = [[F(0), F(1)]]
    F0 = [[F(1), F(0)]]
    Z1 = [[F(0), F(-1)], [F(-1), F(0)]]
    Z2 = [[F(1), F(0)], [F(0), F(1)]]
    B1 = [[F(1), F(0)], [F(1), F(1)]]
    B2 = [[-v for v in row] for row in matmul(B1, Z1)]      # B2 = −B1 Z1
    # 可达性检查
    chk = [[sum(matmul(B1, Z1)[i][j] + matmul(B2, Z2)[i][j] for _ in [0]) for j in range(2)]
           for i in range(2)]
    print('B1 Z1 + B2 Z2 =', [[str(v) for v in r] for r in chk], '（应全 0）')
    H = E + B1
    HA = F0 + B2
    print('H =', [[str(v) for v in r] for r in H], '  rank =', rank(H))
    print('H_A =', [[str(v) for v in r] for r in HA], ' rank =', rank(HA))
    print('rank[H;H_A] =', rank(H + HA), '（= 2 ⟹ (5a) ✓）')
    minors = []
    for rr in itertools.combinations(range(3), 2):
        for cc in itertools.combinations(range(2), 2):
            h = [[H[i][j] for j in cc] for i in rr]
            hA = [[HA[i][j] for j in cc] for i in rr]
            detH = h[0][0] * h[1][1] - h[0][1] * h[1][0]
            detHA = hA[0][0] * hA[1][1] - hA[0][1] * hA[1][0]
            mix = (h[0][0] * hA[1][1] + hA[0][0] * h[1][1]
                   - h[0][1] * hA[1][0] - hA[0][1] * h[1][0])
            minors.append([detHA, -mix, detH])
    print('子式（低次在前）=', [[str(c) for c in p] for p in minors])
    g = None
    for p in minors:
        if pdeg(list(p)) >= 0:
            g = list(p) if g is None else pgcd(g, list(p))
    print('gcd =', [str(c) for c in g] if g else None, ' 次数 =', pdeg(g) if g else None)
    print('⟹', '好（可行）→ q_min = 3' if (g and pdeg(g) == 0) else '坏')




def scan():
    """扫描 B_1 的两行（小整数），看是否存在**好点**（gcd 的次数 = 0）。"""
    E = [[F(0), F(1)]]
    F0 = [[F(1), F(0)]]
    Z1 = [[F(0), F(-1)], [F(-1), F(0)]]
    Z2 = [[F(1), F(0)], [F(0), F(1)]]
    good, bad = [], []
    for a1 in range(-2, 3):
        for b1 in range(-2, 3):
            for a2 in range(-2, 3):
                for b2 in range(-2, 3):
                    B1 = [[F(a1), F(b1)], [F(a2), F(b2)]]
                    if rank(B1) < 2:
                        continue
                    B2 = [[-v for v in row] for row in matmul(B1, Z1)]
                    H = E + B1
                    HA = F0 + B2
                    if rank(H) != 2 or rank(H + HA) != 2:
                        continue
                    minors = []
                    for rr in itertools.combinations(range(3), 2):
                        h = [H[rr[0]], H[rr[1]]]
                        hA = [HA[rr[0]], HA[rr[1]]]
                        detH = h[0][0] * h[1][1] - h[0][1] * h[1][0]
                        detHA = hA[0][0] * hA[1][1] - hA[0][1] * hA[1][0]
                        mix = (h[0][0] * hA[1][1] + hA[0][0] * h[1][1]
                               - h[0][1] * hA[1][0] - hA[0][1] * h[1][0])
                        minors.append([detHA, -mix, detH])
                    g = None
                    for p in minors:
                        if pdeg(list(p)) >= 0:
                            g = list(p) if g is None else pgcd(g, list(p))
                    ok = (g is not None and pdeg(g) == 0)
                    (good if ok else bad).append(((a1, b1, a2, b2), pdeg(g) if g else None))
    print(f'扫描：好 {len(good)} 个，坏 {len(bad)} 个（B1 的非奇异小整数取法）')
    for t in good[:5]:
        print('  好点：(a1,b1,a2,b2) =', t[0])
    if good:
        print('⟹ 该层**存在好点** ⟹ q_min = 3')
    else:
        print('⟹ 扫描范围内**全坏**（提示：该层可能整层坏 ⟹ q_min >= 4，但需证明）')


if __name__ == '__main__':
    main()
    scan()
