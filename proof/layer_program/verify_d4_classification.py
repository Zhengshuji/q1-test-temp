"""核验 d=4 分类的三条引理（RCP §83 / proof/layer_31_theorems/d4_classification.md）。

引理 2.1（mu 二分）、引理 3.1（(N) 二分）、引理 4.1（提升存在 + 类型 (3,1)）。
固定种子 987654、n=6、p=1、随机 A 与随机 phi，全部有理算术。
"""
import itertools, random, sys
from fractions import Fraction as Fr
sys.path.insert(0,'tools/exact_linalg')
import audit_independent as AI
import importlib.util as iu
spec = iu.spec_from_file_location('Q','proof/rho1_layer/quotient_selfcheck.py')
Qm = iu.module_from_spec(spec); spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

rng = random.Random(987654)
mu_ok = mu_tot = 0
N_ok = N_tot = 0
lift_ok = lift_tot = 0
phi_perp_count = 0
for trial in range(40):
    n = 6
    A = [[Fr(rng.randint(-2,2)) for _ in range(n)] for _ in range(n)]
    C = [[Fr(rng.randint(-2,2)) for _ in range(n)] for _ in range(1)]
    Q = Qm.Quotient(A, C)
    if Q.d != 4: continue
    d = Q.d; B = Q.B
    phi = [Fr(rng.randint(-2,2)) for _ in range(d)]
    if not any(phi): continue
    ns = AI.nullspace([phi])
    if not ns: continue
    U = rb(ns)
    if len(U) != 3: continue
    mu = len(B) + 3 - rank([r[:] for r in B] + [r[:] for r in U])
    phi_perp_B = all(sum(phi[k]*b[k] for k in range(d)) == 0 for b in B)
    if phi_perp_B: phi_perp_count += 1
    want = len(B) if phi_perp_B else len(B) - 1
    mu_tot += 1
    if mu == want: mu_ok += 1
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    N_holds = all(rank([r[:] for r in U] + [r[:] for r in B] + [v]) ==
                  rank([r[:] for r in U] + [r[:] for r in B]) for v in fU)
    N_tot += 1
    if not phi_perp_B:
        if N_holds: N_ok += 1
    else:
        cond = all(rank([r[:] for r in U] + [v]) == len(U) for v in fU)
        if N_holds == cond: N_ok += 1
    W0 = rb([Q.pi(r) for r in C] + [Q.pi(mm([r], A)[0]) for r in C])
    if all(rank(U + [w]) == len(U) for w in W0):
        K = []
        span = [r[:] for r in Q.J]
        for i in range(n):
            e = [Fr(1) if t==i else Fr(0) for t in range(n)]
            if rank(span+[e]) > len(span): K.append(e); span = rb(span+[e])
            if len(span)==n: break
        j0 = [C[0][k] - sum((Q.pi(C[0]))[i]*Q.lift([Fr(1) if t==i else Fr(0) for t in range(d)])[k] for i in range(d)) for k in range(n)]
        V = rb([Q.lift(u) for u in U] + [j0])
        lift_tot += 1
        if (len(V) == 4 and rank([Q.pi(v) for v in V]) == 3
                and len(V) + len(Q.J) - rank(V + Q.J) == 1
                and all(rank(V + [list(r)]) == 4 for r in C)):
            lift_ok += 1
print(f"引理 2.1（μ 二分）：{mu_ok}/{mu_tot}（其中 φ⊥B 的 {phi_perp_count} 例）")
print(f"引理 3.1（(N) 二分）：{N_ok}/{N_tot}")
print(f"引理 4.1（提升存在 + 类型 (3,1)）：{lift_ok}/{lift_tot}")
