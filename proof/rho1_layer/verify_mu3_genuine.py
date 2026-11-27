"""在真实实例上验证定理 2（mu=3：型层不被覆盖）。

构造：取 n=9、p=3，使 dim J = 6 => d = 3（于是 U = X 是唯一的 3 维子空间），
并且 dim B = 3（生成 => mu = 3）。此时行可以完全自由（E = U = X），
按定理 2 的构造取基 v_k 使 w^T v_k != 0、C = V Λ V^{-1}（Λ 互异），验证 (5b) 成立。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI
import importlib.util

spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = importlib.util.spec_from_file_location('C', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(CV)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def main():
    rng = random.Random(90909)
    tot = ok = 0
    for _ in range(200):
        n, p = 9, 3
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        Q = Qm.Quotient(A, C)
        if Q.d != 3 or len(Q.B) != 3:
            continue
        U = [[Fr(1) if i == j else Fr(0) for j in range(3)] for i in range(3)]   # U = X
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
        if len(E) != 3:
            continue
        w = E[0]
        if not any(w):
            continue
        # 行自由：直接取 v_k 为基，使 w^T v_k != 0
        # 找基 v_k 使 w^T v_k != 0 且 rank = 3（用小搜索，避免 w 恰好是坐标轴时退化）
        Vb = None
        for _try in range(200):
            cand = [list(w)]
            for _k in range(2):
                cand.append([w[j] + Fr(rng.randint(-3, 3)) for j in range(3)])
            if rank(cand) == 3 and all(sum(w[k] * v[k] for k in range(3)) != 0 for v in cand):
                Vb = cand
                break
        if Vb is None:
            continue
        # 行数据来自 C = V Λ V^{-1}（V 的**列**是 v_k）：C 的行是 c_i，
        # 铅笔（U 坐标 = X 坐标）的行 = lam*e_i - c_i，第 4 行 = -w
        lams = [Fr(1), Fr(2), Fr(3)]
        Vcols = [[Vb[k][i] for k in range(3)] for i in range(3)]     # V 的第 i 行 = (v_1[i], v_2[i], v_3[i])
        Vinv = AI.inv(Vcols)
        Lam = [[lams[i] if i == j else Fr(0) for j in range(3)] for i in range(3)]
        Cmat = mm(mm(Vcols, Lam), Vinv)
        prow = []
        for i in range(3):
            ei = [Fr(1) if i == j else Fr(0) for j in range(3)]
            prow.append((ei, [Cmat[i][j] for j in range(3)]))
        prow.append(([Fr(0)] * 3, list(w)))
        tot += 1
        if CV.pencil_minors_gcd_one(prow, 3, 3):
            ok += 1
    print(f"mu=3（真实实例，dim B = 3, d = 3）：{tot} 个；按定理 2 构造后 (5b) 成立: {ok}")


if __name__ == '__main__':
    main()
