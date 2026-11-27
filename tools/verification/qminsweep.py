"""qminsweep.py —— 用证书化的逐阶判定扫描 $q_{\\min}$（$q_0$ 起，逐阶向上）

对每个实例：从 $q_0$ 开始逐阶调用 [joint_theta.py](joint_theta.py) 的 `decide`，
遇到 `FEASIBLE`（带见证、过七条检查）即停 ⟹ 该阶即 $q_{\\min}$（下界由前面各阶的不可行结论给出）。

结果写入 `workspace/augmentation_family/data/qmin_certified.tsv`（增量保存，便于分批）。

用法：python -u tools/verification/qminsweep.py [--budget 600] [--nmax 6]
"""

import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import joint_theta as JT                  # noqa: E402

OUT = os.path.join(_ROOT, 'workspace', 'augmentation_family', 'data', 'qmin_certified.tsv')


def main():
    budget = 600.0
    nmax = 6
    args = sys.argv[1:]
    if '--budget' in args:
        budget = float(args[args.index('--budget') + 1])
    if '--nmax' in args:
        nmax = int(args[args.index('--nmax') + 1])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    new = not os.path.exists(OUT)
    fh = open(OUT, 'a', encoding='utf-8', newline='\n')
    if new:
        fh.write('n\tp\tr\tseed\tq0\tn0\tq_min\torders\tverdicts\ttime\n')
    t_start = time.time()
    done = 0
    stat = {'feasible': 0, 'no_feasible': 0, 'timeout': 0}
    for n in range(5, nmax + 1):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    if time.time() - t_start > budget:
                        print(f'[budget] 已用 {time.time() - t_start:.0f}s，停止')
                        fh.close()
                        return
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    n0 = LQ.rank(O)
                    hi = n0 - p
                    if hi < q0:
                        continue
                    t0 = time.time()
                    orders = []
                    verdicts = []
                    found = None
                    for q in range(q0, hi + 1):
                        v, why, w = JT.decide(A, C, L0, q)
                        orders.append(q)
                        verdicts.append(v)
                        if v == 'FEASIBLE':
                            found = q
                            stat['feasible'] += 1
                            break
                        if time.time() - t0 > 240:
                            stat['timeout'] += 1
                            break
                    if found is None:
                        stat['no_feasible'] += 1
                    qmin = found if found is not None else f'>{hi}'
                    el = round(time.time() - t0, 1)
                    fh.write(f'{n}\t{p}\t{r}\t{seed}\t{q0}\t{n0}\t{qmin}\t{orders}\t{verdicts}\t{el}\n')
                    fh.flush()
                    done += 1
                    print(f'n={n} p={p} r={r} seed={seed}: q0={q0} n0={n0} ⟹ q_min={qmin}'
                          f'（{el}s；{" → ".join(verdicts)}）')
    fh.close()
    print(f'\n完成 {done} 个实例；{stat}；总耗时 {time.time() - t_start:.0f}s')


if __name__ == '__main__':
    main()
