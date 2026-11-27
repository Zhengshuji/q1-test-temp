r"""Theorem F（实现定理）的数值验证：规范坐标 $C=[I_p\mid0]$ 下显式构造 $A$。

设 $W=\ker C$（坐标 $e_{p+1},\dots,e_n$）、$V\subseteq W$、$Z\subseteq W$、$\bar A=0$（取最简情形）。
构造：$\beta:W\to\mathbb R^p$ 以 $V$ 为核；$\gamma:W\to W$ 满足 $\gamma(V)\subseteq Z$；$A|_W=(\beta,\gamma)$，$A$ 在前 $p$ 列任意。

验证：$V=\ker[C;CA]$、诱导映射 $=0$（即 $AV\subseteq Z$）、$(A)$ 成立。

用法：python proof/layer_program/c245_realization_verify.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def main():
    rng = random.Random(7)
    passed = 0
    trials = 6
    for trial in range(trials):
        n, p = 6, 2
        C = [[Fr(1) if j == i else Fr(0) for j in range(n)] for i in range(p)]
        # W = ker C = span(e_3..e_6)：用「W 坐标」(长度 n-p) 表示
        m = n - p
        def from_Wcoords(c):
            return [Fr(0)] * p + list(c)
        # V：W 中 dim m-1 的子空间（codim_W V = 1 ≤ p）
        vdim = m - 1
        Vrows = [[Fr(rng.randint(-2, 2)) for _ in range(m)] for _ in range(vdim)]
        Vb = [from_Wcoords(r) for r in Vrows]
        if AI.rank(Vb) < vdim:
            continue
        # β：核为 V 的 p×m 矩阵（rank 1）
        # 找 w4 使 V + span(w4) = W
        w4 = None
        for _ in range(200):
            cand = [Fr(rng.randint(-2, 2)) for _ in range(m)]
            if AI.rank(Vrows + [cand]) > vdim:
                w4 = cand
                break
        if w4 is None:
            continue
        beta = [[Fr(0)] * m for _ in range(p)]
        beta[0][:] = w4            # β(w4) = e1；β 在 V 上为 0（因为 V 的向量与 w4 的坐标关系）
        # 更准确：β 用「在基 V + w4 下的坐标」定义；直接用 w4 的对偶泛函
        # 求对偶泛函 φ 使 φ(V)=0、φ(w4)=1：解线性系统
        # 用 rref 求 [Vrows; w4] 的逆——这里简化：取 φ = 最后一个基向量在 [Vrows;w4] 逆矩阵中的行
        A0 = Vrows + [w4]
        R, piv = AI.rref([row[:] for row in A0])
        # A0 可逆 ⟹ rref = I；φ = e_{m-1} · A0^{-1} 的第 vdim 行
        # 求 A0^{-1}：对 A0 做列变换不便；改用 solve：φ(x) 使 φ(A0_i) = δ_{i,vdim}
        # 解 A0^T φ^T = e_vdim
        aug = [A0[i][:] + [Fr(1) if i == vdim else Fr(0)] for i in range(m)]
        R2, piv2 = AI.rref(aug)
        phi = [Fr(0)] * m
        for row in R2:
            pp = next((t for t in range(m + 1) if row[t] != 0), None)
            if pp is None or pp == m:
                continue
            phi[pp] = row[m]
        beta = [[Fr(0)] * m for _ in range(p)]
        beta[0] = phi
        # Z：W 中 dim d 的子空间
        d = rng.randint(1, m - 1)
        Zrows = [[Fr(rng.randint(-2, 2)) for _ in range(m)] for _ in range(d)]
        if AI.rank(Zrows) < d:
            continue
        Zb = [from_Wcoords(r) for r in Zrows]
        Zm = [[Zb[k][i] for k in range(len(Zb))] for i in range(n)]
        # γ：W→W，像 ⊆ Z（这样 γ(V) ⊆ Z 自动成立）
        gamma_rows = []          # 每个是 m 维行向量（W 坐标）
        for _ in range(m):
            coeff = [Fr(rng.randint(-2, 2)) for _ in range(d)]
            r = [sum(coeff[k] * Zrows[k][j] for k in range(d)) for j in range(m)]
            gamma_rows.append(r)
        # A|_W：把 W 的基向量 e_{p+i} 送到 (β(e_i), γ(e_i))
        # 注意 β 用 W 坐标：β(e_i) = beta[:,i]
        A = [[Fr(0)] * n for _ in range(n)]
        for i in range(m):
            col = p + i
            for r in range(p):
                A[r][col] = beta[r][i]
            g = gamma_rows[i]
            for r in range(m):
                A[p + r][col] = g[r]
        # 前 p 列任意取 0
        CA = AI.mul(C, A)
        Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
        Vc = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
        # 检查 span(Vb) == span(Vc)
        Vm = [[Vb[k][i] for k in range(len(Vb))] for i in range(n)]
        same = (AI.rank([list(Vm[i]) + list(Vc[i]) for i in range(n)]) == vdim == len(Vv))
        # 诱导映射：A V ⊆ Z ?
        AV = SG.apply_col(A, Vm)
        ind = (AI.rank([list(Zm[i]) + list(AV[i]) for i in range(n)]) == d)
        # (A)：rank[Z, AZR] = d
        CAZ = AI.mul(CA, Zm)
        Rv = AI.nullspace(CAZ)
        Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
        AZ = SG.apply_col(A, Zm)
        AZR = AI.mul(AZ, Rm)
        M1 = [list(Zm[i]) + list(AZR[i]) for i in range(n)]
        okA = AI.rank(M1) == d
        print(f'trial {trial}: n={n}, p={p}, dim V={len(Vv)}（应 {vdim}）⟹ ker 相同={same}；'
              f'AV⊆Z={ind}；(A)={okA}')
        if same and ind and okA:
            passed += 1
    print(f'\n通过 {passed}/{trials}')


if __name__ == '__main__':
    main()
