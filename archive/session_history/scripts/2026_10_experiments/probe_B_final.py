# -*- coding: utf-8 -*-
"""
probe_B_final.py —— 打印一个 Ω* 非空的支 B 实例，并判定 Ω* 的维数

只用最小规模、最快路径：一旦找到就打印矩阵并做维数判定，然后退出。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]
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

def cA(W, AT, BAT):
    WB = W + BAT
    return rk(WB + mm(W, AT)) == rk(WB)

rng = random.Random(20260202)
for trial in range(3000):
    n, p, r = 5, 1, 1
    for _ in range(30):
        Ac = Q.mat([[rng.randint(-1,1) for _ in range(n)] for _ in range(n)])
        Cc = Q.mat([[rng.randint(-1,1) for _ in range(n)] for _ in range(p)])
        Lc = Q.mat([[rng.randint(-1,1) for _ in range(n)] for _ in range(r)])
        if Q.rank(Cc)!=p or Q.rank(Lc)!=r or Q.rank(Lc+Cc)!=r+p: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k != 1: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2,k2)!=(r,k) or s<=k: continue
        if 2*p+q0 >= n: continue
        m = k*(s-k)
        hit_pts = [[F(a),F(b)] for a in range(-2,3) for b in range(-2,3)
                   if cA(WJ([F(a),F(b)], r,k,s,dC), AT, BAT)]
        if not hit_pts: continue
        print("### 支 B 实例 (n=%d p=%d r=%d q0=%d k=%d s=%d, 2p+q0=%d<n=%d, Θ 维数=%d)"
              % (n,p,r,q0,k,s,2*p+q0,n,m))
        print("A =", [[str(x) for x in row] for row in Ac])
        print("C =", [[str(x) for x in row] for row in Cc])
        print("L =", [[str(x) for x in row] for row in Lc])
        print("\n网格上的 (A)-点数 = %d / 25   ⟹ Ω* 在网格上已稠密命中" % len(hit_pts))
        print("(A)-点分布 =", [[str(x) for x in q] for q in hit_pts])
        base = hit_pts[0]
        # 小扰动命中率
        H = sum(1 for _ in range(400)
                if cA(WJ([base[0]+F(rng.randint(-1,1),32), base[1]+F(rng.randint(-1,1),32)],
                         r,k,s,dC), AT, BAT))
        print("\nΘ₀=%s 附近小扰动 400 个（步长 1/32）命中 %d ⟹ 命中率 %.3f"
              % ([str(x) for x in base], H, H/400))
        for a in range(2):
            lh = sum(1 for v in range(-6,7)
                     if cA(WJ([base[0]+(F(v,4) if a==0 else F(0)),
                               base[1]+(F(v,4) if a==1 else F(0))], r,k,s,dC), AT, BAT))
            print("   沿 Θ[%d] 直线（13 点，步长 1/4）命中 %d/13" % (a, lh))
        print("\n【判读】")
        print("  网格 25 点中有 %d 个命中、附近命中率 %.2f" % (len(hit_pts), H/400))
        print("  · 若命中率 ≫ 0 且直线大多命中 ⟹ Ω* **含开集**（正维数）")
        print("  · 若仅个别孤立点命中       ⟹ Ω* 是**有限孤立点**（与 FINAL 一致）")
        raise SystemExit
print("未找到 Ω* 非空的支 B 实例")
