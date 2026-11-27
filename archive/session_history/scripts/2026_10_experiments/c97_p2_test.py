r"""
c97_p2_test.py -- 新覆盖：p=2（多输出），检验缺口 ρ=obs

此前所有测试都是 p=1。本脚本用 p=2 的系统（n=6 => d=n-2p=2；n=7 => d=3）
"""
import os, io, contextlib, random, itertools, sys, time
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
    print("=== 新覆盖 p=2（多输出）：检验缺口 ρ=obs ===\n")
    tot=0; sols=0; bad=0; nWinU=0
    t0=time.time(); trials=0
    while time.time()-t0<400 and tot<3000:
        trials+=1
        n=random.Random(710000+trials).choice([6,7])
        rng=random.Random(610000+trials)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        # C 为 2×n，rank 2
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(2)]
        if rk(Cc)!=2: continue
        CA=mm(Cc,A)
        if rk(CA)!=2: continue
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
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        R0b=rowspace_basis(R0)
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        # L0: 1×n，与 C 行独立
        L0=None
        for _x in range(30):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=3: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
            if all(x==0 for x in pv): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=3: continue
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=d+1; kk=q-1; npar=kk*mB
        if npar>8: continue
        rr=random.Random(77+trials)
        pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(120)]
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                if len(z)<mB: break
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if len(A0)!=q: continue
            if not cond_5a(A0,A1): continue
            tot+=1
            U=rowspace_basis(A0)
            if rk([r[:] for r in U]+[r[:] for r in R0b])==len(U): nWinU+=1
            if cond_5b(A0,A1):
                sols+=1
                if rk(A0)!=obs:
                    bad+=1
                    if bad<=3:
                        print("  **反例** n=%d p=2 d=%d obs=%d ρ=%d" % (n,d,obs,rk(A0)))
    print()
    print("检验候选 %d ；W⊆U %d ；解 %d ；**ρ≠obs 的反例 %d**" % (tot,nWinU,sols,bad))
    if bad==0 and sols>0:
        print("\n⟹ p=2 也零反例（%d 个解）⟹ 缺口证据扩展到多输出 ✓" % sols)
    elif sols==0:
        print("\n（未命中解 —— p=2 的解更稀疏）")


if __name__=="__main__":
    main()
