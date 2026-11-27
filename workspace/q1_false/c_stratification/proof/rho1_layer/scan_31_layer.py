"""层级别扫描：(3,1) 层在**真实实例**上是否可行？（验证 ≠ 证明）

做法：
  1. 取真实实例 (A, C, L0)（n=5,6）。
  2. 用 A-不变闭包造 V ⊇ row(L0)：V ← V + {x A : x ∈ 基(V)} 直到稳定（这保证 (5a)）。
  3. 计算 rho = rank[L;CA;C] - dim J、c = dim(V ∩ J)；只保留 (rho,c) = (3,1)。
  4. tau 自由度 = 给非 L0 的行加 J 的元素（保持 (rho,c) 不变）。
  5. 用堆叠判据 cond_5a_orig / cond_5b_orig 精确判定。
输出：找到多少个 (3,1) 的 V；其中可行/不可行各多少。
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def rc(L, A, C, J):
    rho = AI.rank(AI.vstack([L, mm(C, A), C])) - len(J)
    c = len(L) + len(J) - AI.rank(AI.vstack([L, J]))
    return rho, c


def closure(rows, A):
    V = AI.row_basis(rows)
    while True:
        new = [r[:] for r in V]
        for x in V:
            new.append(mm([x], A)[0])
        V2 = AI.row_basis(new)
        if len(V2) == len(V):
            return V
        V = V2


def main():
    rng = random.Random(4242)
    n31 = 0
    feas = 0
    infeas = 0
    for trial in range(400):
        n = rng.choice([5, 6])
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        J = AI.row_basis(C + mm(C, A))
        if len(J) == 0 or len(J) >= n:
            continue
        r = [Fr(rng.randint(-1, 1)) for _ in range(n)]
        V = closure([L0[0], r], A)
        L = AI.row_basis(V)
        if len(L) < 3:
            continue
        if rc(L, A, C, J) != (3, 1):
            continue
        if not AI.cond_5a_orig(A, C, L):
            continue
        n31 += 1
        # tau 自由度：给最后一行加 J 元素
        ok = False
        cands = [L]
        for _t in range(12):
            d = [sum(Fr(rng.randint(-2, 2)) * b[k] for b in J) for k in range(n)]
            L2 = AI.row_basis([L[0], L[1], [L[2][k] + d[k] for k in range(n)]])
            if len(L2) == 3 and rc(L2, A, C, J) == (3, 1) and AI.cond_5a_orig(A, C, L2):
                cands.append(L2)
        for Lx in cands:
            if AI.cond_5b_orig(A, C, Lx):
                ok = True
                break
        if ok:
            feas += 1
        else:
            infeas += 1
    print(f"找到 (rho,c)=(3,1) 且 (5a) 成立的实例: {n31}")
    print(f"  其中可行: {feas}；不可行: {infeas}")
    print("说明：V 用 A-不变闭包构造（比 (5a) 更强的子类）；样本很小，仅作方向性观察。")


if __name__ == '__main__':
    main()
