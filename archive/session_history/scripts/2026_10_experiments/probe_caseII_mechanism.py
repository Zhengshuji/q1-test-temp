# -*- coding: utf-8 -*-
"""
probe_caseII_mechanism.py —— 情形 II 的 **(A)∧(S)** 机制：独立复核 + 结构定位

【出发点（本项目已验证的事实）】
  T5′：(A) 的分解 ⟹ F = Λ·H         （H = L·N_CA, F = L·A·N_CA）
  T5 ：(S) ⟺ im H ∩ ker(λI−Λ) = 0 ∀λ，即 (S) 失败 ⟺ ∃λ, im H ∩ ker(λI−Λ) ≠ 0

【本轮的结构性猜想（本脚本要检验它）】
  令  H1 := { y ∈ (Q^q0)* : y·L·N_CA·A  ∈ row(N_CA) }   （“对偶不变”见证空间）
  则   H1 ≠ 0  ⟹  存在 Λ（满足 F=ΛH 的那一族）在 im H 上有特征向量
                 ⟹  (S) **必然失败**
  而 H1 ≠ 0 的对偶刻画正是：  rk[ (L·N_CA) ; (L·A·N_CA) ] == rk(L·N_CA)   （行空间包含 ✓）
  —— 这恰好是**本项目 T12 所证明的 (A)⟹T5a 那个机制**的"秩满版"。

【复核内容】
  ① (A) 成立时，rk[H;F] == rk H 是否**恒成立**？
  ② 若是 ⟹ 对**每一个**满足 F=ΛH 的 Λ，检查 Λ 在 im H 上是否必有特征向量
     （即 (S) 是否必失败）—— 用精确子式 gcd 判据 vs 直接构造特征向量对照
  ③ 反例搜索：随机/穷举大量 (A)-点，找 (A) ∧ (S) 同时成立者
"""
import os, io, contextlib, itertools, random
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
solve_Lambda = _ns3["solve_Lambda"]
S_holds = _ns3["S_holds"]


def rows(M):
    return [r[:] for r in M]


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


def eigen_on_imH(Lam, H):
    """
    检查 Λ 在 im H 上是否有特征向量（**等价于 (S) 失败**）。
    精确做法：把 H 的**列空间**取成基 U（q0×rho），在 U 上表示 Λ：
        需要解 Λ·U = U·B   （B 为 rho×rho）
    再判 B 是否有特征向量（在 Q 上：B 的特征多项式有有理根；本项目 λ 取 C ⟹ 恒有 ✓）
    """
    q0, d = len(H), len(H[0])
    rho = rk(H)
    if rho == 0:
        return False, None
    # 取 H 的列空间的基 U
    Ht = [[H[i][j] for i in range(q0)] for j in range(d)]     # d×q0，行张成 im H
    U = [r[:] for r in ker_basis(Ht)]                         # ？这里改用行化简
    # 更稳：直接对 H^T 求列空间的基 = H 的列基
    Ut = [[H[i][j] for i in range(q0)] for j in range(d)]
    # 用 rref 求 Ut 的列基：
    R = [r[:] for r in Ut]
    piv = []
    rr = 0
    for c in range(q0):
        sel = None
        for i in range(rr, d):
            if R[i][c] != 0:
                sel = i; break
        if sel is None:
            continue
        R[rr], R[sel] = R[sel], R[rr]
        pv = R[rr][c]; R[rr] = [x / pv for x in R[rr]]
        for i in range(d):
            if i != rr and R[i][c] != 0:
                f = R[i][c]; R[i] = [R[i][j] - f * R[rr][j] for j in range(q0)]
        piv.append(c); rr += 1
        if rr == d:
            break
    basis_cols = [c for c in piv]
    Ucols = [[Ut[i][c] for c in basis_cols] for i in range(d)]   # 错：应是 q0×rho
    Umat = [[H[i][c] for c in basis_cols] for i in range(q0)]    # q0 × rho ✓
    # 解 Λ·Umat = Umat·B  （B 为 rho×rho）
    unk = rho * rho
    Des, rhs = [], []
    for i in range(q0):
        for j in range(rho):
            row = [F(0)] * unk
            for t in range(rho):
                row[t * rho + j] = Umat[i][t]
            Des.append(row)
            rhs.append([sum(Lam[i][k] * Umat[k][j] for k in range(q0))])
    sol = solve_exact(Des, rhs)
    if sol is None:
        return None, None       # im H 不 Λ-不变 ⟹ 无 B（不应发生，因为 F=ΛH）
    Bm = [[sol[0][t * rho + j] for t in range(rho)] for j in range(rho)]
    # 检查 Bm 是否有特征向量（在 Q 上；若在 Q 上无，仍可能有复特征向量，
    # 因为本项目 λ ∈ C ⟹ 复数也可）
    # 判据：任何复矩阵都有特征值 ⟹ 只要 rho ≥ 1 就有 ⟹ 等价于直接检查
    # im H ∩ ker(λI−Λ) ≠ 0 对某个复 λ。用"秩亏"判据：
    #   ∃λ: rk(λH − ΛH) < rk(H)  ⟺  rank_{Q[λ]}(λH − F) < rk H
    return True, Bm


def main():
    print("=== 情形 II 的 (A)∧(S) 机制：独立复核 ===\n")
    A_list = [
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("nilp6b", mat([[0,0,0,1,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
    ]
    C_list = [
        ("p2a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
        ("p1",  mat([[0,0,0,1,0,0]])),
    ]
    tot_pts = tot_A = tot_A_and_S = tot_H1 = 0
    for aname, A in A_list:
        n = len(A)
        for cname, C in C_list:
            CA = matmul(C, A)
            R = stack(C, CA)
            B = ker_basis(R)
            if not B or not B[0]:
                continue
            d = len(B[0])
            Bg = _left_inverse(B)
            if Bg is None:
                continue
            rng = random.Random(hash((aname, cname)) & 0xffff)
            npts_A = nS = nH1 = 0
            for trial in range(120):
                # 随机造一行/两行 L（L0 随机 + 增广行随机），大小系数
                rank_ok = False
                for _ in range(60):
                    L0 = [[F(rng.randint(-2, 2)) for _ in range(n)]]
                    if rk(L0) != 1:
                        continue
                    L1 = [[F(rng.randint(-2, 2)) for _ in range(n)]]
                    L = L0 + L1
                    if rk(L) != 2:
                        continue
                    rank_ok = True
                    break
                if not rank_ok:
                    continue
                tot_pts += 1
                if not condA(A, C, L):
                    continue
                npts_A += 1
                tot_A += 1
                H = matmul(L, B)
                Fm = matmul(matmul(L, A), B)
                # H1 ≠ 0 ⟺ rk[H;F] == rk H
                h1 = (rk(stack(H, Fm)) == rk(H))
                if h1:
                    nH1 += 1
                    tot_H1 += 1
                sols = solve_Lambda(A, C, L)
                found_S = False
                for Lam in sols:
                    if matmul(Lam, H) != Fm:
                        continue
                    if S_holds(Lam, H):
                        found_S = True
                        break
                if found_S:
                    nS += 1
                    tot_A_and_S += 1
            print("[%s/%s] n=%d p=%d d_CA=%d | (A)-点 %d  其中 H1≠0: %d  (S) 成立: %d" %
                  (aname, cname, n, len(C), d, npts_A, nH1, nS))
    print("\n=== 汇总 ===")
    print("随机点总数 = %d ；其中 (A)-点 = %d" % (tot_pts, tot_A))
    print("(A)-点中 H1≠0（即 rk[H;F]==rk H）= %d / %d" % (tot_H1, tot_A))
    print("(A)-点中 (S) 成立 = %d / %d  ⟹ **反例（YES）**" % (tot_A_and_S, tot_A))
    if tot_A_and_S == 0:
        print("\n⟹ 在本批实例上，(A) ⟹ (S) 失败 恒成立 ⟹ 与 FINAL「情形 II：(A)∧(S)=0/200」一致 ✓")
    else:
        print("\n⟹ **发现 (A)∧(S) 同时成立的点** ⟹ 与 FINAL §4.5 冲突，必须复核 ✗")


def _left_inverse(B):
    n, d = len(B), len(B[0])
    Bt = [[B[i][j] for i in range(n)] for j in range(d)]
    out = []
    for j in range(d):
        ej = [[F(1) if i == j else F(0)] for i in range(d)]
        r = solve_exact(Bt, ej)
        if r is None:
            return None
        out.append(r[0])
    return out


if __name__ == "__main__":
    main()
