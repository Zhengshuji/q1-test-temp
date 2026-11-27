# -*- coding: utf-8 -*-
"""
batch_r2.py —— 在 r>=2（q0 = r+k >= 3）下验证 c6′
复用 batch_c6p_k.py 的辅助函数（其 main 有 __main__ 保护 ✓）
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
    src = fh.read()
src = src.split("def main()")[0]           # 只取辅助函数
exec(compile(src, "helpers", "exec"), _ns3)
mat = _ns3["mat"]; rk2 = _ns3["rk2"]; mm2 = _ns3["mm2"]
checkA = _ns3["checkA"]; solve_Lambda = _ns3["solve_Lambda"]; S_holds = _ns3["S_holds"]


def main():
    print("=== r>=2 下验证 c6′（q0 = r+k >= 3）===\n")
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
            rca = [row[:] for row in R if any(x != 0 for x in row)]
            if not rca:
                continue
            for (r, k) in [(2, 1), (2, 2), (3, 1)]:
                q0 = r + k
                need = (r - 1) + k                  # L0 里除 l0 外的行 + k 个额外行
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
                    if rk2(P0 + PA) != 1:           # 真平行 ✓
                        continue
                    if not checkA(A, C, L):         # (A) ✓
                        continue
                    H = mm2(L, B)
                    if not (rk2(H) < q0):           # T5a ✓
                        continue
                    n_ok += 1
                    sols = solve_Lambda(A, C, L)
                    Ft = mm2(mm2(L, A), B)
                    found = any(mm2(Lam, H) == Ft and S_holds(Lam, H) for Lam in sols)
                    if found:
                        n_S += 1
                    print("[%s/%s] n=%d d_CA=%d r=%d k=%d q0=%d | 真平行T (A)T T5aT | 解=%d (S)成立？%s" %
                          (aname, cname, n, d, r, k, q0, len(sols), found))
                    done = True
                    break
                if not done:
                    pass
    print("\n=== 统计 ===")
    print("满足 真平行∧(A)∧T5a 的实例：%d" % n_ok)
    print("其中 (S) 成立的：%d" % n_S)
    if n_ok and n_S == 0:
        print("⟹ c6′ 在 r>=2 下**全部成立** ✓")
    elif n_S:
        print("⟹ **发现反例** ⟹ c6′ 假 ⟹ 情形 II 平行可为 YES ✓✓")
    return n_ok, n_S


if __name__ == "__main__":
    main()
