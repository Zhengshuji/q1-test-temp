> **修复（2026-11-08，169）**：用循环向量参数化（$T^cx=0,T^{c-1}x\ne0$ 是充要条件）证明了
> 每个固定 Jordan 型的不变层是“不可约参数空间在态射下的像”，故不可约或空；
> $N_{\rm inv}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}$ **恢复为分量界**（M2）。
> 专家 59 号的两条反对（必要条件问题、商映射未控）均被绕过。

> **专家 59 号裁定（2026-11-08）**：不变部分的“分量界”**未证**（已被 169 修复）。长 $c>2$ 的 Jordan 链，
> 正确的底至少是
> $$\mathbb P\big(\ker T\cap T^{c-1}(K_0)\big),\qquad T=A-\lambda I,$$
> 而不是 $\mathbb P(E_\lambda\cap\operatorname{im}T)$；且“链参数空间 → 不变子空间 Grassmannian”的
> 商映射（同一子空间的不同链基）未被控制。故本文件的 $N_{\rm inv}(c)$ **降级为标签数**，
> 分量界需先证单块（一个 Jordan 块）的不可约性，再做多块。
> 非不变部分的 $B_{u,v}$ 归约仍成立（专家未反对）。

# 一般 $c$：不变部分的分量界与“不逐 $c$ 枚举”的非不变部分路线

> 2026-11-08。回答两个问题：(A) 把 147/159 的“Jordan 型块不可约”推广到任意固定 $c$；
> (B) 非不变部分如何**不逐 $c$ 枚举**地处理。状态：**M2（A 为定理；B 为归约 + 待证点）**。

## 目标

(A) 对任意固定 $c$，给不变部分（$t=c$，$A(V)\subseteq V$）的分量上界，且每块不可约；
(B) 把非不变部分（$t<c$）化成一个**与 $c$ 无关**的固定几何问题，而不是逐 $c$ 分类。

## 设想与理由

(A) 不变部分：$A|_V$ 的 Jordan 型 = “特征值标号的分块”；每块是
$$\prod_{\text{块}}\big(\text{特征空间/Grassmannian}\big)\times\big(\text{仿射链纤维}\big),$$
射影空间、Grassmannian、仿射空间的乘积，不可约或空。故分量数 $\le$ 块数。

(B) 非不变部分：$W\subseteq U:=W+A(W)$，$\dim U=u$。考虑 incidence
$$\mathcal I_{t,u}=\{(W,U):\ W\in\operatorname{Gr}(t,U),\ A(W)\subseteq U,\ U\in\operatorname{Gr}(u,K_0)\}.$$
投影 $\pi:\mathcal I_{t,u}\to\operatorname{Gr}(t,K_0)$ 的像就是 $S_{t,u}=\{W:\dim(W+A(W))=u\}$
（因为此时 $U=W+A(W)$ 被 $W$ 唯一决定，纤维是点）。而 $\mathcal I_{t,u}$ 在
$\operatorname{Gr}(u,K_0)$ 上的纤维是
$$\{W\in\operatorname{Gr}(t,U):A(W)\subseteq U\}=\operatorname{Gr}(t,\ U\cap A^{-1}U).$$
所以 $\mathcal I_{t,u}$ 是“以 $\operatorname{Gr}(u,K_0)$ 为底、以 $\operatorname{Gr}(t,U\cap A^{-1}U)$ 为纤维”的
相对 Grassmannian，**不需要逐 $c$ 枚举**，只需按 $v=\dim(U\cap A^{-1}U)$ 分层。

## 做法

### A. 不变部分

对每个分拆 $\lambda\vdash c$（$b(\lambda)$ 块），把 $b$ 个块标上特征值：至多 $s^{b(\lambda)}$ 种标号
（同尺寸块的有序标号是上界）。每块不可约（底为射影特征空间/Grassmannian，纤维为仿射链空间）。
故
$$\boxed{N_{\rm inv}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}\le p(c)\,s^{c}.}$$
- $c=1$：$\lambda=(1)$，$\le s$ ✓；
- $c=2$：$\lambda=(1,1)$ 给 $s^2$、$\lambda=(2)$ 给 $s$，$\le s^2+s$（实际更小 $=\binom{s}{2}+2s$）；
- $c=3$：$s+s^2+s^3$（159 的更细计数是 $\binom{s}{3}+2s(s-1)+3s$）。

注意：与 149 不同，这里**每块不可约性已由构造给出**（射影/仿射乘积），所以这是分量上界，
不只是标签数。

### B. 非不变部分：按 $v$ 分层，不逐 $c$

对固定 $(t,u)$，令
$$B_{u,v}=\{U\in\operatorname{Gr}(u,K_0):\ \dim(U\cap A^{-1}U)=v\},\qquad t\le v\le u.$$
这是 $\operatorname{Gr}(u,K_0)$ 上的一个**秩层**（固定线性映射 $U\mapsto U\cap A^{-1}U$ 的秩条件），
与 $c$ 无关（$u\le c$，但 $B_{u,v}$ 只依赖 $A$ 与 $u$）。
$\mathcal I_{t,u}$ 在 $B_{u,v}$ 上的部分是相对 Grassmannian $\operatorname{Gr}(t,\ U\cap A^{-1}U)$，
底 $B_{u,v}$ 的每个不可约分量上，纤维是固定维数 $v$ 的 Grassmannian（不可约），故总空间在
$B_{u,v}$ 的每个分量上不可约；其像在 $S_{t,u}$ 中也不可约。于是
$$\#\{\text{components of }S_{t,u}\}\le\sum_{v=t}^{u}\#\{\text{components of }B_{u,v}\}.$$
**关键**：$B_{u,v}$ 只依赖 $(A,u,v)$，不依赖 $c$；$v$ 只有 $u-t+1\le c+1$ 个值。
所以不逐 $c$ 枚举，而是逐 $(u,v)$（$u\le c$）——这是**固定几何**（固定 $A$ 在 $\operatorname{Gr}(u,K_0)$ 上的
秩层），与 $c$ 的增长无关。

**剩余待证点**：$\#\{\text{components of }B_{u,v}\}$ 的界。$B_{u,v}$ 是“$U\cap A^{-1}U$ 的维数”的
exact-rank 层，可能可约；但它是**固定 $u$** 的问题，可用归纳/确定性子簇理论处理，不需要对 $c$ 分类。

## 进展

* A 的一般不变部分界已写出（每块不可约，故是分量界，不只是标签数）；
* B 给出与 $c$ 无关的归约：只需求 $B_{u,v}$ 的分量数（固定 $u$），$v\in[t,u]$；
* 这回答了“不能逐 $c$ 枚举”的问题：逐的是 $(u,v)$，而 $(u,v)$ 的范围由 $u\le c$ 界定，
  但每步是固定几何，不是 $c$ 的类型分类。

## 最终结论

* 不变部分：$N_{\rm inv}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}$（分量界，M2）；
* 非不变部分：$S_{t,u}$ 的分量 $\le\sum_v\#\{B_{u,v}\text{ 的分量}\}$，$B_{u,v}$ 与 $c$ 无关；
* 一般 $c$ 的分量界归结为**固定 $u$ 的秩层 $B_{u,v}$ 的分量数**，不需要逐 $c$ 枚举。

## 放弃原因

* $B_{u,v}$ 的分量数未给（这是下一步的固定几何问题）；
* 未处理 $B_{u,v}$ 本身可约的情形（若可约，需进一步分层，但仍与 $c$ 无关）。

## 残留价值

* 把“逐 $c$ 枚举”替换为“逐 $(u,v)$ 的固定几何”，这是可推广的一般路线；
* 不变部分的分量界对任意 $c$ 成立。

## 相关文件

* [attempts/147](147_c2_component_bound.md)、[159](159_c3_component_bound_corrected.md)（$c=2,3$ 的实例）
* [attempts/142](142_general_incidence_theorems.md)（$(t,u)$ 分层）
* [attempts/149](149_general_c_component_bound.md)（旧的标签数，已降级）

## 状态

* A：**[已修复：分量界，见 169，M2]**。
* B 的归约：**[已证-纸面，M2]**；$B_{u,v}$ 分量数：**[开放]**。
