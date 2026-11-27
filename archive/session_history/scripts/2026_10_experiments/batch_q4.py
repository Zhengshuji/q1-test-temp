# -*- coding: utf-8 -*-
"""
batch_q4.py —— 扩展到 q0>=4 验证 c6′

关键构造（由 §9/§12 的结构性事实）：
  1. 取满足 c·A^2 = 0 的 C  ⟹ ker[C;CA] 是 A-不变的 ✓
  2. 取 u = B 的某列（在 K 中）以及 A' 的特征方向（此处 u 取使 uA' ∥ u 的方向）
  3. 解 l·B = u 得到解空间（维数 n-d+1）⟹ 其中**每一行**自动满足 Π(l) = u 且 Π(lA) ∥ u ✓
  4. 取 r 行 ⟹ Π(L0) 全部 ∥ u ⟹ 真平行 ✓
  5. 再补 k 行 ∈ row[C;CA] ⟹ (A) 保持 ✓ 且 T5a 自动成立 ✓（rank Π 仍 ≤ r < r+k）
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

_ns3 = {"__file__": os.path.join(_HERE, "batch_c6p_k.py")}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    src = fh.read().split("def main()")[0]
exec(compile(src, "helpers", "exec"), _ns3)
mat = _ns3["mat"]; rk2 = _ns3["rk2"]; mm2 = _ns3["mm2"]
checkA = _ns3["checkA"]; solve_Lambda = _ns3["solve_Lambda"]; S_holds = _ns3["S_holds"]
se = _ns3["se"]


def solve_row(M, n):
    k = len(M[0])
    rows = [[M[j][t] for j in range(n)] for t in range(k)]
    res = se(rows, [[F(0)] for _ in range(k)])
    if res is None:
        return None
    y, nsol = res
    for v in ([y] if any(x != 0 for x in y) else []) + nsol:
        if any(x != 0 for x in v):
            return v[:]
    return None


def rows_with_pi(Lam_vec, B, A, r, n):
    """解 l·B = u（u = Σ coef·B 列），返回 r 个独立解"""
    d = len(B[0])
    Des = [[B[j][t] for j in range(n)] for t in range(d)]
    b = [[Lam_vec[t]] for t in range(d)]
    res = se(Des, b)
    if res is None:
        return []
    y, nsol = res
    cands = ([y] if any(x != 0 for x in y) else []) + nsol
    out = []
    for v in cands:
        if any(x != 0 for x in v):
            out.append(v)
    return out


def main():
    print("=== q0>=4 下验证 c6′ ===\n")
    A_list = [
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("N3a", mat([[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],
                     [0,0,0,0,1,0],[0,0,0,0,0,1],[0,0,0,0,0,0]])),
    ]
    n_ok = n_S = 0
    import itertools as it
    for aname, A in A_list:
        n = len(A)
        A2 = mm2(A, A)
        c = solve_row(A2, n)
        if c is None:
            continue
        C = [c]
        CA = mm2(C, A); R = C + CA
        B = ker(R)
        if not B or not B[0]:
            continue
        d = len(B[0])
        AB = mm2(A, B)
        if rk2([B[i] + AB[i] for i in range(n)]) != rk2(B):
            continue                          # 不变性
        rca = [row[:] for row in R if any(x != 0 for x in row)]
        if not rca:
            continue
        # 找 A' 的特征方向（**零空间法** ✓ —— 不用枚举 ✗）
        DesB = [[B[t][i] for i in range(d)] for t in range(n)]
        # (1) 求 M：解 B·M = A·B（逐列）
        Mcols = []
        okM = True
        for j in range(d):
            r = se(DesB, [[AB[t][j]] for t in range(n)])
            if r is None:
                okM = False; break
            Mcols.append(r[0])
        if not okM:
            continue
        M = [[Mcols[j][i] for j in range(d)] for i in range(d)]
        # (2) 对有理 λ，解 (M - λI)v = 0 的零空间
        eigdirs = []
        lams = [F(k) for k in range(-3, 4)] + [F(1,2), F(-1,2)]
        for lam in lams:
            N = [[M[i][j] - (lam if i == j else 0) for j in range(d)] for i in range(d)]
            r = se(N, [[F(0)] for _ in range(d)])
            if r is None:
                continue
            y, nsol = r
            for v in ([y] if any(x != 0 for x in y) else []) + nsol:
                if any(x != 0 for x in v):
                    u = [sum(v[j] * B[i][j] for j in range(d)) for i in range(n)]
                    if any(x != 0 for x in u):
                        eigdirs.append(u)
        if not eigdirs:
            print("[%s] 未找到特征方向，跳过" % aname)
            continue
        for u in eigdirs[:1]:
            base_rows = rows_with_pi(u, B, A, 3, n)
            if len(base_rows) < 2:
                continue
            for (r, k) in [(2, 2), (3, 1), (2, 3)]:
                q0 = r + k
                if len(base_rows) < r:
                    continue
                if len(rca) < k:
                    continue
                L = [base_rows[i] for i in range(r)] + [rca[t % len(rca)] for t in range(k)]
                P0 = mm2(L, B); PA = mm2(mm2(L, A), B)
                if rk2(P0 + PA) != 1:
                    continue
                if not checkA(A, C, L):
                    continue
                H = mm2(L, B)
                if not (rk2(H) < q0):
                    continue
                n_ok += 1
                sols = solve_Lambda(A, C, L)
                Ft = mm2(mm2(L, A), B)
                found = any(mm2(Lam, H) == Ft and S_holds(Lam, H) for Lam in sols)
                if found:
                    n_S += 1
                print("[%s] n=%d d_CA=%d r=%d k=%d q0=%d | 真平行T (A)T T5aT | 解=%d (S)成立？%s" %
                      (aname, n, d, r, k, q0, len(sols), found))
                break
    print("\n=== 统计（q0>=4）===")
    print("满足 真平行∧(A)∧T5a 的实例：%d" % n_ok)
    print("其中 (S) 成立的：%d" % n_S)
    if n_ok and n_S == 0:
        print("⟹ c6′ 在 q0>=4 下也**全部成立** ✓")
    elif n_S:
        print("⟹ **发现反例** ⟹ c6′ 假 ✓✓")
    return n_ok, n_S


if __name__ == "__main__":
    main()
