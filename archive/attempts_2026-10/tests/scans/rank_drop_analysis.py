"""rank_drop_analysis.py — 中间层证书的"降 rho"机制分析（Q1-FALSE）

问题：下降算法保持 rho，遇到中间层就停。那中间层证书里的
      q=3, rho=2  ->  q=2, rho=1
这一步到底做了什么？

本脚本对 certificate_middle_layer.json 做结构对比：
  - V2（证书解，q=2, rho=1）与 V3（搜到的 q=3, rho=2）
  - 包含关系、交、和、W=V∩J
  - 判据 K0^⊥ ⊆ F 在两个解上的取值
  - 最小 ci 子空间（Kleiman–Krener，模 K 的 A^T 闭包）
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

mul, tr, rank = AI.mul, AI.tr, AI.rank


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def sub_dim(X, Y):
    """dim(X ∩ Y)"""
    return len(AI.row_basis([list(x) for x in X] + [list(y) for y in Y])) + 0, \
           len(AI.row_basis([list(x) for x in X])) + len(AI.row_basis([list(y) for y in Y])) - \
           len(AI.row_basis([list(x) for x in X] + [list(y) for y in Y]))


def dim(X):
    return len(AI.row_basis(X)) if X else 0


def main():
    path = os.path.join(ROOT, "lit", "certificate_middle_layer.json")
    d0 = json.load(open(path, encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
    Kb = [[Nmat[i][j] for i in range(n)] for j in range(len(Nv))]   # K 基
    J = AI.row_basis(mul(C, A) + C)
    print(f"n={n} d={len(Nv)} dimJ={len(J)}")

    V2 = AI.row_basis(toF(d0["L_2row"]))
    V3, rho3 = LA.find_solution(A, C, L0, 3, random.Random(5), 8000, rho_target=2, Nmat=Nmat)
    V3 = AI.row_basis(V3)
    print(f"V2: dim={len(V2)} rho={rank(mul(V2, Nmat))}")
    print(f"V3: dim={len(V3)} rho={rank(mul(V3, Nmat))}")

    # 包含关系
    def subset(X, Y):
        return dim(AI.row_basis([list(x) for x in X] + [list(y) for y in Y])) == dim(Y)
    print(f"V2 ⊆ V3 ? {subset(V2, V3)}   V3 ⊆ V2 ? {subset(V3, V2)}")
    print(f"dim(V2+V3) = {dim(V2 + V3)}   dim(V2∩V3) = {dim(V2)+dim(V3)-dim(V2+V3)}")

    W2 = AI.row_basis([x for x in V2 if rank([list(x)] + J) == len(J)])  # 不可靠，改用下法
    # W = V ∩ J：用线性方程组
    def intersect(X, Y):
        # X, Y 为行空间；求交的基
        # 简单做法：Z ⊆ X 且 Z ⊆ Y ⟺ Z 的每行在 X 和 Y 中
        # 用零空间法：X 的坐标 c 使 Σ c_i X_i ∈ Y
        # 这里用笨办法：解 M c = Y 的组合
        import sympy
        q = len(X)
        # 找 c ≠ 0 使 Σ c_i X_i ∈ span(Y)：等价于 [X 的行] 与 Y 的行线性组合
        # 构造矩阵，求同时属于两者的向量空间：用 (X^⊥ + Y^⊥)^⊥
        Xp = AI.nullspace(X)
        Yp = AI.nullspace(Y)
        both = AI.row_basis(Xp + Yp)
        return AI.nullspace(both) if both else X
    W2 = intersect(V2, J)
    W3 = intersect(V3, J)
    print(f"W2 = V2∩J: dim={len(W2)}   W3 = V3∩J: dim={len(W3)}")

    # 判据
    def crit(V):
        Kb_ = Kb
        AK = [[sum(A[i][j] * k[j] for j in range(n)) for i in range(n)] for k in Kb_]
        F = AI.row_basis([[dot(v, y) for v in V] for y in (Kb_ + AK)])
        import sympy
        q = len(V)
        G = sympy.Matrix([[dot(V[i], V[j]) for j in range(q)] for i in range(q)])
        rows = []
        for k0 in L0:
            b = sympy.Matrix([dot(V[i], k0) for i in range(q)])
            rows.append([Fr(x) for x in G.LUsolve(b)])
        K0p = AI.nullspace(rows)
        inter = AI.row_basis([x for x in K0p if dim(AI.row_basis([list(x)] + F)) == len(F)])
        return len(F), len(K0p), len(inter)

    for nm, V in (("V2", V2), ("V3", V3)):
        f, k, i = crit(V)
        print(f"{nm}: dimF={f} dimK0^⊥={k} 交={i}  条件(K0^⊥⊄F)={i < k}")

    # 最小 ci 子空间（模 K 的 A^T 闭包）
    K0 = AI.row_basis(L0)
    W = [row[:] for row in K0]
    for _ in range(n + 2):
        Wt = AI.row_basis(W + [[sum(A[i][j] * v[j] for j in range(n)) for i in range(n)] for v in W])
        # 模 K：quotient，直接看它是否 ci：WA ⊆ W + J
        if rank(AI.vstack([mul(W, A), W, J])) == rank(AI.vstack([W, J])):
            break
        W = Wt
    print(f"最小 ci（迭代近似）: dim={len(W)}  (K0 dim={len(K0)})")
    print(f"  W ⊆ V2? {subset(W, V2)}   W ⊆ V3? {subset(W, V3)}")
    print(f"  W 是解? {M.cond5b(W, A, C) if len(W) else 'skip'}")


if __name__ == "__main__":
    main()
