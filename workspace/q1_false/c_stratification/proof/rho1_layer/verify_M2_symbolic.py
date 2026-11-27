"""M2 的符号计算（sympy）：一个 3 参数族上的**整族覆盖**证明（不是抽样）。

设定：X = Q^5；B = <e5>；f = diag(a,b,c) 在 <e1,e2,e3> 上、e4,e5 -> 0；
族：U_s = <e5, e1, e2 + s e3>（3 维、含 B、mu=1）。

输出：
  * (N) 的条件（对 s 与 f 的参数）；
  * 在可允许子簇上，"坏条件"（存在 E^perp 内特征向量 <=> 铅笔 3x3 子式的 gcd 非常量）是否**恒成立**。
"""
import itertools
import sympy as sp


def main():
    a, b, c, s = sp.symbols('a b c s')
    lam = sp.Symbol('lam')

    # (N): f(e2 + s e3) = b e2 + s c e3 必须属于 <e1, e2 + s e3>
    # => 存在 al, be: b e2 + s c e3 = al e1 + be (e2 + s e3)
    # => al = 0, be = b, be*s = s*c => s*(b - c) = 0
    Ncond = sp.expand(sp.simplify(b * s - s * c))
    print("(N) 的条件：", Ncond, " = 0")

    # 在 (N) 成立时（b = c 或 s = 0），T 在 U 坐标下是 diag(a, b, 0)（e5 -> 0）
    T = sp.Matrix([[a, 0, 0], [0, b, 0], [0, 0, 0]])
    E = sp.Matrix([[0, 0, 1]])          # E = <e5> 是 U 的第 3 个基

    M = sp.zeros(4, 3)
    for i in range(3):
        for j in range(3):
            M[i, j] = (lam - T[i, j]) if i == j else -T[i, j]
    for j in range(3):
        M[3, j] = E[0, j]

    minors = []
    for rs in itertools.combinations(range(4), 3):
        for cs in itertools.combinations(range(3), 3):
            det = sp.expand(M[list(rs), list(cs)].det())
            if det != 0:
                minors.append(det)
    print("非零 3x3 子式：", minors)

    polys = [sp.Poly(d, lam) for d in minors]
    g = polys[0]
    for q in polys[1:]:
        g = sp.gcd(g, q)
    print("gcd =", g)
    print("=> 坏条件恒成立（gcd 非常量）？", g.degree() > 0)

    # 把 (N) 代入（b = c），再看
    polys2 = [sp.Poly(d.subs(b, c), lam) for d in minors]
    g2 = polys2[0]
    for q in polys2[1:]:
        g2 = sp.gcd(g2, q)
    print("在 b = c 上：gcd =", g2, "; 非常量？", g2.degree() > 0)

    print()
    print("结论：该 3 参数族在可允许子簇上**整族被覆盖**（符号证明，不是抽样）。")
    print("机制：T 是对角的 => e1, e2 都是特征向量，且都在 E^perp 里（E = <e5>）。")


if __name__ == '__main__':
    main()
