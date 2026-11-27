# 泄漏 gadget 的构造尝试：条件、失败点与下一步

> 2026-11-09。第 4 项（泄漏 gadget，$c\ge2$）的构造尝试。结论：条件自洽（seed10 为例），
> 但把乘法 gadget 直接放到 $K_0$ 上、再加泄漏块的构造在 $\lambda=0$ 处谱失败；
> 随机搜索 40 个 $c=2$ 实例未找到可行见证。状态：**未完成（构造 + 负结果）**。

## 目标

构造 $A(K_0)\not\subseteq K_0$、存在不变 $V$ 使 $A(V)\subseteq K_0$、且 $(5a)(5b)$ 可行的 $c=2$ gadget 实例。

## 设想与理由

210 更正后，路线是：
1. $A(K_0)\not\subseteq K_0$（避开 205 全局定理）；
2. $V$ 不变、$A(V)\subseteq K_0$（乘法 gadget 的 chart 方程成立）；
3. 铅笔在这类 $V$ 上可以好（seed10 证明局部不变 + 全局泄漏可可行）。

## 做法：一个显式的失败构造

取 $n=6$、$p=1$、$C=e_5^*$、$E=\operatorname{span}\{e_1,\dots,e_4\}=K_0$、$G=\operatorname{span}\{e_5,e_6\}$。
$A$ 在 $E$ 上取乘法 gadget：
$$A e_1=0,\quad A e_2=e_2,\quad A e_3=0,\quad A e_4=e_4-e_1,$$
并加泄漏 $A e_1\mapsto e_6$（或 $A e_4\mapsto e_4-e_1+e_6$），$A e_5=e_5$、$A e_6=e_5$。
则 $K_0=E$、$A(K_0)\not\subseteq K_0$；取 $V=\operatorname{span}(e_2,e_3)$（gadget 不变、$A(V)\subseteq V\subseteq K_0$）。
$L_0=e_1+e_4$ 使 $V=\ker[L_0N;L_0AN]$（$c=2$）。

**谱失败**：$V^\perp=\operatorname{span}(e_1^*,e_4^*)$；$l=e_1$ 的 $lA=0$（$A e_1$ 的 $K_0$ 分量为 0，泄漏到 $e_6$），
$l=e_4$ 的 $lA=e_4^*-e_1^*$。故 $l\mapsto lA$ 在 $V^\perp$ 上秩 **1**，在 $\lambda=0$ 处
$\operatorname{rank}P(0)\le1<2$。这是 $B_*=0$ 型的谱障碍。

**两难**：
- 若改 $A e_1$ 使其 $K_0$ 分量非零（增大秩），则 $V=\operatorname{span}(e_2,e_3)$ 不再不变（或 $L_0$ 的 $W_L$ 改变）；
- 若换 $V$（例如让 $V$ 含 $e_1$ 方向），则 $L_0$ 的核条件与 gadget chart 都要重排。

## 随机搜索

对 $n=6$、$p=1$、$C=e_5^*$、随机 $A$（元素 $-2..2$）、随机 $L_0$，保留 $k=4$ 的实例，
用求解器试 $(q,\omega)=(4,2),(3,2)$：40 个实例中 **0 个 FOUND**。
（这是搜索失败，不是不可行证明；但说明可行泄漏 $c=2$ 实例不容易随机碰到。）

## 进展

* 泄漏 gadget 的条件写成；
* 一个显式构造的谱失败点定位（$\lambda=0$、$lA$ 秩 1）；
* 随机搜索 40 例无果。

## 最终结论

* 条件自洽（seed10 为证），但直接把 gadget 放在 $K_0$ 上 + 泄漏块会在顶部特征值处谱失败；
* 需要重新安排 chart：让 $V^\perp$ 上的 $l\mapsto lA$ 在两个方向都有非零像；
* 或者接受更高的 $q$/不同的 $L_0$，把谱条件救回来。

## 放弃原因

* 未找到可行构造；
* 未系统搜索 $L_0$/$V$/泄漏块；
* 未做符号判定。

## 残留价值

* 明确的失败机制（$A e_1$ 的 $K_0$ 分量为 0 导致 $lA$ 秩 1）；
* 为下一轮指明“调整 chart/泄漏”的方向。

## 相关文件

* [attempts/210](210_local_leakage_correction.md)（更正与条件）
* [attempts/200](200_multiplication_gadget.md)（gadget）
* [attempts/204](204_spectral_gadget_conditions.md)（谱条件）

## 状态

* 尝试：**[未完成]**。
* 可行泄漏 gadget：**[未找到]**。
