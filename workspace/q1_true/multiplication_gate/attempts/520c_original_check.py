"""520c：用原始矩阵核验 sound gadget（n=5,q=3）在两个点上的 (5a)/(5b)。"""
import sympy as sp

x, y, z, lam = sp.symbols('x y z lam')
A = sp.Matrix([[-2, 0, 0, 0, 0],
               [0, -2, 0, 0, 0],
               [0, 0, 2, 0, 0],
               [2 * y, 2, -2, 0, 0],
               [0, 0, 0, 1, 0]])
C = sp.Matrix([[0, 0, 0, 0, 1]])
L0 = sp.Matrix([[z, x, 0, -1, 0],
                [y, 1, 0, 2, 0],
                [0, 0, 1, 2, 0]])

for (xv, yv, zv, tag) in [(2, 3, 6, 'gate z=xy'), (2, 3, 7, 'off-gate z!=xy')]:
    sub = {x: xv, y: yv, z: zv}
    L = L0.subs(sub)
    Am = A.subs(sub)
    Cm = C
    LCA = sp.Matrix.vstack(L, Cm * Am, Cm)
    r0 = LCA.rank()
    LA = L * Am
    five_a = sp.Matrix.vstack(LA, L, Cm * Am, Cm)
    r5a = five_a.rank()
    ranks = []
    for lv in [0, 1, 2, 3, 5]:
        P = sp.Matrix.vstack(lam * L - LA, Cm * Am, Cm).subs(lam, lv)
        ranks.append(P.rank())
    print(tag, 'rank[L;CA;C]=', r0, 'rank[LA;L;CA;C]=', r5a, 'ranks(lambda=0,1,2,3,5)=', ranks)
