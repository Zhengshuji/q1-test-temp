# -*- coding: utf-8 -*-
"""
c6_k_ge1.py -- ⭐⭐⭐ 决定性问题：**非退化平行 + k≥1** 的实例上，(5a)∧(5b) 能否同时满足？

【构造（利用 d ∦ c）】
  取 A, C 使  CA²|_K ≠ 0（**非**不变）  且  CA³|_K = 0
  令 u := CA²N（1×d 向量），ℓ0 := CA²，r := CA
  L0 := [ℓ0 + r ; ℓ0]
      π(L0)   = [u ; u]          ⟹ 平行、非退化 ✓
      π(L0A)  = [CA³N + CA²N ; CA³N] = [0 + u ; 0] = [u ; 0]  ⟹ 仍成比例 ✓
      c = (1,1), d = (1,0)  ⟹ d ∦ c  ⟹ **L0 本身不满足 (A)** ⟹ k ≥ 1 ✓

【判定】对 q0 = r + k 行的 L，测 (5a) ∧ (5b)（**直接测 (5b)**）
"""
import os, io, contextlib, random, itertools
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

# ---- 多项式 ----
def pt(p):
    while len(p) > 1 and p[-1] == 0: p = p[:-1]
    return p
def padd(a,b):
    n=max(len(a),len(b)); return pt([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n)])
def psub(a,b):
    n=max(len(a),len(b)); return pt([(a[i] if i<len(a) else F(0))-(b[i] if i<len(b) else F(0)) for i in range(n)])
def pmul(a,b):
    if a==[F(0)] or b==[F(0)]: return [F(0)]
    r=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return pt(r)
def pdivmod(a,b):
    a=a[:]; b=pt(b[:])
    if b==[F(0)]: return None
    db=len(b)-1; q=[F(0)]*max(1,len(a)-db)
    while len(a)-1>=db and not (len(a)==1 and a[0]==0):
        d=len(a)-1-db; co=a[-1]/b[-1]; q[d]+=co
        for i in range(len(b)): a[d+i]-=co*b[i]
        a=pt(a)
    return pt(q),a
def pgcd(a,b):
    a=pt(a[:]); b=pt(b[:])
    while not (len(b)==1 and b[0]==0):
        r=pdivmod(a,b)
        if r is None: break
        a,b=b,r[1]
    if len(a)>1 and a[-1]!=0:
        lc=a[-1]; a=[x/lc for x in a]
    return a
def pdet(M,k):
    if k==1: return M[0][0][:]
    tot=[F(0)]
    for j in range(k):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        d=pdet(sub,k-1); pr=pmul(M[0][j],d)
        tot=padd(tot,pr) if j%2==0 else psub(tot,pr)
    return pt(tot)


def check_5ab(Lm, Ac, Cc):
    """返回 ((5a)成立?, (5b)成立?)"""
    CAc = mm(Cc, Ac)
    LA = mm(Lm, Ac)
    base = [r[:] for r in Lm] + [r[:] for r in CAc] + [r[:] for r in Cc]
    r0 = rk(base)
    m = len(base); n = len(base[0])
    # (5a)
    r5a = rk([r[:] for r in LA] + base)
    a_ok = (r5a == r0)
    if r0 == 0: return a_ok, True
    # (5b) gcd
    nL = len(Lm)
    P = []
    for i in range(m):
        row = []
        for j in range(n):
            if i < nL:
                row.append([-LA[i][j], Lm[i][j]])
            else:
                row.append([base[i][j]])
        P.append(row)
    polys = []
    cnt = 0
    for rows in itertools.combinations(range(m), r0):
        for cols in itertools.combinations(range(n), r0):
            sub = [[P[i][j] for j in cols] for i in rows]
            d = pdet(sub, r0)
            if d is not None and not all(x == 0 for x in d):
                polys.append(d)
            cnt += 1
            if cnt > 1500: break
        if cnt > 1500: break
    if not polys: return a_ok, True
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
        if len(g) == 1: break
    return a_ok, (len(g) == 1)


def main():
    print("=== 非退化平行 + k≥1：(5a)∧(5b) 能否同时满足？ ===\n")
    print("%-8s %4s %4s %4s %5s %6s %6s %8s %8s" %
          ("trial","n","q0","k","r=2","非退化","平行","L0满足5a","最好结果"))
    print("-" * 74)
    rng = random.Random(97531)
    tot = 0
    found_yes = 0
    for trial in range(600000):
        if tot >= 10: break
        n, p = 6, 1
        Ac = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        CA = mm(Cc, Ac)
        W = Cc + CA
        dCA = n - rk(W)
        if dCA < 2: continue
        N = ker_basis(W)
        if not N or not N[0] or len(N[0]) != dCA: continue
        # 条件：CA²|_K ≠ 0（非不变），且 CA³|_K **平行于** CA²|_K
        CA2N = mm(CA, N)          # = CA² N
        CA3N = mm(mm(CA, Ac), N)  # = CA³ N
        if all(all(x == 0 for x in r) for r in CA2N): continue   # 需 ≠ 0
        if rk(CA2N + CA3N) != rk(CA2N): continue                 # 需平行
        # 构造 L0 = [CA² + CA ; CA²]
        row1 = [CA2N[i][0] if False else (mm(Cc, Ac)[0][i] + mm(Cc, Ac)[0][i]) for i in range(n)]
        # 直接矩阵层：ℓ0 = CA²（行向量），CA2 = mm(Cc,Ac) 再乘 A
        CA2 = mm(CA, Ac)          # 1×n, = C A²
        ell0 = CA2[0][:]
        rvec = CA[0][:]
        L0 = [[ell0[i] + rvec[i] for i in range(n)], ell0[:]]
        if rk(L0) != 2: continue
        if rk(L0 + Cc) != 3: continue
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(dCA)]
        pL = [pv(L0[0]), pv(L0[1])]
        pLA = [pv(mm([L0[0]], Ac)[0]), pv(mm([L0[1]], Ac)[0])]
        if all(all(x == 0 for x in w) for w in pL): continue
        if rk(pL + pLA) != 1: continue       # 平行
        # H4
        def obs(M, A, n):
            rows=[list(x) for x in M]; cur=[list(x) for x in M]
            for _ in range(n-1): cur=mm(cur,A); rows+=cur
            return rows
        if rk(obs(L0, Ac, n) + obs(Cc, Ac, n)) != rk(obs(Cc, Ac, n)): continue
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - 2
        if k < 1: continue
        tot += 1
        # L0 本身 (5a)？
        a0, b0 = check_5ab(L0, Ac, Cc)
        best = "失败" if not (a0 and b0) else "**L0 即可**"
        # 搜索 R
        hit = None
        for _ in range(200):
            rows = [r[:] for r in L0]
            for _i in range(k):
                rows.append([F(rng.randint(-3,3)) for _ in range(n)])
            L = rows
            a_ok, b_ok = check_5ab(L, Ac, Cc)
            if a_ok and b_ok:
                hit = L; break
            if a_ok and b_ok is False:
                pass
        if hit is not None:
            best = "**YES ✓**"
            found_yes += 1
        print("%-8d %4d %4d %4d %5s %6s %6s %8s %8s" %
              (trial, n, q0, k, "2", "✓", "✓",
               "是" if a0 else "否", best))
    print()
    print("非退化平行 + k≥1 实例数：%d" % tot)
    print("其中找到 (5a)∧(5b) 的：%d" % found_yes)
    print()
    if found_yes:
        print("⟹⟹⟹ **非退化平行 + k≥1 也可为 YES** ⟹ c6′ 的证伪**扩展到硬度相关范围** ⭐⭐⭐")
    else:
        print("⟹ 未找到 ⟹ 若成立则 c6′ 在 **k≥1** 范围**仍可能为真**")
        print("   ⟹ 本轮证伪只影响 k=0（不需增广）的实例")


if __name__ == "__main__":
    main()
