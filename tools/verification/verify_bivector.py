r"""`bivector.has_decomposable` 的**可靠性**交叉核对（不是完备性）。

检查的是"算法不会说谎"，而不是"算法总能给出答案"：

| 算法输出 | 必须成立的检查 |
|---|---|
| `False`（由 $(x,y,z)^s\subseteq I$ 判定）| 小整数格点上**找不到**可分解元（否则是 bug）|
| `True`（给了见证）| 见证**确实**可分解（`rank M(p)\le2`）|
| `True`（维数计数/各向同性，无见证）| 只记录，不做格点核对（见证需要代数数）|
| `None`（未决）| 只计数 |

另外**必须**各打印至少一个"有解"与"无解"的实例——否则是空检验（CLAUDE §7 / 地基检查）。

**等级**：精确验证（有理算术、有限格点）。格点搜索只能证伪，不能证真。

用法：python tools/verification/verify_bivector.py
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import bivector as BV


def brute(K, m, bound=2):
    """格点枚举；返回第一个可分解元或 None。"""
    l = len(K)
    for coefs in itertools.product(range(-bound, bound + 1), repeat=l):
        if all(c == 0 for c in coefs):
            continue
        p = [sum(Fr(coefs[j]) * K[j][i] for j in range(l)) for i in range(len(K[0]))]
        if BV.decomposable(p, m):
            return p
    return None


def rand_vec(rng, N):
    while True:
        v = [Fr(rng.randint(-2, 2)) for _ in range(N)]
        if any(x != 0 for x in v):
            return v


def rand_indep(rng, N, l):
    while True:
        vs = []
        for _ in range(l):
            while True:
                v = rand_vec(rng, N)
                if BV.AI.rank(vs + [v]) > len(vs):
                    vs.append(v)
                    break
        if len(vs) == l:
            return vs


def main():
    rng = random.Random(20261101)
    stats = {'True': 0, 'False': 0, 'None': 0}
    bad = []
    examples = {'yes': None, 'no': None}
    for m in (3, 4, 5):
        N = m * (m - 1) // 2
        for l in (1, 2, 3):
            if l > N:
                continue
            for t in range(12):
                K = rand_indep(rng, N, l)
                verdict, wit, info = BV.has_decomposable(K, m)
                key = str(verdict)
                stats[key] = stats.get(key, 0) + 1
                if verdict is False:
                    w = brute(K, m, bound=2)
                    if w is not None:
                        bad.append(('说 False 但格点找到', m, l, K, w, info))
                    if examples['no'] is None:
                        examples['no'] = (m, l, K, info)
                elif verdict is True and wit is not None:
                    if not BV.decomposable(wit, m):
                        bad.append(('见证不可分解', m, l, K, wit, info))
                    if examples['yes'] is None:
                        examples['yes'] = (m, l, K, info)
                elif verdict is True and wit is None:
                    w = brute(K, m, bound=1)      # 只作记录，见证可能是代数数
                    if examples['yes'] is None:
                        examples['yes'] = (m, l, K, dict(info, brute=('found' if w else 'grid-miss')))
    print('统计：', stats)
    print('\n示例（有解）：', examples['yes'])
    print('示例（无解）：', examples['no'])
    # m=4、ℓ≥2 的"恒真"命题：单独核对
    ok4 = 0
    for t in range(20):
        K = rand_indep(rng, 6, 2)
        v, w, info = BV.has_decomposable(K, 4)
        assert v is True, 'm=4,ℓ=2 应恒真'
        ok4 += 1
    print(f'\nm=4、ℓ=2 恒真命题：“各向同性”{ok4}/20 全为 True ✓')
    for b in bad:
        print('  !!', b)
    assert not bad, '可靠性检查失败'
    assert examples['yes'] is not None and examples['no'] is not None, '缺 True/False 示例（空检验）'
    print('\n可靠性检查 ✓（无“说谎”的情形）')


if __name__ == '__main__':
    main()
