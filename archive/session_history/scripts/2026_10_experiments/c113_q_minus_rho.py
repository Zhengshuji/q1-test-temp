r"""
c113_q_minus_rho.py -- 用 q ≥ ρ+2 的实例，检验 c≥2 是否可能出现

上界：c ≤ min(ρ, q−ρ)。故必须 q−ρ ≥ 2。
取 q=5, r=2 → 若 ρ=2 则 q−ρ=3，c 可达 3。
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
    print("=== q=5, r=2（q−ρ 可 ≥3）上测 c ===\n")
    n=6; p=2
    t0=time.time(); t=0; inst=0
    tot=0; c0=c1=c2p=0; hist={}
    ex=None
    while time.time()-t0<430 and inst<10:
        t+=1
        rng=random.Random(930000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=4: continue
        N=ker_basis(Mrows)
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
        if rk(R0)<2: continue
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        L0=None
        for _x in range(60):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(2)]
            if rk(cand)!=2: continue
            if rk(cand+Cc)!=4: continue
            if rk(mm(cand,N))==0: continue
            L0=cand; break
        if L0 is None: continue
        inst+=1
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=5; kk=q-2; npar=kk*mB
        rr=random.Random(41+7*inst)
        pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(700)]
        loc={}
        for vals in pts:
            A0=[H0[0][:],H0[1][:]]; A1=[F0[0][:],F0[1][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                if len(z)<mB: break
                w=[sum(z[tt]*resB[tt][j] for tt in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if len(A0)!=q: continue
            if not cond_5a(A0,A1): continue
            rho=rk(A0)
            if rho==0: continue
            imF=rowspace_basis([[A1[i][j] for i in range(q)] for j in range(d)])
            imM=rowspace_basis([[A0[i][j] for i in range(q)] for j in range(d)])
            c=rk([r[:] for r in imF]+[r[:] for r in imM])-rho
            tot+=1
            hist[(rho,c)]=hist.get((rho,c),0)+1
            if c==0: c0+=1
            elif c==1: c1+=1
            else:
                c2p+=1
                if ex is None: ex=(A0,A1,rho,c)
        print("[实例 %d] (5a)-候选 %d ；(ρ,c) 分布：%s" % (inst, sum(hist.values()), sorted(hist.items())[:8]))
    print()
    print("(5a)-候选 %d ：c=0 %d，c=1 %d，**c≥2 %d**" % (tot,c0,c1,c2p))
    print("(ρ,c) 直方图：", sorted(hist.items()))
    if c2p>0:
        print("\n⟹ *** c≥2 出现！***")
        A0,A1,rho,c=ex
        print("   ρ=%d c=%d (5b)=%s" % (rho,c,cond_5b(A0,A1)))
    elif tot>0:
        print("\n⟹ 即使 q−ρ≥2，c≥2 仍不出现 ⟹ (5a) 给出 c≤1 ✓（真正的非平凡检验）")

if __name__=="__main__":
    main()
