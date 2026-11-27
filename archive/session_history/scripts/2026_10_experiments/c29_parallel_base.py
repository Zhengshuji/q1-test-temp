r"""
c29_parallel_base.py -- ⭐⭐⭐⭐ 检验：rho=1 构造要求基行"平行"？

【rho=1 构造分析（与 §7.17 衔接）】
  所有行必须是 (c_i·a, d_i·a)（同一 a），且**固定行**（来自 L0）也必须是！
  固定行 = (α0, α0A' + β0) = (L0·N, L0·A·N)
  ⟹ 必须有  α0 ∥ a  且  α0A' + β0 ∥ a
  ⟹ **基行"平行"：γ0 := α0A' + β0 ∥ α0**

【假设 H2】rho=1 构造可行（从而有解）⟺ 基行平行 ∧ 行数足够
   ⟹ 若基行**不**平行 ⟹ 只能靠 rho≥2 的构造 ⟹ (5b) 难满足

【测】c19 的"空"实例 vs c28 的"稀疏非空"实例
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

def row_space_basis(M):
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


def describe(tag, A, Cc, L0, N, d, n):
    AN=mm(A,N)
    Nt=[[N[i][j] for i in range(n)] for j in range(d)]
    iNtN=minv(mm(Nt,N))
    if iNtN is None:
        print("%s: iNtN 奇异，跳过" % tag); return
    Ap=mm(mm(iNtN,Nt),AN)
    NAp=mm(N,Ap)
    R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
    Rrow=row_space_basis(R); e=len(Rrow)
    acc=[r[:] for r in Rrow]; cur=[r[:] for r in Rrow]
    while rk(acc)<d:
        cur=mm(cur,Ap)
        if rk(acc+[r[:] for r in cur])==rk(acc): break
        acc=acc+[r[:] for r in cur]
    obs=rk(acc)
    # 基行
    a0=mm(L0,N); g0=mm(mm(L0,A),N)
    rho0=rk(a0)
    # "平行"：g0 是否在 a0 的张成里（对 r=1：rank[a0;g0] == rank(a0)）
    par = (rk([a0[0][:], g0[0][:]]) == rho0)
    # rho=1 构造的两个条件
    #  (a,0) ∈ W ⟺ ker(·AN) ⊄ ker(·N)
    K1 = ker_basis(AN)        # n×e1
    K2 = ker_basis(N)
    c1 = True if (not K1 or not K1[0]) else (rk(mm(N, K1)) != 0)   # K1 中有向量不被 N 杀死
    c2 = True if (not K2 or not K2[0]) else (rk(mm(AN, K2)) != 0)  # K2 中有向量不被 AN 杀死
    print("%s：d=%d, m=%d, e=%d, obs=%d, rho0=%d" % (tag,d,d+e,e,obs,rho0))
    print("       基行平行（g0 ∥ a0）？ %s" % ("**是**" if par else "否"))
    print("       (a,0)∈W ？ %s ； (0,a)∈W ？ %s" % ("是" if c1 else "否", "是" if c2 else "否"))
    print()


def get_c19():
    """c19 的实例：n=5, seed 123455, trial 4"""
    n=5; rng=random.Random(123450+n)
    for trial in range(80000):
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
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
        if trial==4:
            return A,Cc,L0,N,d,n
    return None


def get_c28():
    """c28 的实例：n=4, seed 70052, trial 5"""
    n=4; rng=random.Random(70000+n*13)
    for trial in range(150000):
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
        if trial==5:
            return A,Cc,L0,N,d,n
    return None


def main():
    print("=== 检验：rho=1 构造是否要求基行平行？ ===\n")
    a=get_c19()
    if a: describe("c19 实例（531,441 全枚举**无解**）", *a)
    b=get_c28()
    if b: describe("c28 实例（稀疏但**有解**，80/624 个）", *b)
    print("【判读】")
    print("  若 c19 基行**不平行**且 c28 基行**平行** ⟹ H2 成立")
    print("     ⟹ rho=1 构造（从而有解）⟺ 基行平行 ∧ 行数足够")
    print("     ⟹ 而 c6′ 曾猜『平行 ⟹ NO』—— 恰好**相反**！")


if __name__=="__main__":
    main()
