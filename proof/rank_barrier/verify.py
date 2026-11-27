r"""秩屏障（proof/rank_barrier/README.md 命题 1）的精确复核。

对随机实例与随机 $\lambda_0$ 检查两条：
  (i)  rank[λ0 L − LA; CA; C] ≤ j + r(λ0)，其中 r(λ0) = rank[λ0 I − A; C; CA] − j；
  (ii) 若 ρ > r(λ0)，则 rank[λ0 L − LA; CA; C] < r0 = rank[L; CA; C]。

并额外检查：λ0 不是特征值时 r(λ0) = d（推论 1 的依据）。

用法：python proof/rank_barrier/verify.py [--trials 300]
验证 ≠ 证明（CLAUDE §4）。
"""
import random
import sys
from fractions import Fraction as F


def mm(X, Y):
    assert len(X[0]) == len(Y), 'dim mismatch'
    return [[sum(F(X[i][k]) * F(Y[k][j]) for k in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def rank(M):
    if not M:
        return 0
    M = [[F(x) for x in r] for r in M]
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def one_case(rng, n):
    A = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    C = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(rng.choice([1, 1, 2]))]
    L0 = [[rng.randint(-2, 2) for _ in range(n)]]
    CA = mm(C, A)
    J = C + CA
    j = rank(J)
    if j >= n:
        return None
    q = j + rng.randint(1, n - j)
    L = [L0[0][:]] + [[rng.randint(-2, 2) for _ in range(n)] for _ in range(q - 1)]
    if rank(L) < q:
        return None
    r0 = rank(L + J)                      # = j + ρ
    rho = r0 - j
    lams = [F(0), F(1), F(-1), F(2), F(-2), F(1, 2), F(rng.randint(-3, 3))]
    out = []
    for lam in lams:
        M = [[(lam if a == b else 0) - A[a][b] for b in range(n)] for a in range(n)]
        r_lam = rank(M + C + CA) - j      # r(λ0)
        LA = mm(L, A)
        lhs = rank([[lam * L[i][k] - LA[i][k] for k in range(n)] for i in range(len(L))]
                   + CA + C)
        assert lhs <= j + r_lam, '秩不等式失败'
        if rho > r_lam:
            assert lhs < r0, 'ρ>r(λ0) 却秩满'
            fail = True
        else:
            fail = None
        off_spec = (rank([[M[a][b] for b in range(n)] for a in range(n)]) == n)
        if off_spec:
            assert r_lam == n - j, '非特征值处 r(λ0) 应等于 d'
        out.append((lhs, r0, r_lam, fail))
    return out


def main():
    trials = 300
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261030)
    checked = fails = 0
    for _ in range(trials):
        res = one_case(rng, rng.choice([4, 4, 5]))
        if not res:
            continue
        for lhs, r0, r_lam, fail in res:
            checked += 1
            if fail:
                fails += 1
    print(f'秩不等式 + 必失败方向：{checked} 次检查全部通过 ✓')
    print(f'其中 "ρ>r(λ0) ⟹ 该 λ0 处失败"：{fails} 例 ✓')

    # 定向测试：rank(A) ≤ 1 的实例 ⟹ r(0) ≤ 1 ⟹ 任何 ρ ≥ 2 的层在 λ=0 处必失败
    directed = 0
    for _ in range(120):
        n = 5
        u = [rng.randint(-2, 2) for _ in range(n)]
        v = [rng.randint(-2, 2) for _ in range(n)]
        A = [[F(u[i] * v[j]) for j in range(n)] for i in range(n)]
        C = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(2)]
        CA = mm(C, A)
        J = C + CA
        j = rank(J)
        if j >= n:
            continue
        q = min(n, j + rng.randint(2, n - j))
        L = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(q)]
        if rank(L) < q:
            continue
        r0 = rank(L + J)
        rho = r0 - j
        if rho < 2:
            continue
        M0 = [[-A[a][b] for b in range(n)] for a in range(n)]
        r_zero = rank(M0 + C + CA) - j
        LA = mm(L, A)
        lhs = rank([[-LA[i][k] for k in range(n)] for i in range(len(L))] + CA + C)
        assert r_zero <= 1, 'rank(A)≤1 时 r(0) 应 ≤1'
        assert rho > r_zero and lhs < r0, '定向测试失败'
        directed += 1
    print(f'定向测试（rank(A)≤1，ρ≥2）：{directed} 例在 λ=0 处全部失败 ✓')

    # §82 反例：r(0) = 1 < 3 = ρ ⟹ (3,1) 层在 λ=0 处必失败
    import itertools
    A = [[-1, 0, 2, 1, -1, -1], [0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
         [-2, -1, 4, 2, -2, -2], [-2, 0, 4, 2, -2, -2], [0, -2, 0, 0, 0, 0]]
    C = [[2, 1, -2, 2, -1, -1], [2, 2, 2, 1, -1, 1]]
    A = [[F(x) for x in r] for r in A]
    C = [[F(x) for x in r] for r in C]
    CA = mm(C, A)
    J = C + CA
    j = rank(J)
    M0 = [[(0 if a == b else 0) - A[a][b] for b in range(6)] for a in range(6)]
    r0 = rank(M0 + C + CA) - j
    print(f'§82 实例：j={j}、r(0)={r0} ⟹ 任何 ρ>r(0) 的层（含 (3,1)）在 λ=0 处必失败 ✓')
    assert j == 3 and r0 == 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
