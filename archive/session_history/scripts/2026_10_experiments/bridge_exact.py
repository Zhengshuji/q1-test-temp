# -*- coding: utf-8 -*-
"""
bridge_exact.py -- 精确判定 (A) 与分解的等价性

【理论】
  (A)  : row(LA) ⊆ row[L, C, CA]
  分解 : ∃ Λ, G0, G1 : LA = ΛL + G0 C + G1 CA

  (A) ⟹ 存在 U (q0×q0), S, T 使 LA = U L + S C + T CA（这只是 (A) 的展开）
  ⟹ 取 Λ := U, G0 := S, G1 := T **就得到分解** ✓

  ⚠️ 但要注意：(A) 保证 LA 的行在 row[L,C,CA] 中，即对**每一行**分别展开 ⟹
     LA = U L + S C + T CA 确实成立（逐行）✓ ⟹ **分解等价于 (A)** ✓

【本脚本】用精确求解验证：对反例，解 LA = U L + S C + T CA。
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


def condA(L, A, W):
    return rk(mm(L, A) + L + W) == rk(L + W)


def try_decomp(Lc, Ac, Cc, CAc, q0, r, g, verbose=False):
    """解 LA = U L + S C + T CA（逐行解线性方程组）

    未知量：U (q0×q0), S (q0×g), T (q0×g) —— 逐行解
    """
    LA = mm(Lc, Ac)
    n = len(Lc[0])
    # 行空间的行堆叠 [L; C; CA]
    Rstack = [row[:] for row in Lc] + [row[:] for row in Cc] + [row[:] for row in CAc]
    # 对 LA 的每一行，解 [L;C;CA]^T · x = (LA 的第 i 行)^T
    # 即：解 (Rstack)^T · x = (LA row i)^T
    RstackT = [[Rstack[j][k] for j in range(len(Rstack))] for k in range(n)]
    for i in range(len(LA)):
        b = [[LA[i][k]] for k in range(n)]
        res = solve_exact(RstackT, b)
        if res is None:
            return False, None
        y = res[0] if isinstance(res, tuple) else res
        # 残差校验
        for k in range(n):
            if sum(RstackT[k][j] * y[j] for j in range(len(RstackT[0]))) != b[k][0]:
                return False, None
    return True, None


def main():
    print("=== 精确判定：(A) ⟺ 分解 ? ===\n")
    # 用手算的反例
    A = [[F(-1), F(0), F(-1), F(-1), F(-1), F(0)],
         [F(0), F(1), F(0), F(1), F(0), F(1)],
         [F(1), F(-1), F(-1), F(-1), F(1), F(-1)],
         [F(0), F(1), F(1), F(-1), F(0), F(-1)],
         [F(0), F(1), F(1), F(0), F(1), F(0)],
         [F(-1), F(0), F(1), F(-1), F(-1), F(0)]]
    C = [[F(-1), F(0), F(0), F(-1), F(-1), F(-1)],
         [F(1), F(1), F(-1), F(0), F(0), F(0)]]
    L = [[F(-2), F(1), F(-1), F(2), F(1), F(0)],
         [F(-1), F(0), F(0), F(-1), F(-1), F(-2)]]
    W = C + mm(C, A)
    print("(A) 成立？", condA(L, A, W))
    print("rk(L) =", rk(L), " rk([L;LA]) =", rk(L + mm(L, A)))
    print("⟹ ker(L) ⊆ ker(LA)？", rk(L + mm(L, A)) == rk(L))
    print()
    ok, _ = try_decomp(L, A, C, mm(C, A), len(L), 2, 2)
    print("分解 LA = U L + S C + T CA 可解？", ok)
    print()
    print("【判读】")
    print("  · 分解可解 ⟹ (A) ⟹ 分解成立 ✓（G0,G1 弥补了 ker 缺口）")
    print("  · 分解不可解 ⟹ (A) 严格弱于分解 ✗（桥接无效）")
    print()
    print("=== 随机批量 ===")
    rng = random.Random(112233)
    tot = aok = dok = 0
    for trial in range(300000):
        if tot >= 12: break
        n, p = 6, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        q0 = 2
        Lc = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q0)]
        if rk(Lc) != q0: continue
        if not condA(Lc, Ac, W): continue
        CAc = mm(Cc, Ac)
        d, _ = try_decomp(Lc, Ac, Cc, CAc, q0, 1, 1)
        tot += 1
        aok += 1
        dok += 1 if d else 0
        print("trial=%-7d (A)=True  分解可解？ %s" % (trial, "✓" if d else "**✗**"))
    print()
    print("⟹ (A) 成立的 %d 个实例中，分解可解 %d 个" % (aok, dok))


if __name__ == "__main__":
    main()
