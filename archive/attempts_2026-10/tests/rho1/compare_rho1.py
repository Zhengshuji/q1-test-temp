"""compare_rho1.py — rho=1 判定器 vs 搜索（对拍）

对每个实例：
  - 判定器：solve_case 是否给出 q=2, rho=1 的解
  - 搜索：c166.find_solution(q=2, rho_target=1)
两者应一致（q=2 是最小可能行数；q=2 的解只能是 rho=0 或 1，
rho=0 意味着 L0 本身是解，此时 q_min=1）。

用法：
    python q1_false/tests/compare_rho1.py --random 12 --seed 51
"""
import sys
import os
import random
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))
sys.path.insert(0, HERE)

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA
import rho1_solver as RS
import c164_trusted_baseline as TB

mul, rank = AI.mul, AI.rank


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--random", type=int, default=12)
    ap.add_argument("--seed", type=int, default=51)
    ap.add_argument("--trials", type=int, default=4000)
    ap.add_argument("--r", default="1,2")
    ap.add_argument("--targeted", action="store_true", help="L0 取 row[C;CA] 的组合（rho0=0）")
    args = ap.parse_args()

    if args.targeted:
        rng = random.Random(args.seed)
        insts = []
        for t in range(args.random):
            n = rng.choice([4, 5, 6])
            p = rng.choice([1, 2, 3])
            A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
            C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
            CA = mul(C, A)
            J = AI.row_basis(CA + C)
            if not J:
                continue
            # L0 = J 的随机组合（保证 L0N = 0）
            coef = [Fr(rng.randint(-2, 2)) for _ in J]
            L0 = [[sum(coef[i] * J[i][j] for i in range(len(J))) for j in range(n)]]
            if rank(L0) != 1:
                continue
            insts.append((f"targ_s{args.seed}_{t}", A, C, L0))
    else:
        insts = LA.random_instances(args.random, args.seed,
                                    r_choices=tuple(int(x) for x in args.r.split(",")))
    agree = 0
    total = 0
    for name, A, C, L0 in insts:
        n = len(A)
        Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
        if not Nv:
            continue
        Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
        D = M.reduced_data(A, C, L0)
        if not D["inV"]:
            continue
        if len(L0) != 1:
            continue                      # 判定器目前只处理 r=1
        total += 1
        sol = RS.solve_case(A, C, L0)
        if sol is not None:
            # 判定器给出的是构造解：用可信基线独立复核，通过即为真值
            ok, _det = TB.check_solution(sol[0], A, C, L0)
            pred = True
            truth = ok
            if not ok:
                print(f"{name}: 判定器构造解未通过复核！{_det}")
        else:
            pred = False
            found, _ = LA.find_solution(A, C, L0, 2, random.Random(7), args.trials,
                                        rho_target=1, Nmat=Nmat)
            truth = found is not None
        agree += (pred == truth)
        mark = "✓" if pred == truth else "✗"
        print(f"{name:22s} 判定={pred}  搜索={truth} {mark}   q_min(audit)=", end="")
        a = LA.audit_instance(name, A, C, L0, random.Random(1), 60, verbose=False)
        print(a.get("qmin"))
    print(f"\n一致 {agree}/{total}")


if __name__ == "__main__":
    main()
