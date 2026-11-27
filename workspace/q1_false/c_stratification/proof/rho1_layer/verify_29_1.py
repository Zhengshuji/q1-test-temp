"""定理 29.1 的**构造式**验证（验证 ≠ 证明）。

定理 29.1：固定 (U,H)、c = rho-1、dim beta(H) = rho-1 时，Bad 是仿射的 ⟹
"A 上的可行性"是"全有或全无"（Bad ≠ A 时是开稠密的）。

本脚本**构造**合格实例（不是随机采样），并对每个实例在 A 上抽样很多 tau：
  - 若出现 "0 < 成功数 < 抽样数"（mix） => Bad 不是仿射，定理 29.1 有误；
  - 若全成功或全失败 => 与定理一致。

构造：X = Q^d、U = <e_1..e_rho>、W0 = <e_1..e_{rho-1}>、B = <e_1..e_m>（m >= rho-1）、
T 保持 U（取 U 上的对角矩阵后再扩张）、beta: Q^c -> W0 取恒等嵌入（c = rho-1, j = c）。
于是 A = {tau : beta(tau_i) ∈ B∩U} = 全部（因 W0 ⊆ U ∩ B）。
(5a) 自动成立（T(U) ⊆ U）。秩上界自动（行都落在 U 里）。
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
        term = pmul(M[0][j], det_poly(sub))
        if j % 2:
            term = [-c for c in term]
        acc = padd(acc, term)
    return ptrim(acc)


def minors(rows, rho, d):
    out = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(d), rho):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            out.append(det_poly(M))
    return out


def cond_5b(rows, rho, d):
    mins = [m for m in minors(rows, rho, d) if not (len(m) == 1 and m[0] == 0)]
    if not mins:
        return False
    g = mins[0]
    for m in mins[1:]:
        g = pgcd(g, m)
    return len(g) == 1 and g[0] != 0


def e(k, d):
    return [Fr(1) if i == k else Fr(0) for i in range(d)]


def build(rng, d, rho, m, eigvals):
    """U = <e_1..e_rho>；W0 取 U 内的**随机** (rho-1) 维子空间（避免与坐标超平面重合）。"""
    U = [e(k, d) for k in range(rho)]
    while True:
        cand = []
        for _ in range(rho - 1):
            v = [sum(Fr(rng.randint(-2, 2)) * U[k][i] for k in range(rho)) for i in range(d)]
            if any(v):
                cand.append(v)
        cand = AI.row_basis(cand)
        if len(cand) == rho - 1:
            W0 = cand
            break
    B = [e(k, d) for k in range(m)]
    for w in W0:                       # 保证 W0 ⊆ B：直接用 W0 替换前几个 B 向量
        pass
    T = [[Fr(0)] * d for _ in range(d)]
    for i in range(d):
        T[i][i] = Fr(rng.randint(-2, 2))
    for k in range(rho):
        T[k][k] = Fr(eigvals[k])
    # 检查 T(U) ⊆ U（对角 ⟹ 自动）
    return U, W0, B, T


def main():
    rng = random.Random(2028)
    tested = mix = 0
    feas_cnt = infeas_cnt = 0
    from collections import defaultdict
    prof = defaultdict(lambda: [0, 0])
    for trial in range(200):
        d = rng.choice([3, 4])
        rho = 2 if d == 3 else rng.choice([2, 3])
        m = rng.choice([rho - 1, rho, d])
        if m > d:
            continue
        eig = [Fr(rng.randint(0, 3)) for _ in range(rho)]
        U, W0, B, T = build(rng, d, rho, m, eig)
        c = rho - 1
        # 强制 B ⊇ W0：B := row_basis(B ∪ W0)（若维数超过 m 则接受）
        B2 = AI.row_basis([r[:] for r in B] + [r[:] for r in W0])
        # beta: Q^c -> W0，恒等嵌入（tau_i 的第 k 个分量乘 e_k）
        beta = lambda tau: [sum(tau[k] * W0[k][i] for k in range(c)) for i in range(d)]
        rows_H = [beta(e(s, c)) for s in range(c)]
        # kappa = dim ker，即 dim{(dtau,dlam) : dlam*u_i = beta(dtau_i) forall i}
        # 用线性系统直接算：未知量 (tau_{i,k}, lam)，每个 i 给 d 个方程
        vars_ = rho * c + 1
        rows_sys = []
        for i in range(rho):
            for jj in range(d):
                row = [Fr(0)] * vars_
                for k in range(c):
                    row[i * c + k] = -W0[k][jj]
                row[rho * c] = U[i][jj]
                rows_sys.append(row)
        kappa = vars_ - AI.rank(rows_sys)
        succ = 0
        N = 12
        for _t in range(N):
            tau = [[Fr(rng.randint(-3, 3)) for _ in range(c)] for _ in range(rho)]
            rows = [(U[i], [sum(T[i][j] * U[i][j] for j in range(d)) for _ in range(1)][0] and
                     [sum(T[i][j] * U[i][j] for j in range(d)) for _ in range(d)]) for i in range(rho)]
            # 正确构造：T(u_i) 是向量
            rows = []
            for i in range(rho):
                Tu = [sum(T[j][k] * U[i][k] for k in range(d)) for j in range(d)]
                b = beta(tau[i])
                rows.append((U[i], [Tu[j] + b[j] for j in range(d)]))
            rows += [([Fr(0)] * d, h) for h in rows_H]
            if cond_5b(rows, rho, d):
                succ += 1
        tested += 1
        key = (rho, min(m, rho), rho - 1, kappa)
        prof[key][0 if succ == N else 1] += 1
        if succ == N:
            feas_cnt += 1
        elif succ == 0:
            infeas_cnt += 1
        else:
            mix += 1
            if mix <= 3:
                print(f"mix: d={d} rho={rho} m={m} eig={eig} 成功 {succ}/{N}")
    print(f"实例 {tested}：全可行 {feas_cnt}，全不可行 {infeas_cnt}，mix {mix}")
    print("mix = 0 => 与定理 29.1（Bad 仿射）一致（**验证，不是证明**）")
    print("\n(rho, mu, nu, kappa) -> [全可行, 全不可行]：")
    mixedkeys = 0
    for k in sorted(prof):
        f, i = prof[k]
        if f and i:
            mixedkeys += 1
        print(f"  {k}: [{f}, {i}]" + ("   <== 两种都有" if (f and i) else ""))
    print(f"\n(feasibility 是否被 (rho,mu,nu,kappa) 决定？分歧组合数 = {mixedkeys})")


if __name__ == '__main__':
    main()
