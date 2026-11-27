r"""
c25_invariant_diff.py -- ⭐⭐⭐⭐ 系统对比 Type I / Type II 的细不变量

【思路】前面测过的秩量都相同 ⟹ 差异必在 $(A', \operatorname{row}R)$ 的**结构**里
【候选不变量】
  e   = m − d = dim row(R)
  Rinv: R 的 row 空间是否 A'-不变（dim(rowR + rowR·A') − e）
  cp   : charpoly(A') 的**根结构**（是否在 ℚ 有根；是否有重根）
  mp   : A' 的极小多项式次数
  obs  : 对 (A', rowR) 的"可观测性指数" = dim Σ_k rowR·A'^k
  base : 基础铅笔 (H0,F0) 的秩 / 其"有理特征值"个数
"""
import os, io, contextlib, random, itertools, time
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
def Pdv(a,b):
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
        _,r=Pdv(a,b); a,b=b,r
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

def cond_5b(A0,A1,maxm=400):
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    P=[[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxm: break
        if cnt>maxm: break
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

def has_rat_root(coef, maxdens=12):
    c=[x for x in coef]
    while len(c)>1 and c[-1]==0: c.pop()
    if len(c)<=1: return True
    if len(c)==2: return True
    if c[0]==0: return True
    def divs(m):
        m=abs(m); out=[]
        for i in range(1,int(m**0.5)+1):
            if m%i==0:
                out.append(i)
                if i!=m//i: out.append(m//i)
        return out
    a0=c[0]
    # 清分母
    from math import gcd as ig
    L=1
    for x in c:
        dd=x.denominator; L=L*dd//ig(L,dd)
    ints=[int(x*L) for x in c]
    g=0
    for x in ints: g=ig(g,abs(x))
    if g: ints=[x//g for x in ints]
    if ints[0]==0: return True
    for p in divs(ints[0])[:40]:
        for q in divs(abs(ints[-1]))[:20]:
            for s in (1,-1):
                x=Fr(s*p,q); v=Fr(0)
                for cc in reversed(ints): v=v*x+cc
                if v==0: return True
    return False

def sqfree_deg(coef):
    """charpoly 的平方自由部分次数（判重根）"""
    c=Pt([x for x in coef])
    if len(c)<=1: return 0
    def deriv(q): return [Fr(i)*q[i] for i in range(1,len(q))] or [Fr(0)]
    g=Pg(c, deriv(c))
    q,r=Pdv(c,g) if len(g)>1 or (len(g)==1 and g[0]!=0) else (c,[Fr(0)])
    return len(Pt(q))-1


def main():
    print("=== Type I / Type II 的细不变量对比 ===\n")
    hdr = ("%-3s %-5s %3s %3s %3s %5s %5s %5s %5s %6s %8s" %
           ("n","inst","d","m","e","Rinv","cpℚ?","sfd","obs","ρ0","成功率"))
    print(hdr); print("-"*len(hdr))
    data=[]
    for n in [5,6]:
        rng=random.Random(314100+n)
        done=0; t_all=time.time()
        for trial in range(80000):
            if done>=8 or time.time()-t_all>400: break
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
            Rrow=row_space_basis(R); e=len(Rrow)
            if e==0: continue                       # 只要非不变
            # Rinv: dim(rowR + rowR·A') − e
            RAp=mm(Rrow,Ap)
            Rinv=rk([r[:] for r in Rrow]+[r[:] for r in RAp])-e
            cp=charpoly(Ap)
            hr=has_rat_root(cp)
            sfd=sqfree_deg(cp)
            # obs: dim Σ_{k<d} rowR·A'^k
            cur=[r[:] for r in Rrow]; acc=[r[:] for r in Rrow]
            for _k in range(d-1):
                cur=mm(cur,Ap); acc=acc+[r[:] for r in cur]
            obs=rk(acc)
            H0=mm(L0,N); F0=mm(mm(L0,A),N); rho0=rk(H0)
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=row_space_basis(Mcol); mB=len(resB)
            q=d+1; k=q-1
            rng2=random.Random(654321+97*trial+n)
            ns=0; nb=0
            tt=time.time()
            while ns<250 and time.time()-tt<25:
                ns+=1
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(k)]
                A0=[H0[i][:] for i in range(1)]; A1=[F0[i][:] for i in range(1)]
                for z in rr:
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                if cond_5b(A0,A1): nb+=1
            rate=100.0*nb/ns if ns else -1
            print("%-3d %-5d %3d %3d %3d %5d %5s %5d %5d %6d %7.1f%%" %
                  (n,trial,d,mB,e,Rinv,"Y" if hr else "N",sfd,obs,rho0,rate))
            data.append((Rinv,hr,sfd,obs,rate))
            done+=1
        print()
    print("【分组】")
    for name,idx in [("Rinv",0),("cpℚ?",1),("sfd",2),("obs",3)]:
        T=[t[4] for t in data if t[idx]]
        F=[t[4] for t in data if not t[idx]]
        print("  %-6s: 真值组 均值%7.1f%% (n=%d) ; 假值组 均值%7.1f%% (n=%d)" %
              (name, sum(T)/len(T) if T else -1, len(T),
               sum(F)/len(F) if F else -1, len(F)))
    print()
    print("【判读】若某不变量的真/假分组成功率分离（~95% vs ~0%）⟹ 判据找到")


if __name__=="__main__":
    main()
