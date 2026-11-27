# 324 超平面层的有效分量定理：$\delta+1$ 成立，但分量不是底片

> 承接 323（专家 94 号裁决：下一步做**有效分量定理**，显式参数化，先 $\delta=1,2$）。
> 本文件给出全空间 $Z$ 的分量结构与显式参数化，并更正我此前两处说法。
> 验证：[c332](../../../../tools/verification/c332_104_component_split.py)（104 的 $\delta=1$ 例）。

## 目标

1. 给出 lifted incidence 空间 $Z$ 的**不可约分量**的显式描述与个数上界。
2. 用它回答：123 的"按层抽样"是否有缺口？（专家 94 号的定理 B 需要完整分解。）

## 设想与理由

把约束写进 $K$-坐标会看清结构。自由行的数据是
$$(a_i,b_i)=\bigl(N^{\mathsf T}r_i^{\mathsf T},\ N^{\mathsf T}A^{\mathsf T}r_i^{\mathsf T}\bigr)\in\mathcal T=\operatorname{row}[N\ AN],$$
而 $r_i v=0,\ r_iAv=0$ 等价于 $a_i\perp\sigma$、$b_i\perp\sigma$（$v=N\sigma^{\mathsf T}$）。所以

$$Z=\Bigl\{(\sigma,y_1,\dots,y_m):\ \sigma\in B,\ y_i\in W_\sigma\Bigr\},\qquad
W_\sigma=\{(a,b)\in\mathcal T:\ \sigma\!\cdot\!a=\sigma\!\cdot\!b=0\},$$

其中 $B=\{\sigma\in\mathbb P(K_0):\ \sigma\cdot V_0=0\}$ 是**射影线性子空间**（可容许底），
$\dim W_\sigma=d_0-\rho(\sigma)$，$\rho(\sigma)=\operatorname{rank}$ 那对线性泛函 $\in\{1,2\}$。

$\rho$ 只在**特征 locus** 上掉到 1：
$$E=\bigcup_{\lambda}\ E_\lambda,\qquad E_\lambda=\mathbb P\bigl(K_0\cap\ker(A-\lambda I)\bigr)\cap B .$$
于是 $B^\circ=B\setminus E$ 是开集，$W_\sigma$ 在其上是秩 $d_0-2$ 的向量丛，在 $E_\lambda$ 上是秩 $d_0-1$ 的向量丛。

## 做法

### 1. 分量定理

> **定理.** 设 $B\ne\varnothing$。记
> $$Z^\circ=\overline{\{(\sigma,y):\ \sigma\in B^\circ,\ y_i\in W_\sigma\}},\qquad
> F_\lambda=\{(\sigma,y):\ \sigma\in E_\lambda,\ y_i\in W_\sigma\}.$$
> 则
> $$Z=Z^\circ\ \cup\ \bigcup_{\lambda:\ E_\lambda\ne\varnothing}F_\lambda,$$
> 且右边的每一项都是 $Z$ 的**不可约分量**（空项删去）。因此
> $$\#\{\text{分量}\}\le 1+\#\{\lambda:\ E_\lambda\ne\varnothing\}\le 1+\delta .$$

> **更正（专家 97 号，2026-11-16 收到）**：**计数 $\le1+\delta$ 成立，但"每项都是不可约分量"未证。**
> 下面的 (iv) 用"纤维维数不同"主张 $Z^\circ$ 与 $F_\lambda$ 不可比，**不成立**：
> 闭包的纤维不等于纤维的闭包（极限可同时让底点移动），且可容许行空间族
> （含 $\dim(V\cap K_0)=k-1$ 的条件）未必是向量丛。
> 要补的是：把行空间入射簇及其 Grassmann 层显式化，证明**极限行空间构成可容许特征纤维的真闭子集**
> （可用 Plücker 坐标），且族在常秩意义下是丛。**在这之前，本文只能声称计数上界，不能声称"这就是分量分解"。**
>
> **修复（[343](343_stratified_cover_fix.md)）**：判据其实**不需要分量**——只需有限个不可约块的**覆盖**。
> 用 Grassmann 的有限仿射图卡切块，每块不可约 ⟹ 逐块 generic-gcd 判据照旧成立。
> 所以本文的正确用途是"**有限不可约覆盖 + 计数上界**"，"分量"一词应撤掉。

*证明.* (i) 覆盖：任取 $(\sigma,y)\in Z$；若 $\sigma\in B^\circ$ 则在开部，否则 $\sigma\in E_\lambda$ 某个，故在 $F_\lambda$。(ii) $Z^\circ$ 不可约：它是"不可约底 $B^\circ$ + 向量丛纤维"的全空间之闭包。(iii) $F_\lambda$ 不可约：$E_\lambda$ 是不可约射影子空间，$W_\sigma$ 在其上秩恒为 $d_0-1$，故是向量丛。(iv) 两两不可比：$Z^\circ$ 有底在 $B^\circ$ 上的点，故 $Z^\circ\not\subseteq F_\lambda$；反之 $F_\lambda$ 在 $\sigma\in E_\lambda$ 处的纤维是 $d_0-1$ 维，而 $Z^\circ$ 在该处的纤维是 $\{W_{\sigma'}\}$ 的极限——Grassmannian 里 $d_0-2$ 维子空间的极限仍是 $d_0-2$ 维（且含于 $W_\sigma$），故可取 $y\in F_\lambda\setminus Z^\circ$。$\square$
> **（(iv) 已被 97 号指出有漏洞，见上方更正。）**

**个数界**：不同 $\lambda$ 的特征子空间 $K_0\cap\ker(A-\lambda I)$ 线性无关，其直和含于
$D_A=K_0\cap A^{-1}K_0$，故非空者个数 $\le\sum_\lambda\dim\le\dim D_A=\delta$。$\square$

### 2. 显式参数化（这就是"effective"的含义）

- $B^\circ$：$\{\sigma:\sigma\cdot V_0=0\}$ 去掉有限个线性子空间；用射影坐标图（$\sigma_j=1$）显式写出；
- $E_\lambda$：$\mathbb P(K_0\cap\ker(A-\lambda I))$，由一次线性方程组给出；
- 纤维：$W_\sigma=\ker M(\sigma)$，其中 $M(\sigma)$ 是 $2\times d_0$ 的矩阵（两行是 $\sigma\cdot a$、$\sigma\cdot b$ 在 $\mathcal T$ 的基下的系数），**线性**于 $\sigma$，秩 $\rho(\sigma)$；
- 开条件 $\operatorname{rank}H=\omega$、$\operatorname{rank}[L_0;R]=q$ 与开集求交（不可约性保持）。

于是每个分量都是"显式射影底 + 显式核丛"，参数个数 = $\dim B+ m(d_0-\rho)$，与 94 号要求的记账方式一致。

### 3. 与 104 的一致性（$\delta=1$）

104 的实例：$\delta=1$、$B=\mathbb P^1$、$E$ 是单点 $\sigma=(1,0,0)$。定理给 2 个分量：
$Z^\circ$（纤维 1 维，$\gcd=\lambda$，整支全坏）与 $F$（纤维 2 维，一般点 $\gcd=1$，好）。
与 [c332](../../../../tools/verification/c332_104_component_split.py) 的 $Z=Z_1\cup Z_2$ 完全一致（$Z_1=F$、$Z_2=Z^\circ$）。

## 进展

1. **分量定理**：$\#$分量 $\le 1+\delta$，且每个分量有显式描述（底 + 核丛）。
2. **两个更正**（都是我此前说错的）：
   - **323 说"$Z$ 的分量数不是 $\le\delta+1$"——错**。$\delta+1$ 对**全空间**同样成立；
     我举的 104 不是反例（$\delta=1$、分量数 $2=\delta+1$）。真正的差别是：分量**不是**底片本身
     （底空间这里是 1 个分量，全空间是 2 个），分量的形状是"一般闭包 + 各特征 locus 上的满纤维"。
   - **322 §4 说"123 的按层抽样有缺口"——错**。由定理，每个层恰好贡献**一个**分量（$F_\lambda$），
     外加 $Z^\circ$；123 对每个特征 $\lambda$ 取一个点、对开层取一个一般点，**正好命中每个分量**。
     我担心的"好分量维数更低、抽样漏掉"在同一层里不会发生——同层只有一个分量。
3. 定理 B（有限归约）现在有了可操作的内容：枚举 $1+\#$特征子空间个分量（$\le1+\delta$），逐个算 generic gcd。

## 最终结论

- 超平面层的**分量结构已闭合**：$\#$分量 $\le1+\delta$，显式参数化（底 = 射影子空间 / 开集，纤维 = 显式矩阵的核）。
- 因此 94 号的**定理 B 可以落地**；剩下的只有**定理 C** 的两个成本项：核丛参数下的 generic gcd（PIT）与位复杂度记账。
- 123 的算法在**正确性**上没有问题（此前我的"缺口"说法撤回）；问题仍然只是"它给的是特化点而不是 generic point"。
- **新颖性说明**：这是"秩分层 + 核丛 + 闭包"的标准论证（Kronecker/射影丛一路），**很可能不新**。
  它的价值不在数学新意，而在于：把 94 号的**定理 B 落地**，并给出**可操作**的参数化与个数界，
  为定理 C 的成本分析提供骨架。

## 放弃原因

- 没有处理**正维** $E_\lambda$（$A$ 有重特征值且 $K_0$ 含高维特征子空间）时的纤维分裂细节——定理的形式覆盖了它，
  但"$W_\sigma$ 在 $E_\lambda$ 上秩恒为 $d_0-1$"需要 $\sigma\mapsto$ 约束矩阵的秩在 $E_\lambda$ 上确实恒定（对 $\rho=1$ 成立）。
- 没有把开条件 $\operatorname{rank}H=\omega$、$\operatorname{rank}[L_0;R]=q$ 的非空性写成可判条件（会删掉某些分量）。
- 实点/有理点未处理（94 号 §6）。
- 没有做 $\delta=2$ 的第二个实例核对（c332 只覆盖 104）。

## 残留价值

- 一个可写进论文的"有效分量定理"（含显式参数化与个数界），正好是 94 号要求的下一步里程碑；
- 两条自我更正（$\delta+1$ 仍成立；123 无 soundness 缺口），避免后续会话按错的前提工作；
- 把定理 C 的缺口精确化为"核丛参数下的 generic gcd + 位复杂度"。

## 相关文件

- [attempts/121](121_hyperplane_vector_bundle.md)（底空间分解）
- [attempts/123](123_hyperplane_algorithm.md)（抽样算法）
- [attempts/322](322_hyperplane_determinism_components.md)（generic-gcd 判据；§4 已按本文件更正）
- [attempts/323](323_expert94_verdict.md)（94 号裁决；其中的分量数说法已更正）
- [attempts/104](104_p2_constrained_locus.md)（$\delta=1$ 的例）
- [c332](../../../../tools/verification/c332_104_component_split.py)

## 状态

- 计数 $\le1+\delta$：**[已证-纸面]**（专家 97 号确认）。
- 分量分解（"每项都是不可约分量"）：**[未证]**——97 号指出不可比性有漏洞（见定理后的更正）。
- 104 核对：**[精确验证]**（c332；$\delta=1$ 的例子可直接验）。
- 定理 C（成本）：**[未证]**；实/有理点：**[未做]**。
