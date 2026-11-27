r"""
c132_monotone.py -- 检验单调性：ρ≤1 失败时，2 维 A 能否满足 (5b)？

对 d=3 的实例：
 1. 检查 ρ≤1 判据（L0 ∈ S 且 (u,w) 像 2 维）
 2. 若失败，枚举 2 维 A ⊇ span{α0}（用 β 参数化）
 3. 对每个 A：检查 Φ(A)=A（行能张成 A）且 (5a)(5b) 满足
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

def in_A(vec, Abasis):    # vec ∈ span(Abasis)?
    if not vec or all(v==0 for v in vec): return True
    return rk([r[:] for r in Abasis]+[vec])==len(Abasis)

def S_A(Nt, ANt, Abasis, n, d):
    """{ℓ : ℓN ∈ A, ℓAN ∈ A} 的基（每个是 n 维向量）"""
    k=len(Abasis)
    nv=n+2*k
    Amat=[]
    for tt in range(d):
        Amat.append([Nt[tt][i] for i in range(n)]+[-Abasis[i][tt] for i in range(k)]+[Fr(0)]*k)
    for tt in range(d):
        Amat.append([ANt[tt][i] for i in range(n)]+[Fr(0)]*k+[-Abasis[i][tt] for i in range(k)])
    sols=nullsp(Amat)
    return [s[:n] for s in sols]

def main():
    print("=== 单调性检验：ρ≤1 失败时 2 维 A 能救吗？ ===\n")
    n=7; p=2
    tested=0; fails_rho1=0; rescued=0
    for t in range(1,60):
        rng=random.Random(9995000+t)
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
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        R0row=rb(R0)
        if not R0row: continue
        # 取 L0 使 alpha0 = R0row[0]
        # 解 L0 N = a0
        a0=R0row[0]
        Amat=[[N[i][j] for i in range(n)] for j in range(d)]
        bv=[a0[j] for j in range(d)]
        # 简单求解
        M2=[[Fr(Amat[i][j]) for j in range(n)]+[Fr(bv[i])] for i in range(d)]
        piv=[]; r=0
        for c in range(n):
            p2=None
            for i in range(r,d):
                if M2[i][c]!=0: p2=i; break
            if p2 is None: continue
            M2[r],M2[p2]=M2[p2],M2[r]; pv=M2[r][c]; M2[r]=[x/pv for x in M2[r]]
            for i in range(d):
                if i!=r and M2[i][c]!=0:
                    ff=M2[i][c]; M2[i]=[M2[i][j]-ff*M2[r][j] for j in range(n+1)]
            piv.append(c); r+=1
            if r==d: break
        bad=False
        for i in range(r,d):
            if all(M2[i][j]==0 for j in range(n)) and M2[i][n]!=0: bad=True
        if bad: continue
        L0=[Fr(0)]*n
        for i,c in enumerate(piv): L0[c]=M2[i][n]
        if all(x==0 for x in L0): continue
        # rho≤1 判据
        Ab1=rb([a0])
        SA=S_A(Nt,ANt,Ab1,n,d)
        pairs=[]
        for l in SA:
            val=[sum(Nt[t2][i]*l[i] for i in range(n)) for t2 in range(d)]
            # val = u*a0
            # 求 u
            j0=next((j for j in range(d) if a0[j]!=0), None)
            if j0 is None: continue
            u=val[j0]/a0[j0]
            val2=[sum(ANt[t2][i]*l[i] for i in range(n)) for t2 in range(d)]
            w=val2[j0]/a0[j0]
            pairs.append((u,w))
        dim_img = rk([[pairs[i][0],pairs[i][1]] for i in range(len(pairs))]) if pairs else 0
        rho1_ok = (len(Ab1)==1) and dim_img==2
        tested+=1
        if rho1_ok: continue
        fails_rho1+=1
        # 尝试 2 维 A = span{a0, β}
        found=False
        for trial in range(40):
            rr=random.Random(31337*t+trial)
            beta=[Fr(rr.randint(-2,2)) for _ in range(d)]
            Ab2=rb([a0,beta])
            if len(Ab2)!=2: continue
            SA2=S_A(Nt,ANt,Ab2,n,d)
            if not SA2: continue
            # Φ(A)=A? 即 {ℓN : ℓ∈S_A} 张成 A
            imgs=[]
            for l in SA2:
                val=[sum(Nt[t2][i]*l[i] for i in range(n)) for t2 in range(d)]
                imgs.append(val)
            Phi=rb(imgs) if imgs else []
            if len(Phi)!=2: continue
            # 造 rows：取 S_A 的两个行，要求其 N-像独立
            rows=[]
            for l in SA2:
                rows.append(l)
                if len(rows)>=2:
                    Ms=mm(rows,N)
                    if rk(Ms)==2: break
            if len(rows)<2: continue
            Ms=mm(rows,N); Fs=mm([[sum(rows[i][j]*A[j][k2] for j in range(n)) for k2 in range(n)] for i in range(2)],N)
            if rk(Ms)!=2: continue
            K=ker_basis(Ms)
            ok5a=(not K or not K[0]) or rk(mm(Fs,K))==0
            ok5b=cond_5b(Ms,Fs)
            if ok5a and ok5b:
                found=True; break
        if found: rescued+=1
    print("检验实例 %d ；其中 ρ≤1 失败 %d ；被 2 维 A 救回 %d" % (tested,fails_rho1,rescued))
    if fails_rho1>0 and rescued>0:
        print("\n⟹ *** 非单调！2 维 A 能救 ⟹ 需 Grassmann 搜索 ⟹ q1 可能为真 ***")
    elif fails_rho1>0:
        print("\n⟹ 未发现救回（样本小，不能断言单调）")

if __name__=="__main__":
    main()
