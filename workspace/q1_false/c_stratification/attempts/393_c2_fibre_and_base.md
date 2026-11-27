# 393 Phase 3+4：修正后的纤维；$c=2$ 的底几何（三种谱情形）与"单谱有限可判"

> 承接 392（专家 107 号：纤维公式错、层号定为 $c=k-\rho$、先做 $K$-split 子类）。
> 本文件落实 Phase 3（重建纤维）与 Phase 4（$c=2$ 的底几何），并给出一条**可判性**
> 结果：实谱单谱时 $c=2$ 的搜索是有限的。

## 目标

1. 把两个纤维公式写成正式陈述（含证明）；
2. 把 $\mathcal I_2(M)=\{D\in\operatorname{Gr}(2,K):M(D)\subseteq D\}$ 在三种谱情形下描述清楚（分量与维数）；
3. 由 1+2 给出 $c=2$ 的可判性结论（单谱 ⟹ 有限多个 gcd 检验）。

## 设想与理由

$c=1$ 的底是"有限个射影特征空间之并"（$\mathbb P(E_\mu)$），因为一维不变子空间就是特征向量。
$c=2$ 的底是"$M$-不变 2-子空间簇"，它由 $M$ 的 Jordan/有理标准形完全决定：**不变子空间 = Jordan 链段的直和**。
所以底的分量结构可以直接从 $M$ 的谱与块结构读出，不需要任何新几何。

## 做法

$$\boxed{c:=k-\rho,\qquad t:=q-\rho,\qquad q=\rho+t,\qquad D:=\ker H=K\cap V^\perp}$$

（行相关时 $t:=\dim V-\rho$。）

### Phase 3：两个纤维

**命题 1（full 问题）.** 固定 $D$，$U_D:=D+AD$。可行设计是

$$\mathcal F_D=\Big\{V\in\operatorname{Gr}(q,U_D^\perp):\ V_0\subseteq V,\ K\cap V^\perp=D\Big\}.$$

- $V\subseteq U_D^\perp$ 只给 $D\subseteq K\cap V^\perp$，**等式**是额外要求；
- 等式 $\iff$ **$K\cap U_D=D$**；*证明*：$U_D\subseteq V^\perp$ ⟹ $K\cap U_D\subseteq K\cap V^\perp=D$；反向因 $D\subseteq U_D$。$\square$
- 非空还需 $V_0\subseteq U_D^\perp$ 与 $\dim U_D\le n-q$。

**命题 2（$K$-split 问题）.** 再加 $V=(V\cap K)\oplus(V\cap K^\perp)$，并设 $M(D)\subseteq D$。则

$$V\cap K=D^{\perp_K},\qquad V=D^{\perp_K}\oplus W,\qquad W\subseteq T_D:=K^\perp\cap(A_{21}D)^\perp,$$

$$\boxed{\ \mathcal F_D^{\rm split}\cong\operatorname{Gr}\bigl(t-w_0,\ T_D/W_0\bigr)\ }$$

**但必须先把底限制到满足预设行的方向**（专家 108 号更正）：

$$\mathcal B_{\rm pres}=\{D\in\mathcal I_c(M):\ P_K(V_0)\subseteq D^{\perp_K}\}\quad(\text{等价于 } D\perp P_K(V_0)),$$

并要求 $W_0=P_{K^\perp}(V_0)\subseteq T_D$。即 $V_0\subseteq V$ 是**两个**独立条件，缺一不可：

$$P_K(V_0)\subseteq D^{\perp_K}\quad\text{（底条件，限制分量）},\qquad W_0\subseteq W\quad\text{（纤维条件，商掉 }W_0).$$

维数 $(t-w_0)(\rho_{\rm amb}-r(D)-t)$，非空 $\iff w_0\le t\le\rho_{\rm amb}-r(D)$。
（**注意**：这里用 $\rho_{\rm amb}:=n-k=\dim K^\perp$，**不是** $\rho:=\rank H$；见 400 的更正；
预设行条件与底限制见 404 与专家 108 号 §3。）

*证明.* (i) $V\cap K=\{x\in K: x\perp V\}^\perp_K$：由 $K$-split，$V^\perp\cap K=(V\cap K)^\perp\cap K=D^{\perp_K}$ ✓。
(ii) $V\subseteq U_D^\perp$：对 $d\in D$，$\langle d,V\rangle=\langle d,D^{\perp_K}\rangle+\langle d,W\rangle=0+\langle d,W\rangle$（$d\perp D^{\perp_K}$ 因两者都在 $K$）；
而 $Ad=Md+A_{21}d$ 且 $Md\in D$，故 $\langle Ad,V\rangle=\langle A_{21}d,W\rangle$；于是
$V\perp AD\iff W\perp A_{21}D\iff W\subseteq T_D$ ✓。
(iii) 预设行：$V_0\subseteq V\iff P_K(V_0)\subseteq D^{\perp_K}$ 且 $W_0\subseteq W$；
前者是 $D$ 上的闭条件、后者给出 $W$ 含固定子空间 ⟹ 商掉 $W_0$ 得 Grassmannian ✓。
(iv) 维数：$\dim T_D=\dim K^\perp-\rank(A_{21}|_D)=\rho_{\rm amb}-r(D)$，其中 $\rho_{\rm amb}=n-k$；$\dim\operatorname{Gr}(t-w_0,\rho-r-w_0)=(t-w_0)(\rho-r-t)$ ✓。$\square$

### Phase 4：$\mathcal I_2(M)$ 的三种谱情形

**定理 3（底几何）——按专家 108 号 §4 重写为"主分量分类".** 设 $M$ 在 $K$ 上的实主分解为
$K=\bigoplus_{\lambda\in\mathbb R}K_\lambda\oplus\bigoplus_{\{\mu,\bar\mu\}}K_{\{\mu,\bar\mu\}}$。
不变子空间按主分量分解，故 $M$-不变 2-平面必为下列三类之一：

1. **含于一个实主分量**的 2 维不变子空间（其结构由该分量的 Jordan 分划决定：**单个** Jordan 块内
   只有链的前两段；**多个** Jordan 块时还取决于特征向量与广义特征向量的**相对位置**，不只是链前缀）；
2. **两个不同实主分量**的不变直线之和，$\mathbb P(K_\lambda)\times\mathbb P(K_\mu)$，
   维数 $(d_\lambda-1)+(d_\mu-1)$；
3. **不可约二次主分量**（共轭对 $\{\mu,\bar\mu\}$）：由复特征空间 $E_\mu$ 中的**复特征直线**给出，
   族为 $\mathbb P_{\mathbb C}(E_\mu)\cong\mathbb{CP}^{g_\mu-1}$，**实维数 $2(g_\mu-1)$**，
   其中 $g_\mu=\dim_{\mathbb C}E_\mu$ 是**几何**重数（不是代数重数）。
   $g_\mu=1$ 时退化为一个孤立点。

（旧版写"共轭对贡献一个孤立点""Jordan 块只给链前缀"，在多重 Jordan 块与 $g_\mu>1$ 时**不完整**；
以本定理为准。见 404。）

于是

$$\dim\mathcal I_2(M)=\max\Big\{2(d_\lambda-2)\ (d_\lambda\ge3),\ (d_\lambda-1)+(d_\mu-1)\Big\},\qquad
\#\{\text{孤立点}\}=\binom{\#\text{实特征值}}{2}+\#\{\text{共轭对}\}\ (\text{半单情形}).$$

**推论 4（单谱 ⟹ 有限）.** 若 $M$ 的全部特征值互异（实谱互异、且共轭对各不同），则
$\mathcal I_2(M)$ 是**有限集**，恰有 $\binom{k_{\mathbb R}}{2}+\#\{\text{共轭对}\}$ 个点。
此时 $K$-split $c=2$ 的搜索 = **有限多个 Grassmannian 纤维**，每个纤维一次函数域 gcd 检验 ⟹ **可判**，
且不需要在底上取图卡（底没有参数）。

> 这与 $c=1$ 的结构完全平行：$c=1$ 的底是有限个 $\mathbb P(E_\mu)$（每个一维），
> $c=2$ 单谱时底退化为有限个点；$c=2$ 重根时底才出现正维的 $\operatorname{Gr}(2,E_\mu)$。

### 秩分层

$r(D)=\rank(A_{21}|_D)\in\{0,1,2\}$，$\dim U_D=2+r(D)$，$\dim T_D=\rho_{\rm amb}-r(D)$（$\rho_{\rm amb}=n-k$）。
在 $\operatorname{Gr}(2,E_\lambda)$ 或 $\mathbb P\times\mathbb P$ 上，$r(D)\le s$ 是**行列式条件**
（$A_{21}|_{\mathcal S}$ 的 $(s+1)$-阶子式为零），故每个 $r$ 层是局部闭子簇；
在常秩层上 $T_D$ 是常秩丛，纤维 $\operatorname{Gr}(t-w_0,T_D/W_0)$ 给出相对 Graßmann 丛。

## 进展

- 命题 1、2 与定理 3 的证明已写出（纸面）；定理 3 是经典"不变子空间 = 链段直和"的专门化；
- 推论 4 给出**单谱时 $c=2$ 的有限可判性**（与 386 的"固定 $p$ 单谱多项式"同一精神，但这里是 $c=2$）；
- 精确核对（[c395](../../../../tools/verification/c395_c2_base_geometry.py)）：$k=4$ 的四种 $M$
  的坐标 2-平面中的不变者与预测分量一致（情形 1 六个点、情形 2 六个点 + 一个 Gr(2,E₁)、
  情形 3 Gr(2,E₁) 正维、情形 4 Jordan 块只有 flag 前两段）；
- $c=2$ 反例证书见 [c394](../../../../tools/verification/c394_c2_certificate.py)（非不变 $D$ 下 $\dim(V\cap K)=1\ne\rho$）。

## 最终结论

1. **Phase 3 完成**：两个纤维公式（full 与 $K$-split），$K$-split 的纤维是 $\operatorname{Gr}(t-w_0,T_D/W_0)$；
2. **Phase 4 完成**：$\mathcal I_2(M)$ 由 $M$ 的 Jordan/有理结构完全决定；重根才出现正维分量；
3. **新结论（推论 4）**：单谱时底有限 ⟹ $c=2$ 的 $K$-split 判定 = 有限多个 gcd 检验 ⟹ 可判；
4. 下一步是 Phase 5：在**重根**的底上取图卡（底变成 $\operatorname{Gr}(2,E_\lambda)$），把 $(5b)$ 加到总图卡上。

## 放弃原因

- 没有算 $\mathcal I_2(M)$ 的分量**个数与次数**（重根 + 共轭对的混合情形；专家说无通用公式，需逐谱型算）；
- 推论 4 只给了"单谱 ⟹ 有限"，没有给位复杂度（那是 Phase 6）；
- 没有证明 $K$-split 归一化定理（专家明确说这是 full 问题的关键缺口）。

## 残留价值

- **两个可用的纤维公式**（含证明）；
- **$\mathcal I_2(M)$ 的三情形定理**与维数/孤立点计数；
- **单谱 ⟹ 有限可判**这条结论，可直接作为 $c=2$ 论文的第一个定理；
- 秩分层与相对丛的表述（Phase 5 的入口）。

## 相关文件

- [attempts/392](392_expert107_audit.md)（专家 107 号裁决）
- [attempts/391](../../decision_algorithms/attempts/391_c_gt_1_entry.md)（三个量、方向定理、对齐表）
- [c394](../../../../tools/verification/c394_c2_certificate.py)（反例证书）、[c395](../../../../tools/verification/c395_c2_base_geometry.py)（底几何核对）
- [attempts/386](../../decision_algorithms/attempts/386_bit_complexity_proof.md)（$c=1$ 的固定 $p$ 复杂度，思路可借）
