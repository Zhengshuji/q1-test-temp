r"""
c124_perturb.py -- 扰动反例的 A，检验 ρ<obs 的解是否存在

基准反例：n=7, p=2, L0 = e1ᵀ − e5ᵀ（固定），ℓ1 = e4ᵀ
然后对 A 施加随机扰动 A → A + A₁（A₁ 随机小整数），
对每个扰动实例：重新算 N, A', R0, obs，然后在 q=2 的族里搜解。
"""
import os, io, contextlib, random, itertools, sys
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

def invcl(M0,Ap,d):
    b=rb(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rb(b)

n=7
Z=Fr(0); O=Fr(1)
# 基准反例
A0=[[Z]*n for _ in range(n)]
A0[0][1]=O; A0[1][2]=O; A0[3][0]=O; A0[4][1]=O; A0[5][3]=O; A0[6][4]=O
C=[[Z]*n for _ in range(2)]
C[0][5]=O; C[1][6]=O
L0=[[Z]*n]; L0[0][0]=O; L0[0][4]=Fr(-1)

def analyze(A, tag, pts=None):
    CA=mm(C,A); Mrows=C+CA
    d=n-rk(Mrows)
    N=ker_basis(Mrows)
    if not N or not N[0]: return None
    dd=len(N[0])
    AN=mm(A,N)
    Nt=[[N[i][j] for i in range(n)] for j in range(dd)]
    iN=minv(mm(Nt,N))
    if iN is None: return None
    Ap=mm(mm(iN,Nt),AN)
    R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(dd)] for i in range(n)]
    Vb=invcl(R0,Ap,dd); obs=len(Vb)
    # 搜 q=2 的族
    Mcol=[N[i][:]+AN[i][:] for i in range(n)]
    resB=rb(Mcol); mB=len(resB)
    H0=mm(L0,N); F0=mm(mm(L0,A),N)
    q=2; kk=q-1; npar=kk*mB
    rrr=random.Random(12345+hash(tag)%10000)
    if npar<=5:
        plist=list(itertools.product([-2,-1,0,1,2],repeat=npar))
    else:
        plist=[[rrr.randint(-2,2) for _ in range(npar)] for _ in range(1200)]
    sols=[]
    for vals in plist:
        Aa=[H0[0][:]]; Fa=[F0[0][:]]
        for ti in range(kk):
            z=vals[ti*mB:(ti+1)*mB]
            if len(z)<mB: break
            w=[sum(z[tt]*resB[tt][j] for tt in range(mB)) for j in range(2*dd)]
            Aa.append(w[:dd]); Fa.append(w[dd:])
        if len(Aa)!=q: continue
        K=ker_basis(Aa)
        if K and K[0] and rk(mm(Fa,K))!=0: continue
        if not cond_5b(Aa,Fa): continue
        rho=rk(Aa)
        if rho==0: continue
        sols.append(rho)
    return dd,obs,len(sols),sols

print("=== 扰动实验：基准反例 vs 扰动版 ===\n")
r0=analyze(A0,"base")
print("基准: d=%d obs=%d 解数=%d rho=%s" % r0 if r0 else "基准失败")
print()
print("扰动 A（随机 -1/0/1 项，幅度 1）：")
found_lt=0; tot=0
for t in range(1,13):
    rng=random.Random(770000+t)
    A=[r[:] for r in A0]
    for _ in range(2):
        i=rng.randrange(n); j=rng.randrange(n)
        A[i][j]=A[i][j]+Fr(rng.choice([-1,1]))
    r=analyze(A,"p%d"%t)
    if r is None: 
        print("  [%d] 分析失败" % t); continue
    dd,obs,nsol,sols=r
    tot+=1
    mins=min(sols) if sols else None
    flag = ""
    if sols and mins<obs: flag=" ** rho<obs **"; found_lt+=1
    print("  [%2d] d=%d obs=%d 解数=%-4d rho分布=%s%s" % (t,dd,obs,nsol,sorted(set(sols)),flag))
print()
print("扰动实例 %d ；其中出现 rho<obs 的 %d" % (tot,found_lt))
if found_lt>0:
    print("\n⟹ *** rho<obs 在扰动下存活 ⟹ 不是测度零现象 ⟹ 我的'一般位置'假设错 ✗ ***")
else:
    print("\n⟹ 扰动后不再出现 rho<obs ⟹ 支持'反例是退化实例'")
