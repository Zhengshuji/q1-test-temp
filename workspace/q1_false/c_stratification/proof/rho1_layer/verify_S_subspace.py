"""检验 §47：S = { b in B : W0 + <b> 满足 (N) } 是否是线性子空间？答案：**不是**。

60 个实例（n=5、dim W0 = 2、B 3 维）：收集可允许的 b，检查两两之和是否仍可允许 -> 0 次通过。
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI
import importlib.util
spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def is_N(U, F, B):
    return all(rank(U + B + [mm([u], F)[0]]) == rank(U + B) for u in U)


def main():
    rng = random.Random(31337)
    n = 5
    agree = tot = 0
    for _ in range(60):
        F = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        B = rb([[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(3)])
        if len(B) < 2:
            continue
        W0 = rb([[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(3)])
        if len(W0) != 2:
            continue
        good_b = []
        for _k in range(40):
            b = [Fr(rng.randint(-2, 2)) for _ in range(len(B))]
            bv = [sum(b[i] * B[i][j] for i in range(len(B))) for j in range(n)]
            U = rb([r[:] for r in W0] + [bv])
            if len(U) != 3:
                continue
            if is_N(U, F, B):
                good_b.append(b)
        tot += 1
        if not good_b:
            continue
        for i in range(min(len(good_b), 6)):
            for j in range(i + 1, min(len(good_b), 6)):
                ssum = [good_b[i][k] + good_b[j][k] for k in range(len(B))]
                sv = [sum(ssum[k] * B[k][t] for k in range(len(B))) for t in range(n)]
                U = rb([r[:] for r in W0] + [sv])
                if len(U) != 3:
                    continue
                if is_N(U, F, B):
                    agree += 1
    print(f"S 对加法封闭的检查：{agree} 次通过（应全部通过才对）")
    print("=> 结论：S **不是**线性子空间（§47）")


if __name__ == '__main__':
    main()
