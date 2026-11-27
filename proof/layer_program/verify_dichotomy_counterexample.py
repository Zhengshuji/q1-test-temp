# ⚠️ 本脚本里的"⟂"判据**不是不变量** ✗（§77–§79）—— 它的筛选/判断用坐标点积，
# 而正确的不变形式是**秩/包含**条件：w ∈ (λI−T)(U)（见 RESTRICTED_COMPLETION_MODEL §80）。
# 本脚本仅作为**过程记录**保留；正确的反例脚本是 verify_counterexample_final.py（§81）。
"""§77：把定理 76.1 的抽象反例**实现**为真实的 (A, C0, L0)。

目标（层级别二分猜想的反例）：
  * 存在固定方向 e1 = π(ℓ0) ≠ 0，且 f(e1) = 0（即 ℓ0 A ∈ 𝒥）⟹ e1 是 f-特征向量（λ=0）；
  * dim B = d − 2 ⟹ 由引理 60.1，**每个** 3 维 U ⊇ ⟨e1⟩ 都 μ≥1 ⟹ P2 = YES；
  * 由命题 75.1（e1 落在 B 的零化子里）⟹ **每个**格子都被覆盖 ⟹ 层不可行。
  ⟹ "P2 = YES ⟹ 存在好格子" **不成立** ✓

构造（row-vector 约定：x·A 的第 k 个坐标 = Σ_i x_i A[i][k]）：
  n = 8；C 取 [e7; e5]；A 的第 6 行 = e7（于是 e6·A = e7 ∈ 𝒥）、第 7 行 = e7。
  ℓ0 = e6，L0 = [e6] ⟹ π(ℓ0) = e1 ≠ 0，π(ℓ0 A) = π(e7) = 0 ⟹ f(e1) = 0 ✓
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

n = 8


def build_A(rng):
    """n=8：第 6 行 = e8（于是 e6·A = e8 ∈ J）；其余随机。
    取 C = [e8; e7] ⟹ J = <e8,e7,e8A,e7A>（4 维）、d = 4、dim B = 2。"""
    A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
    A[5] = [Fr(0)] * 7 + [Fr(1)]     # e6·A = e8
    return A


def cell_covered(Q, A, U):
    d = Q.d
    B = Q.B
    mu = len(B) + len(U) - rank([r[:] for r in B] + [r[:] for r in U])
    if mu == 0:
        return True, 0
    _rows = [[B[i][k] for i in range(len(B))] + [-U[j][k] for j in range(len(U))] for k in range(d)]
    E = []
    for sol in AI.nullspace(_rows):
        v = [sum(sol[i] * B[i][k] for i in range(len(B))) for k in range(d)]
        if any(v):
            E.append(v)
    E = rb(E)
    rho = len(U)
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
        return True, mu
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    good = (len(g) == 1 and g[0] != 0)
    return (not good), mu


def main():
    rng = random.Random(20251030)
    e = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
    for trial in range(300):
        A = build_A(rng)
        C = [list(e[7]), list(e[6])]        # C = [e8; e7]
        Q = Qm.Quotient(A, C)
        from collections import Counter
        globals().setdefault('_diag', Counter())
        _diag[(Q.j, Q.d, len(Q.B))] += 1
        if Q.d != 4 or len(Q.B) != 2:
            continue
        l0 = list(e[5])                      # ℓ0 = e6
        u0 = Q.pi(l0)
        if not any(u0):
            continue
        u0A = Q.pi(mm([l0], A)[0])
        if any(u0A):
            continue                         # 要求 f(e1) = 0
        W0 = rb([u0, u0A])
        # 命题 75.1 的关键条件：e1 落在 B 的零化子里（B ⊥ e1，坐标内积）
        if not all(sum(b[k] * u0[k] for k in range(Q.d)) == 0 for b in Q.B):
            continue
        print(f"trial {trial}: n=8, j={Q.j}, d={Q.d}, dim B={len(Q.B)}, dim W0={len(W0)} ✓")
        print(f"  e1 = π(e6) = {[str(x) for x in u0]}")
        print(f"  f(e1) = π(e6·A) = {[str(x) for x in u0A]} ✓(=0)")
        # 族：所有 3 维 U ⊇ W0；随机取一些
        stats = {'covered': 0, 'good': 0, 'degenerate': 0}
        mus = set()
        for _ in range(30):
            z1 = [Fr(rng.randint(-2, 2)) for _ in range(Q.d)]
            z2 = [Fr(rng.randint(-2, 2)) for _ in range(Q.d)]
            U = rb([r[:] for r in W0] + [z1, z2])
            if len(U) != 3:
                stats['degenerate'] += 1
                continue
            cov, mu = cell_covered(Q, A, U)
            mus.add(mu)
            stats['covered' if cov else 'good'] += 1
        print(f"  族里 30 个随机 U：{stats}；μ 取值 {sorted(mus)}")
        # 详细诊断：取第一个非退化的 U，打印 T、a、以及 e1 在其坐标下的表现
        for _ in range(20):
            z1 = [Fr(rng.randint(-2, 2)) for _ in range(Q.d)]
            z2 = [Fr(rng.randint(-2, 2)) for _ in range(Q.d)]
            U = rb([r[:] for r in W0] + [z1, z2])
            if len(U) != 3:
                continue
            d = Q.d; B = Q.B
            _rows = [[B[i][k] for i in range(len(B))] + [-U[j][k] for j in range(len(U))] for k in range(d)]
            E = []
            for sol in AI.nullspace(_rows):
                v = [sum(sol[i] * B[i][k] for i in range(len(B))) for k in range(d)]
                if any(v):
                    E.append(v)
            E = rb(E)
            if not E:
                break
            rho = 3
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
            ER = AI.rref([[U[j][k] for j in range(rho)] + [E[0][k]] for k in range(d)])[0]
            a = [Fr(0)] * rho
            for row in ER:
                piv = next((j for j in range(rho) if row[j] != 0), None)
                if piv is None:
                    continue
                a[piv] = row[rho] / row[piv]
            # e1 在 U 坐标下
            ER2 = AI.rref([[U[j][k] for j in range(rho)] + [u0[k]] for k in range(d)])[0]
            e1c = [Fr(0)] * rho
            for row in ER2:
                piv = next((j for j in range(rho) if row[j] != 0), None)
                if piv is None:
                    continue
                e1c[piv] = row[rho] / row[piv]
            Te1 = [sum(T[i][j] * e1c[j] for j in range(rho)) for i in range(rho)]
            ae1 = sum(a[i] * e1c[i] for i in range(rho))
            print(f"  诊断：e1 坐标 = {[str(x) for x in e1c]}；T·e1 = {[str(x) for x in Te1]}；a·e1 = {ae1}")
            break
        if stats['covered'] > 0 and stats['good'] == 0:
            print("  => **每个**格子都被覆盖 ✗ ⟹ P2=YES 但层不可行 ⟹ **二分猜想反例** ✓✓")
            print(f"  A = {[[int(x) for x in r] for r in A]}")
            return
        elif stats['good'] > 0:
            print("  => 有好格子（这个实例不是反例）✗，继续找")
    print("300 个 trial 里没有找到'全族都坏'的实例")
    print("  诊断 (j, d, dimB) 分布：", dict(list(globals().get('_diag', {}).items())[:8]))


if __name__ == '__main__':
    main()
