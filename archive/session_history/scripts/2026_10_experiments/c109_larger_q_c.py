r"""
c109_larger_q_c.py -- 在更大的 q 下检验：c≥2 是否可能出现？

此前只在 q=d+1 上测过。c ≤ min(ρ, q−ρ)，故更大的 q 可能允许 c≥2。
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
    print("=== 更大 q 下：c≥2 是否出现？ ===\n")
    n=4; rng=random.Random(707080)
    got=0; t0=time.time()
    results={}
    while got<6 and time.time()-t0<400:
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
        try: _Lx,eta=p1(A,Cc,L0)
        except Exception: continue
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        got+=1
        for qq in (d+1, d+2, d+3):
            kk=qq-1; npar=kk*mB
            if npar>12: continue
            rr=random.Random(11+97*got+qq)
            pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(400)]
            c0=c1=c2=0
            for vals in pts:
                A0=[H0[0][:]]; A1=[F0[0][:]]
                for ti in range(kk):
                    z=vals[ti*mB:(ti+1)*mB]
                    if len(z)<mB: break
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if len(A0)!=qq: continue
                if not cond_5a(A0,A1): continue
                rho=rk(A0)
                if rho==0: continue
                imF=rowspace_basis([[A1[i][j] for i in range(qq)] for j in range(d)])
                imM=rowspace_basis([[A0[i][j] for i in range(qq)] for j in range(d)])
                c=rk([r[:] for r in imF]+[r[:] for r in imM])-rho
                if c==0: c0+=1
                elif c==1: c1+=1
                else: c2+=1
            results[(got,qq)]=(c0,c1,c2)
            print("[实例 #%d q=%2d] (5a)-候选: c=0: %3d ; c=1: %3d ; **c≥2: %3d**" % (got,qq,c0,c1,c2))
    print()
    tot2=sum(v[2] for v in results.values())
    print("全部 (q,实例) 组合中 c≥2 的总数：%d" % tot2)
    if tot2==0:
        print("\n⟹ 即使 q 增大，c≥2 也不出现 ⟹ (5a)+可实现 ⟹ c≤1 的实证更强 ✓")
    else:
        print("\n⟹ **c≥2 出现了！** ⟹ 需要重新审视")

if __name__=="__main__":
    main()
