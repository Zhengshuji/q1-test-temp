"""§81：按**修正后的**充分条件（命题 80.2）实现反例。

关键（§80）：
  若 rank(f) <= 2（即 dim π(X·A) <= 2）且 w ∈ im(f)，则**每个**格子都被覆盖
  （因为在 λ=0 处 w ∈ im(0·I − T) = im T）。
  而 w = β(h) ∈ B = π(𝒥 A) ⊆ π(X A) = im(f) **自动成立** ✓
  ⟹ 只需要 rank(A) <= 2 就够了 ✓ ✓。
  再让 μ≥1 自动（dim B ≥ d−2）⟹ P2 = YES 而层不可行 ⟹ **二分猜想反例** ✓
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util as iu
spec = iu.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = iu.spec_from_file_location('C2', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = iu.module_from_spec(spec2)
spec2.loader.exec_module(CV)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def covered(T, Erows, rho):
    """铅笔判据（正确的秩/gcd 形式）：True = 被覆盖。"""
    rows = [[[-T[i][k], Fr(1) if i == k else Fr(0)] for k in range(rho)] for i in range(rho)]
    for er in Erows:
        rows.append([[er[k]] for k in range(rho)])
    polys = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(rho), rho):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = CV.V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return True
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    good = (len(g) == 1 and g[0] != 0)
    return not good


def cell_data(Q, A, U):
    d = Q.d
    B = Q.B
    rho = len(U)
    mu = len(B) + rho - rank([r[:] for r in B] + [r[:] for r in U])
    if mu == 0:
        return None
    _rows = [[B[i][k] for i in range(len(B))] + [-U[j][k] for j in range(len(U))] for k in range(d)]
    E = []
    for sol in AI.nullspace(_rows):
        v = [sum(sol[i] * B[i][k] for i in range(len(B))) for k in range(d)]
        if any(v):
            E.append(v)
    E = rb(E)
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    nunk = rho * rho + rho * len(B)
    eqs = []
    for i in range(rho):
        for k in range(d):
            row = [Fr(0)] * nunk + [fU[i][k]]
            for j in range(rho):
                row[j * rho + i] = U[j][k]
            for t in range(len(B)):
                row[rho * rho + i * len(B) + t] = B[t][k]
            eqs.append(row)
    R = AI.rref(eqs)[0]
    s_ = [Fr(0)] * nunk
    for row in R:
        piv = next((j for j in range(nunk) if row[j] != 0), None)
        if piv is None:
            continue
        s_[piv] = row[nunk] / row[piv]
    T = [[s_[j * rho + i] for j in range(rho)] for i in range(rho)]
    Erows = []
    for er in E:
        ER = AI.rref([[U[j][k] for j in range(rho)] + [er[k]] for k in range(d)])[0]
        a = [Fr(0)] * rho
        for row in ER:
            piv = next((j for j in range(rho) if row[j] != 0), None)
            if piv is None:
                continue
            a[piv] = row[rho] / row[piv]
        Erows.append(a)
    return T, Erows, rho, mu


def main():
    rng = random.Random(20251030)
    n = 6
    for trial in range(200):
        # 秩 2 的 A（两个秩 2 因子相乘）
        L = [[Fr(rng.randint(-2, 2)) for _ in range(2)] for _ in range(n)]     # n x 2
        Rm = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(2)]    # 2 x n
        A = mm(L, Rm)
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(2)]
        Q = Qm.Quotient(A, C)
        # d=3 时 U = X 是唯一的 3 维子空间 ⟹ 族是单点，但二分猜想不要求正维 ✓
        if Q.d != 3 or len(Q.B) < 1:
            continue
        print(f"trial {trial}: n=6, rank(A)={rank(A)}, j={Q.j}, d={Q.d}, dim B={len(Q.B)}")
        print(f"  dim π(X·A) = {rank([Q.pi(mm([e], A)[0]) for e in [[Fr(1) if t==i else Fr(0) for t in range(n)] for i in range(n)]])} (应 ≤ 2)")
        W0 = rb([[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(1)])   # d=3 时 W0 取 1 维即可
        stats = {'covered': 0, 'good': 0, 'degenerate': 0}
        mus = set()
        for _ in range(30):
            z = [Fr(rng.randint(-2, 2)) for _ in range(Q.d)]
            z2 = [Fr(rng.randint(-2, 2)) for _ in range(Q.d)]
            U = rb([r[:] for r in W0] + [z, z2])
            if len(U) != 3:
                stats['degenerate'] += 1
                continue
            out = cell_data(Q, A, U)
            if out is None:
                stats['degenerate'] += 1
                continue
            T, Erows, rho, mu = out
            mus.add(mu)
            if covered(T, Erows, rho):
                stats['covered'] += 1
            else:
                stats['good'] += 1
        print(f"  30 个 U：{stats}；μ 取值 {sorted(mus)}")
        if stats['covered'] > 0 and stats['good'] == 0:
            print("  => **整族都被覆盖** ✗ ⟹ P2=YES（μ≥1 自动）但层不可行 ⟹ **二分猜想反例** ✓✓")
            print(f"  A = {[[int(x) for x in r] for r in A]}")
            print(f"  C = {[[int(x) for x in r] for r in C]}")
            return
    print("200 个 trial 里没有找到（可能 rank(A)<=2 与 d=4、dim B=2 不常同时成立）")


if __name__ == '__main__':
    main()
