# -*- coding: utf-8 -*-
"""
b1_resolve.py —— 用**同一个实例**同时做"精细网格"与"±1/32 扰动"两种测试，
                  定位之前矛盾（孤立点 vs 9% 命中）的根源。
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

def A_ok(t, r, k, s, dC, AT, BAT):
    W = WJ(t, r, k, s, dC); WB = W + BAT
    return rk(WB + mm(W, AT)) == rk(WB)

def find_instance(seed):
    rng = random.Random(seed)
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
            if not A_ok([F(0),F(0)], r,k,s,dC, AT, BAT): continue
            return (n,p,r,q0,k,s,dC,AT,BAT)
    return None

def main():
    print("=== 定位矛盾：同一实例，两种测试 ===\n")
    inst = find_instance(20260203)
    if inst is None:
        print("未找到实例"); return
    n,p,r,q0,k,s,dC,AT,BAT = inst
    print("实例 n=%d p=%d r=%d q0=%d k=%d s=%d  Θ 维数 m=%d" % (n,p,r,q0,k,s,k*(s-k)))
    print("Θ₀=(0,0) 是 (A)-点：", A_ok([F(0),F(0)], r,k,s,dC, AT, BAT))
    print()
    # 测试 1：精细网格
    print("[测试1] 精细网格（步长 1/8，±1/2）：")
    h1 = []
    for ai in range(-4,5):
        for bi in range(-4,5):
            if A_ok([F(ai,8),F(bi,8)], r,k,s,dC, AT, BAT):
                h1.append((F(ai,8),F(bi,8)))
    print("   命中 %d：%s" % (len(h1), [[str(x) for x in q] for q in h1]))
    # 测试 2'：±1/32 扰动，**排除零扰动**（da=db=0）
    print("\n[测试2'] ±1/32 扰动，**排除 (0,0) 零扰动**：")
    rng2 = random.Random(999)
    h2 = []; nz = 0
    while len(h2) + nz < 400:
        da, db = F(rng2.randint(-1,1),32), F(rng2.randint(-1,1),32)
        if da == 0 and db == 0:
            nz += 1; continue
        if A_ok([da,db], r,k,s,dC, AT, BAT):
            h2.append((da,db))
        if len(h2) + nz >= 400: break
    print("   非零扰动命中 %d（零扰动出现 %d 次，已排除）" % (len(h2), nz))
    print("   命中点：", [[str(x) for x in q] for q in h2][:10])
    # 测试 4：非零扰动、更细步长
    print("\n[测试4] 非零扰动，步长 1/1024，1000 次：")
    rng4 = random.Random(4242); h4 = []
    for _ in range(1000):
        da, db = F(rng4.randint(-1,1),1024), F(rng4.randint(-1,1),1024)
        if da == 0 and db == 0: continue
        if A_ok([da,db], r,k,s,dC, AT, BAT): h4.append((da,db))
    print("   非零扰动命中 %d / 1000" % len(h4))
    print("\n【结论】")
    print("  若测试1 只有 (0,0) 而测试2/3 有多个命中 ⟹ 存在**实现不一致**（需查 on which side）")
    print("  若测试1、2、3 都只有 (0,0) ⟹ Ω* 是孤立点（probe_B_final 的 9% 是别的实例）")

if __name__ == "__main__":
    main()
