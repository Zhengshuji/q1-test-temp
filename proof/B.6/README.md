# B.6 · 右最小指标与无穷初等因子

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.6` 条目（§0.1 归并表）。

## 命题

**B.6（a）〔原 B.6〕（右最小指标为零）** 设 $L$ 满足 $(5a)$。则观测器铅笔 $Q_L(\lambda)=[\lambda L-LA;CA;C]$ 的**右最小指标全为 $0$**
（右零模有常值基）。只用 $(5a)$，不需要 $(5b)$。

## 纸面证明

*证明*：[proof/kron_null_module/theorem.md](../kron_null_module/theorem.md)——按 $\lambda$ 的幂展开，最高次系数
$v_d$ 满足 $Lv_d=CAv_d=Cv_d=0$，由 $(5a')$ 得 $LAv_d=0$，故 $v_d$ 是常值零向量；减去 $\lambda^dv_d$ 后归纳。
**表述要点（专家 2026-11-04 §1）**：结论应写成"右零模由常值向量在 $\mathbb C[\lambda]$ 上**生成**"：
取常值零空间的**向量空间基**即得该模的多项式基，故右最小指标全为 0（这一步正是"模是常值零空间的多项式扩张"）。

位置：[proof/kron_null_module/](../kron_null_module/README.md)。
**注意**：这是一般铅笔理论中"常数秩 ⇏ 右指标 0"（反例 $[\lambda\ 1]$，见 [proof/refuted R18](../refuted/README.md)）的**对照**——
这里用的是 $Q_L$ 的**分块结构 + $(5a)$**，不是 $(5b)$。

**B.6（b）〔原 B.7〕（无穷初等因子全是 1 次）** 设 $L$ 满足 $(5a)$，$h=\operatorname{rank}[L;CA;C]$。则观测器铅笔
$Q_L(\lambda)=[\lambda L-LA;CA;C]$ 的无穷初等因子全是 1 次，故 $d_\infty=h-\operatorname{rank}L$。
配合 B.6 与全局恒等式得 $\sum_j\varepsilon_j=\operatorname{rank}L-d_{\rm fin}$（$d_{\rm fin}$ = 有限初等因子的总次数）；
**只有再加 $(5b)$（$d_{\rm fin}=0$）才有 $\sum_j\varepsilon_j=\operatorname{rank}L$**。
**B.7 本身只用 $(5a)$，不需要 $(5b)$。**
*证明*（**2026-11-04 按专家审阅意见重写**；旧证明"$D(\lambda)$ 在 $\mu=0$ 可逆故不贡献无穷因子"是**错的**——反转后 $D_{\rm rev}(\mu)$ 的下对角块是 $\mu I$，在 $\mu=0$ 奇异）：

反转铅笔 $Q_{\rm rev}(\mu)=\mu Q_L(1/\mu)=[\,\mathcal L-\mu\mathcal LA;\,\mu CA;\,\mu C\,]$。

1. $\mu=0$ 处 $\operatorname{rank}Q_{\rm rev}(0)=\operatorname{rank}[\mathcal L;0;0]=q$（$\mathcal L$ 行满秩）；法秩为 $h$。
2. 取 $H=[\mathcal L;CA;C]$ 的 $h$ 个线性无关行，**包含 $\mathcal L$ 的全部 $q$ 行**（可做到，因这 $q$ 行无关，
   可延拓成 $H$ 的行基）；再取 $h$ 列使对应的 $h\times h$ 子式非零。
   对应的 $Q_{\rm rev}(\mu)$ 的 $h\times h$ 子式为 $\mu^{h-q}(c+O(\mu))$，$c\ne0$：
   每个被选中的下方行贡献一个 $\mu$，而前 $q$ 行在 $\mu=0$ 处 specialize 为 $\mathcal L$。
3. 另一方面 $Q_{\rm rev}$ 的**任何** $h\times h$ 子式都被 $\mu^{h-q}$ 整除：只有 $q$ 个顶行，
   故任意 $h$ 行的选取至少含 $h-q$ 个下方行。
   ⟹ 第 $h$ 个行列式因子在 $\mu=0$ 的赋值**恰为** $h-q$。
4. $\mu=0$ 处秩为 $q$ ⟹ 前 $q$ 个局部不变因子是单位；法秩为 $h$ ⟹ 其余 $h-q$ 个非单位，
   其赋值之和 $=h-q$ ⟹ 每个赋值恰为 $1$。

故无穷初等因子全为 1 次、总次数 $d_\infty=h-q=h-\operatorname{rank}\mathcal L$。$\square$

位置：[proof/t4b_infinite_divisors/](../t4b_infinite_divisors/README.md)。
**注意**：$d_\infty$ 必须按反转铅笔不变因子在 $\mu=0$ 的**阶**算，不能用多项式总次数（[proof/refuted R20](../refuted/README.md)）。
**推论（必要性屏障）**：若 $(5a)+(5b)$ 同时成立，则 $\operatorname{rank}L\le q+2p-h$
（左指标个数 $q+2p-h$ 非负、和 $=\operatorname{rank}L$）。
**惩罚**：早先把 $\sum\varepsilon=\operatorname{rank}L$ 写成 $(5a)$ 的推论是错的，已登记 [R21](../refuted/README.md)。

## Lean

* 等级行引用的 Lean 声明：`KronCoeff.kron_coeff_chain_strong`、`KronCoeff.kron_coeff_mem_N`、`KronFactor.kron_block_factor`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

**等级**：[已证-纸面] $+$ **[Lean-conditional]**（`KronCoeff.kron_coeff_chain_strong`：系数方程的倒向归纳；`KronCoeff.kron_coeff_mem_N`：系数全在 $N$ 里。**差异**：多项式←→系数序列的翻译、以及"右零模有常值基 ⟹ 右最小指标为 0"的 Kronecker 步骤在纸面，未 Lean 化）$+$ **[精确验证 150/150]**（$n=6,7,8$，每维 50 个满足 $(5a)$ 的铅笔）。
**等级**：[已证-纸面] $+$ **[Lean-conditional]**（`KronFactor.kron_block_factor`：分解恒等式 $LA=XL+Y_1CA+Y_2C\Rightarrow\lambda L-LA=(\lambda I-X)L-\dots$，仍用于第 2 步起点的写法；**差异**：行列式因子的 $\mu$-赋值未 Lean 化）$+$ **[精确验证 151/151]**（$n=6,7,8,9,10$，含 43 个不可行；反例 0）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

[kron_null_module/](../kron_null_module/README.md)、[t4b_infinite_divisors/](../t4b_infinite_divisors/README.md)、[descriptor_reduction/](../descriptor_reduction/README.md)、[left_index_count/](../left_index_count/README.md)、[toeplitz_criterion/](../toeplitz_criterion/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

证明给出的是**更强**结论：多项式右零模由常值向量生成（不只是每个右指标为 0）；不需要 $(5b)$。
