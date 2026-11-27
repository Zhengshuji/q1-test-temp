r"""
c93_W_in_U_iff_5b.py -- W ⊆ U 与 (5b) 的关系

在 (5a) 成立的候选中，检验：
   (5b)  ⟺  W := im(R₀ᵀ) ⊆ U := im(Mᵀ) ？
若等价 ⟹ 缺口变成"证明 (5b) ⟹ W⊆U"
若只单向 ⟹ 记录方向
"""
import os, io, contextlib, random, itertools, sys
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
    print("=== (5a) 成立时：W ⊆ U ⟺ (5b) ？ ===\n")
    n=4
    rng=random.Random(818181)
    got=0; tt=0; both=0; only5b=0; onlyW=0; neither=0
    t0=__import__("time").time()
    while got<6 and __import__("time").time()-t0<300:
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA; N=ker_basis(W)
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
        R0b=rowspace_basis(R0)             # W = im(R0ᵀ) = rowspace(R0)
        L0=None
        for _x in range(60):
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
        pts=list(itertools.product([-1,0,1],repeat=npar)) if npar<=6 else \
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(500)]
        a=b=c=e=0
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            tt+=1
            g=cond_5b(A0,A1)
            U=rowspace_basis(A0)
            WinU = (rk([r[:] for r in U]+[r[:] for r in R0b])==len(U))
            if g and WinU: both+=1; a+=1
            elif g and not WinU: only5b+=1; b+=1
            elif (not g) and WinU: onlyW+=1; c+=1
            else: neither+=1; e+=1
        print("[#%d] d=%d | 过(5a) %4d | 两者都✓ %3d ; 只(5b) %3d ; 只W⊆U %3d ; 都✗ %3d"
              % (got,d,tt,a,b,c,e))
        got+=1
        break
    print()
    print("=== 汇总（(5a) 成立的候选）===")
    print("总计 %d ；两者都✓ %d ; 仅(5b) %d ; 仅W⊆U %d ; 都✗ %d" % (tt,both,only5b,onlyW,neither))
    print()
    if only5b==0 and onlyW==0:
        print("⟹ **W⊆U ⟺ (5b)** （在 (5a) 成立时）⟹ 缺口 = 证 (5b) ⟹ W⊆U")
    elif only5b==0:
        print("⟹ (5b) ⟹ W⊆U ✓（反向不成立）⟹ 这正是我们需要的方向 ✓")
    elif onlyW==0:
        print("⟹ W⊆U ⟹ (5b)（单向，方向相反）")
    else:
        print("⟹ 两个条件**不相关** ⟹ W⊆U 不是 (5b) 的等价形式")


if __name__=="__main__":
    main()
