"""The q=4 rank-one gate spectral tension (attempt 280).

Two E placements are compared, with H0=[e1;e2], Y supported on e3,e4,
and the fixed block HA0 = swap(H0) (M = [[0,1],[1,0]]).

Case 1: E offsets in the fixed directions e1,e2.
  => (5a) holds automatically, det P = (lam-2)^2(lam-1)(lam+1)*det(Z),
     but rank P(2) = 2 < 3 (free eigenvalue 2).

Case 2: E offsets in the free directions e3,e4.
  => det P is not identically zero on det(Z)=0, and rank P(0)=rank P(2)=4,
     so (5b) fails.

Run: python tools/verification/c280_tension.py
"""
import sympy as sp

lam, r11, r12, r21, r22, s1, s2, t1, t2 = sp.symbols(
    'lam r11 r12 r21 r22 s1 s2 t1 t2')


def H_matrix():
    return sp.Matrix([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, r11, r12],
                      [0, 0, r21, r22]])


def HA_case1():
    # E on fixed directions e1,e2: free rows get (s1,s2,2r11,2r12)
    return sp.Matrix([[0, 1, 0, 0],
                      [1, 0, 0, 0],
                      [s1, s2, 2 * r11, 2 * r12],
                      [t1, t2, 2 * r21, 2 * r22]])


def HA_case2():
    # E on free directions e3,e4: free rows get (0,0,2r11+s1,2r12+s2)
    return sp.Matrix([[0, 1, 0, 0],
                      [1, 0, 0, 0],
                      [0, 0, 2 * r11 + s1, 2 * r12 + s2],
                      [0, 0, 2 * r21 + t1, 2 * r22 + t2]])


def main():
    H = H_matrix()
    pt = {r11: 1, r12: 2, r21: 3, r22: 6, s1: 1, s2: 2, t1: 3, t2: 4}
    assert H.subs(pt).rank() == 3

    P1 = sp.expand(lam * H - HA_case1())
    det1 = sp.factor(P1.det())
    print('case 1 det P =', det1)
    print('case 1 ranks at 0,1,2,3 =', [P1.subs(pt).subs(lam, t).rank() for t in (0, 1, 2, 3)])
    assert sp.factor(P1.det()).has(sp.Symbol('r11'))  # nonzero polynomial
    assert P1.subs(pt).subs(lam, 2).rank() == 2

    P2 = sp.expand(lam * H - HA_case2())
    det2 = sp.factor(P2.det())
    print('case 2 det P =', det2)
    print('case 2 ranks at 0,1,2,3 =', [P2.subs(pt).subs(lam, t).rank() for t in (0, 1, 2, 3)])
    assert P2.subs(pt).subs(lam, 0).rank() == 4
    assert P2.subs(pt).subs(lam, 2).rank() == 4

    print('PASS: q=4 rank-one gate shows the E-placement spectral tension')


if __name__ == '__main__':
    main()
