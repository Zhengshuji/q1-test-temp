r"""$\omega=2$ 的秩-only 检验：两个"秩相同但答案不同"的例子。

若下面的计算确认，则**秩-only 猜想在 $\omega\ge2$ 不成立**（$\omega=1$ 时专家已证它成立）。

两个例子（$q=3$、$\omega=2$、$k=2$，故 $P=\lambda U-G$ 直接是 $3\times2$ 铅笔）：
  E1（专家型，可行）：$U=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}$、$G=\begin{pmatrix}0&1\\0&0\\1&0\end{pmatrix}$
  E2（不可行）      ：$U$ 同、$G=\begin{pmatrix}0&0\\0&0\\1&0\end{pmatrix}$

比较的"秩不变量"：$\operatorname{rank}U$、$\operatorname{rank}G$、$\operatorname{rank}[U\ G]$、
$\operatorname{rank}$ of $[U;G]$、$\dim(\operatorname{im}U\cap\operatorname{im}G)$。
判据：$\omega$ 阶子式的 gcd 是否为非零常数（等价：$\operatorname{rank}(\lambda U-G)=2$ 对一切 $\lambda$）。
"""

import itertools
import sympy as sp

lam = sp.Symbol('lam')


def minors_and_gcd(U, G):
    P = lam * U - G
    q, k = P.shape
    ms = []
    for rows in itertools.combinations(range(q), k):
        m = sp.expand(P[list(rows), :].det())
        ms.append(m)
    g = None
    for m in ms:
        if sp.simplify(m) != 0:
            g = m if g is None else sp.gcd(g, m)
    return ms, g, (g is not None and sp.degree(g, lam) == 0)


def ranks(U, G):
    q = U.rows
    stacked_cols = U.row_join(G)          # [U | G]
    stacked_rows = U.col_join(G)          # [U ; G]
    # im U ∩ im G 的维数
    inter = []
    for i in range(U.cols):
        v = U[:, i]
        # 判断是否在 im G 中
        aug = G.row_join(v)
        if aug.rank() == G.rank():
            inter.append(v)
    return dict(rankU=U.rank(), rankG=G.rank(), rank_UG=stacked_cols.rank(),
                rank_U_stacked=stacked_rows.rank())


def main():
    U = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    G1 = sp.Matrix([[0, 1], [0, 0], [1, 0]])
    G2 = sp.Matrix([[0, 0], [0, 0], [1, 0]])
    for tag, G in (('E1', G1), ('E2', G2)):
        ms, g, ok = minors_and_gcd(U, G)
        r = ranks(U, G)
        print(f'{tag}: 2 阶子式 = {[sp.factor(m) for m in ms]}')
        print(f'    gcd = {sp.factor(g) if g is not None else None} ⟹ '
              f'{"可行（gcd 为常数）" if ok else "不可行（gcd 非常数）"}')
        print(f'    秩不变量: {r}')


def search():
    """在固定秩不变量下搜"答案不同"的例子。"""
    import itertools as it
    U = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    target = (2, 2, 3, 2)
    buckets = {}
    for entries in it.product(range(-1, 2), repeat=6):
        G = sp.Matrix([[entries[0], entries[1]], [entries[2], entries[3]], [entries[4], entries[5]]])
        r = ranks(U, G)
        key = (r['rankU'], r['rankG'], r['rank_UG'], r['rank_U_stacked'])
        if key != target:
            continue
        ms, g, ok = minors_and_gcd(U, G)
        buckets.setdefault(ok, []).append((entries, sp.factor(g) if g is not None else None))
    for ok in (True, False):
        lst = buckets.get(ok, [])
        print(f'不变量的答案 {ok}: {len(lst)} 个')
        for e, g in lst[:3]:
            print('   G =', e, ' gcd =', g)
    if buckets.get(True) and buckets.get(False):
        print('⟹ 同一组秩不变量下**答案不同** ⟹ 秩-only 猜想在 omega=2 **不成立**')
    else:
        print('⟹ 未找到同不变量下的反例（本搜索范围内）')


if __name__ == '__main__':
    main()
    print()
    search()
