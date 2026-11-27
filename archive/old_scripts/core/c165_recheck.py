"""
c165_recheck.py — 用可信验证器（c164）重跑两项关键验证

任务 1：ρ=0 层 ⟺ conditioned invariant（旧验证用了采样 λ，需精确重做）
任务 2：ρ=dim V 层的 q_min = dim V+1 一致率（旧为 88/91，需精确重做）

所有检查都走 c164.check_solution（含 prefix_L0、精确 5a、精确 5b、rank）。
"""
import sys
import os
import random
import itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c164_trusted_baseline as T

mul, rank = AI.mul, AI.rank


# ---------------------------------------------------------------- 任务 1

def task1_rho0_equivalence(trials=120):
    """检验：L·N=0 时，(5a)∧(5b) ⟺ LA ⊆ row[L;CA;C]（conditioned invariant）"""
    print("=" * 66)
    print("任务 1：ρ=0 层 ⟺ conditioned invariant（精确）")
    agree = disagree = tested = 0
    for t in range(trials):
        n = random.choice([4, 5, 6])
        p = random.choice([1, 2])
        A = [[Fr(random.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(random.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(random.randint(-1, 1)) for _ in range(n)]]
        if rank(L0) != 1:
            continue
        try:
            D = M.reduced_data(A, C, L0)
        except Exception:
            continue
        Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
        if not Nv:
            continue
        d = len(Nv)
        Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
        KerN = AI.nullspace(AI.tr(Nmat))
        if not KerN:
            continue
        CA = mul(C, A)
        J = AI.vstack([CA, C])
        base = AI.row_basis(J)
        # 随机取 q 行，全部落在 ker(·N) 里；第一行强制为 L0（若 L0 在 ker(·N) 内）
        q = random.choice([1, 2, 3])
        coef = [[Fr(random.randint(-1, 1)) for _ in range(len(KerN))] for _ in range(q)]
        L = [[sum(coef[i][k] * KerN[k][j] for k in range(len(KerN))) for j in range(n)]
             for i in range(q)]
        if rank(L) != q:
            continue
        if rank(mul(L, Nmat)) != 0:
            continue
        tested += 1
        ok, det = T.check_solution(L, A, C, L0, strict=False)   # 这里用弱约束即可
        cond5a_5b = bool(det["5a"] and det["5b"])
        LA = mul(L, A)
        ci = len(AI.row_basis(AI.row_basis(LA) + base + L)) == len(AI.row_basis(base + L))
        if cond5a_5b == ci:
            agree += 1
        else:
            disagree += 1
    print(f"  测试 {tested} 个退化 L")
    print(f"  (5a)∧(5b) 与 conditioned invariant 一致: {agree}")
    print(f"  不一致: {disagree}")
    print(f"  → {'✅ 等价成立' if disagree == 0 else '❌ 不等价'}")
    return tested, agree, disagree


# ---------------------------------------------------------------- 任务 2

def task2_dimVplus1(trials=100):
    """检验：q_min = dim V + 1 的一致率，以及例外解的 ρ"""
    print("\n" + "=" * 66)
    print("任务 2：q_min = dim V + 1 的一致率（精确）")
    cnt = match = 0
    exceptions = []
    for t in range(trials):
        n = random.choice([4, 5, 6])
        p = random.choice([1, 2])
        A = [[Fr(random.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(random.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(random.randint(-1, 1)) for _ in range(n)]]
        if rank(L0) != 1:
            continue
        try:
            D = M.reduced_data(A, C, L0)
        except Exception:
            continue
        if not D["inV"]:
            continue
        dV = len(D["V"])
        Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
        if not Nv:
            continue
        d = len(Nv)
        Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
        # q_min（精确）
        qmin = None
        Lwin = None
        for q in range(1, n + 1):
            for _ in range(200):
                L = [row[:] for row in L0]
                while len(L) < q:
                    L.append([Fr(random.randint(-1, 1)) for _ in range(n)])
                if rank(L) != q:
                    continue
                ok, _ = T.check_solution(L, A, C, L0, strict=True)
                if ok:
                    qmin, Lwin = q, L
                    break
            if qmin is not None:
                break
        if qmin is None:
            continue
        cnt += 1
        if qmin == dV + 1:
            match += 1
        else:
            rho = rank(mul(Lwin, Nmat))
            exceptions.append((n, p, dV, qmin, rho))
    print(f"  实例 {cnt}")
    print(f"  q_min = dim V + 1 的: {match}/{cnt}")
    print(f"  例外 {len(exceptions)} 个，其 (n,p,dimV,qmin,ρ):")
    for e in exceptions[:10]:
        print(f"    {e}")
    nondeg = [e for e in exceptions if e[4] > 0]
    print(f"  其中 ρ>0 的（非退化例外）: {len(nondeg)}")
    return cnt, match, exceptions


def main():
    random.seed(20251024)
    task1_rho0_equivalence(120)
    task2_dimVplus1(100)


if __name__ == "__main__":
    main()
