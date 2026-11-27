r"""
c136_correct_algorithm.py -- 检验正确形式的算法

rho_min =? min_{r ∈ row(R0)} dim Φ^∞(span{α0, r})

对每个 r：构造 A_r，若 A_r ∩ row(R0) ≠ 0，则尝试 lift 并检查 (5a)(5b)。
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

def A_inf(seed,Nt,ANt,n,d,iters=12):
    Ab=rb(seed)
    for _ in range(iters):
        nb=rb(Ab+Phi(Nt,ANt,Ab,n,d))
        if len(nb)==len(Ab): break
        Ab=nb
    return Ab

def lift_rows(Ab,Nt,ANt,n,d):
    k=len(Ab); rows=[]
    for a in Ab:
        Amat=[]; bv=[]
        for tt in range(d):
            Amat.append([Nt[tt][i] for i in range(n)]+[Fr(0)]*k); bv.append(a[tt])
        for tt in range(d):
            Amat.append([ANt[tt][i] for i in range(n)]+[-Ab[i][tt] for i in range(k)]); bv.append(Fr(0))
        s=solve(Amat,bv)
        if s is None: return None
        rows.append(s[:n])
    return rows

def main():
    print("=== 正确形式：A_r = Φ^∞(span{α0,r}) ===\n")
    n=6; p=2
    tested=0; tried=0; succ=0
    bestdims=[]
    for t in range(1,120):
        rng=random.Random(7770000+t)
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
        tested+=1
        got=False
        # r 取 row(R0) 的基 + 一些组合
        cands=[R0row[0]]
        if len(R0row)>1: cands.append(R0row[1])
        cands.append(a0)
        cands.append([a0[i]+R0row[0][i] for i in range(d)])
        if len(R0row)>1:
            cands.append([a0[i]+R0row[1][i] for i in range(d)])
        best=99
        for r in cands:
            if all(v==0 for v in r): continue
            Ar=A_inf([a0,r],Nt,ANt,n,d)
            if not Ar: continue
            inter=rb([v for v in Ar if rk(R0row+[v])==len(R0row)])
            if not inter: continue
            best=min(best,len(Ar))
            rows=lift_rows(Ar,Nt,ANt,n,d)
            if rows is None: continue
            tried+=1
            q=len(rows)
            M=[[sum([rows[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
            LA=[[sum([rows[i][j]*A[j][k2] for j in range(n)],Fr(0)) for k2 in range(n)] for i in range(q)]
            F=[[sum([LA[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
            K=ker_basis(M)
            ok5a=(not K or not K[0]) or rk(mm(F,K))==0
            if ok5a and cond_5b(M,F):
                succ+=1; got=True; break
        if best<99: bestdims.append(best)
    print("检验 %d 个实例；尝试 %d 次构造；成功 %d" % (tested,tried,succ))
    print("A_r 的最小维数分布：", sorted(set(bestdims))[:10] if bestdims else "—")
    print()
    if tried>0 and succ>0:
        print("⟹ *** 正确形式的算法能产出解（%d 次成功）*** ✓" % succ)
    elif tried>0:
        print("⟹ 仍未成功（需进一步检查）")

if __name__=="__main__":
    main()
