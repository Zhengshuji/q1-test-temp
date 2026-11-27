"""QA8 第 2 项：判据的行/列约定 + 基无关性验证（30/30）。

约定：T 按列作用；w 是行；判据 covered <=> ∃λ: rank[[λI−T],[w]] < ρ。
换基：T' = P T P^{-1}，w' = w P^{-1}  => 结果不变（本脚本验证）。
对照：错误地取 w' = P w 只有 26/30（RCP §79）。
"""
import itertools, random, sys
from fractions import Fraction as Fr
sys.path.insert(0,'tools/exact_linalg')
import audit_independent as AI
import importlib.util as iu
spec = iu.spec_from_file_location('C2','proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = iu.module_from_spec(spec); spec.loader.exec_module(CV)
mm, rank = CV.mm, CV.rank

def good_cell(T, w, rho):
    """铅笔 [[λI−T],[w]] 的最大子式 gcd 恒为 1 => 好格子（不被覆盖）。"""
    rows = [[[-T[i][k], Fr(1) if i==k else Fr(0)] for k in range(rho)] for i in range(rho)]
    rows.append([[w[k]] for k in range(rho)])
    polys = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(rho), rho):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = CV.V.det_poly(M)
            if not (len(v)==1 and v[0]==0): polys.append(v)
    if not polys: return False
    g = polys[0]
    for q in polys[1:]: g = CV.V.pgcd(g, q)
    return (len(g)==1 and g[0]!=0)

rng = random.Random(24680)
agree = tot = 0
for trial in range(30):
    T = [[Fr(rng.randint(-2,2)) for _ in range(3)] for _ in range(3)]
    w = [Fr(rng.randint(-2,2)) for _ in range(3)]
    if not any(w): continue
    base = good_cell(T, w, 3)
    while True:
        P = [[Fr(rng.randint(-2,2)) for _ in range(3)] for _ in range(3)]
        if rank(P) == 3: break
    Pinv = AI.inv(P)
    Tp = mm(mm(P, T), Pinv)
    wp = mm([w], Pinv)[0]
    after = good_cell(Tp, wp, 3)
    tot += 1
    if base == after: agree += 1
print(f"正确行变换 w' = w P^-1：{agree}/{tot} 一致")
