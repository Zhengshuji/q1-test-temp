r"""
c46_why_5a_fails.py -- 具体检查：α0∉V 时 rank-1 候选为何过不了 (5a)

【已知】ρ=obs=1 时，U = span(α_i) = span(α0)（因 α0∈U 且 dim U=1）
   ⟹ (5a) 迫使 γ0 ∈ span(α0)
   ⟹ 需 α0A' ∈ span(α0) + W0 （W0 = row R）

【本脚本】打印具体数值，看是哪一步断掉
"""
import os, io, contextlib, random, itertools, time
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

def row_space_basis(M):
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
    basis=row_space_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d and basis:
        cur=mm(cur,Ap)
        if rk(basis+[r[:] for r in cur])==len(basis): break
        basis=basis+[r[:] for r in cur]
    return row_space_basis(basis)

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

def in_span(basis, v):
    if not basis:
        return all(x==0 for x in v)
    return rk([r[:] for r in basis]+[v[:]])==len(basis)


def main():
    print("=== α0∉V 时 rank-1 候选为何失败：具体数值 ===\n")
    n=4
    rng=random.Random(555000)
    t_all=time.time()
    for trial in range(5000):
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
        if d<2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        V=invariant_closure(R, Ap, d)
        if len(V)>=d: continue
        a0=None
        for _try in range(30):
            cand=[Fr(rng.randint(-2,2)) for _ in range(d)]
            if all(x==0 for x in cand): continue
            if rk([r[:] for r in V]+[cand])>len(V):
                a0=cand; break
        if a0 is None: continue
        L0=solve_row(N, a0)
        if L0 is None: continue
        L0=[L0]
        if rk(L0+Cc)!=2: continue
        try:
            _Lx,eta=p1(A,Cc,L0)
        except Exception:
            continue
        if not eta: continue
        # 找到了一个 (obs<d, α0∉V) 的实例
        W0=row_space_basis(R)
        print("实例 trial=%d:  d=%d  obs=%d  dim W0=%d" % (trial,d,len(V),len(W0)))
        print("  α0 = %s" % [str(x) for x in a0])
        print("  V  = %s" % [[str(x) for x in r] for r in V])
        print("  W0 = %s" % [[str(x) for x in r] for r in W0])
        a0Ap=[sum(a0[i]*Ap[i][j] for i in range(d)) for j in range(d)]
        print("  α0·A' = %s" % [str(x) for x in a0Ap])
        print()
        print("  **关键检验**：α0A' ∈ span(α0) + W0 ？")
        basis_plus=[a0[:]]+[r[:] for r in W0]
        print("     span(α0)+W0 的维数 = %d（d=%d）" % (rk(basis_plus), d))
        print("     α0A' ∈ 其中？ **%s**" % ("是" if in_span(basis_plus, a0Ap) else "**否**"))
        print()
        print("  ⟹ 若是「否」：ρ=obs=1 时 U=span(α0)，(5a) 要求 γ0∈U")
        print("     而 γ0 = α0A' + β0（β0∈W0）⟹ 需 α0A'∈span(α0)+W0 ⟹ **不可能** ✓ 机制确认")
        print()
        break
    print("（用时 %.1f s）" % (time.time()-t_all))


if __name__=="__main__":
    main()
