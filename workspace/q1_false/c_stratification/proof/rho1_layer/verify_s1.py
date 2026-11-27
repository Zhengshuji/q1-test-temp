"""S1 区判据的精确验证 v2（验证 ≠ 证明）。

被测命题：[theorem.md §24.3 / §25.3]
    设 c >= rho-1、rho >= 2，则第 (rho,c) 层可行  <=>  dim{ b in B : T(b) in B } >= rho .

v1 的教训（v1 已备份到 trash/verify_s1_v1.py.bak）：
  * v1 把 (5a) 写成 T(U) ⊆ U+B —— **错的**；正确形式是 T(U) ⊆ U（docs/02 A.0）；
  * v1 的 cond_5b 最初只查秩下界（gcd），会假阳性；必须同时查 (rho+1) 子式恒零。

本版要点：
  * 强制真实 (5a)：T(U) ⊆ U；
  * 于是 T(u)+beta(tau) ∈ U（当 beta(tau) ∈ U），秩上界自动成立；
  * q(lam) 的行：lam*u_i - (T(u_i)+beta(tau_i)) 与 -beta(h_s)；两个方向都查。
构造：先取 B 与 U，再令 T 在 U 上为单位、其它随机（保证 T(U) ⊆ U）；beta 把 Q^m 的基映到 B。
"""
import itertools
import random
import sys
from fractions import Fraction as F

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


# ---------- 多项式（系数从低到高，Fraction） ----------
def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdivmod(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        c = r[-1] / b[-1]
        dd = len(r) - len(b)
        q[dd] = c
        for i, bi in enumerate(b):
            r[i + dd] -= c * bi
        r = ptrim(r)
    return ptrim(q), ptrim(r)


def pgcd(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    while not (len(b) == 1 and b[0] == 0):
        _, r = pdivmod(a, b)
        a, b = b, r
    return a


def _pmul(a, b):
    o = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return ptrim(o)


def _padd(a, b):
    o = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] += x
    for i, y in enumerate(b):
        o[i] += y
    return ptrim(o)


def _det(M):
    n = len(M)
    if n == 1:
        return ptrim(list(M[0][0]))
    acc = [F(0)]
    for j in range(n):
        sub = [r[:j] + r[j + 1:] for r in M[1:]]
        term = _pmul(M[0][j], _det(sub))
        if j % 2 == 1:
            term = [-c for c in term]
        acc = _padd(acc, term)
    return ptrim(acc)


def minors_pencil(rows, rho, d):
    out = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(d), rho):
            out.append(_det([[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]))
    return out


def cond_5b(rows, rho, d):
    """rank Q(lam) = rho 对一切 lam：两个方向都查。"""
    if rho + 1 <= min(len(rows), d):
        for m in minors_pencil(rows, rho + 1, d):
            if not (len(m) == 1 and m[0] == 0):
                return False
    mins = [m for m in minors_pencil(rows, rho, d) if not (len(m) == 1 and m[0] == 0)]
    if not mins:
        return False
    g = mins[0]
    for m in mins[1:]:
        g = pgcd(g, m)
    return len(g) == 1 and g[0] != 0


# ---------- 线性代数 ----------
def rank(vs):
    return AI.rank(vs) if vs else 0


def in_span(vs, v):
    return rank(vs + [v]) == rank(vs)


def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def e(k, d):
    return [F(1) if i == k else F(0) for i in range(d)]


def main():
    rng = random.Random(20261028)
    nI = nII = 0
    badI = badII = 0
    for _ in range(600):
        d = rng.choice([3, 4])
        m = rng.choice([2, 3])
        if m > d:
            continue
        rho = 2 if d == 3 else rng.choice([2, 3])
        if rho > d:
            continue
        c = rho - 1
        B = [e(k, d) for k in range(m)]
        branchI = rng.random() < 0.5
        if branchI:
            if m < rho:
                continue
            U = [e(k, d) for k in range(rho)]
        else:
            if m < rho - 1:
                continue
            W0 = [e(k, d) for k in range(rho - 1)]
            u = None
            for _t in range(20):
                cand = [F(rng.randint(-2, 2)) for _ in range(d)]
                if any(cand) and not in_span(W0, cand):
                    u = cand
                    break
            if u is None:
                continue
            U = W0 + [u]
            if rank(U) != rho:
                continue
        # T：U 上取单位，其它随机；再整体检查 T(U) ⊆ U
        T = [[F(1) if i == j else F(0) for j in range(d)] for i in range(d)]
        for i in range(d):
            for j in range(d):
                if rng.random() < 0.3:
                    T[i][j] += F(rng.randint(-2, 2))
        if not all(in_span(U, mat_vec(T, x)) for x in U):
            continue
        K = [b for b in B if in_span(B, mat_vec(T, b))]
        crit = rank(K) >= rho
        if branchI != crit:
            continue                      # 只保留与分支意图一致的实例
        BU = [x for x in U if in_span(B, x)]
        if rank(BU) < c:
            continue

        def beta(tau):
            return [sum((tau[k] * B[k][i] for k in range(m)), F(0)) for i in range(d)]

        rows_H = [beta(e(k, m)) for k in range(c)]
        feas = []
        for _t in range(5):
            # tau 必须落在 A 里：beta(tau_i) ∈ B∩U = <e_1..e_c>
            tau = [[F(rng.randint(-1, 1)) if k < c else F(0) for k in range(m)] for _ in range(rho)]
            rows = [(x, [mat_vec(T, x)[i] + beta(tau[k])[i] for i in range(d)])
                    for k, x in enumerate(U)]
            rows += [([F(0)] * d, h) for h in rows_H]
            feas.append(cond_5b(rows, rho, d))
        if crit:
            nI += 1
            if not any(feas):
                badI += 1
                if badI <= 3:
                    print(f"[I] 不一致 d={d} m={m} rho={rho} feas={feas}")
        else:
            nII += 1
            if any(feas):
                badII += 1
                if badII <= 3:
                    print(f"[II] 不一致 d={d} m={m} rho={rho} feas={feas}")
    print(f"(I) 判据为真 {nI} 例，不一致 {badI}；(II) 判据为假 {nII} 例，不一致 {badII}")
    print("结论：0 不一致 => 判据与抽象模型逐例一致（**验证，不是证明**）")


if __name__ == '__main__':
    main()
