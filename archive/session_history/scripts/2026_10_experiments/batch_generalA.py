# -*- coding: utf-8 -*-
"""
batch_generalA.py —— 用**非 A^2=0** 的结构验证 c6′

关键：不变性的充分条件是 **CA^2 = 0**（比 A^2 = 0 弱 ✓）。
给定 A（A^2 ≠ 0），解出满足 c·A^2 = 0 的非零行 c 作 C ⟹ ker[C;CA] 自动 A-不变 ✓
"""
import os, io, contextlib
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
    """求 M^T 的核中非零行 c（即 c·M = 0）"""
    # 方程：Σ_j c_j M[j][k] = 0  对每个 k
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


def main():
    print("=== 非 A^2=0 结构下验证 c6′（用 CA^2=0 保证不变性）===\n")
    A_list = [
        ("N3a", mat([[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],
                     [0,0,0,0,1,0],[0,0,0,0,0,1],[0,0,0,0,0,0]])),
        ("N3b", mat([[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],
                     [0,0,0,0,1,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("N4",  mat([[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],
                     [0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,0,0]])),
    ]
    n_ok = n_S = 0
    for aname, A in A_list:
        n = len(A)
        A2 = mm2(A, A)
        print("[%s] A^2 == 0 ？%s" % (aname, all(x == 0 for r in A2 for x in r)))
        c = solve_row(A2, n)                 # c·A^2 = 0
        if c is None:
            print("  未找到满足 cA^2=0 的非零行，跳过")
            continue
        C = [c]
        CA = mm2(C, A); R = C + CA
        B = ker(R)
        if not B or not B[0]:
            print("  退化，跳过"); continue
        d = len(B[0])
        # 不变性检验（正确的列拼接判据 ✓）
        AB = mm2(A, B)
        inv = rk2([B[i] + AB[i] for i in range(n)]) == rk2(B)
        print("  d_CA=%d  不变性(列拼接)？%s" % (d, inv))
        if not inv:
            continue
        rca = [row[:] for row in R if any(x != 0 for x in row)]
        if not rca:
            continue
        for (r, k) in [(1, 1), (2, 1)]:
            q0 = r + k
            need = (r - 1) + k
            if len(rca) < need:
                continue
            extra = [rca[t % len(rca)] for t in range(need)]
            done = False
            for i in range(n):
                l0 = [F(1) if kk == i else F(0) for kk in range(n)]
                L = [l0] + [e[:] for e in extra]
                P0 = mm2(L, B); PA = mm2(mm2(L, A), B)
                if not any(x != 0 for x in P0[0]):
                    continue
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
                print("  r=%d k=%d q0=%d | 真平行T (A)T T5aT | 解=%d (S)成立？%s" %
                      (r, k, q0, len(sols), found))
                done = True
                break
            if done:
                break
    print("\n=== 统计（非 A^2=0）===")
    print("满足 真平行∧(A)∧T5a 的实例：%d" % n_ok)
    print("其中 (S) 成立的：%d" % n_S)
    if n_ok and n_S == 0:
        print("⟹ c6′ 在非 A^2=0 结构下也**全部成立** ✓（不变性来自 CA^2=0 ✓）")
    elif n_S:
        print("⟹ **发现反例** ⟹ c6′ 假 ✓✓")
    return n_ok, n_S


if __name__ == "__main__":
    main()
