# -*- coding: utf-8 -*-
"""
batch_c6p_k.py —— 在 **k>=1**（项目设定 q0 = r+k）下批量验证 c6′

设定：L 是 q0×n，q0 = r+k；L0 = 前 r 行。
  (A)  ⟺ rk[LA;L;C;CA] == rk[L;C;CA]
  T5a  ⟺ rk(L·N_CA) < q0
  真平行 ⟺ rk[Π(L); Π(L·A)] == 1   （**必须**用它过滤 ✓ —— 第 24 处自查）
  (S)  ⟺ rank_{Q(λ)}(λH - ΛH) == rank H，H = L·N_CA

构造：L = [l0 ; l1]，l1 ∈ row[C;CA]（⟹ Π(l1)=0 ✓），l0 取使 Π(l0)≠0 且真平行的行 ✓
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    s = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s, "lib", "exec"), _ns)
ker = _ns["ker_basis"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rk2, se, mm2 = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]


def mat(r):
    return [[F(x) for x in q] for q in r]


def checkA(A, C, L):
    return rk2(mm2(L, A) + L + C + mm2(C, A)) == rk2(L + C + mm2(C, A))


def nullspace(N):
    r = se(N, [[F(0)] for _ in range(len(N))])
    return [] if r is None else r[1]


def det_of(M):
    n = len(M)
    if n == 0:
        return F(1)
    if n == 1:
        return M[0][0]
    A = [row[:] for row in M]
    det = F(1)
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0:
                piv = i; break
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]; det = -det
        det *= A[c][c]
        inv = F(1) / A[c][c]
        for i in range(c + 1, n):
            f = A[i][c] * inv
            if f != 0:
                A[i] = [A[i][j] - f * A[c][j] for j in range(n)]
    return det


def solve_Lambda(A, C, L):
    """解 (A) 的分解 LA = ΛL + G0 C + G1 CA，返回满足 ΛH = F 的**全部** Λ（抽样的）。

    ⚠️ **2026 修正（重要）**：原实现用库 `solve`（exact_count_thm7.py）取解，
    但**库 solve 在本系统上会给出不满足残差的"解"** —— 实测：
        同一实例上，独立求解器给的 Λ 满足 ΛH = F，库给的 Λ 不满足 ✗
    （`scripts/core/diag_Lambda_map.py` 逐解对照；200 个 (A)-点中 193 个分歧）
    ⟹ 这里改用 `linalg_exact.solve_exact`（**带维数断言**的独立实现），
      并对每条解**显式验证残差全零**（杜绝静默错误）。
    """
    r, n, p = len(L), len(A), len(C)
    CA = mm2(C, A)
    LA = mm2(L, A)
    nunk = r * r + 2 * r * p
    rows = []
    for i in range(r):
        for j in range(n):
            row = [F(0)] * nunk
            for kk in range(r):
                row[kk * r + i] = L[kk][j]
            for kk in range(p):
                row[r * r + i * p + kk] = C[kk][j]
            for kk in range(p):
                row[r * r + r * p + i * p + kk] = CA[kk][j]
            rows.append(row)
    rhs = [[LA[i][j]] for i in range(r) for j in range(n)]   # ← 原为 -LA ✗（符号错，见下）
    res = se(rows, rhs)                      # ← 独立求解器（原为库 solve ✗）
    if res is None:
        return []
    y, nsol = res

    def _resid(sol):
        return all(sum(rows[i][j] * sol[j] for j in range(nunk)) == rhs[i][0]
                   for i in range(len(rows)))

    out = []
    for sol in [y] + nsol:
        if not _resid(sol):                  # 显式残差检查（静默错误防线）
            continue
        Lam = [[sol[kk * r + i] for kk in range(r)] for i in range(r)]
        out.append(Lam)
    return out


def S_holds(Lam, H):
    """(S) ⟺ rank_{Q(λ)}(λH - ΛH) == rank H。用 ρ 阶子式的 gcd 判定。"""
    r, d = len(H), len(H[0])
    rho = rk2(H)
    if rho == 0:
        return True
    Fm = mm2(Lam, H)
    polys = []
    for ri in itertools.combinations(range(r), rho):
        for cj in itertools.combinations(range(d), rho):
            a = det_of([[H[i][j] for j in cj] for i in ri])
            b = -det_of([[Fm[i][j] for j in cj] for i in ri])
            if a != 0 or b != 0:
                polys.append((a, b))
    if not polys:
        return False
    # 一次多项式的公共因子：若所有 (a,b) 有公因子 (a0 λ + b0) ⟹ (S) 失败
    # 判据：存在 λ 使全部子式同时为 0。一次多项式的公共根 = 两两的公共根。
    base = None
    for p in polys:
        if p[0] == 0:
            return True                     # 有非零常数子式 ⟹ gcd=1
        if base is None:
            base = p; continue
        # base = a1λ+b1, p = a2λ+b2；公共根 λ = -b1/a1 需满足 a2λ+b2=0
        lam = -base[1] / base[0]
        if p[0] * lam + p[1] != 0:
            return True                     # 无公共根 ⟹ gcd=1
    return False                            # 全部有同一个公共根 ⟹ (S) 失败


def main():
    print("=== k>=1 下批量验证 c6′ ===\n")
    A_list = [
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("nilp6b", mat([[0,0,0,1,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
    ]
    C_list = [
        ("p2a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
        ("p2b", mat([[0,0,0,1,1,0],[0,0,0,0,1,0]])),
        ("p1",  mat([[0,0,0,1,0,0]])),
    ]
    n_ok = n_S = 0
    for aname, A in A_list:
        n = len(A)
        for cname, C in C_list:
            CA = mm2(C, A); R = C + CA
            B = ker(R)
            if not B or not B[0]:
                continue
            d = len(B[0])
            # r=1, k=1 ⟹ q0=2 ⟹ L 有两行：l0（基础）+ l1 ∈ row[C;CA]
            l1 = None
            for row in R:
                if any(x != 0 for x in row):
                    l1 = row[:]; break
            if l1 is None:
                continue
            # 找 l0：Π(l0)≠0 且 [Π(l0);Π(l0A)] 秩 1
            for i in range(n):
                l0 = [F(1) if kk == i else F(0) for kk in range(n)]
                L = [l0, l1]
                P0 = mm2(L, B); PA = mm2(mm2(L, A), B)
                if not any(x != 0 for x in P0[0]):
                    continue
                if rk2(P0 + PA) != 1:
                    continue
                if not checkA(A, C, L):
                    continue
                H = mm2(L, B)
                if not (rk2(H) < len(L)):
                    continue
                n_ok += 1
                sols = solve_Lambda(A, C, L)
                Fm_true = mm2(mm2(L, A), B)
                found_S = False
                for Lam in sols:
                    if mm2(Lam, H) != Fm_true:
                        continue
                    if S_holds(Lam, H):
                        found_S = True; break
                if found_S:
                    n_S += 1
                print("[%s/%s] n=%d d_CA=%d q0=2 k=1 | (A)T T5a T 真平行 T | 解=%d  (S)成立？%s" %
                      (aname, cname, n, d, len(sols), found_S))
                break
    print("\n=== 统计 ===")
    print("满足 真平行∧(A)∧T5a 的实例：%d" % n_ok)
    print("其中 (S) 成立的：%d" % n_S)
    if n_ok and n_S == 0:
        print("⟹ c6′ 在 k=1 下**全部成立** ✓（平行 ∧ (A) ∧ T5a ⟹ (S) 失败）")
    elif n_S:
        print("⟹ **发现反例** ⟹ c6′ 假 ⟹ 情形 II 平行可为 YES ✓✓")
    return n_ok, n_S


if __name__ == "__main__":
    main()
