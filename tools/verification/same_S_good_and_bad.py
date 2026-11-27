r"""专家优先级 3：在 $k>\omega$ 找"**同一个 $S$ 上既有好点又有坏点**"的例子。

实例：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=3$；$\omega=2$；$m=q-r=2$。
  $C=e_1^{\mathsf T}$；$A$ 第一行 $e_5^{\mathsf T}$（$CA=e_5$、$\operatorname{rank}[C;CA]=2$、$K=\langle e_2,e_3,e_4\rangle$）；
  $A$ 的列 2,3,4 $=e_3,\ e_5,\ e_1$ ⟹ $Ae_2=e_3\in K$、$Ae_3=e_5\notin K$、$Ae_4=e_1\notin K$
  ⟹ $\ker T=\{(-e_3,e_2)\}$（$d=1$），$Z_1=(0,-1,0)$、$Z_2=(1,0,0)$（K-坐标）。
  $L_0=e_4^{\mathsf T}$ ⟹ $E=(0,0,1)$、$F_0=0$。

对每个 2 维 $S$（用余向量 $\sigma$ 表示，$S=\{x:x\sigma=0\}$）与每个 $x\in X_S$：
  $y$ 的解集是"特解 + $\ker(y\mapsto yZ_2)$ 的交"，枚举其小整数元素，逐个分类（好/坏）。
"""

import itertools
from fractions import Fraction as Fr

F = Fr


def rank(M):
    if not M:
        return 0
    A = [list(map(F, row)) for row in M]
    r, rows, cols = 0, len(A), len(A[0])
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        r += 1
    return r


def pdeg(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return -1 if (len(p) == 1 and p[0] == 0) else len(p) - 1


def pdivmod(p, q):
    p, q = list(p), list(q)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    r = list(p)
    quot = [F(0)] * max(1, len(p) - len(q) + 1)
    while pdeg(r) >= pdeg(q):
        d = pdeg(r) - pdeg(q)
        f = r[pdeg(r)] / q[pdeg(q)]
        quot[d] = f
        for i in range(len(q)):
            r[i + d] -= f * q[i]
        while len(r) > 1 and r[-1] == 0:
            r.pop()
    return quot, r


def pgcd(p, q):
    p, q = list(p), list(q)
    while pdeg(q) >= 0:
        _, r = pdivmod(p, q)
        p, q = q, r
    return p


def dot(x, Z):
    return sum(x[t] * Z[t] for t in range(len(x)))


def minors_gcd(H, HA):
    """P = λH − H_A 的全部 2 阶子式的 gcd（列表，低次在前）。"""
    out = []
    for rr in itertools.combinations(range(3), 2):
        for cc in itertools.combinations(range(3), 2):
            h = [[H[i][j] for j in cc] for i in rr]
            hA = [[HA[i][j] for j in cc] for i in rr]
            detH = h[0][0] * h[1][1] - h[0][1] * h[1][0]
            detHA = hA[0][0] * hA[1][1] - hA[0][1] * hA[1][0]
            mix = (h[0][0] * hA[1][1] + hA[0][0] * h[1][1]
                   - h[0][1] * hA[1][0] - hA[0][1] * h[1][0])
            out.append([detHA, -mix, detH])
    g = None
    for p in out:
        if pdeg(list(p)) >= 0:
            g = list(p) if g is None else pgcd(g, list(p))
    return g


def main():
    E = [F(0), F(0), F(1)]
    F0 = [F(0), F(0), F(0)]
    Z1 = [F(0), F(-1), F(0)]
    Z2 = [F(1), F(0), F(0)]

    results = {}
    for sc in itertools.product([-2, -1, 0, 1, 2], repeat=3):
        if all(v == 0 for v in sc):
            continue
        k0 = next(i for i, v in enumerate(sc) if v != 0)
        sc = [F(v, sc[k0]) for v in sc]
        key = tuple(str(v) for v in sc)
        # S = {x : x·sc = 0}（行向量），取基
        nz = [i for i in range(3) if sc[i] != 0]
        if len(nz) < 2:
            continue
        i0, i1 = nz[0], nz[1]
        b1 = [F(0)] * 3; b1[i0] = sc[i1]; b1[i1] = -sc[i0]
        b2 = [F(0)] * 3; b2[nz[2] if len(nz) > 2 else 2] = F(1)
        # 补第三个基（仅当 len(nz)==2 时 nz[2] 不存在）
        if len(nz) == 2:
            b2 = [F(0)] * 3
            b2[3 - nz[0] - nz[1]] = F(1)
        Srows = [b1, b2]
        if rank(Srows) != 2:
            continue
        # E ⊆ S ?
        if dot(E, sc) != 0:
            continue
        # X_S：x ∈ S 且 ∃y∈S: xZ1 + yZ2 = 0 ⟺ −x_2 + y_1 = 0 ⟺ y_1 = x_2
        # S 里是否有 y 使 y_1 = x_2？
        ys = [y for y in Srows + [[r[0] + r[1] for r in zip(Srows[0], Srows[1])]]
              if y[0] == F(0)]      # 简化：只看 y_1=0 的情形
        X = [x for x in Srows if x[1] == F(0)]
        if not X:
            continue
        verdicts = set()
        for x in X:
            if rank([E, x]) < 2:
                continue
            # 解 y ∈ S, y_1 = x_2
            for y in ys + [[y[0] + F(2) * y[2] for y in Srows[0]]]:
                if y[0] != x[1]:
                    continue
                # 检验 x Z1 + y Z2 = 0
                if dot(x, Z1) + dot(y, Z2) != 0:
                    continue
                H = [E, x, [F(0)] * 3]
                HA = [F0, y, [F(0)] * 3]
                if rank(H) != 2:
                    continue
                g = minors_gcd([[F(v) for v in r] for r in H],
                               [[F(v) for v in r] for r in HA])
                good = (g is not None and pdeg(g) == 0)
                verdicts.add('好' if good else '坏')
        if verdicts:
            results[key] = verdicts
    both = {k: v for k, v in results.items() if len(v) == 2}
    print(f'候选 S（含 E）共 {len(results)} 个；其中**既有好点又有坏点**的 {len(both)} 个')
    for k, v in list(both.items())[:6]:
        print('  sigma =', k, ' 判决集合 =', v)
    if not both:
        cnt = {}
        for v in results.values():
            cnt[tuple(sorted(v))] = cnt.get(tuple(sorted(v)), 0) + 1
        print('  各 S 的判决分布：', cnt)


if __name__ == '__main__':
    main()
