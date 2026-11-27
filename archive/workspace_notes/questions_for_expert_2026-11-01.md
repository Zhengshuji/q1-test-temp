# 待专家确认的纸面证明清单（2026-11-01）

> **用途**：下面这些命题的**纸面证明已经完成**，但 Lean 形式化还差一段（或成本过高）。
> 我们不再替它们做 Lean，而是把"纸面论证"原样登记，**统一请专家确认论证是否足够**。
> 每条的"要问的问题"写在最后一行——专家只需回答那一条。
>
> 与 [docs/02](../../docs/02_theorems_proven.md) 的等级标注一致：这些在 docs 里是 `[已证]` 或 `[已证] + [Lean 内核]`。

---

## 1. B.2（顶层可观测性，$\rho=d$）

- **陈述**：$\rho=d$ 时 $(5b)\iff(D_W^{\mathsf T},T_W)$ 可观测。
- **纸面证明**：[proof/top_layer_observability/theorem.md](../../proof/top_layer_observability/theorem.md)
  （引理 1.1 分块恒等式 + 定理 2.1 双向 + PBH）。
- **Lean 到哪**：分块恒等式的**逐点版**（`B2Block.block_on_J / block_on_W`）✅；PBH ✅（`PBH.pbh_iff`）。
  **缺**：把逐点分块组装成矩阵并接"秩恒为 $d$"（纯建模，非数学）。
- **要问的问题**：定理 2.1 的论证（尤其"$\operatorname{rank}Q_{\mathcal V}(\lambda)=d\ \forall\lambda\iff$ 无 $\ker D_W$ 里的特征向量"
  这一步用 PBH）**是否足够严格**？有没有需要补的边角（例如 $d=0$ 或 $c=0$ 的退化情形）？

---

## 2. K.1（$m=3$：每个非零双向量可分解）

- **陈述**：$\dim V=3$ 时每个 $0\ne w\in\Lambda^2V$ 都可写成 $u\wedge v$（即 $\mathrm{Gr}(2,3)=\mathbb P(\Lambda^2\mathbb C^3)$）。
- **纸面证明**：[proof/bivector_r2/README.md](../../proof/bivector_r2/README.md) §2；
  论证是"$\dim\Lambda^2V=3$ 且 $w\wedge w=0$（因 $\Lambda^4V=0$），而 $w\wedge w=0\iff w$ 可分解"。
- **Lean 到哪**：**没有**（需要外代数与 $\wedge^4$；Mathlib 有 `ExteriorAlgebra`，但"$w\wedge w=0\iff$ 可分解"未现成）。
- **要问的问题**：用"$w\wedge w=0\iff$ 可分解"作为 K.1 的证明**是否标准可接受**？
  还是专家建议直接写"$\mathbb P(\Lambda^2\mathbb C^3)$ 与 $\mathrm{Gr}(2,3)$ 都是 $\mathbb P^2$，且后者被前者包含"？
  （后者更短，但需要 Grassmannian 的维数事实。）

---

## 3. K.3（$\ell\ge N-(2m-4)$ 时必有可分解元）

- **陈述**：$\ell\ge N-(2m-4)$ 时 $K\le\Lambda^2\mathbb C^m$ 必含可分解元。
- **纸面证明**：[proof/bivector_r2/README.md](../../proof/bivector_r2/README.md) §3（维数计数：
  $\mathbb P(K)$ 的维数是 $\ell-1$，而 $\mathrm{Gr}(2,m)$ 的维数是 $2m-4$，故相交非空）。
- **Lean 到哪**：**没有**（需要 Grassmannian 的维数定理 $\dim\mathrm{Gr}(2,m)=2(m-2)$，Mathlib 无）。
- **要问的问题**：这个维数计数论证**是否足够**？（"两个射影簇维数之和 $\ge$ 环境维数 $\Rightarrow$ 相交"需要代数闭域上的
  射影维数定理；我们的场合是 $\mathbb P(\Lambda^2\mathbb C^m)$，是否可以直接引用？）

---

## 4. D.1（$P$ 的下界）

- **陈述**：$P(A,B,S)\ge\dim S+\dim\frac{AS+S+B}{S+B}$。
- **纸面证明**：[proof/p_is_polynomial/theorem.md](../../proof/p_is_polynomial/theorem.md)（
  $AW\subseteq W+B\Rightarrow AS+M\subseteq W+M$，再取商维数）。
- **Lean 到哪**：**已完整**（`D1Core.P` 定义 + `d1_P_lower_bound` 陈述；逐 $W$ 版 `d1_lower_bound`）。
  只剩"可行集非空"这一建模条件。
- **要问的问题**：$P$ 的定义（对 $U$ 取 min 的那一层）在文献里与 $q_0$ 的关系**是否如我们所写**？
  （我们的 $P$ 是"$\rho_{ci}$ 侧"的，$q_0$ 是"$(A)$ 侧"的；P1/P2 里两者的关系是否有更精确的表述？）

---

## 5. J（行列式因子判据）

- **陈述**：$(5b)\iff[U\mid P(\lambda)]$ 的全部 $(r+t)$-阶子式的 $\gcd$ 为常数。
- **纸面证明**：[docs/02](../../docs/02_theorems_proven.md) §J + [tools/verification/poly_smith.py](../../tools/verification/poly_smith.py) 的 Smith 形实现。
- **Lean 到哪**：**没有**（需要 $\mathbb Q[\lambda]$ 上的 gcd/Smith 形与"秩 $=\rho\ \forall\lambda\iff$ 子式 gcd 为常数"的桥）。
- **要问的问题**：这个判据的**多项式环版本**（在 $\mathbb C[\lambda]$ 上）是否是标准结果？
  我们只需要"$\gcd\ne1$ 的那组子式有公根 $\iff\exists\lambda$ 秩降"，是否可以用 Hilbert 零点定理直接说？

---

## 6. 其他（已登记但未 Lean 的次要项）

| 命题 | 纸面位置 | 状态 |
|---|---|---|
| E.1（$\rho_{ci}=P$）| [proof/p_is_polynomial/reduction.md](../../proof/p_is_polynomial/reduction.md) | 依赖 D.1/D.2/D.3 的接口 |
| F.2（$\min_\lambda r<\rho_{ci}\Rightarrow$ 无解）| [proof/rank_barrier/README.md](../../proof/rank_barrier/README.md) | 由 E.1 + F.1 算术 |
| H.2 | [proof/h2_dim_arithmetic/](../../proof/h2_dim_arithmetic/README.md) | **已 Lean** ✓ |
| A.4（$q_0$ 下界）| 文献 P1/P2 | 引用，不是本项目定理 |

---

## 7. 一句话汇总

> 上面 1–5 条的**数学**都已证完（纸面），Lean 缺口集中在三类：
> **(i)** 矩阵/坐标建模（B.2、J）；**(ii)** 外代数与 Grassmannian 维数（K.1、K.3）；
> **(iii)** $\min$ 定义的接口（D.1）。
> 需要专家确认的是：这些**纸面论证本身**是否足够严格，而不是 Lean 的问题。

---

## 8. 附：D.1 / J / K.1 / K.3 的 Lean 可行性评估（本轮新增）

| 命题 | Mathlib 现状 | 需要新建的 | 估计 |
|---|---|---|---|
| **D.1** | 子空间 API 齐全 | 只需包含关系（已 Lean：`D1Core.d1_core`/`d1_dim`）+ $P$ 的 $\min$ 接口 | 小（接口是建模决策）|
| **J** | 无"子式/极小秩" API（`Matrix.det` 有，但"秩 $=k\iff$ 某 $k$-子式 $\ne0$"没有）| 子式定义 + 秩-子式桥 + $\mathbb C[\lambda]$ 上的 gcd | 大 |
| **K.1** | `ExteriorAlgebra` 有 $\iota$、`ιMulti`；**无**"可分解"与"$w\wedge w=0$"判据 | 可分解定义 + $\Lambda^2$ 维数 + $w\wedge w=0\iff$ 可分解 | 大 |
| **K.3** | 无 Grassmannian 维数定理 | $\dim\mathrm{Gr}(2,m)=2m-4$ + 射影相交维数定理 | 很大 |

**结论**：D.1 的核心已 Lean（剩余是 $P$ 的接口）；J/K.1/K.3 各是一块独立的基础设施，
建议先请专家确认纸面论证（本文件 §1–§5），再决定是否投入。
