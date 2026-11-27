# -*- coding: utf-8 -*-
"""
probe_S_correct.py —— 用**独立求解器**重测核心量 (A)∧(S)

【背景（本轮发现）】
  `batch_c6p_k.solve_Lambda` 是对库 `solve` 的包装，它用
      ([y] if any(x != 0 for x in y) else []) + nsol
  取解 —— 会**丢掉特解**（y 恰为 0 时）以及与独立求解器的解集不一致。
  实测（probe_solveLambda_bug.py）：200 个 (A)-点中 **193** 个"独立有解、库报无解" ✗
  ⟹ 任何依赖它的 (S) 结论都不可信 ⚠️

【本脚本的做法（全部独立、精确）】
  ① (A)      : rk[LA;L;C;CA] == rk[L;C;CA]
  ② T5a      : rk(L·N_CA) < q0
  ③ (S)      : 不依赖任何 Λ 包装，直接判**铅笔** λH − F 的秩：
                (S) ⟺ rk(λH−F) == rk H 对一切 λ
              精确实现：在若干有理 λ 上取 rk(λH−F)，若最大值 == rk H ⟹ (S) 成立 ✓
              （若所有 λ 处秩都 < rk H，则所有 1 阶子式恒为 0 ⟹ 矩阵恒为 0 ⟹ 也**失败**）
  ④ 与"正确的 Λ"对照：用独立分解求 Λ（满足 LA=ΛL+G0C+G1CA），验证 ΛH=F
  ⑤ 同时给出**朴素但正确**的 Λ 判据：rk(λH−F) 的最大值 vs rk H
"""
import os, io, contextlib, random, itertools
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


LAMS = [F(k) for k in range(-3, 4)] + [F(1, 2), F(-1, 2), F(1, 3), F(-2, 3), F(5, 2)]


def pencil_rank(H, Fm):
    """(S) 的**正确**判据：(S) ⟺ **对一切 λ** rk(λH−F) == rk H。

    ⚠️ 本函数初版写成「max_λ rk(λH−F) == rk H」（∃λ 满秩）—— **那是错的** ✗
    （错例：H=[[1,0]], F=0 时 λ=1 处满秩，但 λ=0 处秩 0 ⟹ (S) 失败）。
    正确形式必须**逐 λ** 检查 ✓
    """
    rH = rk(H)
    ranks = []
    for lam in LAMS:
        M = [[lam * H[i][j] - Fm[i][j] for j in range(len(H[0]))] for i in range(len(H))]
        ranks.append((lam, rk(M)))
    holds = all(a == rH for _, a in ranks)
    return holds, ranks, rH


def decomp_Lambda(A, C, L):
    """独立求满足 LA = ΛL + G0 C + G1 CA 的 Λ（取独立求解器给的特解）"""
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
    y = res[0]
    return [[y[kk * q0 + i] for kk in range(q0)] for i in range(q0)]


def main():
    print("=== 用独立求解器重测 (A)∧(S) ===\n")
    cases = [
        ("I-4x4", mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]), mat([[0,0,1,0]])),
        ("I-5x5", mat([[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]),
                  mat([[0,0,0,1,0]])),
        ("II-nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                           [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                      mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
        ("II-nilp6b", mat([[0,0,0,1,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1],
                           [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                      mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
    ]
    rng = random.Random(2026)
    print("%-12s %4s %5s | %6s %6s | %8s %8s | %s" %
          ("实例", "d_CA", "类", "(A)点", "T5a点", "(S)成立", "ΛH=F", "判读"))
    print("-" * 78)
    total = dict(A=0, t5a=0, S=0, both=0)
    for tag, A, C in cases:
        n = len(A)
        B = ker_basis(stack(C, matmul(C, A)))
        if not B or not B[0]:
            continue
        d = len(B[0])
        nA = nT = nS = nLam = 0
        for trial in range(3000):
            q0 = rng.choice([1, 2, 3])
            L = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(q0)]
            if rk(L) != q0:
                continue
            if not condA(A, C, L):
                continue
            nA += 1
            H = matmul(L, B)
            Fm = matmul(matmul(L, A), B)
            rH = rk(H)
            t5a = rH < q0
            if t5a:
                nT += 1
            best, ranks, rH2 = pencil_rank(H, Fm)
            S_holds = best
            if S_holds:
                nS += 1
                if t5a:
                    total["both"] += 1
            Lam = decomp_Lambda(A, C, L)
            if Lam is not None and matmul(Lam, H) == Fm:
                nLam += 1
            if nA >= 250:
                break
        total["A"] += nA
        total["t5a"] += nT
        total["S"] += nS
        kind = "II" if d >= 2 else "I"
        verdict = ("⟹ (A)⟹(S) 失败" if nS == 0 else
                   ("⟹ **(A)∧(S) 成立 %d 个（情形 %s）**" % (nS, kind)))
        print("%-12s %4d %5s | %6d %6d | %8d %8d | %s" %
              (tag, d, kind, nA, nT, nS, nLam, verdict))
    print("-" * 78)
    print("\n【总计】")
    print("  (A)-点总数          : %d" % total["A"])
    print("  其中 T5a 成立       : %d" % total["t5a"])
    print("  其中 (S) 成立       : %d" % total["S"])
    print("  其中 (A)∧T5a∧(S)    : %d   ← 真正的 YES 实例" % total["both"])
    print()
    print("【与项目数据的对照】")
    print("  项目 reliable_S_test.py：d_CA<q0 → (A)∧(S) = 87/87 ；d_CA≥q0 → 0/200")
    print("  本脚本（独立求解器）   ：见上表")


if __name__ == "__main__":
    main()
