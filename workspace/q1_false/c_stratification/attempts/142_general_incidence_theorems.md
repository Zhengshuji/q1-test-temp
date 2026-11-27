# 两条一般 incidence 定理：有限 $(t,u)$ 分层与相对 Grassmannian

> 2026-11-08。按专家 56 号的建议（§5.2–5.3），把“型控制猜想”之前**能真正证明**的一般结构
> 先固定下来。状态：**M2（纸面）**；不声称分量数上界。

## 目标

设 $\mathcal X$ 为环境状态空间，$K_0\subseteq\mathcal X$，$D=K_0\cap A^{-1}K_0$，
$\iota:D\hookrightarrow K_0$、$A_0=A|_D:D\to K_0$。对 $W\in\operatorname{Gr}(t,D)$ 记
$$U=W+A_0(W),\qquad u=\dim U.$$
证明两条一般定理：

* **定理 A（有限分层）**：对固定 $t$，条件 $\dim(W+A_0(W))=u$ 是 $\operatorname{Gr}(t,D)$ 中的
  局部闭代数层；$u$ 只取有限个值。
* **定理 B（相对 Grassmannian）**：在固定 $(t,u)$ 层上，$U$ 构成代数子丛，
  $\operatorname{Gr}(c-u,K_0/U)$ 构成相对 Grassmannian；精确纤维条件
  $\operatorname{rank}\Phi_V=c-t$ 是开条件，故总 incidence 空间是该相对 Grassmannian 的**开子簇**。

## 设想与理由

* $t\le u\le2t$：$U$ 由 $W$ 与 $A_0(W)$ 张成，维数介于 $t$ 与 $2t$。
* 固定 $c$ 时 $t\in[0,c]$、$u\in[t,2t]$ 只有有限对——这是“有限分层”的来源。
* 一般理论：Grassmannian 上的 universal subbundle $\mathcal S$，映射
  $\mathcal S\oplus\mathcal S\to K_0\otimes\mathcal O$、$(w_1,w_2)\mapsto\iota(w_1)+A_0(w_2)$
  的像就是 $U$；$\dim U=u$ 是行列式秩条件。
* 固定 $(t,u)$ 后 $U$ 随 $W$ 代数地变化（子丛），商空间 $K_0/U$ 也代数地变化；
  $\operatorname{Gr}(c-u,K_0/U)$ 是相对 Grassmannian。

## 做法

**定理 A**。在 $\operatorname{Gr}(t,D)$ 上取 universal 子丛 $\mathcal S$。映射
$$\varphi:\mathcal S\oplus\mathcal S\longrightarrow K_0\otimes\mathcal O,\qquad (w_1,w_2)\mapsto\iota(w_1)+A_0(w_2)$$
在纤维 $W$ 上的像为 $U=W+A_0(W)$。对固定 $u$，$\operatorname{rank}\varphi=u$ 是
“所有 $(u+1)$-子式为零、某个 $u$-子式非零”的局部闭条件，故
$$\operatorname{Gr}(t,D)_{\le u}\setminus\operatorname{Gr}(t,D)_{\le u-1}$$
是局部闭层。$u$ 的范围 $[t,2t]$ 有限。

**定理 B**。在固定 $(t,u)$ 层 $S_{t,u}$ 上，$\varphi$ 的像给出秩 $u$ 的子丛
$\mathcal U\subseteq K_0\otimes\mathcal O$；商丛 $K_0\otimes\mathcal O/\mathcal U$ 的纤维是 $K_0/U$。
相对 Grassmannian
$$\operatorname{Gr}(c-u,\ (K_0\otimes\mathcal O)/\mathcal U)\longrightarrow S_{t,u}$$
的参数是“包含 $U$ 的 $c$-平面 $V\subseteq K_0$”。
精确条件 $\operatorname{rank}\Phi_V=c-t$（$\Phi_V:V\to\mathcal X/V$、$v\mapsto Av+V$，
$\ker\Phi_V=V\cap A^{-1}V$）是开条件；故总空间
$$\mathcal I_{t,u}=\{((W),V):\ W\in S_{t,u},\ U\subseteq V,\ \operatorname{rank}\Phi_V=c-t\}$$
是相对 Grassmannian 的开子簇。

**推论（分量，条件性）**。若 $S_{t,u}$ 不可约且上述开子簇非空，则 $\mathcal I_{t,u}$ 不可约；
$\mathcal I$ 的分量落在各 $(t,u)$ 层的像中。**这不给出分量数的上界**：行列式层本身可能可约。

## 进展

* 定理 A、B 的陈述与证明已写出（M2）；不依赖 Jordan 型/Kronecker 标准形。
* 与 135 的关系：135 的纤维是 $\operatorname{Gr}(c-u,K_0/U)$ 的开子集；142 把它升级为
  “相对 Grassmannian 的开子簇”。
* 与 136/137 的关系：$c=2,3$ 的逐型分类是 $(t,u)$ 层内的进一步细分；142 给出外层框架。

## 最终结论

* **有限 $(t,u)$ 分层**与**相对 Grassmannian 结构**是一般 $c$ 可证的定理（不是猜想）。
* 分量数上界仍未知；需要额外证明各层的不可约性/分量数。

## 放弃原因

* 未证各 $(t,u)$ 层的不可约性；未给分量数上界。
* Lean：相对 Grassmannian/子丛的 Mathlib 支持有限，专家建议不形式化。

## 残留价值

* 一般 $c$ 的**结构定理**（M2），可作为论文的一般框架；
* 把“型控制猜想”降级为“层内进一步细分”的问题，而不是全局猜想。

## 相关文件

* [attempts/135](135_exact_fibre_theorem.md)（精确纤维，已改 $\mathcal X/V$）
* [attempts/136](136_c2_rewrite.md)、[137](137_c3_repair.md)（$c=2,3$ 细分）
* [attempts/139](../../decision_algorithms/attempts/139_type_control_conjecture.md)（型控制猜想）

## 状态

* 定理 A、B：**[已证-纸面，M2]**；分量推论：**[条件性，M2]**。
* Lean：**[未做]**（专家建议不形式化）。
