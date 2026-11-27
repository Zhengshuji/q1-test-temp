"""探测：在 (5a) 已成立的前提下，(5b) 的失败有多常见？失败由什么刻画？

对随机实例与随机 L（按层号正确辨识 (rho,c)），做两类统计：
  (i)  P_raw  = P[(5b) 对 L 本身成立]
  (ii) P_tau  = P[存在 J-扰动使 (5b) 成立]        （tau 的自由度）
并按 (rho, c, w_is_zero, mu, nu) 分组，看失败集中在哪类。

回答的问题：**tau 障碍是"经常咬人"还是"几乎不咬人"**——这决定 S1/Q-C1 该往哪边攻。
"""
import random
import sys
from collections import Counter, defaultdict
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


def main():
    rng = random.Random(777)
    stat = defaultdict(lambda: [0, 0, 0])      # key -> [raw_ok, tau_ok, total]
    for _trial in range(2500):
        n = rng.choice([5, 6])
        m = rng.choice([2, 3])                       # W = span{e_1..e_m}，A 保持 W ⟹ 行在 W 内即 (5a)
        A, C, L0 = AI.block_instance(rng, n, m)
        CA = mm(C, A)
        J = AI.row_basis(C + CA)
        j = len(J)
        if j == 0:
            continue
        k = rng.choice([2, 3])
        rows = [[Fr(rng.randint(-1, 1)) if t < m else Fr(0) for t in range(n)] for _ in range(k)]
        L = AI.row_basis(rows)
        if len(L) < 2:
            continue
        if not AI.cond_5a_orig(A, C, L):
            continue
        rho, c = layer(L, A, C, J)
        if rho < 1 or c < 1:
            continue
        raw = AI.cond_5b_orig(A, C, L)
        tau_ok = raw
        if not raw:
            for _m2 in range(15):
                d1 = [sum(Fr(rng.randint(-1, 1)) * b[t] for b in J) for t in range(n)]
                d2 = [sum(Fr(rng.randint(-1, 1)) * b[t] for b in J) for t in range(n)]
                L2 = AI.row_basis([[L[0][t] + d1[t] for t in range(n)],
                                   [L[1][t] + d2[t] for t in range(n)]] + [r[:] for r in L[2:]])
                if len(L2) == len(L) and layer(L2, A, C, J) == (rho, c) and AI.cond_5a_orig(A, C, L2):
                    if AI.cond_5b_orig(A, C, L2):
                        tau_ok = True
                        break
        key = (rho, c)
        stat[key][0] += 1 if raw else 0
        stat[key][1] += 1 if tau_ok else 0
        stat[key][2] += 1
    print("(rho,c) -> raw 成立率 / tau 后可成立率 / 样本数")
    for key in sorted(stat):
        raw, tau, tot = stat[key]
        print(f"  {key}: {raw}/{tot} = {raw/tot:.2f} ; tau 后 {tau}/{tot} = {tau/tot:.2f} ; n={tot}")
    print("\n若 'tau 后' 接近 1 => tau 障碍很少咬人（难点在 type+(5a)）；")
    print("若明显 <1 => tau 障碍经常咬人（Q-C1 真的是难点）。")


if __name__ == '__main__':
    main()