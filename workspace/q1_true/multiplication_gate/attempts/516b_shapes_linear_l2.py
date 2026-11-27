"""516b：对多个 l1 形状，l2 取 9 参数一次式，解 D1(gate)=0 并看 D2。"""
import sympy as sp

x, y, z = sp.symbols('x y z')
a0, a1, a2, b0, b1, b2, c0, c1, c2, p, q, r = sp.symbols('a0 a1 a2 b0 b1 b2 c0 c1 c2 p q r')
r1 = sp.Matrix([[1, 0, 0]])
r2 = sp.Matrix([[1 - y, 0, 1]])
r3 = sp.Matrix([[p, q, r]])
A = sp.Matrix.vstack(r1, r2, r3)
l2 = sp.Matrix([[a0 + a1 * x + a2 * y, b0 + b1 * x + b2 * y, c0 + c1 * x + c2 * y]])

shapes = {
    '(z,0,x)': (z, 0, x),
    '(z,1,x)': (z, 1, x),
    '(1,z,x)': (1, z, x),
    '(z,y,x)': (z, y, x),
}
for name, sh in shapes.items():
    l1 = sp.Matrix([[sh[0], sh[1], sh[2]]])
    HA0 = sp.Matrix.vstack(l1 * A, l2 * A)
    D1g = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(0)).det().subs(z, x * y))
    eqs = [sp.expand(co) for _, co in sp.Poly(D1g, x, y).terms()]
    sol = sp.solve(eqs, [a0, a1, a2, b0, b1, b2, c0, c1, c2], dict=True)
    print('===', name, 'eqs', len(eqs), 'sol', len(sol))
    for s in sol[:1]:
        D2 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(1)).det().subs(s))
        print('   D2 =', sp.factor(D2))
