"""c248_kappa_random.py —— 精确随机验证：kappa_obs = codim{ΔR : ΔR N = 0 且 ΔR A N = 0} = r·rank[N, AN]

**被验证的公式（claim，不是本脚本能证明的东西）**
设 A ∈ Q^{n×n}, C ∈ Q^{p×n}, L0 ∈ Q^{r0×n}（rank L0 = r0 = 1），
    K0 = ker[C; CA] ⊂ Q^n,  N ∈ Q^{n×k} 为 K0 的一组基（k = n - rank[C; CA]），
    q ≥ r0 + 1,  r = q - r0 ≥ 1 为"自由行数"，ΔR 遍历 Q^{r×n} 全体。
定义线性映射
        T : Q^{r×n} -> Q^{r×2k},      T(ΔR) = ( ΔR·N , ΔR·A·N ),
于是 ker T = { ΔR : ΔR N = 0 且 ΔR A N = 0 }。有效观测维数定义为该子空间的余维：
        kappa_obs := codim_{Q^{r×n}} ker T = rank(T)。
待验公式：  kappa_obs = r · rank[N, AN]     （等价地 dim ker T = r·n - r·rank[N, AN]）。

**本脚本做的四件事（全部有理/整数精确算术，无浮点、无随机方向采样）**
  1) 生成 n ∈ [4,6], p ∈ [1,2], r0 = 1, r ∈ [1,3]（q = r0 + r）的随机整数实例；
  2) 用 sympy 精确算 [C; CA] 的零空间基 N（不是采样、不是数值 null space），以及 rank[N, AN]；
  3) 把 T **显式**构造为 (r·2k) × (r·n) 有理矩阵——列 = 逐个坐标基 E_ij 的像，按
     "先 ΔR·N 的 r 行、再 ΔR·A·N 的 r 行"的行优先展平；并与 Kronecker 形式 I_r ⊗ [N, AN]^T
     对秩（相差一个行置换）；
  4) 算 rank(T)、dim ker(T)，断言
        rank(T) == r·rank[N, AN]                     （即 kappa_obs 公式）
        dim ker(T) == r·n - r·rank[N, AN]            （余维的补）
        dim ker(T) == r·(n - rank[N, AN])            （逐行独立的等价说法）
     并把 ker(T) 的**每一根基**代回：ΔR N = 0、ΔR A N = 0（集合相等的实算方向）；
     另外构造"真点/假点"（§10.2 地基检查）：非零的 ΔR ∈ ker T 存在、以及某个 ΔR 使 T(ΔR) ≠ 0。

**等级**：`[精确验证]`，覆盖 50 个随机小实例（n ≤ 6, p ≤ 2, r ≤ 3）；**验证 ≠ 证明**。
本脚本不覆盖：k > 2n 的一般性、大 n、以及"K0 基的选取无关性"以外的任何结构断言。

**自检（§7.21：证书必须能在坏输入上打挂）**——见 mutation_report()：
  M1 丢掉 A·N 块（把 AN 置零）后 rank 变成 r·rank(N)，在有 rank N < rank[N,AN] 的实例时断言必挂；
  M2 把余维误当维数（kappa 写成 dim ker）时，在 rank T ≠ r·n - rank T 的实例时断言必挂；
  M3 把自由行数写成 r+1 时断言必挂（只要 rank[N,AN] > 0）。
  三者都必须至少命中一个实例，否则脚本报 FAIL（说明这组测试分辨不出对错）。

用法：
    python -u tools/verification/c248_kappa_random.py            # 默认 50 例，seed 20261109
    python -u tools/verification/c248_kappa_random.py --seed 7 --cases 100
"""

import argparse
import random
import sys

import sympy as sp


# ----------------------------------------------------------------------------- 工具
def vec_row(X):
    """行优先展平（第一个下标变得最慢）——与 build_T 的列顺序约定一致。"""
    return sp.Matrix([X[i, j] for i in range(X.rows) for j in range(X.cols)])


def flatten_blocks(dRN, dRAN):
    """把 (ΔR N, ΔR A N) 按 T 的约定展平：先 ΔR N 的 r 行，再 ΔR A N 的 r 行。"""
    assert dRN.shape == dRAN.shape
    r, k = dRN.rows, dRN.cols
    return sp.Matrix([dRN[i, j] for i in range(r) for j in range(k)] +
                     [dRAN[i, j] for i in range(r) for j in range(k)])


def zeros_if(rows, cols):
    return sp.zeros(rows, cols)


def build_T(r, n, N, AN):
    """显式构造 T 的矩阵（(2rk) × (rn)），用坐标基逐个求像。

    列坐标 (i, j)  <<->>  ΔR = E_{ij}（r×n 单位阵元）。
    输出坐标：前 r·k 个 = ΔR·N 的行优先展平，后 r·k 个 = ΔR·A·N 的行优先展平。
    """
    assert N.rows == n and AN.rows == n
    assert N.cols == AN.cols
    k = N.cols
    T = sp.zeros(2 * r * k, r * n)
    for i in range(r):
        for j in range(n):
            E = sp.zeros(r, n)
            E[i, j] = 1
            assert E.cols == N.rows, 'dimension mismatch before E*N'
            img = flatten_blocks(E * N, E * AN)      # 长度 2rk
            assert img.shape == (2 * r * k, 1)
            for a in range(2 * r * k):
                T[a, i * n + j] = img[a, 0]
    return T


def gen_instance(rng, nmin=4, nmax=6):
    """生成一个随机整数实例（A, C, L0, q）；不保证任何一般位置，允许退化（k=0 等）。"""
    n = rng.randint(nmin, nmax)
    p = rng.randint(1, min(2, n - 1))
    r0 = 1
    r = rng.randint(1, min(3, n - r0))          # q = r0 + r <= n，r >= 1
    q = r0 + r

    def rand_mat(rows, cols):
        return sp.Matrix(rows, cols, [rng.randint(-1, 1) for _ in range(rows * cols)])

    A = rand_mat(n, n)
    C = rand_mat(p, n)
    for _ in range(200):
        L0 = rand_mat(r0, n)
        if L0.rank() == r0:
            break
    else:
        raise RuntimeError('cannot draw full-row-rank L0')
    return {'n': n, 'p': p, 'r0': r0, 'r': r, 'q': q, 'A': A, 'C': C, 'L0': L0}


# ----------------------------------------------------------------------------- 核心
def analyze(inst, detail=False):
    """算全部不变量；(detail=True 时打印)。返回结果 dict（已含全部断言）。"""
    A, C, L0 = inst['A'], inst['C'], inst['L0']
    n, p, r0, r, q = inst['n'], inst['p'], inst['r0'], inst['r'], inst['q']

    # ---- 0. 类型/维数不变量：先断言，再做任何乘法（§7.14）----
    assert A.shape == (n, n), f'A.shape={A.shape}, want {(n, n)}'
    assert C.shape == (p, n), f'C.shape={C.shape}, want {(p, n)}'
    assert L0.shape == (r0, n), f'L0.shape={L0.shape}, want {(r0, n)}'
    assert q == r0 + r and r >= 1, (q, r0, r)
    assert A.is_Matrix and all(x.is_rational for x in A)      # 数据类型：整数/有理数
    assert all(x.is_rational for x in C) and all(x.is_rational for x in L0)

    rkL0 = L0.rank()
    assert rkL0 == r0, f'rank(L0)={rkL0} != r0={r0}'
    assert r == q - rkL0, 'r != q - rank(L0)（定义式）'

    # ---- 1. K0 = ker[C; CA]，精确零空间基 N ----
    assert C.rows == p and C.cols == A.rows
    S = sp.Matrix.vstack(C, C * A)
    assert S.shape == (2 * p, n), f'stack[C;CA].shape={S.shape}'
    rho = S.rank()
    k = n - rho
    ker_basis = S.nullspace()
    assert len(ker_basis) == k, f'dim ker[C;CA]={len(ker_basis)} != n-rank={k}'
    N = sp.Matrix.hstack(*ker_basis) if k else sp.zeros(n, 0)
    assert N.shape == (n, k), f'N.shape={N.shape}'
    assert N.rank() == k, f'rank(N)={N.rank()} != k={k}（N 必须是基）'
    # N 真的落在 K0 里
    assert C * N == sp.zeros(p, k), 'C N != 0'
    assert (C * A) * N == sp.zeros(p, k), 'C A N != 0'

    # ---- 2. M = [N, AN]，rank[N, AN] ----
    assert A.cols == N.rows
    AN = A * N
    assert AN.shape == (n, k)
    M = sp.Matrix.hstack(N, AN) if k else sp.zeros(n, 0)
    assert M.shape == (n, 2 * k), f'M.shape={M.shape}'
    rank_M = M.rank()
    assert rank_M <= min(n, 2 * k)

    # ---- 3. 显式构造 T 与其秩 ----
    dim_amb = r * n            # dim Q^{r×n}
    dim_tgt = r * 2 * k        # dim Q^{r×2k}
    T = build_T(r, n, N, AN)
    assert T.shape == (dim_tgt, dim_amb), f'T.shape={T.shape}, want {(dim_tgt, dim_amb)}'
    rank_T = T.rank()

    # Kronecker 交叉核对：T 与 I_r ⊗ [N, AN]^T 只差行置换，秩必须相同
    T_kron = sp.kronecker_product(sp.eye(r), M.T) if k else sp.zeros(0, dim_amb)
    assert T_kron.shape == (dim_tgt, dim_amb)
    assert rank_T == T_kron.rank(), 'explicit T and Kronecker form disagree on rank'

    # ---- 4. 断言公式：kappa_obs = r·rank[N,AN]，dim ker = r·n - r·rank[N,AN] ----
    kappa_obs = rank_T                      # 定义：余维 = rank(T)
    ker_dim = dim_amb - rank_T
    assert rank_T == r * rank_M, (
        f'kappa_obs={rank_T} != r*rank[N,AN]={r}*{rank_M}')
    assert ker_dim == dim_amb - r * rank_M, (
        f'dim ker={ker_dim} != r*n - r*rank[N,AN]={dim_amb - r * rank_M}')
    assert ker_dim == r * (n - rank_M), 'row-wise count disagrees'

    # ---- 5. 实算方向：ker(T) 的每根基都满足两条约束；再验真点/假点 ----
    nullvecs = T.nullspace()
    assert len(nullvecs) == ker_dim, f'nullspace dim={len(nullvecs)} != {ker_dim}'
    for v in nullvecs:
        assert v.shape == (dim_amb, 1)
        dR = sp.Matrix(r, n, list(v))
        assert dR * N == sp.zeros(r, k), 'ker(T) element violates ΔR N = 0'
        assert dR * A * N == sp.zeros(r, k), 'ker(T) element violates ΔR A N = 0'

    # 编码一致性：随机 ΔR 上 T·vec(ΔR) 必须等于 flatten(ΔR N, ΔR A N)
    vrng = random.Random(hash((n, p, r, rho)) & 0xFFFF)
    grounded = {'true_point': None, 'false_point': None}
    for _ in range(5):
        dR = sp.Matrix(r, n, [vrng.randint(-2, 2) for _ in range(r * n)])
        lhs = T * vec_row(dR)
        rhs = flatten_blocks(dR * N, dR * AN)
        assert lhs == rhs, 'T is not the map ΔR -> (ΔR N, ΔR A N)'

    # 真点：若 rank[N,AN] < n，左侧零空间里取非零 v，dR = e_1 v^T 必在 ker T
    if rank_M < n:
        lnull = M.T.nullspace()
        assert len(lnull) == n - rank_M
        v = lnull[0]
        assert v.shape == (n, 1) and v.T * M == sp.zeros(1, 2 * k)
        dR = sp.zeros(r, n)
        for j in range(n):
            dR[0, j] = v[j]
        assert dR != sp.zeros(r, n)
        assert T * vec_row(dR) == sp.zeros(dim_tgt, 1)
        grounded['true_point'] = 'v^T in left-null([N,AN])'

    # 假点：rank[N,AN] > 0 时存在 ΔR 使 T(ΔR) != 0
    if rank_M > 0:
        ai, bj = next((i, j) for i in range(n) for j in range(2 * k) if M[i, j] != 0)
        dR = sp.zeros(r, n)
        dR[0, ai] = 1
        assert T * vec_row(dR) != sp.zeros(dim_tgt, 1)
        grounded['false_point'] = f'e_{ai} in row 0'

    res = {
        'n': n, 'p': p, 'r0': r0, 'r': r, 'q': q,
        'rank_C': C.rank(), 'rank_L0': rkL0, 'rho': rho, 'k': k,
        'rank_N': N.rank(), 'rank_NAN': rank_M,
        'dim_amb': dim_amb, 'dim_tgt': dim_tgt,
        'rank_T': rank_T, 'kappa_obs': kappa_obs, 'ker_dim': ker_dim,
        'grounded': grounded, 'T': T, 'M': M, 'N': N, 'AN': AN,
    }

    if detail:
        print(f'  --- 不变量（先打印，后下结论）---')
        print(f'    n={n} p={p} r0={r0} q={q} r=q-r0={r}')
        print(f'    rank[C;CA]={rho}   k=dim K0=n-rank={k}   rank(N)={N.rank()}')
        print(f'    rank[N,AN]={rank_M}   (M is {n}x{2 * k})')
        print(f'    dim Q^(r x n)={dim_amb}   dim Q^(r x 2k)={dim_tgt}')
        print(f'    rank(T)={rank_T}   dim ker(T)={ker_dim}   r*rank[N,AN]={r * rank_M}')
        print(f'    grounded: {grounded}')
    return res


# ----------------------------------------------------------------------------- 负对照
def mutation_report(results, rng):
    """§7.21：证明这些断言能在坏输入上打挂。

    M1 丢掉 A·N 块  -> 若某实例 rank N < rank[N,AN]，则 kappa 变成 r·rank N != r·rank[N,AN]；
    M2 余维/维数混淆 -> 若某实例 rank_T != rn - rank_T，则"kappa = dim ker"必挂；
    M3 自由行数写错  -> 若某实例 rank[N,AN] > 0，则 (r+1)·rank[N,AN] != r·rank[N,AN]。
    返回各 mutation 命中的实例数，调用方断言 > 0。
    """
    hits = {'M1_missing_AN': 0, 'M2_codim_as_dim': 0, 'M3_wrong_r': 0}
    for res in results:
        r, n, k = res['r'], res['n'], res['rank_NAN']
        N, AN = res['N'], res['AN']
        if k > 0 and res['rank_N'] < k:
            hits['M1_missing_AN'] += 1
            T1 = build_T(r, n, N, sp.zeros(N.rows, N.cols))
            assert T1.rank() == r * res['rank_N']
            assert T1.rank() != r * k, 'M1 mutation did not change the answer'
        if k > 0 and res['rank_T'] != res['dim_amb'] - res['rank_T']:
            hits['M2_codim_as_dim'] += 1
            assert res['dim_amb'] - res['rank_T'] != r * k
        if k > 0:
            hits['M3_wrong_r'] += 1
            assert (r + 1) * k != r * k
    return hits


# ----------------------------------------------------------------------------- 主程序
def main(argv=None):
    ap = argparse.ArgumentParser(description='exact random check of kappa_obs = r*rank[N,AN]')
    ap.add_argument('--seed', type=int, default=20261109)
    ap.add_argument('--cases', type=int, default=50)
    ap.add_argument('--nmin', type=int, default=4)
    ap.add_argument('--nmax', type=int, default=6)
    ap.add_argument('--quiet', action='store_true')
    a = ap.parse_args(argv)

    rng = random.Random(a.seed)
    print('=' * 96)
    print('c248  exact random verification:  kappa_obs = codim{ΔR : ΔR N = 0, ΔR A N = 0} = r*rank[N, AN]')
    print(f'      seed={a.seed}  cases={a.cases}  n in [{a.nmin},{a.nmax}]  p in [1,2]  r0=1  r in [1,3]')
    print('      field = Q (exact, sympy Rational/integer);  only K0 is computed by nullspace, everything else')
    print('      (T, rank(T), dim ker(T), the two constraint products) is checked by explicit multiplication.')
    print('=' * 96)

    results = []
    detail_budget = {'first': 3, 'big_k': 1, 'load_bearing': 1}

    for case in range(a.cases):
        inst = gen_instance(rng, a.nmin, a.nmax)
        want_detail = case < detail_budget['first']
        res = analyze(inst, detail=False)
        # 选若干"有信息量"的实例额外详印
        if (not want_detail and detail_budget['big_k'] > 0
                and res['k'] >= 2 and res['rank_NAN'] > res['rank_N']):
            want_detail = True
            detail_budget['big_k'] -= 1
        if want_detail and case >= detail_budget['first']:
            print(f'\n[case {case}] extra detail')
            analyze(inst, detail=True)
        elif want_detail:
            print(f'\n[case {case}]')
            analyze(inst, detail=True)

        results.append(res)
        if not a.quiet:
            print(f"  [case {case:2d}] n={res['n']} p={res['p']} r0={res['r0']} q={res['q']} r={res['r']} "
                  f"k={res['k']} rankN={res['rank_N']} rank[N,AN]={res['rank_NAN']} | "
                  f"rn={res['dim_amb']} 2rk={res['dim_tgt']} rankT={res['rank_T']} ker={res['ker_dim']} | "
                  f"kappa={res['kappa_obs']}  OK")

    # ---- 汇总 ----
    ncases = len(results)
    stats = {
        'k0': sum(1 for x in results if x['k'] == 0),
        'k_ge2': sum(1 for x in results if x['k'] >= 2),
        'load_bearing': sum(1 for x in results if x['rank_NAN'] > x['rank_N']),
        'injective': sum(1 for x in results if x['rank_T'] == x['dim_amb']),
        'codim_ne_dim': sum(1 for x in results if x['rank_T'] != x['dim_amb'] - x['rank_T']),
        'r_dist': {rr: sum(1 for x in results if x['r'] == rr) for rr in (1, 2, 3)},
        'n_dist': {nn: sum(1 for x in results if x['n'] == nn) for nn in range(a.nmin, a.nmax + 1)},
        'p_dist': {pp: sum(1 for x in results if x['p'] == pp) for pp in (1, 2)},
        'true_points': sum(1 for x in results if x['grounded']['true_point']),
        'false_points': sum(1 for x in results if x['grounded']['false_point']),
    }
    print('\n' + '-' * 96)
    print('summary')
    print(f'  cases                 : {ncases}')
    print(f'  k = dim K0 = 0        : {stats["k0"]}    (退化实例，N 为 n×0，T 为 0 行矩阵)')
    print(f'  k >= 2               : {stats["k_ge2"]}')
    print(f'  rank N < rank[N,AN]  : {stats["load_bearing"]}    (A·N 块真的加秩，公式不是 rank(N) 的伪装)')
    print(f'  T injective          : {stats["injective"]}    (kappa = r*n)')
    print(f'  kappa != dim ker     : {stats["codim_ne_dim"]}    (余维 ≠ 维数，断言可分辨)')
    print(f'  n distribution        : {stats["n_dist"]}')
    print(f'  p distribution        : {stats["p_dist"]}')
    print(f'  r distribution        : {stats["r_dist"]}')
    print(f'  grounded true points  : {stats["true_points"]}    (非零 ΔR ∈ ker T 的显式构造)')
    print(f'  grounded false points : {stats["false_points"]}    (T(ΔR) != 0 的显式构造)')

    hits = mutation_report(results, rng)
    print('\nnegative controls (assertions must be able to fail on wrong formulas):')
    print(f'  M1 drop A·N block   -> kappa becomes r*rank(N): {hits["M1_missing_AN"]} case(s) catch it')
    print(f'  M2 codim as dim ker -> kappa becomes dim ker  : {hits["M2_codim_as_dim"]} case(s) catch it')
    print(f'  M3 write r+1        -> kappa becomes (r+1)*rk  : {hits["M3_wrong_r"]} case(s) catch it')
    assert hits['M1_missing_AN'] > 0, 'M1 never fires: the test cannot distinguish rank(N) from rank[N,AN]'
    assert hits['M2_codim_as_dim'] > 0, 'M2 never fires: the test cannot distinguish codim from dim'
    assert hits['M3_wrong_r'] > 0, 'M3 never fires: the test cannot distinguish r from r+1'
    assert stats['load_bearing'] > 0, 'no instance has rank(N) < rank[N,AN]: A slot is never exercised'
    assert stats['true_points'] > 0, 'no grounded true point'
    assert stats['false_points'] > 0, 'no grounded false point'

    print('-' * 96)
    print(f'PASS: {ncases}/{ncases} cases — for every instance')
    print('        rank(T) = kappa_obs = r*rank[N,AN]  and  dim ker T = r*n - r*rank[N,AN],')
    print('      with ker(T) = {ΔR : ΔR N = 0 and ΔR A N = 0} verified by explicit multiplication.')
    print('      [exact verification 50/50] — NOT a proof; only n<=6, p<=2, r<=3, random integer data.')
    print('-' * 96)
    return 0


if __name__ == '__main__':
    sys.exit(main())
