# -*- coding: utf-8 -*-
"""
probe_YES_hunt2.py —— 在 **k ≥ 1（真的有增广行）且 H ≠ 0** 的过滤下搜索 (A)∧T5a∧(S)

【上一轮的教训】
  probe_YES_hunt.py 命中的唯一"反例"是 q0 = r = 1（即 **k = 0**，根本没有增广行）且 H = 0
  —— 那是**退化点**，不是项目的目标情形（项目定义 q0 = r + k，k ≥ 1）。
  ⟹ 必须把 **k ≥ 1** 与 **H ≠ 0** 作为显式过滤条件 ✓
  （同时也说明：c6′ 若为真，其陈述里"H ≠ 0"这一条是**必要**的，不是装饰 ✓）

【过滤条件】
  · k ≥ 1       ⟺ q0 > r（真的加了增广行）
  · H ≠ 0       ⟺ rk(L·N_CA) ≥ 1
  · (A)         : rk[LA;L;C;CA] == rk[L;C;CA]
  · T5a         : rk(L·N_CA) < q0
  · (S)         : ∀λ, rk[λL−LA;CA;C] == rk[L;CA;C]（判据A）
                  且 ∀λ, rk(λH−F) == rk H        （判据B）
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


LAMS = [F(0), F(1), F(-1), F(2), F(-2), F(3), F(-3), F(1, 2), F(-1, 2),
        F(1, 3), F(-2, 3), F(5, 7), F(7, 5), F(4, 9)]


def S_A(A, C, L):
    CA = matmul(C, A)
    LA = matmul(L, A)
    base = rk(stack(L, CA, C))
    return all(rk(stack([[lam * L[i][j] - LA[i][j] for j in range(len(L[0]))]
                         for i in range(len(L))], CA, C)) == base for lam in LAMS)


def S_B(H, Fm):
    rH = rk(H)
    return all(rk([[lam * H[i][j] - Fm[i][j] for j in range(len(H[0]))]
                   for i in range(len(H))]) == rH for lam in LAMS)


def main():
    print("=== 在 k≥1 且 H≠0 下搜索 (A)∧T5a∧(S)（情形 II）===\n")
    A_list = [
        ("I-4x4", mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]), mat([[0,0,1,0]])),
        ("I-5x5", mat([[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]),
                  mat([[0,0,0,1,0]])),
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                   mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
    ]
    rng = random.Random(999)
    tot = dict(A=0, A_k=0, A_k_H=0, A_k_H_T=0, S=0)
    hits = []
    for tag, A, C in A_list:
        n = len(A)
        B = ker_basis(stack(C, matmul(C, A)))
        if not B or not B[0]:
            continue
        d = len(B[0])
        nA = nk = nkH = nkT = nS = 0
        for trial in range(30000):
            q0 = rng.choice([2, 3, 4, 5])
            L = [[F(rng.randint(-4, 4)) for _ in range(n)] for _ in range(q0)]
            if rk(L) != q0 or not condA(A, C, L):
                continue
            nA += 1
            if not (q0 >= 2):                 # k = q0 - r ≥ 1
                continue
            nk += 1
            H = matmul(L, B)
            Fm = matmul(matmul(L, A), B)
            if rk(H) == 0:                    # H ≠ 0
                continue
            nkH += 1
            if not (rk(H) < q0):              # T5a
                continue
            nkT += 1
            sa, sb = S_A(A, C, L), S_B(H, Fm)
            if sa or sb:
                nS += 1
                hits.append((tag, A, C, L, H, Fm, d, q0, sa, sb))
                print("★ %s q0=%d d_CA=%d | (S)A=%s (S)B=%s  L=%s"
                      % (tag, q0, d, sa, sb, [[str(x) for x in r] for r in L]))
            if nA >= 1500:
                break
        print("  [%s] (A)点 %d → k≥1 %d → 且 H≠0 %d → 且 T5a %d → 且 (S) %d"
              % (tag, nA, nk, nkH, nkT, nS))
        tot["A"] += nA; tot["A_k"] += nk; tot["A_k_H"] += nkH
        tot["A_k_H_T"] += nkT; tot["S"] += nS
    print("\n=== 汇总（k≥1, H≠0, 情形 II）===")
    print("(A)-点                     : %d" % tot["A"])
    print("  k≥1                      : %d" % tot["A_k"])
    print("  且 H≠0                   : %d" % tot["A_k_H"])
    print("  且 T5a                   : %d" % tot["A_k_H_T"])
    print("  且 (S)                   : %d   ← **YES 实例**" % tot["S"])
    if tot["S"] == 0:
        print("\n⟹ 在 k≥1、H≠0 的过滤下，(A)∧T5a **恒推出 (S) 失败** ⟹ 支持 c6′ ✓")
        print("   （且说明 c6′ 的陈述中「H≠0」是必要假设 ✓）")
    else:
        print("\n⟹⟹ **发现真正的反例** ⟹ 情形 II 可为 YES ⟹ c6′ 假 ⚠️")


if __name__ == "__main__":
    main()
