"""放大扫描：尝试**证伪**猜想 C31（rho>=3, c=1 时 (5b) 无害）。

与 scan_31_layer.py 的区别：
  * V 用"**模 J 的 A-闭包**"（只要求 VA ⊆ V+J，即 (5a) 本身），而不是 A-不变闭包（更强的子类）；
  * tau 的方向数从 12 提到 20；
  * n 扩到 7；
  * 记录每个实例的候选数与成功数；若某实例"候选非空且全部失败" => **C31 被证伪**。

判据：cond_5a_orig / cond_5b_orig（堆叠形式，精确有理算术）。
"""
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


def closure_mod(rows, A, J):
    """模 J 的 A-闭包：反复加入违反 (5a) 的 x A，直到 VA ⊆ V + J。"""
    V = AI.row_basis(rows)
    for _ in range(50):
        bad = None
        for x in V:
            xa = mm([x], A)[0]
            if not inspan([r[:] for r in V] + [r[:] for r in J], xa):
                bad = xa
                break
        if bad is None:
            return V
        V = AI.row_basis([r[:] for r in V] + [bad])
    return V


def rc(L, A, C, J):
    rho = AI.rank(AI.vstack([L, mm(C, A), C])) - len(J)
    c = len(L) + len(J) - AI.rank(AI.vstack([L, J]))
    return rho, c


def main():
    rng = random.Random(777001)
    n31 = 0
    feas = 0
    infeas = 0
    refuted = []
    for trial in range(600):
        n = rng.choice([6, 7])
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        J = AI.row_basis(C + mm(C, A))
        if len(J) == 0 or len(J) >= n - 2:
            continue
        r = [Fr(rng.randint(-1, 1)) for _ in range(n)]
        V = closure_mod([L0[0], r], A, J)
        L = AI.row_basis(V)
        # 注意：(rho,c)=(3,1) 蕴含 dim V = rho + c = 4（不是 3）
        if len(L) != 4:
            continue
        if rc(L, A, C, J) != (3, 1):
            continue
        n31 += 1
        # tau：给第 3 行加 J 元素
        cands = [L]
        for _t in range(20):
            d = [sum(Fr(rng.randint(-2, 2)) * b[k] for b in J) for k in range(n)]
            L2 = AI.row_basis([L[0], L[1], L[2], [L[3][k] + d[k] for k in range(n)]])
            if len(L2) == 4 and rc(L2, A, C, J) == (3, 1) and AI.cond_5a_orig(A, C, L2):
                cands.append(L2)
        ok = False
        for Lx in cands:
            if AI.cond_5b_orig(A, C, Lx):
                ok = True
                break
        if ok:
            feas += 1
        else:
            infeas += 1
            if len(refuted) < 3:
                refuted.append(dict(n=n, A=[[str(x) for x in row] for row in A],
                                    C=[[str(x) for x in row] for row in C],
                                    L0=[[str(x) for x in row] for row in L0],
                                    L=[[str(x) for x in row] for row in L]))
    print(f"(3,1)&(5a) 实例: {n31}；其中可行 {feas}，**全部失败 {infeas}**")
    if refuted:
        import io, json
        txt = json.dumps(refuted, ensure_ascii=False, indent=1)
        io.open('proof/rho1_layer/candidate_c31_counterexample.json', 'w', encoding='utf-8', newline='\n').write(txt)
        print("  已写出候选反例 proof/rho1_layer/candidate_c31_counterexample.json")
    else:
        print("  没有找到 C31 的反例 ✓（在本次扫描范围内）")


if __name__ == '__main__':
    main()
