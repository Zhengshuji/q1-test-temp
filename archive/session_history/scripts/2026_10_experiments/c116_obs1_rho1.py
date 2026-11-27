r"""
c116_obs1_rho1.py -- 决定性：d=2, obs=1 时是否有 ρ=1 的解？

若 YES ⟹ ρ=d 猜想假（但 ρ=obs 仍可成立）
若 NO  ⟹ 支持 "obs<d ⟹ 无解"
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
    print("=== d=2, obs=1：是否有 ρ=1 的解？ ===\n")
    n=4; p=1
    t0=time.time(); t=0; inst=0
    tot=0; found=False
    while time.time()-t0<420 and inst<8:
        t+=1
        rng=random.Random(950000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=2: continue
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
        if rk(R0)==0: continue
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        if obs!=1: continue
        inst+=1
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        L0=None
        for _x in range(80):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            if rk(mm(cand,N))==0: continue
            L0=cand; break
        if L0 is None: continue
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=2; kk=q-1; npar=kk*mB
        if npar<=6:
            pts=list(itertools.product([-2,-1,0,1,2],repeat=npar))
        else:
            rr=random.Random(71+7*inst)
            pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(3000)]
        loc=0; locrho={}
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
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
            loc+=1; locrho[rho]=locrho.get(rho,0)+1
            tot+=1
            if rho==1 and not found:
                found=True
                print("   *** 找到 ρ=1 < d=2 的解！ (obs=1) ***")
                print("   M =", [[str(x) for x in r] for r in A0])
                print("   F =", [[str(x) for x in r] for r in A1])
        print("[实例 %d] obs=1, d=2 ；解 %d ；ρ 分布 %s" % (inst,loc,sorted(locrho.items())))
    print()
    print("解 %d ；找到 ρ=1 的解：%s" % (tot,found))
    if found:
        print("\n⟹ *** ρ=d 猜想假 ***（但 ρ=obs=1 仍成立 ✓）")
        print("   说明：真正的规律是 ρ=obs，不是 ρ=d")
    elif tot>0:
        print("\n⟹ obs=1 时所有解 ρ=? 见分布")
    else:
        print("\n⟹ obs=1 时无解 ⟹ 支持 'obs<d ⟹ 无解'")

if __name__=="__main__":
    main()
