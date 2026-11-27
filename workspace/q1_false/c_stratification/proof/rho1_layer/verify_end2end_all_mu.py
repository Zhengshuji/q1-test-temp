"""端到端验证（全通道，10 条逐项）—— 用**正确的提升求解**，覆盖 mu = 1, 2, 3。

提升的正确做法：
  要让 pi(ℓ_i A) ∈ U，需要 beta(τ_i) = r - pi(u_i A)，其中 r ∈ U 且 r - pi(u_i A) ∈ B。
  这样的 r 存在 <=> (N)。求解：在 U + B 里把 pi(u_i A) 写成 u-part + b-part，取 r = u-part，
  再解 τ_i 使 beta(τ_i) = -b-part。

每个成功实例逐项检查 10 条（dim U=3、W0⊆U、w≠0、(N)、mu≥1、row(L0)⊆V、dim V=4、类型 (3,1)、(5a)、(5b)）。
"""
import itertools
import random
import sys
from collections import Counter
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util as iu
spec = iu.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

spec2 = iu.spec_from_file_location('E', 'proof/rho1_layer/verify_end2end_genuine.py')
E2E = iu.module_from_spec(spec2)
spec2.loader.exec_module(E2E)


def lift_row(Q, u, U, B, lift):
    """构造一行 ℓ 使 pi(ℓ) = u 且 pi(ℓ A) ∈ U。失败返回 None。"""
    img = Q.pi(mm([lift], Q.A)[0])
    # 把 img 写成 u-part + b-part（模 U + B 应相容）
    Lb = rb([r[:] for r in U] + [r[:] for r in B])
    if rank([r[:] for r in Lb] + [img]) != len(Lb):
        return None
    # 解 img = sum a_i U_i + sum c_j B_j
    M = [[Lb[i][t] for i in range(len(Lb))] + [img[t]] for t in range(Q.d)]
    R, _ = AI.rref(M)
    sol = [Fr(0)] * len(Lb)
    for row in R:
        for t in range(len(Lb)):
            if row[t] != 0:
                sol[t] = row[len(Lb)] / row[t]
                break
    # b-part
    bvec = [Fr(0)] * Q.d
    for j in range(len(U), len(Lb)):
        for t in range(Q.d):
            pass
    # 直接用 B 的基重算 b-part
    # img - (U 分量) = B 分量；U 分量由 rb(U+B) 的前 len(U) 个基给出（若 U 与 B 独立）
    Uc = [Fr(0)] * Q.d
    for i in range(len(U)):
        for t in range(Q.d):
            Uc[t] += sol[i] * U[i][t]
    bpart = [img[t] - Uc[t] for t in range(Q.d)]
    if rank([r[:] for r in B] + [bpart]) != len(B):
        return None
    tau = E2E.solve_tau(Q, [(-x) % Q.p if False else -x for x in bpart])
    row = [lift[t] + tau[t] for t in range(Q.n)]
    return row, tau


def attempt(A, C, L0):
    Q = Qm.Quotient(A, C)
    if Q.d < 3 or Q.m < 1:
        return None
    u0 = Q.pi(L0[0])
    if not any(u0):
        return None
    W0 = rb([u0] + [Q.pi(mm([r], A)[0]) for r in L0])
    for _k in range(10):
        U = rb([u0] + [[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(3)])
        if len(U) != 3:
            continue
        U = rb([u0] + [r for r in U if rank([u0] + [r]) == 2][:2])
        if len(U) != 3 or rank([u0] + U) != 3:
            continue
        if not all(rank(U + [x]) == 3 for x in W0):
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
        if not E:
            continue
        w = next((e for e in E if any(e)), None)
        if w is None:
            continue
        # 三行：第 0 行固定为 ℓ0；另两行用 lift_row
        rows = [list(L0[0])]
        ok = True
        for i in (1, 2):
            res = lift_row(Q, U[i], U, B if False else Q.B, Q.lift(U[i]))
            if res is None:
                ok = False
                break
            rows.append(res[0])
        if not ok:
            continue
        h = E2E.solve_tau(Q, w)
        rows.append(list(h))
        V = rb(rows)
        CA = mm(C, A)
        J = rb(C + CA)
        j = len(J)
        rho = rank(V + CA + C) - j
        cc = len(V) + j - rank(V + J)
        conds = {
            'dimU': len(U) == 3,
            'W0': all(rank(U + [x]) == 3 for x in W0),
            'w': any(w),
            'N': all(rank(U + Q.B + [mm([Q.lift(u)], A)[0]]) == rank(U + Q.B) for u in U),
            'mu': len(E) >= 1,
            'L0': all(rank(V + [list(r)]) == len(V) for r in L0),
            'dimV': len(V) == 4,
            'type': (rho, cc) == (3, 1),
            '5a': E2E.cond5a(V, A, C),
            '5b': E2E.cond5b(V, A, C),
        }
        return conds, len(E)
    return None


rng = random.Random(20260729)
stats = Counter()
tried = 0
for trial in range(60):
    n = rng.choice([6, 7])
    p = rng.choice([1, 2])
    A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
    C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
    L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
    out = attempt(A, C, L0)
    if out is None:
        continue
    conds, mu = out
    tried += 1
    if all(conds.values()):
        stats[mu] += 1
print(f"尝试 {tried} 个候选；全部 10 条通过的 mu 分布：{dict(stats)}")
