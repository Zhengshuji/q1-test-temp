"""(N) <=> 经典 (A,K)-条件不变性（K = J + J A）的验证。见 RESTRICTED_COMPLETION_MODEL §26.1。"""
import random, sys
from fractions import Fraction as Fr
sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI
import importlib.util
spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec); spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

def main():
    rng = random.Random(20261030)
    agree = tot = 0
    for _ in range(120):
        n = rng.choice([5, 6, 7]); p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        Q = Qm.Quotient(A, C)
        if Q.d < 2:
            continue
        k = rng.choice([1, 2, min(3, Q.d)])
        U = rb([[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(k + 1)])
        if len(U) != k:
            continue
        barU = rb([Q.classmod(u) for u in U])
        fU = [Q.classmod(Q.pi(mm([Q.lift(u)], A)[0])) for u in U]
        cond_N = all(rank(barU + [w]) == len(barU) for w in fU)
        Ut = rb([Q.lift(u) for u in U])
        K = rb([r[:] for r in Q.J] + mm(Q.J, A))
        cond_cl = rank(mm(Ut, A) + Ut + K) == rank(Ut + K)
        tot += 1
        if cond_N == cond_cl:
            agree += 1
    print(f"(N) 与经典 (A,K)-条件不变性一致：{agree}/{tot}")

if __name__ == '__main__':
    main()
