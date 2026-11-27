# 硬度/增广线索引（文档 390–427）

> 本文件是**硬度线**（q1 的不可行性来源）的索引：做什么、已证什么、撤回过什么、卡在哪、下一步。
> **编号约定**：本线文档占用 **390–427**（连续、按时间顺序）。
> `workspace/augmentation_family/attempts/` 下另有**另一条线**（$c=1$/图卡/判定器，编号 3xx），
> 由其他人推进；两边不共用编号，互不覆盖。

---

## 一、这条线在做什么

问：$(5a)(5b)$ 的**可行集**能不能承担一个 NP-难的归约？
具体路线：把源问题编码进实例数据 $(A,C,L_0)$，让 q1 的"可行"等价于源问题的"可满足"。

判据（专家 100 号给的形态）：$K_0=\ker[C;CA]$、$H=LN$、$H_A=LAN$、$\omega=\operatorname{rank}H$；
$$(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad (5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda .$$

---

## 二、已证 / 已验证的结论

| # | 结论 | 等级 | 文档 |
|---|---|---|---|
| 1 | 载体界 $d_0\le n-p$ ⟹ 逐行忠实编码不可能（$p\ge1$） | 已证 + 7 模式 | [390](../q1_true/arm_reduction/attempts/390_arm_translation_analysis.md) |
| 2 | **钉住引理**：$\dim(AK_0)=\operatorname{rank}H_0=\omega_0$ ⟹ 任何可行 $R$ 有 $\operatorname{row}H=\operatorname{row}H_0$ | 已证 | [391](../q1_true/multiplication_gate/attempts/391_multiplication_pinning.md) |
| 3 | 钉住 ⟹ 可行集 = 线性 ∩ Zariski 开 ⟹ **表达力恰为线性**（编不了乘法） | 已证 | [392](../q1_true/multiplication_gate/attempts/392_pinned_gadgets_cannot_multiply.md) |
| 4 | 极大性引理 | 已证 | [393](../q1_false/c_stratification/attempts/393_maximality_lemma.md) |
| 5 | **核等式引理**：可行 ⟹ $\ker H=\ker H_A$（同零列、同子集秩） | 已证（专家复核） | [406](../q1_false/decision_algorithms/attempts/406_expert100_audit.md) |
| 6 | **$k$ 块合取定理**：锚定直和块，$m=k$ 时可行 $\iff\prod t_i\ne0$ | 已证（任意 $k$） | [400](../q1_true/multiplication_gate/attempts/400_and_composition.md)…[403](../q1_true/multiplication_gate/attempts/403_k_block_soundness.md)、[406](../q1_false/decision_algorithms/attempts/406_expert100_audit.md) |
| 7 | **纤维级刚性**：可行集在每个活纤维 $M_W$ 里 Zariski 开且稠密 ⟹ 关系在该纤维上恒成立 | 已证（专家 100 修正版） | [399](../q1_false/c_stratification/attempts/399_relation_gadgets_impossible.md) |
| 8 | **见证侧只能开**：$q$ 在所有可行 $R$ 上为零 ⟹ $q$ 在活纤维上恒零 ⟹ 筛不掉点 | 已证 | [414](../q1_false/c_stratification/attempts/414_witness_side_vacuous.md) |
| 9 | **等式门**：可行 $\iff t=0$（$\dim(AK_0)=1$ 只留层 1） | 已证 + 5/5 | [409](../q1_false/c_stratification/attempts/409_usable_equation_gate.md) |
| 10 | **层 1 条件的行列式形式**：$\det\begin{pmatrix}a_1&a_2\\ t_1b_1&t_2b_2\end{pmatrix}=0$ | 已证 | [412](../q1_true/multiplication_gate/attempts/412_booleanity_gate.md) |
| 11 | **布尔性门**：可行 $\iff x(x-1)=0$ | 已证 + 5/5 | [412](../q1_true/multiplication_gate/attempts/412_booleanity_gate.md) |
| 12 | **等式合取**：可行 $\iff x=0\wedge y=0$ | 已证 + 4/4 | [413](../q1_false/c_stratification/attempts/413_equation_conjunction_and_mismatch.md) |
| 13 | **方阵铅笔障碍**：$r=k=\omega$ ⟹ 谱条件不可能 | 已证 | [411](../q1_true/multiplication_gate/attempts/411_expert102_audit.md) |
| 14 | **$\omega=0$ 平凡层**：$L_0[N\ AN]=0$ ⟹ 恒可行 ⟹ $r_0=0$ 的实例对归约无用 | 已证 | [422](../q1_false/c_stratification/attempts/422_trivial_layer.md) |
| 15 | **$\omega=1$ 钉死**：非零固定 $h^0$ 把 $W$ 钉成唯一点 | 已证 | [421](../q1_false/c_stratification/attempts/421_omega1_excluded.md) |
| 16 | $(5a)\Rightarrow\operatorname{rank}P(\lambda)\le\omega$ **自动**；方阵 $r=k=\omega$ 必坏（FTA） | 已证 | [427](../q1_false/c_stratification/attempts/427_criterion_validated.md) |
| 17 | **活跃子空间判据**（专家 104）：可行 $\iff\exists W$ 满足相容 + 秩补全 + 生成铅笔 $\gcd=1$ | 已证（判据形式） | [417](../q1_false/decision_algorithms/attempts/417_expert104_audit.md) |
| 18 | **单 $W$ 判据**（左零空间参数化，$T_W=\mathcal S\cap(W\oplus W)$） | 精确验证 | [426](../q1_false/decision_algorithms/attempts/426_retract_multi_active.md)、[427](../q1_false/c_stratification/attempts/427_criterion_validated.md) |
| 19 | 活跃集**离散且受参数控制**；布尔值 $\leftrightarrow$ $\mathbb P^1$ 的两个坐标点 | 精确验证 | [419](../q1_true/multiplication_gate/attempts/419_active_set_discrete.md) |
| 20 | **完整层表**（含 $\omega=0$）：布尔性门判定对其成立 | 精确验证 | [423](../q1_true/multiplication_gate/attempts/423_layer_table_check.md) |

---

## 三、撤回清单（都留了记录）

| # | 被撤回的说法 | 原因 | 文档 |
|---|---|---|---|
| 1 | "任意次数的关系型 gadget 都不可能" | 过度概括 ⟹ 改为**纤维级刚性** | [399](../q1_false/c_stratification/attempts/399_relation_gadgets_impossible.md) |
| 2 | "只给开条件 ⟹ 无硬度" | 纤维内开 ≠ 全局；SAT 也是构造集 | [405](../q1_false/c_stratification/attempts/405_layer_separation_and_equations.md) |
| 3 | **Route A（层 2 遮蔽）** | $2\times2$ 铅笔在层 2 必坏；该实例每层都不可行 | [411](../q1_true/multiplication_gate/attempts/411_expert102_audit.md) |
| 4 | 硬度线"收束"（源变量两侧都不通） | 错在把"约束自动成立"当成"归约不可能" | [415](../q1_false/c_stratification/attempts/415_hardness_line_closure.md) → [416](../q1_true/multiplication_gate/attempts/416_selfcheck_closure_retracted.md) |
| 5 | $\operatorname{Gr}(2,3)$ 上"2 个活跃 $W$" | **采样假象**：自由行没落在 $T_W$ 里 | [425](../q1_false/c_stratification/attempts/425_multi_active_found.md) → [426](../q1_false/decision_algorithms/attempts/426_retract_multi_active.md) |
| 7 | "$\omega<k$ 的层本质退化"（解释搜索全空） | $\operatorname{rank}P\le\omega$ 由 $(5a)$ **自动**成立，不是额外退化；全空原因**未查明** | [427](../q1_false/c_stratification/attempts/427_criterion_validated.md) |
| 6 | "$r_0=0$ 情形未定" | 解决：正是平凡层 ⟹ 恒可行 | [421](../q1_false/c_stratification/attempts/421_omega1_excluded.md) → [422](../q1_false/c_stratification/attempts/422_trivial_layer.md) |

---

## 四、当前框架（下一步都在这上面做）

$$\text{可行}\iff\exists W\in\operatorname{Gr}(\omega,k):\
\text{(i) 固定行相容}\ \wedge\ \text{(ii) 秩补全}\ \wedge\ \text{(iii) 生成铅笔}\ \gcd=1 .$$

三层结构：
$$\underbrace{(A,C,L_0)}_{\text{数据}}\longrightarrow \mathcal S=\operatorname{row}[N\ AN]\longrightarrow \mathcal T_W=\mathcal S\cap(W\oplus W)\longrightarrow \text{生成铅笔}.$$

**纪律**：任何可行性判定必须给**完整层表**（$\omega=0,1,2,\dots$），不许静默跳过 \([423]\)(423_layer_table_check.md)。

---

## 五、开放问题（按重要性）

1. **多活跃 $W$**（里程碑 4）：能否让一个实例的活跃集恰为若干孤立点（理想 $2^s$ 个，对应 $2^s$ 个源赋值）？
   已知：$\omega=1$ 不可能（钉死）；随机实例只适合顶层 $\omega=k$；非顶层须用 $c=1$ 类结构化实例。
2. **$W$ 上的布尔性**（里程碑 4 的另一半）：把布尔条件放在 Grassmann 坐标上（专家 104 的建议）。
3. **系数编码型归约的表达力**：$\{(A,C,L_0):\exists R\}$ 这一族到底多大（[416](../q1_true/multiplication_gate/attempts/416_selfcheck_closure_retracted.md)）。
4. **均匀归约**（里程碑 5）：多项式规模、常数显式。

---

## 六、文档地图（按主题）

| 主题 | 文档 |
|---|---|
| 载体界与翻译 | [390](../q1_true/arm_reduction/attempts/390_arm_translation_analysis.md) |
| 钉住与乘法不可能 | [391](../q1_true/multiplication_gate/attempts/391_multiplication_pinning.md)、[392](../q1_true/multiplication_gate/attempts/392_pinned_gadgets_cannot_multiply.md)、[393](../q1_false/c_stratification/attempts/393_maximality_lemma.md)、[397](../q1_true/multiplication_gate/attempts/397_no_go_all_strata.md) |
| CLP（单行/反例） | [395](../q1_true/multiplication_gate/attempts/395_clp_single_row.md)、[396](../q1_true/multiplication_gate/attempts/396_clp_counterexample.md) |
| 合取（AND，任意 $k$） | [400](../q1_true/multiplication_gate/attempts/400_and_composition.md)、[401](../q1_true/multiplication_gate/attempts/401_and_soundness.md)、[402](../q1_true/multiplication_gate/attempts/402_two_block_soundness.md)、[403](../q1_true/multiplication_gate/attempts/403_k_block_soundness.md) |
| OR / NOT | [404](../q1_true/multiplication_gate/attempts/404_or_not.md) |
| 核等式引理、纤维级刚性、$k$ 块定理 | [399](../q1_false/c_stratification/attempts/399_relation_gadgets_impossible.md)、[406](../q1_false/decision_algorithms/attempts/406_expert100_audit.md)、[414](../q1_false/c_stratification/attempts/414_witness_side_vacuous.md) |
| 层、遮蔽、等式门 | [408](../q1_true/multiplication_gate/attempts/408_equation_gate_layer_masking.md)、[409](../q1_false/c_stratification/attempts/409_usable_equation_gate.md)、[407](../q1_false/c_stratification/attempts/407_mixed_anchor_equations.md) |
| 析取 | [410](../q1_false/c_stratification/attempts/410_disjunction_obstruction.md)、[404](../q1_true/multiplication_gate/attempts/404_or_not.md) |
| 布尔性 / 等式合取 | [412](../q1_true/multiplication_gate/attempts/412_booleanity_gate.md)、[413](../q1_false/c_stratification/attempts/413_equation_conjunction_and_mismatch.md) |
| 活跃子空间（判据、实测、撤回） | [417](../q1_false/decision_algorithms/attempts/417_expert104_audit.md)、[418](../q1_true/multiplication_gate/attempts/418_active_subspace_first_check.md)、[419](../q1_true/multiplication_gate/attempts/419_active_set_discrete.md)、[420](../q1_false/decision_algorithms/attempts/420_multiactive_tension.md)、[424](../q1_false/c_stratification/attempts/424_m4_probe.md)、[425](../q1_false/c_stratification/attempts/425_multi_active_found.md)、[426](../q1_false/decision_algorithms/attempts/426_retract_multi_active.md)、[427](../q1_false/c_stratification/attempts/427_criterion_validated.md) |
| 层表与平凡层 | [421](../q1_false/c_stratification/attempts/421_omega1_excluded.md)、[422](../q1_false/c_stratification/attempts/422_trivial_layer.md)、[423](../q1_true/multiplication_gate/attempts/423_layer_table_check.md) |
| 自查与更正 | [416](../q1_true/multiplication_gate/attempts/416_selfcheck_closure_retracted.md)、[426](../q1_false/decision_algorithms/attempts/426_retract_multi_active.md) |
| 专家审计 | [394](../q1_true/multiplication_gate/attempts/394_expert98_audit.md)、[398](../q1_false/decision_algorithms/attempts/398_expert99_audit.md)、[406](../q1_false/decision_algorithms/attempts/406_expert100_audit.md)、[411](../q1_true/multiplication_gate/attempts/411_expert102_audit.md)、[417](../q1_false/decision_algorithms/attempts/417_expert104_audit.md) |

---

## 七、专家往来（全部已成对归档）

| 编号 | 主题 | 落实文档 |
|---|---|---|
| 98 | 合取/乘法门审计 | [394](../q1_true/multiplication_gate/attempts/394_expert98_audit.md) |
| 99 | 全层 no-go 审计 | [398](../q1_false/decision_algorithms/attempts/398_expert99_audit.md) |
| 100 | 纤维级刚性、核等式引理、$k$ 块定理 | [406](../q1_false/decision_algorithms/attempts/406_expert100_audit.md) |
| 101 | 超平面层（另一条线） | — |
| 102 | 等式门与析取墙 | [411](../q1_true/multiplication_gate/attempts/411_expert102_audit.md) |
| 103 | 超平面参数化（另一条线） | — |
| 104 | 原语清单与活跃子空间刻画 | [417](../q1_false/decision_algorithms/attempts/417_expert104_audit.md) |

归档位置：`workspace/for_expert/archive/<NN>_<topic>.md` 与 `-reply.md`。

---

## 八、验证脚本

`tools/verification/` 下与本线相关：`c335_lambda_movement.py`（共享判定器）、
`c362_and_composition.*`、`c363_*`、`c365_*`、`c366_or_not_gates.m`、`c369_*`、
`c371_equation_gate_v2.py`、`c372_booleanity_gate.py`、`c373_equation_conjunction.py`、
`c374_active_subspace_criterion.py`、`c375_layer_table.py`。

---

## 状态

- 本索引：**[整理]**（2026-11-18 编号整理后建立）。
- 结论与撤回：见上两表（每条都点到文档）。
- 开放问题：见 §五（4 条）。
