"""517：改 r2=(1,0,y)（r1=(1,0,0)），常数 l2，检查五种 l1 形状的 D1(gate)=0 与 D2。"""
import sympy as sp

x, y, z = sp.symbols('x y z')
A1, A2, A3 = sp.symbols('A1 A2 A3')
a, b, c, p, q, r = sp.symbols('a b c p q r')
r1 = sp.Matrix([[1, 0, 0]])
r2 = sp.Matrix([[1, 0, y]])
r3 = sp.Matrix([[p, q, r]])
A = sp.Matrix.vstack(r1, r2, r3)
l1 = sp.Matrix([[A1, A2, A3]])
l2 = sp.Matrix([[a, b, c]])
HA0 = sp.Matrix.vstack(l1 * A, l2 * A)
D1g = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(0)).det().subs(z, x * y))
D2 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(1)).det())

shapes = {
    '(z,x,0)': (z, x, 0),
    '(z,x,1)': (z, x, 1),
    '(z,y,1)': (z, y, 1),
    '(z,0,x)': (z, 0, x),
    '(1,z,x)': (1, z, x),
}
for name, sh in shapes.items():
    d1 = sp.expand(D1g.subs({A1: sh[0], A2: sh[1], A3: sh[2]}))
    d2 = sp.expand(D2.subs({A1: sh[0], A2: sh[1], A3: sh[2]}))
    eqs = [sp.expand(co) for _, co in sp.Poly(d1, x, y).terms()]
    sol = sp.solve(eqs, [b, c, q, p], dict=True)
    print('===', name, 'eqs', len(eqs), 'sol', len(sol))
    for s in sol[:1]:
        print('   D2 =', sp.factor(sp.expand(d2.subs(s))))
