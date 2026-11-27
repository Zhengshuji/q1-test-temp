r"""
c108_c_leq_1.py -- 决定性测试：(5a) 是否蕴涵 c := dim(imF+imM) − ρ ≤ 1 ？

若成立 ⟹ 结合 A25（c≥1）得 c=1 ⟹ 掉幅=1 ⟹ obs=ρ ⟹ 缺口闭合
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
    print("=== 决定性测试：(5a) ⟹ c ≤ 1 ？（c = dim(imF+imM) − ρ）===\n")
    n=4; rng=random.Random(606070)
    got=0; tot=0; c0=0; c1=0; cge2=0; t0=time.time()
    ex=None
    while got<8 and time.time()-t0<380:
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
        q=d+1; kk=q-1; npar=kk*mB
        pts=list(itertools.product([-1,0,1],repeat=npar)) if npar<=6 else \
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(300)]
        got+=1
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            rho=rk(A0)
            if rho==0: continue
            # imF = col space of A1 (q×d) ; imM = col space of A0
            imF=rowspace_basis([[A1[i][j] for i in range(q)] for j in range(d)])
            imM=rowspace_basis([[A0[i][j] for i in range(q)] for j in range(d)])
            dimsum=rk([r[:] for r in imF]+[r[:] for r in imM])
            c=dimsum-rho
            tot+=1
            if c==0: c0+=1
            elif c==1: c1+=1
            else:
                cge2+=1
                if ex is None:
                    ex=(A0,A1,rho,c)
                if cge2<=3: print("  **c=%d**  ρ=%d (5a)=True" % (c,rho))
    print()
    print("(5a)-候选 %d 个：c=0 有 %d ；c=1 有 %d ；**c≥2 有 %d**" % (tot,c0,c1,cge2))
    if cge2==0:
        print("\n⟹ *** (5a) ⟹ c ≤ 1 成立（全部候选）***")
        print("   结合 A25（(5b) ⟹ c≥1）得 c=1 ⟹ obs=ρ ⟹ **缺口闭合**")
    else:
        print("\n⟹ 存在 c≥2 的 (5a)-候选 ⟹ (5a) 不足；需检查这些候选是否满足 (5b)")
        A0,A1,rho,c=ex
        print("   例：ρ=%d c=%d" % (rho,c))
        print("   M =", [[str(x) for x in r] for r in A0])
        print("   F =", [[str(x) for x in r] for r in A1])
        print("   (5b) =", cond_5b(A0,A1))

if __name__=="__main__":
    main()
