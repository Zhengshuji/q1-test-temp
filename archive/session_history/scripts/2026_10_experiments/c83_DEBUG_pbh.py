r"""
c83_DEBUG_pbh.py -- 用 sympy 作为独立裁判，定位 c82 的 2/40 不一致

造一个 ρ=1<d=3 的实例，分别用：
  (A) 我的 cond_5b     （铅笔 ρ 阶子式 gcd）
  (B) 我的 pbh_form     （[Λᵀ−λI | N] 的 q 阶子式 gcd）
  (C) sympy 独立计算    （两者的行列式多项式 gcd）
判定谁对。
"""
import os, io, contextlib, itertools
from fractions import Fraction as Fr
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

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

def to_sp(x):
    return sp.Rational(x.numerator, x.denominator)

def main():
    lam = sp.symbols("lam")
    d, q = 3, 4
    # 构造：M 秩 1（后 3 行是第 0 行倍数）
    M = [
        [Fr(1), Fr(2), Fr(0)],
        [Fr(1), Fr(2), Fr(0)],
        [Fr(-1), Fr(-2), Fr(0)],
        [Fr(0), Fr(0), Fr(0)],
    ]
    print("M =", [[str(x) for x in r] for r in M], " rank =", rk(M))
    Lam = [
        [Fr(0), Fr(1), Fr(0), Fr(0)],
        [Fr(0), Fr(0), Fr(1), Fr(0)],
        [Fr(0), Fr(0), Fr(0), Fr(1)],
        [Fr(1), Fr(0), Fr(0), Fr(0)],
    ]
    F = mm(Lam, M)
    print("F = ΛM =", [[str(x) for x in r] for r in F])
    rho = rk(M)
    print("ρ =", rho)

    # ---- (A) 我的 cond_5b：ρ 阶子式（这里是 1 阶 = 各元素）的 gcd
    entries = []
    for i in range(q):
        for j in range(d):
            e = sp.Rational(to_sp(M[i][j]))*lam - sp.Rational(to_sp(F[i][j]))
            if e != 0: entries.append(sp.expand(e))
    print("\n铅笔元素 (= 1 阶子式):", entries)
    gA = sp.gcd_list(entries) if entries else sp.Integer(0)
    print("(A) gcd of 1-minors =", sp.factor(gA), " 常数？", gA.is_number)

    # ---- (B) 我的 pbh_form：[Λᵀ − λI | N]
    Mt = [[M[i][j] for i in range(q)] for j in range(d)]
    Ns = nullspace_rows(Mt)
    print("\nker Mᵀ 的基 (维数 %d):" % len(Ns), [[str(x) for x in v] for v in Ns])
    # 组装 sympy 矩阵
    cols = q + len(Ns)
    Msym = sp.zeros(q, cols)
    for i in range(q):
        for j in range(q):
            a = to_sp(Lam[j][i])
            Msym[i, j] = sp.Rational(a) - (lam if i==j else 0)
        for t in range(len(Ns)):
            Msym[i, q+t] = sp.Rational(to_sp(Ns[t][i]))
    print("矩阵 [Λᵀ−λI | N] =")
    sp.pprint(Msym)
    minors = []
    for cs in itertools.combinations(range(cols), q):
        m = Msym[:, list(cs)].det()
        m = sp.expand(m)
        if m != 0: minors.append(m)
    gB = sp.gcd_list(minors) if minors else sp.Integer(0)
    print("\n(B) gcd of q-minors =", sp.factor(gB), " 常数？", gB.is_number)

    # ---- (C) 正确的 (5b)：任意 λ 处 rank(λM − F) = ρ
    P = sp.zeros(q, d)
    for i in range(q):
        for j in range(d):
            P[i, j] = sp.Rational(to_sp(M[i][j]))*lam - sp.Rational(to_sp(F[i][j]))
    print("\n铅笔 λM−F =")
    sp.pprint(P)
    print("rank over Q(λ) =", P.rank())
    print("\n判定：")
    print("  (A) 说 (5b) =", gA.is_number)
    print("  (B) 说 PBH  =", gB.is_number)
    print("  真实 rank = %d vs ρ = %d  →  (5b) 真实值 = %s" %
          (P.rank(), rho, P.rank()==rho))


if __name__=="__main__":
    main()
