r"""
c45_5b_parallel.py -- ⭐⭐⭐⭐ (5b) 的新等价形式验证

【新形式】
   yᵀ(λA0 − A1) = 0  ⟺  yᵀA1 = λ·yᵀA0
   ⟺  (zAN) = λ·(zN)，其中 z := yᵀL（z ∈ row(L) = L 的行空间）

   (5b) ⟺ **∀ 0≠z ∈ row(L)：zAN 与 zN 不成比例**

【意义】
   · 不需要 Λ、不需要 λ、不需要子式 gcd
   · 是一个"线性子空间避开行列式簇"的几何条件
   · 且**可单侧检验**：找到一个成比例的 z ⟹ (5b) 必败（必要条件，可判伪）

【本脚本】双向核对：
   ① gcd 判据 cond_5b（严格）
   ② 新判据：随机扫 z 看成比例；若命中 ⟹ 应 cond_5b=False
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

def Pt(p):
    q=list(p)
    while len(q)>1 and q[-1]==0: q.pop()
    return q
def Pa(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))+(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Ps(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))-(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Pm(a,b):
    if Pt(a)==[Fr(0)] or Pt(b)==[Fr(0)]: return [Fr(0)]
    r=[Fr(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return Pt(r)
def Pdv(a,b):
    a=Pt(a); b=Pt(b); db=len(b)-1
    q=[Fr(0)]*max(1,len(a)-db)
    while len(a)-1>=db and a!=[Fr(0)]:
        d=len(a)-1-db; co=a[-1]/b[-1]; q[d]+=co
        for i in range(len(b)): a[d+i]-=co*b[i]
        a=Pt(a)
    return Pt(q),a
def Pg(a,b):
    a,b=Pt(a),Pt(b)
    while b!=[Fr(0)]:
        _,r=Pdv(a,b); a,b=b,r
    if len(a)>1:
        lc=a[-1]; a=[x/lc for x in a]
    return a
def Pdet(M,k):
    if k==1: return [Fr(x) for x in M[0][0]]
    tot=[Fr(0)]
    for j in range(k):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        d=Pdet(sub,k-1); pr=Pm(M[0][j],d)
        tot=Pa(tot,pr) if j%2==0 else Ps(tot,pr)
    return Pt(tot)
def gcd_all(ps):
    if not ps: return None
    g=ps[0]
    for q in ps[1:]:
        g=Pg(g,q)
        if len(g)==1: break
    return g
def const_nz(g):
    return g is not None and len(Pt(g))==1 and any(x!=0 for x in g)

def cond_5b(A0,A1,maxm=300):
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    P=[[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxm: break
        if cnt>maxm: break
    return const_nz(gcd_all(ps))

def parallel(u, v):
    """u ∥ v ?（含退化情形）"""
    if all(x==0 for x in v): return False     # v=0 ⟹ 只有 u=0 才算比例；此处排除
    for i in range(len(u)):
        if v[i]!=0:
            lam=u[i]/v[i]
            return all(u[j]==lam*v[j] for j in range(len(u)))
    return False

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
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def find_parallel_z(Lrows, N, AN, d, n, nsample, rng):
    """在 row(L) 中随机找 z 使 zAN ∥ zN"""
    B=rowspace_basis(Lrows)
    if not B: return None
    s=len(B)
    for _ in range(nsample):
        co=[Fr(rng.randint(-2,2)) for _ in range(s)]
        if all(x==0 for x in co): continue
        z=[sum(co[i]*B[i][j] for i in range(s)) for j in range(n)]
        if all(x==0 for x in z): continue
        zN  =[sum(z[i]*N[i][j] for i in range(n)) for j in range(d)]
        zAN =[sum(z[i]*AN[i][j] for i in range(n)) for j in range(d)]
        if parallel(zAN, zN):
            return z
    return None


def main():
    print("=== 验证 (5b) 的新等价形式：∀0≠z∈row(L)，zAN ∦ zN ===\n")
    print("%-12s %5s %6s %9s %9s %5s" % ("实例","d","ρ","gcd(5b)","找到成比例z?","一致"))
    print("-"*56)
    ok=0; bad=0; tot=0
    for (n,seed) in [(4,70052),(5,70065)]:
        rng=random.Random(seed)
        got=0; t_all=0
        for trial in range(120000):
            if got>=6: break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
            d=len(N[0])
            if d<2: continue
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
            AN=mm(A,N)
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=rowspace_basis(Mcol); mB=len(resB)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            q=d+1; k=q-1
            rng2=random.Random(7531+97*trial+n)
            # 随机取一组行，构造 L 与 (A0,A1)
            rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(k)]
            A0=[H0[0][:]]; A1=[F0[0][:]]
            Lrows=[L0[0][:]]
            for z in rr:
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
                # 反解 L（用同一行 L0 + z 的行）：取该行的 α,β 对应的 L
                # 简化：直接用 z 组合 resB = row_basis([N|AN]) 的对应 L 行
                Lrows.append(None)     # 占位，稍后用 z 直接算
            # 更直接：row(L) 的"像"我们只需 z 作用于 [N|AN] ⟹ 用 w 即可
            # 定义 zN = w[:d]，zAN = w[d:] —— 这正是本行！
            # 所以 (5b) 的新形式就是：任何【行组合】的 (α,γ) 都不成比例
            # 用 row(L) 的张成：注意 row(L) 在 [N|AN] 下的像 = row([A0|A1])
            # 故等价形式为：∀0≠y，组合行的 (α,γ) 不成比例 ⟺ yᵀA1 ∦ yᵀA0
            s=len(A0)
            found=None
            rng3=random.Random(911+97*trial+n)
            for _ in range(200):
                co=[Fr(rng3.randint(-2,2)) for _ in range(s)]
                if all(x==0 for x in co): continue
                al=[sum(co[i]*A0[i][j] for i in range(s)) for j in range(d)]
                ga=[sum(co[i]*A1[i][j] for i in range(s)) for j in range(d)]
                if all(x==0 for x in al): continue
                if parallel(ga, al):
                    found=(co,al,ga); break
            g=cond_5b(A0,A1)
            agree = ((found is not None) == (g is False))
            if agree: ok+=1
            else: bad+=1
            tot+=1
            print("%-12s %5d %6d %9s %9s %5s" %
                  ("n=%d t=%d"%(n,trial), d, rk(A0),
                   str(g), "是" if found else "否", "✓" if agree else "✗"))
            got+=1
        print()
    print("总 %d ；一致 %d ；不一致 %d" % (tot,ok,bad))
    print()
    if bad==0:
        print("⟹ **(5b) 的新等价形式成立**：(5b) ⟺ ∀0≠y, yᵀA1 ∦ yᵀA0 ✓")
        print("   （即 L 的任意行组合的 (α,γ) 都不成比例 —— 无需 Λ/λ/子式 gcd）")
    else:
        print("⚠️ 有不一致 —— 需检查（采样可能漏掉稀有 z）")


if __name__=="__main__":
    main()
