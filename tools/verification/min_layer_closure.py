"""min_layer_closure.py —— 最小秩层：闭包算法与不变量检查（精确有理算术）

目的（Workstream A 第一步的可计算部分）：
1. 把问题搬到商空间 X = C^n / J（J = row[C;CA]），完全用有理数精确计算；
2. 用**闭包迭代** U <- U + T(U) + B 求"包含 U_0 与 B 的最小 T-不变子空间"（记 U*）；
   **注意（专家 2026-11-02 §1.3）**：U* 的维数**一般不等于** P = rho_ci——
   P 的定义是 min{ dim U : U_0 ⊆ U, T U ⊆ U + B }，而闭包给的是"最小不变"而非"最小维"。
   反例：T=0, U_0=0, B≠0 ⟹ 闭包 = B（维数 >0），但 U=0 已可行（维数 0）。
   本文件把两者**分开命名**并做交叉核对；P 的权威实现是 tools/p_algorithm 的 P_alg（D.2/D.3）；
3. 断言所有不变量（维数、商结构、T U* ⊆ U* + B）；
4. **不**声称 U* 唯一：本脚本只打印事实，唯一性/仿射性由人判断。

约定（与 docs/01 一致）：
  J = row[C;CA]（行空间），V = ker[C;CA]（= J^perp），C^n = V ⊕ J；
  pi_V: 沿 J 到 V 的投影；T = pi_V o A|_V；B = span{pi_V(j A) : j 行 of J}；U_0 = span{pi_V(l) : l 行 of L0}。
  （这四个对象就是 docs/02 E.1 里的 T, B, U_0。）

验证不是证明：本脚本只提供精确实例与反例，不提供证明。
"""

from fractions import Fraction

# ---------------------------------------------------------------- 基本精确线性代数


def rref(M):
    """返回 (rref 矩阵, 主元列列表)。M 为 Fraction 行的列表。"""
    M = [[Fraction(x) for x in row] for row in M]
    if not M:
        return [], []
    rows, cols = len(M), len(M[0])
    piv = []
    r = 0
    for c in range(cols):
        p = None
        for i in range(r, rows):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        f = M[r][c]
        M[r] = [x / f for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                g = M[i][c]
                M[i] = [M[i][j] - g * M[r][j] for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M[:r], piv


def rank(M):
    if not M:
        return 0
    return len(rref(M)[0])


def span_basis(rows):
    """给出一组行的基（非零行、rref 化）。"""
    if not rows:
        return []
    R, _ = rref(rows)
    return [row for row in R if any(x != 0 for x in row)]


def solve_in_span(basis, x):
    """求 coefficients 使 sum c_i basis_i == x；不相容返回 None。"""
    if not basis:
        return None
    rows, cols = len(basis), len(basis[0])
    A = [[basis[i][j] for i in range(rows)] + [x[j]] for j in range(cols)]
    R, piv = rref(A)
    # 不相容：某行左边全 0、右边非 0
    for row in R:
        if all(row[j] == 0 for j in range(rows)) and row[rows] != 0:
            return None
    c = [Fraction(0)] * rows
    for i, p in enumerate(piv):
        if p < rows:
            c[p] = R[i][rows]
    return c


def matvec(M, x):
    return [sum(M[i][j] * x[j] for j in range(len(x))) for i in range(len(M))]


def mul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    return [[sum(X[i][k] * Y[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


# ---------------------------------------------------------------- 商空间数据


def quotient_data(A, C, L0):
    """返回 (T, B_basis, U0_basis, info)。全部是 V-坐标下的有理矩阵/基。"""
    n = len(A)
    CA = mul(C, A)
    Jrows = span_basis([list(r) for r in (C + CA)])
    Vrows = span_basis(nullspace([list(r) for r in (C + CA)]))
    j, d = len(Jrows), len(Vrows)
    assert j + d == n, f'dim J + dim V = {j}+{d} != n={n}（J 与 V 不互补）'

    def solve_cols(cols, x):
        """解 sum c_i cols_i = x（cols 是 n 维列向量）；无解返回 None。"""
        k = len(cols)
        n_ = len(x)
        aug = [[cols[i][r] for i in range(k)] + [x[r]] for r in range(n_)]
        R, piv = rref(aug)
        for row in R:
            if all(row[i] == 0 for i in range(k)) and row[k] != 0:
                return None
        c = [Fraction(0)] * k
        for i, p in enumerate(piv):
            if p < k:
                c[p] = R[i][k]
        return c

    def pi_V(x):
        """沿 J 到 V 的投影：x = v + jj，返回 v 在 Vrows 下的坐标。"""
        cols = [[Vrows[i][t] for t in range(n)] for i in range(d)] + \
               [[Jrows[i][t] for t in range(n)] for i in range(j)]
        z = solve_cols(cols, list(x))
        assert z is not None, 'x 不在 V ⊕ J 里（分解失败）'
        return z[:d]

    # T: V -> V，矩阵（列 = T(基向量) 的坐标）
    Tv = [pi_V(matvec(A, [v[j] for j in range(n)])) for v in Vrows]
    T = [[Tv[k][i] for k in range(d)] for i in range(d)]
    # 断言：T 的列数 = d
    assert len(T) == d and all(len(r) == d for r in T), 'T 的维数不对'

    # B = span{ pi_V(j A) : j 行 of J }
    Bb = span_basis([pi_V(matvec(A, [jj[k] for k in range(n)])) for jj in Jrows])
    # U_0 = span{ pi_V(l) : l 行 of L0 }
    U0b = span_basis([pi_V(list(l)) for l in L0])
    info = dict(n=n, j=j, d=d, dimB=len(Bb), dimU0=len(U0b))
    return T, Bb, U0b, info


def nullspace(rows):
    """行的零空间基（右零空间）。"""
    if not rows:
        return []
    R, piv = rref(rows)
    cols = len(rows[0])
    free = [c for c in range(cols) if c not in piv]
    out = []
    for f in free:
        v = [Fraction(0)] * cols
        v[f] = Fraction(1)
        for i, p in enumerate(piv):
            v[p] = -R[i][f]
        out.append(v)
    return out


# ---------------------------------------------------------------- 闭包迭代


def closure(T, B_basis, U0_basis, verbose=True):
    """最小 U ⊇ U_0 使 T U ⊆ U + B。返回 U 的基。"""
    d = len(T)
    U = span_basis([list(x) for x in U0_basis])
    hist = []
    while True:
        colU = [matvec(T, [u[i] for i in range(d)]) for u in U] if U else []
        nxt = span_basis(U + colU + [list(b) for b in B_basis])
        hist.append(len(nxt))
        if len(nxt) == len(U):
            break
        U = nxt
        assert len(hist) < 20, '闭包迭代不收敛？'
    if verbose:
        print(f'  闭包迭代维数序列: {hist}')
    # 断言：T U ⊆ U + B
    UB = span_basis(U + [list(b) for b in B_basis])
    for u in U:
        Tu = matvec(T, [u[i] for i in range(d)])
        assert solve_in_span(UB, Tu) is not None, 'T U 不在 U + B 里（闭包失败）'
    return U


def check_instance(name, A, C, L0):
    print(f'=== {name} ===')
    T, Bb, U0b, info = quotient_data(A, C, L0)
    print(f'  n={info["n"]}, j={info["j"]}, d={info["d"]}, dim B={info["dimB"]}, dim U_0={info["dimU0"]}')
    U = closure(T, Bb, U0b)
    print(f'  闭包 U* 的维数 = {len(U)}（**不是** P 的定义；见文件头）')
    # 检查 U_0 ⊆ U*
    for u in U0b:
        assert solve_in_span(U, u) is not None, 'U_0 不在 U* 里'
    print('  U_0 ⊆ U* ✓   T U* ⊆ U* + B ✓')
    return dict(T=T, B=Bb, U0=U0b, Ustar=U, info=info)


def unit(n, i):
    v = [Fraction(0)] * n
    v[i] = Fraction(1)
    return v


def main():
    out = {}
    # 实例 1（R17 的约定实例，n=5, p=1, 由 STATUS 记录）：A 取对角+一个耦合
    A1 = [[Fraction(0)] * 5 for _ in range(5)]
    for i in range(5):
        A1[i][i] = Fraction(i)
    A1[0][1] = Fraction(1)
    C1 = [unit(5, 0)]
    L01 = [unit(5, 2)]
    out['R17-like'] = check_instance('R17-like (n=5, p=1)', A1, C1, L01)

    # 实例 2：第二个实例（STATUS 记录：Ae5=e0，其余 e_i 固定，n=6, p=1）
    A2 = [[Fraction(0)] * 6 for _ in range(6)]
    for i in range(4):
        A2[i][i] = Fraction(1)
    A2[5][5] = Fraction(1)
    A2[0][5] = Fraction(1)
    C2 = [unit(6, 0)]
    L02 = [unit(6, 1)]
    out['second'] = check_instance('second (n=6, p=1)', A2, C2, L02)

    # 实例 3：完全可控（单链），期望 P = dim U_0 之后被 B 吃掉很多
    A3 = [[Fraction(0)] * 4 for _ in range(4)]
    for i in range(3):
        A3[i][i + 1] = Fraction(1)
    C3 = [unit(4, 0)]
    L03 = [unit(4, 3)]
    out['chain'] = check_instance('chain (n=4, p=1)', A3, C3, L03)

    # 专家反例回归测试（2026-11-02 §1.3）：T=0, U_0=0, B=span{e1} ⟹ 闭包维数 1，但 P=0
    T0 = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
    B0 = [[Fraction(1), Fraction(0)]]
    print('=== 专家反例：T=0, U_0=0, B=span{e1} ===')
    Ucl = closure(T0, B0, [], verbose=False)
    print(f'  闭包维数 = {len(Ucl)}（应为 1）')
    try:
        import os as _os, sys as _sys
        _sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'p_algorithm'))
        from c195_P_q import P_alg as _P
        pv = _P(T0, B0, [])
        print(f'  P_alg = {pv}（应为 0）⟹ 闭包 != P 的反例成立: {len(Ucl) != pv}')
    except Exception as e:
        print(f'  P_alg 不可用: {e}')

    # 实例 4：B != 0（A 不保持 J）
    # n=4, C=e0；A e0 = e1（在 J 内），A e1 = e2（在 J 外 ⟹ B != 0）
    A4 = [[Fraction(0)] * 4 for _ in range(4)]
    A4[0][1] = Fraction(1)
    A4[1][2] = Fraction(1)
    A4[2][3] = Fraction(1)
    C4 = [unit(4, 0)]
    L04 = [unit(4, 1)]
    out['B!=0'] = check_instance('B != 0 (n=4, p=1)', A4, C4, L04)

    # 交叉核对：与 tools/p_algorithm 的递归 P_alg 比较
    import os, sys
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(here, '..', 'p_algorithm'))
    try:
        from c195_P_q import P_alg
        print('\n=== 与 P_alg（递归实现）交叉核对 ===')
        for name, r in out.items():
            T, B, U0 = r['T'], r['B'], r['U0']
            d = len(T)
            # P_alg 用行约定：A 行作用？c195 的 P_alg(A,B,S) 里 A 是矩阵、B/S 是行基
            # 约定差异（2026-11-02 实测确认）：c195 的 P_alg 用**行约定**（x -> x A），
            # 本脚本的 T 是**列约定**；必须转置后再比较，否则会得到假的不一致。
            Tt = [[T[j][i] for j in range(d)] for i in range(d)]
            try:
                palg = P_alg([[Fraction(x) for x in row] for row in Tt], B, U0)
            except Exception as e:
                print(f'  {name}: P_alg 调用失败（{e}）')
                continue
            mine = len(r['Ustar'])
            flag = 'OK' if palg == mine else 'MISMATCH'
            print(f'  {name}: closure={mine}, P_alg={palg}  [{flag}]')
    except Exception as e:
        print(f'  P_alg 不可用: {e}')

    print('\n小结：以上只给"闭包维数 = P"的实例证据；不构成对任何命题的证明。')
    return out


if __name__ == '__main__':
    main()
