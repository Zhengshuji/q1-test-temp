# -*- coding: utf-8 -*-
"""
probe_exhaustive_q2.py —— **穷举**搜索：情形 II 下是否存在 (A) ∧ T5a ∧ (S) ？

【方法（完备搜索，非采样）】
  取 q0 = 2（k=1）的最小形状。第二行 l 在 Q^n 中，把 (A) 与 T5a 作为关于 l 的条件：
    (A)  : rk[LA;L;C;CA] == rk[L;C;CA]，  L = [L0 ; l]
    T5a  : rk(L·N_CA) < 2，  即 l 在 K = im N_CA 上与 L0 **成比例**
    (S)  : ∃λ, rk(λH − F) < rk H    （H = L·N_CA，F = L·A·N_CA）

  **参数化（完备）**：T5a ⟺ l|_K = μ·(L0|_K)。把 l 拆成
        l = μ·L0 + z ,   z|_K = 0   即 z ∈ row[C;CA]
  —— 由 T5a 的线性性，这是**全部**满足 T5a 的 l ✓（μ ∈ Q，z ∈ row[C;CA]）。
  于是只需枚举（μ, z）即覆盖所有候选，再逐个精确判 (A) 与 (S)。

  row[C;CA] 的基可从 [C;CA] 的行化简得到 ✓。
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]
rref_lib = _ns["rref"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rank_exact, solve_exact, matmul = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]

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


def rowspace_basis(M):
    """M 的行空间的一组基（行向量列表）"""
    if not M or not M[0]:
        return []
    R, piv = rref_lib([[F(x) for x in row] for row in M])
    return [R[i][:] for i in range(len(piv))]


def add(u, v):
    return [a + b for a, b in zip(u, v)]


def smul(a, u):
    return [a * x for x in u]


def S_holds_correct(H, Fm):
    """(S) 的**正确**判据：(S) ⟺ 对一切 λ, rk(λH−F) == rk H。

    ⚠️ 初版把 (S) 写成「∃λ 满秩」—— 那是**错的**（H=[[1,0]],F=0 的反例）。
    这里逐 λ 检查 ✓（λ 取 0,±1,±2,±3,±1/2,±1/3）
    """
    rH = rk(H)
    for lam in [F(0), F(1), F(-1), F(2), F(-2), F(3), F(1, 2), F(-1, 3), F(5, 7)]:
        M = [[lam * H[i][j] - Fm[i][j] for j in range(len(H[0]))] for i in range(len(H))]
        if rk(M) != rH:
            return False
    return True


def main():
    print("=== 穷举：情形 II 下 (A) ∧ T5a ∧ (S) 是否存在 ===\n")
    A_list = [
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("nilp6b", mat([[0,0,0,1,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("nilp3",  mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,0],
                        [0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
    ]
    C_list = [
        ("p2a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
        ("p2b", mat([[0,0,0,1,1,0],[0,0,0,0,1,0]])),
        ("p1",  mat([[0,0,0,1,0,0]])),
    ]
    L0_list = [
        ("e1", mat([[1,0,0,0,0,0]])),
        ("e2", mat([[0,1,0,0,0,0]])),
        ("e1+e2", mat([[1,1,0,0,0,0]])),
        ("e1+e6", mat([[1,0,0,0,0,1]])),
        ("e3", mat([[0,0,1,0,0,0]])),
    ]
    mus = [F(0), F(1), F(-1), F(2), F(1, 2)]
    tot = dict(inst=0, cand=0, A=0, t5a_A=0, S=0, both=0)
    log = []
    for aname, A in A_list:
        n = len(A)
        for cname, C in C_list:
            CA = matmul(C, A)
            R = stack(C, CA)
            B = ker_basis(R)
            if not B or not B[0]:
                continue
            d = len(B[0])
            RB = rowspace_basis(R)                    # row[C;CA] 的基（= z 的可选空间）
            for l0name, L0 in L0_list:
                q0 = 2
                if d < q0:
                    continue                          # 只要情形 II
                tot["inst"] += 1
                # (A) 是否可能？（先看 L0 自身 + 任意 z 的情形）
                # 枚举 μ 与 z = row[C;CA] 中的**小系数组合**
                maxz = len(RB)
                coeff_grid = [F(-1), F(0), F(1)]
                zs = [[F(0)] * n]
                for j in range(maxz):
                    zs.append(RB[j][:])
                for idx in itertools.combinations(range(maxz), 2):
                    for a in coeff_grid:
                        for b in coeff_grid:
                            if a == 0 and b == 0:
                                continue
                            zs.append(add(smul(a, RB[idx[0]]), smul(b, RB[idx[1]])))
                seen = set()
                for mu in mus:
                    for z in zs:
                        l = add(smul(mu, L0[0]), z)
                        key = tuple(l)
                        if key in seen:
                            continue
                        seen.add(key)
                        L = [L0[0][:], l]
                        if rk(L) != 2:
                            continue
                        tot["cand"] += 1
                        H = matmul(L, B)
                        Fm = matmul(matmul(L, A), B)
                        rH = rk(H)
                        if not (rH < 2):
                            continue                  # T5a 必须成立
                        if not condA(A, C, L):
                            continue
                        tot["A"] += 1
                        tot["t5a_A"] += 1
                        found_S = False
                        if S_holds_correct(H, Fm):
                            found_S = True
                        if found_S:
                            tot["S"] += 1
                            tot["both"] += 1
                            log.append((aname, cname, l0name, mu, l, H, Fm))
                print("  [%s/%s/%s] 累计：候选 %d，满足 (A)∧T5a 的 %d，其中 (S) 成立 %d"
                      % (aname, cname, l0name, tot["cand"], tot["t5a_A"], tot["S"]))
    print("\n=== 汇总 ===")
    print("实例×L0 组合        : %d" % tot["inst"])
    print("枚举到的候选 l 数    : %d" % tot["cand"])
    print("其中 (A)∧T5a 成立    : %d" % tot["t5a_A"])
    print("其中 (S) 也成立      : %d      ← **YES 实例**" % tot["S"])
    if tot["both"] == 0:
        print("\n⟹ 穷举范围内：情形 II 的 **(A)∧T5a ⟹ (S) 失败** 无例外 ⟹ 支持 c6′ ✓")
    else:
        print("\n⟹⟹ **反例！** 情形 II 可为 YES ⟹ c6′ 假 ⚠️")
        for rec in log[:5]:
            print("   ", rec[0], rec[1], rec[2], "mu=", rec[3], "l=", [str(x) for x in rec[4]])


if __name__ == "__main__":
    main()
