# -*- coding: utf-8 -*-
"""
certify_solveLambda_bug.py —— 提取 `batch_c6p_k.solve_Lambda` 丢解的**最小证书**

【bug】
    s_lam = ([y] if any(x != 0 for x in y) else []) + nsol
  当库 `solve` 给出的**特解 y 恰为 0 向量**时，y 被丢弃 ⟹ 解集中**缺一个解** ✗

【为什么影响结论】
  (A) 的分解 LA = ΛL + G₀C + G₁CA 的解空间是**仿射**的；丢掉特解 ⟹ 解集**不完整**。
  下游用 `for Lam in sols: if ΛH == F and S_holds(Lam,H)` 判 (S)，缺解可能
  把"(S) 成立" **误报为真** ✗（空集上全称命题为真）。

【证书内容】
  ① 一个具体实例：库给的 y 与独立求解器给的 y*（二者都应满足 ΛH = F）
  ② 二者在 (S) 判据下的结果是否不同
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]
lib_solve = _ns["solve"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rank_exact, solve_exact, matmul = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]

_ns3 = {"__file__": os.path.join(_HERE, "batch_c6p_k.py")}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    exec(compile(fh.read().split("def main()")[0], "helpers", "exec"), _ns3)
mat = _ns3["mat"]
solve_Lambda_lib = _ns3["solve_Lambda"]
S_holds_lib = _ns3["S_holds"]


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


def build_system(A, C, L):
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
    return rows, rhs, nunk


def main():
    print("=== `batch_c6p_k.solve_Lambda` 丢解的最小证书 ===\n")
    cases = [
        ("I-4x4", mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]), mat([[0,0,1,0]])),
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                   mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
    ]
    rng = random.Random(20261015)
    cert = None
    for tag, A, C in cases:
        n = len(A)
        B = ker_basis(stack(C, matmul(C, A)))
        for trial in range(20000):
            q0 = rng.choice([2, 3])
            L = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(q0)]
            if rk(L) != q0 or not condA(A, C, L):
                continue
            rows, rhs, nunk = build_system(A, C, L)
            lib = lib_solve(rows, rhs)
            ind = solve_exact(rows, rhs)
            if lib is None or ind is None:
                continue
            y_lib = lib[0]
            y_ind = ind[0]
            if any(x != 0 for x in y_lib):
                continue                     # 只找 y=0 的实例（bug 触发条件）
            if not any(x != 0 for x in y_ind):
                continue
            cert = (tag, A, C, L, B, q0, y_lib, y_ind, len(lib[1]), len(ind[1]))
            break
        if cert:
            break
    if not cert:
        print("未找到 y=0 的实例")
        return
    tag, A, C, L, B, q0, y_lib, y_ind, nb_lib, nb_ind = cert
    print("【实例】%s  n=%d p=%d q0=%d" % (tag, len(A), len(C), q0))
    print("  L =", [[str(x) for x in r] for r in L])
    print()
    print("【库 solve 给出的特解 y】 全零？%s" % (not any(x != 0 for x in y_lib)))
    print("   零空间基个数 = %d" % nb_lib)
    print("【独立求解器给出的特解 y*】全零？%s" % (not any(x != 0 for x in y_ind)))
    print("   零空间基个数 = %d" % nb_ind)
    print()
    H = matmul(L, B)
    Fm = matmul(matmul(L, A), B)
    print("  H = L·N_CA =", [[str(x) for x in r] for r in H], " rkH =", rk(H))
    print("  F = LA·N_CA =", [[str(x) for x in r] for r in Fm], " rkF =", rk(Fm))
    print()
    # 库的 Λ 列表
    libs = solve_Lambda_lib(A, C, L)
    print("  库 solve_Lambda 给出 %d 个 Λ" % len(libs))
    ok_lib = any(matmul(Lm, H) == Fm for Lm in libs)
    print("    其中满足 ΛH = F 的：%s" % ok_lib)
    # 独立的 Λ
    Lam_ind = [[y_ind[kk * q0 + i] for kk in range(q0)] for i in range(q0)]
    print("  独立求解器给的 Λ =", [[str(x) for x in r] for r in Lam_ind])
    print("    满足 ΛH = F ？%s" % (matmul(Lam_ind, H) == Fm))
    print("    独立版 (S)（逐 λ 判秩）是否成立：", end="")
    rH = rk(H)
    LAMS = [F(0), F(1), F(-1), F(2), F(1, 2)]
    sa = all(rk([[lam * H[i][j] - Fm[i][j] for j in range(len(H[0]))]
                 for i in range(len(H))]) == rH for lam in LAMS)
    print(sa)
    if ok_lib:
        for Lm in libs:
            if matmul(Lm, H) == Fm:
                print("    库版 S_holds(Λ_lib, H) =", S_holds_lib(Lm, H))
    print()
    print("【诊断】库丢掉特解 y=0 ⟹ 解集不完整 ⟹ 依赖它的 (A)-分解类结论不可信 ⚠️")
    print("        （注：项目主统计脚本 reliable_S_test.py 用的是 (H,F) 子式 gcd，**不受影响** ✓）")


if __name__ == "__main__":
    main()
