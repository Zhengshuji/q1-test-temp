r"""
c53_rho_gt_obs.py -- 验证引理：ρ > obs ⟹ U ∩ V^⊥ ≠ 0

【证明（2 行维数计数）】
   dim ker H = d − ρ；dim V = obs
   ρ > obs ⟹ dim(ker H + V) ≤ (d−ρ) + obs < d
   ⟹ (ker H + V)^⊥ ≠ 0
   而 (ker H+V)^⊥ = (ker H)^⊥ ∩ V^⊥ = row(H) ∩ V^⊥ = U ∩ V^⊥   ✓
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

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
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def invariant_closure(M, Ap, d):
    basis=rowspace_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d and basis:
        cur=mm(cur,Ap)
        if rk(basis+[r[:] for r in cur])==len(basis): break
        basis=basis+[r[:] for r in cur]
    return rowspace_basis(basis)

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
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def nullspace(M):
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
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

def solve_row(Mat, rhs):
    n=len(Mat); m=len(Mat[0])
    A2=[[Fr(Mat[i][j]) for i in range(n)]+[Fr(rhs[j])] for j in range(m)]
    rows=len(A2); cols=n+1
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,rows):
            if A2[i][c]!=0: p=i; break
        if p is None: continue
        A2[r],A2[p]=A2[p],A2[r]
        pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
        for i in range(rows):
            if i!=r and A2[i][c]!=0:
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[r][j] for j in range(cols)]
        piv.append(c); r+=1
        if r==rows: break
    for i in range(r,rows):
        if all(A2[i][j]==0 for j in range(n)) and A2[i][n]!=0:
            return None
    x=[Fr(0)]*n
    for i,c in enumerate(piv): x[c]=A2[i][n]
    return x


def main():
    print("=== 验证：ρ > obs ⟹ U ∩ V^⊥ ≠ 0 ===\n")
    print("%-14s %3s %5s %6s %9s %8s" % ("实例","d","obs","ρ","dim(U∩V⊥)","判定"))
    print("-"*54)
    ok=0; tot=0
    for (n,seed) in [(4,555000),(5,70065)]:
        rng=random.Random(seed)
        got=0; t=0
        for trial in range(200000):
            if got>=5: break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
            d=len(N[0])
            if d<3: continue
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            V=invariant_closure(R, Ap, d)
            obs=len(V)
            if obs>=d: continue
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
            try:
                _Lx,eta=p1(A,Cc,L0)
            except Exception:
                continue
            if not eta: continue
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=rowspace_basis(Mcol); mB=len(resB)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            q=d+1; kk=q-1
            # 取几个候选（含高 rank 的）
            rng2=random.Random(11+97*trial+n)
            for _try in range(60):
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(kk)]
                A0=[H0[0][:]]; A1=[F0[0][:]]
                for z in rr:
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                rho=rk(A0)
                if rho<=obs: continue
                U=rowspace_basis(A0)
                Vp=nullspace(V)          # V^⊥ 的基（行向量）
                inter=rowspace_basis(U+Vp) if Vp else U
                dint=rk([r[:] for r in U]+[r[:] for r in Vp])-len(Vp) if Vp else len(U)
                # 更稳：交集维数 = dim U + dim V⊥ − dim(U+V⊥)
                dimVp=d-obs
                dsum=rk([r[:] for r in U]+[r[:] for r in Vp])
                dint=len(U)+dimVp-dsum
                tot+=1
                okk = (dint>0)
                if okk: ok+=1
                print("%-14s %3d %5d %6d %9d %8s" %
                      ("n=%d t=%d"%(n,trial), d, obs, rho, dint, "✓" if okk else "**✗**"))
                got+=1
                if got>=5: break
            if got>=5: break
        print()
    print("总 %d ；满足 dim(U∩V⊥)>0 的 %d 个" % (tot,ok))
    if ok==tot and tot>0:
        print("\n⟹ **引理成立**：ρ > obs ⟹ U ∩ V^⊥ ≠ 0  ✓")


if __name__=="__main__":
    main()
