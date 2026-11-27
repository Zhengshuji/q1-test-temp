r"""$q=\omega+1=3$、$\omega=2$、$k=3$ 的显式检验：$\det[w,Aw]\ne0$ 能否在可达族上达成？

基无关形式（由 $q=\omega+1$ 判据等价改写）：
  $W=\operatorname{im}H$；$\ker B\cong\{x:\ H_Ax\in W\}/\ker H$；
  $$\text{好}\iff\text{对每个 }0\ne x\ \text{满足 }H_Ax\in W\ \text{且}\ Hx\ne0:\quad H_Ax\ \text{不平行于}\ Hx$$
  即 $\operatorname{rank}[H_Ax,\ Hx]=2$（$3\times2$ 矩阵）。

实例：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=3$、$\omega=2$、$m=2$。
  $K=\langle e_2,e_3,e_4\rangle$；$E=(0,0,1)$、$F_0=0$、$Z_1=(0,-1,0)$、$Z_2=(1,0,0)$（K-坐标）。
  可达：$b_1\in\mathbb C^{2\times3}$ 任意，$b_2$ 的第 1 列 $=-b_1Z_1$，第 2、3 列**自由**。
  $H=\binom{E}{b_1}$、$H_A=\binom{0}{b_2}$。
"""

import itertools
import random
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
        if r == rows:
            break
    return r


def nullspace(M):
    """解 M z = 0（M 为 list of rows），返回列基（列表，每个是长度 cols 的列表）。"""
    if not M:
        return []
    rows, cols = len(M), len(M[0])
    A = [list(map(F, row)) for row in M]
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        piv.append(c)
        r += 1
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for fc in free:
        z = [F(0)] * cols
        z[fc] = F(1)
        for i, pc in enumerate(piv):
            z[pc] = -A[i][fc]
        basis.append(z)
    return basis


def main():
    E = [F(0), F(0), F(1)]
    Z1 = [F(0), F(-1), F(0)]
    rng = random.Random(20261121)
    ngood = nbad = 0
    trials = 300
    for _ in range(trials):
        b1 = [[F(rng.randrange(-2, 3)) for _ in range(3)] for _ in range(2)]
        col1 = [-sum(b1[i][t] * Z1[t] for t in range(3)) for i in range(2)]
        b2 = [[col1[0], F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))],
              [col1[1], F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))]]
        H = [E] + b1
        HA = [[F(0), F(0), F(0)]] + b2
        if rank(H) != 2:
            continue
        # 解 H_A x = H x'  ⟺  [H_A | −H] (x; x') = 0
        M = [[HA[i][j] for j in range(3)] + [-H[i][j] for j in range(3)] for i in range(3)]
        sol = nullspace(M)
        # 取出 x 部分（前 3 个坐标）构成的子空间基
        Xs = []
        for z in sol:
            xv = z[:3]
            if rank(Xs + [xv]) > len(Xs):
                Xs.append(xv)
        good = True
        for xv in Xs:
            Hx = [sum(H[i][t] * xv[t] for t in range(3)) for i in range(3)]
            if rank([Hx]) == 0:
                continue                     # Hx = 0，对应 ker H，不算
            HAx = [sum(HA[i][t] * xv[t] for t in range(3)) for i in range(3)]
            # [H_A x , H x] 的秩：2 ⟹ 不平行 ⟹ 该 x 不给出坏
            pair = [[HAx[i], Hx[i]] for i in range(3)]
            if rank(pair) < 2:
                good = False
                break
        if good:
            ngood += 1
        else:
            nbad += 1
    print(f'{trials} 个随机可达对（rank H = 2）：**好 {ngood} / 坏 {nbad}**')
    if ngood:
        print('⟹ 该层（q=3, ω=2, k=3）**存在好点** ⟹ 可行（至少该层可行）')
    else:
        print('⟹ 抽样范围内全坏（提示整层坏，但需证明）')


if __name__ == '__main__':
    main()
