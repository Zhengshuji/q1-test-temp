"""rho1_characterization.py — rho=1 层的结构刻画（Q1-FALSE）

推导
----
取 q=2、rank(LN)=1 的解 L。令 M=LN=u v^T（u∈R^2, v∈R^d 非零），A' 为压缩，N'=L R0。
(5b) ⟺ ker(λM - MA' - N') = ker M = v^⊥。

取 z ∦ u，把 R^2 分解为 span{u} ⊕ span{z}，写 N'ξ = a(ξ)u + b(ξ)z。

结论（本脚本验证）：
  (C1)  b(ξ) = c·(v^T ξ)，c ≠ 0；            （否则某个 λ 处向量为零）
  (C2)  在 v^⊥ 上：a(ξ) = -(w^T ξ)，w = A'^T v。 （否则 ker 变大）

等价的矩阵形式（w = A'^T v）：
  (C2') N' + u w^T 的每一行都是 v^T 的倍数；
  (C1') 对任意 z ∦ u，π_z ∘ N' ∝ v^T。

用法：
    python q1_false/tests/rho1_characterization.py --inst certificate_middle_layer.json
"""
import sys
import os
import json
import random
import argparse

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


def verify(A, C, L0, L):
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    D = M.reduced_data(A, C, L0)
    Ap = D["Ap"]
    R0 = D["R0"]

    Mx = mul(L, Nmat)          # 2×d
    Nx = mul(L, R0)            # 2×d（注意 R0 是 n×d）
    if rank(Mx) != 1:
        print(f"  rank(M)={rank(Mx)} ≠ 1，跳过")
        return

    # u：M 的非零列；v：由 M = u v^T 解出（选一个 u_i ≠ 0）
    u = None
    for j in range(d):
        col = [Mx[i][j] for i in range(2)]
        if any(x != 0 for x in col):
            u = col
            v = [Mx[0][j] / u[0] if u[0] != 0 else Mx[1][j] / u[1] for j in range(d)]
            break
    # 验证 M = u v^T
    okM = all(Mx[i][j] == u[i] * v[j] for i in range(2) for j in range(d))
    print(f"  M = u v^T ? {okM}   u={[str(x) for x in u]} v={[str(x) for x in v]}")

    # z ∦ u：取 e_1 或 e_2 中不平行者
    z = [Fr(1), Fr(0)] if u[0] * 0 - u[1] * 1 != 0 else [Fr(0), Fr(1)]
    # 解 N'ξ = a u + b z：b = π_z(N'ξ)
    # 基：解 [u z] [a;b]^T = N'ξ  —— 用坐标：b = det(N'ξ, u)/det(z,u)
    det_zu = z[0] * u[1] - z[1] * u[0]
    b = []
    for j in range(d):
        col = [Nx[i][j] for i in range(2)]
        num = col[0] * u[1] - col[1] * u[0]   # det(col, u)
        b.append(num / det_zu)                # b = det(N'ξ,u)/det(z,u)
    # C1: b ∝ v
    okC1 = all(b[j] * v[0] == b[0] * v[j] for j in range(d)) and any(x != 0 for x in b)
    c = b[0] / v[0] if v[0] != 0 else None
    print(f"  C1: b ∝ v ? {okC1}   c={str(c) if c is not None else '?'}")

    # C2: w = A'^T v = v^T A'（注意 A' 是 d×d，v 是行向量）
    w = [sum(v[i] * Ap[i][j] for i in range(d)) for j in range(d)]
    # 检查 N' + u w^T 的行是否为 v 的倍数
    rows = []
    for i in range(2):
        row = [Nx[i][j] + u[i] * w[j] for j in range(d)]
        rows.append(row)
    okC2 = all(rows[i][j] * v[0] == rows[i][0] * v[j] for i in range(2) for j in range(d))
    print(f"  C2: (N' + u w^T) 行 ∝ v ? {okC2}   w={[str(x) for x in w]}")
    return okM, okC1, okC2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inst", default="certificate_middle_layer.json")
    ap.add_argument("--trials", type=int, default=8000)
    args = ap.parse_args()

    path = args.inst if os.path.isabs(args.inst) else os.path.join(ROOT, "lit", args.inst)
    d0 = json.load(open(path, encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]

    # 用证书自带的解（若有），否则搜索
    L = None
    for key in ("L_2row", "L"):
        if key in d0 and len(d0[key]) == 2:
            cand = toF(d0[key])
            if rank(mul(cand, Nmat)) == 1:
                L = cand
                print(f"用文件里的 {key}")
                break
    if L is None:
        L, _ = LA.find_solution(A, C, L0, 2, random.Random(9), args.trials, rho_target=1, Nmat=Nmat)
        if L is None:
            print("没找到 q=2, rho=1 的解")
            return
        print("搜索得到的解")

    print([str(x) for x in L])
    verify(A, C, L0, L)


if __name__ == "__main__":
    main()
