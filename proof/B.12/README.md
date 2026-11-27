# B.12 · 谱条件的可观性归约

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.12` 条目（§0.1 归并表）。

## 命题

**B.12（谱条件的可观性归约；专家 2026-11-04 §3 给出，本项目独立核验）** 设 $(5a)$ 成立，取
$$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA\qquad(\Lambda\in\mathbb C^{q\times q}),$$
令 $V=\ker[C;CA]$、$U:=\mathcal L(V)\subseteq\mathbb C^q$。则
$$(5b)\iff U\ \text{不含}\ \Lambda\ \text{的非零特征向量}
\iff (E,\Lambda)\ \text{可观测}\ (\ker E=U)
\iff \operatorname{rank}\bigl[E;E\Lambda;\dots;E\Lambda^{q-1}\bigr]=q .$$

## 纸面证明

*证明*（逐步）：
1. $Q_{\mathcal L}(\lambda)=D(\lambda)H$，其中 $H=[\mathcal L;CA;C]$、
   $D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix}$
   （第一块：$(\lambda I-\Lambda)\mathcal L-G_1CA-G_0C=\lambda\mathcal L-\mathcal LA$ ✓）。
2. 对任意两个映射，$\operatorname{rank}(DH)=\operatorname{rank}H\iff\ker D\cap\operatorname{im}H=0$
   （秩-零化度：$\operatorname{rank}(DH)=\dim\operatorname{im}H-\dim(\ker D\cap\operatorname{im}H)$）。
3. $\ker D(\lambda)=\{(u,0,0):(\lambda I-\Lambda)u=0\}$；
   $\operatorname{im}H=\{(\mathcal Lx,CAx,Cx):x\in\mathbb C^n\}$。
4. 故 $\ker D(\lambda)\cap\operatorname{im}H\ne0\iff\exists x\in V,\ \mathcal Lx\ne0,\
   \Lambda\mathcal Lx=\lambda\mathcal Lx$。
5. 于是 $(5b)$（$\operatorname{rank}Q(\lambda)=h$ 对所有 $\lambda$）$\iff$ 不存在这样的 $(x,\lambda)$
   $\iff U$ 不含 $\Lambda$ 的非零特征向量。
6. 取 $E$ 使 $\ker E=U$。PBH：$(E,\Lambda)$ 不可观测 $\iff\exists\lambda:\operatorname{rank}
   \begin{pmatrix}\lambda I-\Lambda\\ E\end{pmatrix}<q\iff\exists$ 特征向量 $u$ 使 $Eu=0\iff U$ 含特征向量。
   故三个等价成立；最后一个是最优观测性矩阵的秩判据。$\square$


在 44 个 $(5a)$-可行候选上与 Toeplitz 判据**完全一致**，含 $V\cap\mathcal Z\ne0$ 的掉秩样本）。
*意义*：
* **固定候选的谱检验降为一个 $q$ 维可观性秩计算**——不用极大子式、gcd、Smith 形，也不必对 $\lambda$ 量化；
* 给 $\exists\mathbb R$ 编码一个更紧凑的证书（观测性矩阵的左逆），且 $s=\operatorname{rank}\mathcal L(V)$
  只有 $q+1$ 种取值 ⟹ 层析取是多项式的；
* **因子化不唯一，但判据不变**：$\Lambda,G_0,G_1$ 的选取不是典范的；不同选取给出不同的 $(E,\Lambda)$，
  但每个观测性检验都等价于**同一个** $(5b)$（第 5 步对任意可行因子化成立），故真值不依赖选取。
* **边界（必须一起读）**：这是"给定 $\mathcal L$"的多项式时间检验；**不**给出选择 $\mathcal L$ 的多项式算法，
  也不改变 $q1$ 的开放状态；$\Lambda,E,\mathcal L$ 是**耦合的设计变量**，全局搜索仍未解决。
*位置*：本文件 B.10；专家 2026-11-04 §3；[workspace/for_expert/archive/10_status_and_direction-answer.md](../../workspace/for_expert/archive/10_status_and_direction-answer.md)。

## Lean（2026-11-06 已同步登记）

**[Lean-conditional]** —— 内核只覆盖代数/维数骨架，矩阵实例化与其余分部为纸面。

* 内核：`B12_Observability.pow_finrank_eq_neg_sum`、`observable_iff_krylov`、`observable_iff_rank_krylov`
* 均在 `tools/lean/MyProof/` 下，已登记进 `tools/lean/STATEMENT_MAP.md`；WSL 侧 `lake build MyProof` exit=0。
* 差异：矩阵实例化/行空间翻译与其余分部仍为纸面（详见 `## 状态与历史` 的等级行）。

## 精确验证

* `tools/verification/observability_test.py`

## 状态与历史

*等级*：**[已证-纸面]** + **[精确验证 44/44]**（`tools/verification/observability_test.py`：
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。




## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

无（证据全部在本卷宗内）。
