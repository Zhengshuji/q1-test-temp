r"""对账实验：$p=1$ 时 $q=2$ 的可行性有多常见？（检验"$q_{\\min}\\le2$"的猜测）

做法（**只给充分见证，不做否定结论**）：对小整数实例 $(A,C,L_0)$，枚举有限候选集
$R\\in\\{-1,0,1\\}^{n}$，对每个 $(A,C,L_0,R)$ 用 `consistency_checks.check_candidate` 精确判定
$(5a)$ 与 $(5b)$；只要有一个 $R$ 通过，就**证明**该实例 $q=2$ 可行（$q_{\\min}\\le2$）。

输出：每个实例的 $(\\dim K,\\ \\omega\\ \\text{是否总能}<2,\\ \\text{是否找到可行 }R)$ 与总体比例。
**限定**：找不到可行 $R$ **不**说明 $q=2$ 不可行（候选集太小）；故本实验只支持"$q_{\\min}\\le2$ 常见"。
"""

import os
import sys
import itertools
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import consistency_checks as CC   # noqa: E402

F = Fr


def to_rows(M):
    return [[F(x) for x in row] for row in M]


def instance_ok(A, C, L0, R):
    L = [row[:] for row in L0] + [row[:] for row in R]
    try:
        res = CC.check_candidate(A, C, L0, L)
    except Exception:
        return None, None
    if not isinstance(res, dict):
        return None, None
    return res.get('cond'), res.get('five_b')


def main():
    vals = (-1, 0, 1)
    As = []
    # n=3 的小整数 A：限定第一行 = e2（使 rank[C;CA]=2），其余 6 个位置枚举
    for rest in itertools.product(vals, repeat=6):
        A = [[F(0), F(1), F(0)],
             [F(rest[0]), F(rest[1]), F(rest[2])],
             [F(rest[3]), F(rest[4]), F(rest[5])]]
        As.append(A)
    C = [[F(1), F(0), F(0)]]

    total = 0
    found = 0
    by_k = {}      # k -> [found, total]
    examples = []
    for A in As:
        for i in range(3):
            L0 = [[F(1) if j == i else F(0) for j in range(3)]]
            total += 1
            # dim K = n - rank[C;CA]
            import linalg_q as LQ
            M = C + LQ.mul(C, A)
            k = 3 - LQ.rank(M)
            by_k.setdefault(k, [0, 0])
            by_k[k][1] += 1
            ok_any = False
            for r in itertools.product(vals, repeat=3):
                R = [[F(r[0]), F(r[1]), F(r[2])]]
                cond, five_b = instance_ok(A, C, L0, R)
                if cond and five_b:
                    ok_any = True
                    if len(examples) < 3:
                        examples.append((A, L0, R))
                    break
            if ok_any:
                found += 1
                by_k[k][0] += 1
    print(f'实例总数 {total}（n=3, p=1, q=2；A 的第一行固定为 e2，其余 6 位 ∈ {{-1,0,1}}；L0 取 e1..e3）')
    print(f'找到 q=2 可行见证（R ∈ {{-1,0,1}}^3）的实例数 {found}  ⟹ 比例 {found}/{total}')
    print('按 dim K 分解（found/total）：')
    for k in sorted(by_k):
        f, t = by_k[k]
        print(f'  dim K={k}: {f}/{t}')
    for A, L0, R in examples:
        print(f'  例：A={[[int(x) for x in row] for row in A]} L0={[[int(x) for x in row] for row in L0]} '
              f'R={[[int(x) for x in row] for row in R]}')


if __name__ == '__main__':
    main()
