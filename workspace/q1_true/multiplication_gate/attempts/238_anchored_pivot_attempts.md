# (5a) 门（九）：固定枢轴的三种尝试与失败

> 2026-11-09。按专家 71 号 Step 2（固定枢轴、保持 rank $M_0$ 恒定），试了三种设计：
> （1）改 $L_0$ 使 $\operatorname{rank}M_0$ 恒定；（2）对角 $A$ 的显式块；（3）随机搜索“锚定二次”行列式。
> 都没有得到 $\det=d-bc$ 或 $1\cdot z-x y$ 形式。状态：**精确计算 + 负结果**。

## 目标

构造固定枢轴的 anchored 门：
$$\det\begin{bmatrix}1&x\\y&z\end{bmatrix}=z-xy,$$
其中 $1$ 由 $A,C,L_0$ 固定，且 $\operatorname{rank}M_0$ 对所有 $L$ 恒定（使 $\det=0\iff(5a)$ 全局成立）。

## 设想与理由

234 的门 $\det M=ad-bc$ 需要 $a\ne0$ 才能解码；专家建议把 $1$ 固定进行列式，
并把 $M_0$ 的秩钉住，避免 $(c,d)=0$ 时的 rank 跳变。

## 做法

### 1. 改 $L_0$ 固定秩

取 234 的 $A$、$C=e_5$，改 $L_0$：
- $L_0=e_1+e_3$：$\operatorname{rank}M_0=4$ 恒定（含 $c=d=0$），但
  $$\det M=ab+4ad+b^2-bc+cd,$$
  不可约二次型，不是门；
- $L_0=e_1+e_4$：同样 rank 恒定，$\det=-a^2-ab-3ac+ad-bc-c^2$；
- $L_0=e_1+e_3+e_4$：另一个不可约二次型。

### 2. 对角 $A$ 的显式设计

取 $A=\operatorname{diag}(0,1,1,1,0)$，则 $lA=(0,b,c,d,0)$。
对 $L_0\in\{e_1,e_1+e_3,e_1+e_4\}$、$C\in\{e_5,e_4,e_2+e_5,\dots\}$ 枚举：
- 部分组合 $\operatorname{rank}M_0=4$ 恒定；
- 但 $\det M$ 是**单项式**（如 $-ad$、$ac$、$-d(a-e)$），不是门。

### 3. 随机“锚定二次”搜索

$L_0=e_1+e_3$、$C=e_5$，500 个随机 $A$；要求 $\det M$ 只含 $d$、$bc$、常数项
（即 $\alpha d+\beta bc+\gamma$）。**无结果**。

## 进展

* 找到 $\operatorname{rank}M_0$ 恒定的 $L_0$ 修改（$e_1+e_3$ 等）；
* 但行列式变成不可约二次型/单项式，失去门结构；
* 500 例锚定二次搜索无果。

## 最终结论

* 固定秩与“门形式”在这组 $n=5$、$q=2$ 的设计里**不能同时满足**；
* 需要更大的 $n$（$n\ge6$）或真正的 Schur 枢轴块；
* 下一步：把 $L_0=e_1+e_3$ 的恒定秩性质与 234 的 $ad-bc$ 结构结合，或用 $n=6$ 搜索。

## 放弃原因

* 未找到 anchored 门；
* 只试了有限 $L_0,C,A$；
* 未做 $n=6$。

## 残留价值

* 恒定秩的 $L_0$ 选择；
* 三种失败模式的清晰记录；
* 为 $n=6$ 提供起点。

## 相关文件

* [attempts/234](234_explicit_gate.md)、[237](237_71_verdict.md)
* [for_expert/archive/71 answer](../../../for_expert/archive/71_explicit_gate_branches-answer.md)

## 状态

* 负结果：**[精确计算 + 搜索]**。
* Anchored 门：**[未找到]**。
