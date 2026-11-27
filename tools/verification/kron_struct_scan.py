"""kron_struct_scan.py —— Workstream B 的五步实验（专家 2026-11-02）

对一组真实实例 $(A,C,L_0)$，枚举"对 $x\\mapsto xA$ 不变、含 $\\operatorname{row}L_0$"的子空间
$\\mathcal V$（每个 $\\mathcal V$ 给一个候选 $L$），构造观测器铅笔 $Q_L(\\lambda)=[\\lambda L-LA;CA;C]$，
记录它的 Kronecker 数据，并按专家的五步整理：

  1. 只有右奇异块（$\\varepsilon=\\varnothing$ 且无有限初等因子）；
  2. 只有左奇异块（$\\eta=\\varnothing$ 且无有限初等因子）；
  3. 正则块 + 奇异块（有有限初等因子）；
  4. $U$（即 $\\mathcal V$）变化时最小指标如何变；
  5. 固定 $\\rho$ 下可行/不可行的对比。

输出：`workspace/kronecker/data/scan_<seed>.tsv` + 终端摘要。
**证据，不是证明**：报告写清"记录到的类型"，不声称"只能出现这些"。
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

F = Fraction


def quotient_data(A, C, L):
    """返回 (rho, c)：$\\rho=\\dim\\pi(\\mathcal V)$、$c=\\dim(\\mathcal V\\cap\\mathcal J)$。"""
    CA = LQ.mul(C, A)
    J = LQ.stack(C, CA)
    V = L
    rj = LQ.rank(J)
    rv = LQ.rank(V)
    rvj = LQ.rank(V + J)
    c = rv + rj - rvj            # dim(V ∩ J)
    rho = rv - c
    return rho, c


def collect(seeds=(1002, 1003, 1015, 1019), n=6, trials=6):
    rows = []
    for seed in seeds:
        from find_layer_instance import make_instance
        A, C, L0 = make_instance(n, seed)
        seen = set()
        skipped = 0
        # 先放"规范"候选（已知可行的那类）：L = C、L = [C;CA]、L = [C;CA;L0]
        CA = LQ.mul(C, A)
        canon = [[row[:] for row in C], LQ.stack(C, CA)]
        canon.append([row[:] for row in C] + [row[:] for row in CA] + [row[:] for row in L0])
        modj = list(MJ.candidate_Ls_modJ(A, C, L0, trials=trials, seed=seed))
        for L in canon + list(OP.candidate_Ls(A, C, L0, n_extra=1, trials=trials, seed=seed)) + modj:
            key = tuple(tuple(str(x) for x in r) for r in L)
            if key in seen:
                continue
            seen.add(key)
            try:
                info = OP.observer_pencil(A, C, L)
            except AssertionError as e:
                print(f'  [seed {seed}] 跳过：{e}')
                continue
            if not info['condA']:
                skipped += 1
                continue
            rho, c = quotient_data(A, C, L)
            k = info['kron']
            rows.append(dict(
                seed=seed, q=len(L), h=info['h'], rho=rho, c=c,
                fin=[d['degree'] for d in k['finite_divisors']],
                inf=[d['degree'] for d in k['infinite_divisors']],
                eta=k['right_min_indices'], eps=k['left_min_indices'],
                no_fin=k['no_finite_elementary_divisors'],
                five_a=info['condA'], five_b=info['five_b'],
                rows=k['shape'][0], cols=k['shape'][1],
            ))
        print(f'  [seed {seed}] 记录 {len(seen)} 个，跳过 (5a) 失败 {skipped} 个')
    return rows


def dump_tsv(rows, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write('seed\tq\th\trho\tc\trows\tcols\tfin\tinf\teta\teps\tno_fin\tfive_a\tfive_b\n')
        for r in rows:
            fh.write(f'{r["seed"]}\t{r["q"]}\t{r["h"]}\t{r["rho"]}\t{r["c"]}\t{r["rows"]}\t{r["cols"]}\t'
                     f'{r["fin"]}\t{r["inf"]}\t{r["eta"]}\t{r["eps"]}\t{r["no_fin"]}\t{r["five_a"]}\t{r["five_b"]}\n')


def report(rows):
    print(f'\n共记录 {len(rows)} 个观测器铅笔。')
    print('\n--- 步骤 1：只有右奇异块（eps 空 且 no_fin）---')
    s1 = [r for r in rows if not r['eps'] and r['no_fin']]
    print(f'  {len(s1)} 个：' + ('; '.join(f"seed{r['seed']} q={r['q']} eta={r['eta']}" for r in s1[:5]) or '无'))
    print('--- 步骤 2：只有左奇异块（eta 空 且 no_fin）---')
    s2 = [r for r in rows if not r['eta'] and r['no_fin']]
    print(f'  {len(s2)} 个：' + ('; '.join(f"seed{r['seed']} q={r['q']} eps={r['eps']}" for r in s2[:5]) or '无'))
    print('--- 步骤 3：正则块 + 奇异块（no_fin 为 False）---')
    s3 = [r for r in rows if not r['no_fin']]
    print(f'  {len(s3)} 个；例如 ' + ('; '.join(
        f"seed{r['seed']} q={r['q']} fin={r['fin']} eta={r['eta']} eps={r['eps']}" for r in s3[:3]) or '无'))
    print('--- 步骤 4：随 $\\mathcal V$ 变化的最小指标 ---')
    by_seed = {}
    for r in rows:
        by_seed.setdefault(r['seed'], []).append(r)
    for seed, rs in by_seed.items():
        print(f'  seed {seed}: ' + ' | '.join(
            f"q={r['q']} eta={r['eta']} eps={r['eps']} fin={r['fin']}" for r in rs))
    print('--- 步骤 5：固定 $\\rho$ 下可行/不可行 ---')
    by_rho = {}
    for r in rows:
        by_rho.setdefault(r['rho'], []).append(r)
    for rho, rs in sorted(by_rho.items()):
        feas = [r for r in rs if r['five_b']]
        print(f'  rho={rho}: {len(rs)} 个铅笔，其中 (5b) 成立 {len(feas)} 个'
              + ('' if not feas else '；例如 q=' + str(feas[0]['q'])))
    # 全局检查
    bad = [r for r in rows if r['five_a'] and r['five_b'] and not r['no_fin']]
    assert not bad, '内部矛盾：five_b 为真但 no_fin 为假'
    bad2 = [r for r in rows if not r['five_a']]
    print(f'\n(5a) 失败的候选 {len(bad2)} 个（构造上应全为 0）')


def main():
    rows = collect()
    out = os.path.join(_ROOT, 'workspace', 'kronecker', 'data', 'scan_2026-11-02.tsv')
    dump_tsv(rows, out)
    print(f'TSV 已写入 {out}')
    report(rows)


if __name__ == '__main__':
    main()
