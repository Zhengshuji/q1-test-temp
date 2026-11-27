"""qmin_scan_pr.py —— 多 $p,r$ 的可观测实例上测 $q_{\\min}$ 相对闭包的偏移（WP2 第 5 步）

上一轮（[qmin_scan.py](qmin_scan.py)）只做了 $n=5,p=r=1$，且 $L_0$ 取可观性矩阵行的**随机组合**
（条目增长快，$n\\ge6$ 太慢）。本轮改为：

* $A$ 取稀疏小整数（$\\{0,\\pm1\\}$）；
* $C$ 取 $p$ 个稀疏标准基行的小组合；
* $L_0$ 直接取 $[C;CA;CA^2]$ 中的 $r$ 行（**自动可估**，条目只到 $\\|A\\|^2$ 量级），并要求 $\\operatorname{rank}[C;L_0]=p+r$。

然后对每个实例扫 $q=$ 闭包 $\\dots$ 闭包 $+2$，每阶 12 条链式前像样本，用 Toeplitz 判据判 $(5b)$。

**假设 $H$**：$q_{\\min}=\\mathrm{cl}+1$（等价说法：$(5a)$ 的最小阶上 $(5b)$ 从不成立，再高一阶总成立）。
本脚本的任务是**证伪**它。

用法：python -u tools/verification/qmin_scan_pr.py
"""

import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import omega_construct as OC              # noqa: E402

F = Fraction


def observability_matrix(A, C, depth=None):
    rows = [r[:] for r in C]
    cur = [r[:] for r in C]
    for _ in range((depth or len(A)) - 1):
        cur = LQ.mul(cur, A)
        rows += [r[:] for r in cur]
    return rows


def make_instance(n, p, r, seed):
    rng = random.Random(seed)
    # 稀疏小整数 A
    A = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if rng.random() < 0.35:
                A[i][j] = F(rng.choice([-1, 0, 1]))
    # C：p 个稀疏标准基行（带小系数）
    C = []
    used = set()
    for _ in range(p):
        row = [F(0)] * n
        for _t in range(rng.randint(1, 2)):
            j = rng.randrange(n)
            used.add(j)
            row[j] += F(rng.choice([-1, 1]))
        C.append(row)
    if LQ.rank(C) != p:
        return None
    # L0：取 [C; CA; CA^2] 中的 r 行（自动可估），要求与 C 的行独立
    S = observability_matrix(A, C, depth=min(3, n))
    base = [row[:] for row in C]
    L0 = []
    cand = S[len(C):]                      # 去掉 C 本身
    rng.shuffle(cand)
    for row in cand:
        if LQ.rank(base + L0 + [row]) > len(base) + len(L0):
            L0.append(row[:])
        if len(L0) == r:
            break
    if len(L0) != r:
        return None
    if LQ.rank([x[:] for x in C] + [x[:] for x in L0]) != p + r:
        return None
    return A, C, L0


def main():
    print('=== 多 (p,r) 可观测实例：q_min 相对闭包的偏移 ===')
    stats = dict(inst=0, obs=0, found=0, dist={}, nohit=[])
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    made = make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    stats['inst'] += 1
                    O = observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue                       # 不功能可观测
                    stats['obs'] += 1
                    clo = len(OC.closure(A, C, L0))
                    first, cells = None, []
                    for q in range(clo, min(n, clo + 2) + 1):
                        samples = OC.sample_chains(A, C, L0, q, 12, seed * 13 + q)
                        feas = sum(1 for L in samples if TC.analyse(A, C, L)['five_b'])
                        cells.append(f'q={q}:{feas}/{len(samples)}')
                        if feas and first is None:
                            first = q
                    if first is None:
                        stats['nohit'].append((n, p, r, seed, clo))
                        tag = 'q_min 未知（≤闭包+2 未找到）'
                    else:
                        stats['found'] += 1
                        stats['dist'][first - clo] = stats['dist'].get(first - clo, 0) + 1
                        tag = f'偏移 +{first - clo}'
                    print(f'  n={n} p={p} r={r} seed={seed} 闭包={clo} ' + ' '.join(cells) + '  → ' + tag)
    print(f'\n合计：候选实例 {stats["inst"]}，可观测 {stats["obs"]}，找到见证 {stats["found"]}')
    print(f'偏移分布 {stats["dist"]}（假设 H 要求全部是 +1）')
    if stats['nohit']:
        print(f'未找到见证（需更大 q 或更强搜索）：{stats["nohit"]}')


if __name__ == '__main__':
    main()
