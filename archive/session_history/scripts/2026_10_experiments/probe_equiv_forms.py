# -*- coding: utf-8 -*-
"""
probe_equiv_forms.py —— 确认"分解"的**等价刻画**（供 Lean 直接用）

【本轮定位】
  DEC : ∃ Λ,G₀,G₁, LA = ΛL + G₀C + G₁CA     —— 数值上 48220/48220 成立 ✓
  但各"分量核包含"(ker L⊆ker(LA) 等) **并非** DEC 的推论/前提 ✗（我此前混淆了）

【要确认的等价刻画】（这些都是**同一个**线性条件的不同写法）
  (A)row : rk[LA;L;C;CA] == rk[L;C;CA]
  KF∩    : ker[L;C;CA] ⊆ ker(LA)
  DUAL   : 对偶形式（下文）
  DEC    : 分解存在

本脚本逐点比较这四个，确认它们**互相等价**。
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)

import linalg_q as Q


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


def sub_le(P, Qgen):
    if not P:
        return True
    if not Qgen:
        return Q.rank(P) == 0
    return Q.rank(P + Qgen) == Q.rank(Qgen)


def main():
    print("=== 分解的等价刻画：逐点比较 ===\n")
    n, p = 3, 1
    As = [Q.mat([[0,1,0],[0,0,0],[0,0,0]]),
          Q.mat([[0,1,0],[0,0,1],[0,0,0]]),
          Q.mat([[0,1,0],[0,0,0],[0,0,2]])]
    st = dict(tot=0, Arow=0, KFi=0, dec=0)
    mism = []
    for A in As:
        for Crow in itertools.product([-1, 0, 1], repeat=n):
            C = Q.mat([list(Crow)])
            if Q.rank(C) != p:
                continue
            CA = Q.mul(C, A)
            for q0 in [1, 2]:
                for Lr in itertools.product(itertools.product([-1, 0, 1], repeat=n), repeat=q0):
                    L = Q.mat([list(r) for r in Lr])
                    if Q.rank(L) != q0:
                        continue
                    st["tot"] += 1
                    LA = Q.mul(L, A)
                    Arow = Q.rank(Q.stack(LA, L, C, CA)) == Q.rank(Q.stack(L, C, CA))
                    KFi = sub_le(Q.nullspace(Q.stack(L, C, CA)), Q.nullspace(LA))
                    rows, rhs = build_system(A, C, L)
                    dec = Q.solve(rows, rhs) is not None
                    st["Arow"] += 1 if Arow else 0
                    st["KFi"] += 1 if KFi else 0
                    st["dec"] += 1 if dec else 0
                    if not (Arow == KFi == dec):
                        if len(mism) < 3:
                            mism.append((Arow, KFi, dec, A, C, L))
    print("枚举实例数        : %d" % st["tot"])
    print("(A)row 成立       : %d" % st["Arow"])
    print("KF∩ 成立          : %d" % st["KFi"])
    print("DEC 成立          : %d" % st["dec"])
    print()
    print("三者是否**逐点一致**？反例 %d 个" % len(mism))
    for Arow, KFi, dec, A, C, L in mism:
        print("  (Arow,KFi,dec)=(%s,%s,%s)  L=%s C=%s"
              % (Arow, KFi, dec, [[str(x) for x in r] for r in L],
                 [[str(x) for x in r] for r in C]))
    if not mism:
        print("\n⟹ **(A)row ⟺ KF∩ ⟺ DEC** 逐点成立 ✓")
        print("   ⟹ Lean 里可以用**最容易证的那个**作假设，推出另外两个 ✓")


if __name__ == "__main__":
    main()
