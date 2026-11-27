# 353 乘法门再试：钉住引理与"钉住 ⟹ 线性、不钉住 ⟹ 逃逸"的权衡

> 用户指定：试乘法门，并先看前史。
> **结论**：没有造出 sound 乘法门；但得到一条**钉住引理**（层可以被固定行 + $\dim(A K_0)$ 夹死）
> 与一条**权衡**：钉住后 $(5a)$ 退化成线性条件（只能编**齐次线性**约束，非齐次仿射需单独构造），不钉住则 307 的逃逸成立。
> 这解释了 303 为什么失败，也说明"钉住"救不了乘法，但能提供 ARM 翻译所需的**齐次线性**限制（非齐次仿射约束仍需单独构造，见 98 号 §6.2 的更正）。

## 目标

1. 清点乘法门的前史。
2. 判断"把秩层钉死"能否使 303 的乘法门变 sound。

## 设想与理由

307 号已把 soundness 拆成三条义务（C 完备 / S 任何可行 $R$ 都解码 / R 层被钉住），
并指出 rank forcing 的失败模式：自由行跳到**满行空间**使 $(5a)$ 变成空条件。
80 号给的诊断是要"一个全局行空间不变量 + 局部坐标子空间"（其 §5.4 六步），缺口在"第 6 步：
任何额外自由行要么落在 $W$ 里、要么违反 $(5b)$"。

于是问题变成：**能不能让 $(5b)$ 惩罚"额外行"？** 我们刚在 $c=1$ 线里得到的 $\lambda=0$ 障碍正好是这种惩罚工具。

## 前史清点（乘法门）

| # | 文件 | 做了什么 | 结果 |
|---|---|---|---|
| 1 | [303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md) | 79 号的完整乘法门：$H=[e;e;v_x;0]$、$H_A=[0;e;(0,y,z);(0,\beta,w)]$，证 $(5a)\iff z=xy$、$(5b)\iff\beta\ne0$ | **full-observer realization**（在指定见证下精确） |
| 2 | [306](306_80_soundness_correction.md) | 80 号反例：$R=0$ 时 $(5a)(5b)$ 仍成立但不约束 $z=xy$ | **unsound** |
| 3 | [307](../../../q1_false/decision_algorithms/attempts/307_soundness_obligations.md) | 三条义务 C/S/R；rank forcing 的失败：自由行跳到满行层，$(5a)$ 变空 | 结构分析 |
| 4 | [308](308_soundness_expressiveness.md)、[309](../../../q1_false/decision_algorithms/attempts/309_port_rigidity.md) | 表达力与 port 刚性；no-go 只覆盖特定架构 | 部分 no-go |
| 5 | [80 号答复](../../../for_expert/archive/80_wiring_copy_gadget-answer.md) | 全局设计程序（§5.4 六步）+ 位移脚手架（§5.5） | **缺口 = 第 6 步** |
| 6 | [83/315](../../arm_reduction/attempts/315_83_verdict_roadmap.md) | 判局部乘法门为"不值得再投"，转 ARM | 停 |

## 做法：钉住引理

记 $\omega_0=\operatorname{rank}H_0$（固定行给出的秩），$H=LN$、$H_A=LAN$。

> **引理（钉住）.** 若 $\dim(A K_0)=\omega_0$，则**任何**满足 $(5a)\wedge(5b)$ 的 $R$ 都满足
> $$\operatorname{rank}H=\omega_0,\qquad \operatorname{row}H=\operatorname{row}H_0 .$$

*证明.* (i) $\operatorname{row}H\supseteq\operatorname{row}H_0$ ⟹ $\operatorname{rank}H\ge\omega_0$。
(ii) $(5b)$ 在 $\lambda=0$ 处给 $\operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H$，即 $\operatorname{rank}H_A=\operatorname{rank}H$；
而 $\operatorname{rank}H_A=\operatorname{rank}(LAN)\le\dim(A K_0)=\omega_0$。故 $\operatorname{rank}H\le\omega_0$。
(iii) 两式合并得 $\operatorname{rank}H=\omega_0$；又 $\operatorname{row}H_0\subseteq\operatorname{row}H$ 且两者维数相同，故相等。$\square$

**这是 307 的"R 义务"的一个显式实现**：层被固定行（下界）与 $\dim(A K_0)$（上界）夹死。

## 权衡：钉住之后 $(5a)$ 变线性

钉住后 $\operatorname{row}H=W_0:=\operatorname{row}H_0$，于是

$$(5a)\iff\text{每个自由行的 }H_A\text{ 行}\in W_0 .$$

而自由行的对 $(h_i,g_i)$ 只能取自 $\mathcal T=\operatorname{row}[N\ AN]$，故可行集变成
$$\{(h_i,g_i)\}_{i}\in\bigl(\mathcal T\cap(W_0\times W_0)\bigr)^{m}\ \text{再叠加 }(5b).$$
**前一部分是线性条件**——也就是说：钉住把 $(5a)$ 的非线性全部消掉了。

- **好处**：这恰好是 352 说的"q1 缺的仿射控制"——**钉住块可以编码齐次线性限制**（非齐次仿射约束如 $x_1+x_2=1$ 需单独构造）；
- **坏处**：乘法是**非线性**的，钉住之后 $(5a)$ 不再能表达它；能表达乘法的只剩 $(5b)$，
  而 $(5b)$ 是一个**开条件**（铅笔正则），它逼不出等式。

这就解释了 303 的失败：**它没有钉住**，于是自由行可以加方向把 $\operatorname{row}H$ 撑大、令 $(5a)$ 变空（$R=0$ 正是最极端的一例）。
而钉住能修好"逃逸"，却同时把表达力降到线性——**要乘法就得在未钉住的层里做**，那正是 307 说会逃逸的地方。

## 进展

1. 前史 6 条已清点（303 实现 / 306 unsound / 307 三义务 / 308-309 部分 no-go / 80 六步程序 / 83 停）。
2. **钉住引理已证**（秩计数，三步）：$\dim(A K_0)=\operatorname{rank}H_0$ ⟹ 所有可行 $R$ 都有 $\operatorname{row}H=\operatorname{row}H_0$。
3. **权衡已明确**：钉住 ⟹ $(5a)$ 线性（可编齐次线性约束，不可编乘法）；不钉住 ⟹ $(5a)$ 非线性但逃逸（307）。
4. 因此"钉住救 303"这条路**只能救一半**：能淘汰 $R=0$ 与所有"加行"逃逸，但乘法关系随之失去表达力。

## 最终结论

1. **没有 sound 乘法门**；但得到一个明确的二分：
   $$\text{钉住}\ \Longrightarrow\ \text{线性（齐次）表达力};\qquad
   \text{不钉住}\ \Longrightarrow\ \text{非线性表达力但逃逸}.$$
2. 这对两条线都有用：
   - **ARM 翻译**（352）：钉住块正好提供它缺的**齐次线性**限制能力（非齐次仿射仍缺）；
   - **乘法门**：必须做在未钉住层，且需要一个新的"惩罚额外行"机制（80 的第六步），
     我能想到的候选惩罚就是 $\lambda=0$ 障碍的反向使用（让 $\dim(A K_0)$ 严格小于目标层），但那与钉住矛盾——**这正是困难所在**。
3. 下一步（若继续）：**混合块**——钉住块编齐次线性约束、未钉住块编乘法，用 port 把两者的行空间接起来；
   80 号 §5.4 的六步框架能容纳这种混合，但第 6 步仍要重做。

## 放弃原因

- 没有造出乘法门；也没有证明"钉住 + 非线性"不可能（只是给出权衡）。
- 混合块的构造没有开始；80 号的第 6 步仍空。
- 钉住引理只在"$\dim(A K_0)=\omega_0$ 恰好相等"时成立；$\dim(A K_0)>\omega_0$ 时只能给上界。

## 残留价值

- **钉住引理**（三步秩计数，已证）：层可以被夹死，这是 307 那个"R 义务"的显式实现；
- **权衡**："钉住 ⟹ 线性"解释了 303 的失败与"钉住救不了乘法"；
- 把 352 与乘法门两条线接上：钉住块给齐次线性限制（正是 ARM 翻译缺的一半；非齐次仿射仍需构造）。

## 相关文件

- [303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md)、[306](306_80_soundness_correction.md)、[307](../../../q1_false/decision_algorithms/attempts/307_soundness_obligations.md)、[308](308_soundness_expressiveness.md)、[309](../../../q1_false/decision_algorithms/attempts/309_port_rigidity.md)
- [80 号答复](../../../for_expert/archive/80_wiring_copy_gadget-answer.md)
- [315](../../arm_reduction/attempts/315_83_verdict_roadmap.md)（83 号：停局部门、转 ARM）
- [352](../../arm_reduction/attempts/390_arm_translation_analysis.md)（ARM 翻译缺线性/仿射控制）
- [337](../../../q1_false/c_stratification/attempts/337_lambda0_obstruction.md)（$\lambda=0$ 障碍，即本引理用到的上界）

## 状态

- 前史清点：**[完成]**。
- 钉住引理：**[已证-纸面]**（秩计数）。
- 权衡：**[已证-纸面]**（结论是"$(5a)$ 在钉住后是线性条件"）。
- 乘法门：**[未得到]**；已定位到"未钉住层 + 惩罚额外行"。
