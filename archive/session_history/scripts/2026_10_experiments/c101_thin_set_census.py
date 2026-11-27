r"""
c101_thin_set_census.py -- 在薄集 γ₀∥α₀ 上做彻底普查

理由（c100）：反例只可能出现在 γ₀∥α₀ 的实例上。
本脚本：构造这类实例，穷尽/密集扫候选，统计 ρ 的分布
"""
import os, io, contextlib, random, sys, time, itertools
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]

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

def nullspace_rows(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

def invcl(M0,Ap,d):
    b=rowspace_basis(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rowspace_basis(b)

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

def main():
    print("=== 薄集 γ₀∥α₀ 上的彻底普查 ===\n")
    print("%-8s %3s %4s %5s %10s %12s" % ("#","d","obs","|薄集|","解数","ρ<obs?"))
    print("-"*50)
    t0=time.time(); t=0; inst=0; tot_sol=0; viol=0
    while time.time()-t0<400 and inst<8:
        t+=1
        n=random.Random(940000+t).choice([4,5])
        rng=random.Random(840000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        N=ker_basis(Cc+CA)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        if obs<2: continue
        # 薄集：找 w 与 L0 使 γ₀=w α₀
        got=None
        for w in (Fr(0),Fr(1),Fr(2),Fr(-1)):
            MWt=[[AN[i][j]-w*N[i][j] for i in range(n)] for j in range(d)]
            ann=nullspace_rows(MWt)
            for av in ann:
                L0=[av[:]]
                if rk(L0)!=1: continue
                if rk(L0+Cc)!=2: continue
                a0=mm(L0,N)[0]
                if all(x==0 for x in a0): continue
                got=(L0,w,a0); break
            if got: break
        if not got: continue
        L0,w,a0=got
        inst+=1
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=d+1; kk=q-1; npar=kk*mB
        if npar>6:
            rr=random.Random(99+t)
            pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(2000)]
            exh=False
        else:
            pts=list(itertools.product([-1,0,1],repeat=npar)); exh=True
        ns=0; sols=0; bad=0; dist={}
        for vals in pts:
            ns+=1
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                if len(z)<mB: break
                wv=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(wv[:d]); A1.append(wv[d:])
            if len(A0)!=q: continue
            if not cond_5a(A0,A1): continue
            if not cond_5b(A0,A1): continue
            sols+=1
            r0=rk(A0); dist[r0]=dist.get(r0,0)+1
            if r0<obs: bad+=1
        tot_sol+=sols; viol+=bad
        method="穷尽" if exh else "采样"
        print("%-8s %3d %4d %5s %10d %12s" %
              ("#%d"%inst, d, obs, method+str(ns), sols, "**%d**"%bad if bad else "0"))
        for r0 in sorted(dist):
            print("        ρ=%d: %d 个%s" % (r0,dist[r0], " ← obs" if r0==obs else (" **<obs**" if r0<obs else "")))
    print()
    print("实例 %d ；总解 %d ；**ρ<obs 的解 %d**" % (inst,tot_sol,viol))
    if viol==0 and tot_sol>0:
        print("\n⟹ 薄集上也**没有** ρ<obs 的解 ⟹ ρ≥obs 证据极强 ✓（但仍非证明 ✗）")
    elif tot_sol==0:
        print("\n（薄集上无解）")


if __name__=="__main__":
    main()
