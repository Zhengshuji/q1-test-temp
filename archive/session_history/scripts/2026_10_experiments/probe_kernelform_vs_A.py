# -*- coding: utf-8 -*-
"""
probe_kernelform_vs_A.py —— (A) 的行空间形式 vs 核形式 vs 分解存在性

【三个条件】
  (A)row : rk[LA;L;C;CA] == rk[L;C;CA]                     ← 项目的 (A)，FINAL T1
  KF∩    : (ker L ∩ ker C ∩ ker CA) ⊆ ker(LA)              ← 项目 Lean 里用的"核形式"
  KFsep  : ker L ⊆ ker(LA) ∧ ker C ⊆ ker(LA) ∧ ker CA ⊆ ker(LA)   ← 分解真正需要的
  DEC    : ∃(Λ,G₀,G₁), LA = ΛL + G₀C + G₁CA

【要回答】
  ① (A)row ⟹ DEC ？（应成立，见 probe_A_vs_decomp.py 的 48220/48220）
  ② (A)row ⟹ KFsep ？（若成立，则 Lean 里可用 KFsep 作假设）
  ③ KF∩ ⟹ KFsep ？（若成立，则项目现有的"核形式"假设够用）
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)

import linalg_q as Q


def kernel_of(M, n):
    """ker(M) 的基（行向量列表，长度 n）"""
    return Q.nullspace(M)


def sub_le(Pgen, Qgen, n):
    """span(Pgen) ⊆ span(Qgen) ？"""
    if not Pgen:
        return True
    P = [list(r) for r in Pgen]
    M = P + [list(r) for r in Qgen]
    if not Qgen:
        return Q.rank(P) == 0
    return Q.rank(M) == Q.rank(Qgen)


def build_system(A, C, L):
    q0, n, p = len(L), len(A), len(C)
    CA = Q.mul(C, A)
    LA = Q.mul(L, A)
    nunk = q0 * q0 + 2 * q0 * p
    rows, rhs = [], []
    for i in range(q0):
        for j in range(n):
            row = [F(0)] * nunk
            for kk in range(q0):
                row[kk * q0 + i] = L[kk][j]
            for m in range(p):
                row[q0 * q0 + i * p + m] = C[m][j]
            for m in range(p):
                row[q0 * q0 + q0 * p + i * p + m] = CA[m][j]
            rows.append(row)
            rhs.append([LA[i][j]])
    return rows, rhs


def main():
    print("=== (A)row vs KF∩ vs KFsep vs DEC ===\n")
    n, p = 3, 1
    stats = dict(tot=0, Arow=0, KFi=0, KFsep=0, dec=0,
                 Arow_not_KFsep=0, KFi_not_KFsep=0, Arow_not_dec=0, ex=[])
    A_list = [Q.mat([[0, 1, 0], [0, 0, 0], [0, 0, 0]]),
              Q.mat([[0, 1, 0], [0, 0, 1], [0, 0, 0]]),
              Q.mat([[0, 1, 0], [0, 0, 0], [0, 0, 2]])]
    for A in A_list:
        for Crow in itertools.product([-1, 0, 1], repeat=n):
            C = Q.mat([list(Crow)])
            if Q.rank(C) != p:
                continue
            CA = Q.mul(C, A)
            LA_full = C  # 占位
            for q0 in [1, 2]:
                for Lrows in itertools.product(itertools.product([-1, 0, 1], repeat=n), repeat=q0):
                    L = Q.mat([list(r) for r in Lrows])
                    if Q.rank(L) != q0:
                        continue
                    stats["tot"] += 1
                    LA = Q.mul(L, A)
                    Arow = Q.rank(Q.stack(LA, L, C, CA)) == Q.rank(Q.stack(L, C, CA))
                    # 各核
                    kerL = Q.nullspace(L)
                    kerC = Q.nullspace(C)
                    kerCA = Q.nullspace(Q.mul(C, A))
                    kerLA = Q.nullspace(LA)
                    # KF∩：kerL ∩ kerC ∩ kerCA ⊆ kerLA
                    M = Q.stack(L, C, Q.mul(C, A))
                    kerALL = Q.nullspace(M)
                    KFi = sub_le(kerALL, kerLA, n)
                    # KFsep
                    KFsep = sub_le(kerL, kerLA, n) and sub_le(kerC, kerLA, n) and sub_le(kerCA, kerLA, n)
                    # DEC
                    rows, rhs = build_system(A, C, L)
                    dec = Q.solve(rows, rhs) is not None
                    if Arow:
                        stats["Arow"] += 1
                        if not KFsep:
                            stats["Arow_not_KFsep"] += 1
                        if not dec:
                            stats["Arow_not_dec"] += 1
                        if len(stats["ex"]) < 3 and not KFsep:
                            stats["ex"].append((A, C, L))
                    if KFi:
                        stats["KFi"] += 1
                        if not KFsep:
                            stats["KFi_not_KFsep"] += 1
                    if KFsep:
                        stats["KFsep"] += 1
                    if dec:
                        stats["dec"] += 1
    print("枚举实例数                : %d" % stats["tot"])
    print("(A)row 成立               : %d" % stats["Arow"])
    print("KF∩ 成立                  : %d" % stats["KFi"])
    print("KFsep 成立                : %d" % stats["KFsep"])
    print("DEC 成立                  : %d" % stats["dec"])
    print()
    print("(A)row 成立但 KFsep 不成立 : %d   ← 若 >0，则核形式不足以做分解" % stats["Arow_not_KFsep"])
    print("KF∩ 成立但 KFsep 不成立    : %d   ← 若 >0，则项目现有核形式假设不够" % stats["KFi_not_KFsep"])
    print("(A)row 成立但 DEC 不成立   : %d   ← 若 >0，则 (A) 不蕴含分解" % stats["Arow_not_dec"])
    if stats["ex"]:
        print("\n(A)row✓ 但 KFsep✗ 的例子：")
        for A, C, L in stats["ex"]:
            print("  A=", [[str(x) for x in r] for r in A])
            print("  C=", [[str(x) for x in r] for r in C])
            print("  L=", [[str(x) for x in r] for r in L])


if __name__ == "__main__":
    main()
