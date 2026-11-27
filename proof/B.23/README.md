# B.23 · 统一分块因子化

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.23` 条目（§0.1 归并表）。

## 命题

**B.23（谱侧的统一因子化：$Q_{\mathcal L}(\lambda)=P(\lambda)H_0$）** 设 $\mathcal L$ 满足 $(5a)$、$\operatorname{rank}\mathcal L=q$；
取 $B\in\mathbb C^{r_1\times n}$ 满行秩且 $\operatorname{row}B=\operatorname{row}[CA;C]$，令 $H_0=[\mathcal L;B]$。由 $(5a)$ 的
$\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}H_0$ 得 $\mathcal LA=KH_0$，记 $K=[K_1\ K_2]$（$K_1$ 为 $q\times q$、$K_2$ 为 $q\times r_1$）。则
$$Q_{\mathcal L}(\lambda)=\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\ B\end{bmatrix}
=P(\lambda)\,H_0,\qquad P(\lambda)=\begin{bmatrix}\lambda I_q-K_1&-K_2\\ 0&I_{r_1}\end{bmatrix},$$
且对每个 $\lambda\in\mathbb C$：
$$\operatorname{rank}Q_{\mathcal L}(\lambda)=\operatorname{rank}H_0-\dim\bigl(\ker P(\lambda)\cap\operatorname{im}H_0\bigr),\qquad
\det P(\lambda)=\det(\lambda I_q-K_1).$$
于是
$$(5b)\ \text{失败}\iff\exists\lambda:\ \ker P(\lambda)\cap\operatorname{im}H_0\ne0,$$
且这样的 $\lambda$ **必是 $K_1$ 的特征值**（因 $\det P(\lambda)=\det(\lambda I_q-K_1)$）。

## 纸面证明

*证明*：逐块相乘即得因子化；秩公式是 $\operatorname{rank}(PH)=\operatorname{rank}H-\dim(\ker P\cap\operatorname{im}H)$；
行列式由下三角块的 $I_{r_1}$ 得到。$\square$

*推论*：
1. **B.22 是等号特例**：$h=q+r_1$ 时 $\operatorname{im}H_0=\mathbb{C}^{q+r_1}$，于是 $K_1$ 的任一特征值都给出秩跌；$q\ge1$ 时必有特征值 ⟹ 必失败 ✓。
2. **谱侧统一为一个对 $(K_1,\operatorname{im}H_0)$ 的问题**：$(5b)\iff$ 对 $K_1$ 的每个特征值 $\lambda$，$\ker P(\lambda)$ 与 $\operatorname{im}H_0$ 交为零。
   即"坏广义特征向量避开子空间 $\operatorname{im}H_0$"。
3. 由此 $(5b)$ 的失败只可能发生在**有限个** $\lambda$ 上（$K_1$ 的特征值），这与 B.16 的"坏集是有限并"一致。

`tools/verification/b23_factorization_rank.py`）。

## Lean

* 等级行引用的 Lean 声明：`WorkA.finrank_range_comp`、`B22.det_blockIdentity`、`B22.exists_root_of_pos_natDegree`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`WorkA.finrank_range_comp` 秩公式、`B22.det_blockIdentity` 方块行列式、`B22.exists_root_of_pos_natDegree`；差在矩阵实例化与 $\lambda$-依赖运算） $+$ **[精确验证 8128/8128]**（因子化、秩一致、行列式一致；
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

无（证据全部在本卷宗内）。

## 专家复核意见（成立）

$\det P(\lambda)=\det(\lambda I_q-K_1)$ 只由块三角性得到；不需要 $K_1$ 可对角化或可逆。
