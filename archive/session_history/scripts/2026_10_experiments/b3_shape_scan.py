# -*- coding: utf-8 -*-
"""
b3_shape_scan.py —— 任务 B3：把 dim Ω* = 0（孤立点）的验证**扩到更多形状**

目标形状（支 B: 2p+q0 < n）：
  (k, s) = (1,3), (1,4), (2,3), (2,4), (1,5) 等
记录每个形状上："Ω* 非空的实例数" 与 "切空间维数取值"。
"""
import os, io, contextlib, random, itertools
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


def mats(t, r, k, s, dC, AT, BAT):
    W = WJ(t, r, k, s, dC); WB = W + BAT
    return WB + mm(W, AT), WB


def ok_A(t, r, k, s, dC, AT, BAT):
    MB, WB = mats(t, r, k, s, dC, AT, BAT)
    return rk(MB) == rk(WB)


def det_of(M):
    n = len(M)
    if n == 0: return F(1)
    A = [row[:] for row in M]; d = F(1)
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0: piv = i; break
        if piv is None: return F(0)
        if piv != c: A[c], A[piv] = A[piv], A[c]; d = -d
        d *= A[c][c]; inv = F(1)/A[c][c]
        for i in range(c+1, n):
            f = A[i][c]*inv
            if f: A[i] = [A[i][j]-f*A[c][j] for j in range(n)]
    return d


def tangent_dim(base, m, r, k, s, dC, AT, BAT):
    MB, WB = mats(base, r, k, s, dC, AT, BAT)
    rho = rk(WB); nr, nc = len(MB), len(MB[0])
    h = F(1, 500); rows = []
    for ri in itertools.combinations(range(nr), rho+1):
        for cj in itertools.combinations(range(nc), rho+1):
            def val(t):
                M2, _ = mats(t, r, k, s, dC, AT, BAT)
                return det_of([[M2[i][j] for j in cj] for i in ri])
            grad = [(val([base[a]+h if a==b else base[a] for a in range(m)])
                     - val([base[a]-h if a==b else base[a] for a in range(m)]))/(2*h)
                    for b in range(m)]
            if any(g != 0 for g in grad): rows.append(grad)
    return (m - rk(rows)) if rows else 0 if rho == nr else m


def main():
    print("=== B3：多形状扫描 dim Ω* ===\n")
    rng = random.Random(20260205)
    shapes = [(1,3),(1,4),(2,3),(2,4),(1,5)]
    summary = {}
    for (kk, ss) in shapes:
        found = 0; dims = []; tried = 0
        for trial in range(60000):
            n, p, r = 7, 1, 1
            for _ in range(20):
                Ac = Q.mat([[rng.randint(-1,1) for _ in range(n)] for _ in range(n)])
                Cc = Q.mat([[rng.randint(-1,1) for _ in range(n)] for _ in range(p)])
                Lc = Q.mat([[rng.randint(-1,1) for _ in range(n)] for _ in range(r)])
                if Q.rank(Cc)!=p or Q.rank(Lc)!=r or Q.rank(Lc+Cc)!=r+p: continue
                try: Lx, eta = p1(Ac, Cc, Lc)
                except Exception: continue
                if not Lx: continue
                q0 = sum(eta); k = q0 - r
                if k != kk: continue
                bt = build_norm_T(Ac, Cc, Lc, Lx)
                if bt is None: continue
                dC, s, k2, r2, AT, BAT = bt
                if (r2,k2)!=(r,kk) or s != ss: continue
                if 2*p+q0 >= n: continue
                tried += 1
                m = k*(s-k)
                # 小网格找 (A)-点
                base = None
                rngg = [F(x) for x in (-2,-1,0,1,2)]
                for combo in itertools.product(rngg, repeat=m):
                    if ok_A(list(combo), r,k,s,dC, AT, BAT):
                        base = list(combo); break
                if base is None: continue
                dT = tangent_dim(base, m, r, k, s, dC, AT, BAT)
                dims.append(dT); found += 1
                break
            if found >= 4: break
        summary[(kk,ss)] = (tried, found, dims)
        print("形状 (k=%d, s=%d, m=%d)：考察 %d 个支B实例，找到 Ω* 非空者 %d 个；dimT 取值 = %s"
              % (kk, ss, kk*(ss-kk), tried, found, dims))
    print("\n【汇总】")
    allz = all(d == 0 for (_,_,ds) in summary.values() for d in ds)
    tot = sum(len(ds) for (_,_,ds) in summary.values())
    print("  共测 %d 个 Ω* 非空的支 B 实例" % tot)
    print("  切空间维数全为 0？", allz)
    if allz and tot:
        print("  ⟹ 支持「支 B 的 Ω* 是孤立点（有限集）」✓（样本仍有限，非证明）")
    elif tot:
        print("  ⟹ **出现正维数** ⟹ FINAL §8 需修正 ✗")


if __name__ == "__main__":
    main()
