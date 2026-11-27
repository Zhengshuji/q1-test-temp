"""test_two_mechanisms.py — 检验"两个机制取大"（Q1-FALSE）

区域：d=1（rho 只能是 0 或 1）、L0 的行在 J=row[C;CA] 里（故 rho0=0）、L0 本身不是解。
此时 delta=1，rho*∈{0,1}，修正公式预测 q_min = max(r+1, rho*+1) = r+1（r>=2）。

做法：随机造这样的实例，搜 q=r+1 的解；再确认 q=r 不可能（L0 不是解即排除）。
若 q=r+1 总能找到 => "两机制取大"在这区域成立；若找不到但更大的 q 有解 => 第三种机制。
"""
import sys
import os
import json
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA
import c164_trusted_baseline as TB

mul, rank = AI.mul, AI.rank


def main():
    rng = random.Random(424242)
    stats = {}
    for t in range(300):
        n, p = 5, 2
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        CA = mul(C, A)
        if rank(AI.vstack([C, CA])) != n - 1:
            continue                      # 要 d=1
        Nv = AI.nullspace(AI.vstack([C, CA]))
        if len(Nv) != 1:
            continue
        Nmat = [[Nv[j][i] for j in range(1)] for i in range(n)]
        J = AI.row_basis(CA + C)
        r = rng.choice([2, 3])
        if len(J) < r:
            continue
        # L0 = J 的 r 个随机组合
        idx = rng.sample(range(len(J)), r)
        L0 = [J[i][:] for i in idx]
        if rank(L0) != r:
            continue
        if not M.cond5a(L0, A, C):
            pass                          # 我们希望 L0 不是解
        l0sol = M.cond5a(L0, A, C) and (M.cond5b(L0, A, C) == 0)
        if l0sol:
            continue
        D = M.reduced_data(A, C, L0)
        if not D["inV"]:
            continue
        q = r + 1
        L, rho = LA.find_solution(A, C, L0, q, random.Random(t), 4000, Nmat=Nmat)
        key = (r, "found" if L is not None else "none")
        stats[key] = stats.get(key, 0) + 1
        if L is not None:
            ok, det = TB.check_solution(L, A, C, L0)
            if not ok:
                print(f"  t={t} 找到的解未通过复核: {det}")
        elif stats[key] <= 2:
            # 没找到 q=r+1，试 q=r+2
            L2, rho2 = LA.find_solution(A, C, L0, r + 2, random.Random(t + 1), 4000, Nmat=Nmat)
            print(f"  t={t} r={r}: q={q} 无解；q={r+2} -> {'有解 rho='+str(rho2) if L2 is not None else '无解'}")
    print("\n统计（r, q=r+1 是否找到解）:")
    for k in sorted(stats):
        print(f"  r={k[0]}: {k[1]} -> {stats[k]}")


if __name__ == "__main__":
    main()
