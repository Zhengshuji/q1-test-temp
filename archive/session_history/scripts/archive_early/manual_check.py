"""
手工核实：A = diag(1,2), C = [1,0], L0 = [e1], L = [a,b] (b≠0)
在 s = 2 处 (S) 是否真的失败？
"""
from fractions import Fraction as F


def rref(M):
    M = [row[:] for row in M]
    if not M:
        return M, []
    nrow, ncol = len(M), len(M[0])
    piv, r = [], 0
    for c in range(ncol):
        p = None
        for i in range(r, nrow):
            if M[i][c] != 0:
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == nrow:
            break
    return M, piv


def rank_exact(M):
    if not M or not M[0]:
        return 0
    return len(rref(M)[1])


a, b = F(1), F(1)
A = [[F(1), F(0)], [F(0), F(2)]]
C = [[F(1), F(0)]]
CA = [[F(1), F(0)]]          # C*A = [1,0]*diag(1,2) = [1,0]
L = [[a, b]]

print("手工核实")
print(f"  A = diag(1,2), C = [1,0], CA = [1,0], L = [{a},{b}]")
print()

for s in (F(0), F(1), F(2), F(3)):
    # sL - LA   (1x2)
    LA = [[a * A[0][0], b * A[1][1]]]          # [a, 2b]
    sl = [[s * L[0][0] - LA[0][0], s * L[0][1] - LA[0][1]]]
    left = sl + C + CA
    right = L + C + CA
    print(f"  s = {s}:")
    print(f"     sL - LA = {[[str(x) for x in r] for r in sl]}")
    print(f"     left  = {[[str(x) for x in r] for r in left]}  rank = {rank_exact(left)}")
    print(f"     right = {[[str(x) for x in r] for r in right]}  rank = {rank_exact(right)}")
    print(f"     (5b) 在此 s 处: {rank_exact(left) == rank_exact(right)}")
    print()

print("=" * 70)
print("另取 L = [1, 0.5]（b ≠ 0，与上一例不同）")
a2, b2 = F(1), F(1, 2)
L2 = [[a2, b2]]
for s in (F(0), F(1), F(2)):
    LA2 = [[a2 * A[0][0], b2 * A[1][1]]]
    sl2 = [[s * L2[0][0] - LA2[0][0], s * L2[0][1] - LA2[0][1]]]
    left2 = sl2 + C + CA
    right2 = L2 + C + CA
    print(f"  s={s}: sL-LA={[[str(x) for x in r] for r in sl2]}  "
          f"rank_left={rank_exact(left2)} rank_right={rank_exact(right2)}  "
          f"ok={rank_exact(left2)==rank_exact(right2)}")
