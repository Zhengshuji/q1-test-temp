r"""
c51_Einf_criterion.py -- 验证 (5b) 的新代数刻画：

   E := im(H) ⊆ ℝ^q，T := Λ|_E = (Hx ↦ Fx)（由 (5a) 唯一确定）
   E_1 := {v ∈ E : Tv ∈ E}，E_{k+1} := {v ∈ E_k : Tv ∈ E_k}，E_∞ = 稳定值
   **(5b) ⟺ E_∞ = 0**

【要点】与 c49 的区别：T 是 E→ℝ^q 的映射（不是算子），E_∞ 只用到 T 在 E 上的值
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

def cond_5b(A0,A1,maxm=400):
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

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

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

def nullspace(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

def T_on(A0,A1,v):
    """v ∈ im(A0) ⟹ 求 x: A0 x = v，返回 F x = T v"""
    q=len(A0); d=len(A0[0])
    m=[[Fr(A0[i][j]) for j in range(d)]+[Fr(v[i])] for i in range(q)]
    piv=[]; r=0
    for c in range(d):
        p=None
        for i in range(r,q):
            if m[i][c]!=0: p=i; break
        if p is None: continue
        m[r],m[p]=m[p],m[r]
        pv=m[r][c]; m[r]=[x/pv for x in m[r]]
        for i in range(q):
            if i!=r and m[i][c]!=0:
                f=m[i][c]
                m[i]=[m[i][j]-f*m[r][j] for j in range(d+1)]
        piv.append(c); r+=1
        if r==q: break
    for i in range(r,q):
        if all(m[i][j]==0 for j in range(d)) and m[i][d]!=0:
            return None      # v ∉ im(A0)
    x=[Fr(0)]*d
    for i,c in enumerate(piv): x[c]=m[i][d]
    return [sum(A1[i][j]*x[j] for j in range(d)) for i in range(len(A1))]

def Einf_basis(A0,A1):
    """E_∞ = {v ∈ im(A0) : T^k v ∈ im(A0) ∀k}"""
    q=len(A0)
    E=rowspace_basis([list(c) for c in zip(*A0)])   # im(A0) 的行表示（每行一个向量）
    E=[[Fr(x) for x in r_] for r_ in E]
    while True:
        # E_1 = {v ∈ E : Tv ∈ E}
        cond=[]
        for b in E:
            Tv=T_on(A0,A1,b)
            if Tv is None: return None
            cond.append(Tv)
        # 需要 v 的组合使 T(组合) ∈ E  ⟹ 组合系数 c 满足 T(c·B) ∈ E
        # T 是线性的：T(Σc_i b_i) = Σ c_i T(b_i)
        # 约束：Σ c_i T(b_i) 在 E 中 ⟹ 用 E 的零化子
        # 简化：直接求 kernel of (compose T with quotient by E)
        # 用 E 的补空间基构造投影
        if not E: return []
        Emat=[[E[i][j] for j in range(q)] for i in range(len(E))]   # |E|×q
        # 找 E 的补：把 Emat 行扩充为 ℝ^q 的基，取补部分
        full=[r_[:] for r_ in Emat]
        for j in range(q):
            e=[Fr(1) if i==j else Fr(0) for i in range(q)]
            if rk(full+[e])==len(full)+1: full.append(e)
            if len(full)==q: break
        comp=full[len(Emat):]
        # quotient 投影：向量 → 在 comp 下的坐标
        if not comp: return E       # E = 整个空间
        # 解 coords·full = w，取后 |comp| 个
        def proj(w):
            n=q
            A2=[[Fr(full[i][j]) for i in range(q)]+[Fr(w[j])] for j in range(q)]
            piv=[]; r=0
            for c in range(q):
                p=None
                for i in range(r,q):
                    if A2[i][c]!=0: p=i; break
                if p is None: continue
                A2[r],A2[p]=A2[p],A2[r]
                pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
                for i in range(q):
                    if i!=r and A2[i][c]!=0:
                        f=A2[i][c]
                        A2[i]=[A2[i][j]-f*A2[r][j] for j in range(q+1)]
                piv.append(c); r+=1
            co=[Fr(0)]*q
            for i,c in enumerate(piv): co[c]=A2[i][q]
            return co[len(Emat):]
        Q=[[proj(Tv)[t] for t in range(len(comp))] for Tv in cond]  # |E| × |comp|
        # 需要 c 使 c·Q = 0 （即 Σ c_i (T b_i)_quot = 0）
        ns=nullspace([[Q[i][j] for i in range(len(Q))] for j in range(len(Q[0]))])  # 解 Q^T c = 0
        if not ns:
            return []        # E_1 = 0
        newE=[]
        for c in ns:
            v=[sum(c[i]*E[i][j] for i in range(len(E))) for j in range(q)]
            newE.append(v)
        newE=rowspace_basis(newE)
        if len(newE)==len(E):
            return E
        E=newE
        if not E: return []


def main():
    print("=== 验证 (5b) ⟺ E_∞ = 0 ===\n")
    print("%-14s %4s %6s %10s %8s %6s" % ("实例","ρ","dimE∞","gcd(5b)","E∞=0?","一致"))
    print("-"*54)
    ok=0; bad=0; tot=0
    for (n,seed) in [(4,70052),(5,70065)]:
        rng=random.Random(seed)
        got=0
        for trial in range(120000):
            if got>=8: break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            Wn=Cc+CA
            N=ker_basis(Wn)
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
            rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(k)]
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for z in rr:
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            g=cond_5b(A0,A1)
            Ei=Einf_basis(A0,A1)
            if Ei is None: continue
            is0 = (len(Ei)==0)
            agree = (g == is0)
            if agree: ok+=1
            else: bad+=1
            tot+=1
            print("%-14s %4d %6d %10s %8s %6s" %
                  ("n=%d t=%d"%(n,trial), rk(A0), len(Ei), str(g), str(is0),
                   "✓" if agree else "✗"))
            got+=1
        print()
    print("总 %d ；一致 %d ；不一致 %d" % (tot,ok,bad))
    if bad==0 and tot>0:
        print("\n⟹ **(5b) ⟺ E_∞ = 0** 成立 ✓")


if __name__=="__main__":
    main()
