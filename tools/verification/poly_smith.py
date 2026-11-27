r"""多项式矩阵的 **Smith 形 / 行列式因子**（精确 $\mathbb Q[\lambda]$ 算术）。

## 为什么有这个模块（专家 2026-11-01 §4.4）

"固定 $U$ 的谱判据"目前是**枚举全部 $(r+t)$ 个极大子式再取 gcd**（`spectral_gcd` / `feasible_by_minors`），
组合爆炸。改用**行列式因子**后同一条判据变成"$\Delta_b$ 是非零常数"，且可在**精确算术模型**下多项式时间算出
（Kaltofen–Krishnamoorthy–Saunders 1987；Storjohann–Labahn 1997）。

## 记号与定理

$Q(\lambda)$ 为 $a\times b$ 多项式矩阵（$a\ge b$，元素 = `Fraction` 系数列表，低次在前）。

- **Smith 不变因子**：存在幺模 $P,R$ 使 $PQR=\operatorname{diag}(d_1,\dots,d_r,0,\dots)$，$d_1\mid d_2\mid\cdots$；
- **行列式因子**：$\Delta_b=\gcd\{\text{全部 } b\times b \text{ 极大子式}\}=d_1d_2\cdots d_b$（差非零常数）；
- **判据**：$\operatorname{rank}Q(\lambda)=b\ \ \forall\lambda\in\mathbb C\iff\Delta_b\in\mathbb Q^\times$
  （$\mathbb C$ 上非常数多项式必有根）。

## 等级

本模块是**工具**，不是判据。它的正确性由 [verify_smith.py](verify_smith.py) 交叉核对：
Smith 路径 vs "枚举子式 + gcd" 路径 vs 逐 $\lambda$ 点检查。

## 规模

`ScaleError` 在矩阵 `> 14×12` 或次数 `> 10` 时抛出；调用点应退回旧路径并**打印**用了哪条
（静默变慢比报错更糟，见 CLAUDE §10.1）。

用法：

```python
import poly_smith as PS
ok, delta, info = PS.full_col_rank_constant(Q)   # Q: a×b，元素是系数列表
```
"""
import itertools
import math
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import spectral_gcd as SG

ptrim, padd, psub, pmul, pdivmod, pgcd, pdeg = (
    SG.ptrim, SG.padd, SG.psub, SG.pmul, SG.pdivmod, SG.pgcd, SG.pdeg)

MAX_A, MAX_B, MAX_DEG = 14, 12, 10
MAX_STEPS = 400000


class ScaleError(RuntimeError):
    """超出本模块的设计规模（调用点应退回枚举路径）。"""


def pzero(p):
    return ptrim(p) == [Fr(0)]


def pmonic(p):
    """首一化；零多项式返回 [0]。"""
    p = ptrim(p)
    if pzero(p):
        return [Fr(0)]
    lead = p[-1]
    return ptrim([x / lead for x in p])


def _shape(Q):
    a = len(Q)
    b = len(Q[0]) if a else 0
    return a, b


def _maxdeg(Q):
    return max((pdeg(x) for row in Q for x in row), default=-1)


def _check_scale(Q):
    a, b = _shape(Q)
    if a > MAX_A or b > MAX_B:
        raise ScaleError(f'矩阵 {a}x{b} 超过 {MAX_A}x{MAX_B}')
    if _maxdeg(Q) > MAX_DEG:
        raise ScaleError(f'次数 {_maxdeg(Q)} 超过 {MAX_DEG}')


def smith_invariants(Q, max_steps=MAX_STEPS):
    r"""返回 Smith 不变因子 $[d_1,\dots,d_r]$（首一，$d_i\mid d_{i+1}$）。

    标准算法：逐个对角位置 (k,k) 用行/列带余除法把行列清零；若 $d_k$ 不整除右下角某元，
    就把该行加到第 $k$ 行重做（每次"坏"情形都使 $d_k$ 的次数严格下降，故终止）。
    """
    _check_scale(Q)
    A = [[ptrim(list(x)) for x in row] for row in Q]
    a, b = _shape(A)
    if a == 0 or b == 0:
        return []
    if any(pzero(x) is False and pdeg(x) < 0 for row in A for x in row):
        raise ValueError('内部错误：出现负次数多项式')
    out = []
    k = 0
    steps = 0
    while k < min(a, b):
        # 找 (k,k) 右下第一个非零元
        piv = None
        for i in range(k, a):
            for j in range(k, b):
                if not pzero(A[i][j]):
                    piv = (i, j)
                    break
            if piv is not None:
                break
        if piv is None:
            break
        i0, j0 = piv
        if i0 != k:
            A[k], A[i0] = A[i0], A[k]
        if j0 != k:
            for r in range(a):
                A[r][k], A[r][j0] = A[r][j0], A[r][k]
        assert not pzero(A[k][k]), '内部错误：主元为零'
        # 把第 k 行/列除主元外清零，并保证主元整除右下全部元素
        while True:
            steps += 1
            if steps > max_steps:
                raise ArithmeticError(f'Smith 形未在 {max_steps} 步内收敛')
            did = False
            for i in range(k + 1, a):
                if pzero(A[i][k]):
                    continue
                q, r = pdivmod(A[i][k], A[k][k])
                A[i] = [psub(A[i][t], pmul(q, A[k][t])) for t in range(b)]
                if not pzero(A[i][k]):
                    A[k], A[i] = A[i], A[k]
                    did = True
                    break
            if did:
                continue
            for j in range(k + 1, b):
                if pzero(A[k][j]):
                    continue
                q, r = pdivmod(A[k][j], A[k][k])
                for r2 in range(a):
                    A[r2][j] = psub(A[r2][j], pmul(q, A[r2][k]))
                if not pzero(A[k][j]):
                    for r2 in range(a):
                        A[r2][k], A[r2][j] = A[r2][j], A[r2][k]
                    did = True
                    break
            if did:
                continue
            bad = None
            for i in range(k + 1, a):
                for j in range(k + 1, b):
                    if pzero(A[i][j]):
                        continue
                    _q, r = pdivmod(A[i][j], A[k][k])
                    if not pzero(r):
                        bad = i
                        break
                if bad is not None:
                    break
            if bad is not None:
                A[k] = [padd(A[k][t], A[bad][t]) for t in range(b)]
                continue
            break
        assert all(pzero(A[i][k]) for i in range(k + 1, a)), '列未清零'
        assert all(pzero(A[k][j]) for j in range(k + 1, b)), '行未清零'
        out.append(pmonic(A[k][k]))
        k += 1
    # 不变因子的整除链是 Smith 形的定义性质，作为内部不变量断言
    for i in range(len(out) - 1):
        _q, r = pdivmod(out[i + 1], out[i])
        assert pzero(r), f'不变因子不整除: d{i + 1} 不被 d{i} 整除'
    return out


def det_divisor(Q):
    r"""$\Delta_b=d_1\cdots d_b$（首一）；若 $\operatorname{rank}Q<b$ 则返回 $[0]$。"""
    a, b = _shape(Q)
    if b == 0:
        return [Fr(1)]
    invs = smith_invariants(Q)
    if len(invs) < b:
        return [Fr(0)]
    prod = [Fr(1)]
    for d in invs[:b]:
        prod = pmul(prod, d)
    return pmonic(prod)


def det_divisor_by_minors(Q, max_subsets=4000):
    r"""同一条 $\Delta_b$，但用"枚举全部 $b$ 行子集 + `pdet` + gcd"（旧路径，交叉验证用）。"""
    a, b = _shape(Q)
    if b == 0:
        return [Fr(1)]
    if math.comb(a, b) > max_subsets:
        raise ScaleError(f'子式个数 C({a},{b}) 超过 {max_subsets}')
    g = None
    for rows in itertools.combinations(range(a), b):
        d = SG.pdet([[Q[r][c] for c in range(b)] for r in rows])
        if pzero(d):
            continue
        g = d if g is None else SG.pgcd(g, d)
        if pdeg(g) == 0:
            break                     # 已是常数 ⟹ 不可能再变小
    if g is None:
        return [Fr(0)]
    return pmonic(g)


def full_col_rank_constant(Q):
    r"""$\operatorname{rank}Q(\lambda)=b\ \forall\lambda$ ？

    返回 `(ok, delta, info)`；`info` 里有 `rank`（Smith 秩 = $\mathbb Q(\lambda)$ 上的秩）、
    `deg`、`shape`、以及 `max_bits`（系数比特长度，按 CLAUDE §7.21 打印不变量用）。
    """
    a, b = _shape(Q)
    if b == 0:
        return True, [Fr(1)], dict(rank=0, deg=0, shape=(a, b), max_bits=0)
    invs = smith_invariants(Q)
    rank = len(invs)
    if rank < b:
        return False, [Fr(0)], dict(rank=rank, deg=-1, shape=(a, b), max_bits=0)
    delta = [Fr(1)]
    for d in invs[:b]:
        delta = pmul(delta, d)
    delta = pmonic(delta)
    bits = max((abs(int(x.numerator)).bit_length() + int(x.denominator).bit_length()
                for x in delta), default=0)
    return (pdeg(delta) == 0), delta, dict(rank=rank, deg=pdeg(delta), shape=(a, b),
                                           max_bits=bits)


def rank_at(Q, lam):
    r"""在 $\lambda=\lambda_0$（有理数）处求数值秩：把多项式求值成有理矩阵再 `AI.rank`。"""
    import audit_independent as AI
    a, b = _shape(Q)
    M = []
    for i in range(a):
        row = []
        for j in range(b):
            acc = Fr(0)
            for t, c in enumerate(Q[i][j]):
                acc += c * (lam ** t)
            row.append(acc)
        M.append(row)
    return AI.rank(M)


def make_pencil(U, P0, P1):
    r"""把 $[U\mid P(\lambda)]$ 拼成多项式矩阵：$U$ 是常数列，$P$ 是 $P_0+\lambda P_1$。

    U: $r$ 个长度为 $w_m$ 的列向量；P0/P1: $w_m\times t$。
    """
    a = len(P0)
    r = len(U)
    t = len(P0[0]) if a else 0
    Q = []
    for i in range(a):
        row = [ptrim([U[j][i]]) for j in range(r)]
        row += [ptrim([P0[i][j], P1[i][j]]) for j in range(t)]
        Q.append(row)
    return Q
