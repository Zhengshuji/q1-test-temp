"""测量：在 Q 上，满足 (N) 的 3 维子空间有多稀有（见 RESTRICTED_COMPLETION_MODEL §32.10）。

结论：X=Q^5, B=<e5>, 随机有理 f => (N) 几乎从不成立（0/7141），因为 B ⊆ U 时 (N) <=> f(U) ⊆ U，
而有理的 f-不变 3 维子空间非常稀有。=> 基于"随机有理 f"的统计有偏，覆盖问题应在 C 上讨论。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util
spec = importlib.util.spec_from_file_location('C', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CV)
mm, rank, rb = CV.Qm.mm, CV.Qm.rank, CV.Qm.rb


def main():
    rng = random.Random(31415)
    B = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
    tot = adm = fam = 0
    for _ in range(60):
        F = [[Fr(rng.randint(-2, 2)) for _ in range(5)] for _ in range(5)]
        anyn = False
        for _k in range(120):
            U = rb([r[:] for r in B] + [[Fr(rng.randint(-2, 2)) for _ in range(5)] for _ in range(2)])
            if len(U) != 3:
                continue
            tot += 1
            fU = [mm([u], F)[0] for u in U]
            if not all(rank(U + B + [v]) == rank(U + B) for v in fU):
                continue
            adm += 1
            anyn = True
        if anyn:
            fam += 1
    print(f"抽样 {tot} 个 3 维 U；(N) 成立 {adm} 个；有非空族的 f：{fam}/60")


if __name__ == '__main__':
    main()
