r"""
c40_quotient_spec.py -- ⭐⭐⭐⭐ 检验必要性的机制缺口

【必要性的机制】
   α0 ∉ V ⟹ α0 在商 Q = ℝ^d/V 上有非零分量 ᾱ0
   模 V 的铅笔含 ᾱ0(λI − Ā') 项
   ⟹ 若 Ā' 在 Q 上有**有理特征值** μ ⟹ λ=μ 处秩降 ⟹ (5b) 失败 ⟹ NO
   缺口：Ā' **是否**总有有理特征值？

【本脚本】对每个实例：
   算 V、Q、Ā' 的 charpoly
   检查 charpoly(A') 与 charpoly(Ā') 的有理根
   与 α0∈V、成功率对照
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr
from math import gcd as ig

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

def invariant_closure(M, Ap, d):
    basis=row_space_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d:
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

def extend_basis(Vb, d):
    """把 Vb（行向量组）扩充为 ℝ^d 的基"""
    basis=[r[:] for r in Vb]
    for j in range(d):
        e=[Fr(1) if i==j else Fr(0) for i in range(d)]
        cand=basis+[e]
        if rk(cand)==len(basis)+1:
            basis.append(e)
        if len(basis)==d: break
    return basis

def quotient_matrix(Vb, Ap, d):
    """Q = ℝ^d/V 上的 Ā'（返回 obs 补维数的方阵）"""
    full=extend_basis(Vb, d)
    dv=len(Vb); dq=d-dv
    comp=full[dv:]                      # 补基
    # 投影到商（用 full 基下去掉 V 部分）
    def proj(v):
        # 求 v 在 full 下的坐标，取后 dq 个
        # 解 coords·full = v
        n=d; m=d
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
        return co[dv:]
    Aq=[]
    for j in range(dq):
        w=comp[j]
        wAp=[sum(w[t]*Ap[t][j2] for t in range(d)) for j2 in range(d)]
        Aq.append(proj(wAp))
    return Aq

def charpoly(M):
    n=len(M)
    if n==0: return [Fr(1)]
    I=[[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
    cs=[]; Acur=[r[:] for r in I]
    for k in range(1,n+1):
        Mk=mm(M,Acur)
        c=-sum(Mk[i][i] for i in range(n))/k
        cs.append(c)
        Acur=[[Mk[i][j]+(c if i==j else Fr(0)) for j in range(n)] for i in range(n)]
    return [Fr(1)]+[cs[-1-i] for i in range(len(cs))]

def rat_roots(coef):
    c=Pt([x for x in coef])
    if len(c)<=1: return []
    if len(c)==2: return ["(线性，有根)"]
    if c[0]==0: return ["0"]
    L=1
    for x in c:
        dd=x.denominator; L=L*dd//ig(L,dd)
    ints=[int(x*L) for x in c]
    g=0
    for x in ints: g=ig(g,abs(x))
    if g: ints=[x//g for x in ints]
    if ints[0]==0: return ["0"]
    def divs(m):
        m=abs(m); out=[]
        for i in range(1,int(m**0.5)+1):
            if m%i==0:
                out.append(i)
                if i!=m//i: out.append(m//i)
        return out
    out=[]
    for pnum in divs(ints[0])[:40]:
        for qden in divs(abs(ints[-1]))[:20]:
            for s in (1,-1):
                x=Fr(s*pnum,qden); v=Fr(0)
                for cc in reversed(ints): v=v*x+cc
                if v==0: out.append(str(x))
    return sorted(set(out))

def Pt(p):
    q=list(p)
    while len(q)>1 and q[-1]==0: q.pop()
    return q


def main():
    print("=== 必要性机制：α0∉V 时 Ā' 在商上是否有有理特征值？ ===\n")
    hdr = "%-12s %3s %5s %6s %9s %14s %12s" % ("实例","d","obs","α0∈V","成功率","rat.roots(A')","rat.roots(Ā')")
    print(hdr); print("-"*len(hdr))
    for (n,seed,trials) in [(4,70052,[0,1,5]),(5,123455,[4]),(5,70065,[0,7])]:
        rng=random.Random(seed)
        for trial in range(300000):
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
            if trial not in trials: continue
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            V=invariant_closure(R, Ap, d)
            a0=mm(L0,N)[0]
            a0in = (rk([r[:] for r in V]+[a0[:]])==len(V)) if V else all(x==0 for x in a0)
            cpA=charpoly(Ap)
            rA=rat_roots(cpA)
            if len(V)==d:
                Aq=None; rQ="-"
            else:
                Aq=quotient_matrix(V, Ap, d)
                rQ=rat_roots(charpoly(Aq)) if Aq else "-"
            print("%-12s %3d %5d %6s %9s %14s %12s" %
                  ("n=%d t=%d"%(n,trial), d, len(V),
                   "Y" if a0in else "N", "(见前)",
                   str(rA)[:14], str(rQ)[:12]))
    print()
    print("【判读】若 α0∉V 的实例都有 rat.roots(Ā') ≠ ∅ ⟹ 机制缺口可补（V 的最小性或许保证）")


if __name__=="__main__":
    main()
