# 专家 76 号裁决落实：incidence 不是决定性障碍，改攻 rank-one 截面

> 2026-11-09。76 号答复确认 266 的分解正确，但指出：
> incidence 与仿射方程的型不匹配只否定“一方程一 incidence”的朴素做法，
> 不否定整个路线；更好的源问题是** rank-3 matroid realization**（Kim–de Mesmay–Miltzow，∃R-完全）。
> 路线 A 在 $q=4,r_0=2,\\omega=3$ 下的核心对象是
> $$\\mathcal V\\cap\\{Z:\\operatorname{rank}Z\\le1\\},$$
> 其中 $\\mathcal V$ 是两个自由行诱导的线性像。状态：**M3（专家裁决）**。

## 目标

落实 76 号答复，确定路线 A 的下一步对象。

## 设想与理由

专家确认：
- $AN=NM+E$ 分解正确；$N^+$ 合法；$E$ 依赖补空间选择；
- 单个 incidence 不是任意仿射超平面，但 incidence 系统（Matroid/Projective）可以编码算术；
- 不要直接嵌 ARM(3)，改用 rank-3 matroid realization；
- $(5b)$ 只作 guard（排除退化分支），不要用它编码乘法；
- 算法侧（固定 $\\kappa_{\\rm obs}$）独立推进。

## 做法：逐条落实

### 1. 分解与 rank-one 几何

$q=4$、$r_0=2$、$\\operatorname{rank}H_0=2$、$\\operatorname{rank}H=3$。
令 $S_0=\\operatorname{row}H_0$、$U=\\operatorname{row}H$、$V=\\mathbb C^k/S_0$、$\\pi$ 商映射。
则 $U/S_0$ 是 $V$ 中的一条线，且
$$\\pi(y_1),\\pi(y_2),\\pi(z_1),\\pi(z_2)\\ \\text{落在同一条线}\\ L\\subset V,$$
即
$$\\operatorname{rank}\\begin{bmatrix}\\pi(Y)\\\\ \\pi(RE)\\end{bmatrix}\\le1.$$
这是 rank-one determinantal 条件。

### 2. 固定行的二分

$T=\\operatorname{span}(\\operatorname{row}H_0,\\operatorname{row}H_{A,0})$。
- $\\dim T=3$：$U=T$ 固定，条件是线性包含，不太可能给硬度；
- $\\dim T=2$：$U$ 是含 $T$ 的变量三平面，$U/T$ 是 $\\mathbb P(V)$ 中的点；这是唯一有希望的情形。

### 3. 常数/规范化的隐患

$\\pi$ 把 $S_0$ 杀掉，所以 Case II 的 rank-one 条件是**齐次**的；
要得到 $z=xy$ 需要某个坐标固定为 1。常数可能来自：
- 非商方向的固定行（但 $\\pi$ 已杀掉 $S_0$）；
- 图卡规范化（某变量 $=1$）；
- Case I 的固定 $H_{A,0}$。

这与 234/237 的“常数/规范”问题同型，需要专门处理；专家也把“projective normalization”列为待研究项。

### 4. 下一步（专家建议）

1. **分类 common-line variety**：对给定 $(N,E)$ 计算
   $$\\mathcal V=\\left\\{\\begin{bmatrix}\\pi(RN)\\\\ \\pi(RE)\\end{bmatrix}:R\\right\\},$$
   研究 $\\mathcal V\\cap\\{\\operatorname{rank}\\le1\\}$ 的参数化；
2. **两门组合测试**：能否用同一自由变量实现两个乘法关系（variable sharing）；
3. **rank-3 matroid realization** 作为源问题；
4. $(5b)$ 仅作 guard；
5. 算法侧（261/262）独立推进。

## 进展

* 76 号的分解确认与战略修正；
* rank-one 截面对象的明确定义；
* 常数/规范化隐患的记录；
* 下一步清单。

## 最终结论

* 路线 A 不关闭，但不再直接嵌 ARM(3)；
* 新目标是 rank-one 线性截面 + incidence/Matroid 源；
* 常数/图卡问题是当前最大技术障碍。

## 放弃原因

* 未分类 $\\mathcal V\\cap\\{\\operatorname{rank}\\le1\\}$；
* 未做两门组合；
* 未接 Matroid realization。

## 残留价值

* 明确的下一步对象；
* 与专家建议对齐；
* 避免继续“一方程一 incidence”的死路。

## 相关文件

* [76 答复](../../../for_expert/archive/76_routeA_summary-answer.md)
* [attempts/266](../../../q1_false/decision_algorithms/attempts/266_q4_r0_decomposition.md)
* [attempts/268](../../../q1_false/decision_algorithms/attempts/268_routeA_incidence_obstruction.md)

## 状态

* 裁决落实：**[M3]**。
* rank-one 截面分类：**[未做]**。
