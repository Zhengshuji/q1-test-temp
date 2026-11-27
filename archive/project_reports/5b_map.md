# (5b) 工作总图（2026-11-02 整理）

> 目的：把散在 12+ 个 `proof/` 目录里的 $(5b)$ 工作收成一张图，**避免再重复研究**。
> 配套工具：`python tools/hygiene/claim_index.py --grep <关键词>`（152 条命题索引）。

## 0. 一句话

$(5b)$ 早已被翻成**有限多个可计算对象**（铅笔的秩恒等式 / 行列式因子 / Smith 形），
各层判据分散在多个目录；**唯一没解决的是判定复杂度**——连续参数上的 $\exists$ 问题。

---

## 1. 等价形式（把 $(5b)$ 变成可分析对象）

| 形式 | 位置 | 等级 |
|---|---|---|
| 商铅笔：$(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\ \forall\lambda$ | [docs/02](../../docs/02_theorems_proven.md) B.1；[proof/pencil_equivalence](../../proof/pencil_equivalence/README.md) | [已证] + [Lean] |
| 铅笔因子化 $P(\lambda)=(\lambda I-\Lambda)H$（由 $(5a)$ **免费**得 $\operatorname{rank}P\le\operatorname{rank}H$）| [proof/5b_upper_bound](../../proof/5b_upper_bound/README.md) | [已证] + Lean |
| 商等价 Theorem Q：$[U\mid P(\lambda)]$ 形式 | docs/02 H.1；[proof/quotient_equivalence](../../proof/quotient_equivalence/README.md) | [已证] |
| 方阵条件（$[U\mid P(\lambda)]$ 何时方） | docs/02 H.2 | [已证] |
| $d=0$ 边界 | docs/02 H.3；[proof/d0_boundary](../../proof/d0_boundary/README.md) | [已证] |
| **固定 $U$**：谱判据 $=$ 行列式因子（Smith 形） | docs/02 J；[tools/verification/poly_smith.py](../../tools/verification/poly_smith.py) | [已证] + 工具 |
| 层程序的**子式 gcd** 形式（全部 $k\times k$ 子式无公根）| [proof/layer_program](../../proof/layer_program/README.md)、[proof/rho1_layer](../../proof/rho1_layer/README.md) | [已证] / [精确验证] |

**$(5a)$ 侧（已解决，不要重做）**：[proof/5a_archive](../../proof/5a_archive/README.md) 给出三种等价形式
（秩形式 / 行包含 / 分解 $LA=\Lambda L+G_0C+G_1CA$），$q_0=\sum_j\eta_j$（P1 Thm 2），
以及 **Lean**：`lean/ABridge.lean`（秩形式 $\iff$ 分解）、`lean/Factor.lean`（分解 $\iff$ 三核包含）。

---

## 2. 各层判据（已解决的部分）

| 层 | 判据 | 位置 |
|---|---|---|
| $\rho=0$ | $(5b)$ 自动 | docs/02 B.3；[proof/rho0_layer](../../proof/rho0_layer/README.md) |
| $\rho=d$（顶层）| $(5b)\iff(D_W^{\mathsf T},T_W)$ 可观测（PBH）| docs/02 B.2；[proof/top_layer_observability](../../proof/top_layer_observability/README.md) |
| $\mathcal V=\mathbb C^n$ | $A^{\mathsf T}$ 无落在 $K=\ker[C;CA]$ 的特征向量 | docs/02 B.4；[proof/b4_full_space](../../proof/b4_full_space/README.md) |
| $c_0=1,\ \rho=d$ | 循环向量判据 $\operatorname{rank}[v_W;v_WT_W;\dots]=d$ | docs/02 B.5；[proof/cyclic_vector_criterion](../../proof/cyclic_vector_criterion/README.md) |
| $(2,1)$ 层 | 三个 $2\times2$ 子式的 $\gcd$；$\tau$ 量词已由线性代数消掉 | [proof/rho1_layer](../../proof/rho1_layer/README.md) |
| $(3,1)$ 层的**格子** | C.1–C.5：由 $\mu=\dim(B\cap\mathcal U)$ 完全决定 | [proof/layer_31_theorems](../../proof/layer_31_theorems/README.md) |
| $c=1$ 一支总览 | T1–T11 与唯一缺口 | [proof/layer_program](../../proof/layer_program/README.md) |

---

## 3. 结构障碍（为什么不能只用整数条件判定）

* **秩屏障**：层可行 $\Rightarrow\rho\le r(\lambda):=\dim\pi(\mathbb C^n(\lambda I-A))$；
  $\min_\lambda r<\rho_{ci}\Rightarrow$ 无解（docs/02 F.1/F.2；[proof/rank_barrier](../../proof/rank_barrier/README.md)，1484 检查）。
* **互补障碍**（[proof/h_bound](../../proof/h_bound/README.md)）：若 $\ker C=\mathcal V\oplus Z$ 且 $\dim V\ge1$，
  则 $(5b)$ 必失败（对满足 $(A)$ 的 $Z$）——要求 $N_c=h$ **且** $h=n-p$ 同时成立（此前的无条件版本被 **R13** 推翻）。
* **阶谱猜想被推翻**（**R17**）：可行性不是单调的，$\mathrm{DEC}(q)\not\Rightarrow\mathrm{DEC}(q+1)$
  ⟹ 判定必须处理**连续参数**，不能化简为纯组合条件。

---

## 4. 复杂度（$q1$ 的核心）

| 结果 | 内容 | 位置 |
|---|---|---|
| **上界** | $\mathrm{DEC}(q)\in\exists\mathbb R$：chart-free 编码，变量/方程 $O(n^3)$、次数 $\le n$、无图卡析取；部分 Lean | [proof/dec_q_existsR](../../proof/dec_q_existsR/README.md) |
| 旧版上界 | Smith 证书版（引理 1–3），已被 chart-free 版取代；引理 1（$\lambda=\infty$ 无假失败）**必须在 $(A)$ 下陈述**（专家 QA10 反例）| [proof/spectral_locus](../../proof/spectral_locus/README.md) |
| **缺口 G.1** | 编码规模三项：约束条数、系数比特长、多项式表示 **未证** | docs/02 G.1 |
| **下界** | $\exists\mathbb R$-hard / NP-hard **完全未知** | —— |

---

## 5. 周边命题（下界 / 归约 / 工具）

| 命题 | 一句话 | 位置 |
|---|---|---|
| $P\in\mathbf P$ | 递归定理 + $O(n^4)$ | [proof/p_is_polynomial](../../proof/p_is_polynomial/README.md)（docs/02 D.1–D.4）|
| $q_{\min}$ 下界 | $\max(r+\varepsilon,\rho+\max(c_0,1))$ | [proof/lower_bound](../../proof/lower_bound/README.md)（A.3）|
| $L_0$ 归约 | $L_0$ 中落在 $\operatorname{row}C$ 的行可去掉（$q_{\min}$ 减 1）| [proof/l0_reduction](../../proof/l0_reduction/README.md) |
| $S=\mathcal J$ 族 | $\langle\mathcal J\rangle_A=\mathbb C^n\Rightarrow q_{\min}=n$（杀 R1/R3）| [proof/s_j_family](../../proof/s_j_family/README.md) |
| 基族 $\mathcal B_{s,k}$ | $S$ 本身怎么选（$K=S\cap\ker\phi$）| [proof/base_family](../../proof/base_family/README.md) |
| 固定 $S$ 的纤维 | A2：纤维上谱可行性的判据 | [proof/incidence_strata](../../proof/incidence_strata/README.md) |
| 全局入射空间 | $\mathcal X_{s,k,\ell}$（QA21 里程碑 1）| [proof/global_incidence](../../proof/global_incidence/README.md) |
| PCC | 参数化共同补空间问题（QA22 Q4）| [proof/PCC](../../proof/PCC/README.md) |
| 双向量（$r=2$）| 可分解性的第一道非线性门槛（K.1–K.3）| [proof/bivector_r2](../../proof/bivector_r2/README.md) |
| $E=W\oplus J$ 工具 | 投影/压缩 | [proof/xw_decomposition](../../proof/xw_decomposition/README.md) |
| H.2 维数算术 | $w_m\times(r+t)$ 的书账 | [proof/h2_dim_arithmetic](../../proof/h2_dim_arithmetic/README.md) |

---

## 6. 已死（**不要重走**）

| 路线 | 死因 | 位置 |
|---|---|---|
| $(5b)\iff$ "可控性"（Q5）| $\beta(\mathcal H)\subseteq B$ **恒成立** ⟹ "输入"恒为零，提法退化 | [proof/controllability_equivalence](../../proof/controllability_equivalence/README.md) |
| 四个闭式 $q_{\min}=\dots$ | 反例 | [proof/refuted](../../proof/refuted/README.md) R1–R4 |
| "$h=n-p\Rightarrow(5b)$ 失败" | 宽矩阵反例 | R13 |
| 阶谱单调/区间猜想 | 反例 | R17 |
| $(5b)\Rightarrow$ 右指标全 $0$ | 常数秩 ⇏ 零空间恒定 | R18 |
| $d_\infty=h-\operatorname{rank}L\iff\ker L=N$ | 维数差 vs 空间相等 | R19 |
| $d_\infty$ 用多项式总次数度量 | 应用 $\mu$-adic 赋值 | R20 |
| $(5a)\Rightarrow\sum\varepsilon=\operatorname{rank}L$ | 要用 $\operatorname{rank}L-d_{\rm fin}$ | R21 |

---

## 7. 工具

| 工具 | 用途 |
|---|---|
| [tools/verification/spectral_gcd.py](../../tools/verification/spectral_gcd.py) | 全部 $k\times k$ 子式的 $\gcd$（$\forall\lambda$ 判据）|
| [tools/verification/poly_smith.py](../../tools/verification/poly_smith.py) | Smith 形 / 行列式因子 / 全列秩常数 |
| [tools/exact_linalg/linalg_q.py](../../tools/exact_linalg/linalg_q.py) | 带断言与残差校验的精确线性代数 |
| [tools/verification/kronecker_pencil.py](../../tools/verification/kronecker_pencil.py) | 铅笔的 Kronecker 数据（含 `d_infinity`）|
| [tools/verification/observer_pencils.py](../../tools/verification/observer_pencils.py) | 从 $(A,C,L)$ 构造观测器铅笔 |
| [tools/verification/descriptor_pencil.py](../../tools/verification/descriptor_pencil.py) | 约化 descriptor 铅笔 $R(\lambda)$ |
| [tools/verification/partition_scan.py](../../tools/verification/partition_scan.py) | 左指标划分的统计 |
| [tools/hygiene/claim_index.py](../../tools/hygiene/claim_index.py) | **命题索引**（152 条，`--grep` 检索）|

---

## 8. 2026-11-01/02 的净新增（本会话）

* **B.6**：$(5a)\Rightarrow$ 右最小指标全 $0$（[proof/kron_null_module](../../proof/kron_null_module/README.md)，Lean `KronCoeff`）。
* **B.7**：$(5a)\Rightarrow$ 无穷初等因子全 1 次、$d_\infty=h-\operatorname{rank}L$（[proof/t4b_infinite_divisors](../../proof/t4b_infinite_divisors/README.md)）。
* **B.8**：$(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}L$（B.6+B.7 的直接推论）。
* **descriptor 约化**：左指标 $=$ $[\lambda E-EX^{\mathsf T}\,B]$ 的右指标 $=$ descriptor 可控性指标
  （[proof/descriptor_reduction](../../proof/descriptor_reduction/README.md)）。
* **observability_chain**：$(5b)$ 恒成立但 $(5a)$ 需链闭合（[proof/observability_chain](../../proof/observability_chain/README.md)）。
* 撤回 **R18–R21**（其中 R18 本身是"重复研究"的一个证据：旧说法"只含右奇异块"早被更正）。
* ⚠️ **重复研究的教训**：本会话重新推导了 $(5a)$ 不是硬度来源、$LA=\Lambda L+G_0C+G_1CA$ 的分解、
  以及 $P=(\lambda I-\Lambda)H$——**这三件事 2026-10-21 就已在 `proof/5a_archive` 与 `proof/5b_upper_bound`**。
  事故分析与防复发措施见 [workspace/process/repeat_research_postmortem_2026-11-02.md](../process/repeat_research_postmortem_2026-11-02.md)。

---

## 9. 现在真正缺的（只有两条）

1. **$\mathrm{DEC}(q)$ 的复杂度**：$\exists\mathbb R$-hard / NP-hard 的下界，或多项式算法。上界已有（$\in\exists\mathbb R$）。
2. **G.1 的编码规模三项**：约束条数、系数比特长、多项式表示——没有它就不能声称"$\exists\mathbb R$-complete"。

**其余都已解决或已判死**，不要再重做。
