"""端到端验证：从"格子判据说可行"出发，**构造出真正的 V**（C^n 里的行），
再用**堆叠判据**在 C^n 里核对 (5a) 和 (5b)。

流程：
  1. 真实实例 (A, C, L0)；
  2. 采样 3 维 U ⊆ X（含 U0），算 E = B ∩ U、t_i（U 分量）；
  3. 用（已证的）格子判据判断该格是否被覆盖；若不被覆盖，抽 e_i ∈ E 使 (5b) 成立；
  4. 用 e_i 反解 tau_i（要求 pi(tau_i A) = e_i），构造
        V 的行 = lift(u_i) + tau_i   (i=1..3)   再加一行 h（beta(h) = w）
     注意 L0 的行必须也在 V 里 —— 这里把 L0 的行并入 V 的生成元（它们已经在 U 内）；
  5. 在 C^n 里用堆叠判据验 (5a)、(5b)。
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
spec2 = importlib.util.spec_from_file_location('C', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(CV)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def solve_tau(Q, e):
    """找 tau ∈ J 使 pi(tau A) = e（e 是 X 坐标）。"""
    # 用 J 的基：rows[i] = pi(J_i A)
    rows = [Q.pi(mm([Q.J[i]], Q.A)[0]) for i in range(Q.j)]
    # 解 sum a_i rows[i] = e
    sysm = [[rows[i][t] for i in range(Q.j)] + [e[t]] for t in range(Q.d)]
    R = AI.rref(sysm)[0]
    sol = [Fr(0)] * Q.j
    for row in R:
        for t in range(Q.j):
            if row[t] != 0:
                sol[t] = row[Q.j] / row[t]
                break
    return [sum(sol[i] * Q.J[i][k] for i in range(Q.j)) for k in range(Q.n)]


def cond5a(V, A, C):
    CA = mm(C, A)
    VA = mm(V, A)
    return rank(VA + V + CA + C) == rank(V + CA + C)


def cond5b(V, A, C):
    """(5b)： 全部 r0 x r0 子式的 gcd 为非零常数（r0 = rank[L;CA;C]）。"""
    CA = mm(C, A)
    VA = mm(V, A)
    base = V + CA + C
    r0 = rank(base)
    rows = [(V[i], VA[i]) for i in range(len(V))]
    for r in CA:
        rows.append(([Fr(0)] * len(r), list(r)))
    for r in C:
        rows.append(([Fr(0)] * len(r), list(r)))
    g = None
    for rs in itertools.combinations(range(len(rows)), r0):
        for cs in itertools.combinations(range(len(V[0])), r0):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            v = CV.V.det_poly(M)
            if len(v) == 1 and v[0] == 0:
                continue
            g = v if g is None else CV.V.pgcd(g, v)
            if len(g) == 1 and g[0] != 0:
                return True            # 提前退出：已是非零常数
    if g is None:
        return False
    return len(g) == 1 and g[0] != 0


def main():
    rng = random.Random(4242)
    tried = feasible = end2end = 0
    for trial in range(60):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        Q = Qm.Quotient(A, C)
        if Q.d < 3 or Q.m == 0:
            continue
        U0 = rb([Q.pi(r) for r in L0])
        if len(U0) > 3:
            continue
        while True:
            U = rb(U0 + [[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(3)])
            if len(U) == 3:
                break
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
        if not E:
            continue
        w = E[0]
        if not any(w):
            continue
        W = Qm.complement(U, Q.d)
        Linv = AI.inv(U + W)
        decompose = lambda x: mm([x], Linv)[0][:3]
        Trows = []
        for u in U:
            ubar = Q.Tbar(u)
            rep = [sum(ubar[k] * Q.Bcomp[k][j] for k in range(len(ubar))) for j in range(Q.d)]
            Trows.append(decompose(rep))
        tried += 1
        # 找使 (5b) 成立的 e_i（在 U 坐标下）
        good = None
        for _t in range(60):
            cs = [[Fr(rng.randint(-2, 2)) for _ in E] for _ in range(3)]
            es = [[sum(cs[i][k] * E[k][j] for k in range(len(E))) for j in range(3)] for i in range(3)]
            eis = [decompose(e) for e in es]      # U 坐标
            prow = []
            for i in range(3):
                ei = [Fr(1) if i == j else Fr(0) for j in range(3)]
                prow.append((ei, [Trows[i][j] + eis[i][j] for j in range(3)]))
            prow.append(([Fr(0)] * 3, list(decompose(w))))
            if CV.pencil_minors_gcd_one(prow, 3, 3):
                good = es
                break
        if good is None:
            continue
        feasible += 1
        # 端到端：构造 V ⊆ C^n
        rowsV = []
        ok_tau = True
        for i in range(3):
            tau = solve_tau(Q, good[i])
            # 验证 pi(tau A) = good[i]
            if Q.pi(mm([tau], A)[0]) != good[i]:
                ok_tau = False
                break
            liftu = Q.lift(U[i])
            rowsV.append([liftu[k] + tau[k] for k in range(n)])
        if not ok_tau:
            continue
        h = solve_tau(Q, w)
        if Q.pi(mm([h], A)[0]) != w:
            continue
        rowsV.append(h)
        for r in L0:                      # 保证 V ⊇ row(L0)
            rowsV.append(list(r))
        V = rb(rowsV)
        a = cond5a(V, A, C)
        b = cond5b(V, A, C)
        if a and b:
            end2end += 1
    print(f"尝试 {tried} 个格子；判据说可行的 {feasible} 个；")
    print(f"其中**端到端**（构造出 V 并在 C^n 里验过 (5a)∧(5b)）: {end2end}")


if __name__ == '__main__':
    main()
