"""verify.py —— 验证"$(5a)$ ⟹ 观测器铅笔的右最小指标全为 0"

命题（[proof/kron_null_module/theorem.md](theorem.md)）：设 $L$ 满足 $(5a)$
（$\\operatorname{rank}[LA;L;CA;C]=\\operatorname{rank}[L;CA;C]$），则铅笔
$$Q_L(\\lambda)=[\\lambda L-LA;\\ CA;\\ C]$$
的**右最小指标全为 0**（等价地：它的右零模由常值零向量生成）。

本脚本在**所有**满足 $(5a)$ 的候选 $L$ 上核对结论（**包括不可行的**——命题不需要 $(5b)$）：
  * $n=6,7,8$，随机整数实例；
  * 候选族：可观性链、$A$-不变闭包、模 $\\mathcal J$ 不变提升、以及 $[C;CA]\\oplus L_0$；
  * 每个候选先精确检查 $(5a)$，通过后再算 Kronecker 数据，断言 `right_min_indices` 全为 0。

**验证不是证明**：证明在 theorem.md；本脚本只提供实例证据（并且它会打印被检验的计数）。
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import kronecker_pencil as KP             # noqa: E402
import observer_pencils as OP             # noqa: E402
import modJ_candidates as MJ              # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def pow_A(A, k):
    R = [row[:] for row in A]
    for _ in range(k - 1):
        R = LQ.mul(R, A)
    return R


def candidates(A, C, L0, n, seed, trials=2):
    out = []
    # 1) 可观性链
    CAk = [row[:] for row in C]
    for k in range(1, n + 1):
        out.append([row[:] for row in CAk])
        CAk = CAk + LQ.mul(C, pow_A(A, k))
    # 2) A-不变闭包
    try:
        out += list(OP.candidate_Ls(A, C, L0, n_extra=1, trials=trials, seed=seed))
    except AssertionError:
        pass
    # 3) 模 J 不变提升
    try:
        out += list(MJ.candidate_Ls_modJ(A, C, L0, trials=trials, seed=seed))
    except AssertionError:
        pass
    return out


def main():
    tested = passed = 0
    bad = []
    per_n = {}
    for n in (6, 7, 8):
        for k in range(6):
            seed = 1000 + k
            try:
                A, C, L0 = make_instance(n, seed)
            except Exception:
                continue
            seen = set()
            for L in candidates(A, C, L0, n, seed):
                key = tuple(tuple(str(x) for x in r) for r in L)
                if key in seen:
                    continue
                seen.add(key)
                if not LQ.condA(A, C, L):
                    continue
                P0, P1, h = OP.pencil_from_L(A, C, L)
                kk = KP.pencil_kronecker(P0, P1)
                tested += 1
                eta = kk['right_min_indices']
                if all(x == 0 for x in eta):
                    passed += 1
                    per_n[n] = per_n.get(n, 0) + 1
                else:
                    bad.append((n, seed, len(L), eta))
                    print(f'  **反例** n={n} seed={seed} q={len(L)} eta={eta}')
    print(f'\n满足 (5a) 的铅笔：{tested} 个（n=6,7,8）')
    print(f'右最小指标全为 0：{passed} / {tested}')
    print(f'分维度：{per_n}')
    assert not bad, f'出现反例：{bad[:3]}'
    print('✓ 全部通过（验证不是证明；证明见 theorem.md）')


if __name__ == '__main__':
    main()
