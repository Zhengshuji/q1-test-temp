"""端到端（修正版 lift_row）：在商空间 X/U 里解 B-分量，覆盖 mu = 1,2,3。

上次失败的原因（§51.2）：在 [U;B] 的基下展开，但 U∩B≠0 时那不是直和，解不唯一。

这次：令 π' : X → X/U 为商映射。对每行的像 im，
  需要 b ∈ B 使 π'(im − b) = 0，即 π'(b) = π'(im)。
  这是关于 b 的系数（B 的基）的线性方程组 —— 唯一解或不相容，直接 rref 判定。
"""
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


def rows_in_U(Q, U, u_list, lifts):
    """给 u_i 的 lifts，求 tau_i 使 pi((lift_i + tau_i) A) ∈ U。返回 (rows, ok)。"""
    # 商映射 π' : X → X/U ：取 U 的补空间 W，坐标就是 W 分量
    n = Q.n
    W = []
    span = [r[:] for r in U]
    for i in range(n):
        e = [Fr(1) if j == i else Fr(0) for j in range(n)]
        if rank(span + [e]) > len(span):
            W.append(e)
            span = rb(span + [e])
        if len(span) == n:
            break
    Linv = AI.inv(U + W)          # X 的坐标 -> (U 坐标, W 坐标)

    def proj_W(x):
        c = mm([x], Linv)[0]
        return c[len(U):]          # W 分量 = π'(x) 的坐标

    rows = []
    for i, u in enumerate(u_list):
        im = Q.pi(mm([lifts[i]], Q.A)[0])
        t = proj_W(im)
        if not any(t):
            tau = [Fr(0)] * n
        else:
            # 解 π'(b) = t，b = sum c_j B_j
            M = [proj_W(Q.B[j]) + [t[k]] for k in range(len(W)) for j in []]
            M = [[proj_W(Q.B[j])[k] for j in range(len(Q.B))] + [t[k]] for k in range(len(W))]
            R, _ = AI.rref(M)
            sol = [Fr(0)] * len(Q.B)
            bad = False
            for row in R:
                piv = next((j for j in range(len(Q.B)) if row[j] != 0), None)
                if piv is None:
                    if row[len(Q.B)] != 0:
                        bad = True
                    continue
                sol[piv] = row[len(Q.B)] / row[piv]
            if bad:
                return None, False
            bvec = [sum(sol[j] * Q.B[j][k] for j in range(len(Q.B))) for k in range(n)]
            tau = E2E.solve_tau(Q, [(-x) for x in bvec])
        rows.append([lifts[i][k] + tau[k] for k in range(n)])
    return rows, True


def attempt(A, C, L0, rng):
    Q = Qm.Quotient(A, C)
    if Q.d < 3 or Q.m < 1:
        return None
    u0 = Q.pi(L0[0])
    zero_u0 = not any(u0)      # L0 的行在 J 里时 pi(ℓ0)=0 —— 这是合法情形
    W0 = rb([u0] + [Q.pi(mm([r], A)[0]) for r in L0])
    if len(W0) > 1:
        return None      # 只要 dim W0 <= 1 的实例，否则 mu 会被 W0 逼到 >= 2
    for _k in range(12):
        # 强制 mu=1：U 里放**一个** B 的方向（b）+ 一个随机方向
        bdir = [sum(Fr(rng.randint(-2, 2)) * Q.B[j][k] for j in range(len(Q.B))) for k in range(Q.d)]
        seed = [] if zero_u0 else [u0]
        U = rb(seed + [bdir] + [[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(2)])
        if len(U) != 3:
            continue
        U = rb(seed + [bdir] + [r for r in U if rank(seed + [bdir] + [r]) == 3][:1])
        if len(U) != 3:
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
        rows, ok = rows_in_U(Q, U, [U[1], U[2]], [Q.lift(U[1]), Q.lift(U[2])])
        if not ok:
            continue
        h = E2E.solve_tau(Q, w)
        rowsV = [list(L0[0])] + rows + [list(h)]
        V = rb(rowsV)
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


def main():
    rng = random.Random(20260730)
    stats = Counter()
    tried = 0
    for trial in range(80):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [list(C[0])]     # L0 取 C 的第一行 => pi(ℓ0)=0 => dim W0 = 1
        out = attempt(A, C, L0, rng)
        if out is None:
            continue
        conds, mu = out
        tried += 1
        if all(conds.values()):
            stats[mu] += 1
    print(f"尝试 {tried} 个候选；全部 10 条通过的 mu 分布：{dict(stats)}")


if __name__ == '__main__':
    main()
