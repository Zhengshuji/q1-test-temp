"""定理 29.1 的可检验后果（验证 ≠ 证明）。

定理 29.1：在**固定 (U,H)** 且 dim beta(H) = rho-1 时，Bad 是**仿射**的且 Bad ⊆ A，
于是"可行 ⟺ dim Bad < dim A" ⟺ "Bad ≠ A" ⟺ A ⊄ Bad。

可检验后果：在 A 上随机采样 τ（A 是仿射的、好集在 A 上是开的），
**要么几乎全可行、要么全不可行**；若出现"一半一半"（mix），则 Bad 不是仿射 ⟹ 定理 29.1 有误。

做法：用 block 实例（A 保持 W ⟹ 行在 W 内即满足 (5a)），
τ 的自由度实现为"给行加 J 的元素"（并保持 (rho,c) 与 (5a)）。
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def layer(L, A, C, J):
    rho = AI.rank(AI.vstack([L, mm(C, A), C])) - len(J)
    c = len(L) + len(J) - AI.rank(AI.vstack([L, J]))
    return rho, c


def beta_dim(L, A, C, J):
    """dim beta(H) = dim pi((V∩J) A)"""
    H = [r for r in AI.row_basis(J) if AI.rank([x[:] for x in L] + [r[:]]) == len(L)]
    H = AI.row_basis(H)
    if not H:
        return 0
    HA = mm(H, A)
    return len(AI.row_basis([r[:] for r in HA] + [r[:] for r in J])) - len(J)


def main():
    rng = random.Random(2027)
    tested = mix = 0
    for _trial in range(600):
        n = 5
        mblk = rng.choice([2, 3])
        A, C, L0 = AI.block_instance(rng, n, mblk)
        J = AI.row_basis(C + mm(C, A))
        if len(J) == 0:
            continue
        k = rng.choice([2, 3])
        rows = [[Fr(rng.randint(-1, 1)) if t < mblk else Fr(0) for t in range(n)] for _ in range(k)]
        L = AI.row_basis(rows)
        if len(L) < 2 or not AI.cond_5a_orig(A, C, L):
            continue
        rho, c = layer(L, A, C, J)
        if rho < 2 or c < 1 or c < rho - 1:
            continue
        if beta_dim(L, A, C, J) != rho - 1:
            continue                       # 只测定理 29.1 覆盖的情形
        succ = 0
        trials = 20
        for _t in range(trials):
            ds = []
            for i in range(len(L)):
                d = [sum(Fr(rng.randint(-1, 1)) * b[t] for b in J) for t in range(n)]
                ds.append([L[i][t] + d[t] for t in range(n)])
            L2 = AI.row_basis(ds)
            if len(L2) != len(L) or layer(L2, A, C, J) != (rho, c):
                continue
            if not AI.cond_5a_orig(A, C, L2):
                continue
            if AI.cond_5b_orig(A, C, L2):
                succ += 1
        tested += 1
        if 0 < succ < trials:
            mix += 1
            if mix <= 3:
                print(f"mix: n={n} rho={rho} c={c} beta_dim={rho-1} 成功 {succ}/{trials}")
    print(f"符合定理 29.1 假设的实例 {tested} 个；出现 'mix' 的 {mix} 个")
    print("mix = 0 => 与'Bad 仿射'一致（**验证，不是证明**）；mix > 0 => 定理 29.1 有误")


if __name__ == '__main__':
    main()