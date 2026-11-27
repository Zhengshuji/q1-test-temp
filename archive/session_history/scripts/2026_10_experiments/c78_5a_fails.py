r"""
c78_5a_fails.py -- 广泛验证新猜想：obs<ρ ⟹ (5a) 失败

对 (5a) 通过率按 (ρ vs obs) 分层统计
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

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

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
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def invariant_closure(M, Ap, d):
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
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def main():
    print("=== 验证：obs<ρ ⟹ (5a) 失败 ===\n")
    print("%-22s %8s %8s %8s" % ("(d,obs,ρ)","样本","过(5a)","通过率"))
    print("-"*50)
    stats={}
    for n in (5,6,7):
        rng=random.Random(440000+n)
        got=0; t0=time.time()
        while got<3 and time.time()-t0<200:
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
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            V=invariant_closure(R, Ap, d)
            obs=len(V)
            if obs>=d: continue
            L0=None
            for _x in range(40):
                cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
                if rk(cand)!=1: continue
                if rk(cand+Cc)!=2: continue
                pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
                if all(x==0 for x in pv): continue
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
            q=d+1; kk=q-1
            npar=kk*mB
            rng2=random.Random(19+97*got+n)
            NS=300; ns=0
            while ns<NS:
                ns+=1
                vals=[rng2.randint(-2,2) for _ in range(npar)]
                A0=[H0[0][:]]; A1=[F0[0][:]]
                for ti in range(kk):
                    z=vals[ti*mB:(ti+1)*mB]
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                r0=rk(A0)
                key=(d,obs,r0)
                if key not in stats: stats[key]=[0,0]
                stats[key][0]+=1
                if cond_5a(A0,A1): stats[key][1]+=1
            got+=1
    for key in sorted(stats):
        d,obs,r0=key
        tot,ok=stats[key]
        if r0>obs:                       # 只需 obs<ρ
            mark = "  ← **obs<ρ**" if tot>=5 else ""
            print("%-22s %8d %8d %7.0f%%%s" % (str(key), tot, ok, 100.0*ok/tot, mark))
    print()
    print("【判读】obs<ρ 各层的 (5a) 通过率若为 0 ⟹ 猜想成立 ✓")


if __name__=="__main__":
    main()
