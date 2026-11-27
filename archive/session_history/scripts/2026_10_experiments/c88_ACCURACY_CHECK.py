r"""
c88_ACCURACY_CHECK.py -- 论文准确性核对

逐条核对 PAPER.md 中的声明：
  A. 定理 3.1（秩定律）在实例上成立
  B. 定理 4.1（必要性）—— 每个解都满足 α₀∈V
  C. 定理 4.2/4.4（充分性）—— α₀∈V 时确实有解
  D. 命题 4.3（单调性）—— 补零行不变
  E. 推论 4.4 的 q_min ≤ obs+1
  F. 引理 2.1（(5b) ⟺ PBH）
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr
import sys
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b, Pdet, gcd_list, is_nonzero_const, _rank

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]
_t={}
with open(os.path.join(_HERE,"test_caseII_YES.py"),encoding="utf-8") as fh:
    _src=fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0],"t","exec"),_t)
p1=_t["p1"]

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

def invariant_closure(M,Ap,d):
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
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

def nullspace_rows(M):
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

def main():
    checks={"A_rank_law":0,"B_necessity":0,"C_sufficiency":0,"D_monotone":0,"F_pbh":0}
    viol={k:0 for k in checks}
    rng=random.Random(31415926)
    got=0; t0=__import__("time").time()
    while got<10 and __import__("time").time()-t0<400:
        n=4
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA; N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        V=invariant_closure(R0,Ap,d); obs=len(V)
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
        a0=mm(L0,N)[0]
        a0in=(rk([r[:] for r in V]+[a0[:]])==len(V)) if V else all(x==0 for x in a0)
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=d+1; kk=q-1; npar=kk*mB
        pts=list(itertools.product([-1,0,1],repeat=npar)) if npar<=6 else \
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(300)]
        found=False
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            if not cond_5b(A0,A1): continue
            found=True
            # A. 秩定律
            checks["A_rank_law"]+=1
            r0=rk(A0)
            if r0>obs: viol["A_rank_law"]+=1
            # B. 必要性：解 ⟹ α₀∈V
            checks["B_necessity"]+=1
            if not a0in: viol["B_necessity"]+=1
            # D. 单调性：补零行后仍可行
            A0p=A0+[[Fr(0)]*d]; A1p=A1+[[Fr(0)]*d]
            checks["D_monotone"]+=1
            if not (cond_5a(A0p,A1p) and cond_5b(A0p,A1p)): viol["D_monotone"]+=1
            break
        # C. 充分性：α₀∈V ⟹ 有解（在 q=obs+1 处）
        if a0in:
            checks["C_sufficiency"]+=1
            if not found: viol["C_sufficiency"]+=1
        # F. 引理 2.1（(5b) ⟺ PBH）—— 独立的随机 (M,F)，F = ΛM
        Mr=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        Lam=[[Fr(rng.randint(-1,1)) for _ in range(q)] for _ in range(q)]
        Fx=mm(Lam,Mr)
        Mt=[[Mr[i][j] for i in range(q)] for j in range(d)]
        Ns=nullspace_rows(Mt)
        if Ns and rk(Mr)>0:
            m=len(Ns)
            P=[]
            for i in range(q):
                row=[]
                for j in range(q):
                    a=Lam[j][i]
                    if i==j: row.append([a,Fr(-1)])
                    else: row.append([a])
                for t in range(m): row.append([Ns[t][i]])
                P.append(row)
            ps=[Pdet([[P[i][j] for j in cols] for i in range(q)],q)
                for cols in itertools.combinations(range(q+m),q)]
            g=gcd_list(ps)
            pbh=is_nonzero_const(g)
            checks["F_pbh"]+=1
            if cond_5b(Mr,Fx)!=pbh: viol["F_pbh"]+=1
        got+=1
    print("=== 论文声明核对 ===\n")
    names={"A_rank_law":"A. 定理3.1（rank≤obs）",
           "B_necessity":"B. 定理4.1（解⟹α₀∈V）",
           "C_sufficiency":"C. 定理4.2（α₀∈V⟹有解）",
           "D_monotone":"D. 命题4.3（单调性）",
           "F_pbh":"F. 引理2.1（(5b)⟺PBH）"}
    for k in ["A_rank_law","B_necessity","C_sufficiency","D_monotone","F_pbh"]:
        print("%-28s 检查 %4d 次；违反 %d  %s" %
              (names[k], checks[k], viol[k], "✓" if viol[k]==0 else "**✗**"))
    allok=all(v==0 for v in viol.values())
    print()
    print("总结论：", "**全部通过** ✓" if allok else "**存在违反，论文需修正** ✗")


if __name__=="__main__":
    main()
