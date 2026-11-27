"""A' 第 3 步：在候选实例上，用**唯一**的 3 维 T-不变子空间 U = im(T - 1)，
构造所有合法 V 并判定 (5b)。

d = 4 时，3 维 T-不变子空间 U 对应商 X/U（1 维）上的标量作用，故标量必须是有理特征值；
本实例的有理特征值只有 1，所以 U = im(T - 1) 是**唯一**的 3 维不变子空间（dim 3 ✓）。
于是型层（在 Q 上）完全由 U 与 h ∈ J、以及 lift 自由度决定 —— 可以**穷尽**。
"""
import io
import json
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

sys.path.insert(0, 'proof/rho1_layer')
import importlib.util
spec = importlib.util.spec_from_file_location('q', 'proof/rho1_layer/quotient_T.py')
Qm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Qm)

mm = Qm.mm


def main():
    d0 = json.load(io.open('proof/rho1_layer/candidate_c31_counterexample.json', encoding='utf-8'))[0]
    F = lambda M: [[Fr(x) for x in r] for r in M]
    A, C, L0 = F(d0['A']), F(d0['C']), F(d0['L0'])
    n = len(A)
    Q = Qm.quotient_data(A, C)
    J, comp, j, d, Tm = Q['J'], Q['comp'], Q['j'], Q['d'], Q['Tm']
    L0b = AI.row_basis(L0)
    CA = mm(C, A)

    def lift(u):
        v = [Fr(0)] * n
        for k in range(d):
            if u[k]:
                v = [v[i] + u[k] * comp[k][i] for i in range(n)]
        return v

    # U = im(T - lam)，lam = 1
    lam = Fr(1)
    M = [[Tm[i][k] - (lam if i == k else Fr(0)) for k in range(d)] for i in range(d)]
    # im(M) 的基（列空间 -> 转置成行）
    cols = [[M[i][k] for i in range(d)] for k in range(d)]
    U = AI.row_basis(AI.tr(cols))
    print("dim im(T-1) =", len(U))
    if len(U) != 3:
        print("不是 3 维，退出")
        return
    Ub = [lift(u) for u in U]

    # 让 V = span{L0row, lift(u_a), lift(u_b), h} 的 pi-维数 = 3：
    # 需要 {pi(L0row), pi(u_a), pi(u_b)} 张成 U ✓（u_a,u_b 取 U 的两基向量；L0row 的像在 U 里）
    rng_j = [Fr(0)]
    found_V = 0
    feas = 0
    results = []
    for h in AI.row_basis(J) + [[Fr(0)] * n]:
        for ia in range(len(Ub)):
            for ib in range(len(Ub)):
                if ia == ib:
                    continue
                rows = [L0b[0], Ub[ia], Ub[ib], list(h)]
                L = AI.row_basis(rows)
                if len(L) != 4:
                    continue
                rho = AI.rank(AI.vstack([L, CA, C])) - j
                c = len(L) + j - AI.rank(AI.vstack([L, J]))
                if (rho, c) != (3, 1):
                    continue
                if not AI.cond_5a_orig(A, C, L):
                    continue
                found_V += 1
                b5 = AI.cond_5b_orig(A, C, L)
                results.append(([[str(x) for x in r] for r in L], b5))
                if b5:
                    feas += 1
    print(f"构造出的合法 V: {found_V} 个；其中 (5b) 成立: {feas}")
    for L, b5 in results:
        print("   (5b) =", b5, " L =", L)


if __name__ == '__main__':
    main()
