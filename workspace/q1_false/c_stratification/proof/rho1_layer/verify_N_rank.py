"""结构性观察：对 (3,1) 的一个格子，
   (N)  <=>  rank(f|_U) <= 3 - mu,
因为 q_B(U) = (U+B)/B ≅ U/(U∩B) 的维数是 3 - mu。
"""
import random, sys
from fractions import Fraction as Fr
sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI
import importlib.util
spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec); spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def main():
    rng = random.Random(555)
    agree = tot = 0
    from collections import Counter
    dims = Counter()
    for _ in range(300):
        d = rng.choice([5, 6]); mB = rng.choice([1, 2, 3])
        if mB >= d:
            continue
        A = [[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(d)]
        while True:
            B = rb([[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(mB)])
            if len(B) == mB:
                break
        while True:
            U = rb([[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(3)])
            if len(U) == 3:
                break
        E = [b for b in B if rank(U + [b]) == 3]
        mu = len(E)
        if mu == 0:
            continue
        fU = [mm([u], A)[0] for u in U]
        condN = all(rank(U + B + [v]) == rank(U + B) for v in fU)
        crit = (rank(fU) <= 3 - mu)
        tot += 1
        dims[(mu, 3 - mu)] += 1
        if condN == crit:
            agree += 1
    print(f"(N) <=> rank(f|_U) <= 3-mu 一致：{agree}/{tot}")
    print("  (mu, 3-mu) 分布：", dict(dims))


if __name__ == '__main__':
    main()
