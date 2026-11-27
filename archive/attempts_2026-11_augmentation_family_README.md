# augmentation_family —— 增广族的几何（专家 WP2）

> **2026-11-26 说明**：本目录是**主线研究日志**（attempts `001`–`487`，共 501 篇），不是单一小专题。
> 下面的「目标 / 已有进展」写于第 7 篇 attempt 的时代，只覆盖 001–007 阶段；当前索引见下面的阶段表。
> 目录名 `augmentation_family` 是历史名（源自"增广族"）；内容已从增广族演化到层程序与硬度。

## 阶段索引（按编号区间；边界是按主题的近似，个别条目跨阶段）

| 阶段 | 编号 | 主题 | 代表条目 |
|---|---|---|---|
| 1 | 001–098 | 增广族几何：P1 参数化、$\Omega$-抽样、闭包与 $q_0$ 扫描、$Z$-生成 | `01_p1_family`、`02_omega_construct`、`06_z_generator`、`07_q0_scan` |
| 2 | 100–199 | $c=1$ / $c=2$ 层的结构与不变量、证书、rank 4 | `102_free_fibre_criterion`、`142_general_incidence_theorems`、`162_direct_original_pencil_certificate`、`182_c1_infeasibility_lemma` |
| 3 | 200–299 | gadget 与 rank 门、固定 $q$ / 子空间归约、$q=4$ 二分 | `202_gadget_naive_embedding`、`242_rank4_n5_impossible`、`262_bezout_qe_dependencies`、`283_q4_r1_dichotomy` |
| 4 | 300–399 | 层程序、超平面层参数化与复杂度、专家审计 | `303_79_verdict_lifts`、`322_hyperplane_determinism_components`、`343_stratified_cover_fix`、`375_stage2_bit_complexity`、`392_expert107_audit` |
| 5 | 400–487 | 两层判定、行空间恒等式、判据验证与撤回、复杂度审计 | `402_two_strata_decide`、`412_rowspace_identity_proof`、`427_criterion_validated`、`447_criterion_summary`、`467_two_more_retractions`、`487_complexity_audit` |

## 目标

把 $(5a)$ 的**增广族**变成一个可计算的对象，并回答专家 §12 第 5 步：

> 完备增广族是否**不可约**？（若不可约，"$(5b)$ 在某成员上成立"要么退化恒不成立、要么是稠密开集 ⟹
> 一个点即可判定。）

## 已有进展

| 项 | 内容 | 位置 |
|---|---|---|
| P1 §V 的参数化 | $N_C$、$T$、$Y_J(\Theta)$、$W_J(\Theta)$、$L(\Theta)=W_J(\Theta)(N_CT)^{+}$；对**任意阶** $q$ 用 $k=q-r$ | [tools/verification/p1_family.py](../../tools/verification/p1_family.py) |
| 逐点核验 | $n=5,6,7$ 各 3 seed：51 图卡、306 采样；每点断言行满秩、$\operatorname{row}L_0\subseteq\operatorname{row}L$；$(5a)$ 成立 **35/306（11.4%）** | 同上，`python tools/verification/p1_family.py` |
| 族内变化 | 同一 $(A,C,L_0,q)$ 内 $(5b)$ 的判定会变（3 个实例有显式证据）| [workspace/kronecker/attempts/02](../kronecker/attempts/02_family_sequences.md) |

**关于 $(5a)$ 的位置（避免误读）**：P1 §V 的参数化描述的是**所有最小维候选**；$(5a)$ 是之后附加的条件，
其约化形式是 P1 Lemma 2 / 式 (20)（一个秩条件）。所以"盲抽 $\Theta$ 只有 35/306 落入可行集"只是
**抽样命中率**，**不是**关于 $(5a)$ 的数学结论——$(5a)$ 早在 2026-10-21 就解决
（[proof/5a_archive](../../proof/5a_archive/README.md)；P1 Thm 1/3 给出构造与完备族）。

它的唯一用处：**$(5b)$ 的扫描必须在可行集 $\Omega^{\star}_{A,J}$ 内做**，否则大部分样本是无效候选，
"没找到 $(5b)$" 就没有说服力。

**另一个读数**：在 $q=q_0$ 上抽样 306 点，**没有**找到 $(5b)$ 成立的成员（所有 $(5a)$ 点都失败），
与"$q_{\min}>q_0$ 常见"一致；但 $\Theta$ 的可行集可能是薄的（CLAUDE 纪律 12），**不能**由"没找到"下结论。

## 构造式 $\Omega$-抽样（第 2 步）

不走"在 $\Theta$ 里盲抽"，直接用 $(5a)$ 的子空间形式：
$V_{\min}$（闭包）+ 一步前像 $U=\{x: xA\in V_{\min}+W\}$。
**12 实例、1172 个合法样本、78 个 $(5b)$ 成立**；两个实例的 $q_{\min}$ 被精确确定
（$5/1000\to3$、$6/1001\to5$，都 $>q_0$）。见
[attempts/02_omega_construct.md](../q1_false/feasibility_geometry/attempts/02_omega_construct.md)。

**待核**：闭包维数（$(5a)$ 下的精确最小行数）在 $2/12$ 个实例上**严格大于** $\Sigma\eta_j$。

## 功能可观测性：上一轮"未找到"的真因（第 3 步）

上一轮 24 个随机实例里只有 5 个**功能可观测**（$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O_C$）；
不满足时观测器**根本不存在**，$(5b)$ 无解是平凡的。在构造的可观测实例上（$n=5$，6 个 seed）：

$$q_{\min}=\text{闭包}+1\quad(6/6,\ 10/10\ \text{见证})$$

与上一轮两个精确例合并：**8/8**。见
[attempts/03_functional_observability.md](../q1_false/feasibility_geometry/attempts/03_functional_observability.md)。

> ~~**若该规律成立，则 $q1$ 是 $P$**~~ —— **C1（$q_{\min}=\mathrm{cl}+1$）已推翻**（40 个反例，见
> [proof/refuted/C1_closure_plus_one.md](../../proof/refuted/C1_closure_plus_one.md)）。
> 幸存：$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$（54/56 可观测实例，未证）。

## 闭包处 $(5b)$ 的可计算条件：B.9（第 4 步）

$q=\mathrm{cl}$ 时 $(5a)$ 解唯一，故该处 $(5b)$ 是结构问题。交叉表（
[closure_feasibility.py](../../tools/verification/closure_feasibility.py)）显示 $m=q+2p-h=0$ 的实例全失败；
由此得

$$\text{零左指标}=2p-r_1,\qquad \text{非零左指标}=q+r_1-h,\qquad
\boxed{(5b)\Rightarrow h<q+r_1}$$

**已证**（[proof/left_index_count](../../proof/left_index_count/README.md)，用 B.6+B.8）+ **验证 56/56**；
样本里 16 个失败**全部**由它解释。见
[attempts/04_zero_left_indices.md](../q1_false/feasibility_geometry/attempts/04_zero_left_indices.md)。

## 未做（下一步）

1. **不可约性**：把 $(A)$ 写成 $\Theta$ 的多项式方程组，问其零集是否不可约（小 $n$ 上可用
   精确消元/Gröbner；当前环境没有 CAS，需要自己实现或只在 $k(s-k)\le2$ 的低维情形手算）；
2. **维数**：每个图卡的可行集维数（$\Theta$ 空间维数 $k(s-k)$ 减去 $(A)$ 的独立方程数）；
3. **$q>q_0$ 的完备族**：现在的 $k=q-r$ 推广覆盖"所有 $q$ 维、含 $L_0$ 的候选"，但没有用到
   $(A)$ 的显式刻画（P1 Lemma 2），因此只能抽样。

## 复现

```bash
python tools/verification/p1_family.py        # 族构造 + (5a) 密度
python tools/verification/family_sequences.py # 族内 $(5b)$ 变化（按 (instance,q) 分组）
```

## 相关

- [archive/expert_correspondence/answer_2026-11-02_notes.md](../../archive/expert_correspondence/answer_2026-11-02_notes.md)（专家 WP2 建议）
- [proof/toeplitz_criterion](../../proof/toeplitz_criterion/README.md)（判据）
- [docs/05 Q1](../../docs/05_open_questions.md)

## 更正（专家 2026-11-02 答复后）：闭包不是精确最小维数；间隔可以为 2

1. **闭包不可作为最小值**：公开例子（复现见 [proof/fernando_2gap](../../proof/fernando_2gap/README.md)）
   $q_0=3$ 而闭包 $=4$。贪心加入 $xA$（而非其模 $W$ 的剩余类）可能**加多行**（专家 §8.1 的提醒成立）。
   权威量：$q_0=\sum_j\eta_j$（`tools/ledger/c208_q0_lower_bound.py`）。
2. **$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$ 被推翻**（[C3](../../proof/refuted/C3_gap_can_be_two.md)）：
   公开例子 $q_0=3$、$q_{\min}=5$，间隔 **2**。
3. 幸存：$q_0\le q_{\min}\le n_0-p$，上端点保证可行。
4. **加强的必要条件**（已证）：$q+r_1-s\le h<q+r_1$，且 $d_{\rm fin}\le s-(q+r_1-h)$。

## 任意阶候选生成：Z-参数化（第 5 步）

闭包只能给 $\ge$ 闭包维数的候选；[z_generator.py](../../tools/verification/z_generator.py)
用 $\mathcal Z=\ker[C;\mathcal L]\subseteq\ker[C;L_0]$ 的参数化生成**任意阶**（含最小阶 $q_0$）的候选。

公开例子上的结果：$q=4$ 的 **40 个代数可行候选全部谱不可行**；$q=5$ 40/40 可行；
$q=3$ **0/240**——$(A)$ 在 $q_0$ 处是薄集，抽样判不了，必须代数地解 $(A)$。见
[attempts/06_z_generator.md](../q1_false/feasibility_geometry/attempts/06_z_generator.md)。

## 最小阶的正确统计（第 6 步）

Z-参数化使得**在 $q_0$ 阶**判定 $(5b)$ 成为可能（闭包会加多行）。56 个功能可观测实例：

* **$q_{\min}=q_0$（精确，有见证）：39**
* $q_{\min}>q_0$：16（其中 **3 个** $(A)$ 满维、$(5b)$ 全失败 = 纯几何障碍）
* $q_0$ 阶代数薄集、无样本：1

见 [attempts/07_q0_scan.md](../q1_false/feasibility_geometry/attempts/07_q0_scan.md)。此结论**取代**所有基于闭包的 $\mathrm{cl}$ 统计。
