r"""检验 $k=\omega$ 定理：$k=2$、$\omega=2$、$q=3$（$n=4$、$p=1$、$r=1$）上的随机抽样。

定理预言：若存在好点，则好集在 $\mathcal U=\{\operatorname{rank}H=2\}$ 中**开稠密**，
故在 $\mathcal U$ 上随机抽样应几乎全为好点（比例接近 1）；若不存在好点，则抽样应几乎全为坏点。

同时核对：$(5a)$ 自动成立（因 $\ker H=0$，$\operatorname{rank}H=k$ 满列秩）。
"""

import itertools
import random
from fractions import Fraction as Fr

F = Fr


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
        if r == rows:
            break
    return r


def mul(X, Y):
    return [[sum(X[i][t] * Y[t][j] for t in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


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


def main():
    n, p, q, r = 4, 1, 3, 1
    C = [[F(1), F(0), F(0), F(0)]]
    A = [[F(0), F(0), F(0), F(1)],
         [F(0), F(0), F(1), F(0)],
         [F(0), F(1), F(0), F(0)],
         [F(0), F(0), F(0), F(0)]]
    # K = <e2,e3>
    NK = [[F(0), F(0)], [F(1), F(0)], [F(0), F(1)], [F(0), F(0)]]
    ANK = [[sum(A[i][t] * NK[t][j] for t in range(n)) for j in range(2)] for i in range(n)]
    L0 = [[F(0), F(0), F(1), F(0)]]
    E = mul(L0, NK)
    F0 = mul(mul(L0, A), NK)
    print('E =', [[str(x) for x in row] for row in E], ' F0 =', [[str(x) for x in row] for row in F0])
    print('K 的基列 =', [[str(NK[i][j]) for j in range(2)] for i in range(n)])
    print('注意：rank H = 2 = k ⟹ ker H = 0 ⟹ (5a) 自动成立（无需 row 包含条件）')

    rng = random.Random(20261120)
    ngood = nbad = nopen = 0
    trials = 400
    for _ in range(trials):
        R = [[F(rng.randrange(-3, 4)) for _ in range(n)] for _ in range(q - r)]
        H = E + mul(R, NK)
        HA = F0 + mul(mul(R, A), NK)
        if rank(H) != 2:
            nopen += 1
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
        for mm in minors:
            if pdeg(list(mm)) >= 0:
                g = list(mm) if g is None else pgcd(g, list(mm))
        ok = (g is not None and pdeg(g) == 0)
        if ok:
            ngood += 1
        else:
            nbad += 1
    print(f'{trials} 个随机 R：rank H < 2 的 {nopen} 个；其余 {ngood + nbad} 个中 好 {ngood} / 坏 {nbad}')
    frac = ngood / max(1, ngood + nbad)
    print(f'好点比例 = {frac:.3f}')
    print('⟹ 若接近 0：该实例在 k=omega 下**不可行**（generic gcd 非常数）')
    print('⟹ 若接近 1：**可行**且好集开稠密（符合定理）')
    print('⟹ 中间值：与"开稠密"不符，需要检查（可能是我方 gcd 实现有误）')


if __name__ == '__main__':
    main()
