"""kron_t4b_prime.py —— 检验专家的 T4-b' 与链族上的 T4-b

**T4-b'（专家 2026-11-02 §7.2）**：对观测器铅笔 $Q_L$，若
$$w\\in\\ker L,\\quad Cw=CAw=0,\\quad LAw\\in\\operatorname{im}L,$$
则 $LAw=0$。
（若成立 ⟹ 不存在由这类向量产生的"长度 ≥ 2 的无穷链"。）

本脚本：
  1. 对样本里每个满足 $(5a)$ 的 $L$，构造
     $K_\\infty=\\{w:\\ Lw=0,\\ Cw=CAw=0\\}$，检查
     $LA(K_\\infty)\\cap\\operatorname{im}L$ 是否平凡；
  2. 对**可观性链**族单独核对 T4-b 的干净形式：$\\sum_j\\varepsilon_j=\\operatorname{rank}L$。

用法：python tools/verification/kron_t4b_prime.py
"""

import os
import sys
from collections import Counter
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import kronecker_pencil as KP             # noqa: E402
import observer_pencils as OP             # noqa: E402
import kron_sweep as KS                   # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def row_basis(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def k_infty(A, C, L):
    """$K_\\infty=\\{w: Lw=0, Cw=CAw=0\\}$ 的基（列向量）。"""
    CA = LQ.mul(C, A)
    M = LQ.stack(L, C, CA)
    return LQ.nullspace(M)          # 每行是一个基向量（行约定）


def im_L(L):
    """$\operatorname{im}L\subseteq\mathbb C^q$ 的基（L 的各列，长度 $q$）。"""
    q, n = len(L), len(L[0])
    cols = [[L[i][j] for i in range(q)] for j in range(n)]
    return row_basis(cols)


def la_on(A, L, w):
    """$(LA)w$。"""
    n = len(A)
    v = [sum(w[i] * A[i][t] for i in range(n)) for t in range(n)]   # Aw（列约定）
    m = len(L)
    return [sum(L[r][t] * v[t] for t in range(n)) for r in range(m)]


def check_t4b_prime(A, C, L):
    """返回 (平凡?, 维数信息)。$LA(K_\\infty)\\cap\\operatorname{im}L$ 是否平凡。"""
    Kin = k_infty(A, C, L)              # 行 = 基向量
    if not Kin:
        return True, (0, 0)
    LAK = row_basis([la_on(A, L, w) for w in Kin])
    imL = im_L(L)
    inter = LQ.rank(LAK) + LQ.rank(imL) - LQ.rank(LAK + imL)
    return inter == 0, (LQ.rank(LAK), LQ.rank(imL), inter)


def main():
    print('=== 1. T4-b\'：对样本中所有满足 (5a) 的铅笔 ===')
    bad = []
    tested = 0
    inter_dims = Counter()
    for n in (6, 7):
        for k in range(4):
            seed = 1000 + k
            try:
                A, C, L0 = make_instance(n, seed)
            except Exception:
                continue
            seen = set()
            cands = []
            CAk = [row[:] for row in C]
            for t in range(1, n + 1):
                cands.append([row[:] for row in CAk])
                CAk = CAk + LQ.mul(C, KS._pow(A, t))
            cands += list(OP.candidate_Ls(A, C, L0, n_extra=1, trials=2, seed=seed))
            for L in cands:
                key = tuple(tuple(str(x) for x in r) for r in L)
                if key in seen:
                    continue
                seen.add(key)
                if not LQ.condA(A, C, L):
                    continue
                tested += 1
                ok, info = check_t4b_prime(A, C, L)
                inter_dims[info[2] if len(info) == 3 else 0] += 1
                if not ok:
                    bad.append((n, seed, len(L), info))
    print(f'  测试 {tested} 个铅笔；LA(K_inf) ∩ im L 非平凡的有 {len(bad)} 个')
    print(f'  交的维数分布: {dict(inter_dims)}')
    if bad:
        for b in bad[:3]:
            print('   **反例**', b)
    assert not bad, 'T4-b\' 出现反例（请人工核查）'

    print('\n=== 2. 链族的 T4-b：sum(eps) = rank L ？===')
    rows = []
    for n in (6, 7, 8):
        for k in range(4):
            seed = 1000 + k
            try:
                A, C, L0 = make_instance(n, seed)
            except Exception:
                continue
            CAk = [row[:] for row in C]
            for t in range(1, n + 1):
                L = [row[:] for row in CAk]
                CAk = CAk + LQ.mul(C, KS._pow(A, t))
                if not LQ.condA(A, C, L):
                    continue
                info = OP.observer_pencil(A, C, L)
                if not info['five_b']:
                    continue
                kk = info['kron']
                sum_eps = sum(kk['left_min_indices'])
                rankL = LQ.rank(L)
                rows.append((n, t, len(L), rankL, sum_eps, info['h'],
                             sum(kk['right_min_indices']),
                             sum(d['degree'] for d in kk['infinite_divisors'])))
    ok = sum(1 for r in rows if r[4] == r[3])
    print(f'  链族可行铅笔 {len(rows)} 个；sum(eps)=rank L 成立 {ok}/{len(rows)}')
    for r in rows[:6]:
        print(f'    n={r[0]} k={r[1]} q={r[2]} rankL={r[3]} sum_eps={r[4]} h={r[5]} '
              f'sum_eta={r[6]} d_inf={r[7]}')
    assert ok == len(rows), '链族上 sum(eps)=rank L 失败'


if __name__ == '__main__':
    main()
