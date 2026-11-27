"""kron_known_instances.py —— 在**已知可行**的实例上看 Kronecker 型

动机（Workstream B 的下一步）：上一轮扫描的 4 个实例在 $\\rho\\ge1$ 全不可行，看不到"同一个 $\\rho$
下可行与不可行并存"。这里改用项目里**已知有解**的实例：

  * `mu1_good`：$n=6$、$(\\rho,c)=(3,1)$、$(5a)$ 与 $(5b)$ 都成立（来源
    `proof/rho1_layer/verify_mu1_good_instance.py` §55，构造在下面重抄一份，避免 import 副作用）；
  * `L=C` 型平凡解（任意实例）：作为"可行铅笔"的对照。

对每个候选 $L$ 打印 $q,h,\\rho,c$、Kronecker 数据与 $(5a)/(5b)$ 判定；并断言
"$(5b)$ 成立 ⟺ 无有限初等因子"（本工具的定义一致性）。
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import observer_pencils as OP             # noqa: E402
import kronecker_pencil as KP             # noqa: E402

Fr = Fraction


def _rowspace(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def mu1_good():
    """§55 的实例：n=6，(rho,c)=(3,1)，(5a)+(5b) 都成立。"""
    n = 6

    def companion(cf):
        M = [[Fr(0)] * 3 for _ in range(3)]
        for i in range(2):
            M[i][i + 1] = Fr(1)
        for j in range(3):
            M[2][j] = Fr(cf[j])
        return M

    A = [[Fr(0)] * n for _ in range(n)]
    Aw = companion([3, 2, 1])       # x^3 - x^2 - 2x - 3
    for i in range(3):
        for j in range(3):
            A[i][j] = Aw[i][j]
    A[3][3] = Fr(1)
    A[4][5] = Fr(1)
    A[5][0] = Fr(1)
    A[5][4] = Fr(1)
    C = [[Fr(-1), Fr(-2), Fr(0), Fr(0), Fr(0), Fr(-1)]]
    L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1), Fr(0)]]
    e = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
    V = _rowspace([e[0], e[1], e[2], e[4]])
    return A, C, L0, V


def analyse(name, A, C, L0, L):
    P0, P1, h = OP.pencil_from_L(A, C, L)
    if not LQ.condA(A, C, L):
        print(f'  [{name}] (5a) 失败 ⟹ 非法候选，跳过类型分析')
        return None
    info = OP.observer_pencil(A, C, L)
    CA = LQ.mul(C, A)
    J = _rowspace(list(C) + list(CA))
    c = LQ.rank(L) + LQ.rank(J) - LQ.rank([r[:] for r in L] + J)
    rho = LQ.rank(L) - c
    k = info['kron']
    ok, msg = OP.crosscheck(A, C, L, info)
    print(f'  [{name}] q={len(L)} h={info["h"]} rho={rho} c={c} '
          f'(5a)={info["condA"]} (5b)={info["five_b"]}')
    print(f'      {KP.summary(k)}')
    print(f'      交叉核对: {"OK" if ok else "FAIL"} — {msg}')
    # 定义一致性断言：five_b ⟺ no_fin（给定 h = normal_rank）
    assert info['five_b'] == (k['no_finite_elementary_divisors'] and k['normal_rank'] == info['h']), \
        'five_b 与 no_fin 的定义不一致'
    return dict(rho=rho, c=c, q=len(L), five_b=info['five_b'], kron=k)


def main():
    print('=== 已知可行实例 §55（mu=1, (rho,c)=(3,1)）===')
    A, C, L0, V = mu1_good()
    res = analyse('mu1_good/V', A, C, L0, V)
    assert res['five_b'], '已知可行实例应判为可行！'
    print('\n=== 对照：同一实例上的 L = C ===')
    analyse('mu1_good/L=C', A, C, L0, [row[:] for row in C])
    print('\n=== 对照：L = [C;CA] ===')
    analyse('mu1_good/L=[C;CA]', A, C, L0, LQ.stack(C, LQ.mul(C, A)))
    print('\n完成。')


if __name__ == '__main__':
    main()
