r"""
c130_intersection_basis.py -- 修正版判据检验：直接算 W ∩ row(R0) 的基

对交集基的每个向量（及其小幅倍数）尝试构造，验证 ρ=1 与 (5a)(5b)。
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

def nullsp_rows(M):
    """M 的行给出的齐次方程组的解空间（每个解是一行）"""
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

def intersect_basis(Wb, Vb, d):
    """W∩V 的基（都是 d 维行向量的基）；用 c,d 系数： sum c_i W_i = sum d_j V_j"""
    k=len(Wb); m=len(Vb)
    if k==0 or m==0: return []
    # 方程： sum_i c_i W_i - sum_j d_j V_j = 0  (d 个方程，k+m 未知)
    Amat=[]
    for t in range(d):
        row=[Wb[i][t] for i in range(k)]+[-Vb[j][t] for j in range(m)]
        Amat.append(row)
    sols=nullsp_rows(Amat)   # 每个解是 k+m 向量
    out=[]
    for s in sols:
        c=s[:k]
        x=[sum(c[i]*Wb[i][t] for i in range(k)) for t in range(d)]
        if any(v!=0 for v in x): out.append(x)
    return rb(out)

def main():
    print("=== 修正版：用交集基构造 ===\n")
    n=7; p=2
    both=0; onlyW=0; onlySucc=0; neither=0
    for t in range(1,150):
        rng=random.Random(9970000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mr=Cc+CA
        if rk(Mr)!=4: continue
        N=ker_basis(Mr)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=3: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        if rk(R0)==0: continue
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]
        perp=nullsp_rows(ANt)
        W=rb(mm(perp,N)) if perp else []
        R0row=rb(R0)
        I=intersect_basis(W,R0row,d)
        pred = len(I)>0
        succ=False
        if pred:
            for base in I:
                for mult in (1,-1,2,-2,3,-3):
                    a0=[mult*base[j] for j in range(d)]
                    Amat=[]; bv=[]
                    for j in range(d):
                        Amat.append([N[i][j] for i in range(n)]); bv.append(a0[j])
                    for j in range(d):
                        Amat.append([AN[i][j] for i in range(n)]); bv.append(Fr(0))
                    s=solve(Amat,bv)
                    if s is None: continue
                    A2m=[]; b2=[]
                    for j in range(d):
                        A2m.append([N[i][j] for i in range(n)]); b2.append(Fr(0))
                    for j in range(d):
                        A2m.append([AN[i][j] for i in range(n)]); b2.append(a0[j])
                    l1=solve(A2m,b2)
                    if l1 is None: continue
                    Lam=[s, l1]
                    M=mm(Lam,N); F=mm(mm(Lam,A),N)
                    rho=rk(M)
                    K=ker_basis(M)
                    ok5a=(not K or not K[0]) or rk(mm(F,K))==0
                    ok5b=cond_5b(M,F)
                    if rho==1 and ok5a and ok5b:
                        succ=True; break
                if succ: break
        if pred and succ: both+=1
        elif pred and not succ: onlyW+=1
        elif (not pred) and succ: onlySucc+=1
        else: neither+=1
    print("预测有 ∧ 构造成功 : %d" % both)
    print("预测有 ∧ 构造失败 : %d" % onlyW)
    print("预测无 ∧ 构造成功 : %d  ← 若 >0 则判据错" % onlySucc)
    print("预测无 ∧ 构造失败 : %d" % neither)
    print()
    if onlySucc==0 and onlyW==0:
        print("⟹ *** 判据完全吻合 *** ✓")
    elif onlySucc==0:
        print("⟹ 必要性无反例；充分性缺口 %d" % onlyW)
    else:
        print("⟹ 判据错 ✗")

if __name__=="__main__":
    main()
