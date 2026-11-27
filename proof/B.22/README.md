# B.22 · 等号障碍：$h=q+r_1$ 时 $(5b)$ 必失败

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.22` 条目（§0.1 归并表）。

## 命题

**B.22（等号障碍：$h=q+r_1$ 时 $(5b)$ 必失败；专家 2026-11-05 给出证明）** 设 $\mathcal L$ 满足 $(5a)$、
$\operatorname{rank}\mathcal L=q\ge1$、$h=\operatorname{rank}[\mathcal L;CA;C]=q+r_1$，其中 $r_1=\operatorname{rank}[CA;C]$。则
$$\exists\lambda_0\in\mathbb C:\ \operatorname{rank}Q_{\mathcal L}(\lambda_0)<h,$$
故 $(5b)$ 失败。更强地：$Q_{\mathcal L}$ 严格等价于 $\operatorname{diag}(\lambda I_q-K_1,\ I_{r_1})$，于是
$$d_{\rm fin}=q,\qquad d_\infty=r_1 .$$

## 纸面证明

*证明*（专家原文的分步）：
1. 取 $B\in\mathbb C^{r_1\times n}$ 满行秩且 $\operatorname{row}B=\operatorname{row}[CA;C]$；令 $H_0=[\mathcal L;B]$。
   等号 $h=q+r_1$ 意即 $\operatorname{rank}H_0=q+r_1$，即 $H_0$ **满行秩**（$q+r_1$ 行）。
2. 由 $(5a)$，$\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}[\mathcal L;CA;C]=\operatorname{row}H_0$，故存在
   $K=[K_1\ K_2]\in\mathbb C^{q\times(q+r_1)}$（$K_1$ 为 $q\times q$、$K_2$ 为 $q\times r_1$）使 $\mathcal LA=KH_0$。
3. **关键因子化**：
$$\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\ B\end{bmatrix}
=\begin{bmatrix}\lambda\mathcal L-K_1\mathcal L-K_2B\\ B\end{bmatrix}
=\begin{bmatrix}\lambda I_q-K_1&-K_2\\ 0&I_{r_1}\end{bmatrix}
\begin{bmatrix}\mathcal L\\ B\end{bmatrix}.$$
4. 左端与 $Q_{\mathcal L}(\lambda)$ 的秩相同（$B$ 与 $[CA;C]$ 行空间相同）；右端的 $H_0$ 满行秩，故右端秩 = 那个方块
   $P(\lambda):=\begin{bmatrix}\lambda I_q-K_1&-K_2\\ 0&I_{r_1}\end{bmatrix}$ 的秩。
5. $\det P(\lambda)=\det(\lambda I_q-K_1)$ 是**$q$ 次首一**多项式；$q\ge1$ 时在 $\mathbb C$ 上有根 $\lambda_0$，
   该处 $\operatorname{rank}P(\lambda_0)=q-1+r_1<h$（hmm：见下注），故 $(5b)$ 失败。
6. 定量：用常数可逆行变换消去 $-K_2$，$\begin{bmatrix}I_q&K_2\\0&I\end{bmatrix}P(\lambda)=\operatorname{diag}(\lambda I_q-K_1,I_{r_1})$，
   故 $d_{\rm fin}=q$、$d_\infty=r_1$（$r_1$ 个无穷初等因子，全为 1 阶）。$\square$

*注*：第 5 步的秩：$P(\lambda_0)$ 是 $q+r_1$ 阶方阵且 $\det=0$，故 $\operatorname{rank}<q+r_1=h$ ✓。
*意义*：这是**等号情形的完整解**——不需要 Kronecker 形、不需要可观测性、不需要 B.21。配合行数界
（$h>q+r_1$ 时 $\operatorname{rank}Q\le q+r_1<h$ 直接排除），得到
$$h\ge q+r_1\ \Longrightarrow\ (5b)\ \text{失败}.$$
*等级*：**[已证-纸面]**（专家证明）$+$ **[Lean-conditional]**（`B22.det_blockIdentity` 方块行列式、`B22.exists_root_of_pos_natDegree` 正次数有根；差在 $H_0$ 满行秩 ⟹ 秩不变、$K$ 存在性、秩化归三步）。

## Lean

* `B22.lean` —— `det_blockIdentity`（分块行列式恒等式）、`exists_root_of_pos_natDegree`（次数为正则有根）
* 差异：矩阵级块因子化 $Q_{\mathcal L}=P(\lambda)H_0$ 的实例化是纸面；内核只覆盖两块基石

## 精确验证

* `tools/verification/equality_case.py`、`equality_search.py`（等号层扫描）
* `tools/verification/b22_equality_obstruction.py`（早期实现，太慢已弃用）





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 状态与历史

经专家复核（2026-11-05）：证明正确；标 `[Lean-conditional]` 而非 `[Lean]`，因为矩阵实例化是纸面。
