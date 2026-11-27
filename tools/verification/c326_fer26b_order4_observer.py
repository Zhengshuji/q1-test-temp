"""c326_fer26b_order4_observer.py

Verification of the explicit order-4 functional observer for the example of
arXiv:2609.37992 Sec. VII (the example whose claimed nu_min = 5 is refuted by
c325).  Everything below is exact rational arithmetic.

Objects (as supplied):
  L4 : 4 x 8 augmented functional matrix, first two rows = L of the paper,
  Z4 : 8 x 2, the nullspace matrix of c325,
  E  : 4 x 2,  F : 4 x 4,  G : 4 x 2,  H : 4 x 1,  P = L4 - E C,
  B  = e1 + e8.

Checks:
  (1) rank[C; L4] = 6 and ker[C; L4] = im Z4,
  (2) P A - F P - G C = 0            (observer Sylvester equation),
  (3) H = P B                        (feedthrough),
  (4) F is Hurwitz, by exact Routh-Hurwitz on its characteristic polynomial.
"""

import sympy as sp

A = sp.Matrix([
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, -1, 1, 0, 0, 0, 0, -1],
    [1, 0, -1, 1, 0, 0, 1, -1],
    [-1, -1, 0, -2, 0, 0, 0, 0],
    [0, 0, 0, 0, -2, 0, 0, 1],
    [0, 0, 0, 0, 0, -2, 1, 0],
    [0, 0, 0, 0, 0, -1, -2, 1],
    [0, 0, 0, 0, 0, 0, 1, -2]])
C = sp.Matrix([[-2, -2, 2, -2, -1, 0, 1, -3],
               [0, 0, 1, 2, 2, 3, -1, -2]])
L = sp.Matrix([[-2, -1, -2, -3, -1, 3, 2, 0],
               [1, -1, -2, 1, 0, 2, 0, 1]])

R = sp.Rational

L4 = sp.Matrix([
    [-2, -1, -2, -3, -1, 3, 2, 0],
    [1, -1, -2, 1, 0, 2, 0, 1],
    [R(-42919, 32067), R(-55096, 10689), 1, 0, 0, 0, 0, 0],
    [R(3283, 4581), R(118, 1527), 0, 1, 0, 0, 0, 0]])

j = sp.Matrix([390, -97, 22, -272, 419, -58, 252, -55])
w = sp.Matrix([-369, 174, 403, 251, -893, 368, -501, 362])
Z4 = sp.Matrix.hstack(j, w)

E = sp.Matrix([
    [R(33402, 8119), R(-2075, 8119)],
    [R(25283, 8119), R(-2075, 8119)],
    [R(1510585844, 260351973), R(-125950181, 260351973)],
    [R(2123410, 37193139), R(-384916, 37193139)]])

F = sp.Matrix([
    [R(25283, 8119), R(-58887, 8119), R(5278, 8119), R(78307, 8119)],
    [R(33402, 8119), R(-58887, 8119), R(5278, 8119), R(78307, 8119)],
    [R(1770937817, 260351973), R(-2215989256, 260351973), R(-84104118, 260351973),
     R(4528570590, 260351973)],
    [R(2123410, 37193139), R(-3085700, 37193139), R(1732122, 37193139),
     R(-40597911, 37193139)]])

G = sp.Matrix([
    [R(-86747912, 65918161), R(42418094, 65918161)],
    [R(118524765, 65918161), R(25571169, 65918161)],
    [R(15504215545115, 2113797668787), R(873308471959, 2113797668787)],
    [R(85428098920, 301971095541), R(-1395320500, 301971095541)]])

H = sp.Matrix([R(146622, 8119), R(138503, 8119),
               R(6952569497, 260351973), R(36501895, 37193139)])

B = sp.zeros(8, 1)
B[0, 0] = 1
B[7, 0] = 1


def main() -> int:
    ok = True

    # (0) L4 really extends L
    assert L4[:2, :] == L, "first two rows of L4 must be L"
    print("(0) first two rows of L4 equal L:", L4[:2, :] == L)

    # (1) rank and kernel
    st = sp.Matrix.vstack(C, L4)
    print("(1) rank[C;L4] =", st.rank(), " (expected 6)")
    print("    dim ker[C;L4] =", 8 - st.rank(), " (expected 2 = rank Z4)")
    print("    Z4 in ker[C;L4]:", (C * Z4).is_zero_matrix and (L4 * Z4).is_zero_matrix)
    ok &= (st.rank() == 6)

    # (2) Sylvester equation P A - F P - G C = 0
    P = L4 - E * C
    syl = sp.simplify(P * A - F * P - G * C)
    print("(2) P A - F P - G C is zero:", syl.is_zero_matrix)
    if not syl.is_zero_matrix:
        print("    residual:", syl.tolist())
    ok &= syl.is_zero_matrix

    # (3) feedthrough
    hh = sp.simplify(P * B - H)
    print("(3) H = P B :", hh.is_zero_matrix)
    if not hh.is_zero_matrix:
        print("    difference:", [sp.nsimplify(x) for x in hh])
    ok &= hh.is_zero_matrix

    # (4) F Hurwitz, exact Routh-Hurwitz
    lam = sp.symbols("lam")
    chi = sp.expand(F.charpoly(lam).as_expr())
    print("(4) char poly of F:", chi)
    coeffs = sp.Poly(chi, lam).all_coeffs()      # a4..a0, a4 = 1
    a4, a3, a2, a1, a0 = [sp.nsimplify(c) for c in coeffs]
    print("    a3,a2,a1,a0 =", a3, a2, a1, a0)
    row2 = a3 * a2 - a1
    row3 = a3 * a2 * a1 - a1**2 - a3**2 * a0
    print("    a3*a2 - a1            =", sp.nsimplify(row2),
          " >0:", row2 > 0)
    print("    a3a2a1 - a1^2 - a3^2a0 =", sp.nsimplify(row3),
          " >0:", row3 > 0)
    hurwitz = (a4 > 0) and (a3 > 0) and (a2 > 0) and (a1 > 0) and (a0 > 0) \
        and (row2 > 0) and (row3 > 0)
    print("    Hurwitz (exact Routh-Hurwitz):", hurwitz)
    ok &= hurwitz

    print()
    print("VERDICT:", "all checks pass -- the order-4 observer is valid" if ok
          else "SOME CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
