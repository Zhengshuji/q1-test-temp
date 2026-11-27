"""在**真实实例** $(A,C,L_0)$ 上验证格子级判据（定理 2/5/11）。

做法：
  1. 用 quotient_selfcheck.py 的 Quotient 实现商空间；
  2. 取 3 维 U ⊆ X（含 U0），取补空间 W（X = U ⊕ W）；
  3. 对 u_i ∈ U：取 barT(u_i) 在 X 中的代表，按 X = U ⊕ W 分解，U 分量记 t_i；
  4. E = B ∩ U；w ∈ E 非零；取 h ∈ J 使 pi(hA) = w；
  5. 铅笔（U 坐标）：行 λ u_i − t_i − e_i（e_i ∈ E）与 −w；
  6. 直接测：抽样 e_i，判定是否 (5b)；
  7. 判据（定理 11）：被覆盖 ⟺ T（以 t_i 为行）有特征向量 v 使 w^T v = 0。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI
import importlib.util

spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = importlib.util.spec_from_file_location('V', 'proof/rho1_layer/verify_mu1_criterion.py')
V = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(V)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def solve_for_h(Q, w):
    """找 h ∈ J 使 pi(h A) = w（E 在 U 内，w 是 X 坐标）。"""
    # 未知数：J 的系数 a；方程：pi(a J A) = w
    rows = [Q.pi(mm([[Q.J[i][k] for k in range(Q.n)]], Q.A)[0]) for i in range(Q.j)]
    # 解 sum a_i rows[i] = w
    sysm = [[rows[i][t] for i in range(Q.j)] + [w[t]] for t in range(Q.d)]
    R = AI.rref(sysm)[0]
    sol = [Fr(0)] * Q.j
    for row in R:
        for t in range(Q.j):
            if row[t] != 0:
                sol[t] = row[Q.j] / row[t]
                break
    h = [sum(sol[i] * Q.J[i][k] for i in range(Q.j)) for k in range(Q.n)]
    return h


def pencil_minors_gcd_one(rows, rho, d):
    g = None
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(d), rho):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            v = V.det_poly(M)
            if len(v) == 1 and v[0] == 0:
                continue
            g = v if g is None else V.pgcd(g, v)
            if len(g) == 1 and g[0] != 0:
                return True
    if g is None:
        return False
    return len(g) == 1 and g[0] != 0


def has_eig_perp(T, w):
    """T 是否有特征向量 v 满足 w^T v = 0（w 作为行向量）。"""
    rows = [[[-T[i][j], Fr(1) if i == j else Fr(0)] for j in range(3)] for i in range(3)]
    rows.append([[w[j]] for j in range(3)])
    polys = []
    for rs in itertools.combinations(range(4), 3):
        for cs in itertools.combinations(range(3), 3):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return True          # 全部为零 => 任何 v 都是"零化"的极端情形
    g = polys[0]
    for q in polys[1:]:
        g = V.pgcd(g, q)
    return not (len(g) == 1 and g[0] != 0)   # 有公共根 <=> 存在这样的特征向量


def main():
    rng = random.Random(777)
    rows = []
    for trial in range(40):
        n = rng.choice([4, 5])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(1)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        Q = Qm.Quotient(A, C)
        if Q.d < 3 or Q.m == 0:
            continue
        U0 = rb([Q.pi(r) for r in L0])
        if len(U0) > 3:
            continue
        # 取含 U0 的 3 维 U
        while True:
            U = rb(U0 + [[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(3)])
            if len(U) == 3:
                break
        # E = B ∩ U
        # μ = dim(B ∩ U)：维数公式（§61：不能数"B 的基向量里有多少个落在 U 里" ✗）
        mu = len(Q.B) + len(U) - rank(Q.B + U)
        E = []
        if mu > 0:
            _rows = [[Q.B[i][k] for i in range(len(Q.B))] + [-U[j][k] for j in range(len(U))] for k in range(Q.d)]
            for _sol in AI.nullspace(_rows):
                _v = [sum(_sol[i] * Q.B[i][k] for i in range(len(Q.B))) for k in range(Q.d)]
                if any(_v):
                    E.append(_v)
            E = rb(E)
        mu = len(E)
        if mu < 1:
            continue
        # w ∈ E 非零；h 使 pi(hA)=w
        w = E[0]
        if not any(w):
            continue
        h = solve_for_h(Q, w)
        # 补空间 W（X = U ⊕ W），把 barT(u_i) 的代表分解
        W = Qm.complement(U, Q.d)
        def decompose(x):
            # 解 x = sum a_i U_i + sum b_j W_j
            L = U + W
            Linv = AI.inv(L)
            c = mm([x], Linv)[0]
            return c[:len(U)], c[len(U):]
        Trows = []
        for u in U:
            ubar = Q.Tbar(u)                       # X/B 的坐标
            rep = [sum(ubar[k] * Q.Bcomp[k][j] for k in range(len(ubar))) for j in range(Q.d)]
            upart, _ = decompose(rep)
            Trows.append(upart)
        # 判据
        crit = has_eig_perp(Trows, w)
        # 直接测：抽样 e_i ∈ E
        found = False
        for _t in range(40):
            cs = [[Fr(rng.randint(-2, 2)) for _ in E] for _ in range(3)]
            prow = []
            for i in range(3):
                e = [sum(cs[i][k] * E[k][j] for k in range(len(E))) for j in range(3)]
                prow.append((U[i], [Trows[i][j] + e[j] for j in range(3)]))
            prow.append(([Fr(0)] * 3, list(w)))
            if pencil_minors_gcd_one(prow, 3, 3):
                found = True
                break
        rows.append((mu, crit, not found))
    # 统计
    agree = sum(1 for mu, c, cov in rows if c == cov)
    print(f"真实实例的格子：{len(rows)} 个")
    print(f"  判据（被覆盖 <=> 有 v 使 w^T v=0）与直接测量一致：{agree}/{len(rows)}")
    from collections import Counter
    print("  按 mu 分布：", Counter(mu for mu, _, _ in rows))
    bad = [(mu, c, cov) for mu, c, cov in rows if c != cov]
    if bad:
        print("  不一致（mu, 判据, 直接）:", bad[:5])


if __name__ == '__main__':
    main()
