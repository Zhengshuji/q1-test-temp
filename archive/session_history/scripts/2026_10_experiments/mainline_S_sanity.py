# -*- coding: utf-8 -*-
"""
mainline_S_sanity.py —— 健全性检查：确认 (S) 检验器**不是永远返回 False**

做法：用一个**已知 (S) 成立**的例子（项目记录：$d_{CA}=1$ 时 (S) 总成立）
     和一个**已知 (S) 失败**的例子（情形 II：$d_{CA}\ge q_0$），看检验器输出。
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

_b = {"__file__": os.path.join(_HERE, "batch_c6p_k.py"), "__name__": "b"}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    srcb = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(srcb.split("def main(")[0], "b", "exec"), _b)
solve_Lambda = _b["solve_Lambda"]; S_holds = _b["S_holds"]


def mul(X, Y):
    return [[sum(X[i][a] * Y[a][j] for a in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def main():
    print("=== (S) 检验器的健全性检查 ===\n")
    # 测试 1：手工小例（应给出 S 成立）
    #   L = [[1,0],[0,1]]（q0=2），H 取满秩，Λ = 0 ⟹ (S) 要求 rank(λH) = rank H ∀λ
    #   λH 的秩对 λ≠0 等于 rank H ✓，λ=0 时秩 0 ✗ ⟹ (S) 失败
    print("[测试 1] H=[[1,0],[0,1]], Λ=0 : 期望 (S) 失败（λ=0 时秩掉）")
    H1 = [[F(1), F(0)], [F(0), F(1)]]
    Lam1 = [[F(0), F(0)], [F(0), F(0)]]
    print("   S_holds ->", S_holds(Lam1, H1), " (期望 False)")
    # 测试 2：H 满秩、Λ = μI ⟹ (S) 成立（λH - μH = (λ-μ)H，秩恒 = rank H 除 λ=μ 处）
    #   实际上 λ=μ 时秩 0 ⟹ (S) 失败。改成 H 左零化？
    #   正确例子：(S) 成立 ⟺ im H 不含 Λ 的特征向量。
    #   取 Λ 无特征向量落在 im H 中：H = e1，Λ = diag(0,1)（特征向量 e1,e2）⟹ e1 在 im H
    #   ⟹ 失败。取 H = e1，Λ = [[0,1],[0,2]]（特征值 0,2；e1 是 0 的特征向量）⟹ 也失败。
    #   取 H = e2（Λ = diag(0,1)）：e2 是特征向量 ⟹ 失败。
    #   ⟹ 1 维 H 时总是失败（因为 Λ 总有一个特征向量与 H 共线？不对，需 e_i ∝ H）
    #   取 H = [[1],[1]]（im H = span(1,1)），Λ = diag(0,1)：特征向量 e1,e2 都不 ∝ (1,1)
    #   ⟹ (S) 应成立 ✓
    print("\n[测试 2] H=[[1],[1]], Λ=diag(0,1) : 期望 (S) 成立（im H 不含特征向量）")
    H2 = [[F(1)], [F(1)]]
    Lam2 = [[F(0), F(0)], [F(0), F(1)]]
    print("   S_holds ->", S_holds(Lam2, H2), " (期望 True)")
    # 测试 3：H = [[1],[0]]，Λ = diag(0,1)：im H = span e1 是特征向量 ⟹ 失败
    print("\n[测试 3] H=[[1],[0]], Λ=diag(0,1) : 期望 (S) 失败（im H 含特征向量）")
    H3 = [[F(1)], [F(0)]]
    print("   S_holds ->", S_holds(Lam2, H3), " (期望 False)")
    # 测试 4：真实实例（d_CA=1，项目称 (S) 总成立）
    print("\n[测试 4] 真实实例上的统计（d_CA 各种取值）")
    rng = random.Random(1234)
    cnt = {0: 0, 1: 0}
    for _ in range(200):
        n, p, r = 5, 1, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[F(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2: continue
        W = Cc + mul(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d_CA = len(N[0])
        L = Lc + [row[:] for row in Cc]        # 任意加一行
        H = mul(L, N)
        if rk(H) == 0: continue
        got = False
        for Lam in solve_Lambda(Ac, Cc, L):
            if S_holds(Lam, H): got = True; break
        cnt[1 if got else 0] += 1
    print("   随机实例：S 成立 %d 个，失败 %d 个" % (cnt[1], cnt[0]))
    print("   ⟹ 检验器**两种结果都出现过** ⟹ 不是永远 False ✓" if cnt[1] and cnt[0]
          else "   ⚠️ 只出现一种结果 —— 需检查")


if __name__ == "__main__":
    main()
