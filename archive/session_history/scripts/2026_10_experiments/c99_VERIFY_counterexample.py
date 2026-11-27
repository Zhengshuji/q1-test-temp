r"""
c99_VERIFY_counterexample.py -- 严格验证 c98 构造的反例是否**可实现**

关键检查：$[M|F]$ 的每一行必须在 rowspace([N|AN]) 中
（即存在 L 使 LN=M, LAN=F）
"""
import os, io, contextlib, random, sys, time
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]

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
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def invcl(M0,Ap,d):
    b=rowspace_basis(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rowspace_basis(b)

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
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def solve_row(Mat,rhs):
    n=len(Mat[0]); m=len(Mat)
    A2=[[Fr(Mat[i][j]) for j in range(n)]+[Fr(rhs[i])] for i in range(m)]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A2[i][c]!=0: p=i; break
        if p is None: continue
        A2[r],A2[p]=A2[p],A2[r]
        pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
        for i in range(m):
            if i!=r and A2[i][c]!=0:
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[r][j] for j in range(n+1)]
        piv.append(c); r+=1
        if r==m: break
    for i in range(r,m):
        if all(A2[i][j]==0 for j in range(n)) and A2[i][n]!=0: return None
    x=[Fr(0)]*n
    for i,c in enumerate(piv): x[c]=A2[i][n]
    return x

def main():
    print("=== 验证 c98 反例的可实现性 ===\n")
    t=0; real=0; fake=0; found=0
    t0=time.time()
    while time.time()-t0<400:
        t+=1
        n=random.Random(830000+t).choice([4,5,6])
        rng=random.Random(730000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        N=ker_basis(Cc+CA)
        if not N or not N[0]: continue
        d=len(N[0])
        if d<2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        W0=rowspace_basis(R0)
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        if obs<2: continue
        # [N|AN] 的行空间（n 行，2d 列）—— 可实现行必须落在其中
        NA_cols=[N[i][:]+AN[i][:] for i in range(n)]
        RS=rowspace_basis(NA_cols)
        # 找 L0
        L0=None
        for _x in range(30):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
            if all(x==0 for x in pv): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        a0=mm(L0,N)[0]
        if all(x==0 for x in a0): continue
        g0=[sum(a0[i]*Ap[i][j] for i in range(d)) for j in range(d)]
        span=[a0[:]]+[r[:] for r in W0]
        if rk(span+[g0])!=rk(span): continue
        k=len(W0)
        Mat=[[a0[j]]+[W0[i][j] for i in range(k)] for j in range(d)]
        rhs=[-g0[j] for j in range(d)]
        sol=solve_row(Mat,rhs)
        if sol is None: continue
        w=sol[0]
        if w==1: continue
        q=d+1
        u=[Fr(0)]*q; u[0]=Fr(1)
        up=[Fr(0)]*q; up[0]=w
        if q>1: up[1]=Fr(1)
        A0=[[u[i]*a0[j] for j in range(d)] for i in range(q)]
        A1=[[up[i]*a0[j] for j in range(d)] for i in range(q)]
        rho=rk(A0)
        if rho>=obs: continue
        if not cond_5b(A0,A1): continue
        found+=1
        # === 关键：可实现性检查 ===
        # 行 i: (u_i·a0 | up_i·a0) 必须在 RS 中
        okall=True
        for i in range(q):
            row=[u[i]*a0[j] for j in range(d)]+[up[i]*a0[j] for j in range(d)]
            if rk([r[:] for r in RS]+[row])!=len(RS):
                okall=False; break
        # 第一行必须是 L0 的实现：L0·[N|AN] = (a0|γ0)
        g_actual=[sum(L0[0][i]*AN[i][j] for i in range(n)) for j in range(d)]
        first_ok=(g_actual==[up[0]*a0[j] for j in range(d)])
        if okall and first_ok:
            real+=1
            print("*** t=%d n=%d d=%d obs=%d ρ=%d —— **真反例（可实现）** ***" % (t,n,d,obs,rho))
            print("    M =", [[str(x) for x in r] for r in A0])
            print("    F =", [[str(x) for x in r] for r in A1])
            print("    L0 =", [str(x) for x in L0[0]])
            break
        else:
            fake+=1
            if fake<=3:
                print("  t=%d: NOT realizable (rows_in_RS=%s, first_ok=%s) —— 伪反例" % (t,okall,first_ok))
    print()
    print("找到 (ρ<obs 且 (5a)∧(5b)) 的抽象 (M,F)：%d 个" % found)
    print("其中**可实现**（存在 L）：%d ；不可实现（伪）：%d" % (real,fake))
    if real>0:
        print("\n*** 反例成立：存在真解使 ρ<obs ⟹ ρ≥obs **为假** ⟹ 需重新评估 q1 ***")
    elif found>0:
        print("\n⟹ 所有抽象构造都**不可实现** ⟹ ρ<obs 的解**不存在**（在已测范围内）")
        print("   这解释了为何 474,970 个随机解都满足 ρ=obs ✓")

if __name__=="__main__":
    main()
