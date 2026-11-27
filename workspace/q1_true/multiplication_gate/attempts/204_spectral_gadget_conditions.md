# 谱 gadget 的必要条件与扫描结果

> 2026-11-09。Task C：在 $A(K_0)\subseteq K_0$ 的 gadget 实例中让铅笔好。本文件记录：
> （1）谱条件在顶部特征值处的必要条件；（2）$L_0$/$q$/$\omega$ 的扫描（0 个见证）；
> （3）只有两个特征值的 gadget $A$ 必然失败的结构原因。状态：**M2（分析 + 精确扫描）**。

## 目标

找出谱 gadget 的设计条件，并解释为什么 202 的 gadget $A$ 及其自然变体不行。

## 设想与理由

在顶部行 $h_0=L_0N$ 的特征值 $\lambda_0$ 处，$(\lambda_0 I-A_*)h_0=0$（顶部行消失）。要使
$\operatorname{rank}P(\lambda_0)=\omega$，需要底部行在 $\lambda_0$ 的值补足 $\omega-\rho_s$ 维
（$\rho_s$ 是其余顶部行的存活秩）。

底部值：对 $l\in\mathcal L_V$，$P(\lambda_0)$ 的底部行为 $l(\lambda_0 I-A)N$。所以可用的方向是
$$(\lambda_0 I-A)\big|_{\mathcal L_V}.$$
当 $A(K_0)\subseteq K_0$ 且 $V$ 不变时，$\mathcal L_V=V^\perp$（201）；因此必要条件是
$$\operatorname{rank}\big((\lambda_0 I-A)|_{V^\perp}\big)\ge\omega-\rho_s.$$
若 $L_0$ 是单特征向量（$\rho_s=0$），需要该映射在 $V^\perp$ 上**满秩** $\omega$，即
$$E_{\lambda_0}\cap V^\perp=0\iff V+E_{\lambda_0}=K_0.$$

## 做法：扫描

### 1. 202 的 gadget（$k=4$，特征值 $0,1$）

$V$ 不变、$V\subseteq W_L$。若 $V=E_{\lambda_0}$（$\lambda_0$ 为顶部特征值），则 $V^\perp$ 落在另一个
特征子空间里；在那个特征值 $\lambda_1$ 处，$(\lambda_1 I-A)$ 把 $V^\perp$ 杀掉，底部值全零或平行。
两个特征值的 gadget 无法同时在两个特征值处保持秩。

**这就是 202 失败的根源**，与 $L_0$ 的选择无关（扫描 $L_0\in\{e_1,e_2,e_3,e_4\}$、$q=3..5$、$\omega=1..3$：
`total found 0`）。

### 2. 加谱“旁观者”（$k=5$，特征值 $0,1,2$）

构造：$K_0=\mathbb C^5$，$e_1\mapsto0$、$e_2\mapsto e_2$、$e_3\mapsto0$、$e_4\mapsto e_4-e_1$、$e_5\mapsto2e_5$；
$C=[e_6;e_7]$。扫描 $L_0\in\{e_1,\dots,e_5\}$、$(q,\omega)\in\{(4,2),(5,3),(5,2)\}$：
`none`（0 个见证）。

说明：单纯加一个旁观者特征值还不够；$V$ 的选取、顶部行的特征值、提升的支撑必须同时满足
“每个特征值处都有底部方向存活”。

## 进展

* 谱必要条件的公式化；
* 两个特征值 gadget 的结构性不可能；
* $L_0$/$q$/$\omega$ 扫描 0 见证；三特征值朴素变体也无见证。

## 最终结论

* 谱 gadget 的必要条件：在顶部特征值 $\lambda_0$ 处，
  $\operatorname{rank}((\lambda_0 I-A)|_{V^\perp})\ge\omega-\rho_s$；
* 两特征值 gadget 必然违反某个特征值处的要求；
* 需要更精细的设计：$V^\perp$ 跨越多个广义特征子空间，且顶部行不全在同一特征值消失。

## 放弃原因

* 未构造出满足所有特征值条件的实例；
* 未系统搜索 $V$ 与 $L_0$ 的联合设计；
* 未 Lean 化。

## 残留价值

* 谱必要条件的可检验公式；
* 解释了 202 与朴素变体的失败；
* 为 Task C 指明日标。

## 相关文件

* [attempts/202](202_gadget_naive_embedding.md)（谱障碍）
* [attempts/203](203_invariance_theorem.md)（不变性）
* [attempts/201](201_pair_lift_theorem.md)（$\mathcal L_V$）

## 状态

* 分析/扫描：**[M2 + 精确扫描]**。
* 可行谱 gadget：**[未做]**。
