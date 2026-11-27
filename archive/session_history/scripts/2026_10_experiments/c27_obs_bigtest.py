r"""
c27_obs_bigtest.py -- ⭐⭐⭐⭐ obs 判据的**大规模独立复核**

【判据】Type II ⟺ obs < d_CA，其中 obs = dim(含 row(R) 的最小 A'-不变子空间)
【本脚本】30+ 实例，n ∈ {4,5,6,7}，用**独立 rng** 采样，统计分离度
   · 只要 obs=d 的实例 → 应高成功率
   · 只要 obs<d 的实例 → 应 0%
   · **任何失配都要报出来**
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

def cond_5b(A0,A1,maxm=250):
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
    print("=== obs 判据：大规模独立复核 ===\n")
    hdr = "%-3s %-6s %3s %3s %3s %5s %6s %8s %4s" % ("n","inst","d","m","e","obs","obs<d","成功率","OK")
    print(hdr); print("-"*len(hdr))
    nI=nII=nMis=0; mism=[]
    for n in [4,5,6,7]:
        rng=random.Random(70000+n*13)
        done=0; t_all=time.time()
        want = 8 if n<=6 else 5
        for trial in range(150000):
            if done>=want or time.time()-t_all>300: break
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
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            Rrow=row_space_basis(R); e=len(Rrow)
            if e==0: continue
            acc=[r[:] for r in Rrow]; cur=[r[:] for r in Rrow]
            while rk(acc) < d:
                cur=mm(cur,Ap)
                new=rk(acc+[r[:] for r in cur])
                if new==rk(acc): break
                acc=acc+[r[:] for r in cur]
            obs=rk(acc)
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=row_space_basis(Mcol); mB=len(resB)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            q=d+1; k=q-1
            rng2=random.Random(1234567+97*trial+n)
            ns=0; nb=0
            tt=time.time()
            while ns<150 and time.time()-tt<20:
                ns+=1
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(k)]
                A0=[H0[i][:] for i in range(1)]; A1=[F0[i][:] for i in range(1)]
                for z in rr:
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                if cond_5b(A0,A1): nb+=1
            rate=100.0*nb/ns if ns else -1
            pred = "II" if obs<d else "I"
            actual = "II" if rate < 1.0 else "I"
            ok = (pred==actual)
            if not ok:
                nMis+=1; mism.append((n,trial,d,obs,rate))
            if actual=="I": nI+=1
            else: nII+=1
            print("%-3d %-6d %3d %3d %3d %5d %6s %7.1f%% %4s" %
                  (n,trial,d,mB,e,obs,"Y" if obs<d else "N",rate,"✓" if ok else "**✗**"))
            done+=1
        print()
    print("="*56)
    print("Type I：%d ；Type II：%d ；**失配：%d**" % (nI,nII,nMis))
    for m in mism:
        print("  失配：n=%d inst=%d d=%d obs=%d rate=%.1f%%" % m)
    print()
    if nMis==0 and nI>0 and nII>0:
        print("⟹⟹⟹ **obs 判据在 %d 个实例上全部吻合** ✓✓✓" % (nI+nII))
        print("     Type I（obs=d）：%d 个，全部 >1%% 成功率" % nI)
        print("     Type II（obs<d）：%d 个，全部 0%%" % nII)
    elif nII==0:
        print("⚠️ 本次没有抽到 Type II 实例（obs<d 稀有）—— 需定向构造")
    else:
        print("⚠️ 有失配，判据需修正")


if __name__=="__main__":
    main()
