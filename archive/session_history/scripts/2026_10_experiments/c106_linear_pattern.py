r"""
c106_linear_pattern.py -- 验证：解是否总有 dim V^(k) = max(ρ−k, 0)？

若成立 ⟹ α_k = 0 ⟹ 无 i.e.d. ⟹ 缺口闭合
并检查：(5a)-only 的反例是否破坏该模式
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

def preimage(Fmat, S_basis, d, q):
    cols=d+len(S_basis) if S_basis else d
    Mat=[]
    for i in range(q):
        row=[Fmat[i][j] for j in range(d)]
        for s in S_basis: row.append(-s[i])
        Mat.append(row)
    ker=nullspace_rows(Mat)
    out=[]
    for v in ker:
        x=v[:d]
        if any(y!=0 for y in x): out.append(x)
    return out

def verdier_dims(Mmat, Fmat, d, q, kmax=5):
    Mb=rowspace_basis([[Mmat[i][j] for i in range(q)] for j in range(d)])
    dims=[len(Mb)]
    for k in range(kmax):
        if not Mb: break
        Mp=preimage(Fmat, Mb, d, q)
        if not Mp: dims.append(0); break
        Mx=[[sum(Mmat[i][j]*x[j] for j in range(d)) for i in range(q)] for x in Mp]
        Mb=rowspace_basis(Mx)
        dims.append(len(Mb))
    return dims

def main():
    print("=== 验证 dim V^(k) = max(ρ−k,0) ===\n")
    n=4; rng=random.Random(404050)
    got=0; tot=0; okpat=0; badpat=0; t0=time.time()
    # 同时收集 (5a)-only 反例的模式
    bad5a=0; bad5a_pat=0
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
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(150)]
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
            negF=[[-x for x in r] for r in A1]
            dims=verdier_dims(A0,negF,d,q,kmax=4)
            pred=[max(rho-k,0) for k in range(len(dims))]
            is5b=cond_5b(A0,A1)
            if is5b:
                tot+=1
                if dims==pred: okpat+=1
                else:
                    badpat+=1
                    if badpat<=3: print("  **解但模式不符** ρ=%d dims=%s pred=%s" % (rho,dims,pred))
            else:
                # (5a)-only
                bad5a+=1
                if dims==pred: bad5a_pat+=1
                if bad5a<=2: print("  [(5a)-only] ρ=%d dims=%s pred=%s" % (rho,dims,pred))
    print()
    print("解 %d 个；**模式 dim V^(k)=max(ρ−k,0) 成立 %d ；不符 %d**" % (tot,okpat,badpat))
    print("(5a)-only 候选 %d 个；其中模式成立 %d" % (bad5a,bad5a_pat))
    if badpat==0 and tot>0:
        print("\n⟹ *** 所有解满足 dim V^(k)=ρ−k ⟹ α_k=0 ⟹ 无 i.e.d. ***")
        print("   这支持缺口，并把待证的事变成：证明该线性模式")

if __name__=="__main__":
    main()
