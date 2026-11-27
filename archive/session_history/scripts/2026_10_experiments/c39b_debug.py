r"""c39b_debug.py -- 调试 c39 的构造：为何 ns=0"""
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

def solve_full(Mat, rhs):
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
    x0=[Fr(0)]*n
    for i,c in enumerate(piv):
        x0[c]=A2[i][n]
    free=[c for c in range(n) if c not in piv]
    kern=[]
    for f in free:
        v=[Fr(0)]*n; v[f]=Fr(1)
        for i,c in enumerate(piv):
            v[c]=-A2[i][f]
        kern.append(v)
    return x0, kern

# 复现 n=4 t=0
n=4; seed=70052; target=0
rng=random.Random(seed)
found=None
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
    if trial==target:
        found=(A,Cc,L0,N,d); break

A,Cc,L0,N,d=found
print("n=4 t=0: d =", d)
print("N 形状：%d 行 × %d 列" % (len(N), len(N[0])))
print("rank(N) =", rk(N))
print("N =", [[str(x) for x in r] for r in N])
print()
ee=[Fr(1)]+[Fr(0)]*(d-1)
res=solve_full(N, ee)
print("solve_full(N, e0) =", "None（不相容）" if res is None else "有解")
if res:
    x0,kern=res
    print("  x0 =", [str(x) for x in x0])
    print("  核基个数 =", len(kern))
    # 验证残差
    val=[sum(x0[i]*N[i][j] for i in range(n)) for j in range(d)]
    print("  x0·N =", [str(x) for x in val])
    print("  期望 =", [str(x) for x in ee])
    print("  一致？", val==[Fr(x) for x in ee])
