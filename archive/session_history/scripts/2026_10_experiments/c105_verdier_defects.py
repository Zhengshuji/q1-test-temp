r"""
c105_verdier_defects.py -- 实现 Verdier 约化链，计算缺陷 alpha_k

约化（Verdier Def 2.3）：
   V^(0) = im E = im M
   M^(k+1) = M^(k) ∩ A^{-1}(E M^(k))    (A = −F)
   V^(k+1) = E M^(k)
正则情形（(5b)）：
   alpha_k = dim V^(k−1) − 2 dim V^(k) + dim V^(k+1)

检验：
 1. 对所有解（(5a)∧(5b)）：alpha_1 = alpha_2 = 0 ？
 2. alpha_1 > 0 是否与 W ⊄ U 对应？
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

def nullspace_rows(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

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

def preimage(Fmat, S_basis, d):
    """F^{-1}(span(S_basis)) 的基（Fmat: q×d，S_basis: q 维向量列表）"""
    q=len(Fmat)
    # x 满足 Fx ∈ span(S_basis)
    # 即 Fx = S·c  ⟹  [F | -S]·(x,c)=0
    cols=d+len(S_basis)
    Mat=[]
    for i in range(q):
        row=[Fmat[i][j] for j in range(d)]+[-S_basis[t][i] for t in range(len(S_basis))]
        Mat.append(row)
    ker=nullspace_rows(Mat)
    out=[]
    for v in ker:
        x=v[:d]
        if any(y!=0 for y in x): out.append(x)
    return out

def verdier_V(Mmat, Fmat, d, kmax=4):
    """返回 [dim V^(0), dim V^(1), ...]"""
    V=[rowspace_basis(Mmat)]     # V^(0) = im M （Mmat: q×d ⟹ im = col space）
    # im M 的基：M 的列
    q=len(Mmat)
    Mb=rowspace_basis([[Mmat[i][j] for i in range(q)] for j in range(d)])   # im(M) 作为 q 维向量
    dims=[len(Mb)]
    Mbasis=Mb
    for k in range(kmax):
        # M^(k+1) = {x : Fx ∈ span(Mbasis)}
        Mbasis_v=[[Mbasis[t][i] for t in range(len(Mbasis))] for i in range(q)]  # hmm 需转置
        S=[ [Mbasis[t][i] for t in range(len(Mbasis))] for i in range(q) ]       # S[i] = i-th coord of basis vecs
        # preimage 需要 S_basis 为 q 维向量列表
        S_basis=Mbasis    # 每个是 q 维向量
        Mp=preimage(Fmat, S_basis, d)
        if not Mp: 
            dims.append(0); break
        # V^(k+1) = M(M^(k+1))
        Mp_rows=[[Mp[t][j] for j in range(d)] for t in range(len(Mp))]
        nb=rowspace_basis(Mm(mm(Mmat,[[]]))) if False else None
        # 直接算 M·x
        Mx=[[sum(Mmat[i][j]*x[j] for j in range(d)) for i in range(q)] for x in Mp]
        Mbasis2=rowspace_basis(Mx)
        dims.append(len(Mbasis2))
        Mbasis=Mbasis2
        if len(Mbasis2)==0: break
    return dims

def main():
    print("=== Verdier 缺陷计算：解是否满足 alpha_k = 0 ？ ===\n")
    n=4
    rng=random.Random(202030)
    got=0; t0=time.time()
    while got<5 and time.time()-t0<350:
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
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        R0b=rowspace_basis(R0)
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
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(200)]
        got+=1
        nsol=0; alphanonzero=0
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            if not cond_5b(A0,A1): continue
            nsol+=1
            if nsol>3: break
            dims=verdier_V(A0,[[-x for x in r] for r in A1],d,kmax=3)
            # dims = [dim V^(0), dim V^(1), ...]
            al=[]
            for k in range(1,len(dims)-1):
                al.append(dims[k-1]-2*dims[k]+dims[k+1])
            print("  解 #%d (ρ=%d): dim V^(k) = %s ; alpha = %s" % (nsol,rk(A0),dims,al))
            if any(a!=0 for a in al): alphanonzero+=1
        print("[实例 #%d] 解数 %d ；alpha≠0 的解 %d" % (got,nsol,alphanonzero))
        print()
    print("⟹ 若所有解 alpha=0，则与 Cor 8.8 一致（无 i.e.d.）✓")


if __name__=="__main__":
    main()
