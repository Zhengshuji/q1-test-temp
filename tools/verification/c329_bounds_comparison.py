"""Compare the new spectral lower bound with the older quotient-space bound
   q_min >= max(r + eps, rho + max(c0,1))     (proof/lower_bound, old framework)
on the example of Appendix B.

Old framework: J = row[C;CA]; for a solution L, V = row L, c = dim(V cap J),
rho = dim pi(V) = dim V - c; c0 = dim(row L0 cap J); eps = 1 if L0 is not a solution.
New framework: q_min >= r0 + max(0, rank[U0;V0] - s0 + 1).
"""

import sympy as sp

A = sp.Matrix([
 [0,1,0,1,0,0,0,0],[0,-1,1,0,0,0,0,-1],[1,0,-1,1,0,0,1,-1],[-1,-1,0,-2,0,0,0,0],
 [0,0,0,0,-2,0,0,1],[0,0,0,0,0,-2,1,0],[0,0,0,0,0,-1,-2,1],[0,0,0,0,0,0,1,-2]])
C = sp.Matrix([[-2,-2,2,-2,-1,0,1,-3],[0,0,1,2,2,3,-1,-2]])
L0 = sp.Matrix([[-2,-1,-2,-3,-1,3,2,0],[1,-1,-2,1,0,2,0,1]])
R = sp.Rational
Rrows = sp.Matrix([[R(-42919,32067),R(-55096,10689),1,0,0,0,0,0],
                   [R(3283,4581),R(118,1527),0,1,0,0,0,0]])
L = sp.Matrix.vstack(L0, Rrows)

Jm = sp.Matrix.vstack(C, C*A)              # row space J
j = Jm.rank()

def cap(Arows, Brows):
    """dim(row A cap row B) = rank(A) + rank(B) - rank[A;B]"""
    return Arows.rank() + Brows.rank() - sp.Matrix.vstack(Arows, Brows).rank()

c0 = cap(L0, Jm)
c  = cap(L, Jm)
rho = L.rank() - c

print("j = dim J =", j)
print("c0 = dim(row L0 cap J) =", c0)
print("c  = dim(row L  cap J) =", c, "  rho = q - c =", rho)
print("old bound on this solution: rho + max(c0,1) =", rho + max(c0, 1))
print("old bound, min over rho unknown; r + eps =", 2 + 1)

# new bound
N = sp.Matrix.hstack(*sp.Matrix.vstack(C, C*A).nullspace())
U0 = L0*N; V0 = L0*A*N
rankUV = sp.Matrix.vstack(U0, V0).rank()
s0 = sp.Matrix.hstack(L0*N, L0*A*N).rank()
new = 2 + max(0, rankUV - s0 + 1)
print()
print("rank[U0;V0] =", rankUV, " s0 =", s0)
print("new bound: r0 + max(0, rank[U0;V0] - s0 + 1) =", new)
print()
print("q_min (proved elsewhere) = 4")
