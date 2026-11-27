"""
核实 Lemma 4（(S) 的开集性）的严格论证所需的代数事实。

Lemma 4 的要点：
  (5b) ⟺ rank P_L(s) ≡ rank H_L ,  P_L(s) = (sL − LA)N_{CA},  H_L = L N_{CA}
  且 rank P_L(s) ≤ rank H_L 恒成立
  ⟹ (5b) ⟺ "存在某个 h 阶子式不恒为零"（h = rank H_L）⟹ Zariski-开。

本脚本核实两个支撑事实：
  (F1) rank P_L(s) ≤ rank H_L 对所有 s 成立
  (F2) (5b) 与 "存在 h 阶子式不恒零" 等价（即两者真值一致）
"""
import numpy as np

TOL = 1e-7
rng = np.random.default_rng(777001)


def rk(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return 0 if s.size == 0 else int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def st(*b):
    b = [np.atleast_2d(np.asarray(x, float)) for x in b]
    nc = max((x.shape[1] for x in b), default=0)
    b = [x for x in b if x.shape[0] > 0]
    return np.zeros((0, nc)) if not b else np.vstack(b)


def nullspace_basis(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.shape[0] == 0:
        return np.eye(M.shape[1])
    u, s, vt = np.linalg.svd(M)
    r = int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))
    return vt[r:].T


f1_bad = f2_bad = 0
tested = 0
for _ in range(400):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if rk(C) < p or rk(L) < q:
        continue
    tested += 1

    NCA = nullspace_basis(st(C, C @ A))
    H = L @ NCA
    h = rk(H)

    # (F1) rank P(s) <= rank H 对所有 s
    pts = [complex(x) for x in (-5., -2., -1., -.5, 0., .5, 1., 2., 5.)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(15)]
    ok_f1 = True
    for s in pts:
        P = (s * L - L @ A) @ NCA
        if rk(P.real) > h:
            ok_f1 = False
            break
    if not ok_f1:
        f1_bad += 1

    # (F2) (5b) 真值 == "存在 h 阶子式不恒零"
    # (5b)：rank[sL-LA; CA; C] == rank[L; CA; C] 对所有 s
    rhs = rk(st(L, C @ A, C))
    cond_5b = all(rk(st((s * L - L @ A).real, C @ A, C)) == rhs for s in pts)
    # "存在 h 阶子式不恒零" ⟺ rank P(s) 不恒 < h ⟺ max_s rank P(s) == h
    max_rank_P = max(rk(((s * L - L @ A) @ NCA).real) for s in pts)
    cond_open = (max_rank_P == h)
    if cond_5b != cond_open:
        f2_bad += 1
        if f2_bad <= 2:
            print(f"  (F2) 不一致: (5b)={cond_5b}  子式判据={cond_open}  h={h} maxrankP={max_rank_P}")

print(f"测试实例 {tested}")
print(f"  (F1) rank P(s) ≤ rank H 失败次数        : {f1_bad}")
print(f"  (F2) '(5b)' 与 '子式不恒零' 不一致次数   : {f2_bad}")
print()
print("  若两者均为 0，则 Lemma 4 的两个支撑事实成立。")
