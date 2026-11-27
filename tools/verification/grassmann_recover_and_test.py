r"""Grassmann 判据 → 精确 $R$ → 谱判定（专家 §7 "结果 ③" 的完整实现）。

对每个满足判据的 $S$：
 1. 取 $x_1,\ldots,x_d\in X_S$ 使其像张成 $S/E$（$d=\omega-\dim E$），补零到 $m$ 行 ⟹ $B_1$；
 2. 对每个 $x_i$ 解 $x_iZ_1+y_iZ_2=0$ 得 $y_i\in S$ ⟹ $B_2$；
 3. 由 Prop 2 解 $R N_K=B_1$、$R A N_K=B_2$ 得精确 $R$；
 4. 在 $R$ 上算 $P=\lambda H-H_A$ 的全部 2 阶子式的 **精确一元 gcd**（自写 Euclid，无 CAS）⟹ 好/坏。
"""

from fractions import Fraction as Fr
import itertools

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


def solve_cols(M, rhs):
    """解 M z = rhs（列向量，M 为 list of rows）；返回一个特解或 None。"""
    if not M:
        return None
    rows, cols = len(M), len(M[0])
    A = [[F(M[i][j]) for j in range(cols)] + [F(rhs[i])] for i in range(rows)]
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols + 1)]
        piv.append(c)
        r += 1
    for i in range(r, rows):
        if all(A[i][j] == 0 for j in range(cols)) and A[i][cols] != 0:
            return None
    z = [F(0)] * cols
    for i, c in enumerate(piv):
        z[c] = A[i][cols]
    return z


# ---------- 一元多项式（低次在前，Fraction 系数） ----------
def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdeg(p):
    p = ptrim(list(p))
    return -1 if (len(p) == 1 and p[0] == 0) else len(p) - 1


def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return ptrim(out)


def psub(p, q):
    n = max(len(p), len(q))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (p[i] if i < len(p) else F(0)) - (q[i] if i < len(q) else F(0))
    return ptrim(out)


def pdivmod(p, q):
    p = ptrim(list(p)); q = ptrim(list(q))
    if pdeg(q) < 0:
        raise ZeroDivisionError
    r = list(p)
    quot = [F(0)] * max(1, len(p) - len(q) + 1)
    while pdeg(r) >= pdeg(q):
        d = pdeg(r) - pdeg(q)
        f = r[pdeg(r)] / q[pdeg(q)]
        quot[d] = f
        for i in range(len(q)):
            r[i + d] -= f * q[i]
        ptrim(r)
    return ptrim(quot), ptrim(r)


def pgcd(p, q):
    p, q = ptrim(list(p)), ptrim(list(q))
    while pdeg(q) >= 0:
        _, r = pdivmod(p, q)
        p, q = q, r
    return p


def main():
    # ---- 数据（K-坐标 basis e2,e3,e4）----
    Z1 = [[F(0), F(-1)], [F(-1), F(0)], [F(0), F(0)]]
    Z2 = [[F(1), F(0)], [F(0), F(1)], [F(0), F(0)]]
    Erow = [F(0), F(0), F(1)]           # L0 N_K
    F0rows = []                          # L0 A N_K = 0
    omega, m = 2, 2

    # 原始数据（用于回代求 R）
    n = 5
    C = [[F(1), F(0), F(0), F(0), F(0)]]
    A = [[F(0), F(0), F(0), F(0), F(1)],
         [F(0), F(0), F(1), F(0), F(0)],
         [F(0), F(1), F(0), F(0), F(0)],
         [F(0), F(0), F(0), F(0), F(0)],
         [F(0), F(0), F(0), F(1), F(0)]]
    # N_K 的**列**是 K 的基（e2,e3,e4）⟹ n×k，行是坐标分量
    NK = [[F(0), F(0), F(0)],
          [F(1), F(0), F(0)],           # e2
          [F(0), F(1), F(0)],           # e3
          [F(0), F(0), F(1)],           # e4
          [F(0), F(0), F(0)]]
    ANK = [[sum(A[i][t] * NK[t][j] for t in range(n)) for j in range(3)] for i in range(n)]

    def rowtimes(vec, M):
        return [sum(vec[t] * M[t][j] for t in range(len(vec))) for j in range(len(M[0]))]

    for sc in ([F(1), F(1), F(0)], [F(1), F(-1), F(0)]):
        # S = {x : x·sc = 0}
        Srows = []
        for j in range(3):
            pass
        # 解 x sc = 0（sc 视为列）
        Mx = [[sc[0]], [sc[1]], [sc[2]]]
        # 求核：x 为行向量，x Mx = 0
        # 直接解：a1 sc1 + a2 sc2 + a3 sc3 = 0
        # 两个明显基（sc 有两个非零项）
        nz = [i for i in range(3) if sc[i] != 0]
        assert len(nz) == 2, sc
        i0, i1 = nz
        if i0 == 0 and i1 == 1:
            Srows = [[sc[1], -sc[0], F(0)], [F(0), F(0), F(1)]]
        else:
            raise NotImplementedError
        assert rank(Srows) == omega
        # X_S = {x in S : x Z1 ∈ S·Z2}
        SZ2 = [rowtimes(y, Z2) for y in Srows]
        X = [x for x in Srows if rank(SZ2 + [[-v for v in rowtimes(x, Z1)]]) == rank(SZ2)]
        d = omega - rank([Erow])
        # 选 x1..xd 使 E + span{x_i} = S
        chosen = []
        for x in X:
            trial = [Erow] + chosen + [x]
            if rank(trial) == len(trial) and rank(trial + [y for y in Srows]) >= omega:
                chosen.append(x)
            if len(chosen) == d:
                break
        if len(chosen) < d:
            # 退一步：直接找使 E+span 张成 S 的组合
            for comb in itertools.combinations(X, d):
                if rank([Erow] + list(comb)) == omega:
                    chosen = list(comb)
                    break
        assert len(chosen) == d, (sc, X)
        # 找 y_i
        B1, B2 = [], []
        for x in chosen:
            xZ1 = rowtimes(x, Z1)
            # 解 y Z2 = -xZ1, y in S（参数化 y = a·Srows_0 + b·Srows_1）
            # 未知 a,b；方程 2 个
            Meq = [[Srows[0][t] * Z2[t][k] for t in range(3)] for k in range(2)]
            # 行 k：sum_t (a S0_t + b S1_t) Z2[t][k] = -xZ1[k]
            Meq = [[sum(Srows[0][t] * Z2[t][k] for t in range(3)),
                    sum(Srows[1][t] * Z2[t][k] for t in range(3))] for k in range(2)]
            sol = solve_cols(Meq, [-v for v in xZ1])
            assert sol is not None, (sc, x)
            y = [sol[0] * Srows[0][t] + sol[1] * Srows[1][t] for t in range(3)]
            assert rowtimes(y, Z2) == [-v for v in xZ1]
            B1.append(x)
            B2.append(y)
        while len(B1) < m:
            B1.append([F(0)] * 3)
            B2.append([F(0)] * 3)
        H = [Erow] + B1
        HA = [list(r) for r in F0rows] + B2
        while len(HA) < 3:            # 顶部行 (L0 A N_K = 0) 仍是**零行**
            HA = [[F(0)] * 3] + HA
        print(f'\nsigma = {[str(v) for v in sc]}  ⟹  S 基 = {[[str(v) for v in r] for r in Srows]}')
        print('  B1 =', [[str(v) for v in r] for r in B1], ' B2 =', [[str(v) for v in r] for r in B2])
        print('  rank H =', rank(H), ' rank[H;H_A] =', rank(H + HA))
        # 解 R (2x5)：R N_K = B1, R A N_K = B2
        rows_eq, rhs = [], []
        for j in range(3):
            for i in range(2):
                row = [F(0)] * 10
                for t in range(n):
                    row[i * n + t] = NK[t][j]
                rows_eq.append(row); rhs.append(B1[i][j])
        for j in range(3):
            for i in range(2):
                row = [F(0)] * 10
                for t in range(n):
                    row[i * n + t] = ANK[t][j]
                rows_eq.append(row); rhs.append(B2[i][j])
        Rv = solve_cols(rows_eq, rhs)
        print('  R 可解?', Rv is not None)
        if Rv is None:
            continue
        R = [Rv[i * n:(i + 1) * n] for i in range(2)]
        # 谱判定：P = λH − H_A 的 2 阶子式的精确 gcd
        minors = []
        for rr in itertools.combinations(range(3), 2):
            for cc in itertools.combinations(range(3), 2):
                p = [F(0)] * 3
                # det_{rr,cc} (λH − H_A) = λ²·det H[rr,cc] − λ·(混合项) + det H_A[rr,cc]
                h = [[H[i][j] for j in cc] for i in rr]
                hA = [[HA[i][j] for j in cc] for i in rr]
                detH = h[0][0] * h[1][1] - h[0][1] * h[1][0]
                detHA = hA[0][0] * hA[1][1] - hA[0][1] * hA[1][0]
                mix = (h[0][0] * hA[1][1] + hA[0][0] * h[1][1]
                       - h[0][1] * hA[1][0] - hA[0][1] * h[1][0])
                p[2] = detH
                p[1] = -mix
                p[0] = detHA
                minors.append(ptrim(p))
        g = None
        for p in minors:
            if pdeg(p) >= 0:
                g = p if g is None else pgcd(g, p)
        good = (g is not None and pdeg(g) == 0)
        print('  子式 =', [[str(c) for c in p] for p in minors], ' gcd 次数 =', pdeg(g) if g else None)
        print('  ⟹', '好（可行）' if good else '坏（不可行）')


if __name__ == '__main__':
    main()
