# -*- coding: utf-8 -*-
"""
verify_mechanism.py —— 验证 §19.3 的机制链条

检查（在构造出的实例上）：
  (i)  u ∈ K 是 A' 的特征向量：π(uA) = λ·u        （u 视为 K 中元素）
  (ii) π(L·A) = λ·π(L)                            （**关键的一步**）
  (iii) 由 (A) 解出的 Λ 是否满足 Λ·H = λ·H
  (iv) 若 (iii) 成立 ⟹ im H ⊆ ker(λI-Λ) ⟹ (S) 失败 ✓
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


def nullspace(N):
    r = se(N, [[F(0)] for _ in range(len(N))])
    return [] if r is None else r[1]


def main():
    print("=== 验证 §19.3 的机制链条 ===\n")
    A = mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
             [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    C = mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])
    n = len(A)
    CA = mm2(C, A); R = C + CA
    B = ker(R)
    d = len(B[0])
    AB = mm2(A, B)
    print("n=%d d_CA=%d  不变性(列拼接)？%s" %
          (n, d, rk2([B[i] + AB[i] for i in range(n)]) == rk2(B)))

    # M = A' 在基 B 下的矩阵
    DesB = [[B[t][i] for i in range(d)] for t in range(n)]
    Mcols = []
    for j in range(d):
        r = se(DesB, [[AB[t][j]] for t in range(n)])
        if r is None:
            print("M 求解失败"); return
        Mcols.append(r[0])
    M = [[Mcols[j][i] for j in range(d)] for i in range(d)]

    # 找特征方向 u = B·v
    found = False
    for lam in [F(k) for k in range(-3, 4)] + [F(1,2), F(-1,2)]:
        N = [[M[i][j] - (lam if i == j else 0) for j in range(d)] for i in range(d)]
        r = se(N, [[F(0)] for _ in range(d)])
        if r is None:
            continue
        y, nsol = r
        vs = ([y] if any(x != 0 for x in y) else []) + nsol
        for v in vs:
            if not any(x != 0 for x in v):
                continue
            u = [sum(v[j] * B[i][j] for j in range(d)) for i in range(n)]
            # (i) π(uA) = λ u ？
            uA = [sum(u[j] * A[j][i] for j in range(n)) for i in range(n)]
            puA = [sum(uA[j] * B[j][t] for j in range(n)) for t in range(d)]
            lam_u = [lam * sum(u[j] * B[j][t] for j in range(n)) for t in range(d)]
            print("\nλ=%s  u=%s" % (lam, [str(x) for x in u]))
            print("  (i)  π(uA)=λu ？%s   π(uA)=%s" %
                  (puA == lam_u, [str(x) for x in puA]))

            # 造一行 l：l·B = u
            DesL = [[B[j][t] for j in range(n)] for t in range(d)]
            r3 = se(DesL, [[u[t]] for t in range(d)])
            if r3 is None:
                continue
            l = r3[0]
            if all(x == 0 for x in l):
                continue
            L = [l]
            # (ii) π(L·A) = λ·π(L) ？
            LA = mm2(L, A)
            pLA = mm2(LA, B)
            pL = mm2(L, B)
            lam_pL = [[lam * x for x in row] for row in pL]
            print("  l=%s" % [str(x) for x in l])
            print("  (ii) π(LA)=λ·π(L) ？%s" % (pLA == lam_pL))
            print("       π(L)=%s   π(LA)=%s" %
                  ([[str(x) for x in q] for q in pL], [[str(x) for x in q] for q in pLA]))

            # (iii) ΛH = λH ？
            # 补一行 ∈ row[C;CA] 使 (A) 成立、q0=2
            for extra in [row[:] for row in R if any(x != 0 for x in row)]:
                L2 = [l, extra]
                if not checkA(A, C, L2):
                    continue
                H = mm2(L2, B)
                if not (rk2(H) < 2):
                    continue
                sols = solve_Lambda(A, C, L2)
                Ft = mm2(mm2(L2, A), B)
                for Lam in sols:
                    if mm2(Lam, H) != Ft:
                        continue
                    lamH = [[lam * x for x in row] for row in H]
                    ok = (mm2(Lam, H) == lamH)
                    print("  (iii) ΛH = λH ？%s   H=%s" %
                          (ok, [[str(x) for x in q] for q in H]))
                    if ok:
                        print("        ⟹ im H ⊆ ker(λI-Λ) ⟹ **(S) 失败** ✓")
                        found = True
                    else:
                        # 检查更弱的形式：im H ∩ ker(λI-Λ) ≠ {0}
                        kerM = nullspace([[Lam[i][j] - (lam if i == j else 0)
                                           for j in range(2)] for i in range(2)])
                        inter = False
                        for w in kerM:
                            if any(x != 0 for x in w):
                                col = [[w[i]] for i in range(2)]
                                if rk2([H[i] + col[i] for i in range(2)]) == rk2(H):
                                    inter = True
                        print("        更弱形式 im H ∩ ker(λI-Λ) ≠ {0} ？%s" % inter)
                    break
                break
            break
        if found:
            break
    print("\n=== 结论 ===")
    print("机制链条 π(LA)=λπ(L) 直接成立？%s" % found)


if __name__ == "__main__":
    main()
