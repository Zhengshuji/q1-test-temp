r"""
c37_c19_check.py -- 验证 c19（531,441 全枚举无解）的 α0∈V 状态

【判据】YES ⟺ α0 = L0N ∈ V = <row(R)>_{A'}
  c19 无解 ⟹ 判据应预测 α0 ∉ V
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

def row_space_basis(M):
    m_rows=len(M); ncols=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(ncols):
        p=None
        for i in range(r,m_rows):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m_rows):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(ncols)]
        piv.append(r); r+=1
        if r==m_rows: break
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
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def invariant_closure(M, Ap, d):
    basis = row_space_basis(M)
    cur = [r[:] for r in basis]
    while len(basis) < d:
        cur = mm(cur, Ap)
        new = rk(basis + [r[:] for r in cur])
        if new == len(basis):
            break
        basis = basis + [r[:] for r in cur]
    return row_space_basis(basis)

def in_span(basis, v):
    if not basis:
        return all(x==0 for x in v)
    return rk([r[:] for r in basis] + [v[:]]) == len(basis)


def main():
    print("=== c19 实例的 α0∈V 检查 ===\n")
    n=5; seed=123450+n; target=4
    rng=random.Random(seed)
    found=None
    for trial in range(200000):
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
        L0=None
        for _x in range(40):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
            if all(x==0 for x in pv): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        try:
            _Lx,eta=p1(A,Cc,L0)
        except Exception:
            continue
        if not eta: continue
        if trial==target:
            found=(A,Cc,L0,N,d); break
    if found is None:
        print("未复现"); return
    A,Cc,L0,N,d=found
    AN=mm(A,N)
    Nt=[[N[i][j] for i in range(n)] for j in range(d)]
    iNtN=minv(mm(Nt,N))
    Ap=mm(mm(iNtN,Nt),AN)
    NAp=mm(N,Ap)
    R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
    Rrow=row_space_basis(R); e=len(Rrow)
    V=invariant_closure(R, Ap, d)
    a0=mm(L0,N)
    a0in = in_span(V, a0[0])
    print("n=5 t=4（c19 的实例）：d=%d  dim row(R)=%d  **obs=dim V=%d**" % (d,e,len(V)))
    print("α0 = L0N = %s" % [str(x) for x in a0[0]])
    print("V 的基 = %s" % [[str(x) for x in r] for r in V])
    print()
    print("**α0 ∈ V ？ %s**" % ("是" if a0in else "**否**"))
    print()
    print("【判据预测】", end="")
    if a0in:
        print("YES —— 但 c19 在 531,441 全枚举上**无解** ⟹ **判据被反驳** ✗")
    else:
        print("NO —— 与 c19 的 531,441 全枚举无解 **一致** ✓✓")


if __name__=="__main__":
    main()
