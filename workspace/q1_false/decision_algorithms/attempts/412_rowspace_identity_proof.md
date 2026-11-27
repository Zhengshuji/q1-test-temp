# 412 行空间恒等式的一般矩阵证明（专家 109 号 Priority 1 的收尾）

> 承接 411（专家 109 号审计）与 406（像约化）。专家 §10 Priority 1 明确要求：
> "Prove the row-space identity in the general matrix notation, not only on a concrete chart"。
> 本文件给出**一般情形**的完整证明，并核对 406 里"只有纸面 + 单卡数值"的缺口。

## 目标

在**不用任何具体实例**的情况下证明：对 $K_0$-split 设计，
$$\operatorname{row}\bigl(\lambda H-H_A\bigr)=\operatorname{row}\bigl(\lambda H_K-(H_A)_K\bigr)+\Phi(W)
\qquad(\forall\lambda),$$
并由此得到 411 的定理 4（约化可行性判据）。

## 设想与理由

这条恒等式其实是**两步**：

1. **$W$ 行的那两块**（一个恒等式、一个零）：$H$ 的 $W$ 行为零、$H_A$ 的 $W$ 行是 $\varphi_w$；
2. **堆叠矩阵的行空间 = 各块行空间之和**（纯线性代数）。

难点只在于把"行空间"这件事说清楚（用线性映射而不是矩阵下标），其余是计算。

## 做法

### 记号（按专家 110 号 §3.1 修正后的写法）

固定：
- 内积空间 $E$、子空间 $K_0\le E$、基 $N:\mathbb R^k\xrightarrow{\ \sim\ }K_0$（线性同构）；
- **$A$ 在 $K_0$ 上的分解**（两个投影，值域不同）：
  $$A|_{K_0}=P_{K_0}A|_{K_0}+P_{K_0^\perp}A|_{K_0}=:M+A_{21},$$
  即 $M=P_{K_0}A|_{K_0}$（值域 $\subseteq K_0$）、$A_{21}=P_{K_0^\perp}A|_{K_0}$（值域 $\subseteq K_0^\perp$）。
  **不能**把 $M$ 与 $A_{21}$ 当作同一空间上的普通矩阵相加；记号 $Ax=Mx+A_{21}x$（$x\in K_0$）只在
  直和 $E=K_0\perp K_0^\perp$ 的意义下成立；
- **两个泛函先定义在 $K_0$ 上**（不预先识别 $K_0^*$ 与 $\mathbb R^k$）：
  $$h_v:K_0\to\mathbb R,\ \ h_v(x)=\langle v,x\rangle;\qquad
  h^A_v:K_0\to\mathbb R,\ \ h^A_v(x)=\langle v,Ax\rangle .$$
  再**事后**用 $N$ 搬成 $\mathbb R^k$ 上的行向量：$H$ 的第 $v$ 行 $=h_v\circ N$、$H_A$ 的第 $v$ 行 $=h^A_v\circ N$。
  这一步是 $K_0^*\simeq\mathbb R^k$ 的唯一识别处（对应矩阵的"行"约定）；
- 对 $\lambda\in\mathbb R$，$\Psi_\lambda(v):=\lambda h_v-h^A_v\in K_0^*$——即 $\lambda H-H_A$ 的行泛函；
- $\Phi(W):=\operatorname{span}\{\varphi_w:w\in W\}$，其中 $\varphi_w(x)=\langle w,A_{21}x\rangle$（$x\in K_0$）；
- $V=D^{\perp_{K_0}}\oplus W$（$K_0$-split 假设），记 $P:=D^{\perp_{K_0}}$。

### 引理 1（$W$ 行的两块）

设 $w\in W\le K_0^\perp$。则对一切 $x\in K_0$：
$$h_w(x)=0\quad\text{且}\quad h^A_w(x)=\varphi_w(x).$$

*证明.* $Nx\in K_0$，而 $w\perp K_0$，故 $h_w(x)=\langle w,Nx\rangle=0$ ✓。
又 $ANx=M(Nx)+A_{21}(Nx)$，其中 $M(Nx)\in K_0\perp w$，故
$h^A_w(x)=\langle w,MNx\rangle+\langle w,A_{21}Nx\rangle=0+\varphi_w(x)$ ✓。$\square$

### 引理 2（行空间对直和的加性）

设 $\Psi:E\to F$ 线性、$V=P\oplus W$（子空间直和）。则
$$\Psi(V)=\Psi(P)+\Psi(W)\qquad(\text{子空间意义下的和}).$$

*证明.* $V\subseteq P+W$ ⟹ $\Psi(V)\subseteq\Psi(P)+\Psi(W)$；反之 $P,W\subseteq V$ ⟹ 反向包含 ✓。$\square$

### 定理（行空间恒等式，一般情形）

对一切 $\lambda\in\mathbb R$：
$$\boxed{\ \Psi_\lambda(V)=\Psi_\lambda(P)+\Phi(W)\ }$$
其中 $\Psi_\lambda(P)=\operatorname{row}\bigl(\lambda H_K-(H_A)_K\bigr)$、$\Psi_\lambda(W)=\operatorname{span}\{\Psi_\lambda(w):w\in W\}=\Phi(W)$。

*证明.* 由引理 2 只需算 $\Psi_\lambda(W)$。对 $w\in W$、$x\in K_0$：
$$\Psi_\lambda(w)(x)=\lambda h_w(x)-h^A_w(x)=0-\varphi_w(x),$$
由引理 1。故 $\Psi_\lambda(W)=\operatorname{span}\{-\varphi_w:w\in W\}=\Phi(W)$（符号不影响张成空间）✓。
$P$ 一侧 $\Psi_\lambda(P)$ 按定义就是 $\lambda H_K-(H_A)_K$ 的行空间 ✓。$\square$

**注意**：$\Psi_\lambda$ 在 $W$ 上与 $\lambda$ **无关**（恒等于 $-\varphi_\cdot$）——这正是"像约化"的全部内容：
$W$ 只通过 $\Phi(W)$ 影响铅笔，而 $\Phi(W)\subseteq D^\circ$（$\dim=c$）。

### 推论（411 的定理 4，重述）

固定 $D$。则
$$\exists W\ (W_0\subseteq W\subseteq T_D,\ \dim W=t)\ \text{使 }(5b)\iff
\exists\Phi\ \text{满足定理 3（411）且}\ \dim\bigl(\Psi_\lambda(P)+\Phi\bigr)=\omega\ \forall\lambda,$$
后者等价于 $\dim\Phi-\dim\bigl(\Phi\cap\Psi_\lambda(P)\bigr)=\omega-r_D(\lambda)$（$r_D(\lambda)=\dim\Psi_\lambda(P)$）。

*证明.* 由定理，$\operatorname{row}(\lambda H-H_A)=\Psi_\lambda(P)+\Phi(W)$；再用
$\dim(X+Y)=\dim X+\dim Y-\dim(X\cap Y)$ ✓。$\square$

## 进展

- 恒等式**在一般情形下证完**（引理 1 + 引理 2 + 定理），不再依赖具体实例；
- 证明只有三块内容：$W$ 行的两项计算、行空间对直和的加性、符号无关——没有隐藏假设；
- 与 406 的单卡核对（`c409`）一致：那里 $H$ 与 $s$ 无关、$H_A$ 的 $W$ 行线性于 $s$，
  正是引理 1 的两个结论（$W$ 行在 $H$ 中为零、在 $H_A$ 中是 $\varphi_w$）的具体表现。

## 最终结论

1. **Priority 1 收尾**：行空间恒等式有了**一般矩阵/泛函形式的完整证明**；
2. 像约化的三步链完整：$W$ 行计算（引理 1）→ 直和加性（引理 2）→ 恒等式（定理）→ 约化判据（推论）；
3. 该恒等式的"矩阵层"性质（$H$ 的 $W$ 行为零）是**结构性的**，与所选实例无关。

## 放弃原因

- 没有 Lean 化这条恒等式：它需要把"行空间"翻成矩阵 API（`Matrix.rowSpace`、块堆叠、坐标识别
  $K_0^*\simeq\mathbb R^k$），成本远高于本轮收益；数学内容（直和加性 + 两个内积计算）已在
  406 的两条 Lean 引理里覆盖；
- 没有讨论 $\operatorname{rank}H=\omega$ 与 $\rank\Psi_\lambda$ 的精确关系（$\lambda$ 依赖），
  那属于 408 的满秩图卡。

## 残留价值

- **一般形式的行空间恒等式证明**（专家 Priority 1 的验收项）；
- 把"行的泛函写法"与"矩阵写法"的桥写清（$h_v,h^A_v,\Psi_\lambda$），避免以后在坐标上纠缠；
- 与单卡数值核对的一致性说明。

## 相关文件

- [attempts/406](../../c_stratification/attempts/406_eliminate_W.md)（像约化简版，定理 2）
- [attempts/411](411_expert109_audit.md)（专家裁决；定理 3 与 4）
- [attempts/405](405_real_generic_point.md)（判据，用到 $\rank H=\omega$）
