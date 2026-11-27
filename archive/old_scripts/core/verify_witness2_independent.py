# -*- coding: utf-8 -*-
"""
verify_witness2_independent.py -- ⭐⭐⭐ **k=1** 见证的完全独立验证

【显式实例（可手算！）】
  n=6, p=1, r=1, q0=2, k=1, d_CA=4（情形 II）
  C  = e₁ᵀ = (1,0,0,0,0,0)
  A  的前三行 = e₂ᵀ, e₃ᵀ, 0（其余三行任意）
  L0 = C A = e₂ᵀ                ⟹ π(L0)=0（退化）
  R  = e₃ᵀ,  L = [L0; R] = [e₂ᵀ; e₃ᵀ]

【手算】
  CA = e₂ᵀ, CA² = e₃ᵀ, CA³ = 0
  K  = ker[C;CA] = span{e₃,e₄,e₅,e₆},  d_CA = 4
  CA²|_K = e₃ᵀ|_K ≠ 0   ⟹ **非 A-不变** ✓
  H = L·N = [[0,0,0,0],[1,0,0,0]]        rank 1 < q0=2  ⟹ T5a ✓
  F = LA·N = [[1,0,0,0],[0,0,0,0]]
  im H = span{(0,1)},  im F = span{(1,0)}  ⟹ **不同直线** ⟹ (S) 成立 ⟹ (5b) 可成立
  (5a): rank[LA;L;CA;C] = 3 = rank[L;CA;C] ✓
  (5b): [λL−LA;CA;C] 的行 = λe₂ᵀ−e₃ᵀ, λe₃ᵀ, e₂ᵀ, e₁ᵀ ⟹ 恒 rank 3 ✓

本脚本：用**全新实现**逐项验证（不用项目库）
"""
import os
from fractions import Fraction as Fr
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- 独立实现 ----------
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

# ---------- 多项式（验证 (5b) 的 gcd 判据）----------
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


def main():
    n, p = 6, 1
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    # A：前三行 e2^T, e3^T, 0；其余任意（取一个具体的）
    A = [[Fr(0)]*n for _ in range(n)]
    A[0][1] = Fr(1)          # row0 = e2^T
    A[1][2] = Fr(1)          # row1 = e3^T
    A[2] = [Fr(0)]*n         # row2 = 0
    A[3] = [Fr(1), Fr(0), Fr(0), Fr(1), Fr(0), Fr(0)]
    A[4] = [Fr(0), Fr(1), Fr(0), Fr(0), Fr(1), Fr(0)]
    A[5] = [Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(1)]

    CA = matmul(C, A)
    L0 = CA[:]                                          # e2^T
    R = [[Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]]    # e3^T
    L = vstack(L0, R)

    print("=== k=1 见证的独立验证 ===\n")
    print("C  =", [[str(x) for x in r] for r in C])
    print("A  =", [[str(x) for x in r] for r in A])
    print("L0 =", [[str(x) for x in r] for r in L0], "  (= C A = e2^T)")
    print("R  =", [[str(x) for x in r] for r in R], "  (= e3^T)")
    print()

    ok = {}
    ok["H1 rank C = p"] = (rank(C) == p)
    ok["H2 rank L0 = r"] = (rank(L0) == 1)
    ok["H3 rank[L0;C] = r+p"] = (rank(vstack(L0, C)) == 2)

    def obs(M, A, n):
        rows = [list(x) for x in M]; cur = [list(x) for x in M]
        for _ in range(n-1): cur = matmul(cur, A); rows.extend(cur)
        return rows
    ok["H4 row(O_L0) ⊆ row(O_C)"] = (rank(vstack(obs(L0,A,n), obs(C,A,n))) == rank(obs(C,A,n)))

    W = vstack(C, CA)
    r0 = rank(vstack(L, CA, C))
    r5a = rank(vstack(matmul(L,A), L, CA, C))
    ok["(5a)"] = (r5a == r0)
    ok["rank[L;CA;C] = 3"] = (r0 == 3)

    # (5b) gcd 判据 + 逐 λ
    CAc = matmul(C, A); LA = matmul(L, A); m = len(L) + 2
    base = vstack(L, CAc, C)
    P = []
    for i in range(m):
        row = []
        for j in range(6):
            row.append([-LA[i][j], L[i][j]] if i < len(L) else [base[i][j]])
        P.append(row)
    polys = []
    for rows in combinations(range(m), r0):
        for cols in combinations(range(6), r0):
            d = P_det([[P[i][j] for j in cols] for i in rows], r0)
            if d != [Fr(0)]: polys.append(d)
    G = polys[0]
    for q in polys[1:]:
        G = P_gcd(G, q)
        if len(G) == 1: break
    ok["(5b) gcd 常数"] = (len(P_trim(G)) == 1 and any(x != 0 for x in G))
    print("(5b) 子式数 =", len(polys), " gcd =", [str(x) for x in G])

    lam_ok = True
    for lam in [Fr(0), Fr(1), Fr(-1), Fr(2), Fr(-2), Fr(5), Fr(1,2), Fr(-3,7)]:
        M = [[lam*L[i][j] - LA[i][j] for j in range(6)] for i in range(len(L))]
        if rank(vstack(M, CAc, C)) != r0: lam_ok = False
    ok["(5b) 逐 λ = r0"] = lam_ok

    B = ker_basis(W); dCA = len(B)
    ok["情形 II: d_CA ≥ q0=2"] = (dCA >= 2)
    ok["d_CA = 4"] = (dCA == 4)
    Nb = [[B[j][i] for j in range(dCA)] for i in range(n)]
    H = matmul(L, Nb); Fm = matmul(LA, Nb)
    ok["T5a: rank H = 1 < 2"] = (rank(H) == 1)
    ok["degenerate: π(L0)=0"] = (all(x == 0 for x in H[0]))
    AN = matmul(A, Nb)
    cj = [[Nb[i][j] for j in range(dCA)] + [AN[i][j] for j in range(dCA)] for i in range(n)]
    ok["非 A-不变"] = (rank(cj) > rank(Nb))
    # im F ⊄ im H
    cjFH = [[H[i][j] for j in range(dCA)] + [Fm[i][j] for j in range(dCA)] for i in range(len(H))]
    ok["im F ⊄ im H（机制失效）"] = (rank(cjFH) > rank(H))

    print()
    print("H =", [[str(x) for x in r] for r in H])
    print("F =", [[str(x) for x in r] for r in Fm])
    print()
    allok = True
    for k, v in ok.items():
        print("  %-30s : %s" % (k, "✓" if v else "**✗**"))
        allok = allok and v
    print()
    if allok:
        print("⟹⟹⟹ **k=1 见证经完全独立验证（全部通过）** ⭐⭐⭐")
        print("     ⟹ 非不变 + 退化 + k=1（情形 II）满足 H1–H4 ∧ (5a) ∧ (5b)")
        print("     ⟹ **c6′ 在 k≥1 的硬度相关范围也假**")
    else:
        print("⟹ **验证未通过**")


if __name__ == "__main__":
    main()
