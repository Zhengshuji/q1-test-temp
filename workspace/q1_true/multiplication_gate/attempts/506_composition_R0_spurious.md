# 506 组合接口的第一步：303 B 的 $R=0$ 伪解与 soundness 条件

> 2026-11-27。rank_gates 冻结后转向 multiplication_gate（ChatGPT 建议：先验证已有 sound gadget 能否组合）。
> 本文件把 306 的“$R=0$ 伪解”写成显式引理，并给出组合 soundness 的必要条件。
> 状态：**[已证-纸面]**。

## 目标

为 296（非零门）与 303 B（乘法门）建立组合接口；第一个可检验量是
**组合后是否存在非目标自由度使 q1 可行但乘法约束不成立**（ChatGPT）。

## 303 B 的 $R=0$ 伪解（引理）

取 303 B 的数据：$k=3$、$n=9$、$p=3$，
$$C=[I_3\ 0\ 0],\qquad A=\begin{bmatrix}0&0&I_3\\0&0&0\\0&I_3&0\end{bmatrix},$$
$H_0=[e;e]$、$H_{A,0}=[0;e]$，$H$ 的第 3、4 行是 $v_x=(0,1,x)$ 与 $0$，
$H_A$ 的第 3、4 行是 $(0,y,z)$ 与 $(0,\beta,w)$，其中 $x,y,z,\beta,w$ 都是 $R$ 的条目。

令 $R=0$。则
$$H=\begin{bmatrix}e\\e\\0\\0\end{bmatrix},\qquad H_A=\begin{bmatrix}0\\e\\0\\0\end{bmatrix},\qquad
P(\lambda)=\begin{bmatrix}\lambda e\\(\lambda-1)e\\0\\0\end{bmatrix}.$$
- $\operatorname{rank}H=1$，$\operatorname{rank}P(\lambda)=1$ 对一切 $\lambda$（$\lambda$ 与 $\lambda-1$ 不同时为零）；
- $(5a)$：$\ker H=\ker e=\ker H_A$，成立；
- 所以 **$(5a)\wedge(5b)$ 对任意 $x,y,z$ 成立**，门约束 $z=xy$ 完全不被强制。$\square$

## 组合 soundness 的必要条件

由引理，乘法门的 $(5a)$ 只在“门的自由行非零”时才给出 $z=xy$；$R=0$ 让它空转。因此组合必须：

1. **强制门的自由行非零**（至少 $\beta\ne0$），且
2. **让这个非零条件与门的变量共享**（同一个 $R$ 条目 / 同一个 $AN$ 列），否则非零门只是并行的无关约束。

296 的 $(5b)\iff f\ne0$ 正好提供第 1 条；缺的是第 2 条的 wiring。

## 第一个可检验量（下一步）

构造一个全局 $A$，使同一个自由行同时：
- 在 296 型 gadget 中产生 $f\ne0$ 的强制；
- 在 303 B 型门中充当 $\beta$（即该行的 $AN$ 分量进入 $H_A$ 的第 4 行）。

若 $\beta\ne0$ 被强制后 $(5a)$ 仍允许 $z\ne xy$，则组合 unsound；若 $(5a)$ 变成 $z=xy$，则组合 sound。

## 状态

- $R=0$ 伪解：**[已证-纸面]**（显式矩阵）；
- wiring 构造：**[未做]**。
