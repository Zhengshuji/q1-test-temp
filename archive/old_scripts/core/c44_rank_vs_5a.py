r"""
c44_rank_vs_5a.py -- 检验机制假设：
   α0∉V 时，rank(A0)=obs 的候选**必过不了 (5a)**

【若成立】则机制为：
   (5a) 迫使 A1 = ΛA0 ⟹ A1 的每行 ∈ rowspace(A0) = span(α_i)
   而 γ0 = α0A' + β0 ；α0∉V 使 γ0 的"V 外分量"与 A0 的行冲突
   ⟹ 无解（与 (5b) 无关）
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
    m_rows=len(M); ncols=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(ncols):
        p=None
        for i in range(r,m_rows):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m_rows):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(ncols)]
        piv.append(r); r+=1
        if r==m_rows: break
    return [A[i][:] for i in piv]

def invariant_closure(M, Ap, d):
    basis=row_space_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d and basis:
        cur=mm(cur,Ap)
        if rk(basis+[r[:] for r in cur])==len(basis): break
        basis=basis+[r[:] for r in cur]
    return row_space_basis(basis)

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

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0


def main():
    print("=== 检验：α0∉V 时 rank(A0)=obs 的候选能否过 (5a)？ ===\n")
    n=4
    rng=random.Random(555000)
    done=0
    t_all=time.time()
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
        nfree=d; npar=nfree*mB
        if npar>7: continue
        obs=len(V)
        # 按 rank 分类统计 (5a) 通过率
        stat={}
        for vals in itertools.product([-1,0,1], repeat=npar):
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(nfree):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            rr=rk(A0)
            ok=cond_5a(A0,A1)
            if rr not in stat: stat[rr]=[0,0]
            stat[rr][0]+=1
            if ok: stat[rr][1]+=1
        print("实例 trial=%d：d=%d obs=%d（α0∉V）" % (trial,d,obs))
        for rr in sorted(stat):
            tot,ok=stat[rr]
            mark = "  ← **rank=obs 层**" if rr==obs else ""
            print("   rank(A0)=%d : %4d 个，过 (5a) %4d (%.0f%%)%s" %
                  (rr,tot,ok,100.0*ok/tot,mark))
        print()
        done+=1
    print("【判读】若 rank=obs 层的 (5a) 通过率为 0 ⟹ **假设成立** ⟹ 机制在 (5a)，不在 (5b)")


if __name__=="__main__":
    main()
