r"""
c33_rho1_criterion.py -- ⭐⭐⭐⭐ 检验精确判据：
   rho=1 构造可行 ⟺ 基行平行 ∧ α0 = L0N ∈ row(R)

【推导】
  固定行必须 (α0, γ0) = (c0·u, d0·u) ⟹ **基行平行**
  自由行 (c_i·α0, d_i·α0)：需 d_i·α0 − c_i·α0A' ∈ row(R)
  由基行平行：α0A' = d0·α0 − β0（β0 = L0R ∈ row(R)）
  ⟹ d_i·α0 − c_i·α0A' = (d_i − c_i·d0)·α0 + c_i·β0
  ⟹ 需 (d_i − c_i·d0)·α0 ∈ row(R)
  ⟹ **要么 d_i = c_i·d0（比值与固定行相同，⟹ 全等 ⟹ (5b) 失败）**
     **要么 α0 ∈ row(R)**
  ⟹ **rho=1 可行 ⟺ 基行平行 ∧ α0 ∈ row(R)**
"""
import os, io, contextlib, random, itertools
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


def main():
    print("=== 检验判据：rho=1 可行 ⟺ 基行平行 ∧ α0∈row(R) ===\n")
    print("%-12s %3s %5s %6s %10s %9s %9s %5s" %
          ("实例","d","obs","平行","α0∈rowR","rho=1解","判据预","一致"))
    print("-"*74)
    ok=0; bad=0
    for (n,seed,trials) in [(4,70052,[0,1,5]),(5,70065,[0,7])]:
        rng=random.Random(seed)
        for trial in range(300000):
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
            d=len(N[0])
            if d<2: continue
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
            if trial not in trials: continue
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            Rrow=row_space_basis(R); e=len(Rrow)
            acc=[r[:] for r in Rrow]; cur=[r[:] for r in Rrow]
            while rk(acc)<d:
                cur=mm(cur,Ap)
                if rk(acc+[r[:] for r in cur])==rk(acc): break
                acc=acc+[r[:] for r in cur]
            obs=rk(acc)
            a0=mm(L0,N); g0=mm(mm(L0,A),N)
            par = (rk([a0[0][:], g0[0][:]]) == rk(a0))
            # α0 ∈ row(R)?
            if e==0:
                a0in = all(x==0 for x in a0[0])
            else:
                a0in = (rk([r[:] for r in Rrow] + [a0[0][:]]) == e)
            pred = par and a0in
            # 枚举（只在参数不多时）
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=row_space_basis(Mcol); mB=len(resB)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            nfree=d; npar=nfree*mB
            if npar>6:
                print("%-12s %3d %5d %6s %10s %9s %9s %5s" %
                      ("n=%d t=%d"%(n,trial), d, obs,
                       "Y" if par else "N", "Y" if a0in else "N", "?","?", "skip"))
                continue
            r1=0
            for vals in itertools.product([-1,0,1], repeat=npar):
                A0=[H0[0][:]]; A1=[F0[0][:]]
                for ti in range(nfree):
                    z=vals[ti*mB:(ti+1)*mB]
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                if cond_5b(A0,A1) and rk(A0)==1:
                    r1+=1
            actual = (r1>0)
            good = (pred==actual)
            if good: ok+=1
            else: bad+=1
            print("%-12s %3d %5s %6s %10s %9d %9s %5s" %
                  ("n=%d t=%d"%(n,trial), d, "-",
                   "Y" if par else "N", "Y" if a0in else "N", r1,
                   "有解" if pred else "无解", "✓" if good else "**✗**"))
    print()
    print("一致 %d ；不一致 %d" % (ok,bad))
    if bad==0 and ok>0:
        print("⟹⟹⟹ **判据成立：rho=1 可行 ⟺ 基行平行 ∧ α0∈row(R)** ⭐⭐⭐⭐")
    elif bad>0:
        print("⚠️ 有失配，判据需修正")


if __name__=="__main__":
    main()
