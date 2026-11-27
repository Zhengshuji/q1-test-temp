# -*- coding: utf-8 -*-
"""
c6_degenerate_5b.py -- ⭐⭐⭐ 退化分支（π(L0)=0）+ 非不变 A + k≥1：(5b) 能否满足？

【与项目 14/14 的差别】
  项目实例：π(L0)=0 且 CA²=0（**A-不变**）
  本脚本  ：π(L0)=0 但 CA²|_K ≠ 0（**非不变**）—— c6′ 从未在此测试

【判据】直接测 (5b)（不是约化的 (S)）
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

def check_5ab(Lm, Ac, Cc, maxminors=800):
    CAc = mm(Cc, Ac); LA = mm(Lm, Ac)
    base = [r[:] for r in Lm] + [r[:] for r in CAc] + [r[:] for r in Cc]
    r0 = rk(base); m = len(base); n = len(base[0])
    a_ok = (rk([r[:] for r in LA] + base) == r0)
    if r0 == 0: return a_ok, True
    nL = len(Lm)
    P = [[ ([-LA[i][j], Lm[i][j]] if i < nL else [base[i][j]]) for j in range(n)] for i in range(m)]
    polys=[]; cnt=0
    for rows in itertools.combinations(range(m), r0):
        for cols in itertools.combinations(range(n), r0):
            d = pdet([[P[i][j] for j in cols] for i in rows], r0)
            if d is not None and not all(x==0 for x in d): polys.append(d)
            cnt += 1
            if cnt > maxminors: break
        if cnt > maxminors: break
    if not polys: return a_ok, True
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
        if len(g)==1: break
    return a_ok, (len(g)==1)

def obs(M, A, n):
    rows=[list(x) for x in M]; cur=[list(x) for x in M]
    for _ in range(n-1): cur=mm(cur,A); rows+=cur
    return rows

def matpow(M,k):
    n=len(M); R=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k): R=mm(R,M)
    return R


def main():
    print("=== 退化分支（π(L0)=0）+ 非不变 + k≥1：(5b) 能否满足？ ===\n")
    print("%-8s %4s %4s %4s %8s %8s %8s %10s" %
          ("trial","n","q0","k","不变?","(5a)L0","(5b)可能","结论"))
    print("-" * 70)
    rng = random.Random(112358)
    tot = 0; yes = 0; no = 0
    for trial in range(600000):
        if tot >= 12: break
        n, p = 6, 1
        Ac = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        dCA = n - rk(W)
        N = ker_basis(W)
        if not N or not N[0] or len(N[0]) != dCA: continue
        AN = mm(Ac, N)
        cj0 = [[N[i][j] for j in range(dCA)] + [AN[i][j] for j in range(dCA)] for i in range(n)]
        inv = (rk(cj0) == rk(N))
        if inv: continue                       # 只要**非不变**
        mp = rng.randint(1, 2)
        L0 = mm(Cc, matpow(Ac, mp))
        if rk(L0) != 1: continue
        if rk(L0 + Cc) != 2: continue
        pv = lambda v: [sum(v[i]*N[i][j] for i in range(n)) for j in range(dCA)]
        if not all(x == 0 for x in pv(L0[0])): continue    # 需退化 π(L0)=0
        if rk(obs(L0, Ac, n) + obs(Cc, Ac, n)) != rk(obs(Cc, Ac, n)): continue  # H4
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - 1
        if k < 1: continue
        if dCA < q0: continue                 # 情形 II
        tot += 1
        a0, b0 = check_5ab(L0, Ac, Cc)
        hit = None
        for _ in range(120):
            rows = [r[:] for r in L0]
            for _i in range(k):
                rows.append([F(rng.randint(-3,3)) for _ in range(n)])
            a_ok, b_ok = check_5ab(rows, Ac, Cc)
            if a_ok and b_ok: hit = rows; break
        concl = "**YES ✓**" if hit else "NO"
        if hit: yes += 1
        else: no += 1
        print("%-8d %4d %4d %4d %8s %8s %8s %10s" %
              (trial, n, q0, k, "否", "是" if a0 else "否",
               "✓" if b0 else "—", concl))
    print()
    print("退化+非不变+情形II 实例：%d ；找到 (5a)∧(5b)：%d ；未找到：%d" % (tot, yes, no))
    print()
    if yes:
        print("⟹⟹⟹ **退化分支也可是 YES** ⟹ c6′ **完全被证伪** ⟹ 情形 II 的硬度完全开放 ⭐⭐⭐")
    else:
        print("⟹ 未找到 ⟹ c6′ 在退化分支上仍成立（与项目 14/14 一致，但扩展到非不变 A）")


if __name__ == "__main__":
    main()
