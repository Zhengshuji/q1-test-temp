# -*- coding: utf-8 -*-
"""
bridge_dual_exact.py -- 精确判定**对偶侧**的分解是否存在

【对偶侧的分解形式】
  (LA)* = L* ∘ Λ + C* ∘ G0 + (CA)* ∘ G1
  其中 (LA)* : W* → V*,  L* : W* → V*,  C* : G* → V*,  (CA)* : G* → V*
  ⟹ Λ : W* → W*  ✓；G0, G1 : W* → G*  （让 C* ∘ G0 有定义 ✓）

【矩阵形式（取 V=K^n, W=K^r, G=K^p）】
  (LA)* 的行空间条件 ⟺ ...

  实际检验：把 (LA)*, L*, C*, (CA)* 都写成矩阵，解
      (LA)* = L* · U + C* · S + (CA)* · T
  未知 U (r×r), S (r×p), T (r×p)   —— 注意 S,T 的"行数"=r（因 G0: W*→G* 即 r×p）
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

_lx = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _lx)
solve_exact = _lx["solve_exact"]


def T(mat):
    if not mat: return mat
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]


def condA(L, A, W):
    return rk(mm(L, A) + L + W) == rk(L + W)


def solve_rows(LHS_rows, RHS_rows, ncols):
    """解 RHS_rows = X · LHS_rows（X 为任意行数）—— 逐列解

    这里改用行空间判据：RHS 的每行是否在 LHS 的行空间中
    """
    for r in RHS_rows:
        # 解 LHS^T y = r^T
        LHST = T(LHS_rows)
        b = [[r[k]] for k in range(len(r))]
        res = solve_exact(LHST, b)
        if res is None: return False
        y = res[0] if isinstance(res, tuple) else res
        for k in range(len(r)):
            if sum(LHST[k][j] * y[j] for j in range(len(LHST[0]))) != b[k][0]:
                return False
    return True


def main():
    print("=== 对偶侧分解的精确判定 ===\n")
    print("形式：(LA)* = L*·U + C*·S + (CA)*·T")
    print("      （等价于：row((LA)*) ⊆ row[L*, C*, (CA)*]）\n")
    print("%-8s %8s %10s %10s" % ("trial", "(A)", "对偶行包含?", "结论"))
    print("-" * 44)
    rng = random.Random(777111)
    tot = ok = 0
    for trial in range(300000):
        if tot >= 12: break
        n, p, r = 6, 1, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        q0 = 2
        Lc = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q0)]
        if rk(Lc) != q0: continue
        if not condA(Lc, Ac, W): continue
        CAc = mm(Cc, Ac)
        LAc = mm(Lc, Ac)
        # 行堆叠 [L; C; CA]，看 LA 的行是否在其中
        Rstack = [row[:] for row in Lc] + [row[:] for row in Cc] + [row[:] for row in CAc]
        good = solve_rows(Rstack, LAc, n)
        tot += 1
        ok += 1 if good else 0
        print("%-8d %8s %10s %10s"
              % (trial, "True", "✓" if good else "✗", "分解存在" if good else "**不存在**"))
    print()
    print("⟹ row(LA) ⊆ row[L,C,CA] ⟹ 分解存在：%d/%d" % (ok, tot))
    print()
    print("【重要】上面的检验就是 (A) 本身 ⟹ 分解只要 (A) ✓")


if __name__ == "__main__":
    main()
