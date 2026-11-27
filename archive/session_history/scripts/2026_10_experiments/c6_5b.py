# -*- coding: utf-8 -*-
"""
c6_5b.py -- ⭐⭐⭐ 直接检验问题的 **(5a) ∧ (5b)**（不是约化后的 (S)！）

【问题原文】
  (5a) rang[LA; L; CA; C] = rang[L; CA; C]
  (5b) rang[λL − LA; CA; C] = rang[L; CA; C]   ∀ λ ∈ ℂ

【(5b) 的判定】[λL−LA; CA; C] 的条目关于 λ 一次
  ⟹ (5b) ⟺ rank 恒等于 r0 := rang[L;CA;C]
  ⟺ 全部 r0 阶子式的 gcd 是非零常数

【为什么要重测】(S)（即 rank((λI−Λ)H) 恒定）只是 (5b) 的**必要**条件
  （由 (5b) 右乘 N_CA 得到）⟹ (S) 成立**不蕴含** (5b)
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


def check_5b(Lm, Ac, Cc, verbose=False):
    """直接检验 (5b)：rank[λL−LA; CA; C] 恒定？返回 (成立?, r0, gcd_deg)"""
    CAc = mm(Cc, Ac)
    LA = mm(Lm, Ac)
    base = [r[:] for r in Lm] + [r[:] for r in CAc] + [r[:] for r in Cc]
    r0 = rk(base)
    m = len(base); n = len(base[0])
    if r0 == 0: return True, r0, 0
    # 铅笔矩阵：前 |L| 行是 λL − LA（一次多项式），其余行是常数
    nL = len(Lm)
    P = []
    for i in range(m):
        row = []
        for j in range(n):
            if i < nL:
                row.append([-LA[i][j], Lm[i][j]])       # −LA + λ L
            else:
                row.append([base[i][j]])                # 常数
        P.append(row)
    # 全部 r0 阶子式的 gcd
    polys = []
    for rows in itertools.combinations(range(m), r0):
        for cols in itertools.combinations(range(n), r0):
            sub = [[P[i][j] for j in cols] for i in rows]
            d = pdet(sub, r0)
            if d is not None and not all(x == 0 for x in d): polys.append(d)
        if len(polys) > 400: break        # 采样上限（够用）
    if not polys: return True, r0, 0
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
        if len(g) == 1: break
    return (len(g) == 1), r0, len(g) - 1


def matpow(M, k):
    n=len(M); R=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k): R=mm(R,M)
    return R


def obs(M, A, n):
    """可观测性矩阵 [M; MA; MA^2; …; MA^{n-1}]（行堆叠）"""
    rows = [r[:] for r in M]
    cur = [r[:] for r in M]
    for _ in range(n - 1):
        cur = mm(cur, A)
        rows = rows + cur
    return rows


def h4_ok(L0, Cc, Ac, n):
    """H4：row(O_{L0}) ⊆ row(O_C)  （行堆叠判据）"""
    OL = obs(L0, Ac, n)
    OC = obs(Cc, Ac, n)
    return rk(OL + OC) == rk(OC)


def main():
    print("=== 直接检验 H1–H4 ∧ (5a) ∧ (5b) ===\n")
    print("%-8s %4s %4s %4s %6s %6s %6s %8s" %
          ("trial","n","q0","k","H4","(5a)","rkH","(5b)?"))
    print("-"*58)
    rng = random.Random(246813579)
    tot = 0; yes = 0
    h4fail = 0
    for trial in range(900000):
        if tot >= 8: break
        n, p = 6, 1
        Ac = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        pv = lambda v: [sum(v[i]*N[i][j] for i in range(n)) for j in range(d)]
        found = None
        for _ in range(150):
            row1 = mm(Cc, Ac)[0]
            row2 = [F(rng.randint(-2,2)) for _ in range(n)]
            L0 = [row1, row2]
            if rk(L0) != 2: continue
            if rk(L0 + Cc) != 3: continue
            if not h4_ok(L0, Cc, Ac, n): continue                 # ★ H4（必需！）
            if rk(mm(L0, Ac) + L0 + W) != rk(L0 + W): continue    # (5a)
            pL = [pv(L0[0]), pv(L0[1])]
            if all(all(x==0 for x in w) for w in pL): continue
            pLA = [pv(mm([L0[0]],Ac)[0]), pv(mm([L0[1]],Ac)[0])]
            if rk(pL + pLA) != 1: continue                        # 平行
            found = L0; break
        if found is None: continue
        L0 = found
        ok5b, r0, dg = check_5b(L0, Ac, Cc)
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - 2
        if k != 0: continue
        H = mm(L0, N)
        if rk(H) == 0 or rk(H) >= q0: continue
        tot += 1
        if ok5b: yes += 1
        print("%-8d %4d %4d %4d %6s %6s %6d %8s" %
              (trial, n, q0, k, "✓", "✓", rk(H), "**成立**" if ok5b else "失败"))
    print()
    print("（H1–H4 全部满足的）实例数 %d：(5b) 成立 %d，失败 %d" % (tot, yes, tot - yes))
    print()
    if yes:
        print("⟹⟹⟹ **存在满足 H1–H4 ∧ (5a) ∧ (5b) 的情形 II 平行实例** ⟹ YES ⭐⭐⭐")
        print("     ⟹ c6 / c6′（平行⟹NO）**假** ⟹ 分支 A 未被排除")
    else:
        print("⟹ (5b) 全部失败 ⟹ c6′ 在这些实例上仍成立")


if __name__ == "__main__":
    main()
