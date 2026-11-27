"""kron_sweep.py —— 撒网找"可行且 rho>=1"的观测器铅笔（精确判定）

用途：Workstream B 需要**更多可行样本**才能谈"受限结构"。单个实例里可行铅笔可能一个都没有
（可行集很薄），所以这里扫多个随机实例、多个候选 $\\mathcal V$，把**可行**的都收集起来。

候选 $\\mathcal V$：$A$-不变闭包（快）+ 模 $\\mathcal J$ 不变族（慢一点）。
判定：`observer_pencils.observer_pencil` 里的**精确** Kronecker 数据（$(5b)$ ⟺ 无有限初等因子）。

用法：python tools/verification/kron_sweep.py [n_seeds]
输出：`workspace/kronecker/data/sweep_<n>seeds.tsv` + 摘要。
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
import modJ_candidates as MJ              # noqa: E402
import kronecker_pencil as KP             # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def _pow(A, k):
    """A^k（k>=1）。"""
    n = len(A)
    R = [row[:] for row in A]
    for _ in range(k - 1):
        R = LQ.mul(R, A)
    return R


def rho_c(L, A, C):
    CA = LQ.mul(C, A)
    J = LQ.stack(C, CA)
    j = LQ.rank(J)
    rv = LQ.rank(L)
    c = rv + j - LQ.rank([r[:] for r in L] + J)
    return rv - c, c


def sweep(n_seeds=30, n=6, trials=4):
    feas, allrows = [], []
    for k in range(n_seeds):
        seed = 1000 + k
        try:
            A, C, L0 = make_instance(n, seed)
        except Exception:
            continue
        cands = []
        # 可观性链：[C; CA; ...; CA^{k-1}]（对每个 k）—— 由构造已知 (5b) 自动成立的自然族
        CAk = [row[:] for row in C]
        for k in range(1, n + 1):
            cands.append([row[:] for row in CAk])
            CAk = CAk + LQ.mul(C, _pow(A, k))
        try:
            cands += list(OP.candidate_Ls(A, C, L0, n_extra=1, trials=trials, seed=seed))
        except AssertionError:
            pass
        try:
            cands += list(MJ.candidate_Ls_modJ(A, C, L0, trials=trials, seed=seed))
        except AssertionError:
            pass
        seen = set()
        for L in cands:
            key = tuple(tuple(str(x) for x in r) for r in L)
            if key in seen:
                continue
            seen.add(key)
            if not LQ.condA(A, C, L):
                continue
            try:
                info = OP.observer_pencil(A, C, L)
            except AssertionError:
                continue
            rho, c = rho_c(L, A, C)
            row = dict(seed=seed, q=len(L), rho=rho, c=c, h=info['h'],
                       five_b=info['five_b'], kron=info['kron'])
            allrows.append(row)
            if info['five_b']:
                feas.append(row)
    return allrows, feas


def dump(rows, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write('seed\tq\trho\tc\th\tfive_b\trank\tfin\tinf\teta\teps\n')
        for r in rows:
            k = r['kron']
            fh.write(f'{r["seed"]}\t{r["q"]}\t{r["rho"]}\t{r["c"]}\t{r["h"]}\t{r["five_b"]}\t'
                     f'{k["normal_rank"]}\t{[d["degree"] for d in k["finite_divisors"]]}\t'
                     f'{[d["degree"] for d in k["infinite_divisors"]]}\t{k["right_min_indices"]}\t'
                     f'{k["left_min_indices"]}\n')


def main():
    n_seeds = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    allrows, feas = sweep(n_seeds, n=n)
    out = os.path.join(_ROOT, 'workspace', 'kronecker', 'data', f'sweep_n{n}_{n_seeds}seeds.tsv')
    dump(allrows, out)
    print(f'\n扫描 n={n} 的 {n_seeds} 个实例：共 {len(allrows)} 个合法铅笔，其中可行 {len(feas)} 个。')
    print('可行铅笔（(5b) 成立）的 (rho,c,q) 与型：')
    for r in feas:
        k = r['kron']
        print(f'  seed={r["seed"]} q={r["q"]} (rho,c)=({r["rho"]},{r["c"]}) h={r["h"]} '
              f'fin={[d["degree"] for d in k["finite_divisors"]]} eta={k["right_min_indices"]} '
              f'eps={k["left_min_indices"]}')
    if not feas:
        print('  （无）—— 说明可行集很薄，需要从**已知可行实例**出发（见 kron_known_instances.py）')
    print(f'TSV: {out}')


if __name__ == '__main__':
    main()
