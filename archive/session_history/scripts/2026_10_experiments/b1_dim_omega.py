# -*- coding: utf-8 -*-
"""
b1_dim_omega.py —— 任务 B1：确定 dim Ω*（在已知 (A)-点处的切空间维数）

【判据】
  Ω* 在 Θ₀ 处的 **Zariski 切空间** = ⋂_Δ ker(∇Δ(Θ₀))，其中 Δ 跑遍定义 Ω* 的
  那些"秩降"子式（Δ = rk[W;B] 阶子式的全体）。

  (A): rank[W(Θ); B; W(Θ)Ā] == rank[W(Θ); B]
      令 ρ = rk[W(Θ₀);B]。条件等价于「[W;B;WĀ] 的全部 (ρ+1)×(ρ+1) 子式 = 0」。

  ⟹ 取这些子式在 Θ₀ 处的**梯度**组成的矩阵，其秩 r ⟹ dim T_{Θ₀}Ω* = m − r。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; rref = _ns["rref"]

import linalg_q as Q

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
build_norm_T = _t["build_norm_T"]; p1 = _t["p1"]


def WJ(t, r, k, s, dC):
    W = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [F(0)] * dC; row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def stacked(t, r, k, s, dC, AT, BAT):
    """[W;B;WĀ]（用于 (A)）与 [W;B]"""
    W = WJ(t, r, k, s, dC)
    WB = W + BAT
    return WB + mm(W, AT), WB


def is_A(t, r, k, s, dC, AT, BAT):
    MB, WB = stacked(t, r, k, s, dC, AT, BAT)
    return rk(MB) == rk(WB)


def det_of(M):
    n = len(M)
    if n == 0: return F(1)
    A = [row[:] for row in M]
    d = F(1)
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0: piv = i; break
        if piv is None: return F(0)
        if piv != c: A[c], A[piv] = A[piv], A[c]; d = -d
        d *= A[c][c]
        inv = F(1) / A[c][c]
        for i in range(c + 1, n):
            f = A[i][c] * inv
            if f: A[i] = [A[i][j] - f * A[c][j] for j in range(n)]
    return d


def minors_at(t, r, k, s, dC, AT, BAT, rho):
    """返回全部 (rho+1)x(rho+1) 子式的值（作为 Θ 的函数，在 t 处取值）"""
    import itertools
    MB, WB = stacked(t, r, k, s, dC, AT, BAT)
    nr, nc = len(MB), len(MB[0])
    out = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            out.append((ri, cj))
    return out


def main():
    print("=== B1：dim Ω* （切空间维数）===\n")
    rng = random.Random(20260203)
    for trial in range(3000):
        n, p, r = 5, 1, 1
        for _ in range(30):
            Ac = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(n)])
            Cc = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(p)])
            Lc = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(r)])
            if Q.rank(Cc) != p or Q.rank(Lc) != r or Q.rank(Lc + Cc) != r + p: continue
            try: Lx, eta = p1(Ac, Cc, Lc)
            except Exception: continue
            if not Lx: continue
            q0 = sum(eta); k = q0 - r
            if k != 1: continue
            bt = build_norm_T(Ac, Cc, Lc, Lx)
            if bt is None: continue
            dC, s, k2, r2, AT, BAT = bt
            if (r2, k2) != (r, k) or s <= k: continue
            if 2 * p + q0 >= n: continue
            m = k * (s - k)
            # 找 (A)-点
            base = None
            for a in range(-2, 3):
                for b in range(-2, 3):
                    if is_A([F(a), F(b)], r, k, s, dC, AT, BAT):
                        base = [F(a), F(b)]; break
                if base: break
            if base is None: continue
            rho = rk(stacked(base, r, k, s, dC, AT, BAT)[1])
            print("实例 n=%d p=%d r=%d q0=%d k=%d s=%d  (支B)  Θ 维数 m=%d" %
                  (n, p, r, q0, k, s, m))
            print("  (A)-点 Θ₀ = %s ；  ρ = rk[W;B] = %d" % ([str(x) for x in base], rho))
            # 数值梯度：对每个 (rho+1)-子式，用中心差分求偏导
            h = F(1, 1000)
            idxs = minors_at(base, r, k, s, dC, AT, BAT, rho)
            rows = []
            for (ri, cj) in idxs:
                def val(t):
                    MB, _ = stacked(t, r, k, s, dC, AT, BAT)
                    return det_of([[MB[i][j] for j in cj] for i in ri])
                f0 = val(base)
                grad = []
                for a in range(m):
                    tp = list(base); tp[a] += h
                    tm = list(base); tm[a] -= h
                    grad.append((val(tp) - val(tm)) / (2 * h))
                if any(g != 0 for g in grad):
                    rows.append(grad)
            dimT = m - rk(rows) if rows else m
            print("  [切空间] 非零梯度的子式数 = %d ； dim T_{{Θ₀}}Ω* = %d" %
                  (len(rows), dimT))
            print("  ⟹ 猜想 dim Ω* = m − (约束数)。本例 m=%d, dimT=%d, 余维 = %d"
                  % (m, dimT, m - dimT))
            print()
            print("  对照：若 Ω* 是**有限孤立点**，应得 dimT = 0；")
            print("        若 Ω* 是**曲线**，应得 dimT = 1；依此类推。")
            return
    print("未找到 Ω* 非空的支 B 实例")


if __name__ == "__main__":
    main()
