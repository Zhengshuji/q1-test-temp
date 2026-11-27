r"""
c8_n5_decisive.py -- ⭐⭐⭐ 决定性单点：n=5 的非退化实例在 q=q0+1（k=2）时是否 YES？

【背景】
  c8_verify.py 在 n=5 时，非退化组全部"—"，但那是**枚举上限**（k·n ≤ 8）造成的：
  k=2, n=5 ⟹ k·n = 10 > 8 ⟹ 从未测试 q=q0+1！

  本脚本专门测 n=5, k=2, 域 {−1,0,1}（3¹⁰ = 59049），少量实例。
"""
import os
import io
import contextlib
import random
import itertools
import time
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

def Pt(p):
    q=list(p)
    while len(q)>1 and q[-1]==0: q.pop()
    return q
def Pa(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))+(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Ps(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))-(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Pm(a,b):
    if Pt(a)==[Fr(0)] or Pt(b)==[Fr(0)]: return [Fr(0)]
    r=[Fr(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return Pt(r)
def Pd(a,b):
    a=Pt(a); b=Pt(b); db=len(b)-1
    q=[Fr(0)]*max(1,len(a)-db)
    while len(a)-1>=db and a!=[Fr(0)]:
        d=len(a)-1-db; co=a[-1]/b[-1]; q[d]+=co
        for i in range(len(b)): a[d+i]-=co*b[i]
        a=Pt(a)
    return Pt(q),a
def Pg(a,b):
    a,b=Pt(a),Pt(b)
    while b!=[Fr(0)]:
        _,r=Pd(a,b); a,b=b,r
    if len(a)>1:
        lc=a[-1]; a=[x/lc for x in a]
    return a
def Pdet(M,k):
    if k==1: return [Fr(x) for x in M[0][0]]
    tot=[Fr(0)]
    for j in range(k):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        d=Pdet(sub,k-1); pr=Pm(M[0][j],d)
        tot=Pa(tot,pr) if j%2==0 else Ps(tot,pr)
    return Pt(tot)
def gcd_all(ps):
    if not ps: return None
    g=ps[0]
    for q in ps[1:]:
        g=Pg(g,q)
        if len(g)==1: break
    return g
def const_nz(g):
    return g is not None and len(Pt(g))==1 and any(x!=0 for x in g)

def cond_5a(L,A,N):
    LN=mm(L,N); LAN=mm(mm(L,A),N)
    K=ker_basis(LN)
    if not K or not K[0]: return True
    assert len(LAN[0])==len(K)
    return rk(mm(LAN,K))==0

def cond_5b(L,A,N,maxminors=400):
    d=len(N[0]); AN=mm(A,N); LN=mm(L,N); rho=rk(LN)
    if rho==0: return True
    LAN=mm(L,AN); q=len(L)
    P=[[[-LAN[i][j], LN[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxminors: break
        if cnt>maxminors: break
    return const_nz(gcd_all(ps))


def main():
    print("=== 决定性单点：n=5, k=2（q=q0+1）, 域 {-1,0,1} ===\n")
    n = 5
    dom = [-1,0,1]
    rng = random.Random(424242)
    got = 0
    print("%-6s %3s %3s %6s %8s %10s %10s %8s" %
          ("inst","q0","k0","退化?","枚举数","(5a)点","(5a∧5b)","结论"))
    print("-"*64)
    t0 = time.time()
    for trial in range(200000):
        if got >= 5 or time.time() - t0 > 900:
            break
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        # 只要**非退化** L0
        L0=None
        for _x in range(40):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
            if all(x==0 for x in pv): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        try:
            _Lx,eta=p1(A,Cc,L0)
        except Exception:
            continue
        if not eta: continue
        q0=sum(eta); r=1; k0=q0-r
        if k0!=1: continue
        k=2                                  # q = q0+1
        cnt=0; n5a=0; hit=0
        for vals in itertools.product(dom, repeat=k*n):
            cnt+=1
            R=[[Fr(vals[i*n+j]) for j in range(n)] for i in range(k)]
            L=L0+R
            if not cond_5a(L,A,N): continue
            n5a+=1
            if cond_5b(L,A,N):
                hit+=1
                break
        got+=1
        print("%-6d %3d %3d %6s %8d %10d %10d %8s" %
              (trial, q0, k0, "F", cnt, n5a, hit,
               "**YES ✓**" if hit else "NO"))
    print()
    print("已完成 %d 个实例；用时 %.1f s" % (got, time.time()-t0))
    print()
    print("【判读】")
    print("  若非退化 n=5 在 q0+1 找到 YES ⟹ c8 在 n=5 也成立 ⟹ q1 可能为假")
    print("  若全部 NO ⟹ n=4 的 q*=q0+1 是小 n 巧合 ⟹ c8 不成立")


if __name__ == "__main__":
    main()
