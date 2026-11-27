r"""
c95_W_in_U_broad.py -- 大规模强化检验 (5b) ⟹ W ⊆ U

目标：为唯一的缺口收集更强的证据（此前 0/720）
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
    print("=== 大规模检验 (5b) ⟹ W⊆U ===\n")
    tot=0; n5b=0; bad=0; nWinU=0
    t0=__import__("time").time()
    trials=0
    while time.time()-t0<420 and tot<4000:
        trials+=1
        n=random.Random(4000+trials).choice([4,5])
        rng=random.Random(310000+trials)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA; N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
        if d not in (2,3): continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        R0b=rowspace_basis(R0)
        L0=None
        for _x in range(30):
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
        q=d+1; kk=q-1; npar=kk*mB
        if npar<=6:
            pts=list(itertools.product([-1,0,1],repeat=npar))
        else:
            rr=random.Random(55+trials)
            pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(250)]
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            tot+=1
            U=rowspace_basis(A0)
            WinU=(rk([r[:] for r in U]+[r[:] for r in R0b])==len(U))
            if WinU: nWinU+=1
            if cond_5b(A0,A1):
                n5b+=1
                if not WinU:
                    bad+=1
                    print("  **反例** n=%d d=%d" % (n,d))
        if tot>=4000: break
    print()
    print("检验候选 %d ；W⊆U 成立 %d ；(5b) 成立 %d" % (tot,nWinU,n5b))
    print("**(5b) 且 W⊄U 的反例：%d**" % bad)
    print()
    if bad==0:
        print("⟹ **(5b) ⟹ W⊆U 无反例**（%d 个 (5b) 成立的点）✓" % n5b)
        print("   缺口证据进一步增强；但**仍未证明** ✗")
    else:
        print("⟹ 发现反例 ⟹ 缺口命题为**假** ✗ ⟹ 需换路线")


if __name__=="__main__":
    main()
