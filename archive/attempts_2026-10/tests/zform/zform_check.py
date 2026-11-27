"""zform_check.py — 交叉验证 Z-FORM 与 V-形式（Q1-FALSE × Q1-TRUE 交接）

Z-FORM（见 Q1_TRUE_HANDOFF.md）：
    q_min = n - p - d_max,
    d_max = max dim Z,  Z ⊆ ker C, Z ⊆ L0^⊥, A(Z∩K) ⊆ Z,
            dim((λI-A)K ∩ Z) = dim(K∩Z) ∀λ.

对每个已知解 L（证书），取 Z = ker[C;L]，逐条验证，并检查
    dim Z = n - p - q,   dim(Z∩K) = d - ρ   （与 V-形式的层参数对应）。

用法：
    python q1_false/tests/zform_check.py
"""
import sys
import os
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def dim(X):
    return len(AI.row_basis(X)) if X else 0


def intersect(X, Y):
    """行空间 X ∩ Y 的基，用 (X^⊥ + Y^⊥)^⊥。"""
    Xp = AI.nullspace(X) if X else []
    Yp = AI.nullspace(Y) if Y else []
    both = AI.row_basis(Xp + Yp)
    return AI.nullspace(both) if both else X


def check(fn, key, q):
    d0 = json.load(open(os.path.join(ROOT, "lit", fn), encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
    if key not in d0:
        return None
    L = toF(d0[key])
    n, p = len(A), len(C)
    CA = mul(C, A)
    Kmat = AI.nullspace(AI.vstack([C, CA]))
    K = Kmat                      # 列表：每个是 n 维向量
    Z = AI.nullspace(AI.vstack([C, L]))   # 列表：每个是 n 维向量
    d, rho_dim = len(K), len(Z)
    Nv = AI.nullspace(AI.vstack([C, CA]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)] if Nv else None
    rho = rank(mul(L, Nmat)) if Nmat else 0

    # Z ⊆ ker C, Z ⊆ L0^⊥
    ok_C = all(all(sum(C[i][j] * z[j] for j in range(n)) == 0 for i in range(len(C))) for z in Z) if Z else True
    ok_L0 = all(all(sum(a * b for a, b in zip(z, l0)) == 0 for z in Z) for l0 in L0)
    dimZ_ok = (len(Z) == n - p - len(L))
    ZK = intersect(Z, K)
    AZK = [[sum(A[i][j] * z[j] for j in range(n)) for i in range(n)] for z in ZK]
    semi = (rank(AZK + Z) == len(Z)) if ZK else True
    # 谱条件（修正版：带核项）
    lam_ok = True
    for lam in (0, 1, -1, 2, -3, 5, 3):
        X = [[Fr(lam) * K[j][t] - sum(A[t][s] * K[j][s] for s in range(n)) for t in range(n)]
             for j in range(len(K))]
        # ker((lam I - A)|_K)：解 X^T? 用矩阵形式：X 是向量列表，(λI-A)K 的基
        # ker 维数 = d - rank(X)
        k_lam = len(K) - rank(X)
        I = intersect(X, Z)
        if len(I) != len(ZK) - k_lam:
            lam_ok = False
            break
    print(f"{fn:42s} q={len(L)} rho={rho} d={d} dimZ={rho_dim} "
          f"| Z⊆kerC {ok_C} Z⊆L0⊥ {ok_L0} dimZ=n-p-q {dimZ_ok} "
          f"| A(Z∩K)⊆Z {semi} | 谱(抽样) {lam_ok} | dim(Z∩K)={len(ZK)} d-rho={d-rho}")


def main():
    for fn, key, q in [("counterexample_refute_dimV1.json", "L", 1),
                       ("certificate_middle_layer.json", "L_2row", 2),
                       ("certificate_rhostar_lt_dimV.json", None, 2),
                       ("counterexample_candidate.json", "L", 3),
                       ("counterexample_d4.json", "L", 3)]:
        if key is None:
            continue
        try:
            check(fn, key, q)
        except Exception as e:
            print(f"{fn}: ERR {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
