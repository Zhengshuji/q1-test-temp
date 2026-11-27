r"""
c48_modV_invariant.py -- 验证新引理：
   α0∉V ⟹ Ū = row(A0) mod V 是 ℝ^d/V 中的**非零 Ā'-不变子空间**

【推导】
   γ_i = α_iA' + β_i，β_i ∈ rowR ⊆ V，V 是 A'-不变
   ⟹ mod V：γ̄_i = ᾱ_i Ā'
   而 γ_i ∈ row(A0) = U ⟹ γ̄_i ∈ Ū ；ᾱ_i 张成 Ū
   ⟹ ŪĀ' ⊆ Ū  ✓ （Ū 是 Ā'-不变）
   又 α0 ∉ V ⟹ ᾱ0 ≠ 0 ⟹ Ū ≠ 0  ✓

【本脚本】对实例中所有 rank=obs 且过 (5a) 的候选（若无则取任意候选）验证该引理
"""
import os, io, contextlib, random, itertools, time
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

def row_space_basis(M):
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

def extend_basis(Vb, d):
    basis=[r[:] for r in Vb]
    for j in range(d):
        e=[Fr(1) if i==j else Fr(0) for i in range(d)]
        if rk(basis+[e])==len(basis)+1:
            basis.append(e)
        if len(basis)==d: break
    return basis

def coords_in_full(full, v):
    d=len(full)
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
    return co

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

def solve_row(Mat, rhs):
    n=len(Mat); m=len(Mat[0])
    A2=[[Fr(Mat[i][j]) for i in range(n)]+[Fr(rhs[j])] for j in range(m)]
    rows=len(A2); cols=n+1
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,rows):
            if A2[i][c]!=0: p=i; break
        if p is None: continue
        A2[r],A2[p]=A2[p],A2[r]
        pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
        for i in range(rows):
            if i!=r and A2[i][c]!=0:
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[r][j] for j in range(cols)]
        piv.append(c); r+=1
        if r==rows: break
    for i in range(r,rows):
        if all(A2[i][j]==0 for j in range(n)) and A2[i][n]!=0:
            return None
    x=[Fr(0)]*n
    for i,c in enumerate(piv): x[c]=A2[i][n]
    return x

def invariant_closure(M, Ap, d):
    basis=row_space_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d and basis:
        cur=mm(cur,Ap)
        if rk(basis+[r[:] for r in cur])==len(basis): break
        basis=basis+[r[:] for r in cur]
    return row_space_basis(basis)

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0


def main():
    print("=== 验证引理：α0∉V ⟹ Ū 是 ℝ^d/V 中非零 Ā'-不变 ===\n")
    n=4
    rng=random.Random(555000)
    done=0; t_all=time.time()
    for trial in range(200000):
        if done>=3 or time.time()-t_all>300: break
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
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        V=invariant_closure(R, Ap, d)
        if len(V)>=d: continue
        a0=None
        for _try in range(30):
            cand=[Fr(rng.randint(-2,2)) for _ in range(d)]
            if all(x==0 for x in cand): continue
            if rk([r[:] for r in V]+[cand])>len(V):
                a0=cand; break
        if a0 is None: continue
        L0=solve_row(N, a0)
        if L0 is None: continue
        L0=[L0]
        if rk(L0+Cc)!=2: continue
        try:
            _Lx,eta=p1(A,Cc,L0)
        except Exception:
            continue
        if not eta: continue
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=row_space_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        # 取若干随机候选行（不要求 (5a)），验证"γ̄ ∈ Ū"这一代数恒等
        full=extend_basis(V, d)
        dq=d-len(V)
        Aq=[]
        for j in range(len(V), d):
            w=full[j]
            wAp=[sum(w[t]*Ap[t][jj] for t in range(d)) for jj in range(d)]
            co=coords_in_full(full, wAp)
            Aq.append(co[len(V):])
        ncheck=0; nok=0; nskip=0
        rng2=random.Random(4242+97*trial)
        for _try in range(200):
            nfree=d
            rrs=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(nfree)]
            A0=[H0[0][:]]
            Aset=[H0[0][:]]
            Gset=[F0[0][:]]
            for z in rrs:
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); Aset.append(w[:d]); Gset.append(w[d:])
            # 引理的假设是 (5a) —— 只测通过 (5a) 的候选
            if not cond_5a(A0,Gset):
                nskip+=1; continue
            U=row_space_basis(Aset)
            if not U: continue
            # U 的 mod-V 投影
            Ubar=[]
            for r_ in U:
                co=coords_in_full(full, r_)
                Ubar.append(co[len(V):])
            Ub=row_space_basis(Ubar) if any(any(x!=0 for x in v) for v in Ubar) else []
            if not Ub: continue          # Ū=0，非本引理范围
            # 检查 ŪĀ' ⊆ Ū
            UbA=mm(Ub, Aq) if Aq else []
            ok = (rk([r[:] for r in Ub]+[r[:] for r in UbA])==len(Ub)) if UbA else True
            ncheck+=1
            if ok: nok+=1
        print("实例 trial=%d：d=%d obs=%d dim(ℝ^d/V)=%d" % (trial,d,len(V),dq))
        print("   通过 (5a) 的候选 %d 个（跳过 %d 个不满足 (5a) 的）" % (ncheck,nskip))
        print("   其中 Ū≠0 且 ŪĀ'⊆Ū ：%d 个  %s" %
              (nok,"✓ 引理成立" if ncheck==nok and ncheck>0 else "⚠️"))
        print()
        done+=1
    print("【引理（严格证明，无需数值）】")
    print("    γ_i = α_i A' + β_i，β_i ∈ rowR ⊆ V，V 为 A'-不变")
    print("    ⟹ mod V：γ̄_i = ᾱ_i Ā'")
    print("    (5a) ⟹ γ_i ∈ row(A0) = U ⟹ γ̄_i ∈ Ū")
    print("    ᾱ_i 张成 Ū ⟹ ŪĀ' ⊆ Ū  ✓")
    print("    α0 ∉ V ⟹ ᾱ0 ≠ 0 ⟹ Ū ≠ 0  ✓")
    print("   ⟹ 这是**严格引理**；但它本身**不含矛盾**")


if __name__=="__main__":
    main()
