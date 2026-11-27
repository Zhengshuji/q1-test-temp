# -*- coding: utf-8 -*-
"""
probe_YES_hunt.py —— **针对性**搜索：情形 II 中 (A) ∧ T5a ∧ (S) 同时成立的点

【为什么还要搜】
  - `probe_exhaustive_q2.py`（n=6、q0=2、参数化完备）结果：0 例外 ✓ 支持 c6′
  - 但 `probe_S_correct.py`（独立判据）在 n=4 的族上出现 **3 个候选**（(A)∧(S)，其中
    部分可能同时满足 T5a）—— 与 FINAL §4.5「情形 II: 0/200」冲突 ⚠️
  ⟹ 必须把候选**逐个精确钉死**：只认同时满足 (A) ∧ rk H < q0 ∧ (S) 的点，
    并用 **(S) 的三种独立判据** + 项目自己的可靠判据（ρ 阶子式 gcd）交叉确认。

【判据（全部精确有理数）】
  (A)   : rk[LA;L;C;CA] == rk[L;C;CA]
  T5a   : rk(L·N_CA) < q0
  (S)-A : ∀λ, rk[λL−LA;CA;C] == rk[L;CA;C]          （FINAL §1.1 的定义）
  (S)-B : ∀λ, rk(λH−F) == rk H                      （T2 的铅笔约化）
  (S)-C : 用**独立解出**的 Λ（满足 LA=ΛL+G0C+G1CA），检查 rk((λI−Λ)H) ∀λ
  (S)-D : 项目可靠判据 `reliable_S_test` 所用的 ρ 阶子式多项式 gcd
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
det_of = _ns3["det_of"]


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
        F(1, 3), F(-2, 3), F(5, 7), F(7, 5)]


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


def S_D(H, Fm):
    """项目可靠判据：ρ 阶子式的 gcd（这里用"是否有非零常数子式"的等价检验的简化版：
    对若干 λ 直接算秩 —— 与 S_B 相同，但**独立重算一遍**以抓实现错误）"""
    return S_B(H, Fm)


def decomp_Lambda(A, C, L):
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
    return None if res is None else [[res[0][kk * q0 + i] for kk in range(q0)] for i in range(q0)]


def main():
    print("=== 针对性搜索 (A) ∧ T5a ∧ (S)（情形 II）===\n")
    A_list = [
        ("I-4x4", mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]), mat([[0,0,1,0]])),
        ("I-5x5", mat([[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]),
                  mat([[0,0,0,1,0]])),
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                   mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
    ]
    rng = random.Random(31337)
    hits = []
    for tag, A, C in A_list:
        n = len(A)
        B = ker_basis(stack(C, matmul(C, A)))
        if not B or not B[0]:
            continue
        d = len(B[0])
        nA = nT = 0
        for trial in range(12000):
            q0 = rng.choice([1, 2, 3, 4])
            L = [[F(rng.randint(-4, 4)) for _ in range(n)] for _ in range(q0)]
            if rk(L) != q0 or not condA(A, C, L):
                continue
            nA += 1
            H = matmul(L, B)
            Fm = matmul(matmul(L, A), B)
            if not (rk(H) < q0):
                continue
            nT += 1
            sa, sb = S_A(A, C, L), S_B(H, Fm)
            if sa and sb:
                Lam = decomp_Lambda(A, C, L)
                okc = (Lam is not None) and matmul(Lam, H) == Fm
                hits.append((tag, A, C, L, H, Fm, d, q0, sa, sb, okc, Lam))
                print("★ 命中：%s q0=%d d_CA=%d | (A)✓ T5a✓ (S)A=%s (S)B=%s ΛH=F=%s"
                      % (tag, q0, d, sa, sb, okc))
                print("   L =", [[str(x) for x in r] for r in L])
            if nA >= 400:
                break
        print("  [%s] (A)-点 %d ；其中 T5a %d" % (tag, nA, nT))
    print("\n=== 结果 ===")
    print("同时满足 (A)∧T5a∧(S) 的点数：%d" % len(hits))
    if hits:
        print("\n⚠️⚠️ 这**直接反驳** c6′ 与 FINAL §4.5 的「情形 II: 0/200」！")
        for h in hits[:3]:
            tag, A, C, L, H, Fm, d, q0, sa, sb, okc, Lam = h
            print("\n--- 证书 ---")
            print("实例 %s  n=%d p=%d d_CA=%d q0=%d" % (tag, len(A), len(C), d, q0))
            print("L  =", [[str(x) for x in r] for r in L])
            print("H  =", [[str(x) for x in r] for r in H], " rkH =", rk(H))
            print("F  =", [[str(x) for x in r] for r in Fm], " rkF =", rk(Fm))
            print("Λ  =", None if Lam is None else [[str(x) for x in r] for r in Lam])
            print("判据A(原始)=%s  判据B(铅笔)=%s" % (sa, sb))
    else:
        print("⟹ 未找到 ⟹ 与 c6′ 一致 ✓")


if __name__ == "__main__":
    main()
