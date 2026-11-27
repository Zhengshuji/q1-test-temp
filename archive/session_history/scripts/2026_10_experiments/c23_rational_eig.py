r"""
c23_rational_eig.py -- ⭐⭐⭐⭐ 最后候选判据：A' 是否有**有理**特征值

【理由】
  (5b) 的秩下降只发生在 λ 使 pencil 奇异处。λ 取值在**基域**（ℚ 或 ℝ）。
  · A'（3×3 或有理 d×d）的**实**特征值总存在（奇次）⟹ 不是判据
  · 但**有理**特征值（= 在 ℚ 中）不是总有 ⟹ 可能是判据

【测】判据 R1：charpoly(A') 在 ℚ 中有根（精确：有理根定理）
   与 q=d+1 处成功率的分组对照
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

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

def cond_5b(A0,A1,maxminors=400):
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    P=[[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxminors: break
        if cnt>maxminors: break
    return const_nz(gcd_all(ps))

def row_space_basis(M):
    m_rows=len(M); ncols=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(ncols):
        p=None
        for i in range(r,m_rows):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m_rows):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(ncols)]
        piv.append(r); r+=1
        if r==m_rows: break
    return [A[i][:] for i in piv]

def minv(M):
    n=len(M)
    A2=[[Fr(M[i][j]) for j in range(n)]+[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=None
        for i in range(c,n):
            if A2[i][c]!=0: p=i; break
        if p is None: return None
        A2[c],A2[p]=A2[p],A2[c]
        pv=A2[c][c]; A2[c]=[x/pv for x in A2[c]]
        for i in range(n):
            if i!=c and A2[i][c]!=0:
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def charpoly(M):
    n=len(M)
    I=[[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
    cs=[]; Acur=[r[:] for r in I]
    for k in range(1,n+1):
        Mk=mm(M,Acur)
        c=-sum(Mk[i][i] for i in range(n))/k
        cs.append(c)
        Acur=[[Mk[i][j]+(c if i==j else Fr(0)) for j in range(n)] for i in range(n)]
    return [cs[-1]]+list(reversed(cs[:-1]))+[Fr(1)]

def has_rational_root(coef):
    """有理根定理（精确）：若 p/q 是根，q | a_n, p | a_0"""
    c=[x for x in coef]
    while len(c)>1 and c[-1]==0: c.pop()
    if len(c)<=1: return True                      # 零多项式 ⟹ 处处为根
    if len(c)==2: return True                      # 一次 ⟹ 有有理根
    a0=c[0]
    if a0==0: return True                          # 0 是根
    # 清理分母为整数
    from math import gcd as igcd
    dens=[x.denominator for x in c]
    L=1
    for dd in dens: L=L*dd//igcd(L,dd)
    ints=[int(x*L) for x in c]
    g=0
    for x in ints: g=igcd(g,abs(x))
    ints=[x//g for x in ints] if g else ints
    a0=ints[0]; an=ints[-1]
    if a0==0: return True
    def divisors(m):
        m=abs(m); out=[]
        for i in range(1,int(m**0.5)+1):
            if m%i==0:
                out.append(i)
                if i!=m//i: out.append(m//i)
        return out
    ps=divisors(a0); qs=divisors(an)
    for p in ps:
        for q in qs:
            for sgn in (1,-1):
                x=Fr(sgn*p,q)
                v=Fr(0)
                for cc in reversed(ints):
                    v=v*x+cc
                if v==0: return True
    return False


def main():
    print("=== 最后候选判据：A' 是否有有理特征值 ===\n")
    print("%-3s %-5s %3s %3s %5s %8s %6s %7s" %
          ("n","inst","d","m","dimR","A'有理谱","采样","成功率"))
    print("-"*52)
    data=[]
    for n in [5,6]:
        rng=random.Random(313100+n)
        done=0; t_all=time.time()
        for trial in range(80000):
            if done>=10 or time.time()-t_all>450: break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
            d=len(N[0])
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
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            dimR=rk(R)
            cp=charpoly(Ap)
            rat=has_rational_root(cp)
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            B=row_space_basis(Mcol); mm_=len(B)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            q=d+1; k=q-1
            rng2=random.Random(888111+97*trial+n)
            ns=0; nboth=0
            tt=time.time()
            while ns<250 and time.time()-tt<25:
                ns+=1
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mm_)] for _ in range(k)]
                A0=[H0[i][:] for i in range(1)]; A1=[F0[i][:] for i in range(1)]
                for z in rr:
                    w=[sum(z[t]*B[t][j] for t in range(mm_)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                if cond_5b(A0,A1): nboth+=1
            rate=100.0*nboth/ns if ns else -1
            print("%-3d %-5d %3d %3d %5d %8s %6d %6.1f%%" %
                  (n,trial,d,d+dimR,dimR,"有" if rat else "无",ns,rate))
            data.append((rat,rate))
            done+=1
        print()
    print("【分组】")
    for kk,lab in [(True,"A' 有有理特征值"),(False,"A' 无有理特征值")]:
        v=[r for a,r in data if a==kk]
        if not v: print("  %s: 无样本" % lab); continue
        print("  %-18s: n=%d ; 成功率 %s ; 均值 %.1f%%" %
              (lab,len(v),"[%.1f, %.1f]" % (min(v),max(v)), sum(v)/len(v)))
    print()
    print("【判读】若 '有' 组全 0% 而 '无' 组全 >50% ⟹ **判据找到** ⭐⭐⭐⭐")


if __name__ == "__main__":
    main()
