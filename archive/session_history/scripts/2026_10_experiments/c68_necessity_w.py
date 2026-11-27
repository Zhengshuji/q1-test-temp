r"""
c68_necessity_w.py -- 验证新必要条件：
   (5b) 失败 ⟹ ∃ 0≠w ∈ U, wA' ∈ span(w) + W₀
其中 U = row(A0), W₀ = row(R)，A' 是压缩映射
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
    g=ps[0]
    for q in ps[1:]:
        g=Pg(g,q)
        if len(g)==1: break
    return g
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
    if not ps: return False
    g=gcd_all(ps)
    return len(Pt(g))==1 and any(x!=0 for x in g)

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

def invariant_closure(M, Ap, d):
    basis=rowspace_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d and basis:
        cur=mm(cur,Ap)
        if rk(basis+[r[:] for r in cur])==len(basis): break
        basis=basis+[r[:] for r in cur]
    return rowspace_basis(basis)

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
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def exists_w(U, Ap, W0, d):
    """U 中是否存在 0≠w 使 wA' ∈ span(w) + W0 ？
       等价：dim{w ∈ U : wA' ∈ span(w)+W0} ≥ 1
       用"测试": 对 λ 扫描 + 线性系统"""
    # 对每个 λ：解 wA' - λw ∈ W0，w ∈ U，w≠0
    # 参数化 w = c·Ubasis；条件：c·(Ubasis A' - λ Ubasis) 的"W0 分量"为 0
    Ub=U
    UbA=mm(Ub,Ap) if Ub else []
    for lam in [Fr(0),Fr(1),Fr(-1),Fr(2),Fr(-2),Fr(1,2),Fr(-1,2),Fr(3),Fr(-3)]:
        D=[[UbA[i][j]-lam*Ub[i][j] for j in range(d)] for i in range(len(Ub))]
        # 约束：D 的行组合落在 W0 中 ⟹ 用 W0 的零化子（W0^⊥ 的基）左乘
        # W0^⊥ = ker(W0 作为矩阵的行空间) = nullspace of W0?
        # 更简单：wA' - λw = Σ c_i D_i ∈ W0 ⟺ 对 W0^⊥ 中每个 g: g·(Σ c_i D_i) = 0
        W0b=rowspace_basis(W0)
        if not W0b:
            # W0 = 0 ⟹ 条件 Σc_i D_i = 0
            Mcon=[[D[i][j] for i in range(len(D))] for j in range(d)]
        else:
            # 求 W0 的补，投影
            full=[r[:] for r in W0b]
            for j in range(d):
                e=[Fr(1) if i==j else Fr(0) for i in range(d)]
                if rk(full+[e])==len(full)+1: full.append(e)
                if len(full)==d: break
            comp=full[len(W0b):]
            if not comp: return True      # W0 = 全空间 ⟹ 任何 w 都行
            # 投影到 comp：解 coords
            def proj(v):
                A2=[[Fr(full[i][j]) for i in range(d)]+[Fr(v[j])] for j in range(d)]
                piv=[]; r=0
                for c in range(d):
                    p=None
                    for i in range(r,d):
                        if A2[i][c]!=0: p=i; break
                    if p is None: continue
                    A2[r],A2[p]=A2[p],A2[r]
                    pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
                    for i in range(d):
                        if i!=r and A2[i][c]!=0:
                            f=A2[i][c]
                            A2[i]=[A2[i][j]-f*A2[r][j] for j in range(d+1)]
                    piv.append(c); r+=1
                co=[Fr(0)]*d
                for i,c in enumerate(piv): co[c]=A2[i][d]
                return co[len(W0b):]
            Mcon=[[proj(D[i])[t] for i in range(len(D))] for t in range(len(comp))]
        # 需要 ∃c≠0: Mcon·c = 0 ⟹ rank(Mcon) < len(D)
        if rk(Mcon)<len(D): return True
    return False

def main():
    print("=== 验证：(5b) 失败 ⟹ ∃0≠w∈U, wA'∈span(w)+W₀ ===\n")
    n=4
    rng=random.Random(660220)
    ok=0; bad=0; tot=0
    t0=0
    for trial in range(200000):
        if tot>=10: break
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        W0=rowspace_basis(R)
        L0=None
        for _x in range(40):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
            if all(x==0 for x in pv): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        try:
            _Lx,eta=p1(A,Cc,L0)
        except Exception:
            continue
        if not eta: continue
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=d+1; kk=q-1
        rng2=random.Random(31+97*trial)
        for _try in range(60):
            rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(kk)]
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for z in rr:
                wv=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(wv[:d]); A1.append(wv[d:])
            K=ker_basis(A0)
            if K and K[0]: continue            # 只要 (5a) 成立
            g=cond_5b(A0,A1)
            U=rowspace_basis(A0)
            ew=exists_w(U,Ap,W0,d)
            tot+=1
            if (not g) <= ew: ok+=1
            else:
                bad+=1
                print("  **反例** trial=%d: (5b)=%s, ∃w=%s" % (trial,g,ew))
            print("  #%d (5b)=%-5s  ∃w=%-5s" % (tot,str(g),str(ew)))
            break
    print()
    print("共 %d；(5b)失败⟹∃w 成立 %d ；反例 %d" % (tot,ok,bad))
    if bad==0 and tot>0:
        print("\n⟹ 必要条件成立 ✓")


if __name__=="__main__":
    main()
