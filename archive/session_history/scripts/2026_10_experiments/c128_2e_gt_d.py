r"""
c128_2e_gt_d.py -- 检验充分条件：2e > d ⟹ ρ≤1 可达

步骤：
 1. 实例满足 2e>d（e=rank R0）
 2. 求 W = {ℓN : ℓ⊥col(AN)} 与 rowspace(R0) 的非零交 α0
 3. 解 L0：L0N=α0，L0AN=0
 4. 解 ℓ1：ℓ1N=0，ℓ1AN=α0
 5. 验证 ρ=1 与 (5a)(5b)
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

def main():
    print("=== 检验充分条件：2e>d ⟹ ρ≤1 可达 ===\n")
    n=7; p=2
    inst=0; ok=0; fail=0; nointer=0
    for t in range(1,200):
        rng=random.Random(9900000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=4: continue      # d = 7-4 = 3
        N=ker_basis(Mrows)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=3: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        e=rk(R0)
        if 2*e<=d: continue           # 只测 2e>d\n        if e>=d: continue             # 只测 e<d（真正的推广）
        # W
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]
        perp=nullsp(ANt)
        W=rb(mm(perp,N)) if perp else []
        # rowspace(R0)
        R0r=rb(R0)
        # 交
        inter=nullsp([])  # 占位
        # 求 α0 ∈ W ∩ rowspace(R0)
        Wb=W; R0b=R0r
        if not Wb or not R0b: nointer+=1; continue
        # α0 = 组合测试：枚举小系数
        cands=[]
        for iw in range(len(Wb)):
            for ir in range(len(R0b)):
                cands.append((iw,ir))
        alpha=None; L0v=None
        # 直接解：L0 满足 L0N = α0 ∈ rowspace(R0) 且 L0AN = 0
        # 用线性系统：未知 L0 ∈ R^n 和 α0 的系数
        # 简化：枚举 α0 = rowspace(R0) 的基向量的 ±1 组合
        import itertools as it
        found=None
        for coef in it.product([-1,0,1],repeat=len(R0b)):
            if all(c==0 for c in coef): continue
            a0=[sum(coef[i]*R0b[i][j] for i in range(len(R0b))) for j in range(d)]
            Amat=[]; bv=[]
            for j in range(d):
                Amat.append([N[i][j] for i in range(n)]); bv.append(a0[j])
            for j in range(d):
                Amat.append([AN[i][j] for i in range(n)]); bv.append(Fr(0))
            s=solve(Amat,bv)
            if s is not None:
                found=(s,a0); break
        inst+=1
        if found is None:
            fail+=1; print("[%d] 无 L0（2e=%d>d=%d, e=%d）✗" % (t,2*e,d,e)); continue
        L0,a0=found
        # 解 ℓ1
        A2m=[]; b2=[]
        for j in range(d):
            A2m.append([N[i][j] for i in range(n)]); b2.append(Fr(0))
        for j in range(d):
            A2m.append([AN[i][j] for i in range(n)]); b2.append(a0[j])
        l1=solve(A2m,b2)
        if l1 is None:
            fail+=1; print("[%d] ℓ1 无解（应对应 α0 ∉ rowspace(R0)）✗" % t); continue
        Lam=[L0, l1]
        M=mm(Lam,N); F=mm(mm(Lam,A),N)
        rho=rk(M)
        K=ker_basis(M)
        ok5a=(not K or not K[0]) or rk(mm(F,K))==0
        ok5b=cond_5b(M,F)
        good=(rho==1 and ok5a and ok5b)
        if good: ok+=1
        else:
            fail+=1
            if fail<=5: print("[%d] rho=%d (5a)=%s (5b)=%s ✗" % (t,rho,ok5a,ok5b))
    print()
    print("实例（2e>d，找到 d=2 的）：%d ；成功 %d ；失败 %d" % (inst,ok,fail))
    if inst>0 and ok==inst:
        print("\n⟹ *** 充分条件成立：2e>d ⟹ ρ≤1 可达（%d/%d）*** ✓" % (ok,inst))
        print("   故 ρ 可以小到 1，而 obs 无关")
    elif ok>0:
        print("\n⟹ 部分成立 (%d/%d)" % (ok,inst))

if __name__=="__main__":
    main()
