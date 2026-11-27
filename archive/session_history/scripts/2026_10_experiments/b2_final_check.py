# -*- coding: utf-8 -*-
"""
b2_final_check.py —— 决定性核验：该实例的 (A)-解集到底是单点还是直线？

对同一实例：
  ① 直接数值检验 (A) 在 Θ=(0, t1, 0)（t1 ≠ 0）处是否成立
  ② 整数格扫描
  ③ Groebner 基
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as Fr
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]
_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]


def WJ_of(t, r, k, s, dC):
    W = [[Fr(1) if j == i else Fr(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [Fr(0)] * dC; row[r + i] = Fr(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def get_instance(n, want_s, seed, tries=200000):
    rng = random.Random(seed)
    for _ in range(tries):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - 1
        if k != 1: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (1, 1) or s != want_s: continue
        if 2 + q0 >= n: continue
        return dict(dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def main():
    print("=== 决定性核验：解集是单点还是直线？ ===")
    for t in range(10):
        inst = get_instance(6, 4, 20320000 + 400 + t)
        if inst is None: continue
        dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
        r, k = 1, 1; m = s - 1
        # ① 直接数值检验 (A) 在 Θ=(0, a, 0) 处
        print("\n--- 实例 #%d : dC=%d s=%d m=%d ---" % (t, dC, s, m))
        print("  在 Θ=(0, a, 0) 处直接检验 (A)（用秩降定义）：")
        for a in [Fr(0), Fr(1), Fr(-1), Fr(1, 2), Fr(3), Fr(-7, 3)]:
            W = WJ_of([Fr(0), a, Fr(0)], r, k, s, dC)
            WB = W + BAT
            ok = (rk(WB + mm(W, AT)) == rk(WB))
            print("     a=%8s : (A) = %s   rk[W;B]=%d  rk[W;B;WĀ]=%d"
                  % (str(a), ok, rk(WB), rk(WB + mm(W, AT))))
        # ② 整数格扫描
        cnt = 0; pts = []
        for combo in itertools.product(range(-3, 4), repeat=m):
            W = WJ_of([Fr(x) for x in combo], r, k, s, dC); WB = W + BAT
            if rk(WB + mm(W, AT)) == rk(WB):
                cnt += 1; pts.append(combo)
        print("  整数格 (±3)^%d : 命中 %d 个 %s" % (m, cnt, pts[:8]))
        # ③ 更细的有理格：a 取分母 2,3,4...
        hits = []
        for a in [Fr(p, q) for q in (1, 2, 3, 4, 5) for p in range(-8, 9)]:
            W = WJ_of([Fr(0), a, Fr(0)], r, k, s, dC); WB = W + BAT
            if rk(WB + mm(W, AT)) == rk(WB):
                hits.append(a)
        print("  直线 (0,a,0) 上的有理点（分母≤5, |p|≤8）：命中 a = %s"
              % [str(x) for x in hits[:12]])
        if hits:
            print("  ⟹ ⟹ **解集含正维数直线** ⟹ Ω*_J **不是单点** ✗（我之前的结论错！）")
        else:
            print("  ⟹ 直线 (0,a,0) 上只有 a=0 ⟹ 支持单点 ✓")
        return


if __name__ == "__main__":
    main()
