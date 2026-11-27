r"""
c133_monotone_fixed.py -- 单调性检验（修正版）

对 d=3 实例：若 ρ≤1 失败，枚举 2 维 A ⊇ span{α0}，检查能否得到 (5a)∧(5b) 的解。
关键修正：从 S_A 中按 N-像的秩贪心选行。
"""
import os, io, contextlib, random, sys
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

def SA_basis(Nt,ANt,Ab,k,n,d):
    """{ℓ : ℓN ∈ A, ℓAN ∈ A} 的基"""
    rows=[]
    for tt in range(d):
        rows.append([Nt[tt][i] for i in range(n)]+[-Ab[i][tt] for i in range(k)]+[Fr(0)]*k)
    for tt in range(d):
        rows.append([ANt[tt][i] for i in range(n)]+[Fr(0)]*k+[-Ab[i][tt] for i in range(k)])
    sols=nullsp(rows)
    return [s[:n] for s in sols]

def make_solution(rows, A, N, n):
    """由 rows 构造 M=rows·N, F=rows·A·N"""
    q=len(rows)
    M=[[sum([rows[i][j]*N[j][k2] for j in range(n)], Fr(0)) for k2 in range(len(N[0]))] for i in range(q)]
    LA=[[sum(rows[i][j]*A[j][k2] for j in range(n)) for k2 in range(n)] for i in range(q)]
    F=[[sum(LA[i][j]*N[j][k2] for j in range(n)) for k2 in range(len(N[0]))] for i in range(q)]
    return M,F

def main():
    print("=== 单调性检验（修正版） ===\n")
    n=7; p=2
    tested=0; fails1=0; rescued=0; details=[]
    for t in range(1,50):
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
        # 取 a0 = R0row[0]，构造 L0 (L0 N = a0)
        a0=R0row[0]
        # solve
        # N 是 n×d；要 ℓ·N = a0 → 方程 Σ_i ℓ_i N[i][j] = a0[j]
        M2=[[Fr(N[i][j]) for i in range(n)]+[Fr(a0[j])] for j in range(d)]
        piv=[]; r=0
        ok=True
        for c in range(n):
            pp=None
            for i in range(r,d):
                if M2[i][c]!=0: pp=i; break
            if pp is None: continue
            M2[r],M2[pp]=M2[pp],M2[r]; pv=M2[r][c]; M2[r]=[x/pv for x in M2[r]]
            for i in range(d):
                if i!=r and M2[i][c]!=0:
                    ff=M2[i][c]; M2[i]=[M2[i][j]-ff*M2[r][j] for j in range(n+1)]
            piv.append(c); r+=1
            if r==d: break
        for i in range(r,d):
            if all(M2[i][j]==0 for j in range(n)) and M2[i][n]!=0: ok=False
        if not ok: continue
        L0=[Fr(0)]*n
        for i,c in enumerate(piv): L0[c]=M2[i][n]
        if all(x==0 for x in L0): continue
        # ρ≤1 检验
        Ab1=rb([a0])
        SA1=SA_basis(Nt,ANt,Ab1,1,n,d)
        pairs=[]
        j0=next((j for j in range(d) if a0[j]!=0), None)
        if j0 is None: continue
        for l in SA1:
            val=[sum(Nt[t2][i]*l[i] for i in range(n)) for t2 in range(d)]
            val2=[sum(ANt[t2][i]*l[i] for i in range(n)) for t2 in range(d)]
            pairs.append((val[j0]/a0[j0], val2[j0]/a0[j0]))
        dimg=rk([[pairs[i][0],pairs[i][1]] for i in range(len(pairs))]) if pairs else 0
        rho1 = (dimg==2)
        tested+=1
        if rho1: continue
        fails1+=1
        # 尝试 2 维 A
        got=False
        for trial in range(60):
            rr=random.Random(777*t+trial)
            beta=[Fr(rr.randint(-2,2)) for _ in range(d)]
            Ab2=rb([a0,beta])
            if len(Ab2)!=2: continue
            S2=SA_basis(Nt,ANt,Ab2,2,n,d)
            if not S2: continue
            # 贪心选行使 rank(ℓN) 最大
            chosen=[]; cur=[]
            for l in S2:
                cand=chosen+[l]
                imgs=[[sum(Nt[t2][i]*c2[i] for i in range(n)) for t2 in range(d)] for c2 in cand]
                if rk(imgs)>len(chosen):
                    chosen=cand
                if len(chosen)==2: break
            if len(chosen)<2: continue
            Ms,Fs=make_solution(chosen,A,N,n)
            if rk(Ms)!=2: continue
            K=ker_basis(Ms)
            ok5a=(not K or not K[0]) or rk(mm(Fs,K))==0
            if not ok5a: continue
            if cond_5b(Ms,Fs):
                got=True; break
        if got: rescued+=1; details.append(t)
    print("检验 %d 个实例；ρ≤1 失败 %d 个；被 2 维 A 救回 %d 个" % (tested,fails1,rescued))
    if details: print("救回的实例：", details[:10])
    print()
    if fails1>0 and rescued>0:
        print("⟹ *** 非单调！2 维 A 能救 ⟹ 需 Grassmann 搜索 ⟹ q1 可能为真 ***")
    elif fails1>0:
        print("⟹ 样本内未发现救回（不能断言单调）")

if __name__=="__main__":
    main()
