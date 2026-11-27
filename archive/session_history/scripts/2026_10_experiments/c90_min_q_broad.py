r"""
c90_min_q_broad.py -- 广泛检验猜测：|R|_min = obs+1-r（即 q_min = obs+1）

对多组 (obs, d) 与多实例，检验：
   q = obs      ⟹ 无解？
   q = obs+1    ⟹ 有解？
"""
import os, io, contextlib, random, itertools, time, sys
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]
_t={}
with open(os.path.join(_HERE,"test_caseII_YES.py"),encoding="utf-8") as fh:
    _src=fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0],"t","exec"),_t)
p1=_t["p1"]

def rowspace_basis(M):
    if not M or not M[0]: return []
    mr=len(M); nc=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,mr):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(mr):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def invariant_closure(M,Ap,d):
    basis=rowspace_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d and basis:
        cur=mm(cur,Ap)
        if rk(basis+[r[:] for r in cur])==len(basis): break
        basis=basis+[r[:] for r in cur]
    return rowspace_basis(basis)

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
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

def search_q(H0,F0,resB,mB,d,extra,limit=40000):
    kk=extra; npar=kk*mB
    ns=0; n5a=0; sols=0
    if npar<=5:
        it=itertools.product([-1,0,1],repeat=npar); exh=True
    else:
        rng=random.Random(909+97*npar)
        it=([rng.randint(-2,2) for _ in range(npar)] for _ in range(4000)); exh=False
    for vals in it:
        ns+=1
        if ns>limit: break
        A0=[H0[0][:]]; A1=[F0[0][:]]
        for ti in range(kk):
            z=vals[ti*mB:(ti+1)*mB]
            if len(z)<mB: continue
            w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
            A0.append(w[:d]); A1.append(w[d:])
        if not cond_5a(A0,A1): continue
        n5a+=1
        if cond_5b(A0,A1): sols+=1
    return ns,n5a,sols,exh

def main():
    print("=== 广泛检验：q=obs 无解？ q=obs+1 有解？ ===\n")
    results=[]
    for (n,d_target,obs_target) in [(5,3,2),(6,3,2),(6,4,2),(6,4,3)]:
        rng=random.Random(300011+n*10+d_target*3+obs_target)
        got=0; t0=time.time()
        while got<2 and time.time()-t0<200:
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA; N=ker_basis(W)
            if not N or not N[0]: continue
            d=len(N[0])
            if d!=d_target: continue
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            V=invariant_closure(R0,Ap,d); obs=len(V)
            if obs!=obs_target: continue
            L0=None
            for _x in range(80):
                cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
                if rk(cand)!=1: continue
                if rk(cand+Cc)!=2: continue
                pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
                if all(x==0 for x in pv): continue
                if V and rk([r[:] for r in V]+[pv])!=len(V): continue
                L0=cand; break
            if L0 is None: continue
            if rk(L0+Cc)!=2: continue
            try:
                _Lx,eta=p1(A,Cc,L0)
            except Exception:
                continue
            if not eta: continue
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=rowspace_basis(Mcol); mB=len(resB)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            r_=1
            row=[]
            for target_q in (obs, obs+1):
                extra=target_q-r_
                if extra<0: continue
                ns,n5a,sols,exh=search_q(H0,F0,resB,mB,d,extra)
                row.append((target_q,ns,n5a,sols,exh))
            print("[n=%d d=%d obs=%d #%d] mB=%d" % (n,d,obs,got,mB))
            for (q,ns,n5a,sols,exh) in row:
                lab = "=obs" if q==obs else "=obs+1"
                method = "穷尽" if exh else "采样"
                print("   q=%2d(%-6s) %s %5d：过(5a) %4d；**解 %3d**" % (q,lab,method,ns,n5a,sols))
            results.append((n,d,obs,row))
            print()
            got+=1
    print("=== 汇总 ===")
    bad=0
    for (n,d,obs,row) in results:
        for (q,ns,n5a,sols,exh) in row:
            if q==obs and sols>0: bad+=1
            if q==obs+1 and sols==0: bad+=1
    print("违反猜想的实例数：%d" % bad)
    if bad==0 and results:
        print("\n⟹ 全部支持 |R|_min = obs+1-r ✓（含穷尽与采样）")
        print("   注：q=obs 时若有解则猜测被推翻")


if __name__=="__main__":
    main()
