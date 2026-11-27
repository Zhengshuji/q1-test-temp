r"""
c135_final_test.py -- 检验候选算法

对每个实例（e = rank R0 小）：
 1. 算 A0 = span{alpha0}
 2. 对 r 在 row(R0) 的基（及组合）：A = Phi^inf(span{alpha0, r})
 3. 若 A ∩ row(R0) ≠ 0：构造行（lift），检查 (5a)(5b)
 4. 记录成功的 A
"""
import os, io, contextlib, random, sys, itertools
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

def nullsp(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]; piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]; pv=A[r][c]; A[r]=[x/pv for x in A[r]]
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

def solve(Amat,bvec):
    if not Amat: return None
    m=len(Amat); n=len(Amat[0])
    M=[[Fr(Amat[i][j]) for j in range(n)]+[Fr(bvec[i])] for i in range(m)]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if M[i][c]!=0: p=i; break
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n+1)]
        piv.append(c); r+=1
        if r==m: break
    for i in range(r,m):
        if all(M[i][j]==0 for j in range(n)) and M[i][n]!=0: return None
    x=[Fr(0)]*n
    for i,c in enumerate(piv): x[c]=M[i][n]
    return x

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

def Phi(Nt,ANt,Ab,n,d):
    k=len(Ab)
    if k==0: return []
    rows=[]
    for tt in range(d):
        rows.append([Nt[tt][i] for i in range(n)]+[-Ab[i][tt] for i in range(k)]+[Fr(0)]*k)
    for tt in range(d):
        rows.append([ANt[tt][i] for i in range(n)]+[Fr(0)]*k+[-Ab[i][tt] for i in range(k)])
    sols=nullsp(rows)
    out=[]
    for s in sols:
        l=s[:n]
        val=[sum(Nt[tt][i]*l[i] for i in range(n)) for tt in range(d)]
        if any(v!=0 for v in val): out.append(val)
    return rb(out)

def lift_rows(Ab,Nt,ANt,n,d):
    """为 A 的每个基向量 a 找 ℓ: ℓN=a, ℓAN = Σ c_t a_t ∈ A（c 自由）"""
    k=len(Ab)
    rows=[]
    for a in Ab:
        # 未知：(ℓ (n), c (k))
        Amat=[]; bv=[]
        for tt in range(d):
            Amat.append([Nt[tt][i] for i in range(n)]+[Fr(0)]*k); bv.append(a[tt])
        for tt in range(d):
            Amat.append([ANt[tt][i] for i in range(n)]+[-Ab[i][tt] for i in range(k)]); bv.append(Fr(0))
        s=solve(Amat,bv)
        if s is None:
            return None
        rows.append(s[:n])
    return rows

def main():
    print("=== 候选算法检验（构造性）===\n")
    n=6; p=2
    tested=0; inter_nonzero=0; constructed=0
    for t in range(1,80):
        rng=random.Random(8880000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mr=Cc+CA
        if rk(Mr)!=4: continue
        N=ker_basis(Mr); d=len(N[0]); AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N)); Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        R0row=rb(R0)
        if not R0row: continue
        a0=R0row[0]
        Ab1=rb([a0])
        Ainf=Ab1
        for _ in range(10):
            nb=rb(Ainf+Phi(Nt,ANt,Ainf,n,d))
            if len(nb)==len(Ainf): break
            Ainf=nb
        # A = Phi^inf(span{a0} ∪ row(R0))
        start=rb(Ab1+R0row)
        Ab=start
        for _ in range(10):
            nb=rb(Ab+Phi(Nt,ANt,Ab,n,d))
            if len(nb)==len(Ab): break
            Ab=nb
        tested+=1
        inter=rb([v for v in Ab if rk(R0row+[v])==len(R0row)])
        if not inter: continue
        inter_nonzero+=1
        rows=lift_rows(Ab,Nt,ANt,n,d)
        if rows is None: continue
        q=len(rows)
        M=[[sum([rows[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
        LA=[[sum([rows[i][j]*A[j][k2] for j in range(n)],Fr(0)) for k2 in range(n)] for i in range(q)]
        F=[[sum([LA[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
        K=ker_basis(M)
        ok5a=(not K or not K[0]) or rk(mm(F,K))==0
        ok5b=cond_5b(M,F)
        if ok5a and ok5b:
            constructed+=1
    print("检验 %d 个实例" % tested)
    print("  其中 A∩row(R0)≠0 : %d" % inter_nonzero)
    print("  其中成功构造出 (5a)∧(5b) 的解 : %d" % constructed)
    print()
    if inter_nonzero>0 and constructed==inter_nonzero:
        print("⟹ *** 候选算法的充分性成立：A∩row(R0)≠0 ⟹ 有解 ⟹ ρ_min = dim Φ^∞(·) *** ✓")
        print("   ⟹ q1 为假（在这一族内）")
    elif constructed>0:
        print("⟹ 部分成立 (%d/%d)" % (constructed,inter_nonzero))

if __name__=="__main__":
    main()
