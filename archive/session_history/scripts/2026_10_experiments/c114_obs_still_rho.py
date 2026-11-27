r"""
c114_obs_still_rho.py -- q=5, c=2 的候选：obs 是否仍 = ρ？

这是最关键的检验：如果 obs=ρ 在 c=2 时仍成立，
则主结果不变，只是我此前的"机制"错了。
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

def invcl(M0,Ap,d):
    b=rowspace_basis(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rowspace_basis(b)

def main():
    print("=== q=5 时：c≥2 的候选是否仍满足 obs=ρ ？ ===\n")
    n=6; p=2
    t0=time.time(); t=0; inst=0
    tot=0; eq=0; neq=0; histc={}
    while time.time()-t0<420 and inst<6:
        t+=1
        rng=random.Random(931000+t)
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
        Vb=invcl(R0,Ap,d); obs=len(Vb)
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
        rr=random.Random(51+7*inst)
        pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(500)]
        loc_tot=loc_eq=loc_neq=0
        for vals in pts:
            A0=[H0[0][:],H0[1][:]]; A1=[F0[0][:],F0[1][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                if len(z)<mB: break
                w=[sum(z[tt]*resB[tt][j] for tt in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if len(A0)!=q: continue
            if not cond_5a(A0,A1): continue
            if not cond_5b(A0,A1): continue
            rho=rk(A0)
            if rho==0: continue
            imF=rowspace_basis([[A1[i][j] for i in range(q)] for j in range(d)])
            imM=rowspace_basis([[A0[i][j] for i in range(q)] for j in range(d)])
            c=rk([r[:] for r in imF]+[r[:] for r in imM])-rho
            histc[c]=histc.get(c,0)+1
            loc_tot+=1; tot+=1
            if rho==obs: loc_eq+=1; eq+=1
            else:
                loc_neq+=1; neq+=1
                if neq<=3:
                    print("   **obs≠ρ**：ρ=%d obs=%d c=%d" % (rho,obs,c))
        print("[实例 %d] obs=%d ；解 %d ：obs=ρ %d ；obs≠ρ %d" % (inst,obs,loc_tot,loc_eq,loc_neq))
    print()
    print("解 %d ：obs=ρ %d ；**obs≠ρ %d**" % (tot,eq,neq))
    print("c 的分布：", sorted(histc.items()))
    if neq==0 and tot>0:
        print("\n⟹ *** 即使 c≥2，obs=ρ 仍成立 *** ⟹ 主结果不受影响 ✓")
        print("   但'c≤1'是错的（第 55 处更正）；机制需另寻")
    elif neq>0:
        print("\n⟹ *** obs≠ρ 出现！*** ⟹ 主结果被推翻 ✗ 需重新评估")

if __name__=="__main__":
    main()
