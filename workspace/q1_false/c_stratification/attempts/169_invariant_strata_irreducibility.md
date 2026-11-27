# 不变层的不可约性：循环向量参数化（修复 161 的链论证）

> 2026-11-08。专家 59 号指出 161 的链参数化有“必要条件问题”且“链 → 子空间的商映射未控制”。
> 本文件用**循环向量**（而不是链的基）重新参数化：固定 Jordan 型的不变层是
> “一个开集在多项式映射下的像”，故**不可约或空**。这修复了 161 的不变部分，
> 使其重新成为**分量界**（不只是标签数）。状态：**M2（纸面）**。

## 目标

对任意固定 $c$ 与固定“特征值标号的 Jordan 型”$\tau$，证明
$$S_\tau=\{V\in\operatorname{Gr}(c,K_0):A(V)\subseteq V,\ A|_V\ \text{的型为}\ \tau\}$$
**不可约或空**；由此 $N_{\rm inv}(c)\le\#\{\tau\}$。

## 设想与理由

专家指出的两个问题：
1. 链的底条件（如 $\ell\subseteq\operatorname{im}T$）只是**必要**，不足以保证链存在；
2. “链的基 → 子空间”的商映射（同一子空间的不同链基）未被控制。

**修复**：不用链的多个向量，而用**一个循环向量** $x$（Jordan 块的最高向量）。一个 Jordan 块
$V_i=\operatorname{span}\{x_i,Tx_i,\dots,T^{c_i-1}x_i\}$ 由 $x_i$ 决定，条件是
$$T^{c_i}x_i=0,\qquad T^{c_i-1}x_i\ne0$$
（$T=A-\lambda_iI$）。这两条**既是必要也是充分**：它们保证 $x_i,Tx_i,\dots,T^{c_i-1}x_i$
线性独立（若 $\sum a_jT^jx_i=0$，取最低次 $j$，作用 $T^{c_i-1-j}$ 得 $a_jT^{c_i-1}x_i=0$），
且张成不变 $c_i$ 维空间、型为单块 $(c_i)$。

## 做法

### 单块

固定 $\lambda$、$m=c$。**专家 60 号的关键修正**：$K_0$ 不必是 $A$-不变的，故 $T^jx$ 可能离开 $K_0$。
正确的参数空间是
$$\mathcal K_{\lambda,m}=\{x\in\mathbb C^n:\ T_{\lambda}^mx=0,\ T_{\lambda}^jx\in K_0\ (0\le j<m)\},$$
$$U_{\lambda,m}=\mathcal K_{\lambda,m}\setminus\ker T_{\lambda}^{m-1}
=\{x:\ T_{\lambda}^mx=0,\ T_{\lambda}^jx\in K_0\ (0\le j<m),\ T_{\lambda}^{m-1}x\ne0\}.$$
$\mathcal K_{\lambda,m}$ 是线性子空间（所有条件对 $x$ 线性），$U_{\lambda,m}$ 是其 Zariski 开子集，故不可约或空。
定义
$$\Phi:U_{\lambda,m}\longrightarrow\operatorname{Gr}(m,K_0),\qquad x\longmapsto\operatorname{span}\{x,T_{\lambda}x,\dots,T_{\lambda}^{m-1}x\}.$$
$\Phi$ 是态射（Plücker 坐标是 $x$ 的多项式），像是单块型 $(m)$ 的不变层 $S_{(m),\lambda}$：
* 任何这样的 $V$ 有循环向量 $x$（取链最高向量），$x\in U_{\lambda,m}$，$\Phi(x)=V$；
* 反之 $\Phi(x)$ 的型是 $(m)$（独立性论证同前；所有链向量在 $K_0$ 中）。

**像是不可约的**（不可约簇在态射下的像不可约）。故 $S_{(c),\lambda}$ 不可约或空。

### 多块

固定特征值标号的 Jordan 型 $\tau=\{(\lambda_i,c_i)\}_{i=1}^b$，$c=\sum c_i$。令
$$\Omega=\Big\{(x_1,\dots,x_b)\in\prod_i U_{\lambda_i,c_i}:\ \operatorname{rank}\big[T_{\lambda_i}^jx_i\big]_{i,j}=c\Big\}$$
（第二个条件是“各块张成直和”，是开条件——某个 $c\times c$ 子式非零）。$\Omega$ 是
不可约乘积的开子集，故不可约。定义
$$\Phi_\tau(x_1,\dots,x_b)=\bigoplus_i\operatorname{span}\{T_{\lambda_i}^jx_i\}.$$
这是态射，像是型 $\tau$ 的不变层 $S_\tau$（任何 $V$ 分解成 Jordan 块、取各块循环向量；反之显然）。
故 $S_\tau$ 不可约或空。

**不同特征值**：$x_i$ 落在不同的广义特征子空间，乘积仍不可约；
**同特征值、同尺寸块**：乘积对块标号有序，像是同一个；像不可约（不需要取商）。

### 推论

不同的 $\tau$ 给出不交的层（型由 $V$ 唯一决定），每层不可约或空，故
$$\boxed{N_{\rm inv}(c)\le\#\{\text{特征值标号的 Jordan 型}\}\le\sum_{\lambda\vdash c}s^{b(\lambda)}}$$
（右端是“给分拆 $\lambda$ 的 $b(\lambda)$ 个块标特征值”的**有序**标号数，是上界；
同尺寸块的无序性只会更小）。

## 进展

* 单块与多块的不可约性均已证（循环向量参数化 + 像不可约）；
* 专家 59 号的“必要条件问题”被绕过：循环向量的条件 $T^c x=0,T^{c-1}x\ne0$ 是充要的；
* “商映射未控制”也被绕过：不取商，直接用像；
* 161 的不变部分**恢复为分量界**（不再是标签数）。

## 最终结论

* 固定 Jordan 型的不变层不可约或空；
* $N_{\rm inv}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}$ 是**分量上界**（M2）；
* 专家 59 号的两条反对意见都被解决（循环向量是充要条件；像不可约不需要商）。

## 放弃原因

* 未处理**非不变**部分（$t<c$，$B_{u,v}$ 的秩层）——那是另一条线；
* 未给精确分量数/下界（需要每型非空性）；
* 未 Lean 化。

## 残留价值

* 修复 161 的不变部分；为一般 $c$ 分量界提供地基；
* 一个可复用的论证：“循环向量参数化 + 像不可约”。

## 相关文件

* [attempts/161](161_general_c_invariant_and_rank_strata.md)（被修复的对象）
* [attempts/159](159_c3_component_bound_corrected.md)、[160](160_c3_degenerate_audit.md)（$c=3$ 实例）
* [attempts/164](164_59_verdict_implementation.md)（专家 59 号的意见）

## 状态

* 不变层不可约性：**[已证-纸面，M2]**。
* 非不变部分 / 精确分量数：**[未做]**。
