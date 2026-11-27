r"""
c121_obs3_rho2_proper.py -- 决定性：obs=3, d=4，用正确流程搜 ρ=2 的解

正确流程：
 1. 实例须 obs<d（这里 obs=3, d=4）
 2. L0 须满足 α0 = L0 N ∈ V（否则无解！）
 3. q=2，第二行自由（在 rowspace([N|AN]) 中搜索）
 4. 目标：找 (5a) ∧ (5b) 且 ρ=2 < obs=3 的解 ⟹ 缺口假
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

def rb(M):
    if not M or not M[0]: return []
    mr=len(M); nc=len(M[0]); A=[[Fr(x) for x in r] for r in M]; piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,mr):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]; pv=A[r][c]; A[r]=[x/pv for x in A[r]]
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
        A2[c],A2[p]=A2[p],A2[c]; pv=A2[c][c]; A2[c]=[x/pv for x in A2[c]]
        for i in range(n):
            if i!=c and A2[i][c]!=0:
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def invcl(M0,Ap,d):
    b=rb(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rb(b)

def main():
    print("=== obs=3, d=4：搜 ρ=2 的解（正确流程）===\n")
    n=6; p=1
    t0=time.time(); t=0; inst=0
    tot=0; hist={}
    while time.time()-t0<430 and inst<5:
        t+=1
        rng=random.Random(9100000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=2: continue
        N=ker_basis(Mrows)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=4: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        Vb=invcl(R0,Ap,d)
        if len(Vb)!=3: continue          # obs=3 < d=4
        # 筛 L0 使 alpha0 ∈ V
        L0=None
        for _ in range(600):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            a0=mm(cand,N)[0]
            if all(x==0 for x in a0): continue
            if rk([r[:] for r in Vb]+[a0[:]])!=len(Vb): continue
            L0=cand; break
        if L0 is None: continue
        inst+=1
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rb(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=3; kk=q-2; npar=kk*mB
        rr=random.Random(131+17*inst)
        pts=list(itertools.product([-2,-1,0,1,2],repeat=npar)) if npar<=5 else \
            [[rr.randint(-2,2) for _ in range(npar)] for _ in range(2000)]
        loc={}
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                if len(z)<mB: break
                w=[sum(z[tt]*resB[tt][j] for tt in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if len(A0)!=q: continue
            Kk=ker_basis(A0)
            if Kk and Kk[0] and rk(mm(A1,Kk))!=0: continue
            if not cond_5b(A0,A1): continue
            rho=rk(A0)
            if rho==0: continue
            loc[rho]=loc.get(rho,0)+1
            hist[rho]=hist.get(rho,0)+1
            tot+=1
        print("[实例 %d] obs=3 d=4 ；解 %d ；ρ 分布 %s" % (inst,sum(loc.values()),sorted(loc.items())))
    print()
    print("解总数 %d ；ρ 分布 %s" % (tot,sorted(hist.items())))
    print()
    if any(r==2 for r in hist):
        print("⟹ *** 找到 ρ=2 < obs=3 的解 ⟹ 缺口假 ⟹ q1 可能为真 ***")
    elif tot>0:
        print("⟹ *** obs=3 时所有解都有 ρ=3（=obs）⟹ 强烈支持缺口 *** ✓")
    else:
        print("⟹ 无解（需更多实例）")

if __name__=="__main__":
    main()
