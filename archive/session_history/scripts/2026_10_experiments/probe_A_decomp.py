# -*- coding: utf-8 -*-
"""
probe_A_decomp.py —— 钉死 T5′ 的前提：**(A) 是否总能给出 LA = ΛL + G₀C + G₁CA 的分解？**

【为什么关键】
  T5′（FINAL §4.3、本项目 Lean `F_eq_Lam_comp_H`）把 (A) 的**分解存在性**当作前提，
  由此得 F = Λ·H。若 (A) 单独**不足以保证**分解存在，则：
     · T5′ 的陈述需要加假设（或改用别的 Λ 来源）；
     · 「(A) ⟹ (S) 失败」这条捷径不成立；
     · 但项目 87/87 的 (A)∧(S) 与 0/200 的 (A)∧(S) 仍可能都对。

【本脚本】
  对任意 L，直接（独立地）解系统
      LA[i][j] = Σ_k Λ[i][k] L[k][j] + Σ_m G0[i][m] C[m][j] + Σ_m G1[i][m] CA[m][j]
  并对照：
      (A) 判据  rk[LA;L;C;CA] == rk[L;C;CA]
      F vs ΛH
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rank_exact, solve_exact, matmul = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]

_ns3 = {"__file__": os.path.join(_HERE, "batch_c6p_k.py")}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    exec(compile(fh.read().split("def main()")[0], "helpers", "exec"), _ns3)
mat = _ns3["mat"]


def stack(*Ms):
    out = []
    for M in Ms:
        if not M:
            continue
        if out:
            assert len(out[0]) == len(M[0]), "stack 列数不一致"
        out += [r[:] for r in M]
    return out


def rk(M):
    return rank_exact(M)


def condA(A, C, L):
    CA = matmul(C, A)
    return rk(stack(matmul(L, A), L, C, CA)) == rk(stack(L, C, CA))


def decomp_solutions(A, C, L):
    """独立求解 LA = ΛL + G0 C + G1 CA。返回 [(Λ,G0,G1), ...]（抽样若干）"""
    q0, n, p = len(L), len(A), len(C)
    CA = matmul(C, A)
    LA = matmul(L, A)
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
    res = solve_exact(rows, rhs)
    if res is None:
        return None
    y, ns = res
    sols = []
    for s in [y] + ns:
        Lam = [[s[kk * q0 + i] for kk in range(q0)] for i in range(q0)]
        G0 = [[s[q0 * q0 + i * p + m] for m in range(p)] for i in range(q0)]
        G1 = [[s[q0 * q0 + q0 * p + i * p + m] for m in range(p)] for i in range(q0)]
        sols.append((Lam, G0, G1))
    return sols


def main():
    print("=== (A) 是否总给出 LA = ΛL + G₀C + G₁CA 的分解？ ===\n")
    cases = [
        ("I-4x4", mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]), mat([[0,0,1,0]])),
        ("I-5x5", mat([[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]),
                  mat([[0,0,0,1,0]])),
        ("II-nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                           [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                      mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
    ]
    rng = random.Random(11)
    for tag, A, C in cases:
        n = len(A)
        CA = matmul(C, A)
        B = ker_basis(stack(C, CA))
        d = len(B[0]) if B and B[0] else 0
        print("[%s] n=%d p=%d d_CA=%d" % (tag, n, len(C), d))
        nA = nDecomp = nFH = nFail = 0
        for trial in range(600):
            q0 = rng.choice([1, 2, 3])
            L = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(q0)]
            if rk(L) != q0:
                continue
            if not condA(A, C, L):
                continue
            nA += 1
            sols = decomp_solutions(A, C, L)
            if sols is None:
                nFail += 1
                if nFail <= 3:
                    print("    ⚠️ q0=%d (A)✓ 但**无分解**！（LA 不能用 L,C,CA 表示）" % q0)
                continue
            nDecomp += 1
            H = matmul(L, B)
            Fm = matmul(matmul(L, A), B)
            ok = any(matmul(Lam, H) == Fm for Lam, _, _ in sols)
            if ok:
                nFH += 1
            elif nDecomp - nFH <= 3:
                print("    q0=%d 有分解但**所有解都使 ΛH ≠ F**（rkH=%d rkF=%d）"
                      % (q0, rk(H), rk(Fm)))
            if nA >= 80:
                break
        print("    (A)-点 %d ：有分解 %d ；无分解 %d ；分解⟹ΛH=F %d"
              % (nA, nDecomp, nFail, nFH))
        print()

    print("【结论判读】")
    print("  · 若「无分解」计数 > 0 ⟹ **(A) 不足以保证 T5′ 的分解前提** ⚠️")
    print("  · 若「有分解但 ΛH≠F」> 0 ⟹ 分解存在也不给出 F=ΛH（需检查 N_CA 的角色）⚠️")


if __name__ == "__main__":
    main()
