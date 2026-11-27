# ARM(3) 归约的设计与障碍：第一步表达力引理

> 2026-11-09。专家 62 号建议以仿射秩最小化（ARM，rank 3）为无界 $c$ 硬度的首个目标。
> 本文件记录归约的设计、必须解决的表达力引理与已知障碍。状态：**计划（M0/M1）**，不是定理。

## 目标

规划 $\mathrm{ARM}(3)\to\mathrm{DEC}(q)$ 的归约：给定仿射约束 $\langle A_i,X\rangle=b_i$、$\operatorname{rank}X\le3$，
构造 $(A,C,L_0,q)$ 使“源可行 $\iff$ $\mathrm{DEC}(q)$ 可行”。

## 设想与理由

观察器侧的结构：
$$H=LN,\quad \operatorname{rank}H=\omega=3,\quad H_A=LAN,\quad \ker H\subseteq\ker H_A,\quad
\operatorname{rank}(\lambda H-H_A)=3\ \forall\lambda.$$
若取 $\omega=3$、$k$ 随源实例增长，则 $c=k-3$ 无界，符合“无界 $c$”的目标。
自然的候选变量是压缩矩阵 $H$（或 $Z:H\to\mathbb C^q$），但 $H$ 不是任意矩阵：
它必须来自 $L$，且与 $H_A$ 耦合。

## 做法：需要证明的表达力引理

**引理（目标）**：存在多项式时间构造，把 ARM(3) 的每个仿射约束 $\langle A_i,X\rangle=b_i$ 实现为
观测器数据 $(A,C,L_0)$ 上的一条**线性方程**（作用于某个可识别的变量，如 $Z$ 或 $H$ 的坐标），
且：
1. 每个源变量对应一个可识别的观测器坐标；
2. 每条仿射约束对应一条线性方程；
3. $\operatorname{rank}X\le3$ 对应 $\operatorname{rank}H=3$（或 $Z$ 的秩条件）；
4. 谱条件 $\operatorname{rank}(\lambda H-H_A)=3\ \forall\lambda$ **自动满足**（例如 $B_*$ 在每个特征空间单射）；
5. 不同约束/变量不产生非预期的交互；
6. 反向：每个可行的观测器实例恢复一个满足 ARM 的 $X$。

## 已知障碍

1. **$H$ 没有任意仿射约束**：$H=LN$ 的自由度是 $L$；可容许条件只约束 $H_A$，不约束 $H$ 的任意线性泛函。
   因此 ARM 的 $\langle A_i,X\rangle=b_i$ 不能直接对应 $H$ 的线性方程。
2. **$H$ 与 $H_A$ 同源**：$H_A=LAN$，不能独立选择；这限制了可实现的 $(H,H_A)$ 对。
3. **谱条件**：即便几何可行，铅笔可能恒坏（191/189）；构造必须让 $B_*$ 在每个特征空间单射。
4. **提升/行独立**：$\mathsf P_{\rm ind}$ 下还要 $d'_C\ge\dim\ker Z_{\rm pair}$。
5. **变量识别**：ARM 的 $X$ 是任意的 $m\times n$ 矩阵；观测器侧的可识别变量可能是 $Z$ 或 $H$ 的坐标，
   需要一个显式的线性编码。

## 第一步实验（待做）

最小 gadget：能否用 $(A,C,L_0)$ 让一条仿射约束 $\langle A_1,X\rangle=b_1$ 对应 $H$ 的一个线性方程？
- 尝试把 $A_1$ 实现为 $L_0$ 的某行与 $A$ 的乘积（如 $L_0A^k$），使 $H$ 的某个坐标被固定；
- 若只能固定 $H$ 的行空间/核，而不能固定单个坐标，则记录该限制。

## 进展

* 归约目标与六条要求写成；
* 五个障碍列出；
* 最小 gadget 实验列为下一步。

## 最终结论（计划）

* ARM(3) 是最接近的硬度源，但“$H$ 与 $H_A$ 同源”是核心障碍；
* 第一个要证的是表达力引理：观测器能否实现足够一般的仿射约束；
* 若不能，需找替代源问题（ETR 算术电路）或记录结构性限制。

## 放弃原因

* 尚未做最小 gadget 实验；
* 未验证谱条件自动满足的构造；
* 无具体归约。

## 残留价值

* 归约的清晰规格与障碍清单；
* 为下一步 gadget 实验提供靶子。

## 相关文件

* [attempts/194](../../multiplication_gate/attempts/194_62_verdict_implementation.md)（专家 62 号的硬度建议）
* [attempts/171](../../../q1_false/c_stratification/attempts/171_Buv_rank_strata.md)（chart 的二次项）
* [attempts/152](../../../q1_false/c_stratification/attempts/152_lift_completion_fixed_l0.md)（提升）

## 状态

* 计划：**[M0/M1]**，无定理。
