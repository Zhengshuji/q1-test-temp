"""针对候选反例实例：**直接参数化** (3,1) 型层，密集搜索（验证 ≠ 证明）。

要点：与其随机撒 4 维子空间（满足 (5a) 的概率极低），不如**直接构造** T-不变子空间：
  取 u1,u2,u3 ∈ C^n，U = span{ui}；检查每个 ui*A ∈ U + J（即 pi(ui A) ∈ pi(U)，也就是 (5a) 在 U 上成立）。
  若成立，则 U 是 T-不变的；再取 h ∈ J（beta(h)=pi(hA) ∈ U），V = span{ui + j_i} + <h>（j_i ∈ J 是 lift 自由度 = tau）。
  然后测 (5b)。

这样每个样本都自动满足 (5a) ⟹ 采样效率高得多，可以扫很多点。
"""
import io
import json
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def inspan(basis, v):
    if not basis:
        return all(x == 0 for x in v)
    return AI.rank([r[:] for r in basis] + [v[:]]) == AI.rank([r[:] for r in basis])


def rc(L, A, C, J):
    rho = AI.rank(AI.vstack([L, mm(C, A), C])) - len(J)
    c = len(L) + len(J) - AI.rank(AI.vstack([L, J]))
    return rho, c


def main():
    d = json.load(io.open('proof/rho1_layer/candidate_c31_counterexample.json', encoding='utf-8'))[0]
    F = lambda M: [[Fr(x) for x in r] for r in M]
    A, C, L0 = F(d['A']), F(d['C']), F(d['L0'])
    n = len(A)
    CA = mm(C, A)
    J = AI.row_basis(C + CA)
    j = len(J)
    CAJ = AI.row_basis(C + CA + J)
    L0b = AI.row_basis(L0)
    rng = random.Random(20261101)

    nU = 0        # 找到的 T-不变 3 维 U（含 U0 的像）
    nV = 0        # 通过的 V（类型 (3,1) 且 (5a)）
    nFeas = 0
    for trial in range(60000):
        # 用 Krylov 闭包**构造** T-不变子空间（而不是随机猜）
        x0 = [Fr(rng.randint(-2, 2)) for _ in range(n)]
        U = AI.row_basis([x0])
        grew = True
        while grew and len(U) <= 3:
            grew = False
            for u in [r[:] for r in U]:
                xa = mm([u], A)[0]
                if not inspan([r[:] for r in U] + [r[:] for r in J], xa):
                    U = AI.row_basis([r[:] for r in U] + [xa])
                    grew = True
                    break
        if len(U) != 3:
            continue
        # T-不变性：(5a) 在 U 上（uA ∈ U + J）
        ok = True
        for u in U:
            xa = mm([u], A)[0]
            if not inspan([r[:] for r in U] + [r[:] for r in J], xa):
                ok = False
                break
        if not ok:
            continue
        # 需要 row L0 ⊆ U + J（否则 V 不含 L0）
        if not all(inspan([r[:] for r in U] + [r[:] for r in J], r) for r in L0b):
            continue
        nU += 1
        # 取 h ∈ J：既要有 beta(h) ∈ U（即 hA ∈ U + J），又要让 V 含 row L0（即 L0 的行 ∈ U + <h> + J）
        Jbasis = AI.row_basis(J)
        hs = [r[:] for r in Jbasis]
        for _ in range(8):
            hs.append([sum(Fr(rng.randint(-2, 2)) * b[k] for b in Jbasis) for k in range(n)])
        good_h = []
        for h in hs:
            if not any(h):
                continue
            if not inspan([r[:] for r in U] + [r[:] for r in J], mm([h], A)[0]):
                continue                     # beta(h) 不在 U 里（退化的 h 也允许，但先跳过）
            good_h.append(h)
        if not good_h:
            continue
        # lift 自由度 j_i ∈ J（= tau），并保证 row L0 仍在 V 里
        # 正确的 V 构造：V 必须**包含 row L0**，且 pi(V) = U。
        # 取 V = span{ L0row, lift(u2)+j2, lift(u3)+j3, h }，其中 {pi(L0row), pi(u2), pi(u3)} 张成 U。
        L0row = L0b[0]
        for h in good_h:
          for _t in range(6):
            # 选 u2,u3 ∈ U 使 {L0row, u2, u3} 与 J 一起的秩 = j+3
            pick = None
            for _a in range(20):
                cand = []
                for u in U:
                    cand.append(u)
                rng.shuffle(cand)
                for i in range(len(cand)):
                    for k2 in range(i + 1, len(cand)):
                        test = [L0row, cand[i], cand[k2]] + [r[:] for r in J]
                        if AI.rank(test) == len(J) + 3:
                            pick = (cand[i], cand[k2])
                            break
                    if pick:
                        break
                if pick:
                    break
            if not pick:
                continue
            u2, u3 = pick
            j2 = [sum(Fr(rng.randint(-2, 2)) * b[k] for b in J) for k in range(n)]
            j3 = [sum(Fr(rng.randint(-2, 2)) * b[k] for b in J) for k in range(n)]
            rows = [L0row,
                    [u2[k] + j2[k] for k in range(n)],
                    [u3[k] + j3[k] for k in range(n)],
                    list(h)]
            L = AI.row_basis(rows)
            if len(L) != 4:
                continue
            if rc(L, A, C, J) != (3, 1):
                continue
            if not AI.cond_5a_orig(A, C, L):
                continue
            nV += 1
            if AI.cond_5b_orig(A, C, L):
                nFeas += 1
                if nFeas == 1:
                    print("*** 找到可行解！（该实例的 (3,1) 层可行）")
                    print("   L =", [[str(x) for x in r] for r in L])
        if nFeas:
            break

    print(f"T-不变 3 维 U（含 U0 的像）: {nU} 个样本")
    print(f"通过的 V: {nV} 个；其中 (5b) 成立: {nFeas} 个")
    if nFeas == 0:
        print("=> 仍未找到可行解（候选反例继续加强；仍非证明）")


if __name__ == '__main__':
    main()
