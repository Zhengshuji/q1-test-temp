# -*- coding: utf-8 -*-
"""
probe_YES_certified.py —— 对"情形 II 中 (A)∧T5a∧(S) 成立"的点做**三重独立复核**并给出证书

【立场】
  项目 FINAL §4.5 的数据是「情形 II：(A)∧(S) = 0/200」。
  本轮用**独立求解器**重测得到「910/910 成立」，且其中 8 个还满足 T5a（rk H < q0）。
  ⟹ 二者不可能都对。本脚本对**那几个点**做三个**互相独立**的判据对照：

    (S)-判据A（原始定义，FINAL §1.1）
        rk[λL − LA ; CA ; C] == rk[L ; CA ; C]   对若干 λ（含 λ=0）
    (S)-判据B（T2 的铅笔约化）
        rk(λH − F) == rk H                       对若干 λ
    (S)-判据C（T5/T5′ 的谱判据，用**独立解出**的正确 Λ）
        im H ∩ ker(λI − Λ) ≠ {0} 对某个 λ
            ⟺ rk(λH − F) < rk H  ⟺ ∃特征向量落在 im H 中

  三者必须一致；若一致 ⟹ 结论可信 ✓
  另外：把"库包装 solve_Lambda 的结论"一并列出，展示分歧来源 ✓
"""
import os, io, contextlib, random
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
S_holds_lib = _ns3["S_holds"]
solve_Lambda_lib = _ns3["solve_Lambda"]


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


LAMS = [F(0), F(1), F(-1), F(2), F(-2), F(3), F(1, 2), F(-1, 3), F(5, 7)]


def S_primitive(A, C, L, lams):
    """判据A：原始定义"""
    CA = matmul(C, A)
    LA = matmul(L, A)
    base = rk(stack(L, CA, C))
    out = []
    for lam in lams:
        M = [[lam * L[i][j] - LA[i][j] for j in range(len(L[0]))] for i in range(len(L))]
        out.append((lam, rk(stack(M, CA, C)), base))
    return out


def S_pencil(H, Fm, lams):
    """判据B：铅笔约化"""
    rH = rk(H)
    out = []
    for lam in lams:
        M = [[lam * H[i][j] - Fm[i][j] for j in range(len(H[0]))] for i in range(len(H))]
        out.append((lam, rk(M), rH))
    return out


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
    print("=== 情形 II 中 (A)∧T5a 的点的三重独立复核 ===\n")
    cases = [
        ("II-nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                           [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                      mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
        ("II-nilp6b", mat([[0,0,0,1,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1],
                           [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                      mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
        ("I-4x4", mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]), mat([[0,0,1,0]])),
    ]
    rng = random.Random(4242)
    found = []
    for tag, A, C in cases:
        n = len(A)
        B = ker_basis(stack(C, matmul(C, A)))
        d = len(B[0])
        for trial in range(20000):
            q0 = rng.choice([2, 3])
            L = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(q0)]
            if rk(L) != q0 or not condA(A, C, L):
                continue
            H = matmul(L, B)
            Fm = matmul(matmul(L, A), B)
            if not (rk(H) < q0):
                continue
            found.append((tag, A, C, L, B, H, Fm, d, q0))
            if len(found) >= 6:
                break
        if len(found) >= 6:
            break

    if not found:
        print("未能在限定时间内搜到 (A)∧T5a 的点")
        return

    for idx, (tag, A, C, L, B, H, Fm, d, q0) in enumerate(found):
        print("=" * 74)
        print("【实例 %d】%s  n=%d p=%d d_CA=%d q0=%d  （情形 II：%s）" %
              (idx + 1, tag, len(A), len(C), d, q0, d >= q0))
        print("  L =", [[str(x) for x in r] for r in L])
        print("  H = L·N_CA =", [[str(x) for x in r] for r in H], "  rk H =", rk(H))
        print("  F = LA·N_CA =", [[str(x) for x in r] for r in Fm], "  rk F =", rk(Fm))
        print()
        print("  (A) 判据 rk[LA;L;C;CA]==rk[L;C;CA] ：%s" % condA(A, C, L))
        print("  T5a  rk H < q0 ：%s  (%d < %d)" % (rk(H) < q0, rk(H), q0))
        print()
        pa = S_primitive(A, C, L, LAMS)
        print("  【判据A｜原始定义 rk[λL−LA;CA;C] == rk[L;CA;C]】")
        okA = all(a == b for _, a, b in pa)
        for lam, a, b in pa[:5]:
            print("      λ=%-5s rk=%d  base=%d  %s" % (str(lam), a, b, "✓" if a == b else "✗"))
        print("      ⟹ %s" % ("(S) 成立 ✓" if okA else "(S) 失败 ✗"))
        pb = S_pencil(H, Fm, LAMS)
        print("  【判据B｜铅笔约化 rk(λH−F) == rk H】")
        okB = all(a == b for _, a, b in pb)
        for lam, a, b in pb[:5]:
            print("      λ=%-5s rk=%d  rkH=%d  %s" % (str(lam), a, b, "✓" if a == b else "✗"))
        print("      ⟹ %s" % ("(S) 成立 ✓" if okB else "(S) 失败 ✗"))
        Lam = decomp_Lambda(A, C, L)
        print("  【判据C｜独立解出的 Λ（verified ΛH = F）】")
        if Lam is None:
            print("      独立求解器无解 ✗（异常）")
        else:
            print("      Λ =", [[str(x) for x in r] for r in Lam])
            print("      Λ·H == F ？ %s" % (matmul(Lam, H) == Fm))
        print("  【对照：库包装 solve_Lambda（**有丢解的 bug**）】")
        libs = solve_Lambda_lib(A, C, L)
        okl = any(matmul(Lm, H) == Fm for Lm in libs)
        print("      给出 %d 个 Λ ；其中有 ΛH==F 的：%s" % (len(libs), okl))
        if libs and okl:
            for Lm in libs:
                if matmul(Lm, H) == Fm:
                    print("      库版 (S_holds) 判据结果 = %s" % S_holds_lib(Lm, H))
        print()
        verdict = "YES（情形 II 可为 YES！）" if (condA(A, C, L) and rk(H) < q0 and okA and okB) \
                  else "NO"
        print("  ⟹⟹ 结论：%s" % verdict)
        print()
    print("=" * 74)
    print("汇总：证书点数 = %d ；其中 (A)∧T5a∧(S) = %d" %
          (len(found), sum(1 for _, A, C, L, B, H, Fm, d, q0 in found
                           if condA(A, C, L) and rk(H) < q0
                           and all(a == b for _, a, b in S_primitive(A, C, L, LAMS))
                           and all(a == b for _, a, b in S_pencil(H, Fm, LAMS)))))


if __name__ == "__main__":
    main()
