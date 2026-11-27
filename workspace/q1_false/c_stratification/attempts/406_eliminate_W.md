# 406 消掉 $W$：铅笔只通过 $\Phi(W)\subseteq D^\circ$ 依赖 $W$（$c=2$ 时是 $\mathbb P^1$ 族）

> 专家 108 号 §14 指名的中间目标："whether the fibre condition can be eliminated structurally
> for fixed $D$"。本文件给出 $c=2$ 的肯定答案。

## 目标

1. 证明：给定 $D$ 时，铅笔对 $W$ 的依赖**只通过一个 $c$ 维空间里的子空间** $\Phi(W)$；
2. 由此把 $\exists W\in\operatorname{Gr}(t-w_0,T_D/W_0)$ 的量化换成对 $\Phi$ 的量化——$c=2$ 时最多是 $\mathbb P^1$；
3. 记录精确核对。

## 设想与理由

$K_0$-split 设计 $V=D^{\perp_{K_0}}\oplus W$ 里，$W\subseteq K_0^\perp$。于是：

- $H=V^{\mathsf T}N$ 中**$W$ 对应的行全为零**（$W\perp K_0$）；
- $H_A=V^{\mathsf T}AN$ 中 $W$ 对应的行是 $\varphi_w:=u\mapsto\langle w,A_{21}u\rangle$——
  因为 $\langle w,Mu\rangle=0$（$Mu\in K_0$）。

所以 $W$ 只通过**这些行张成的子空间** $\Phi(W)=\operatorname{span}\{\varphi_w:w\in W\}$ 进入铅笔。
而 $W\subseteq T_D$ 给出 $\varphi_w\perp D$，即 $\Phi(W)\subseteq D^\circ$（$D$ 在 $K_0^*$ 中的零化子），
$$\dim D^\circ=c .$$

**关键**：$\Phi$ 所在空间维数是 $c$，**与 $t$ 无关**。

## 做法

把 $H$ 与 $H_A$ 按"$D^{\perp_{K_0}}$ 行"与"$W$ 行"分块，逐块算它们是什么；再用 $W\subseteq T_D$ 定位 $\Phi(W)$。

## 进展

### 定理（$W$-消去）

设 $D\le K_0$、$M(D)\subseteq D$、$T_D=K_0^\perp\cap(A_{21}D)^\perp$、$W_0\subseteq T_D$，设计为
$V=D^{\perp_{K_0}}\oplus W$，$W_0\subseteq W\subseteq T_D$、$\dim W=t$。记
$$\Phi(W):=\{\varphi_w\in K_0^*:\ \varphi_w(u)=\langle w,A_{21}u\rangle,\ w\in W\}.$$
则

1. $\Phi(W)\subseteq D^\circ$，故 $\dim\Phi(W)\le c$；
2. 对一切 $\lambda$，
$$\operatorname{row}\bigl(\lambda H-H_A\bigr)=\operatorname{row}\bigl(\lambda H_K-(H_A)_K\bigr)+\Phi(W),$$
其中 $H_K,(H_A)_K$ 是 $D^{\perp_{K_0}}$ 那 $(k-c)$ 行给出的块；
3. 因而 $\operatorname{rank}(\lambda H-H_A)=\omega\ \forall\lambda$ **只通过 $\Phi(W)$ 依赖 $W$**。

*证明（要点；**完整一般形式见 [412](../../decision_algorithms/attempts/412_rowspace_identity_proof.md)**）.*
(1) 对 $d\in D$：$\varphi_w(d)=\langle w,A_{21}d\rangle=0$，因 $w\in T_D\subseteq(A_{21}D)^\perp$ ✓。
(2) $H$ 的 $W$ 行是 $w^{\mathsf T}N=\langle w,N\cdot\rangle=0$（$w\perp K_0$）；
$H_A$ 的 $W$ 行是 $w^{\mathsf T}AN=w^{\mathsf T}MN+w^{\mathsf T}A_{21}N=0+\varphi_w$（$w\perp K_0\ni MN$）✓。
(3) 行空间只由两块决定（堆叠矩阵的行空间 = 各块行空间之和），第二块就是 $\Phi(W)$ ✓。$\square$

**412 补充**：这条恒等式已在**一般情形**下证完——
$A=M+A_{21}$（$E=K_0\perp K_0^\perp$ 的分解）、$h_v(x)=\langle v,Nx\rangle$、$h^A_v(x)=\langle v,ANx\rangle$、
$\Psi_\lambda=\lambda h_\cdot-h^A_\cdot$；则引理 1 给 $W$ 行的两块、引理 2 给行空间对直和的加性，
于是 $\Psi_\lambda(V)=\Psi_\lambda(P)+\Phi(W)$ 对一切 $\lambda$ 成立，**不依赖具体实例**。
符号为 $-\varphi_w$（$\Psi_\lambda$ 在 $W$ 上恒等于 $-\varphi_\cdot$），不影响张成空间。

### 推论（$\exists W$ 的化简）

$$\exists W\ \bigl(W_0\subseteq W\subseteq T_D,\ \dim W=t\bigr)\text{ 使 }(5b)\iff
\exists\Phi\subseteq D^\circ\ \bigl(\dim\Phi\le c,\ \varphi(W_0)\subseteq\Phi,\ \Phi\ \text{可由这样的 }W\text{ 实现}\bigr)$$

使 (5b) 成立；且对同一 $\Phi$ 的**任意**代表元 $W$，结论相同。

**可实现性（精确版，专家 109 号 §2.2 要求；见 [411](../../decision_algorithms/attempts/411_expert109_audit.md) 定理 3）.** 记
$\Phi_0:=\varphi(W_0)$、$w_0=\dim W_0$、$\bar\varphi:T_D/W_0\to D^\circ/\Phi_0$ 为诱导映射。则存在
$W$ 使 $W_0\subseteq W\subseteq T_D$、$\dim W=t$、$\varphi(W)=\Phi$ **当且仅当**

$$\boxed{\ \Phi_0\subseteq\Phi\subseteq\varphi(T_D),\qquad
\dim\Phi-\dim\Phi_0\ \le\ t-w_0\ \le\ \dim\ker\bar\varphi+\dim\Phi-\dim\Phi_0\ }$$

（只写"$\Phi_0\subseteq\Phi\subseteq\varphi(T_D)$ + 维数记账"是**不完整**的；上下两个不等式决定哪些
$\Phi$ 真能被 $t$ 维 $W$ 实现。）

**$c=2$ 时**：$\operatorname{Gr}(\le2,D^\circ)$ 只有三类——$\{0\}$、直线（$\mathbb P^1$ 族）、$D^\circ$ 本身。
但正确的是"**至多一个射影直线分量**"（专家 109 号 §2.3）：

| $\dim\Phi_0$ | 可能的 $\Phi$ |
|---|---|
| 0 | $\{0\}$、任一过原点的直线、$D^\circ$ |
| 1 | 只有 $\Phi_0$ 本身，或 $D^\circ$ |
| 2 | 只有 $D^\circ$ |

再加 $\Phi\subseteq\varphi(T_D)$ 与上面的维数不等式，可能进一步缩小。
所以有效 $\Phi$-空间是 $\{0\}\cup\mathbb P(D^\circ)\cup\{D^\circ\}$ 的**子集**，
不是"总有一条 $\mathbb P^1$ 可用"。

### 精确核对（`c406`）

实例 $n=8,p=2,k=4$、$M=\operatorname{diag}(1,1,2,3)$，$D=\operatorname{span}\{e_1+e_2,e_3\}$、$T_D$ 维 3：

| 项 | 结果 |
|---|---|
| $\varphi_w$ 在 $D$ 上为零 | ✓（3 个基向量全为 0） |
| 10 个随机 $W$ 按 $\Phi$ 分组 | 9 个的 $\Phi\propto(1,-1,0,1)$ ⟹ **gcd 全为 0（可行）**；1 个 $\Phi=0$ ⟹ gcd $=2$ |
| 同组内 gcd 是否相同 | **是** ✓ |

（其中 9 个可行样本与 `c399` 的显式可行设计一致；$\Phi\ne0$ 时才可行，$\Phi=0$ 时不可行。）

### Lean 核验（三条，公理审计通过）

模块 `MyProof/SplitFibre.lean`（`namespace Q1PaperC2`，`lake build MyProof.SplitFibre` exit=0）：

| 声明 | 内容 |
|---|---|
| `split_design_orthogonal_D` | $V=(K\sqcap D^\perp)\sqcup W\le D^\perp$（$D\le K$、$W\le K^\perp$） |
| `orthogonal_split_iff` | $V\le(D+AD)^\perp\iff W\le(ND)^\perp$（$A=M+N$、$M(D)\subseteq D$、$\operatorname{im}N\subseteq K^\perp$）——**即 $(5a)\iff W\subseteq T_D$，本文件的核心** |
| `phi_kills_D` | $w\le(ND)^\perp$、$d\in D$ ⟹ $\langle w,Nd\rangle=0$，即 $\Phi(W)\subseteq D^\circ$ |

三条的公理只有 `propext`、`Classical.choice`、`Quot.sound`。

**未 Lean 化的部分**（诚实标注）：

- **行空间恒等式** $\operatorname{row}(\lambda H-H_A)=\operatorname{row}(\lambda H_K-(H_A)_K)+\Phi(W)$——
  这是矩阵层陈述（需要把 $H,H_A$ 从 $V,N,A$ 具体构造出来并做分块），未形式化；
- 因此"同一 $\Phi$ 的任意 $W$ 结论相同"目前是**纸面 + 数值核对**（c406 的 9 例同组同 gcd）。

### 对复杂度的后果

- **有效纤维**从 $\dim\operatorname{Gr}(t-w_0,T_D/W_0)$ 降到 $\dim\operatorname{Gr}(\le c,D^\circ)\le c^2$——
  这恰好解释了早先"$c^2$"直觉的**来源**，但它是**纤维**的维数，不是整个图卡；
- 图卡维数 = **底** $c(d_\lambda-c)$（可 $O(cn)$）+ **有效纤维** $\le c^2$。
  所以诚实的界是 $n^{O(cn+c^2)}$——与专家 108 号 §13.2 的判断一致；
- **$c=2$ 的干净结论**：纤维量化坍缩为 $\mathbb P^1$（或 0/全空间），每张图卡一次 gcd；
  剩下的复杂度瓶颈完全在**底**上（$\operatorname{Gr}(2,E_\lambda)$ 的维数 $2(d_\lambda-2)$）。

## 最终结论

1. **像约化（split-layer image reduction）成立**：铅笔只通过 $\Phi(W)\subseteq D^\circ$（$\dim\le c$）依赖 $W$；
   **注意**：这是 **$K_0$-split 层**的定理，**不**自动适用于非 split 设计（专家 109 号 §7 的命名要求）；
2. $c=2$ 时有效 $\Phi$-空间是 $\{0\}\cup\mathbb P(D^\circ)\cup\{D^\circ\}$ 的**子集**（"至多一个射影直线分量"）；
3. **精确可实现性**（定理 3，见 411）给出上下两个维数不等式，缺了它就不是完整等价；
4. **约化可行性判据**（定理 4，见 411）：$\exists W$ ⟺ $\exists$ 可实现的 $\Phi$ 使
   $\dim(\operatorname{row}P_D(\lambda)+\Phi)=\omega\ \forall\lambda$；
5. 一般 $c$ 时有效纤维维数 $\le\lfloor c^2/4\rfloor$（比 $O(c^2)$ 更准），底仍 $O(cn)$，
   所以**一致复杂度不可能由此得到**——瓶颈在底。

## 放弃原因

- 没有把"可实现性"写成完整的线性代数判据（只说了是线性的：$\Phi\subseteq\varphi(T_D)$ 与维数条件）；
- 没有证"底 $O(cn)$ 的维数不能进一步压缩"（例如用 $\mathcal B_{\rm pres}$ 或其他条件）；
- 一般 $c$ 的 $\operatorname{Gr}(\le c,D^\circ)$ 只是指出，未做图卡与 gcd 的细节。

## 残留价值

- **$W$-消去定理**（含证明）：铅笔只通过 $\Phi(W)\subseteq D^\circ$ 依赖 $W$；
- **$c=2$ 的坍缩到 $\mathbb P^1$**：这是可写进论文的强结构结论，也是判定算法的关键简化；
- 精确核对（9 个同 $\Phi$ 的 $W$ 全可行、1 个 $\Phi=0$ 不可行）；
- 复杂度瓶颈的**定位**：底，不是纤维。

## 相关文件

- [attempts/393](393_c2_fibre_and_base.md)（纤维与 $\mathcal B_{\rm pres}$）
- [attempts/404](../../decision_algorithms/attempts/404_expert108_audit.md)（专家 §14 的中间目标）
- [attempts/405](../../decision_algorithms/attempts/405_real_generic_point.md)（实一般点判据，与本文合起来支撑判定算法）
- [c406](../../../../tools/verification/c406_eliminate_W.py)（核对脚本）、[c399](../../../../tools/verification/c399_c2_feasible_q3.py)（可行设计）
