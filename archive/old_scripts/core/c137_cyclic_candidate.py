r"""
c137_cyclic_candidate.py -- 新候选：rho_min =? min over s in S of dim(A' - cyclic space of {alpha0, s})

对每个实例：
 1. S = row(R0)
 2. 对 s 在 S 的基（及组合）：算 A'-闭包 A_s = span{(alpha0)A'^i, sA'^i}
 3. 检查 admissible： A_s A' subset A_s + S
 4. 检查 A_s ∩ S ≠ 0
 5. 尝试 lift 构造 (a)(b)，记录 rho
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

def Aclosure(seed,Ap,d):
    """seed: 若干行向量；返回它们在 A' 下的闭包基（行右乘 A'）"""
    B=rb(seed)
    while True:
        newB=rb(B+mm(B,Ap))
        if len(newB)==len(B): return B
        B=newB

def main():
    print("=== 新候选：A'-循环空间 ===\n")
    n=6; p=2
    tested=0; candidates_ok=0; solutions=0; got_b=0
    for t in range(1,80):
        rng=random.Random(6540000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mr=Cc+CA
        if rk(Mr)!=4: continue
        N=ker_basis(Mr); d=len(N[0]); AN=mm(A,N)
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        S=rb(R0)
        if not S: continue
        # 取 L0 使 alpha0 != 0
        L0=None
        for _ in range(60):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            a0=mm(cand,N)[0]
            if all(x==0 for x in a0): continue
            L0=cand; break
        if L0 is None: continue
        a0=mm(L0,N)[0]
        tested+=1
        # 候选 s：S 的基 + 组合
        cands=[s[:] for s in S]
        if len(S)>=2:
            cands.append([S[0][i]+S[1][i] for i in range(d)])
        best=None
        for s in cands:
            if all(v==0 for v in s): continue
            # A_s = A'-闭包 of {alpha0, s}
            As=Aclosure([a0,s],Ap,d)
            if len(As)==0: continue
            # admissible?
            lhs=rb([r[:] for r in As]+[r[:] for r in mm(As,Ap)]+[r[:] for r in S])
            rhs=rb([r[:] for r in As]+[r[:] for r in S])
            if len(lhs)!=len(rhs): continue
            # A_s ∩ S ≠ 0 ?
            if not rb([v for v in As if rk(S+[v])==len(S)]): continue
            candidates_ok+=1
            if best is None or len(As)<best: best=len(As)
        if best is not None:
            solutions+=1
        # === 检查 (b) ===
        for s in cands:
            if all(v==0 for v in s): continue
            As=Aclosure([a0,s],Ap,d)
            if not As: continue
            lhs=rb([r[:] for r in As]+[r[:] for r in mm(As,Ap)]+[r[:] for r in S])
            rhs=rb([r[:] for r in As]+[r[:] for r in S])
            if len(lhs)!=len(rhs): continue
            if not rb([v for v in As if rk(S+[v])==len(S)]): continue
            # lift
            k=len(As); rows=[]
            okk=True
            for a in As:
                Amat=[]; bv=[]
                for tt in range(d):
                    Amat.append([Nt[tt][i] for i in range(n)]+[Fr(0)]*k); bv.append(a[tt])
                for tt in range(d):
                    Amat.append([ANt[tt][i] for i in range(n)]+[-As[i][tt] for i in range(k)]); bv.append(Fr(0))
                sp=solve(Amat,bv)
                if sp is None: okk=False; break
                rows.append(sp[:n])
            if not okk: continue
            q=len(rows)
            M=[[sum([rows[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
            LA=[[sum([rows[i][j]*A[j][k2] for j in range(n)],Fr(0)) for k2 in range(n)] for i in range(q)]
            F=[[sum([LA[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
            K=ker_basis(M)
            ok5a=(not K or not K[0]) or rk(mm(F,K))==0
            if ok5a and cond_5b(M,F):
                got_b+=1
                break
    print("检验 %d 个实例" % tested)
    print("  找到合格 A_s（admissible + 交非零）的实例：%d" % solutions)
    print("  其中 A_s 数：%d" % candidates_ok)
    print("  **其中 (a)∧(b) 成立的实例：%d**" % got_b)
    print()
    print("注：这只验证了\"候选存在\"，还需检查 (b) 是否可满足（下一步）")

if __name__=="__main__":
    main()
