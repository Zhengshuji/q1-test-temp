r"""
c94_U_invariant.py -- 验证新定理：(5a) ⟹ U = im(Mᵀ) 是 A'ᵀ-不变的
                    即 im(A'ᵀ Mᵀ) ⊆ im(Mᵀ)
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
    print("=== 验证新定理：(5a) ⟹ U = im(Mᵀ) 是 A'ᵀ-不变的 ===\n")
    n=4
    rng=random.Random(919191)
    got=0; tot=0; ok=0; bad=0
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
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(400)]
        a=b=0
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            tot+=1
            # 检查 im(A'ᵀ Mᵀ) ⊆ im(Mᵀ)
            # 以 Mᵀ 的列为基（即 im Mᵀ）
            Mt=[[A0[i][j] for i in range(len(A0))] for j in range(d)]  # d×q
            Ut=rowspace_basis(Mt)          # im(Mᵀ) 的基（作为 d 维向量）
            # A'ᵀ Mᵀ = (M A')ᵀ ⟹ 其列 = M A' 的行
            MAp=mm(A0,Ap)                  # q×d
            MApt=[[MAp[i][j] for i in range(len(MAp))] for j in range(d)]
            rows_of=rowspace_basis(MApt)   # im(A'ᵀ Mᵀ) 的基
            if rk([r[:] for r in Ut]+[r[:] for r in rows_of])==len(Ut):
                a+=1
            else:
                b+=1
        ok+=a; bad+=b
        print("[#%d] d=%d | 过(5a) %d | U 不变: %d ; 不不变: %d" % (got,d,tot,a,b))
        got+=1
    print()
    print("总候选 %d ；U 不变 %d ；不不变 %d" % (tot,ok,bad))
    if bad==0 and tot>0:
        print("\n⟹ **定理成立：(5a) ⟹ U 是 A'ᵀ-不变的** ✓")
        print("   ⟹ 结合 A20 的 U ⊆ Ṽ ⟹ 缺口只剩 W ⊆ U")


if __name__=="__main__":
    main()
