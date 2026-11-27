"""S1 区真判据的经验搜索（验证 ≠ 证明）。

背景：§22–§26 给出的"充要判据 dim K >= rho"已被精确反例反驳。
本脚本改用**测试先行**：对随机实例与随机 V（按层号 (rho,c) 正确辨识），
同时记录不变量

    mu = dim(B ∩ U) = dim((JA+J) ∩ (V+J)) - j                （B = pi(JA), U = pi(V)）
    nu = dim(beta(H)) = dim(((V∩J) A) + J) - j               （H = V∩J）
    feas = (5a) ∧ (5b)

看 feas 是否能由 (mu, nu, rho, c, j) 决定。
"""
import random
import sys
from collections import defaultdict
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def rref_basis(rows, n):
    return AI.row_basis(rows)


def intersect_dim(X, Y, n):
    return len(AI.row_basis(X)) + len(AI.row_basis(Y)) - len(AI.row_basis([r[:] for r in X] + [r[:] for r in Y]))


def data(A, C, L):
    n = len(A)
    CA = mm(C, A)
    J = AI.row_basis(C + CA)
    j = len(J)
    VJ = AI.row_basis([r[:] for r in L] + [r[:] for r in J])
    rho = AI.rank(AI.vstack([L, CA, C])) - j
    c = len(L) + j - len(AI.row_basis([r[:] for r in L] + [r[:] for r in J]))
    JA = AI.row_basis(mm(J, A))
    JAJ = AI.row_basis([r[:] for r in JA] + [r[:] for r in J])
    mu = intersect_dim(JAJ, VJ, n) - j
    # H = V ∩ J
    H = []
    for r in AI.row_basis(J):
        if AI.rank([x[:] for x in L] + [r[:]]) == len(L):
            H.append(r)
    H = AI.row_basis(H)
    HA = AI.row_basis(mm(H, A)) if H else []
    nu = (len(AI.row_basis([r[:] for r in HA] + [r[:] for r in J])) - j) if H else 0
    return dict(j=j, rho=rho, c=c, mu=mu, nu=nu)


def main():
    rng = random.Random(20261029)
    table = defaultdict(lambda: [0, 0])          # key -> [feas, infeas]
    samples = []
    for _trial in range(4000):
        n = rng.choice([5, 6])
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        rows = []
        k = rng.choice([2, 3, 4])
        for _r in range(k):
            rows.append([Fr(rng.randint(-1, 1)) for _ in range(n)])
        L0 = [rows[0]]
        L = AI.row_basis(rows)
        if len(L) < 2:
            continue
        if not AI.cond_5a_orig(A, C, L):
            continue
        D = data(A, C, L)
        if D['rho'] < 1 or D['c'] < 1:
            continue
        feas = AI.cond_5b_orig(A, C, L)
        key = (D['rho'], D['c'], D['mu'], D['nu'])
        table[key][0 if feas else 1] += 1
        samples.append((D, feas))
    print("(rho,c,mu,nu) -> [可行, 不可行]（只列有分歧或样本>=3 的）")
    both = 0
    for key in sorted(table):
        f, i = table[key]
        flag = "  <== 两种都有" if (f and i) else ""
        if f and i:
            both += 1
        if f + i >= 3 or (f and i):
            print(f"  {key}: [{f}, {i}]{flag}")
    print(f"\n共有 {len(table)} 种组合；其中 '同一 (rho,c,mu,nu) 既有可行又有不可行' 的有 {both} 种")
    print("=> 若 both = 0，则 feas 可能只由 (rho,c,mu,nu) 决定；否则还需要更多不变量")


if __name__ == '__main__':
    main()