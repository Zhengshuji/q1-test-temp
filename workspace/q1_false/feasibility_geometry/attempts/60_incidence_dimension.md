# incidence variety 的维数与覆盖判据（专家 work package 4）

## 目标

专家 2026-11-04 §5 指出：我们把"Type III 只在 $r_1=p+r$ 出现（4/4）"当候选定理是**过早**的——
支配性只给 $r_1\le p+r$，等号不必然；且 $r>1$ 时比例性会削减定义域。
他要求先把 **incidence variety** 写出来并做维数记账。

## 设想与理由

对 $x\in V=\ker[C;CA]$：$C(\lambda x-Ax)=0$ 自动成立，而 $L_0(\lambda x-Ax)=\lambda L_0x-L_0Ax$。
故 $z=(\lambda I-A)x\in K=\ker[C;L_0]$ $\iff$ $\lambda L_0x=L_0Ax$：

* $r=1$：$\lambda=L_0Ax/L_0x$ 唯一；
* $r\ge2$：仅当**比例性** $L_0Ax\in\operatorname{span}\{L_0x\}$ 时有解，解仍唯一。

于是 $\mathfrak I=\{([x],\lambda,[z])\}$ 是 $\mathbb P(V)$ 上（开集 $\cap$ 比例性轨迹）上的**图**，
$z$ 也随之确定，故
$$\dim\mathfrak I\le\dim\mathbb P(V)=n-r_1-1,\qquad
\dim S\le\min(n-r_1-1,\ n-p-r-1)\quad(S=\text{坏点直线的像}).$$

**覆盖判据**：$d=n-p-q$。$\mathbb P(K)$ 中任一 $\mathbb P^{d-1}$ 与 $s$ 维子簇必交当 $s+(d-1)\ge N$，
$N=\dim\mathbb P(K)=n-p-r-1$ ⟹ $s\ge q-r$。故
$$\dim S\ge q-r\ \Longrightarrow\ \text{每个 }d\text{ 维 }\mathcal Z\subseteq K\text{ 都含坏点直线}\ \Longrightarrow\ \text{该阶整族不可行}$$
（前提 $h=n$ 使 $(5a)$ 自动，见 §3.4）。

## 做法

纸面维数记账（射影维数定理）+ 在具体实例上核对 $r_1$、$\dim\mathbb P(V)$、$\dim\mathbb P(K)$、$q-r$，
以及 Type III 候选是否出现。

## 进展

| 实例 | $q_0$ | $r_1$ | $p+r$ | $\dim\mathbb P(V)$ | $\dim\mathbb P(K)$ | $q_0-r$ | 观察 |
|---|---|---|---|---|---|---|---|
| C4（$n=6,p=r=2$）| 3 | 4 | 4 | 1 | 1 | 1 | **整族** Type III（$\dim S=1=q-r$ ✓）|
| $n=7,p=2,r=2$ seed 4004 | 4 | 4 | 4 | 2 | 2 | 2 | Type III 候选存在 |
| **$n=8,p=3,r=2$ seed 4001** | 3 | **6** | **5** | 1 | 2 | 1 | **也有** Type III 候选（30 中 1）|

第三行直接推翻"$r_1=p+r$ 是 Type III 的必要条件"：**$r_1=6>p+r=5$ 仍然出现 Type III 候选**。
所以此前的"4/4"是**我们搜索族的产物**，不是结构定理。

## 最终结论

1. **$\mathfrak I$ 的维数界**：$\dim\mathfrak I\le n-r_1-1$（图 + 比例性削减），$\dim S\le\min(n-r_1-1,n-p-r-1)$；
2. **覆盖判据**（已证）：$\dim S\ge q-r$（且 $h=n$）⟹ 该阶整族不可行——这是"遮蔽/incidence"判据的正确维数形式；
3. **更正**："Type III $\Rightarrow r_1=p+r$"**不成立**（实测反例）；$r_1=p+r$ 只是 $\mathbb P(V)$ 与 $\mathbb P(K)$
   **等维**的特例（C4 与 $n=7,p=2,r=2$ 实例属此列）；
4. 真正要证的是**余维条件** $\dim S\ge q-r$；而 $\dim S$ 的精确值取决于比例性轨迹的维数——这是留给下一步的量。

## 补充：比例性轨迹的维数（B.13b）

比例性条件是二次形式族 $q_{ij}(x)=v_iu_j-v_ju_i=0$（$u=L_0x$、$v=L_0Ax$）的公共零点集 $P\subseteq V$；
令 $\varepsilon=\dim V-\dim P$，则 $\dim S\le\dim\mathbb P(P)=n-r_1-1-\varepsilon$，故覆盖判据
（$\dim S\ge q-r$，且 $h=n$）的必要条件是
$$q-r+\varepsilon\le n-r_1-1 .$$

实测四实例（精确有理核验比例性是否在 $V$ 上恒成立）：

| 实例 | $\dim V$ | $r_1$ | $q_0$ | 比例性恒成立？| $n-r_1-1$ | $q_0-r$ | 结论 |
|---|---|---|---|---|---|---|---|
| C4（$6,2,2$）| 2 | 4 | 3 | **是**（$\varepsilon=0$）| 1 | 1 | 取等 ⟹ 覆盖可能且**发生** |
| $7,2,2$ | 3 | 4 | 4 | 否 | 2 | 2 | $\varepsilon\ge1$ ⟹ 不可能 |
| $8,3,2$ | 2 | 6 | 3 | 否 | 1 | 1 | 同上（30 中仅 1 个失败）|
| $5,2,1$ | 1 | 4 | 2 | 是 | 0 | 1 | 维数不足 ⟹ 不可能 |

⟹ **正确的整族判据与 $r_1=p+r$ 无关**，而是 $q-r+\varepsilon\le n-r_1-1$，$\varepsilon$ 由 **$A$ 在 $V$ 上的作用**决定。

## 放弃原因

不适用（维数记账与更正完成）。**未做**：比例性轨迹维数的一般公式（$r\ge2$ 时可能严格小于 $n-r_1-1$）。

## 残留价值

* 一个**正确**的整族不可行判据（覆盖 + 维数），以及它的三个具体实例核对；
* 撤回了一条被我们当作"候选定理"的错误规律（$r_1=p+r$），并给出反例；
* 明确了下一步的定量对象：**比例性轨迹的维数**。

## 相关文件

- [docs/02_theorems_proven.md](../../../../docs/02_theorems_proven.md) B.13
- [docs/08_results.md](../../../../docs/08_results.md) §4.11（该行已更正）
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [workspace/for_expert/archive/10_status_and_direction-answer.md](../../../for_expert/archive/10_status_and_direction-answer.md)（专家 §5）
