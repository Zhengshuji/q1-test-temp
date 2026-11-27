r"""
c6_ker_criterion.py -- ⭐⭐ 化简：(5a) ⟺ ker H ⊆ ker F

【命题】
  (5a)  rank[LA; L; CA; C] = rank[L; CA; C]
  ⟺  ∃Λ: F = Λ∘H            （history/44 的桥：右乘 N_CA 杀掉 C, CA 项）
  ⟺  ker H ⊆ ker F          （**可提升性**：F 经 H 分解 ⟺ 核包含）

其中 H = L·N_CA,  F = L·A·N_CA（都是 q×d）

【判据实现】ker H ⊆ ker F ⟺ F·(ker H 的基) = 0
"""
import os
import io
import contextlib
import random
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]


def ker_le(M1, M2):
    """ker(M1) ⊆ ker(M2) ？  M1: a×n, M2: b×n

    ⚠️ 库的 ker_basis 返回 **n×d** 矩阵（行=坐标）⟹ 直接用它作 K1m
       （绝不可再转置 —— 否则 mm 会因不检查维数而静默算错 ❗项目第 13 处禁区）
    """
    K1 = ker_basis(M1)                     # n×d
    if not K1 or not K1[0]:
        return True                        # ker M1 = 0 ⟹ 平凡包含
    K1m = K1                               # 已经就是 n×d
    assert len(M2[0]) == len(K1m), "维数不匹配（ker_le）"
    return rk(mm(M2, K1m)) == 0


def solve_lin(Amat, bvec):
    """简单 Gauss；返回一个解或 None"""
    m = len(Amat); n = len(Amat[0])
    M = [[Fr(Amat[i][j]) for j in range(n)] + [Fr(bvec[i])] for i in range(m)]
    piv_row = 0
    where = [-1] * n
    for c in range(n):
        p = None
        for i in range(piv_row, m):
            if M[i][c] != 0:
                p = i; break
        if p is None:
            continue
        M[piv_row], M[p] = M[p], M[piv_row]
        pv = M[piv_row][c]
        M[piv_row] = [x / pv for x in M[piv_row]]
        for i in range(m):
            if i != piv_row and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[piv_row][j] for j in range(n + 1)]
        where[c] = piv_row
        piv_row += 1
        if piv_row == m:
            break
    for i in range(piv_row, m):
        if all(M[i][j] == 0 for j in range(n)) and M[i][n] != 0:
            return None
    x = [Fr(0)] * n
    for c in range(n):
        if where[c] >= 0:
            x[c] = M[where[c]][n]
    return x


def main():
    print("=== 验证 (5a) ⟺ ker H ⊆ ker F ===\n")
    rng = random.Random(31415926)
    agree = 0
    n_tot = 0
    both_true = 0
    both_false = 0
    bad = []

    for trial in range(4000):
        n = 5
        p = rng.choice([1, 2])
        q = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if rk(C) != p:
            continue
        W = C + mm(C, A)
        rCW = rk(W)
        N = ker_basis(W)
        if not N or not N[0]:
            continue
        d = len(N[0])                    # N 已经是 n×d 矩阵（行=坐标）
        Nb = [[N[i][j] for j in range(d)] for i in range(n)]

        # —— 构造 (5a)-成立的 L（一半概率），否则随机 L ——
        mode = "random"
        L = None
        if trial % 2 == 0:
            # 求 v 使 vA ∈ row[C;CA]：vA = a·C + b·CA
            # 未知量 [v_1..v_n, a_1..a_p, b_1..b_p]
            rows = []
            rhs = []
            for j in range(n):
                row = [A[i][j] for i in range(n)]          # (vA)_j = Σ_i v_i A_{ij}
                row += [-C[k][j] for k in range(p)]
                row += [-W[k][j] for k in range(len(W))]
                rows.append(row)
                rhs.append(Fr(0))
            sol = solve_lin(rows, rhs)
            if sol is None:
                continue
            cand = [sol[i] for i in range(n)]
            if rk([cand]) != 1:
                continue
            Lcand = []
            for _i in range(q):
                s = solve_lin(rows, rhs)
                if s is None:
                    break
                v = [s[i] for i in range(n)]
                if rk(Lcand + [v]) == len(Lcand) + 1:
                    Lcand.append(v)
            if len(Lcand) != q:
                continue
            L = Lcand
            mode = "A-ok"
        else:
            L = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q)]
            if rk(L) != q:
                continue

        H = mm(L, Nb)
        Fm = mm(mm(L, A), Nb)

        a_rank = (rk(mm(L, A) + L + W) == rk(L + W))
        a_ker = ker_le(H, Fm)

        n_tot += 1
        if a_rank == a_ker:
            agree += 1
            if a_rank:
                both_true += 1
            else:
                both_false += 1
        elif len(bad) < 5:
            bad.append((trial, mode, a_rank, a_ker, n, p, q, d))

    print("随机实例：%d" % n_tot)
    print("  一致：%d" % agree)
    print("    两者皆 True ：%d   ← **判定力所需**" % both_true)
    print("    两者皆 False：%d" % both_false)
    print("  不一致：%d" % (n_tot - agree))
    for t in bad:
        print("    trial=%d mode=%s rank=%s ker=%s (n=%d,p=%d,q=%d,d=%d)" % t)
    print()
    if n_tot - agree == 0 and both_true > 0 and both_false > 0:
        print("⟹⟹⟹ **命题成立**：两侧都有点 ✓✓")
        print("     ⟹ (5a) ⟺ ker(H) ⊆ ker(F) —— 只依赖 (H,F)，不依赖 R 的具体选择")
        print("     ⟹ 判定问题可在 **d 维空间** 中重述（d = d_CA）⭐")
    elif both_true == 0:
        print("⚠️ 无 True 点 —— 判定力不足")
    else:
        print("⚠️ 有不一致，需检查")


if __name__ == "__main__":
    main()
