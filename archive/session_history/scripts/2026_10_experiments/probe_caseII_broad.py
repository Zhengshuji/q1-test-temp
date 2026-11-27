# -*- coding: utf-8 -*-
"""
probe_caseII_broad.py —— 大范围、多结构地独立复核：**情形 II 下 (A) ⟹ (S) 失败 是否恒成立**

【为什么要做】
  probe_caseII_mechanism.py 在一个族上得到 (A)-点 18/18 都满足
      rk[H ; F] == rk(H)      （H = L·N_CA, F = L·A·N_CA）
  —— 这等价于"存在 y ≠ 0 使 y·L·N_CA·A ∈ row(N_CA)"，也就是 T12 机制的"秩满版"。
  若这在**一般结构**下恒成立，则 (S) 必失败（FINAL §4.5 的 0/200 就是它的表现）。
  若**能造出不成立的点**，则可能出现 (A) ∧ (S) ⟹ 情形 II 可为 YES ⟹ c6′ 假。

【覆盖面（刻意选"可能不成立"的结构）】
  1. 幂零 A（指标 2 / 3 / 4，n=6,7）
  2. A^2 ≠ 0 但 CA^2 = 0
  3. A 为一般随机矩阵（K 非 A-不变）
  4. C 行数 p = 1, 2, 3；增广行数 k = 1, 2
  判据全部用**原始 4 块** (A) 与**精确子式 gcd** (S) ✓
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
rank_exact, matmul = _ns2["rank_exact"], _ns2["matmul"]

_ns3 = {"__file__": os.path.join(_HERE, "batch_c6p_k.py")}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    exec(compile(fh.read().split("def main()")[0], "helpers", "exec"), _ns3)
mat = _ns3["mat"]
solve_Lambda = _ns3["solve_Lambda"]
S_holds = _ns3["S_holds"]


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


def probe(A, C, L, record):
    n = len(A)
    CA = matmul(C, A)
    B = ker_basis(stack(C, CA))
    if not B or not B[0]:
        return None
    d = len(B[0])
    q0 = len(L)
    H = matmul(L, B)
    Fm = matmul(matmul(L, A), B)
    rH = rk(H)
    t5a = rH < q0
    h1 = (rk(stack(H, Fm)) == rH) if rH > 0 else None
    sols = solve_Lambda(A, C, L)
    found_S = False
    for Lam in sols:
        if matmul(Lam, H) == Fm and S_holds(Lam, H):
            found_S = True
            break
    rec = dict(d_CA=d, q0=q0, rH=rH, t5a=t5a, h1=h1, S=found_S, n_lam=len(sols))
    record.append(rec)
    return rec


def main():
    print("=== 情形 II 大范围复核：(A) ⟹ (S) 失败？ ===\n")
    rng = random.Random(20251015)
    shapes = []

    # --- 结构族：手工 + 随机 ---
    def rand_mat(n, lo=-2, hi=2):
        return [[F(rng.randint(lo, hi)) for _ in range(n)] for _ in range(n)]

    families = []
    # (a) 幂零 n=6 指标 2
    families.append(("nilp2_n6", [[F(0),F(0),F(0),F(1),F(0),F(0)],
                                  [F(0),F(0),F(0),F(0),F(1),F(0)],
                                  [F(0),F(0),F(0),F(0),F(0),F(1)],
                                  [F(0)]*6, [F(0)]*6, [F(0)]*6]))
    # (b) 幂零 n=6 指标 3
    families.append(("nilp3_n6", [[F(0),F(0),F(0),F(1),F(0),F(0)],
                                  [F(0),F(0),F(0),F(0),F(1),F(0)],
                                  [F(0)]*6,
                                  [F(0),F(0),F(0),F(0),F(0),F(1)],
                                  [F(0)]*6, [F(0)]*6]))
    # (c) 一般随机 n=6
    for t in range(6):
        families.append(("rand_n6_%d" % t, rand_mat(6)))
    # (d) 一般随机 n=7
    for t in range(3):
        families.append(("rand_n7_%d" % t, rand_mat(7)))

    tot = dict(A=0, t5a=0, h1=0, h1_false=0, S=0, both=0)
    for fname, A in families:
        n = len(A)
        for p in [1, 2]:
            for k in [1, 2]:
                r = 1
                q0 = r + k
                for trial in range(140):
                    C = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
                    L = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q0)]
                    if rk(C) != p or rk(L) != q0:
                        continue
                    CA = matmul(C, A)
                    B = ker_basis(stack(C, CA))
                    if not B or not B[0]:
                        continue
                    d = len(B[0])
                    if d < q0:
                        continue                      # 只要情形 II
                    if not condA(A, C, L):
                        continue
                    tot["A"] += 1
                    H = matmul(L, B)
                    Fm = matmul(matmul(L, A), B)
                    rH = rk(H)
                    if rH < q0:
                        tot["t5a"] += 1
                    h1 = (rk(stack(H, Fm)) == rH)
                    if h1:
                        tot["h1"] += 1
                    else:
                        tot["h1_false"] += 1
                    found_S = False
                    for Lam in solve_Lambda(A, C, L):
                        if matmul(Lam, H) == Fm and S_holds(Lam, H):
                            found_S = True
                            break
                    if found_S:
                        tot["S"] += 1
                        if rH < q0:
                            tot["both"] += 1
        print("  [%s] 累计：情形 II 的 (A)-点 %d ；其中 T5a %d ；H1≠0 %d ；H1=0 %d ；(S) 成立 %d"
              % (fname, tot["A"], tot["t5a"], tot["h1"], tot["h1_false"], tot["S"]))

    print("\n=== 汇总（所有结构族） ===")
    print("情形 II 的 (A)-点总数        : %d" % tot["A"])
    print("  其中 T5a（rk H < q0）成立  : %d" % tot["t5a"])
    print("  其中 H1 ≠ 0（rk[H;F]=rk H）: %d" % tot["h1"])
    print("  其中 H1 = 0                : %d   ← 这些才有可能是 YES" % tot["h1_false"])
    print("  其中 (S) 成立（=YES 候选） : %d" % tot["S"])
    print("  其中 (A)∧T5a∧(S) 同时成立  : %d   ← **真正的反例**" % tot["both"])
    if tot["both"] == 0:
        print("\n⟹ 全部结构族上：情形 II 的 (A)-点 **无一** 使 (S) 成立 ⟹ 与 FINAL §4.5 一致 ✓")
        print("   且 H1≠0 占 %d/%d ⟹ 机制（F=ΛH ⟹ im H 含 Λ-特征向量）可作为**证明路线** ✓"
              % (tot["h1"], tot["A"]))
    else:
        print("\n⟹⟹ **发现 (A)∧T5a∧(S) 的反例** ⟹ 情形 II 可为 YES ⟹ c6′ 假 ⟹ 必须上报 ⚠️")


if __name__ == "__main__":
    main()
