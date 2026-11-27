"""端到端验证（四个格子 mu = 1,2,3）：从格子判据出发构造真正的 V，并在 C^n 里用堆叠判据验 (5a)∧(5b)。

U 的构造是**定向**的（先取 E ⊆ B 的 mu 维子空间，再补到 3 维），否则随机取 U 几乎总得到 mu=1。
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
spec2 = importlib.util.spec_from_file_location('E', 'proof/rho1_layer/verify_end2end_genuine.py')
E2E = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(E2E)
spec3 = importlib.util.spec_from_file_location('M', 'proof/rho1_layer/verify_cell_mu23_genuine.py')
M23 = importlib.util.module_from_spec(spec3)
spec3.loader.exec_module(M23)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def run(target_mu, n, p, trials, rng):
    tried = feas = e2e = 0
    for _ in range(trials):
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        Q = Qm.Quotient(A, C)
        if Q.d < 3 or Q.m < target_mu:
            continue
        U0 = rb([Q.pi(r) for r in L0])
        if len(U0) > 3:
            continue
        U = M23.build_U(Q, U0, target_mu, rng)
        if U is None:
            continue
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
        if len(E) != target_mu:
            continue
        w = E[0]
        if not any(w):
            continue
        W = Qm.complement(U, Q.d)
        Linv = AI.inv(U + W)
        dec = lambda x: mm([x], Linv)[0][:3]
        Trows = []
        for u in U:
            ubar = Q.Tbar(u)
            rep = [sum(ubar[k] * Q.Bcomp[k][j] for k in range(len(ubar))) for j in range(Q.d)]
            Trows.append(dec(rep))
        tried += 1
        good = None
        for _t in range(60):
            cs = [[Fr(rng.randint(-2, 2)) for _ in E] for _ in range(3)]
            es = [[sum(cs[i][k] * E[k][j] for k in range(len(E))) for j in range(3)] for i in range(3)]
            prow = []
            for i in range(3):
                ei = [Fr(1) if i == j else Fr(0) for j in range(3)]
                eis = dec(es[i])
                prow.append((ei, [Trows[i][j] + eis[j] for j in range(3)]))
            prow.append(([Fr(0)] * 3, list(dec(w))))
            if E2E.CV.pencil_minors_gcd_one(prow, 3, 3):
                good = es
                break
        if good is None:
            continue
        feas += 1
        rowsV = []
        ok = True
        for i in range(3):
            tau = E2E.solve_tau(Q, good[i])
            if Q.pi(mm([tau], A)[0]) != good[i]:
                ok = False
                break
            lu = Q.lift(U[i])
            rowsV.append([lu[k] + tau[k] for k in range(n)])
        if not ok:
            continue
        h = E2E.solve_tau(Q, w)
        if Q.pi(mm([h], A)[0]) != w:
            continue
        rowsV.append(h)
        for r in L0:
            rowsV.append(list(r))
        V = rb(rowsV)
        if E2E.cond5a(V, A, C) and E2E.cond5b(V, A, C):
            e2e += 1
    return tried, feas, e2e


def main():
    import sys as _s
    rng = random.Random(2026)
    which = _s.argv[1] if len(_s.argv) > 1 else '12'
    for mu in [int(c) for c in which]:
        if mu == 3:
            tot = run(3, 9, 3, 12, rng)      # n=9,p=3 -> (j,d,dimB)=(6,3,3)，mu=3（已加提前退出）
        else:
            tot = run(mu, 7, 2, 60, rng)   # n=7,p=2：dim J<=4 => d>=3，dim B 常为 2
        print(f"mu={mu}: 尝试 {tot[0]} 个格子，判据可行 {tot[1]}，端到端成功 {tot[2]}")


if __name__ == '__main__':
    main()
