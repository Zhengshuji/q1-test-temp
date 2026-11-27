> **2026-11-10 更新**：本文件是历史工作清单/路线记录；当前状态与下一步见 [STATUS.md](../../../STATUS.md)，项目脉络见 [HISTORY.md](../../../HISTORY.md)，当前送审件见 [83](../../../workspace/for_expert/archive/83_project_consolidation_q1_roadmap.md)。

# 11 · 可用 / 不可用清单、现状与到 $q1$ 的路线

> 2026-11-09。一页纸的“资产盘点 + 现状 + 路线选项”。用于避免继续在已撤回的结论上工作，
> 也用于向专家提问。详细证明见各条链接；这里只列**能不能用**。

---

## 1. 一句话现状

$q1$ 仍开放。文献（Fernando 2026）已解决刻画、存在性、阶谱、逐阶充要、最小阶；
唯一开放的是 $\exists\Theta$ 的判定复杂度。项目目前：
**有 $\exists\mathbb R$ 上界、低 $c$ 分类、刚性、一致谱引理；没有一个 sound 的乘法门，也没有多项式算法。**

---

## 2. 可用（valid）

| 结果 | 等级 | 位置 | 用途 |
|---|---|---|---|
| 刻画/阶谱（文献）| M4（外部）| [docs/07](../../../docs/07_literature_review.md) | 不再重证；$q1$ 只剩复杂度 |
| $\mathrm{DEC}(q)\in\exists\mathbb R$ | M3 | [proof/dec_q_existsR](../../../proof/dec_q_existsR/README.md) | 上界定位 |
| 块判据（坏 $\iff$ 部分特征向量）| M3 | [B.24](../../../proof/B.24/README.md) | 所有低 $c$ 分析的基础 |
| 闭性 + generic gcd | M3 | [B.24](../../../proof/B.24/README.md)、[B.8](../../../proof/B.8/README.md) | 分量/好点判定 |
| $c=0$ 不可能 | M2/M3 | [attempts/186](../../../workspace/q1_false/c_stratification/attempts/186_61_verdict_implementation.md) | 低 $c$ 分类 |
| $c=1$：$W_L\subseteq D$ 不可行 | M2 | [182](../../../workspace/q1_false/c_stratification/attempts/182_c1_infeasibility_lemma.md)、[183](../../../workspace/q1_false/c_stratification/attempts/183_c1_eigenlines.md) | 低 $c$ 分类 |
| $c=1$：$W_L\not\subseteq D$ 可容许真空 | M2 | [188](../../../workspace/q1_false/c_stratification/attempts/188_c1_outside_D.md) | 外点仍需 O2 |
| $c=2$ forced-plane；16/21 全 $q$ 不可行（$\mathsf P_{\rm ind}$）| M2 | [184](../../../workspace/q1_false/c_stratification/attempts/184_q4_excluded.md)、[185](../../../workspace/q1_false/c_stratification/attempts/185_seeds_infeasible_all_q.md) | 低 $c$ 分类 |
| 四层求解器 | M2 | [180](../../../workspace/q1_false/c_stratification/attempts/180_uniform_stratum_solver.md) | 实例判定 |
| 一般 $c$ 分量界（不变 + $B_{u,v}$）| M2 | [149](../../../workspace/q1_false/c_stratification/attempts/149_general_c_component_bound.md)、[171](../../../workspace/q1_false/c_stratification/attempts/171_Buv_rank_strata.md) | 结构 |
| 全局刚性 $A(K_0)\subseteq K_0,\omega>0$ 不可行 | M2 | [205](../../../workspace/q1_true/multiplication_gate/attempts/205_AinvK0_impossible.md) | 排除整条 gadget 路线 |
| 局部泄漏：只给 $A(V)\subseteq V$ | M2/M3 | [210](../../../workspace/q1_true/multiplication_gate/attempts/210_local_leakage_correction.md) | seed 10 反例 |
| 10 维变量核族 | M2（精确验证）| [228](../../../workspace/q1_true/multiplication_gate/attempts/228_68_69_verdict.md)、`c228` | 变量核存在 |
| 一致谱引理（单位子式）| M2 | [215](../../../workspace/q1_true/multiplication_gate/attempts/215_67_verdict_uniform_spectral.md) | $(5b)$ 的 uniform 证书 |
| 固定核 + 提升方向族 | M2 | [224](../../../workspace/q1_true/multiplication_gate/attempts/224_fixed_kernel_lift_family.md) | 但参数是开条件（225）|
| $q=2$ 完整 $(5a)$ 二分：$u\ne0$ 线性、$u=0$ 行列式 | M2 | [240](../../../workspace/q1_true/rank_gates/attempts/240_full_5a_q2_structure.md) | 当前门设计的正确起点 |
| Lean 内核（pair-lift、不变子空间特征向量、B.4 等）| L4/L3 | [tools/lean/STATEMENT_MAP.md](../../../tools/lean/STATEMENT_MAP.md) | 已验证的内核 |

---

## 3. 不可用 / 已撤回

| 结论 | 状态 | 原因 | 记录 |
|---|---|---|---|
| $\omega=2,q=3$ 固定 $L_0$ 变量核不可能（217）| **撤回** | 专家 10 维族反例 | [R22](../../../proof/refuted/README.md)、[228](../../../workspace/q1_true/multiplication_gate/attempts/228_68_69_verdict.md) |
| reduced $\det M=ad-bc$ 是观测器门（234/237/71）| **撤回** | 漏 $L_0A$ 行；完整 $(5a)$ 下实例无可行 $L$ | [R23](../../../proof/refuted/README.md)、[239](../../../workspace/q1_true/multiplication_gate/attempts/239_72_missing_L0A.md) |
| 边界见证 $(0,0,1,1,0)$ | **撤回** | 完整 $(5a)$ 下秩 5≠4 | 239 |
| no-drop 不能编码秩一（233）| **未决**（不是被推翻）| 234 的否证无效 | [233](../../../workspace/q1_true/multiplication_gate/attempts/233_no_drop_obstruction.md) 顶部注 |
| $q_{\min}=4$（$n=5$ 约束例）| 撤回 | $q_{\min}=2$；层≠阶 | §1 历史 |
| “可对角化 $\Rightarrow$ 铅笔好” | 更正 | 特征空间单射 | [191](../../../workspace/q1_false/c_stratification/attempts/191_c1_pencil_criterion.md) |
| 局部泄漏 $\Rightarrow$ 不可行 | 更正 | 只给 $A(V)\subseteq V$；seed 10 | 210 |
| 65/213 “模板不一致” | 更正（模板成立）| $LAN$ 列/行作用混淆 | [214](../../../workspace/q1_true/multiplication_gate/attempts/214_66_verdict_template_valid.md) |

---

## 4. 当前真正的开口

1. **sound 乘法门**：$q=2$ 的完整 $(5a)$ 只有两种：$u\ne0$ 线性（无乘法）、$u=0$ 时
   $\det[S;l;lA]=0$ 的二次型。需要 **rank 4** 的二次型（双曲平面 + 线性项），
   再在归一化 chart 上得到 $z=xy$；并处理 chart 边界。
2. **$(5b)$ 的 uniform 守卫**：单位子式（215）可用，但不能把 $(5a)$ 的行空间饱和。
3. **soundness/completeness**：所有可行 $L$ 都要解码；边界分支要处理。
4. **固定 $c$ 算法**：$c=0/1/2$ 的结构已有，但 O2 外点、$c=2$ 好性仍未算法化。
5. **$q1$ 的复杂度**：没有硬度归约，也没有多项式算法；$\exists\mathbb R$ 是唯一上界。

---

## 5. 到 $q1$ 的路线选项

### A. 硬度（∃R-hardness）

- A1：$u=0$ + rank4 二次型门 → 单门 → 变量共享/电路 → 归约；
- A2：换目标问题（static output feedback、affine rank minimization）做已知 ∃R-完全问题的嵌入；
- A3：用**固定低秩输入结构**（不是 witness）编码方程，避开 no-drop/开条件问题。

### B. 可解性/参数化

- B1：固定 $c$ 的代数算法（Grassmannian 上的消元/行列式理想）；
- B2：参数化复杂度（以 $c$、$q-\omega$、$n-p$ 为参数）；
- B3：证明 $q1$ 在 P（例如可行集是 generic-rank 型，可用线性代数判定）。

### C. 结构论文（不依赖 $q1$）

- 低 $c$ 分类（$c=0,1,2$ + 分量界）；
- 刚性（205/210/228）与一致谱引理（215）；
- $\exists\mathbb R$ 上界 + 条件门的负结果（239/240）。

---

## 6. 可能被忽略的方向（待专家判断）

- **描述复杂度**：$\exists\mathbb R$ vs NP vs P 的定位；是否有“generic rank”类的已知完全性？
- **代数几何算法**：Grassmannian 上的行列式理想、符号消元、实根计数；是否可给出 $c$ 固定时的算法上界？
- **实 vs 复**：项目用复代数闭域；原问题（$A,C,L$ 实？）是否改变复杂度？
- **约定**：$\mathsf P_{\rm ind}$ vs $\mathsf P_{\rm full}$ 对复杂度的影响（$c=2$ 全 $q$ 结论依赖前者）。
- **目标问题的选择**：static output feedback 的 ∃R-完全性（Liu 2026）能否直接嵌入？
- **文献**：Fernando 2026 的 $\exists\Theta$ 是否已有算法/复杂度讨论；传感器放置的 NP-hard 结果是否相关。
- **形式化**：Lean 目前只到内核；是否需要把低 $c$ 分类/刚性形式化？

---

## 7. 给专家的具体问题

1. 按这份“可用/不可用”清单，到 $q1$ 最值得走哪条路线（A/B/C）？为什么？
2. $u=0$ + rank4 的二次型门是否值得继续？有没有已知的障碍（chart 边界、guard 饱和、$L_0A$ 条件）？
3. 是否有项目忽略的方向（描述复杂度、代数几何算法、实/复、约定、其他目标问题）？
4. 现在是否应该把结构结果整理成论文，还是继续冲硬度？
5. 对 $q1$ 的“最可能答案”（hard / tractable / intermediate）有什么判断？

---

## 8. 专家 73 号裁决（2026-11-09）

**路线**：A（rank-4 门/电路）与 C（固定 $c$）**并行**，D（结构论文）现在开始；
B（ARM/static output feedback 归约）并行调查。不要单押 rank-4 门。

**rank-4 门的四个障碍**：
1. 实签名：需 signature $(2,2)$（$xy-zw$），rank 4 不够；
2. 归一化边界 $w=0$ 的额外解：排除/转化/对应合法源解；
3. $L_0A$ 行：必须从完整 $(5a)$ 出发，按严格协议验证；
4. 单门不是电路：还需门组合定理。

**固定 $c$（主优先级）**：层级 $c=0$（不可行）、$c=1$（部分）、$c=2$（有结构归约）、
固定 $c$（可能 FPT/XP）、变 $c$（可能 ∃R-hard）。目标 Theorem A：$c=2$ 化为有限个有界次数多项式系统，
再找结构给出可解性；算法用 Grassmannian/Plücker + 现有求解器的谱 gcd。

**归约源排序**：ARM(3) 最接近；static output feedback 次之；一般算术电路/oriented matroid/polynomial matrix completion 再次。

**被忽略方向**：可行集的代数几何（维数/分量/奇异/generic/universality）、描述复杂度（NP？更小的类？）、
实 vs 复、$\mathsf P_{
m ind}$ vs $\mathsf P_{
m full}$、decision vs synthesis。

**判断**：最可能“中间/参数化”（固定 $c$ 可解、整体困难）；不排除 ∃R-完全。
三种情景：A ∃R-完全；B FPT 但整体难；C 更小代数类。

**最有价值的单一实验**：刻画 $u=0$ 时 $D(l)=\det[S;l;lA]$ 能实现的二次型
（rank、signature、射影边界；$xy-zw$ 是否可实现）。正 → 电路；负 → 排除一整类硬度构造。

**五个猜想**：C1 rank-4 signature-(2,2) 门存在；C2 固定 $c$ 有有界复杂度代数描述；
C3 no-drop 在明确假设下成立；C4 谱条件由有限个商空间不变量表达；C5 实/复可行性重合的结构条件。

**优先级**：固定 $c$ 30%；rank-4 门 25%；ARM 20%；精确实验 15%；结构论文 10%。

---

## 9. 2026-11-09 更新：q=2 门路线关闭

- $q=2$：$u\ne0$ 线性；$u=0$ 时 $\omega=2$ 则 $(5b)$ 失败，$\omega\le1$ 则门平凡（245）。
  所以 $q=2$ 不能编码乘法。
- $q=3$：能同时满足 $(5a)(5b)$（244 的显式实例），但单行门被自由行 $x_2$ 吸收；
  要保留门必须让 $x_2$ 被 $x_1$ 强制（耦合行），或改用 ARM(3) 的 gauge/rank-forcing。
- 结论：rank-4 gate 的“单行架构”已关闭；路线 A 只剩耦合/ARM 两个子方向。
