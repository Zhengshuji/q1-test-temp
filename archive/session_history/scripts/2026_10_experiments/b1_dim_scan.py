# -*- coding: utf-8 -*-
"""
b1_dim_scan.py —— 任务 B1（**修正版**）：在**多个** Ω* 非空的支 B 实例上测 dim Ω*

⚠️ 上一版 probe_B_final.py 的"9.2% 命中"是 bug：扰动 randint(-1,1)/32 在取 (0,0) 时
   **没有扰动**，命中的全是 Θ₀ 本身。本脚本**强制非零扰动**。

判据（三重交叉）：
  ① **切空间**：定义 Ω* 的子式梯度矩阵的秩 r ⟹ dim T = m − r；
  ② **精细网格**：Ω* 在 Θ₀ 附近网格上是否只有 Θ₀；
  ③ **非零随机扰动**：步长 1/1024 的 2000 次非零扰动命中数。
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
    rho = rk(WB)
    nr, nc = len(MB), len(MB[0])
    h = F(1, 1000); rows = []
    for ri in itertools.combinations(range(nr), rho+1):
        for cj in itertools.combinations(range(nc), rho+1):
            def val(t):
                M2, _ = mats(t, r, k, s, dC, AT, BAT)
                return det_of([[M2[i][j] for j in cj] for i in ri])
            grad = []
            for a in range(m):
                tp = list(base); tp[a] += h
                tm = list(base); tm[a] -= h
                grad.append((val(tp)-val(tm))/(2*h))
            if any(g != 0 for g in grad):
                rows.append(grad)
    return (m - rk(rows)) if rows else m


def main():
    print("=== B1（修正版）：多个支 B 实例上的 dim Ω* ===\n")
    rng = random.Random(20260204)
    results = []
    checked = 0
    for trial in range(4000):
        n, p, r = 5, 1, 1
        for _ in range(25):
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
            # 网格找 (A)-点（非零优先）
            base = None
            for a in range(-2,3):
                for b in range(-2,3):
                    if a==0 and b==0: continue
                    if ok_A([F(a),F(b)], r,k,s,dC, AT, BAT):
                        base = [F(a),F(b)]; break
                if base: break
            if base is None:
                if ok_A([F(0),F(0)], r,k,s,dC, AT, BAT):
                    base = [F(0),F(0)]
                else:
                    continue
            checked += 1
            # ① 切空间
            dT = tangent_dim(base, m, r, k, s, dC, AT, BAT)
            # ② 精细网格（若 m==2）
            grid_hits = 1
            if m == 2:
                grid_hits = sum(1 for a in range(-4,5) for b in range(-4,5)
                                if ok_A([base[0]+F(a,16), base[1]+F(b,16)],
                                        r,k,s,dC, AT, BAT))
            # ③ 非零扰动
            nz = 0; nzh = 0
            for _ in range(2000):
                d = [F(rng.randint(-1,1),1024) for _ in range(m)]
                if all(x == 0 for x in d): continue
                nz += 1
                if ok_A([base[i]+d[i] for i in range(m)], r,k,s,dC, AT, BAT):
                    nzh += 1
            results.append((n,p,r,q0,k,s,m,base,dT,grid_hits,nz,nzh))
            print("[%2d] n=%d p=%d r=%d q0=%d k=%d s=%d | m=%d Θ₀=%s | dimT=%d | 网格命中=%d | 非零扰动命中=%d/%d"
                  % (checked, n,p,r,q0,k,s,m, [str(x) for x in base], dT, grid_hits, nzh, nz))
            if checked >= 6: break
        if checked >= 6: break
    print()
    print("【汇总】共 %d 个 Ω* 非空的支 B 实例" % checked)
    if results:
        dts = [x[8] for x in results]
        print("  切空间维数 dimT 的取值：", dts)
        print("  ⟹ 若全为 0 ⟹ Ω* 在这些实例上是**孤立点**（支持 FINAL §8）")
        print("  ⟹ 若有 >0 ⟹ Ω* **正维数**（FINAL §8 需修正）")


if __name__ == "__main__":
    main()
