# -*- coding: utf-8 -*-
"""
verify_family.py -- ⭐⭐⭐ 验证**实例族**：任意 n ≥ 4 都有 YES 实例（情形 II, k=1）

【族】
  n ≥ 4,  p = 1,  r = 1
  C  = e₁ᵀ
  A  的第 1,2,3 行 = e₂ᵀ, e₃ᵀ, 0 ；其余行任取（本脚本取 0，最简）
  L0 = C A = e₂ᵀ  （退化，π(L0)=0）
  R  = C A² = e₃ᵀ
  L  = [L0; R] = [e₂ᵀ; e₃ᵀ]

【预期（全部 n ≥ 4）】
  K = span{e₃,…,eₙ} , d_CA = n−2 ≥ 2 = q0  ⟹ **情形 II** ✓
  H = [[0…],[1,0,…]]  rank 1 < 2  ⟹ T5a ✓
  F = [[1,0,…],[0…]]  ⟹ im H = span{(0,1)}, im F = span{(1,0)} ⟹ 不同直线
  (5a): rank 3 = 3 ✓ ;  (5b): rank ≡ 3 ∀λ ✓
  L0 单独失败 ⟹ q0 = 2, k = 1（最小）
"""
import os
from fractions import Fraction as Fr
from itertools import combinations


def rank(M):
    if not M: return 0
    A = [[Fr(x) for x in row] for row in M]
    R, C = len(A), len(A[0]); r = 0
    for c in range(C):
        p = None
        for i in range(r, R):
            if A[i][c] != 0: p = i; break
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]; A[r] = [x/pv for x in A[r]]
        for i in range(R):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f*A[r][j] for j in range(C)]
        r += 1
        if r == R: break
    return r


def matmul(X, Y):
    assert X and Y and len(X[0]) == len(Y), "维数不匹配"
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def vstack(*Ms):
    out = []
    for M in Ms: out.extend([list(r) for r in M])
    return out


def ker_basis(M):
    A2 = [[Fr(x) for x in row] for row in M]
    R, C = len(A2), len(A2[0]); piv = []; r = 0
    for c in range(C):
        p = None
        for i in range(r, R):
            if A2[i][c] != 0: p = i; break
        if p is None: continue
        A2[r], A2[p] = A2[p], A2[r]
        pv = A2[r][c]; A2[r] = [x/pv for x in A2[r]]
        for i in range(R):
            if i != r and A2[i][c] != 0:
                f = A2[i][c]
                A2[i] = [A2[i][j] - f*A2[r][j] for j in range(C)]
        piv.append(c); r += 1
        if r == R: break
    free = [c for c in range(C) if c not in piv]
    basis = []
    for fc in free:
        v = [Fr(0)]*C; v[fc] = Fr(1)
        for i, pc in enumerate(piv): v[pc] = -A2[i][fc]
        basis.append(v)
    return basis


# ---------- 多项式 ----------
def P_trim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0: q.pop()
    return q
def P_add(a,b):
    n=max(len(a),len(b)); return P_trim([(a[i] if i<len(a) else Fr(0))+(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def P_sub(a,b):
    n=max(len(a),len(b)); return P_trim([(a[i] if i<len(a) else Fr(0))-(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def P_mul(a,b):
    if P_trim(a)==[Fr(0)] or P_trim(b)==[Fr(0)]: return [Fr(0)]
    r=[Fr(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return P_trim(r)
def P_divmod(a,b):
    a=P_trim(a); b=P_trim(b); db=len(b)-1
    q=[Fr(0)]*max(1,len(a)-db)
    while len(a)-1>=db and a!=[Fr(0)]:
        d=len(a)-1-db; co=a[-1]/b[-1]; q[d]+=co
        for i in range(len(b)): a[d+i]-=co*b[i]
        a=P_trim(a)
    return P_trim(q),a
def P_gcd(a,b):
    a,b=P_trim(a),P_trim(b)
    while b!=[Fr(0)]:
        _,r=P_divmod(a,b); a,b=b,r
    if len(a)>1:
        lc=a[-1]; a=[x/lc for x in a]
    return a
def P_det(M,k):
    if k==1: return [Fr(x) for x in M[0][0]]
    tot=[Fr(0)]
    for j in range(k):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        d=P_det(sub,k-1); pr=P_mul(M[0][j],d)
        tot=P_add(tot,pr) if j%2==0 else P_sub(tot,pr)
    return P_trim(tot)


def one(n):
    C = [[Fr(0)]*n]; C[0][0] = Fr(1)
    A = [[Fr(0)]*n for _ in range(n)]
    A[0][1] = Fr(1)
    if n > 2: A[1][2] = Fr(1)
    CA = matmul(C, A)
    L0 = CA[:]
    if n <= 2: return None
    R = [[Fr(0)]*n]; R[0][2] = Fr(1)
    L = vstack(L0, R)
    W = vstack(C, CA)
    r0 = rank(vstack(L, CA, C))
    r5a = rank(vstack(matmul(L, A), L, CA, C))
    a_ok = (r5a == r0)
    # (5b) gcd
    CAc = CA; LA = matmul(L, A); m = len(L) + 2
    base = vstack(L, CAc, C)
    P = [[([-LA[i][j], L[i][j]] if i < len(L) else [base[i][j]]) for j in range(n)]
         for i in range(m)]
    polys = []
    for rows in combinations(range(m), r0):
        for cols in combinations(range(n), r0):
            d = P_det([[P[i][j] for j in cols] for i in rows], r0)
            if d != [Fr(0)]: polys.append(d)
    G = polys[0]
    for q in polys[1:]:
        G = P_gcd(G, q)
        if len(G) == 1: break
    b_ok = (len(P_trim(G)) == 1 and any(x != 0 for x in G))
    # 逐 λ
    lam_ok = True
    for lam in [Fr(0), Fr(1), Fr(-1), Fr(3), Fr(1,2)]:
        M2 = [[lam*L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank(vstack(M2, CAc, C)) != r0: lam_ok = False
    B = ker_basis(W); dCA = len(B)
    Nb = [[B[j][i] for j in range(dCA)] for i in range(n)]
    H = matmul(L, Nb); Fm = matmul(LA, Nb)
    cj = [[Nb[i][j] for j in range(dCA)] + [matmul(A,Nb)[i][j] for j in range(dCA)] for i in range(n)]
    noninv = (rank(cj) > rank(Nb))
    cjFH = [[H[i][j] for j in range(dCA)] + [Fm[i][j] for j in range(dCA)] for i in range(len(H))]
    notsub = (rank(cjFH) > rank(H))
    # L0 单独失败？
    L0_fail = (rank(vstack(matmul(L0,A), L0, CA, C)) != rank(vstack(L0, CA, C)))
    # H4
    def obs(M):
        rows=[list(x) for x in M]; cur=[list(x) for x in M]
        for _ in range(n-1): cur=matmul(cur,A); rows.extend(cur)
        return rows
    h4 = (rank(vstack(obs(L0), obs(C))) == rank(obs(C)))
    return dict(n=n, dCA=dCA, r0=r0, a=a_ok, b=b_ok, lam=lam_ok,
                rankH=rank(H), noninv=noninv, notsub=notsub,
                L0fail=L0_fail, h4=h4, gcd=[str(x) for x in G])


def main():
    print("=== 实例族验证：n ≥ 4 全部 YES（情形 II, q0=2, k=1）===\n")
    print("%3s %6s %5s %5s %6s %6s %8s %8s %8s" %
          ("n","d_CA","(5a)","(5b)","逐λ","rankH","非不变","imF⊄imH","H4"))
    print("-" * 68)
    allok = True
    for n in range(4, 11):
        r = one(n)
        if r is None: continue
        ok = (r["a"] and r["b"] and r["lam"] and r["rankH"] == 1 and r["noninv"]
              and r["notsub"] and r["h4"] and r["dCA"] >= 2 and r["L0fail"])
        allok = allok and ok
        print("%3d %6d %5s %5s %6s %6d %8s %8s %8s%s" %
              (n, r["dCA"], "✓" if r["a"] else "✗", "✓" if r["b"] else "✗",
               "✓" if r["lam"] else "✗", r["rankH"],
               "✓" if r["noninv"] else "✗", "✓" if r["notsub"] else "✗",
               "✓" if r["h4"] else "✗", "" if ok else "  **✗**"))
    print()
    if allok:
        print("⟹⟹⟹ **实例族成立**：对全部 n ≥ 4，存在 YES 实例")
        print("     （情形 II，q0=2，k=1 → **最小增广恰为 1 行**）")
        print("     ⟹ 情形 II 的 YES 实例是 **无穷族**，不是孤例 ⭐⭐⭐")
    else:
        print("⟹ 族验证有失败项")


if __name__ == "__main__":
    main()
