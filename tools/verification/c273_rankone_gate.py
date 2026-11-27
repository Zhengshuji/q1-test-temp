"""Compressed rank-one section gate (attempt 273).

H0 = [e1; e2] (2x4), Y = 2x4 with only columns 3,4 used:
    Y = [[0, 0, r11, r12],
         [0, 0, r21, r22]]
Then H = [H0; Y] is 4x4, and
    rank H = 3  <=>  r11*r22 - r12*r21 = 0.
On the chart r11=1 this is r22 = r12*r21.

Run: python tools/verification/c273_rankone_gate.py
"""
import sympy as sp

r11, r12, r21, r22 = sp.symbols('r11 r12 r21 r22')


def main():
    H0 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    Y = sp.Matrix([[0, 0, r11, r12], [0, 0, r21, r22]])
    H = sp.Matrix.vstack(H0, Y)
    det = sp.factor(sp.expand(H.det()))
    print('det H =', det)
    assert det == r11 * r22 - r12 * r21

    # rank is 3 iff det=0, for a generic specialization
    pt = {r11: 1, r12: 2, r21: 3, r22: 6}
    print('rank H at (1,2,3,6) =', H.subs(pt).rank())
    assert H.subs(pt).rank() == 3

    pt2 = {r11: 1, r12: 2, r21: 3, r22: 7}
    print('rank H at (1,2,3,7) =', H.subs(pt2).rank())
    assert H.subs(pt2).rank() == 4

    # chart r11=1: det=0 <=> r22 = r12*r21
    chart = sp.factor(det.subs(r11, 1))
    print('chart det =', chart)
    assert sp.simplify(chart - (r22 - r12 * r21)) == 0
    print('PASS: rank-one section gives det = r11*r22 - r12*r21')


if __name__ == '__main__':
    main()
