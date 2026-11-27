# 超平面层的函数型观测器可行性：结构参数化、精确判定与固定参数复杂度

> 英文标题（暂定）：Functional-Observer Feasibility in the Hyperplane Layer: Structural Parameterization, Exact Decision, and Fixed-Parameter Complexity

# 1 引言

## 1.1 问题

给定 $A\in\mathbb R^{n\times n}$、$C\in\mathbb R^{p\times n}$ 与预设行 $L_0\in\mathbb R^{r_0\times n}$，求最小的行数 $q$，使存在 $R$ 令 $\mathcal L=[L_0;R]$（$q$ 行、行满秩）满足

$$(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},\qquad
(5b)\ \operatorname{rank}\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\ CA\\ C\end{bmatrix}=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix}\quad\forall\lambda\in\mathbb C .$$

这就是函数型观测器的可行性问题；$(5a)$ 是结构条件，$(5b)$ 是谱条件（后者等价于某个压缩铅笔的秩恒定性）。本文只处理它的**第一层**。

## 1.2 为什么是"超平面层"

压缩后，问题变成：找一个 $q$ 行的行空间 $V$，使

$$H=LN,\qquad H_A=LAN,\qquad \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda,$$

其中 $N$ 是 $K_0=\ker[C;CA]$ 的基、$k=\dim K_0$、$\omega=\operatorname{rank}H$。把差距记为

$$c:=k-\omega,\qquad \omega=\dim(V\cap K_0).$$

$c=0$ 时不需要保留任何方向；$c\ge1$ 时 $\ker H$ 是非零的，$V$ 必须落在它的正交补里——**从此几何开始起作用**。$c=1$ 是最小的非平凡情形：$\ker H$ 是一条直线，$V$ 被限制在一个余维 2 的子空间里。本文把这一层完全描述清楚。

## 1.3 动机：一个诱人的约化是错的

把压缩 $M=\pi_{K_0}A|_{K_0}$ 算出来之后，一个自然的想法是：**每个不同的实特征值取一个特征向量，逐个测试**。本文用精确计算说明这个约化不成立：在某个重复特征空间里，有的方向给出可行的观测器，有的方向则处处不可行。这既是本文第 6 节的内容，也是本文必须把**整个射影特征空间**作为参数的原因。

需要强调的是，这个反例只否定上面那一种约化；它**不**说明重复特征值情形困难，也**不**说明几何单谱是多项式可解的必要条件。

## 1.4 贡献

本文有四组结果。

**(A) 结构：可容许方向就是压缩的特征向量。** 在超平面层，$v$ 可容许当且仅当 $Mv=\mu v$ 对某个实特征值 $\mu$ 成立；带预设行时进一步限制到 $E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)$。这条把"选行空间"的连续问题化成了"先选方向、再在方向上选纤维"的两步。

**(B) 参数化与精确判定。** 层的参数空间是有限个**相对 Graßmann 丛**，纤维为 $\operatorname{Gr}(s-\delta,\mathcal Q_v/\overline V_{0,v})$，维数显式给出。在此参数化上，层的可行性可以用**逐图卡的精确代数计算**判定：坏集是闭的，且在不可约块上"生成好"等价于极大子式在函数域上无公根；满秩首项系数引理把"函数域上正次数"变成"整图卡处处坏"。

**(C) 固定 $p$ 的位复杂度。** 固定 $p$、并在**实谱几何单谱**（每个实特征值的特征空间一维）的输入上，判定是输入比特长的多项式（指数依赖 $p^2$）。这是 promise-class 结果：超出该子类时本文不作复杂度断言。

**(D) 反例。** 上面 1.3 的实例，附完整数据与精确证书。

此外有一个连接性结果：在超平面层，射影方向与既有压缩表述里的公共投影是**对偶**的——$[a]=\mathbb P(\operatorname{Ann}(U))$、$U=a^\circ$。

## 1.5 三条主张的区分

本文出现的三类断言强度不同，正文会逐处标明：

1. **整个层的精确判定**（第 4 节）：对任意输入都给出正确回答，但代价是精确算术的（不承诺多项式时间）；
2. **几何单谱子类上的多项式时间**（第 5 节）：promise-class，超出该子类时算法报告"超出范围"而不是 "不可行"；
3. **反例**（第 6 节）：只否定 1.3 中的那一类约化。

## 1.6 记号与约定

全篇使用标准欧氏内积（因此任何子空间上的限制都非退化，不需要额外假设）；输入矩阵取有理数，行空间 $\mathcal L$ 按定义**行满秩**。其余记号见第 2 节。

## 1.7 结构

第 2 节给压缩表述与判据；第 3 节给层的几何与参数化；第 4 节给精确判定；第 5 节给位复杂度；第 6 节给反例；第 7 节给与既有压缩表述的关系；附录给完整数据与精确证书。

# 2 预备与压缩表述

## 2.1 基本记号

$A\in\mathbb R^{n\times n}$，$C\in\mathbb R^{p\times n}$，$L_0\in\mathbb R^{r_0\times n}$，$\mathcal L=[L_0;R]\in\mathbb R^{q\times n}$ 行满秩，$V=\operatorname{row}\mathcal L$。记

$$K_0=\ker\begin{bmatrix}C\\ CA\end{bmatrix},\qquad k=\dim K_0,\qquad \rho=\operatorname{rank}\begin{bmatrix}C\\ CA\end{bmatrix}=n-k,$$

并固定 $K_0$ 的一个基 $N\in\mathbb R^{n\times k}$（附录 B.1 给出规范化取法）。这里 $\rho$ 是压缩数据的秩，本文的层号是 $c$，两者是不同的量。对行空间 $V$ 记

$$H=LN,\qquad H_A=LAN,\qquad \omega=\operatorname{rank}H,\qquad c=k-\omega .$$

**层**即 $c$。本文只处理 $c=1$，即 $\omega=k-1$。

## 2.2 压缩判据

$\mathcal L$ 可行（满足 $(5a)(5b)$）当且仅当

$$(5a')\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad (5b')\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda\in\mathbb C .$$

这是压缩表述下的等价形式：$(5a')$ 给出 $(5a)$，$\omega$ 与 $\operatorname{rank}[\mathcal L;CA;C]$ 一致；$(5b')$ 由铅笔的秩恒定给出。$(5a')$ 本身只用于把问题限定到参数空间上，本文不把它当作研究对象。

**引理 2.1（谱条件即公根条件）.** 设 $P(\lambda)=\lambda H-H_A$ 是 $q\times k$ 铅笔、$\omega=\operatorname{rank}H$。则在 $\operatorname{row}H_A\subseteq\operatorname{row}H$ 的前提下，$(5b')$ 等价于 $P$ 的全部 $\omega$ 阶极大子式没有公共复根。

*证明.* 若存在 $\lambda_0$ 使 $\operatorname{rank}P(\lambda_0)<\omega$，则由 $(5a')$ 的秩关系，$P(\lambda_0)$ 的 $\omega$ 阶极大子式全为零于 $\lambda_0$，即 $\lambda_0$ 是公共根；反之若 $\lambda_0$ 是公共根，则所有极大子式在 $\lambda_0$ 为零，秩严格下降。$\square$

## 2.3 站立假设

全篇假定：

1. 标准欧氏内积（子空间限制自动非退化）；
2. 输入取有理数；
3. $\mathcal L$ 行满秩，从而 $\operatorname{rank}L_0=r_0$（否则任何合法 $\mathcal L$ 都不存在，见命题 2.2）；
4. 参数化的处理需要 $K_0$ 的一个基；不同基给出的铅笔相互左乘可逆矩阵，可行性不变。

**命题 2.2（秩前置检查）.** 若 $\operatorname{rank}L_0<r_0$，则对任意 $q$ 都不存在行满秩的 $\mathcal L=[L_0;R]$，故实例不可行。

*证明.* $q=\operatorname{rank}\mathcal L\le\operatorname{rank}L_0+(q-r_0)<q$，矛盾。$\square$

## 2.4 层的方向与两个泛函

设 $V$ 在超平面层。则 $\dim(V\cap K_0)=k-1$，故 $\ker H$ 是一条直线 $\mathbb C v$，$v\in K_0\setminus\{0\}$，且 $V\subseteq U_v^\perp$，其中

$$U_v=\operatorname{span}\{v,Av\}.$$

把 $K_0$ 上的两个线性泛函记为

$$\varphi_v(u)=\langle u,v\rangle,\qquad \varphi_{Av}(u)=\langle u,Av\rangle\qquad(u\in K_0).$$

$V\subseteq U_v^\perp$ 等价于：每个 $x\in V$ 都消去 $v$ 与 $Av$，即 $xN$ 同时落在两个泛函的核里。

## 2.5 后文用到的量

$$M=\pi_{K_0}A|_{K_0},\quad A_{21}=\pi_{K_0^\perp}A|_{K_0},\quad E_\mu=\ker(M-\mu I),\quad E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN),$$

$$D_v=K_0\cap U_v^\perp,\quad \mathcal Q_v=U_v^\perp/D_v,\quad V_0=\operatorname{row}L_0,\quad \delta=\dim V_0-\dim(V_0\cap K_0),\quad s=q-k+1,$$

以及纤维的秩 $r(v)=\dim\mathcal Q_v$（第 3 节算出：特征方向为 $\rho$，非特征方向为 $\rho-1$）。

## 2.6 参数空间与"闭/开"的约定

后文把参数空间取成有限个**仿射图卡**的并：方向空间取射影空间的仿射卡，纤维取 Graßmann 的仿射卡。每个图卡是有理定义的实仿射空间，实点在其中 Zariski 稠密。这一约定在第 4 节用来把"generic 代数点"与"可实现实设计"接起来。

# 3 几何与参数化

本节研究超平面层（$c=k-\omega=1$）中可行设计的几何结构。核心结论是：超平面层的可容许设计构成有限个**相对 Graßmann 丛**，其底是压缩算子的实射影特征空间（经预设行条件限制后的子空间），纤维是显式的 Graßmann 流形。这一结构把层的可行性问题化归为有限个参数空间上的代数判定问题（第 4 节），并给出与既有压缩表述的精确对应（3.8 节）。

本节所有内积均指 $\mathbb{R}^n$ 上的标准欧氏内积 $\langle\cdot,\cdot\rangle$；正交补与正交投影相应地定义。

**本节的组织。** 参数化分两步完成，两步各自独立：

1. **方向**。层的核方向不是 $K_0$ 中的任意方向。3.2 节证明它必须且只须是压缩算子 $M=\pi_{K_0}A|_{K_0}$ 的实特征向量；3.3 节进一步把预设行的要求化为对特征空间的一个线性限制 $E_\mu^0$。这一步把"连续地选方向"化归为"在有限个射影特征空间上取点"。
2. **纤维**。方向固定之后，满足结构条件的行空间是 Graßmann 流形中的一族子空间（3.6 节），其维数由两个整数决定：商丛的秩 $r(v)$ 与预设行在商中的像维数 $\delta$。这一步把"选行空间"化归为"在 Graßmann 流形上取点"。

两部分的组合给出 3.7 节的完整参数化定理：层的参数空间是有限个相对 Graßmann 丛。3.8 节给出与既有压缩表述的对偶。第 4 节在上述参数空间上做代数判定。

---

## 3.0 记号与约定

**输入与设计。** 给定 $A\in\mathbb{R}^{n\times n}$、$C\in\mathbb{R}^{p\times n}$、$L_0\in\mathbb{R}^{r_0\times n}$。设计矩阵为行堆叠
$$
\mathcal{L}=\begin{pmatrix}L_0\\ R\end{pmatrix}\in\mathbb{R}^{q\times n},\qquad R\in\mathbb{R}^{(q-r_0)\times n},
$$
要求 $\mathcal{L}$ **行满秩**（于是 $\operatorname{rank}\mathcal{L}=q$）。记 $V=\operatorname{row}\mathcal{L}\subseteq\mathbb{R}^n$，$V_0=\operatorname{row}L_0\subseteq\mathbb{R}^n$。

**压缩数据。** 令
$$
K_0=\ker\begin{pmatrix}C\\ CA\end{pmatrix},\qquad k=\dim K_0,\qquad \rho=\operatorname{rank}\begin{pmatrix}C\\ CA\end{pmatrix}=n-k,
$$
并取 $N\in\mathbb{R}^{n\times k}$，其列构成 $K_0$ 的一组基。与 $\mathcal{L}$ 关联的压缩矩阵为
$$
H=\mathcal{L}N\in\mathbb{R}^{q\times k},\qquad H_A=\mathcal{L}AN\in\mathbb{R}^{q\times k},\qquad \omega=\operatorname{rank}H,
$$
压缩铅笔为 $P(\lambda)=\lambda H-H_A$。

**层。** 记 $c=k-\omega$。本节固定讨论**超平面层** $c=1$，即 $\omega=k-1$。

**压缩算子。** 记 $\pi_{K_0}$、$\pi_{K_0^\perp}$ 为到 $K_0$、$K_0^\perp$ 的正交投影，定义
$$
M=\pi_{K_0}A|_{K_0}\colon K_0\to K_0,\qquad A_{21}=\pi_{K_0^\perp}A|_{K_0}\colon K_0\to K_0^\perp ,
$$
于是对 $u\in K_0$ 有 $Au=Mu+A_{21}u$。对 $\mu\in\mathbb{R}$ 记 $E_\mu=\ker(M-\mu I)\subseteq K_0$ 为压缩算子的特征空间。

**与方向有关的基本对象。** 对 $v\in K_0\setminus\{0\}$ 记
$$
U_v=\operatorname{span}\{v,Av\}\subseteq\mathbb{R}^n,\qquad D_v=K_0\cap U_v^\perp\subseteq K_0,\qquad \mathcal{Q}_v=U_v^\perp/D_v .
$$
进一步的记号：$s=q-k+1$（纤维的参数维数平移），$E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)\subseteq E_\mu$（与预设行相容的方向空间），
$$
d_\mu^0=\dim E_\mu^0,\qquad h_\mu^0=\dim\bigl(E_\mu^0\cap\ker A_{21}\bigr),\qquad \delta=\dim V_0-\dim(V_0\cap K_0).
$$
$\operatorname{Gr}(m,Z)$ 表示向量空间 $Z$ 的 $m$ 维子空间构成的 Graßmann 流形。

**与框架记号的对照。** 本节的 $K_0$ 即整体框架中的不可观测子空间 $K$；本节的 $V$ 即框架中的行空间 $\mathcal{V}$；本节的 $V_0$ 即框架中的固定部分 $S$；本节的 $\rho$ 是观测空间 $\operatorname{row}[C;CA]$ 的维数（框架中记为 $j=n-k$），**不是**框架中用以编号层的 $\rho$。本节的层参数是 $c=k-\omega$；框架中按 $(\rho,c)$ 编号层的做法在本节不出现。

**站立假设。** $\operatorname{rank}L_0=r_0$。这是可行性的必要条件：若 $\operatorname{rank}L_0<r_0$，则 $\dim V\le \operatorname{rank}L_0+(q-r_0)<q$，与 $\mathcal{L}$ 行满秩矛盾，故任何 $q$ 都不可行（见命题 3.8）。

---

## 3.1 行空间的结构条件

本节把"层内的行空间"定义为满足以下三条结构条件的 $q$ 维子空间 $V$：

**(S1)** $V\subseteq U_v^\perp$，其中 $v\in K_0\setminus\{0\}$ 由 $V$ 确定；
**(S2)** $D_v\subseteq V$（等价地 $\dim(V\cap K_0)=k-1$）；
**(S3)** $V_0\subseteq V$。

条件 (S3) 来自原问题的定义（预设行必须保留）；(S2) 与 (S1) 一起给出 $V\cap K_0=D_v$。下述引理说明 $v$ 与 (S1) 是压缩条件的必然推论，(S2) 是层内设计的定义性正规化（与既有文献对超平面层的处理一致）。

> **引理 3.1（核方向与结构条件）.** 设 $\mathcal{L}$ 是满足 $c=1$ 且满足 $(5a)$ 的设计。则
> $$\ker\bigl(\mathcal{L}|_{K_0}\bigr)=K_0\cap V^\perp=\mathbb R v$$
> 对某个唯一的（相差非零倍数）$v\in K_0\setminus\{0\}$ 成立，并且
> $$\mathcal{L}v=0,\qquad \mathcal{L}Av=0,\qquad\text{即}\quad V\subseteq U_v^\perp .$$
> 若另外 $V_0\subseteq V$，则 $L_0v=L_0Av=0$。

*证明.* 由 $H=\mathcal{L}N$ 与 $\omega=k-1$ 得 $\dim\ker H=1$；而 $\ker H=\{c\in\mathbb{R}^k:\ \mathcal{L}Nc=0\}$，故 $\{\mathcal{L}u=0,\ u\in K_0\}=N\ker H$ 是一维的，取生成元 $v$。于是 $V\subseteq U_v^\perp$ 的第一部分 $\mathcal{L}v=0$ 成立。由 $(5a)$，存在矩阵 $X$ 使 $H_A=XH$；于是 $H_A c=XHc=0$ 对一切 $c\in\ker H$ 成立，取 $c$ 使 $Nc=v$ 得 $\mathcal{L}Av=H_Ac=0$。最后，若 $V_0\subseteq V$ 且 $V\subseteq U_v^\perp$，则 $V_0$ 的每行属于 $U_v^\perp$，即 $L_0v=0$、$L_0Av=0$。$\square$

*注.* $(5a)$ 在此处只用于一条推论 $H_Ac=0\ (c\in\ker H)$，即 $\ker H\subseteq\ker H_A$；这与压缩条件"$\operatorname{row}H_A\subseteq\operatorname{row}H$"等价。

*注 3.1.1（(S2) 的确切含义）.* 压缩矩阵的秩有另一个等价刻画：
$$\omega=\operatorname{rank}(\mathcal{L}N)=\dim\pi_{K_0}(V),$$
因为 $\mathcal{L}N$ 的列空间正是 $V$ 的诸行在 $K_0$ 上投影的坐标所张成的空间。由于 $V\cap K_0\subseteq\pi_{K_0}(V)$，恒有
$$\dim(V\cap K_0)\le\omega .$$
在层 $c=1$（$\omega=k-1$）中，这给出 $\dim(V\cap K_0)\le k-1$；而 (S2) 恰是把该不等式取等：$\dim(V\cap K_0)=k-1$。等号成立当且仅当 $\pi_{K_0}(V)\subseteq V$，即 $D_v\subseteq V$（因 $\pi_{K_0}(V)=D_v$）。这就是 3.1 节开头把 (S2) 称为"层内设计的定义性正规化"的确切理由。

> **引理 3.2（$D_v$ 的维数）.** 对任意 $v\in K_0\setminus\{0\}$，
> $$\dim(K_0\cap U_v^\perp)=k-\operatorname{rank}\{\varphi_v,\varphi_{Av}\},$$
> 其中 $\varphi_v(u)=\langle u,v\rangle$、$\varphi_{Av}(u)=\langle u,Av\rangle$ 是 $K_0$ 上的两个线性泛函。特别地 $\dim D_v\ge k-2$。

*证明.* $K_0\cap U_v^\perp=\{u\in K_0:\ \varphi_v(u)=\varphi_{Av}(u)=0\}$ 是两泛函的公共核，其维数为 $k$ 减去两泛函的秩。$\square$

---

## 3.2 方向定理

> **定理 3.3（方向定理）.** 设 $v\in K_0\setminus\{0\}$。则 $v$ 是层内可能出现的核方向（即存在满足 (S1) 的 $V$ 使 $\ker(\mathcal{L}|_{K_0})=\mathbb R v$）当且仅当 $v$ 是压缩算子 $M$ 的特征向量：
> $$Mv=\mu v\quad\text{对某个 }\mu\in\mathbb{R}.$$

*证明.* **（充分性）** 设 $Mv=\mu v$。则对一切 $u\in K_0$，
$$\varphi_{Av}(u)=\langle u,Av\rangle=\langle u,\pi_{K_0}(Av)\rangle=\langle u,Mv\rangle=\mu\langle u,v\rangle=\mu\,\varphi_v(u),$$
故 $\varphi_{Av}=\mu\varphi_v$，两泛函的秩为 $1$（因 $v\ne0$ 且内积正定给出 $\varphi_v\ne0$）。由引理 3.2，$\dim D_v=k-1$。取 $q$ 维子空间 $V$ 使 $D_v\subseteq V\subseteq U_v^\perp$（存在性需 $k-1\le q\le\dim U_v^\perp$，见引理 3.13 的非空条件）。此时 $\pi_{K_0}(V)\subseteq K_0\cap U_v^\perp=D_v$ 且 $\pi_{K_0}(V)\supseteq\pi_{K_0}(D_v)=D_v$，故 $\pi_{K_0}(V)=D_v$，于是 $\omega=\dim\pi_{K_0}(V)=k-1$，即 $c=1$；并且 $\ker(\mathcal{L}|_{K_0})=K_0\cap V^\perp=\mathbb R v$。故 $v$ 可作为层内设计的核方向。

**（必要性）** 设 $v$ 是某个层内设计的核方向。由引理 3.1 及结构条件 (S1)、(S2)，$V\subseteq U_v^\perp$ 且 $\dim(V\cap K_0)=k-1$。又 $V\cap K_0\subseteq K_0\cap U_v^\perp=D_v$，故 $\dim D_v\ge k-1$；结合引理 3.2，$\operatorname{rank}\{\varphi_v,\varphi_{Av}\}\le1$。由于 $\varphi_v\ne0$，存在 $\mu\in\mathbb{R}$ 使 $\varphi_{Av}=\mu\varphi_v$，即对一切 $u\in K_0$ 有 $\langle u,Av-\mu v\rangle=0$，从而 $Av-\mu v\in K_0^\perp$。另一方面，$Av-\mu v=(Mv-\mu v)+A_{21}v$，其中 $Mv-\mu v\in K_0$、$A_{21}v\in K_0^\perp$，故 $Av-\mu v$ 的 $K_0$ 分量是 $Mv-\mu v$；由 $Av-\mu v\in K_0^\perp$ 得 $Mv-\mu v=0$，即 $Mv=\mu v$。

最后 $\mu$ 是实数：$v$ 是实向量且 $v\ne0$，$M$ 是实算子，故 $Mv=\mu v$ 中的 $\mu$ 必为实数。$\square$

*注 3.4.* 定理 3.3 的充分性部分（即每个特征向量方向都可容许）只用到结构条件，与谱条件无关：它说明**方向集**是压缩算子的实射影特征空间之并
$$
\mathcal{D}=\bigcup_{\mu\in\operatorname{Spec}_{\mathbb{R}}(M)}\mathbb{P}(E_\mu),
$$
而不是 $K_0$ 中任意方向。特征值有限，但当 $\dim E_\mu>1$ 时 $\mathbb{P}(E_\mu)$ 是正维射影空间，方向集因此**不是**有限集。

*注 3.4.1（可容许性的等价形式）.* 由定理 3.3 的证明，以下四条等价：(i) $v$ 可作为层内设计的核方向；(ii) $Mv\in\operatorname{span}(v)$；(iii) 两泛函 $\varphi_v,\varphi_{Av}$ 成比例；(iv) $\dim D_v=k-1$。其中 (ii) 与 (iii) 的等价是逐点线性代数，(iii) 与 (iv) 的等价来自 $\dim D_v=k-\operatorname{rank}\{\varphi_v,\varphi_{Av}\}$。这四条形式在 3.6、3.7 两节中分别用到：几何论证用 (i)，纤维的构造用 (iv)。

---

## 3.3 与预设行相容的方向空间

预设行条件 $V_0\subseteq V$ 把方向集进一步限制为

> **定义 3.5.** 对 $\mu\in\operatorname{Spec}_{\mathbb{R}}(M)$ 记
> $$E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)=\{v\in E_\mu:\ L_0v=0,\ L_0Av=0\}.$$

由引理 3.1，$v$ 能成为带预设行的层内设计的核方向必须 $L_0v=L_0Av=0$，故必要条件是 $v\in E_\mu^0$。

> **引理 3.6（预设行相容）.** 设 $\mu\in\operatorname{Spec}_{\mathbb{R}}(M)$、$v\in E_\mu^0\setminus\{0\}$。则
> $$V_0\subseteq U_v^\perp,\qquad V_0\cap D_v=V_0\cap K_0,\qquad \delta=\dim V_0-\dim(V_0\cap K_0)\ \text{与 }v\text{ 无关}.$$
> 并且 $\overline{V}_{0,v}:=(V_0+D_v)/D_v\subseteq\mathcal{Q}_v$ 的维数等于 $\delta$。

*证明.* $v\in E_\mu^0$ 的定义即 $L_0v=L_0Av=0$，故 $V_0$ 的每行消去 $v$ 与 $Av$，即 $V_0\subseteq U_v^\perp$。于是
$$V_0\cap D_v=V_0\cap K_0\cap U_v^\perp=V_0\cap K_0,$$
其中第二个等号用到 $V_0\subseteq U_v^\perp$。右端与 $v$ 无关，故 $\delta$ 固定。最后，$\overline{V}_{0,v}$ 的维数为 $\dim(V_0+D_v)-\dim D_v=\dim V_0-\dim(V_0\cap D_v)=\delta$。$\square$

> **推论 3.7（空层的否定证书）.** 若 $E_\mu^0=\{0\}$ 对一切 $\mu\in\operatorname{Spec}_{\mathbb{R}}(M)$ 成立，则超平面层为空，即该实例对任何 $q$ 都不可行。

*证明.* 由引理 3.1，层内设计的核方向必属于某个 $E_\mu^0$（$\mu$ 实），故无方向即无设计。$\square$

> **命题 3.8（预设行秩的前置检查）.** 若 $\operatorname{rank}L_0<r_0$，则对任意 $q$ 都不存在行满秩的 $\mathcal{L}=[L_0;R]$，故实例不可行。

*证明.* $\dim V\le\operatorname{rank}L_0+(q-r_0)<q$ 与 $\dim V=q$ 矛盾。$\square$

*注.* 命题 3.8 说明 3.0 节的站立假设 $\operatorname{rank}L_0=r_0$ 不是额外限制：它由问题的行满秩要求强制。

---

## 3.4 特征方向与非特征方向的分层

> **引理 3.9（特征方向的线性刻画）.** 设 $\mu\in\operatorname{Spec}_{\mathbb{R}}(M)$、$v\in E_\mu\setminus\{0\}$。则
> $$Av\in\operatorname{span}(v)\iff A_{21}v=0 .$$

*证明.* 由 $Av=Mv+A_{21}v=\mu v+A_{21}v$ 且 $A_{21}v\in K_0^\perp$、$\mu v\in K_0$，得 $Av\in\operatorname{span}(v)\subseteq K_0$ 当且仅当 $A_{21}v$ 的 $K_0^\perp$ 分量为零。$\square$

> **命题 3.10（特征方向构成线性子空间）.** 在 $E_\mu$ 中，特征方向构成线性子空间
> $$E_\mu^{\mathrm{eig}}:=E_\mu\cap\ker A_{21},$$
> 其射影化是射影空间 $\mathbb{P}(E_\mu^{\mathrm{eig}})\subseteq\mathbb{P}(E_\mu)$；非特征方向构成其补集，是 $\mathbb{P}(E_\mu)$ 中的非空 Zariski 开集（当 $E_\mu^{\mathrm{eig}}\ne E_\mu$ 时）。在与预设行相容的情形，
> $$B_\mu^{\mathrm{eig}}=\mathbb{P}\bigl(E_\mu^0\cap\ker A_{21}\bigr),\qquad B_\mu^{\mathrm{non}}=\mathbb{P}(E_\mu^0)\setminus B_\mu^{\mathrm{eig}},$$
> 两者不相交且覆盖 $\mathbb{P}(E_\mu^0)$。

*证明.* $\ker A_{21}$ 是线性子空间，与 $E_\mu$ 之交仍线性；射影化保持线性结构。非特征方向是其补集，为开集；其非空性等价于 $E_\mu^{\mathrm{eig}}\ne E_\mu$。$\square$

> **引理 3.10.1（两支的 $U_v$ 维数）.** 设 $v\in E_\mu\setminus\{0\}$。若 $A_{21}v=0$ 则 $U_v=\operatorname{span}(v)$，$\dim U_v=1$；若 $A_{21}v\ne0$ 则 $v$ 与 $Av$ 线性无关，$\dim U_v=2$。相应地
> $$\dim U_v^\perp=\begin{cases}n-1,& A_{21}v=0,\\ n-2,& A_{21}v\ne0.\end{cases}$$

*证明.* 若 $A_{21}v=0$，则 $Av=\mu v$，故 $U_v=\operatorname{span}(v)$。若 $A_{21}v\ne0$，则 $Av-\mu v\ne0$ 且与 $v$ 正交（$\langle v,Av-\mu v\rangle=\langle v,A_{21}v\rangle=0$，因 $A_{21}v\in K_0^\perp$ 且 $v\in K_0$），故 $v$ 与 $Av$ 线性无关。正交补的维数由 $n-\dim U_v$ 给出。$\square$

*注 3.11.* 按 $A_{21}|_{E_\mu^0}$ 的秩可将 $B_\mu^{\mathrm{eig}}$ 与 $B_\mu^{\mathrm{non}}$ 的非空性分为三种情形：秩为零时全部方向都是特征方向（$B_\mu^{\mathrm{non}}=\varnothing$）；秩等于 $\dim E_\mu^0$ 时无特征方向（$B_\mu^{\mathrm{eig}}=\varnothing$）；介于两者之间时两支都非空。该分类可直接由 $E_\mu^0$ 上的线性代数得到，将在第 4 节的算法中作为第一步筛选使用。

---

## 3.5 商丛的常秩性

> **引理 3.12（商丛与纤维维数）.** 在 $\mathbb{P}(E_\mu^0)$ 上，映射 $v\mapsto D_v$ 与 $v\mapsto\mathcal{Q}_v=U_v^\perp/D_v$ 是常秩向量丛，其秩分别为 $k-1$ 与
> $$r(v)=\begin{cases}\rho,& v\ \text{为特征方向},\\[2pt] \rho-1,& v\ \text{为非特征方向}.\end{cases}$$

*证明.* 由定理 3.3，在 $\mathbb{P}(E_\mu^0)$ 上两泛函成比例（比例即 $\mu$），故其秩恒为 $1$，$D_v$ 的维数恒为 $k-1$。而
$$\dim\mathcal{Q}_v=\dim U_v^\perp-\dim D_v=(n-\dim U_v)-(k-1),$$
且 $\dim U_v=1$ 或 $2$ 由命题 3.10 的两支给出；代入 $\rho=n-k$ 即得所述值。常秩性给出丛结构。$\square$

*注.* 特别地 $r(v)\le\rho\le 2p$：这是第 5 节复杂度估计的出发点。

---

## 3.6 纤维

> **引理 3.13（纤维）.** 设 $\mu\in\operatorname{Spec}_{\mathbb{R}}(M)$、$v\in E_\mu^0\setminus\{0\}$，并设 $\delta\le s\le r(v)$。则固定方向 $[v]$ 后，满足 (S1)–(S3) 且 $\dim V=q$ 的行空间恰为
> $$\bigl\{V:\ V_0+D_v\subseteq V\subseteq U_v^\perp,\ \dim V=q\bigr\},$$
> 它通过 $V\mapsto V/D_v$ 与
> $$\operatorname{Gr}\bigl(s-\delta,\ \mathcal{Q}_v/\overline{V}_{0,v}\bigr)$$
> 一一对应，其维数为 $(s-\delta)\bigl(r(v)-s\bigr)$。该纤维非空当且仅当 $\delta\le s\le r(v)$。

*证明.* 设 $V$ 满足结构条件。由 $D_v\subseteq V\subseteq U_v^\perp$ 得 $V\cap K_0\subseteq K_0\cap U_v^\perp=D_v$，结合 $D_v\subseteq V$ 得 $V\cap K_0=D_v$，故 (S2) 自动满足；反之 (S2) 与 $V\subseteq U_v^\perp$ 给出 $V\cap K_0=D_v$。于是 $V/D_v$ 是 $\mathcal{Q}_v$ 中维数为 $\dim V-\dim D_v=q-k+1=s$ 的子空间，且包含 $\overline{V}_{0,v}=(V_0+D_v)/D_v$（因 $V_0\subseteq V$）。含固定 $\delta$ 维子空间的 $s$ 维子空间与商空间 $\mathcal{Q}_v/\overline{V}_{0,v}$ 中的 $(s-\delta)$ 维子空间一一对应，后者正是 Graßmann 流形。维数按 Graßmann 流形的标准公式 $(s-\delta)\bigl((r(v)-\delta)-(s-\delta)\bigr)=(s-\delta)(r(v)-s)$ 计算；非空条件由 $0\le s-\delta\le r(v)-\delta$ 得到。$\square$

*注 3.13.1（两个免费的必要条件）.* 引理 3.13 的非空条件与引理 3.12 的取值给出四条只依赖整数的不等式：
$$\delta\le s,\qquad k-1\le q,\qquad q\le k-1+\rho=n-1\ \text{（特征支）},\qquad q\le n-2\ \text{（非特征支）}.$$
它们在参数化之前即可检验，且不需要任何铅笔计算；违反其中任何一条就排除了相应的支，若所有支都被排除则层为空（配合推论 3.7 得到完整的结构性否定筛查）。

*注 3.13.2（无预设行的特例）.* 当 $V_0=\{0\}$（即 $L_0$ 为空）时 $\delta=0$，纤维化为 $\operatorname{Gr}(s,\mathcal{Q}_v)$；当 $V_0\subseteq K_0$（预设行本身落在不可观测子空间内）时同样有 $\delta=0$。这两种情形下纤维就是商丛的 Graßmann 化，参数维数为 $s\,(r(v)-s)$。

> **引理 3.14（全行秩归一化）.** 设存在层内设计（满足 (S1)–(S3) 与 $\dim V\le q$）且 $q\le\dim U_v^\perp$。则存在满足 (S1)–(S3)、$\dim V=q$ 的设计，且其铅笔与压缩条件不变。

*证明.* 取 $\tilde V$ 使 $V\subseteq\tilde V\subseteq U_v^\perp$ 且 $\dim\tilde V=q$（存在性由 $q\le\dim U_v^\perp$ 给出）。则 $D_v\subseteq\tilde V$、$V_0\subseteq\tilde V$、$\tilde V\subseteq U_v^\perp$，即 (S1)–(S3) 保持；$\tilde V\cap K_0=D_v$ 亦保持，故压缩矩阵 $\tilde H$ 的秩仍为 $k-1=\omega$。又 $\tilde V$ 的每行消去 $v$ 与 $Av$，于是 $\operatorname{row}\tilde H_A\subseteq\operatorname{row}\tilde H$ 保持（$(5a)$）。铅笔的条件 $(5b)$ 在行空间扩张下保持：$(5b)$ 等价于 $\operatorname{rank}P(\lambda)=\omega$ 对一切 $\lambda$；扩张只增加 $P$ 的行，秩不下降，而 $\omega$ 是上界，故秩恒为 $\omega$。$\square$

---

## 3.7 完整参数化定理

> **定理 3.15（超平面层的完整参数化）.** 设站立假设 $\operatorname{rank}L_0=r_0$ 成立，$c=1$。则超平面层的行空间参数空间是下述有限并：
> $$\bigsqcup_{\mu\in\operatorname{Spec}_{\mathbb{R}}(M)}\Bigl(\ \operatorname{Gr}_{B_\mu^{\mathrm{eig}}}\bigl(s-\delta,\ \mathcal{Q}^{\mathrm{eig}}/\overline{V}_0\bigr)\ \sqcup\ \operatorname{Gr}_{B_\mu^{\mathrm{non}}}\bigl(s-\delta,\ \mathcal{Q}^{\mathrm{non}}/\overline{V}_0\bigr)\Bigr),$$
> 其中 $B_\mu^{\mathrm{eig}}$、$B_\mu^{\mathrm{non}}$ 如命题 3.10，$\mathcal{Q}^{\mathrm{eig}}$、$\mathcal{Q}^{\mathrm{non}}$ 是引理 3.12 给出的两个常秩商丛，$\overline{V}_0$ 是引理 3.6 给出的常秩子丛。每一支是**局部闭实代数底上的代数相对 Graßmann 丛**，其维数分别为
> $$\dim X_\mu^{\mathrm{eig}}=h_\mu^0-1+(s-\delta)(\rho-s),\qquad
> \dim X_\mu^{\mathrm{non}}=d_\mu^0-1+(s-\delta)(\rho-1-s),$$
> 相应的非空条件为
> $$\delta\le s\le\rho\quad\text{（特征支）},\qquad \delta\le s\le\rho-1\quad\text{（非特征支）}.$$
> 每个非空支不可约。

*证明.* 由定理 3.3，层内设计的核方向落在 $\mathbb{P}(E_\mu)$ 上；由引理 3.1 与引理 3.6，带预设行时进一步落在 $\mathbb{P}(E_\mu^0)$ 上。命题 3.10 把每个 $\mathbb{P}(E_\mu^0)$ 分成两支；引理 3.13 在每支上给出纤维，引理 3.12 保证纤维维数在支上恒定，故纤维构成相对 Graßmann 丛。底是射影空间（特征支）或射影空间的开子集（非特征支），它们在实点集上不可约；底不可约且纤维维数恒定时丛不可约。维数按丛的维数公式：$\dim(\text{底})+\dim(\text{纤维})$，其中底维数分别为 $h_\mu^0-1$ 与 $d_\mu^0-1$（后者按开子集维数等于包络的维数），纤维维数由引理 3.13 给出。非空条件由引理 3.13 的 $\delta\le s\le r(v)$ 与引理 3.12 的两个取值代入得到。$\square$

*注 3.15.1（行数 $q=k$ 的特例）.* 当 $q=k$ 时 $s=q-k+1=1$；若此外 $\delta=0$（无预设行或预设行落在 $K_0$ 内），纤维为 $\operatorname{Gr}(1,\mathcal{Q}_v)=\mathbb{P}(\mathcal{Q}_v)$，即一个射影空间，参数维数 $r(v)-1$。$q>k$ 时纤维是维数 $s-\delta\ge2$ 的 Graßmann 流形，不再是射影空间。

*注 3.16（空层与退化情形）.* 约定 $\dim\varnothing=-1$ 时不作维数声明；具体地：若 $h_\mu^0=0$ 则特征支为空；若 $d_\mu^0=0$ 则两支皆空（此时 $E_\mu^0=\{0\}$）。所有支的空与非空可仅由 $(\delta,s,\rho,h_\mu^0,d_\mu^0)$ 判断，不需要铅笔计算。

*注 3.17（参数维数）.* 纤维参数维数满足
$$d_{\mathrm{fib}}=(s-\delta)(r(v)-s)\le\frac{r(v)^2}{4}\le p^2,$$
与 $n$ 无关。若此外 $\dim E_\mu^0=1$ 对一切实特征值成立（"实谱的几何单谱"），则每个底是单点，全部参数都落在纤维上，参数空间的总维数不超过 $p^2$。反之若某个 $\dim E_\mu^0>1$，底贡献 $d_\mu^0-1$ 个额外参数，该数值随 $n$ 增长。

*注 3.18（实点）.* 定理 3.15 中各支的底与纤维都带标准有理实图卡：射影空间与 Graßmann 流形的仿射图卡是 $\mathbb{R}$ 上的仿射空间，其实点在其中 Zariski 稠密。第 4 节由此把"函数域上的代数条件"翻译为"存在实设计"。

---

## 3.8 与压缩表述的对偶

设 $\mathsf{M}=[N\ \ AN]\in\mathbb{R}^{n\times 2k}$，并定义线性映射
$$
\Phi\colon\mathbb{R}^n\longrightarrow\mathbb{R}^{k}\oplus\mathbb{R}^{k},\qquad x\longmapsto (xN,\ xAN),
$$
（按行向量约定）。对行空间 $V$ 记 $W=\Phi(V)=\operatorname{row}(V\mathsf{M})\subseteq\mathbb{R}^{2k}$，记 $\pi_1,\pi_2$ 为 $\mathbb{R}^{2k}$ 到两个 $\mathbb{R}^k$ 因子的坐标投影。对 $a\in\mathbb{R}^k$ 记 $a^\circ=\{h\in(\mathbb{R}^k)^*:\ h(a)=0\}$。

既有压缩表述（Paper II）中，可行设计由 $W$ 刻画：$\pi_2(W)\subseteq\pi_1(W)$，$\dim\pi_\lambda(W)=\dim\pi_1(W)$ 对一切 $\lambda$，且对可行设计 $\pi_1(W)=\pi_2(W)=:U$、$\dim U=\omega$、$\omega+1\le\dim W\le 2\omega$。

> **命题 3.19（方向对偶）.** 设 $V$ 是超平面层内的行空间，方向为 $v=Na$。则
> $$W\subseteq a^\circ\times a^\circ .$$
> 若进一步 $\pi_1(W)=\pi_2(W)=U$ 且 $\dim U=k-1$，则
> $$U=a^\circ,\qquad [a]=\mathbb{P}\bigl(\operatorname{Ann}(U)\bigr),$$
> 即压缩表述中的公共投影与本节的方向是同一个对象的对偶描述。

*证明.* 由 $V\subseteq U_v^\perp$，每行 $x\in V$ 满足 $xv=0$、$xAv=0$；写成 $v=Na$ 即 $xNa=0$、$xANa=0$，故 $W\subseteq a^\circ\times a^\circ$，从而 $\pi_1(W),\pi_2(W)\subseteq a^\circ$。若两者都等于 $U$ 且 $\dim U=k-1=\dim a^\circ$，则 $U=a^\circ$。$a^\circ$ 的零化子在 $(\mathbb{R}^k)^{**}\cong\mathbb{R}^k$ 中是一维的，由 $a$ 张成，故射影点 $[a]$ 由 $U$ 唯一确定。$\square$

> **命题 3.20（$V\mapsto W$ 的纤维）.** 映射 $\Phi$ 的核为
> $$\ker\Phi=\{x:\ xN=0,\ xAN=0\}=(K_0+AK_0)^\perp .$$
> 固定 $W$，记 $T_W=\Phi^{-1}(W)$。设 $S=V_0+D_v$ 且 $S\subseteq T_W$，则 $\Phi$ 诱导
> $$\overline{\Phi}\colon T_W/S\longrightarrow W/\Phi(S),$$
> 而 $W$ 上的提升恰为满足
> $$\overline{\Phi}\bigl(\overline{V}\bigr)=W/\Phi(S),\qquad \dim\overline{V}=q-\dim S$$
> 的子空间 $\overline{V}=V/S\subseteq T_W/S$。因此提升集是 Graßmann 流形中的一个**满射轨迹**，一般不是整个 Graßmann 流形。

*证明.* $\ker\Phi$ 的刻画由定义直接得到；而 $xN=0$ 与 $xAN=0$ 等价于 $x\perp K_0$ 且 $x\perp AK_0$，即 $x\in(K_0+AK_0)^\perp$。设 $V\subseteq T_W$，则 $\Phi(V)=W$ 当且仅当 $\Phi$ 在 $V$ 上的像等于 $W$；商掉 $S$ 后该条件化为 $\overline\Phi(\overline V)=W/\Phi(S)$，其维数条件由 $\dim V=q$ 与 $\dim S$ 给出。$\square$

*注 3.21.* $\Phi$ 一般不单射：$\ker\Phi=(K_0+AK_0)^\perp$ 的正交维数即纤维的自由度。压缩表述只依赖 $W$，因而在判定可行性时更经济；而本节的环境表述保留了预设行与行数约束所需的信息。两者不能互相替代：命题 3.20 说明给定 $W$ 时提升的存在性是一个附加条件，故"$W$ 可行"不能直接推出"存在满足预设行条件的行空间"。

*注 3.22（与压缩表述中维数界的关系）.* 在压缩表述中，可行设计的 $W$ 满足 $\omega+1\le\dim W\le 2\omega$（引用 Paper II）。在超平面层 $\omega=k-1$，故该界为 $k\le\dim W\le 2k-2$。与本节参数的关系是：$\pi_1(W)=N^{\mathsf T}V$，即 $\pi_{K_0}(V)$ 在基 $N$ 下的坐标像，故 $\dim\pi_1(W)=\dim\pi_{K_0}(V)=\omega=k-1$；$\dim W$ 超出 $\omega$ 的部分由 $\pi_2(W)$ 相对 $\pi_1(W)$ 的"增量"决定，即由 $\{N^{\mathsf T}A^{\mathsf T}x:\ x\in V\}$ 相对 $N^{\mathsf T}V$ 的增加量决定。因此 $\dim W$ 不需要独立计算，它由 $W$ 的任一基直接给出。

---

## 3.9 本节的作用

本节的结果把超平面层的可行性问题化为下述形式：层的参数空间是有限个不可约簇（定理 3.15），每个簇都带显式的有理实图卡（注 3.18）；层非空当且仅当某个簇上存在一个点使其铅笔满足 $(5b)$。由于每个簇上的"坏点集"是代数闭集（第 4 节证明），逐图卡的函数域计算即可给出精确判定；而参数维数 $\le p^2$（注 3.17）是第 5 节复杂度估计的基础。结构性的否定证书（推论 3.7、命题 3.8、注 3.13.1）在任何铅笔计算之前就能排除一部分实例。

---

## 3.10 本节结果汇总

| 编号 | 内容 | 状态 |
|---|---|---|
| 引理 3.1 | 核方向与结构条件（$\ker(\mathcal{L}|_{K_0})=\mathbb R v$，$V\subseteq U_v^\perp$） | 已证（本工作） |
| 注 3.1.1 | (S2) 的确切含义：$\dim(V\cap K_0)=\omega$ | 已证（本工作） |
| 引理 3.2 | $D_v$ 的维数公式 | 已证（本工作） |
| 定理 3.3 | 方向定理：可容许方向 $\iff$ $M$ 的实特征向量 | 已证（本工作） |
| 注 3.4 | 方向集是实射影特征空间之并（非有限集） | 已证（本工作） |
| 注 3.4.1 | 可容许性的四条等价形式 | 已证（本工作） |
| 定义 3.5 | 预设行相容空间 $E_\mu^0$ | 定义 |
| 引理 3.6 | 预设行相容：$V_0\subseteq U_v^\perp$ 自动、$V_0\cap D_v=V_0\cap K_0$、$\delta$ 固定 | 已证（本工作） |
| 推论 3.7 | 空层的否定证书（$E_\mu^0=\{0\}$） | 已证（本工作） |
| 命题 3.8 | 预设行秩的前置检查 | 已证（本工作） |
| 引理 3.9 | 特征方向的线性刻画 $Av\in\operatorname{span}(v)\iff A_{21}v=0$ | 已证（本工作） |
| 命题 3.10 | 特征方向构成射影线性子空间，非特征方向是其开补 | 已证（本工作） |
| 引理 3.10.1 | 两支的 $U_v$ 维数（$1$ 或 $2$） | 已证（本工作） |
| 注 3.11 | 按 $\operatorname{rank}(A_{21}|_{E_\mu^0})$ 的三情形分类 | 已证（本工作） |
| 引理 3.12 | 商丛常秩：$r(v)=\rho$ 或 $\rho-1$ | 已证（本工作） |
| 引理 3.13 | 纤维 $=\operatorname{Gr}(s-\delta,\mathcal{Q}_v/\overline{V}_{0,v})$，维数与非空条件 | 已证（本工作） |
| 注 3.13.1 | 四条只依赖整数的免费必要条件 | 已证（本工作） |
| 注 3.13.2 | 无预设行（$\delta=0$）时纤维退化为 $\operatorname{Gr}(s,\mathcal{Q}_v)$ | 已证（本工作） |
| 引理 3.14 | 全行秩归一化 | 已证（本工作） |
| 定理 3.15 | 完整参数化：有限个相对 Graßmann 丛、维数、非空条件、不可约性 | 已证（本工作） |
| 注 3.15.1 | $q=k$、$\delta=0$ 时纤维退化为射影空间 | 已证（本工作） |
| 注 3.16 | 空层与退化情形的显式处理 | 已证（本工作） |
| 注 3.17 | 纤维参数维数 $\le p^2$；几何单谱时底退化为点 | 已证（本工作） |
| 注 3.18 | 标准有理实图卡与实点稠密性 | 已证（本工作） |
| 命题 3.19 | 方向对偶（$U=a^\circ$，$[a]=\mathbb{P}(\operatorname{Ann}(U))$） | 已证（本工作） |
| 命题 3.20 | $V\mapsto W$ 的纤维是满射轨迹 | 已证（本工作） |
| 注 3.21 | 压缩表述与环境表述不可互相替代 | 已证（本工作） |
| 注 3.22 | $\dim W$ 与 Paper II 维数界的关系 | 已证（本工作） |

**结构条件的来源。** (S3) 来自原问题的定义；(S1) 与核方向 $\mathbb R v$ 由压缩条件 $c=1$ 与 $(5a)$ 推出（引理 3.1）；(S2)（等价于 $\dim(V\cap K_0)=k-1$）是超平面层内设计的定义性正规化，与既有文献对压缩问题的处理一致；引理 3.14 说明在 $q\le\dim U_v^\perp$ 时可以把行空间补到 $q$ 维而不破坏可行性。

# 4 精确代数判定

本节把第 3 节的参数化转化为一个可执行的判定程序。全部工具都是精确算术（有理数、代数数、多元多项式），不含浮点近似。

判定分两层。第一层是**几何的**：坏集（存在公共根的参数点集）是闭集，因此"块上是否有好点"只取决于该块的一般点；第二层是**代数的**：在每张图表上，一般点是否有公共根由极大子式在函数域上的最大公因式决定，而"正次数"这一支之所以能推广到整张图表，靠的是超平面层特有的秩不变量 $\operatorname{rank}H\equiv\omega$。

需要强调本节的定位。本节给出的是**整个层的精确判定**（定理 4.1–4.2、命题 4.3、引理 4.6、命题 4.13）：只要所有图表都被枚举并算完，判定结果就是确定的。本节**不**给出任何复杂度断言；"几何单谱子类上多项式时间"是第 5 节的内容，它额外依赖一个关于特征空间维数的假设。两者是不同的命题，行文与结论都必须分开。

## 4.0 记号与约定

沿用第 3 节。$A\in\mathbb C^{n\times n}$，$C\in\mathbb C^{p\times n}$，$L_0\in\mathbb C^{r_0\times n}$ 为预设行，
$$\mathcal L=\binom{L_0}{R},\qquad V=\operatorname{row}\mathcal L,\qquad V_0=\operatorname{row}L_0,$$
$q$ 为行数，$K_0=\ker[C;CA]$，$k=\dim K_0$，$N$ 为 $K_0$ 的基（$n\times k$），
$$H=LN,\qquad H_A=LAN,\qquad \omega=\operatorname{rank}H,\qquad \rho=\operatorname{rank}[C;CA]=n-k .$$
超平面层指 $\omega=k-1$。记 $s=q-k+1$，
$$\delta=\dim V_0-\dim(V_0\cap K_0),\qquad m=s-\delta,\qquad R=r(v)-\delta,$$
其中 $r(v)=\rho$（特征方向）或 $r(v)=\rho-1$（非特征方向）。由第 3 节的纤维引理，$V$ 可容许当且仅当（在固定方向 $[v]$ 上）
$$V_0+D_v\subseteq V\subseteq U_v^\perp,\qquad \dim V=q,$$
其在商 $\mathcal Q_v=U_v^\perp/D_v$ 中的像是一个包含 $\overline V_{0,v}$ 的 $s$ 维子空间，即纤维为 $\operatorname{Gr}(m,R)$。

对参数点 $X$ 记 $L(X)$ 为对应的行矩阵，并记
$$P(X,\lambda)=\lambda H(X)-H_A(X),\qquad H(X)=L(X)N,\quad H_A(X)=L(X)AN .$$
$P$ 是 $q\times k$ 的铅笔，$\omega=k-1$。用 $I$ 同时索引 $\omega$ 个行与 $\omega$ 个列，$m_I(X,\lambda)$ 表示对应的 $\omega$ 阶极大子式。

**约定（图表的取法）.** 本节的"图表"$\mathcal X$ 总是指层的一个参数图表，即其上每一点都满足层的定义条件 $\operatorname{rank}H=\omega$。层由 $c=k-\omega=1$ 定义，故 $\operatorname{rank}H=\omega$ 是层的定义的一部分，不是额外假设。在第 3 节的参数化定理中，它是一个行列式条件；取图表时把它实现为过滤。

**定义（好点与坏点）.** 参数点 $X$ 称为**好**的，若 $\operatorname{rank}P(X,\lambda)=\omega$ 对一切 $\lambda\in\mathbb C$ 成立；否则称为**坏**的。坏点的集合记为 $\mathcal B\subseteq\mathcal X$。

坏性的等价刻画：$X$ 坏 $\iff$ 存在 $\lambda_0\in\mathbb C$ 使全部 $m_I(X,\lambda_0)=0$。只需取一个非零的 $\omega$ 阶子式：$\operatorname{rank}P(X,\lambda)<\omega$ 当且仅当所有 $\omega$ 阶子式在 $\lambda$ 处为零。

## 4.1 坏集的闭性

**定理 4.1（坏集闭）.** 设 $\mathcal X$ 是层的参数图表（本节约定）。则 $\mathcal B\subseteq\mathcal X$ 是 Zariski 闭集。

*证明.* 第一步，齐次化。把 $\lambda$ 视为 $\mathbb P^1$ 上的齐次坐标 $[u:v]$，$\lambda=u/v$，并令
$$P^{\mathrm{hom}}(X,u,v)=u\,H(X)-v\,H_A(X).$$
$m_I(X,\lambda)$ 关于 $\lambda$ 的次数 $\le\omega$，故其齐次化 $m_I^{\mathrm{hom}}(X,u,v)$ 关于 $(u,v)$ 是 $\omega$ 次齐次多项式；且 $m_I^{\mathrm{hom}}(X,u,0)$ 恰为 $H(X)$ 的相应 $\omega$ 阶子式。

第二步，入射集。令
$$\mathcal I=\Bigl\{(X,[u:v])\in\mathcal X\times\mathbb P^1:\ m_I^{\mathrm{hom}}(X,u,v)=0\ \text{对一切}\ I\Bigr\}.$$
$\mathcal I$ 由多项式方程定义，故在 $\mathcal X\times\mathbb P^1$ 中闭。

第三步，无无穷远公共根。由本节约定，每点 $\operatorname{rank}H(X)=\omega$，故至少有一个 $\omega$ 阶子式 $m_{I_0}(X)$ 非零，于是
$$m_{I_0}^{\mathrm{hom}}(X,1,0)=m_{I_0}(X)\neq0 .$$
因此 $[u:v]=[1:0]$ 不属于任何纤维 $\mathcal I_X$：公共根不可能落在无穷远处。于是限制到仿射部分 $v=1$ 不丢失任何点，
$$\mathcal B=\pi_{\mathcal X}(\mathcal I),\qquad \pi_{\mathcal X}:\mathcal X\times\mathbb P^1\to\mathcal X .$$

第四步，投影闭。$\mathbb P^1$ 是紧的（在 $\mathbb C$ 上紧、在代数意义下 proper），故 $\pi_{\mathcal X}$ 是闭映射；闭集的像是闭集，于是 $\mathcal B=\pi_{\mathcal X}(\mathcal I)$ 闭。$\square$

**注 4.1.** 第三步是本节的关键。若没有"$\operatorname{rank}H\equiv\omega$"，公共根可以逃到无穷远，$\mathcal B$ 就可能只是可构造集而非闭集；那时"块上的坏集闭"不成立，一般点判据也随之失效。同一秩不变量在 4.5 节（引理 4.6）中还会再用一次，作用不同：那里它阻止公因子在特化时退化为常数。

**注 4.2.** 定理 4.1 只用到 $H$ 的秩在图表上恒定，与层的其余结构无关；但它在层的图表上**处处**成立，因此可用于 4.2 与 4.3 两小节的推理。

## 4.2 不可约块上的函数域判据

**定理 4.2（一般点判据）.** 设 $\mathcal S\subseteq\mathcal X$ 是不可约参数块（其上 $\operatorname{rank}H\equiv\omega$），$K=\overline{\mathbb Q(\mathcal S)}$ 为函数域。则
$$\mathcal S\ \text{含好点}\iff \deg_\lambda\gcd_I m_I=0\quad\text{在}\ K[\lambda]\ \text{中}.$$
换言之：块含好点当且仅当该块的一般点是好的。

*证明.* ($\Leftarrow$) 设 $\gcd_I m_I=1$ 在 $K[\lambda]$ 中。由 Bézout，存在 $a_I\in K[\lambda]$ 使 $\sum_I a_I m_I=1$。$a_I$ 只有有限个极点，故存在非空 Zariski 开集 $U\subseteq\mathcal S$，使所有 $a_I$ 在 $U$ 上有定义；对 $X\in U$ 特化得 $\sum_I a_I(X,\lambda)m_I(X,\lambda)=1$，故 $X$ 好。于是 $U$ 非空、$\mathcal S$ 含好点。

($\Rightarrow$) 设 $X_0\in\mathcal S$ 好。由定理 4.1，$\mathcal B\cap\mathcal S$ 在 $\mathcal S$ 中闭；$X_0\notin\mathcal B$，故 $\mathcal B\cap\mathcal S$ 是**真**闭子集。$\mathcal S$ 不可约，故其一般点不在任何真闭子集中，即一般点好；而一般点好等价于 $\gcd_I m_I=1$（在函数域上无公共因子）。$\square$

**注 4.3.** 判据只要求 $\operatorname{rank}H\equiv\omega$ 与 $\mathcal S$ 不可约，**不要求** $\mathcal S$ 是 $\mathcal X$ 的不可约分量。这一点在 4.3 中很关键：我们不必做分量分解。

**注 4.4（为什么在代数闭包上判）.** 定理 4.2 中的函数域取 $\overline{\mathbb Q(\mathcal S)}$，因为 $m_I$ 的公共根可以是非有理的（甚至是非实的）代数数。若只在有理参数点上判，会漏掉"公根存在但不在 $\mathbb Q$ 上"的情形。相应地，坏性的定义 $\exists\lambda\in\mathbb C$ 本身就是复的：$(5b)$ 要求对一切 $\lambda\in\mathbb C$ 秩不变。判据与定义因此一致。

## 4.3 有限覆盖原理

**命题 4.3（有限覆盖足够）.** 设
$$\mathcal X=\bigcup_{j=1}^{M}\mathcal S_j$$
是层的一个有限覆盖，每块 $\mathcal S_j$ 不可约、且其上 $\operatorname{rank}H\equiv\omega$。则
$$\mathcal X\ \text{含好点}\iff\exists\,j\ \text{使}\ \deg_\lambda\gcd_I m_I^{(j)}=0\ \text{在}\ \overline{\mathbb Q(\mathcal S_j)}[\lambda]\ \text{中},$$
其中 $m_I^{(j)}$ 是限制在 $\mathcal S_j$ 上的极大子式。

*证明.* ($\Leftarrow$) 由定理 4.2，第 $j$ 块含好点，故 $\mathcal X$ 含好点。

($\Rightarrow$) 设 $X_0\in\mathcal X$ 好，$X_0\in\mathcal S_j$。由定理 4.1，$\mathcal B$ 在 $\mathcal X$ 中闭，故 $\mathcal B\cap\mathcal S_j$ 在 $\mathcal S_j$ 中闭且不含 $X_0$，是真闭子集。$\mathcal S_j$ 不可约 ⟹ 一般点不在 $\mathcal B$ 中 ⟹ 由定理 4.2，$\deg_\lambda\gcd=0$。$\square$

**注 4.5（覆盖从哪来）.** 第 3 节的参数化直接给出一个这样的有限覆盖：对每个实特征值 $\mu$、每个可容许方向的仿射图卡、以及纤维 $\operatorname{Gr}(m,R)$ 的每个标准仿射图卡取一块。若层为空（无实特征值可容许方向），覆盖为空集，判定为不可行。下面 4.4 给出纤维图卡的具体写法。

**注 4.6（为什么不需要分量分解）.** 早先的写法要求把参数空间分解成不可约分量，再逐分量判；这既难做（分量通常不可显式求出）也不必要。命题 4.3 说明：只要覆盖里的块**不可约**且坏集在其上闭，判据就成立。纤维的 Grassmann 图卡是仿射空间，天然不可约，故覆盖容易构造。

## 4.4 Graßmann 图卡与极大子式

**构造 4.4（纤维的仿射图卡）.** 固定一个可容许方向 $[v]\in\mathbb P(E_\mu^0)$，并取 $\mathcal Q_v/\overline V_{0,v}$ 的一组基 $e_1,\dots,e_R$（$R=r(v)-\delta$）。取 $I\subseteq\{1,\dots,R\}$，$|I|=m$，令 $J=\{1,\dots,R\}\setminus I$，$|J|=R-m$。对应的图卡是
$$\mathcal X_I=\Bigl\{X=(X_{ij})_{i\in I,\,j\in J}\in\mathbb C^{m\times(R-m)}\Bigr\},$$
由下式给出纤维中的点（即行空间）：
$$\mathrm{row}_i=e_i+\sum_{j\in J}X_{ij}\,e_j,\qquad i\in I .$$
基行（$V_0+D_v$ 的一组基，共 $(k-1)+\delta$ 个）加上这 $m$ 个图卡行，共
$$(k-1)+\delta+m=(k-1)+s=q$$
个行，构成 $L(X)$。图卡数是 $\binom{R}{m}$，参数个数是
$$d=m(R-m)=(s-\delta)\bigl(r(v)-s\bigr)\le p^2 .$$
$X$ 取遍 $\mathbb C^{d}$ 时，$\mathrm{row}$ 取遍该图卡内的全部 $m$ 维子空间；$m=0$ 时纤维是一个点。

**引理 4.5（子式计数与次数）.** 在构造 4.4 的每张图表上，$L(X)$ 的元素关于 $X$ 是仿射的，故 $H(X),H_A(X)$ 的元素关于 $X$ 仿射；每个极大子式 $m_I(X,\lambda)$ 满足
$$\deg_X m_I\le\omega,\qquad \deg_\lambda m_I\le\omega .$$
极大子式的个数为
$$\binom{q}{\omega}\binom{k}{\omega}=\binom{q}{k-1}\,k=k\binom{q}{s},$$
其中用到 $\binom{k}{k-1}=k$ 与 $\binom{q}{k-1}=\binom{q}{q-k+1}=\binom{q}{s}$。

*证明.* $H(X)=L(X)N$ 关于 $X$ 仿射（$N$ 为常矩阵）；$m_I$ 是 $\omega$ 阶行列式，按列多重线性，关于 $X$ 的次数 $\le\omega$；关于 $\lambda$ 的次数 $\le\omega$。计数是"选 $\omega$ 行、选 $\omega$ 列"的组合数。$\square$

**注 4.7（方向参数必须计入）.** 构造 4.4 是在**固定**方向 $[v]$ 上做的。当 $\dim E_\mu^0>1$（重特征值）时，方向本身也是参数，层在 $\mathbb P(E_\mu^0)$ 上是一个相对 Grassmann 丛（第 3 节的参数化定理）；此时图卡覆盖必须同时覆盖底 $\mathbb P(E_\mu^0)$（取仿射图卡）并在其上取商丛的局部平凡化，参数里既有方向坐标又有纤维坐标。只有这样才能对"整条纤维/整个方向空间"下结论。第 6 节的反例会显示：只取一个方向代表元会给出错误答案。

## 4.5 满秩首项系数引理

在每张图表上，$m_I(X,\lambda)$ 的 $\lambda^\omega$ 系数恰是 $H(X)$ 的相应 $\omega$ 阶子式。由于图表上 $\operatorname{rank}H(X)=\omega$（本节约定），至少一个这样的子式非零，于是

$$\text{对每个 }X\in\mathcal X_I,\ \text{至少有一个指标 }I\ \text{使}\ \deg_\lambda m_I(X,\cdot)=\omega. \tag{4.1}$$

这一条看起来只是记账，它其实是"一般点判据"能推广到**整张图表**的全部理由。

**引理 4.6（满秩首项系数）.** 设 $K$ 是域，$X=(X_1,\dots,X_d)$，$m_1,\dots,m_t\in K[X,\lambda]$ 关于 $\lambda$ 的次数 $\le\omega$，且满足 (4.1)（即对每个 $X_0$，至少一个 $m_i(X_0,\cdot)$ 的次数恰为 $\omega$）。若
$$\deg_\lambda\gcd(m_1,\dots,m_t)>0\quad\text{在}\ K(X)[\lambda]\ \text{中},$$
则对**每个** $X_0$，特化后的 $m_i(X_0,\cdot)$ 都有非平凡公因子。

*证明.* 设 $g=\gcd$ 在 $K(X)[\lambda]$ 中，$\deg_\lambda g>0$。按 Gauss 引理，去掉内容后可取 $g\in K[X][\lambda]$ 本原、正次数，且 $g\mid m_i$（在 $K[X][\lambda]$ 中）对每个 $i$ 成立；写 $m_i=g\,h_i$。

固定 $X_0$。若 $g(X_0,\cdot)\equiv0$，则所有 $m_i(X_0,\cdot)=g(X_0,\cdot)h_i(X_0,\cdot)\equiv0$，与 (4.1) 矛盾。若 $g(X_0,\cdot)$ 是非零常数，则由 $\deg_\lambda m_i\le\deg_\lambda g+\deg_\lambda h_i$ 及 $g$ 在该点次数为 $0$ 得 $\deg_\lambda m_i(X_0,\cdot)\le\deg_\lambda h_i\le\omega-\deg_\lambda g<\omega$ 对一切 $i$ 成立，也与 (4.1) 矛盾。故 $g(X_0,\cdot)$ 非零且非常数，它是所有 $m_i(X_0,\cdot)$ 的非平凡公因子。$\square$

**推论 4.7（逐图表二值）.** 在层的一张图表 $\mathcal X_I$ 上，以下二者恰有一个成立：

1. $\deg_\lambda\gcd_I m_I=0$：该图表含好点（事实上好点在非空 Zariski 开集中）；
2. $\deg_\lambda\gcd_I m_I>0$：该图表的**每个**点都坏。

*证明.* 若 $\deg=0$ 用定理 4.2；若 $\deg>0$ 用引理 4.6（条件 (4.1) 由本节约定保证）。$\square$

**注 4.8（为什么一般族上不成立）.** 没有 (4.1) 时，"一般点有正次数公因子 ⟹ 每点都坏"是**假**命题。取单参数的单多项式族 $m(X,\lambda)=X\lambda+1$：在 $K(X)[\lambda]$ 上 $\gcd=m$，次数 $1>0$；但在 $X_0=0$ 处特化为常数 $1$，该点没有非平凡因子。这里 (4.1) 在 $X_0=0$ 处失效（该点的 $\lambda$-次数为 $0$，而它要求恰为 $1$），结论也随之失效——正说明引理 4.6 的结论不是 gcd 的一般性质，而完全依赖 $\operatorname{rank}H\equiv\omega$ 这一超平面层的不变量。

**注 4.9（与定理 4.1 的统一）.** 同一个秩不变量在两处起作用：定理 4.1 用它排除无穷远公共根（得到闭性），引理 4.6 用它排除公因子退化为常数（得到整图表坏的证书）。因此"精确判定"是层几何的推论，而不是一套外来的符号计算技巧。

## 4.6 实点稠密性

定理 4.2 与引理 4.6 都是关于"一般点"的断言，而一般点是代数点。要把它们翻译成"存在**实**的可容许设计"，需要一步稠密性。

**命题 4.8（实点稠密）.** 构造 4.4 的每张图卡 $\mathcal X_I\cong\mathbb C^{d}$ 带标准实结构 $\mathbb R^{d}$；$\mathbb P(E_\mu^0)$ 的仿射图卡同样带实结构（$\mu$ 为实特征值，$E_\mu^0$ 由实线性方程组定义）。于是：

1. 每个图卡的实点是 Zariski 稠密的；
2. 若某图卡上的好集是非空 Zariski 开集，则它含实点，即含实的可容许设计；
3. 若某图卡上 $\deg_\lambda\gcd>0$，则该图卡的全部**实**点都坏。

*证明.* (1) 非零多项式的零点集在 $\mathbb R^d$ 中无内点，故其补集稠密。(2) 好集是非空 Zariski 开集，即某个非零多项式的非零集，由 (1) 含实点；该实点对应的 $L(X)$ 为实矩阵、行空间为实子空间，故给出实设计。(3) 引理 4.6 的结论对每个点成立，对实点自然成立。$\square$

**注 4.10.** 命题 4.8 是不可省的：一般点好只给出"某个代数点好"，而设计必须是实的。由 (1)–(2)，"非空开好集 ⟹ 实可行"在每个图卡上自动成立，因此命题 4.3 的判据对**实**可行问题同样有效。

## 4.7 证书体系

判定程序的输出应当是可独立复核的对象。本节把证书分成四类，按逻辑强度排列。

### 4.7.1 方向筛（免费的否定证书）

**命题 4.9（方向筛）.** 若对 $M=\pi_{K_0}A|_{K_0}$ 的每个实特征值 $\mu$ 都有
$$E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)=\{0\},$$
则层不可行。

*证明.* 由方向定理（第 3 节），任何可容许方向必属于某个 $E_\mu^0$；若无这样的方向，则无法构造任何行空间。$\square$

**注 4.11.** 这一判据只用实线性代数（在 $\mathbb Q(\mu)$ 上做零空间），不涉及任何子式或 gcd，因此是最便宜的否定证书。它同时说明预设行确实可能"削掉整个特征空间"：$L_0$ 的两个线性条件可以直接把某个 $E_\mu$ 割成零。

### 4.7.2 纤维维数不等式

**命题 4.10（纤维非空必要条件）.** 若某方向 $[v]\in\mathbb P(E_\mu^0)$ 的纤维非空，则
$$\delta\le s\le r(v).$$
若特征方向与非特征方向两个分支上都违反（特征分支：$\delta>s$ 或 $s>\rho$；非特征分支：$\delta>s$ 或 $s>\rho-1$），则层不可行。

*证明.* 由第 3 节的纤维引理，纤维是 $\operatorname{Gr}(m,R)$，$m=s-\delta$，$R=r(v)-\delta$，非空当且仅当 $0\le m\le R$，即 $\delta\le s\le r(v)$。$\square$

**注 4.12.** 这是"结构性"否定证书，仍不需要任何铅笔计算。它与命题 4.9 一起构成判定程序的前两级筛。

### 4.7.3 结式：单向证书

**命题 4.11（结式充分）.** 若存在一对指标 $I,J$ 使
$$\operatorname{Res}_\lambda\bigl(m_I,m_J\bigr)\not\equiv0\quad\text{在}\ K[X],$$
则 $\deg_\lambda\gcd_I m_I=0$，故该图表（从而层）可行。

*证明.* 结式非零意味着 $m_I,m_J$ 在 $K(X)[\lambda]$ 中互素（在代数闭包上无公共根），故全体的 gcd 为 $1$。$\square$

**注 4.13（结式不必要）.** 反过来不成立：可以出现"每对子式都有非平凡公因子，而全体 gcd 为 $1$"的情形。最小的例子是三个多项式
$$f_1=\lambda(\lambda-1),\qquad f_2=\lambda(\lambda-2),\qquad f_3=(\lambda-1)(\lambda-2).$$
两两都有非平凡公因子（分别为 $\lambda$、$\lambda-1$、$\lambda-2$），但 $\gcd(f_1,f_2,f_3)=1$。因此：

* 结式非零是可用的**正向**证书；
* 找不到这样的对**不是**否定证书；
* 精确判定必须算**全体**子式的 gcd，或用等价的"同时公共根"检验。

### 4.7.4 精确代数证书

**命题 4.12（证书的形态）.** 层的一个完整判定证书由下列数据组成：

1. 压缩 $M$ 的特征多项式分解，以及每个不可约因子上 $E_\mu^0$ 的基（或"$E_\mu^0=0$"的说明）；
2. 每个可容许方向、每张图卡（构造 4.4，含图卡数与参数个数）；
3. 对每张图卡，二者之一：
   - **好**：Bézout 恒等式 $\sum_I a_I(X,\lambda)\,m_I(X,\lambda)=1$，$a_I\in K[X][\lambda]$（只需给出 $a_I$，验证是一次多项式乘法）；
   - **坏**：一个非常数的 $g\in K[X][\lambda]$ 与整除恒等式 $g\,h_I=m_I$（对每个 $I$）。

若第 3 步对某张给出"好"，则层可行；若**所有**图卡都给出"坏"，则由推论 4.7 与命题 4.3，层不可行。

*证明.* 好的一支：Bézout 恒等式直接验证 gcd 为 $1$（不需再算 gcd）。坏的一支：由引理 4.6，$g$ 非常数且整除每个子式，故该图卡每点都坏；覆盖有限，逐块都坏 ⟹ 层不可行。$\square$

**注 4.14（证书与实现的区别）.** 命题 4.12 描述的是"可复核的对象"；实现可以选择更快的算法（例如直接做函数域上的 Euclid），只在最后输出上述数据之一。已经做过的精确计算（第 6 节的反例、若干 $n=8$、$p=2$ 实例）都以这一形态记录：好方向给出有理图卡点上的 Bézout 证书，坏方向给出公因子并逐条验证整除。

## 4.8 判定算法

**算法 4.1（整层的精确判定）.**

1. **前置检查.** 若 $\operatorname{rank}L_0<r_0$，输出"不可行"并停止（问题定义要求 $\mathcal L$ 行满秩，故 $r_0=\operatorname{rank}L_0$ 是可行性必要条件）。
2. 计算 $K_0$、$N$、$M=\pi_{K_0}A|_{K_0}$；分解 $\chi_M$，取其**实**不可约因子。
3. 对每个实不可约因子 $f$ 与每个可容许方向 $[v]\in\mathbb P(E_\mu^0)$（$\mu$ 为 $f$ 的根）：计算 $\delta,s,m,R$；若 $\delta>s$ 或 $s>r(v)$，跳过（命题 4.10）。
4. 对每个方向、每张图卡 $\mathcal X_I$（共 $\binom{R}{m}$ 张）：在域 $K=\mathbb Q(\mu)$ 上按构造 4.4 建立 $L(X)$，计算全部 $k\binom{q}{s}$ 个极大子式，并在 $K(X)[\lambda]$ 上求其 gcd。
5. 若某张图卡的 $\deg_\lambda\gcd=0$，输出"可行"并停止。
6. 若所有图卡的 $\deg_\lambda\gcd>0$，输出"不可行"。
7. 若计算无法完成（例如超出实现范围），输出"未判定"——**不得**输出"不可行"。

**命题 4.13（正确性）.** 在步骤 1–6 全部完成时，算法 4.1 的判定正确。

*证明.* 第 1 步由问题定义。第 3 步由命题 4.10。第 5 步：由定理 4.2，$\deg=0$ 的图卡含好点，故可行。第 6 步：由推论 4.7，每张图卡全坏；有限覆盖（注 4.5）⟹ 层无好点 ⟹ 不可行。第 7 步的"未判定"不是判定，故不涉及正确性。$\square$

**注 4.15（共轭根）.** 第 3 步按**不可约因子**枚举而不是按根枚举：$f$ 的各个根对应的特征空间互为 Galois 共轭，而共轭不改变 $\gcd$ 的 $\lambda$-次数，故一个因子只需算一次，结论对该因子的所有根一致。这在实现中是显式使用的（例 4.1 中实例一与实例三的 $\chi_M$ 都含一个三次不可约因子）。

**注 4.16（数的域的一致性）.** 第 4 步的所有线性代数（$E_\mu^0$、$D_v$、$U_v^\perp$、$\mathcal Q_v/\overline V_{0,v}$ 的基与图卡行）都必须在**同一个**域 $K=\mathbb Q(\mu)$ 上完成；若 $\mu\notin\mathbb Q$，这些基不是有理坐标。只有系数域一致，"图卡行 + 子式 + 函数域 gcd"这条链才正确。

**例 4.1（已记录的实例）.** 取 $n=8$、$p=2$、$C=[e_1;e_2]$、$L_0$ 为空，此时 $k=4$、$\rho=4$、$\omega=3$、$q=4$，即 $s=1$；在非特征方向上 $r(v)=\rho-1=3$，纤维为 $\operatorname{Gr}(1,3)=\mathbb P^2$。对三个实例按算法 4.1 计算，得到的证书形态如下：

| 实例 | $\chi_M$ 的因子 | 因子上的结论 | 层 |
|---|---|---|---|
| 一 | $x-1$；三次不可约因子 | 两者皆 $\deg_\lambda\gcd=0$ | 可行 |
| 二 | $x-1$；$x$；$x^2-8$ | 前两者 $\deg_\lambda\gcd=1$，第三者 $\deg_\lambda\gcd=0$ | 可行（由 $x^2-8$ 给出） |
| 三 | $x-1$；三次不可约因子 | 两者皆 $\deg_\lambda\gcd=3$ | 不可行 |

第二、三行说明两件事：单个因子上"全坏"不能推出层不可行（实例二的前两个因子都坏，而第三个因子给出可行点）；要判不可行，必须按命题 4.13 把**全部**实因子、全部分支都算完（实例三正是如此）。这些结论只有精确验证的地位，不是证明；它们的作用是示例证书的形态与判据的用法。

## 4.9 本节不声称什么

为了不把三个不同强度的命题混为一谈，明确划界：

1. **本节给出的是整层的精确判定**（算法 4.1，命题 4.13）。它对所有输入正确，但**没有**任何复杂度断言：枚举全部实特征值、全部方向、全部图卡、全部极大子式，代价可以是指数的。
2. **"几何单谱子类上多项式时间"是第 5 节的命题**，它额外假设每个实特征值的特征空间是一维（几何单重），从而方向的参数空间退化为有限个点；该假设必须写在定理陈述里，且"不在该子类"的输入只能得到"未判定"。
3. **第 6 节的反例是否定一个特定约化**（"每个特征值取一个方向代表元"），它**不**证明重复特征值情形困难，也不证明几何单谱是多项式可解的必要条件。重复特征值情形的一般复杂度在本节的框架内是开放的。

这三条对应论文摘要与引言中的三处不同措辞，不应互相替代。

**状态汇总.**

| 结果 | 内容 | 状态 |
|---|---|---|
| 定理 4.1 | 坏集闭 | 已证（专家复核两轮） |
| 定理 4.2 | 不可约块上的函数域判据 | 已证 |
| 命题 4.3 | 有限覆盖足够 | 已证 |
| 构造 4.4 | 纤维的 Grassmann 图卡 | 构造性定义；实现精确验证 |
| 引理 4.5 | 子式计数 $k\binom{q}{s}$ 与次数 $\le\omega$ | 已证 |
| 引理 4.6 | 满秩首项系数 → 整图表坏 | 已证（专家给出证明） |
| 推论 4.7 | 逐图表二值 | 已证 |
| 命题 4.8 | 实点稠密 | 已证（初等） |
| 命题 4.9 | 方向筛 | 已证；实现精确验证 |
| 命题 4.10 | 纤维维数不等式 | 已证 |
| 命题 4.11 | 结式充分、不必要 | 已证（必要性有反例） |
| 命题 4.12 | 精确证书的形态 | 已证；在记录实例上精确验证 |
| 命题 4.13 | 算法正确性 | 已证（条件：步骤 1–6 完成） |
| 注 4.15–4.16 | 共轭根、域一致性 | 实现层面的事实 |

表中"已证"指有完整纸面证明并经专家复核；"精确验证"指在具体实例上用精确算术复核，不构成证明。

# 5 固定 $p$ 的位复杂度

本节把第 3、4 节的几何与判定程序整理成一条**位复杂度**定理：固定输出维数 $p$ 时，在**实谱几何单谱**的输入上，超平面层的判定是输入比特长的多项式时间。这是本文唯一涉及复杂度的结果，也是唯一带 promise 的结果——第 5.8 节会把它的边界逐条说明。

贯穿全节，$\tau$ 记输入 $(A,C,L_0)$ 与 $q$ 的二进制编码长度（即所有整数分子的最大比特长，分母亦同阶）。所有算术都是精确的，不使用浮点。

---

## 5.1 几何单谱

先固定本节唯一的结构假设。

**定义 5.1（实谱几何单谱）.** 设 $M=\pi_{K_0}A|_{K_0}$ 是压缩。称 $M$ 的**实谱几何单谱**，若对每个实特征值 $\mu$，
$$\dim\ker(M-\mu I)=1 .$$

也就是说：每个实特征值只贡献**一条**射影方向。

这个条件弱于"代数单重"。一个特征值可以有代数重数 $>1$ 而特征空间仍是一维（即非半单、有 Jordan 块），此时它依然只给出一条方向，第 3 节的底 $\mathbb P(E_\mu)$ 仍是一个点。因此定义 5.1 覆盖的类严格大于"实特征值都是单根"的类。

反过来，一旦某个实特征值 $\mu$ 的 $\dim E_\mu=d_\mu\ge2$，底 $\mathbb P(E_\mu)$ 就是维数 $d_\mu-1$ 的射影空间，参数个数随 $n$ 增长——这正是第 5.8 节说明的失效点。

还需要把预设行并进来。第 3 节已经证明：带预设行时实际可枚举的方向不是整个 $E_\mu$，而是
$$E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN).$$
因此在几何单谱下，每个实特征值 $\mu$ 对应**至多一个**待检方向（$E_\mu^0$ 是 $E_\mu$ 的子空间，维数 $\le1$）；若 $E_\mu^0=0$，该特征值直接被排除，不产生任何工作。这一点对复杂度是必要的：算法枚举的是 $E_\mu^0$ 中的方向，而不是 $M$ 的全部特征向量。

> **状态.** 定义与上述两条观察**[已证-纸面]**（第 3 节的引理 3.6 与定理 3.15 的直接推论）。

---

## 5.2 压缩的高度

本节所有后续估计都建立在这一条上：压缩矩阵 $M$ 与基 $N$ 都不"大"。

**引理 5.1（压缩高度）.** 设输入元素的比特长至多 $\tau$。则存在 $\mathrm{poly}(n,\tau)$ 位时间的算法，输出 $K_0$ 的一个本原整数基 $N$ 与压缩 $M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$，且 $N$、$M$ 的元素比特长都是 $\mathrm{poly}(n,\tau)$。

*证明.* 分四步。

(i) **清分母。** 把 $[C;CA]$ 的每个元素写成既约分数，乘以所有分母的最小公倍数，得到整数矩阵 $\widehat W$，其元素比特长 $\le 2\tau+\lceil\log n\rceil$。

(ii) **无分数消元。** 对 $\widehat W$ 作 Bareiss（无分数）消元求核。Bareiss 的中间量是 $\widehat W$ 的子式，因此由 Hadamard 界，任何 $k\times k$ 子式满足
$$\bigl|\det\bigr|\le \bigl(\sqrt{k}\,\|\widehat W\|_\infty\bigr)^{k},$$
即 $\log|\det|\le \frac{k}{2}\log k+k\bigl(2\tau+\log n\bigr)$。于是核基的每个坐标都是一个子式（至多差一个公共分母），比特长 $\mathrm{poly}(n,\tau)$。

(iii) **本原化。** 把核基的每列清分母，再除以列元素的最大公约数，得到本原整数列，比特长不变（除以公因子只会减小）。

(iv) **压缩。** $N^{\mathsf T}N$ 与 $N^{\mathsf T}AN$ 的元素是 $N$ 的二次型，比特长 $\le 2\cdot\mathrm{poly}(n,\tau)+\log n$。$M$ 的元素是 $\det(N^{\mathsf T}N)$ 的余子式与 $N^{\mathsf T}AN$ 的乘积之比；用无分数消元求 $(N^{\mathsf T}N)^{-1}$，中间量仍是子式，故 $M$ 的元素比特长 $\mathrm{poly}(n,\tau)$。四步的算术次数都是 $n$ 的多项式，每步的每个运算作用在 $\mathrm{poly}(n,\tau)$ 位的数上，故总位时间是 $\mathrm{poly}(n,\tau)$。$\square$

> **状态.** **[已证-纸面]**；只用到 Hadamard 界与 Bareiss 消元的标准界。

---

## 5.3 特征多项式与特征值的高度

**引理 5.2（特征多项式高度）.** 记 $\chi_M(t)=\det(tI-M)$，把它的系数清分母并取本原部分后，各系数是比特长 $\mathrm{poly}(n,\tau)$ 的整数；$\chi_M$ 可在 $\mathrm{poly}(n,\tau)$ 位时间内算出。

*证明.* $\chi_M$ 的 $t^{k-i}$ 系数是 $M$ 的 $i$ 阶主子式之和。由引理 5.1，$M$ 的元素比特长为 $\mathrm{poly}$；每个 $i$ 阶子式由 Hadamard 界控制在 $(k^{1/2}2^{\mathrm{poly}})^{k}$ 以内；求和至多 $\binom{k}{i}$ 项，只增加 $\log\binom{k}{i}\le k$ 位。清分母只引入 $M$ 各元素分母的乘积，其次数的对数同样是 $\mathrm{poly}$。计算可按 Faddeev–LeVerrier 或插值法进行，算术次数 $\mathrm{poly}(n)$。$\square$

**引理 5.3（根的高度与次数）.** 设 $\mu$ 是 $\chi_M$ 的任一复根。则
$$[\mathbb Q(\mu):\mathbb Q]\le k\le n,\qquad h(\mu)\le \mathrm{poly}(n,\tau),$$
其中 $h$ 是对数绝对高度。此外，$\chi_M$ 的实根可用精确实根隔离算法在 $\mathrm{poly}(n,\tau)$ 位时间内分离并给出任意精度的有理区间。

*证明.* 次数不超过 $\deg\chi_M=k$。高度：$\mu$ 是引理 5.2 给出的整系数多项式的根，系数比特长为 $\beta=\mathrm{poly}(n,\tau)$；标准的根高度界给出
$$h(\mu)\le \beta+\tfrac12\log(k+1)+\log 2,$$
（等价地，$\mu$ 的极小多项式的 Mahler 测度受系数界控制），故 $h(\mu)=\mathrm{poly}(n,\tau)$。实根隔离：Vincent–Collins–Akritas（连分数）或 Descartes 方法对整系数多项式是位多项式时间的，见标准结论；输出是互不相交的有理区间，每个含恰好一个实根。$\square$

> **状态.** **[已证-纸面]**，其中"根高度界"与"实根隔离的位复杂度"两条是**引用的标准事实**（见 5.9 节 (S1)(S2)）。

---

## 5.4 特征向量与商丛的基

**引理 5.4（特征向量与纤维基的高度）.** 在定义 5.1 下，对每个实特征值 $\mu$：

1. $E_\mu$ 有一个本原向量 $a$，其坐标在 $K=\mathbb Q(\mu)$ 上、比特长 $\mathrm{poly}(n,\tau)$；
2. $E_\mu^0$、$U_v^\perp$、$D_v=K_0\cap U_v^\perp$、以及商 $\mathcal Q_v/\overline V_{0,v}$ 的基都能在同一数域 $K$ 上算出，比特长同为 $\mathrm{poly}(n,\tau)$；
3. 上述计算的总位时间是 $\mathrm{poly}(n,\tau)\cdot\mathrm{poly}(\deg)$，其中 $\deg=[K:\mathbb Q]\le n$。

*证明.* (1) $a$ 是 $(M-\mu I)$ 的核。在 $K$ 上作无分数消元，核向量取为 $k-1$ 阶子式构成的向量（Cramer 法则），每个坐标是子式之比；由引理 5.1 与 5.3，分子分母的比特长都是 $\mathrm{poly}(n,\tau)$，取本原化后得到本原向量。

(2) $E_\mu^0$ 是 $E_\mu$ 与两个线性条件的交，即 $K$ 上一个矩阵的核；$U_v^\perp$ 是 $\{x:\langle x,v\rangle=\langle x,Av\rangle=0\}$ 的核；$D_v$ 是 $K_0$ 上两条线性泛函的公共核；$\mathcal Q_v/\overline V_{0,v}$ 是商空间的一组补基。四者都是 $K$ 上维数 $\le n$ 的矩阵的核、像、和或商，用同一套无分数消元，中间量是子式，故比特长 $\mathrm{poly}(n,\tau)$。

(3) $K$ 上每次算术是 $\mathrm{poly}(\deg,\text{高度})$ 位，消元的算术次数是 $n$ 的多项式。$\square$

**一处必须强调的要点.** 这些基**必须**在 $K$ 上计算，不能退回 $\mathbb Q$。当 $\mu\notin\mathbb Q$ 时，$E_\mu$ 是 $K$ 上的直线而不是 $\mathbb Q$ 上的直线；在 $\mathbb Q$ 上算会把它错误地拆成共轭分量的直和。第 4 节的判定程序因此把"方向枚举"与"纤维构造"都放在同一个 $K$ 里完成。

> **状态.** **[已证-纸面]**。

---

## 5.5 图卡的规模

固定一个实特征值 $\mu$、一条方向 $[v]\in\mathbb P(E_\mu^0)$ 与纤维的一个仿射图卡。第 3 节给出：纤维是 Grassmann 流形
$$\operatorname{Gr}\bigl(s-\delta,\ \mathcal Q_v/\overline V_{0,v}\bigr),\qquad s=q-k+1,\quad \delta=\dim V_0-\dim(V_0\cap K_0),$$
其中 $V_0=\operatorname{row}L_0$。记商丛的秩为
$$\widetilde r:=r(v)-\delta=r(v)-\bigl(\dim V_0-\dim(V_0\cap K_0)\bigr),$$
则图卡参数是一个 $d_{\mathrm{chart}}\times(\widetilde r-d_{\mathrm{chart}})$ 的符号矩阵 $X$（这里 $\widetilde r$ 与第 1 节中自由行块 $R$ 无关，后者不再出现）。

**引理 5.5（图卡规模）.** 在上述记号下：

1. **参数个数** $d_{\mathrm{chart}}=(s-\delta)\bigl(r(v)-s\bigr)\le p^{2}$；
2. **次数** 每个图卡行对 $X$ 是仿射的，每个极大子式对 $X$ 的次数 $\le\omega$、对 $\lambda$ 的次数 $\le\omega$；
3. **子式个数** $\binom{q}{\omega}\binom{k}{\omega}=k\binom{q}{s}=n^{O(p)}$（$p$ 固定）；
4. **图卡数** 每个纤维的图卡覆盖只需 $\binom{\widetilde r}{s-\delta}=\binom{r(v)-\delta}{s-\delta}=O(1)^{p}$ 个图卡；
5. **块数** 特征值至多 $k\le n$ 个，每个至多一条方向。

*证明.* (1) $r(v)\in\{\rho,\rho-1\}$ 且 $\rho\le2p$。函数 $m\mapsto m(\widetilde r-m)$ 在 $m=\widetilde r/2$ 处取最大，故
$$d_{\mathrm{chart}}=(s-\delta)\bigl(\widetilde r-(s-\delta)\bigr)\le \frac{\widetilde r^{2}}{4}\le\frac{(2p)^{2}}{4}=p^{2}.$$

(2) 图卡行是 $\mathrm{comp}_i+\sum_j X_{ij}\mathrm{comp}_{m+j}$，对 $X$ 仿射；铅笔 $\lambda H-H_A$ 对 $\lambda$ 线性；$\omega\times\omega$ 行列式对 $X$ 与 $\lambda$ 的次数都不超过 $\omega$。

(3) 极大子式是"$\omega$ 行 $\times$ $\omega$ 列"，行有 $\binom{q}{\omega}$ 种、列有 $\binom{k}{\omega}=\binom{k}{k-1}=k$ 种。由非空条件 $s\le r(v)\le\rho\le2p$，故
$$\binom{q}{s}\le\sum_{j\le 2p}\binom{n}{j}=n^{O(p)},$$
乘以 $k\le n$ 仍是 $n^{O(p)}$。

(4) $\operatorname{Gr}(m,\widetilde r)$ 的标准图卡数为 $\binom{\widetilde r}{m}=\binom{r(v)-\delta}{s-\delta}\le\binom{\rho}{\lfloor\rho/2\rfloor}\le 2^{\rho}\le 2^{2p}$。

(5) 特征多项式次数为 $k$。$\square$

> **状态.** **[已证-纸面]**。注意 (1) 与第 4 节"满秩首项系数引理"无关；它只用到纤维维数。

---

## 5.6 无分数子结式：为什么不能直接用欧几里得

判定"该图卡生成好"等价于：极大子式 $m_1,\dots,m_\ell$（$\ell=n^{O(p)}$ 个）作为 $K[X][\lambda]$ 的元素，在 $K(X)[\lambda]$ 上的 gcd 次数为零。直接把这个 gcd 实现成"$K(X)[\lambda]$ 上的欧几里得算法"是**不可行**的：

- 每一步除法都把分母乘进去，系数是有理函数；
- 有理函数的分子分母次数在每一步可能翻倍，$\omega$ 步之后是双指数；
- 因此朴素欧几里得**不是**多项式时间的，即使 $K$、$X$ 的个数都固定。

正确的工具是**子结式**（subresultant）链。

**引理 5.6（子结式 gcd）.** 设 $f,g\in K[X][\lambda]$，$\deg_\lambda f,\deg_\lambda g\le\omega$，$X$ 有 $d$ 个变量，系数的高度 $\le\beta$（$\beta$ 为比特长，不是铅笔矩阵 $H$）。则：

1. 它们在 $K(X)[\lambda]$ 上的 gcd 的**本原部分**（对 $X$ 取内容后）可以用子结式 PRS 算出；
2. 该计算是**无分数**的：所有中间量都是 Sylvester 矩阵的子式，因此是 $X$ 的多项式，且系数比特长受 $\mathrm{poly}(\omega,\beta)$ 控制；
3. 计算代价是 $\mathrm{poly}(D,\beta)$，其中
$$D=\binom{d+2\omega^{2}}{d}=n^{O(p^{2})}$$
是子结式的稠密规模（$X$ 次数界 $2\omega^2$、$d$ 个变量）；它也是"$\lambda$ 次数 $\le\omega$、$X$ 次数 $\le\omega$"的多项式稠密规模的上界。

*证明.* 子结式 $S_j$ 是 $(2\omega-j)\times(2\omega-j)$ 的 Sylvester 子矩阵的行列式，其元素是 $f,g$ 在 $\lambda$ 上的系数，即 $X$ 的多项式（次数 $\le\omega$、高度 $\le H$）。子结式序列满足
$$S_{j+1}=\operatorname{prem}(S_{j-1},S_{j})\quad(\text{至多差符号与首项系数的幂}),$$
其中 $\mathrm{prem}$ 是伪余式（乘上首项系数的幂，不引入分母）。于是每一步都是多项式环内的运算，不会产生有理函数；终止时最后一个非零子结式就是 gcd 的本原部分（至多差一个非零常数，不影响"次数是否为零"的判定）。比特长：行列式的每个系数是 $\le(2\omega)!$ 项之和，每项是 $\omega$ 个系数的乘积，故界为 $\mathrm{poly}(\omega)\cdot H$ 量级，与 $\mathrm{poly}(D,H)$ 相容。代价：每个伪余式是一次 $(2\omega)\times(2\omega)$ 的行列式型计算，作用在稠密规模 $D$ 上，步数 $\le\omega$。$\square$

**引理 5.7（多多项式 gcd）.** 设 $m_1,\dots,m_\ell\in K[X][\lambda]$，$\ell=n^{O(p)}$，每个的次数与高度如引理 5.6。则 $\ell$ 个多项式的 gcd（在 $K(X)[\lambda]$ 上）可在 $\mathrm{poly}(\ell,D,H)$ 内算出；其"次数为正"的判据与逐个迭代取 gcd 的结果一致。

*证明.* 迭代：$g_1=m_1$，$g_{i+1}=\gcd(g_i,m_{i+1})$。每一步 $\deg_\lambda g_{i+1}\le\deg_\lambda g_i$，故次数单调不增，至多 $\omega$ 次"真正下降"；其余步直接返回 $g_i$。每步用引理 5.6，代价 $\mathrm{poly}(D,H)$，总代价 $\mathrm{poly}(\ell,D,H)$。$\square$

> **状态.** **[已证-纸面]**，依赖 (S4)（子结式的系数界与伪余式公式，标准结论）。

---

## 5.7 主定理

**定理 5.1（固定 $p$、几何单谱）.**
设 $p$ 固定。在**实谱几何单谱**（定义 5.1）的输入上，超平面层（$c=1$）的可行性判定可在
$$\mathrm{poly}(n,\tau)\quad\text{（具体为 }n^{O(p^{2})}\text{）}$$
位时间内完成，全程精确算术。

*证明.* 算法与代价逐项如下。

1. **压缩**：由引理 5.1，$\mathrm{poly}(n,\tau)$。
2. **分解与实根**：分解 $\chi_M$ 为不可约因子（标准事实 (S1)，$\mathrm{poly}(n,\tau)$）；对每个因子用实根隔离（(S2)）取出实根，代价 $\mathrm{poly}(n,\tau)$。由引理 5.3，每个实根 $\mu$ 满足 $[K:\mathbb Q]\le n$、$h(\mu)=\mathrm{poly}(n,\tau)$。
3. **方向**：几何单谱下 $E_\mu$ 是一维，$E_\mu^0$ 是它的子空间，故每个 $\mu$ 至多一条待检方向。取特征向量与 $E_\mu^0$ 的判定由引理 5.4，代价 $\mathrm{poly}(n,\tau)$。
4. **纤维**：$D_v$、$U_v^\perp$、$\mathcal Q_v/\overline V_{0,v}$ 的基由引理 5.4 给出，$\mathrm{poly}(n,\tau)$。
5. **图卡**：由引理 5.5，参数个数 $d_{\mathrm{chart}}\le p^{2}$（$p$ 固定，故为常数），图卡数 $\le2^{2p}$，子式个数 $n^{O(p)}$，次数 $\le\omega\le n$。
6. **判定**：在每个图卡上算子结式 gcd（引理 5.6、5.7），代价 $\mathrm{poly}(D,\beta)$，其中 $D=n^{O(p^{2})}$、$\beta=\mathrm{poly}(n,\tau)$ 是系数比特长。由于 $p$ 固定，$D=n^{O(p^{2})}$ 是 $n$ 的多项式。
7. **判定规则**：由第 4 节的满秩首项系数引理，$\operatorname{rank}H\equiv\omega$ 在每个图卡上成立，于是"$K(X)[\lambda]$ 上 gcd 次数为零"$\iff$"该图卡每个点都生成好"。因此逐图卡的结果合起来给出层的可行性的完整回答：只要有一个图卡生成好，就可行；若全部图卡全坏，就不可行。

总代价是上述各项之和。块数 $\le k\cdot2^{2p}$，各项都是 $\mathrm{poly}(n,\tau)$ 或 $n^{O(p^{2})}$，故总量为 $n^{O(p^{2})}$。$\square$

**定理 5.1 的强度与边界.** 这是**promise-class** 结果，不是一般情形的复杂度分类：

- 算法的第一步就检查定义 5.1（分解 $\chi_M$ 后看每个实根的特征空间维数），若某个实特征值的特征空间维数 $\ge2$，算法**报告"超出范围"**，而不报告"不可行"。
- 因而定理 5.1 只断言：在承诺子类上，回答正确且代价多项式。
- 第 6 节的反例说明承诺不能被随意去掉（在那里同一特征空间的不同方向给出不同回答），但**不**说明一般情形困难——一般情形的复杂度对本文是开放的。

> **状态.** **[已证-纸面]**，依赖 5.9 节列出的四条标准事实。

---

## 5.8 范围与限制

**重复特征值使底维随 $n$ 增长.** 若某个实特征值 $\mu$ 有 $d_\mu=\dim E_\mu\ge2$，则第 3 节的参数空间在 $\mu$ 处的底是 $\mathbb P(E_\mu)$，维数 $d_\mu-1$。此时图卡参数个数变成
$$\underbrace{(d_\mu-1)}_{\text{方向}}+\underbrace{(s-\delta)\bigl(r(v)-s\bigr)}_{\text{纤维}},$$
其中第二项仍 $\le p^{2}$，但第一项随 $n$ 增长。于是稠密规模 $D$ 变成 $n^{O(d_\mu+p^{2})}$，不再是 $p$ 固定的多项式界——**本节的路线在此失效**。

需要分清三种失效方式：几何还在（第 3 节的参数化对任意 $d_\mu$ 都成立）、精确判定还在（第 4 节的逐图卡计算对任意 $d_\mu$ 都正确），失效的只是**复杂度界**。这与第 1.5 节的三条主张分层一致。

**其它未覆盖的情形.**

1. 本节只处理 $c=1$。$c\ge2$ 的层没有对应的方向—纤维分解，不在本文范围。
2. 本节假设 $\mathcal L$ 行满秩，这与问题的定义一致；由它推出 $\operatorname{rank}L_0=r_0$ 是可行性必要条件（否则任何 $q$ 都不可行），算法把它作为零成本前置检查。
3. 实点稠密性：由第 4 节，每个参数图表是有理实图表、实点 Zariski 稠密，故"生成好"的开集里必含实可行设计；本节的多项式界是对这些实图表的界，不涉及复数点与实数点的差异。

---

## 5.9 依赖的标准事实

本节的结果只依赖以下四条，都可在标准文献中找到；本文不重新证明它们。

- **(S1) 整系数多项式的分解.** 次数 $N$、系数比特长 $\beta$ 的整系数多项式可在 $\mathrm{poly}(N,\beta)$ 位时间内分解为不可约因子（LLL 型算法）。
- **(S2) 实根隔离.** 同上规模的多项式，其相异实根可在 $\mathrm{poly}(N,\beta)$ 位时间内分离为互不相交的有理区间，每个区间含恰好一个实根，并可给出任意精度的有理逼近。
- **(S3) 代数数域的算术.** 对次数 $d$、高度 $h$ 的数域 $K=\mathbb Q[\mu]/(f)$，其元素（用坐标表示）的加、乘、求逆都是 $\mathrm{poly}(d,h)$ 位；判定"是否为零"是精确的。
- **(S4) 子结式.** 两个 $\lambda$-多项式的子结式链给出它们在分式域上的 gcd 的本原部分，且所有中间量都是 Sylvester 子矩阵的行列式，其系数比特长受输入次数与高度的多项式控制。

前三条是代数数论与符号计算的标准结论；第四条是子结式理论的标准部分。本文对它们的依赖仅限于"存在多项式时间的算法"这一层面，不涉及具体常数。

---

## 5.10 状态汇总

| 条目 | 内容 | 状态 |
|---|---|---|
| 定义 5.1 | 实谱几何单谱（$\dim\ker(M-\mu I)=1$） | — |
| 引理 5.1 | 压缩高度：$N,M$ 元素比特长 $\mathrm{poly}(n,\tau)$ | 已证-纸面（Hadamard + Bareiss） |
| 引理 5.2 | $\chi_M$ 系数高度 $\mathrm{poly}(n,\tau)$ | 已证-纸面 |
| 引理 5.3 | 根高度 $h(\mu)$、次数 $\le n$、实根隔离 | 已证-纸面（依赖 (S1)(S2)） |
| 引理 5.4 | 特征向量与纤维基在同一数域上、高度 $\mathrm{poly}$ | 已证-纸面 |
| 引理 5.5 | 图卡规模：$d_{\mathrm{chart}}\le p^{2}$、子式 $n^{O(p)}$、图卡 $O(1)^{p}$、次数 $\le\omega$ | 已证-纸面 |
| 引理 5.6 | 子结式 gcd：无分数、稠密规模 $D=n^{O(p^{2})}$ | 已证-纸面（依赖 (S4)） |
| 引理 5.7 | 多多项式 gcd 的迭代 | 已证-纸面 |
| 定理 5.1 | 固定 $p$ + 几何单谱 $\Rightarrow$ $\mathrm{poly}(n,\tau)$ | 已证-纸面（promise-class） |

**本节不声称的：** 一般（非几何单谱）情形的复杂度；$c\ge2$ 的层；以及"允许 $\mathcal L$ 行相关"的变体（本文按问题定义要求行满秩，见第 5.8 节第 2 条）。

# 6 重复特征值反例

本节给出一个完整的、有理数域上的实例，用来否定超平面层中的一个自然简化：**对压缩的每个相异实特征值只取一个特征向量作为代表方向**。在这一实例中，压缩矩阵有一个二维的实特征空间；该特征空间内的不同射影方向给出**不同**的可行性结论——其中一个方向可行，其余全部不可行。

需要强调的是，本节的结论是有限制的（见 §6.6）：它否定的是上述**代表元约化**，并不证明重复特征空间情形在计算上困难，也不说明"实谱几何单谱"是多项式时间结论的必要条件。

本节的全部计算均为**精确有理算术**（无浮点、无随机采样）；坏方向的结论由函数域上的整除证书给出，好方向的结论由一个有理图卡点上的证书给出。证书的展开形式见附录。

---

## 6.1 记号与层的位置

沿用全文记号：$K_0=\ker[C;CA]$，$k=\dim K_0$，$N$ 为 $K_0$ 的一组基，$H=LN$，$H_A=LAN$，
$\omega=\operatorname{rank}H$，$P(\lambda)=\lambda H-H_A$，$\rho=\operatorname{rank}[C;CA]$（故 $k=n-\rho$），
观测器为 $\mathcal L=[L_0;R]$，共 $q$ 行，行空间 $V=\operatorname{row}\mathcal L$。

本节考虑**超平面层** $c=k-\omega=1$，即 $\omega=k-1$。此时 $\ker H$ 是一维的，
记为 $\mathbb C v$，其中 $v\in K_0$；$\mathcal L$ 的每一行都消去 $v$ 与 $Av$，于是
$$V\subseteq U_v^\perp,\qquad \dim(V\cap K_0)=k-1,\qquad U_v=\operatorname{span}(v,Av).$$

由方向定理，在 $L_0$ 为空时，可容许的方向恰为压缩 $M=\pi_{K_0}A|_{K_0}$ 的实特征向量方向；
若 $Mv=\mu v$，则 $\dim(K_0\cap U_v^\perp)=k-1$。记
$$D_v=K_0\cap U_v^\perp,\qquad \mathcal Q_v=U_v^\perp/D_v,\qquad s=q-k+1 .$$
给定方向 $[v]$ 后，行空间恰为
$$V=D_v\oplus\langle x\rangle,\qquad 0\ne x\in\mathcal Q_v,$$
即该方向的纤维是射影空间 $\mathbb P(\mathcal Q_v)\cong\mathbb P^{r(v)-1}$，其中
$$r(v)=\dim\mathcal Q_v=\begin{cases}\rho,&v\ \text{为特征方向}\ (Av\in\operatorname{span} v),\\ \rho-1,&v\ \text{为非特征方向}.\end{cases}$$

本节取 $s=1$，于是每个方向的纤维是一个射影空间。这一点对后面"覆盖整个纤维"的论证很关键：
当 $s=1$ 时，纤维参数就是商空间中的一个非零向量，函数域上的计算直接覆盖整条纤维。

---

## 6.2 完整实例

取
$$n=8,\qquad p=2,\qquad q=4,\qquad C=\begin{bmatrix}e_1\\ e_2\end{bmatrix},\qquad L_0\ \text{为空}.$$

状态矩阵取
$$
A=\begin{bmatrix}
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
1&-2&1&0&-1&1&1&-1\\
-1&2&1&0&2&-2&-1&2\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&2&0\\
0&0&0&0&0&0&0&3
\end{bmatrix}.
$$

$A$ 的块结构值得记下：右下 $4\times4$ 块是 $\operatorname{diag}(1,1,2,3)$；右上 $4\times4$ 块是
$\begin{bmatrix}0&0&0&0\\0&0&0&0\\-1&1&1&-1\\2&-2&-1&2\end{bmatrix}$，它给出 $A_{21}$；左下 $4\times4$ 块为零；
左上 $4\times4$ 块是 $\begin{bmatrix}0&0&1&0\\0&0&0&1\\1&-2&1&0\\-1&2&1&0\end{bmatrix}$，其前两行给出 $CA=[e_3;e_4]$，后两行是 $CA^2$ 的前四个坐标。
输出矩阵 $C=[e_1;e_2]$ 单独给出，于是 $[C;CA]=[e_1;e_2;e_3;e_4]$。

由 $C=[e_1;e_2]$ 与 $A$ 的前两行可见
$$[C;CA]=\begin{bmatrix}e_1\\ e_2\\ e_3\\ e_4\end{bmatrix},$$
故
$$K_0=\operatorname{span}\{e_5,e_6,e_7,e_8\},\qquad
N=\begin{bmatrix}0&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\\1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}.$$
于是
$$\rho=4,\qquad k=4,\qquad \omega=k-1=3,\qquad s=q-k+1=1 .$$

压缩矩阵为
$$M=\pi_{K_0}A|_{K_0}=\operatorname{diag}(1,1,2,3),$$
其特征多项式为
$$\chi_M(x)=(x-3)(x-2)(x-1)^2 .$$
$A$ 在 $K_0^\perp$ 上的分量 $A_{21}=\pi_{K_0^\perp}A|_{K_0}$，按 $K_0$ 的坐标写成 $8\times4$ 矩阵，为
$$
A_{21}=\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
-1&1&1&-1\\
2&-2&-1&2\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{bmatrix}.
$$

**直接验证（精确）。** 下列各条均成立，可作为实例的自检：

1. $[C;CA]=[e_1;e_2;e_3;e_4]$，故 $K_0=\operatorname{span}\{e_5,\dots,e_8\}$；
2. $N^{\mathsf T}N=I_4$，$N^{\mathsf T}AN=\operatorname{diag}(1,1,2,3)$；
3. $AN=NM+A_{21}$（把 $A$ 在 $K_0$ 上的作用分成 $K_0$ 内与 $K_0^\perp$ 内两部分）；
4. $\chi_M(x)=(x-3)(x-2)(x-1)^2$。

**关于实例的来源。** 该实例由一个更一般的算例经以下方式得到：保留其输出矩阵 $C$ 与 $A$ 在
$K_0$ 之外的部分，只把 $A$ 在 $K_0$ 上的作用替换为 $\operatorname{diag}(1,1,2,3)$。
这样做的目的是**可控地制造一个二维实特征空间**，同时保持 $K_0$ 与层的位置（$\rho=4$、$k=4$、$\omega=3$）
不变；否则"重复特征值"的出现依赖具体数值，不便作为反例。替换后所有几何量（$K_0$、$\rho$、$k$、$\omega$、$s$）
都可直接核验，如上列四条所示。

---

## 6.3 方向几何

$\chi_M$ 的因子 $(x-1)^2$ 给出一个**二维**特征空间
$$E_1=\ker(M-I)=\operatorname{span}\{e_1,e_2\}\subseteq\mathbb C^4 ,$$
这里 $e_1,e_2$ 指 $K_0$ 的坐标向量，对应状态空间中的 $e_5,e_6$。另两个特征值 $2$ 与 $3$ 的特征空间都是一维的。

$E_1$ 中的方向写成
$$v(c_1,c_2)=c_1e_5+c_2e_6,\qquad (c_1,c_2)\ne(0,0),$$
即射影直线 $\mathbb P(E_1)\cong\mathbb P^1$。

**特征/非特征分层。** 对 $c=(c_1,c_2,0,0)^{\mathsf T}\in E_1$，
$$A_{21}c=(c_2-c_1)\begin{bmatrix}1\\-2\\0\\0\\0\\0\\0\\0\end{bmatrix},$$
于是
$$A_{21}c=0\iff c_1=c_2 .$$
即 $E_1$ 中**特征方向只有一个**：$[1:1]$；其余所有方向都是非特征的。这与分层的一般描述一致：
特征方向在 $E_\mu$ 中构成线性子空间 $\ker A_{21}$，此处 $\ker A_{21}\cap E_1$ 是一维的。

对特征方向 $[1:1]$，直接验证得 $Av=v$（即 $v$ 也是 $A$ 本身的特征向量，特征值 $1$），所以 $\dim U_v=1$。

**纤维。** 本节 $s=1$、$\delta=0$（$L_0$ 为空），故给定方向后的纤维是
$$\mathbb P(\mathcal Q_v)\cong\begin{cases}\mathbb P^{2},&r(v)=\rho-1=3\quad(\text{非特征}),\\[2pt] \mathbb P^{3},&r(v)=\rho=4\quad(\text{特征}).\end{cases}$$
也就是说，特征方向 $[1:1]$ 的纤维比其他方向**多一个齐次参数**。

把维数逐项写出来（$n=8$、$k=4$）：

| 量 | 非特征方向 | 特征方向 |
|---|---|---|
| $\dim U_v$ | $2$ | $1$ |
| $\dim U_v^\perp=n-\dim U_v$ | $6$ | $7$ |
| $\dim D_v=k-1$ | $3$ | $3$ |
| $r(v)=\dim U_v^\perp-\dim D_v$ | $3$ | $4$ |
| 纤维 $\mathbb P^{r(v)-1}$ | $\mathbb P^2$ | $\mathbb P^3$ |
| 自由参数个数（齐次坐标） | $3$ | $4$ |

两行的差别完全来自 $\dim U_v$：特征方向把 $Av$ 落进 $\operatorname{span}v$，于是 $U_v$ 少一维、其对偶空间多一维。

**例：方向 $(1:0)$ 的具体几何。** 此时 $v=e_5$，$Av=Ae_5=(0,0,-1,2,1,0,0,0)^{\mathsf T}$。在 $K$ 坐标下
$$D_v=K_0\cap U_v^\perp=\{z\in K_0:\ z\cdot v=z\cdot Av=0\}=\operatorname{span}\{e_6,e_7,e_8\},$$
故 $D_v$ 三维、$\mathcal Q_v=U_v^\perp/D_v$ 三维，纤维为 $\mathbb P^2$：行空间为
$$\operatorname{row}\mathcal L=\operatorname{span}\{e_6,e_7,e_8\}\oplus\langle x\rangle,\qquad 0\ne x\in\mathcal Q_v .$$

取
$$\mathcal L=\begin{bmatrix}\ell_1\\ \ell_2\\ \ell_3\\ x\end{bmatrix},\qquad
\ell_1,\ell_2,\ell_3\ \text{为}\ D_v\ \text{的基},\ x\in\mathcal Q_v,$$
则
$$H=LN,\qquad H_A=LAN,$$
极大子式 $m_I(x,\lambda)$（$3\times3$，共 $\binom43\binom43=16$ 个，其中若干恒为零）是 $(x,\lambda)$ 的多项式。
判定依据是全文的判据：纤维生成好 $\iff$ 全体极大子式在函数域上无公共根，即 $\gcd_I m_I=1$。

---

## 6.4 六个方向的判定结果

在 $\mathbb P(E_1)$ 中取六个方向（第三个为特征方向，其余为非特征）：

| 方向 $(c_1:c_2)$ | 类型 | 纤维 | 非零极大子式个数 | $\deg_\lambda\gcd$ | 结论 |
|---|---|---|---|---|---|
| $(1:0)$ | 非特征 | $\mathbb P^2$ | 2 | 2 | 整条纤维不可行 |
| $(0:1)$ | 非特征 | $\mathbb P^2$ | 2 | 2 | 整条纤维不可行 |
| $(1:1)$ | **特征** | $\mathbb P^3$ | 4 | **0** | **存在可行点** |
| $(1:2)$ | 非特征 | $\mathbb P^2$ | 4 | 2 | 整条纤维不可行 |
| $(2:-1)$ | 非特征 | $\mathbb P^2$ | 4 | 2 | 整条纤维不可行 |
| $(3:1)$ | 非特征 | $\mathbb P^2$ | 4 | 2 | 整条纤维不可行 |

表中"$\deg_\lambda\gcd$"是全体极大子式在相应函数域上的最大公因子的 $\lambda$-次数；次数 $0$ 表示无公共根（生成好），次数 $2$ 表示存在公共根（不可行）。"非零极大子式个数"指 $16$ 个 $3\times3$ 子式中在函数域上不恒为零的个数。

**观察。** 同一个二维特征空间内，方向 $(1:1)$ 的纤维含有可行的行空间，而其余五个方向的每一条纤维都不可行。因此可行性在 $\mathbb P(E_1)$ 上**不是常数**。

**关于 $(1:1)$ 的特殊性。** 它是 $E_1$ 中唯一的特征方向，其纤维维数比其余方向多一。这不是巧合：
特征方向意味着 $Av=\mu v\in\operatorname{span} v$，于是 $\dim U_v=1$、$\dim U_v^\perp=n-1$，从而 $r(v)=\rho$ 比非特征方向的 $\rho-1$ 大一。

**关于"非零子式个数"的差异。** 子式个数在两组方向间不同（$2$ 与 $4$），这是由方向的具体代数结构决定的；它不影响判定，因为判据用的是**全体**子式的 gcd。

### 6.4.1 其余两个特征值

$M$ 的另两个特征值 $2$ 与 $3$ 的特征空间都是一维的，各给出**唯一**一个方向（$\mathbb P^0$ 是一个点），因此不必讨论方向参数。对这两个方向做同样的精确计算：

| 特征值 $\mu$ | 类型 | 纤维 | 非零极大子式个数 | 函数域上的 gcd | 结论 |
|---|---|---|---|---|---|
| $2$ | 非特征 | $\mathbb P^2$ | 4 | $-2x_2(\lambda-1)$ | 整条纤维不可行 |
| $3$ | 非特征 | $\mathbb P^2$ | 2 | $-x_2(\lambda-1)^2$ | 整条纤维不可行 |

两个公因子的 $\lambda$-部分都是 $(\lambda-1)$ 的幂，即公共根恰为 $\lambda=1$。（$x_2$ 同样是退化轨迹上的参数因子，理由与 §6.5.1 相同。）

于是本实例的层中，在**全部被检验的方向**（$E_1$ 的六个方向、$E_2$ 与 $E_3$ 各一个方向）里，唯一可行的是 $[1:1]$——而它恰是 $E_1$ 中唯一的特征方向。这个对比强化了本节的结论：可行性在方向参数上高度不连续，而"取一个代表元"的做法恰好会错过它。

### 6.4.2 公共根的位置

把上面得到的公因子写成 $\lambda$ 的多项式（略去参数因子 $x_2$ 与常数）：

| 方向 | 公因子的 $\lambda$-部分 | 公共根 |
|---|---|---|
| $(1:0)$ | $(\lambda-1)(\lambda-3)$ | $\lambda=1,\ 3$ |
| $\mu=2$ 的方向 | $(\lambda-1)$ | $\lambda=1$ |
| $\mu=3$ 的方向 | $(\lambda-1)^2$ | $\lambda=1$ |

三个方向的公共根分别是 $\{1,3\}$、$\{1\}$、$\{1\}$，都落在压缩矩阵的谱 $\{1,2,3\}$ 之内。这与"谱条件在特征值处最易失效"的一般直觉一致；本节不对这一点作一般性断言，只记录本实例中的事实。

**注意采样范围。** 方向空间 $\mathbb P(E_1)$ 是一维的，本节在其中取了六个点（含唯一的特征方向）。这足以建立"非恒定"（一个好点与一个坏点即可），但**不构成**对 $\mathbb P(E_1)$ 全体方向的分类。

---

## 6.5 证书

### 6.5.1 坏方向：函数域上的整除证书

对表中共五个非特征方向，精确计算给出：在函数域 $\mathbb Q(x_1,\dots,x_{r(v)-1})$ 上，
$$\deg_\lambda g=2,\qquad g\mid m_I\quad\text{对每个极大子式 } I,$$
其中整除性通过函数域上的带余除法验证（余式为零）。

以方向 $(1:0)$ 为例，$r(v)-1=2$，纤维的齐次坐标记为 $(x_0:x_1:x_2)$，其函数域上的 gcd 恰为
$$g=x_2\,(\lambda-1)(\lambda-3).$$
这是一个可以直接核对的显式式子：它的 $\lambda$-部分是 $(\lambda-1)(\lambda-3)$，而因子 $x_2$ 来自参数本身。
$x_2=0$ 的位置正是 $\operatorname{rank}H<\omega$ 的退化轨迹（该处全部极大子式同时消失），不属于参数图卡；
在 $\operatorname{rank}H=\omega$ 的开集上，$g$ 特化为非常数多项式 $x_2\cdot(\lambda-1)(\lambda-3)$，整除每个极大子式。

**为什么"整除"就足以断言整条纤维不可行。** 对一般的多项式族，"函数域上 gcd 正次数"并**不**能推出每个特化点都有公共根——公因子可能在某点退化为非零常数。本实例之所以可以断言整条纤维不可行，依据是全文的**满秩首项系数引理**：

> 在参数图卡的每一点，$\operatorname{rank}H=\omega$ 恒成立；故每一点处至少有一个极大子式的 $\lambda$-次数恰为 $\omega$。
> 若函数域上的公因子 $g$ 为非常数，则它的任一特化 $g(x_0,\cdot)$ 都不可能退化为非零常数（否则每个极大子式的次数都 $<\omega$，矛盾）。
> 于是每个特化点都含非平凡公因子。

由于本节 $s=1$，纤维就是一个射影空间中的一个非零向量（模数乘），上述论证覆盖它的**每一个非退化点**，而不只是某个图卡或某个样本点。这正是本节证书与"测了一个点"的本质区别。

**整除证书的具体形式。** 说"$g$ 整除每个 $m_I$"是指：在函数域上做带余除法
$$m_I=g\cdot q_I+r_I,\qquad \deg_\lambda r_I<\deg_\lambda g,$$
并得到 $r_I=0$。这一步对每个极大子式逐一验证，全部运算是有理数上的精确算术。由于 $g$ 的表达式很短（例如 $(1:0)$ 的 $g=x_2(\lambda-1)(\lambda-3)$），商 $q_I$ 的规模也有限，证书可以逐行写出，见附录。

### 6.5.2 好方向：有理图卡点上的证书

对特征方向 $[1:1]$，在纤维 $\mathbb P^3$ 上取有理点
$$x_0=(1,2,3,4).$$
在该点处，全部极大子式的最大公因子为
$$\gcd_I m_I(x_0,\lambda)=1,$$
即存在多项式 $u_I(\lambda)$ 使
$$\sum_I u_I(\lambda)\,m_I(x_0,\lambda)=1 .$$
这给出一个**具体的可行设计**：$\mathcal L=[\ell_1;\ell_2;\ell_3;x_0]$（按上述基展开为状态空间中的向量），
其压缩铅笔满足两条结构条件与谱条件。

好方向只需要一个点：可行性是一个开条件，一个点可行即足以断言该实例可行。坏方向则相反，需要覆盖整条纤维——两者的证书强度不同，这一点在 §6.5.1 中已经用满秩引理处理。

### 6.5.3 三种"坏"的区别

在讨论覆盖范围时，需要区分三种命题：

1. **某个行空间坏**（某一点上存在公共根）；
2. **某个方向的整条纤维坏**（该纤维的每一点都坏）；
3. **某个特征空间的所有方向都坏**（整个 $\mathbb P(E_\mu)$ 上处处坏）。

本节中，五个非特征方向的结论是第 2 种，由函数域 gcd 加满秩引理得到；方向 $(1:1)$ 的结论是"存在好点"，
即第 1 种的反面。第 3 种在本实例中**不成立**（因为 $(1:1)$ 是好的）——这正是反例的内容。

---

## 6.6 结论的精确措辞

由 §6.4 与 §6.5，可以陈述：

> **命题（反例）。** 存在 $n=8$、$p=2$、$q=4$ 的有理实例，使得超平面层中压缩矩阵有二维实特征空间 $E_1$；
> 在该特征空间内，方向 $[1:1]$ 的纤维含有可行的观测器，而所检验的五个非特征方向的纤维全部不可行。
> 因此可行性在该特征空间上不是常数。

由此立刻得到：

> **推论.** "对压缩的每个相异实特征值取一个特征向量作为代表方向、并据此判定可行性"这一约化**不成立**：
> 选取代表元 $(1:0)$ 会判定该实例不可行，而实例实际可行。

**限制。** 本节的结论不包含以下任何一项：

1. 它**不**证明重复特征空间情形在计算上困难——反例否定的是一个特定的约化，而不是一般算法的存在性；
2. 它**不**说明"实谱几何单谱"是多项式时间可判定性的必要条件——该假设的作用是控制方向参数空间的维数，
   反例只说明这一维数不能被忽略；
3. 它**不**对 $E_1$ 中未被检验的方向作出断言，也不对方向参数空间的正维数部分给出分类。

关于可复现性：矩阵 $A$、$C$、$N$、$M$、$A_{21}$ 与特征多项式已在 §6.2 完整给出；
六方向的判定结果、坏方向的整除证书（含 $(1:0)$ 的显式公因子）与好方向的图卡点证书均为精确有理计算，
其展开形式见附录。

**自检清单。** 独立复现本节结论需要且只需要以下几步，全部在有理数域上进行：

1. 由 $C$ 与 $A$ 算出 $[C;CA]$，验证其等于 $[e_1;e_2;e_3;e_4]$，从而 $K_0=\operatorname{span}\{e_5,\dots,e_8\}$；
2. 取 $N$ 为单位嵌入，验证 $N^{\mathsf T}AN=\operatorname{diag}(1,1,2,3)$ 与 $AN=NM+A_{21}$；
3. 对 $\mu=1,2,3$ 分别求 $\ker(M-\mu I)$，得到 $E_1$（二维）、$E_2$、$E_3$（各一维）；
4. 对每个方向计算 $D_v=K_0\cap U_v^\perp$ 与 $\mathcal Q_v=U_v^\perp/D_v$，取 $V=D_v\oplus\langle x\rangle$；
5. 写出 $H=LN$、$H_A=LAN$ 与全部 $3\times3$ 极大子式 $m_I(x,\lambda)$；
6. 在函数域上算 $\gcd_I m_I$：次数为 $0$ 即该方向可行，为正即整条纤维不可行（用满秩首项系数引理）；
7. 对 $[1:1]$ 在 $x_0=(1,2,3,4)$ 处特化，验证 $\gcd_I m_I(x_0,\lambda)=1$。

第 6、7 步的全部运算都是有理数上的精确算术（函数域上的除法与欧几里得算法），不含任何浮点近似或随机采样。

---

## 6.7 与后文的关系

本节的反例说明：超平面层的参数空间必须保留**整个**射影特征空间 $\mathbb P(E_\mu)$ 作为方向参数
（在几何单谱的情形下它退化为一个点，这正是第 5 节复杂度定理所处理的情形）。
因此第 5 节的多项式时间结论以"实谱几何单谱"为前提，而重复特征空间情形的一般判定问题不在本文的定理范围之内。

从结构上看，本节的实例也印证了参数化定理的两个要点：其一，方向参数是真实的自由度，不能被行空间的参数吸收；
其二，特征与非特征两个分层的纤维维数不同（$\rho$ 与 $\rho-1$），因而在枚举时必须分别处理。

**对判定算法的含义。** 若一个判定程序只在每个特征值处取一个方向，它在本实例上会选择 $(1:0)$（或任何非特征代表），
从而返回"不可行"——与事实相反。要得到正确结论，程序必须（至少在重复特征空间上）枚举整个射影特征空间作为方向参数：
在本节所检验的六个方向中，只有 $[1:1]$ 可行，而它是 $\mathbb P(E_1)\cong\mathbb P^1$ 上由线性条件 $c_1=c_2$ 切出的一个点。
这说明方向参数不能像行空间参数那样"任取一般点"，必须被显式地纳入参数空间或其分层描述之中。

# 7 与既有压缩表述的关系

本文的结果建立在两篇既有工作的压缩表述之上；这一节把"继承"与"新增"分开，避免重复陈述。

## 7.1 从既有工作中继承的部分

- **压缩形式本身**：用 $K_0=\ker[C;CA]$ 的基把 $(5a)(5b)$ 化成 $q\times k$ 铅笔的秩条件，是既有工作给出并使用的形式；本文第 2.2 节的引理 2.1 只是把它写成"公根条件"以便与本文的参数化对接。
- **范数/秩的记账**：$\rho=\operatorname{rank}[C;CA]$、$k=n-\rho$、$\omega=\operatorname{rank}H$ 以及 $\omega=\dim(V\cap K_0)$ 这些量在既有工作中已经建立；本文的 $c=k-\omega$ 只是给它们一个名字。
- **子空间表述的可行性判据**：既有工作用压缩后的行对空间 $W$ 描述可行性，并给出 $\omega+1\le\dim W\le2\omega$ 的阶界；本文第 3 节的对偶命题正是与它对接。
- **公根检验作为谱条件的判据**：极大子式的 $\gcd$ 判据是既有工作的方法；本文在第 4 节沿用，并补上它在"整图卡"上的正确性（满秩首项系数引理）。

## 7.2 本文新增的部分

- **方向定理**：可容许方向恰是 $M$ 的实特征向量（带预设行时是 $E_\mu^0$ 里的方向）。既有工作只给出必要条件的雏形；把"充要"与"预设行相容"一起写出是本文的（第 3 节）。
- **相对 Graßmann 丛参数化**：层的参数空间是有限个相对丛，纤维 $\operatorname{Gr}(s-\delta,\mathcal Q_v/\overline V_{0,v})$，维数显式。既有工作的子空间表述不含这一参数化。
- **精确判定在整图卡上的正确性**：闭性、有限覆盖、满秩首项系数引理、实点稠密性；这是把"公根检验"从一个"图上可算的判据"变成"判定整层的算法"的部分。
- **固定 $p$ 位复杂度**：在实谱几何单谱下的多项式界（第 5 节）。
- **重复特征值反例**（第 6 节）。
- **方向对偶命题**（第 3 节末）：$[a]=\mathbb P(\operatorname{Ann}(U))$、$U=a^\circ$；既有的子空间表述与本文的射影方向表述通过它互相翻译。

## 7.3 对照表

| 内容 | 来源 | 本文的角色 |
|---|---|---|
| 压缩铅笔 $H,H_A$、$\omega$、$\rho,k$ | 既有工作 | 记号与出发点 |
| $(5b)\iff$ 极大子式无公根 | 既有工作 | 判定工具（第 4 节补正确性） |
| $W$ 的可行性与 $\omega+1\le\dim W\le2\omega$ | 既有工作 | 第 3.7 节对偶命题的另一侧 |
| 可容许方向 $=$ 压缩特征向量 | 本文 | 第 3.2 节 |
| 预设行相容空间 $E_\mu^0$ | 本文 | 第 3.3 节 |
| 相对 Graßmann 参数化与维数 | 本文 | 第 3.6 节 |
| 整图卡的判定正确性 | 本文 | 第 4 节 |
| 固定 $p$ 位复杂度 | 本文 | 第 5 节 |
| 重复特征值反例 | 本文 | 第 6 节 |

## 7.4 与"最小阶"的关系

本文不计算最小阶，只判定**给定**的层是否可行。最小阶需要在整个阶谱上做搜索，超出本文范围；本文的贡献是把其中**最小的非平凡层**彻底描述清楚，并提供在该层上的精确判定与（子类上的）复杂度。

# 附录 A 完整数据与精确证书

本附录给出第 6 节反例的全部输入与证书，使读者可以独立复现。所有算术在有理性上进行，无舍入。

## A.1 输入

$n=8$，$p=2$，行数 $q=4$，$L_0$ 为空（$r_0=0$）。

$$C=\begin{bmatrix}1&0&0&0&0&0&0&0\\0&1&0&0&0&0&0&0\end{bmatrix},$$

$$A=\begin{bmatrix}
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
1&-2&1&0&-1&1&1&-1\\
-1&2&1&0&2&-2&-1&2\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&2&0\\
0&0&0&0&0&0&0&3
\end{bmatrix}.$$

## A.2 导出的量

$$\operatorname{rank}\begin{bmatrix}C\\ CA\end{bmatrix}=4,\qquad k=4,\qquad \rho=4,\qquad \omega=3,$$

$$N=\begin{bmatrix}0&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\\1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix},\qquad
M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN=\operatorname{diag}(1,1,2,3),$$

$$\chi_M(t)=(t-3)(t-2)(t-1)^2,\qquad A_{21}=\begin{bmatrix}
0&0&0&0\\0&0&0&0\\-1&1&1&-1\\2&-2&-1&2\\0&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{bmatrix}.$$

注意 $A_{21}$ 有两行非零；它就是第 3 节里区分特征/非特征方向的那个映射。

## A.3 方向与纤维

$\mu=1$ 的特征空间是 $E_1=\operatorname{span}\{e_1,e_2\}\subseteq\mathbb R^4$（$K_0$ 坐标），故 $\mathbb P(E_1)\cong\mathbb P^1$。

对方向 $v=N(c_1,c_2,0,0)$：

- $A_{21}(c_1,c_2,0,0)^{\mathsf T}=0$ 当且仅当 $c_1=c_2$（由 $A_{21}$ 的前两列）；故 $(1,1)$ 是**特征方向**，其余是**非特征方向**。
- 特征方向的纤维是 $\operatorname{Gr}(1,\rho)=\mathbb P^3$（$s=1$，$\delta=0$）；非特征方向是 $\operatorname{Gr}(1,\rho-1)=\mathbb P^2$。

## A.4 六方向的结论

| 方向 $(c_1,c_2)$ | 类型 | $\deg_\lambda\gcd$ | 结论 |
|---|---|---|---|
| $(1,0)$ | 非特征 | 2 | 全坏 |
| $(0,1)$ | 非特征 | 2 | 全坏 |
| $(1,1)$ | **特征** | **0** | **生成好** |
| $(1,2)$ | 非特征 | 2 | 全坏 |
| $(2,-1)$ | 非特征 | 2 | 全坏 |
| $(3,1)$ | 非特征 | 2 | 全坏 |

## A.5 证书

**坏方向**（以 $(1,0)$ 为例）：令 $g(x,\lambda)$ 为函数域上算出的公因子（$\lambda$-次数 2）。证书是

$$g \mid m_I(x,\lambda)\qquad\text{对每个极大子式 } m_I,$$

在有理函数域 $\mathbb Q(x)[\lambda]$ 上逐一验证（带余除法余式为零）。对其余坏方向同理（$(1,2)$、$(2,-1)$、$(3,1)$ 各有 4 个非零极大子式，$(1,0)$、$(0,1)$ 各有 2 个）。

**好方向**（$(1,1)$）：纤维是 $\mathbb P^3$，参数化点 $x_0=(1,2,3,4)$；在该点算出的极大子式互素，即

$$\gcd_I\, m_I(x_0,\lambda)=1,$$

于是该点是可行的；由第 4 节的实点稠密性与开性，整条纤维上生成好。

## A.6 复现方式

1. 由 $A,C$ 算 $K_0$ 的基 $N$ 与 $M$（有理消元）；
2. 分解 $\chi_M$，取 $\mu=1$ 的特征空间；
3. 对每个方向 $c$：构造 $D_v$、$\mathcal Q_v$，取纤维图卡，算铅笔 $P(\lambda)=\lambda H-H_A$ 的极大子式；
4. 在 $\mathbb Q(x)[\lambda]$ 上算 $\gcd$（无分数子结式），得 A.4 表；
5. 对好方向，把 $x$ 取成 $x_0$，验证 $\gcd=1$。

所有步骤只用有理算术；本附录的矩阵与第 6 节表格逐项一致。

# 附录 B 高度与算术界

本附录给第 5 节各引理的**可核对细节**：每一步的比特长如何被 $\mathrm{poly}(n,\tau)$ 控制。记号与第 2、5 节一致：$A\in\mathbb R^{n\times n}$、$C\in\mathbb R^{p\times n}$、$L_0\in\mathbb R^{r_0\times n}$、$\mathcal L=[L_0;R]$（$q$ 行、行满秩）、$K_0=\ker[C;CA]$、$k=\dim K_0$、$\rho=\operatorname{rank}[C;CA]=n-k$、$N\in\mathbb R^{n\times k}$ 为 $K_0$ 的基、$M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$、$\omega=\operatorname{rank}H$（$H=\mathcal L N$）、$s=q-k+1$、$\delta=\dim V_0-\dim(V_0\cap K_0)$。$\tau$ 为输入 $(A,C,L_0)$ 与 $q$ 的二进制编码长度，即所有整数分子与分母的最大比特长。

**约定.** 对整数或分数 $x$，记 $\beta(x)$ 为其分子与分母比特长的最大值，即 $\beta(x)=\lceil\log_2|x|\rceil+1$（整数情形即通常的比特长）。对矩阵 $X$ 记 $\beta(X)=\max_{i,j}\beta(X_{ij})$，$\|X\|_\infty=\max_{i,j}|X_{ij}|$。所有对数以 2 为底。本附录的界**不追求最优常数**，只要求形状为 $\mathrm{poly}(n,\tau)$。

**为什么需要这份附录.** 第 5 节的证明依赖"所有中间量都不大"。这种话在三条路径上都可能失效，本附录逐一封住：

1. **分母**：清分母之后矩阵是整数，但清分母本身可能引入巨大的公共因子（B.1 处理）；
2. **子式**：核基、特征向量、伴随矩阵的元素都是子式之比，子式可以比原矩阵大得多（Hadamard 界，B.1–B.2 处理）；
3. **求逆与 gcd**：$(N^{\mathsf T}N)^{-1}$ 与 $K(X)[\lambda]$ 上的 gcd 都可能让分子分母爆炸（B.2 用 $\det\ge1$ 处理前者，第 5.6 节用子结式处理后者，B.5.2 补充结式的情形）。

三者都有界之后，第 5 节定理的"$\mathrm{poly}(n,\tau)$"才是一个可核对的断言，而不是一句估计。

---

## B.1 压缩基的规范化

第 2.1 节引用了"$K_0$ 的一个基 $N$"，这里把取法定死，并给出它的比特长。共四步。

**第 1 步：清分母.** 把 $[C;CA]\in\mathbb R^{2p\times n}$ 的每个元素写成既约分数。设其分母的最小公倍数为 $D_0$，令
$$\widehat W:=D_0\begin{bmatrix}C\\ CA\end{bmatrix}\in\mathbb Z^{2p\times n}.$$
$[C;CA]$ 共有 $2pn$ 个元素，每个分母的比特长 $\le\tau$，故
$$\beta(D_0)\le 2pn\tau,\qquad \beta(\widehat W)\le \tau+2pn\tau=:\beta_W .$$
（用乘积而非最小公倍数代替 $D_0$ 得到同样的量级，本附录不追求 $D_0$ 的最优。）

**第 2 步：无分数消元求核.** 对 $\widehat W$ 作 Bareiss（无分数）消元。Bareiss 的关键性质是：所有中间量都是 $\widehat W$ 的**子式**，不产生分数。于是中间量的比特长受子式界控制。对任意 $j\times j$ 子矩阵，Hadamard 界给出
$$|\det|\le\prod_{i=1}^{j}\|\text{row}_i\|_2\le\bigl(\sqrt{j}\,\|\widehat W\|_\infty\bigr)^{j},$$
故
$$\log_2|\det|\le \tfrac{j}{2}\log_2 j+j\,\beta_W\le \tfrac{\rho}{2}\log_2\rho+\rho\,\beta_W ,$$
其中 $j\le\rho$（$[C;CA]$ 的秩）。这一步的算术次数是 $O(p\,n\,\min(p,n))$，每个运算作用在 $\mathrm{poly}(n,\tau)$ 位的整数上，故位时间为 $\mathrm{poly}(n,\tau)$。

**第 3 步：核基与清分母.** 消元后读出 $K_0$ 的基：每个坐标是一个 $\rho\times\rho$ 子式与一个非零 $\rho\times\rho$ 主子式之比，故

$$\beta(\text{坐标})\le 2\Bigl(\tfrac{\rho}{2}\log_2\rho+\rho\,\beta_W\Bigr)=:2\beta_K .$$

把每列乘以各分母的最小公倍数，得到**整数**列。

**第 4 步：本原化.** 对整数列的每个列向量，除以它所有分量的最大公约数 $g$。因为 $g\ge1$ 是整数，除以它只会**减小**每个分量的绝对值，故比特长不增加：$\beta(N)\le 2\beta_K$。

**引理 B.1（压缩基）.**
$$\beta(N)\le 2\beta_K=2\Bigl(\tfrac{\rho}{2}\log_2\rho+\rho\,\beta_W\Bigr),\qquad \beta_W=\tau+2pn\tau .$$
基 $N$ 可在 $\mathrm{poly}(n,\tau)$ 位时间内算出。

*说明.* 四步的算术次数都是 $n$ 的多项式；每步的每个运算作用在 $\mathrm{poly}(n,\tau)$ 位的整数上；位时间等于"算术次数 × 单位运算的位代价"，故为 $\mathrm{poly}(n,\tau)$。$\square$

**为什么本原化是必要的一步.** 若不清分母、不除公约数，$N$ 的列可能带有公共的有理因子，使 $N^{\mathsf T}N$ 的行列式变成极小的分数，进而让 $M$ 的分子分母同时膨胀。本原化把 $\det(N^{\mathsf T}N)$ 拉回整数（见 B.2），这是后文所有界的基础。

**B.1.1 为什么 Bareiss 的中间量是子式.** 无分数消元在第 $t$ 步把元素更新为
$$a^{(t+1)}_{ij}=\frac{a^{(t)}_{tt}a^{(t)}_{ij}-a^{(t)}_{it}a^{(t)}_{tj}}{a^{(t-1)}_{t-1,t-1}},$$
分母恰是上一步的枢轴。归纳可见：$a^{(t)}_{ij}$ 等于"由前 $t$ 行与第 $i$ 行、前 $t$ 列与第 $j$ 列组成的 $(t+1)$ 阶子式"除以"前 $t-1$ 步的枢轴乘积"。因此**每个中间量都是子式（至多差一个已知的整数因子）**，其比特长由 Hadamard 界统一控制，而不需要逐步估计增长。这正是用 Bareiss 而不用带分数的高斯消元的原因。

**B.1.2 算术次数.** 消元是 $O(\rho^{2}n)$ 次域运算；读核基、清分母、求每列最大公约数各是 $O(nk)$ 次整数运算；最大公约数用欧几里得算法，代价是操作数比特长的多项式。总计 $\mathrm{poly}(n)$ 次算术。

---

## B.2 压缩矩阵的高度

**引理 B.2（压缩矩阵）.**
$$\beta(N^{\mathsf T}N)\le 2\beta(N)+\log_2 n,\qquad \beta(N^{\mathsf T}AN)\le 2\beta(N)+\tau+2\log_2 n,$$
且 $M$ 的元素满足
$$\beta(M)\le (k-1)\Bigl(\tfrac12\log_2 k+\beta(N^{\mathsf T}N)\Bigr)+\beta(N^{\mathsf T}AN)+\beta\bigl(\det(N^{\mathsf T}N)\bigr),$$
右端是 $\mathrm{poly}(n,\tau)$。

*证明.* (i) $N^{\mathsf T}N$ 的元素是 $\sum_{l=1}^{n}N_{li}N_{lj}$，共 $n$ 项，每项 $\le 2^{2\beta(N)}$，故比特长 $\le 2\beta(N)+\log_2 n$。

(ii) $N^{\mathsf T}AN$ 的元素是 $\sum_{l,m}N_{li}A_{lm}N_{mj}$，共 $n^{2}$ 项，每项 $\le 2^{2\beta(N)+\tau}$，故比特长 $\le 2\beta(N)+\tau+2\log_2 n$。

(iii) $\det(N^{\mathsf T}N)$ 是**正整数**：$N$ 是实矩阵且列满秩，$N^{\mathsf T}N$ 正定；又 $N$ 是整数矩阵，故 $N^{\mathsf T}N$ 是整数矩阵、行列式为正整数，于是
$$\det(N^{\mathsf T}N)\ge 1 .$$
这条下界是关键的：它说明 $(N^{\mathsf T}N)^{-1}=\operatorname{adj}(N^{\mathsf T}N)/\det(N^{\mathsf T}N)$ 的分母不会把分子"挤小"，分子只需由伴随矩阵的界控制。

(iv) $M=\operatorname{adj}(N^{\mathsf T}N)\,N^{\mathsf T}AN/\det(N^{\mathsf T}N)$。伴随矩阵的元素是 $k-1$ 阶子式，由 Hadamard 界
$$\beta\bigl(\operatorname{adj}(N^{\mathsf T}N)\bigr)\le (k-1)\Bigl(\tfrac12\log_2 k+\beta(N^{\mathsf T}N)\Bigr).$$
乘上 $N^{\mathsf T}AN$、再以 $\det(N^{\mathsf T}N)$ 为分母，比特长是三者之和，即所述。$\square$

**推论 B.2.1.** $M$ 的元素的比特长是 $\mathrm{poly}(n,\tau)$；特别地，存在常数 $c_1$ 使
$$\beta(M)\le c_1\bigl(n^{3}\tau+n^{2}\log_2 n\bigr).$$
（本附录不优化 $c_1$；重要的是它是 $n$ 与 $\tau$ 的多项式。）

---

## B.3 特征多项式与根高度

**引理 B.3（特征多项式）.**
$$\beta(\chi_M)\le k\bigl(\beta(M)+\tfrac12\log_2 k\bigr)+\beta(M)+k=\mathrm{poly}(n,\tau),$$
其中 $\beta(\chi_M)$ 指清分母并取本原部分后系数的比特长。

*证明.* $\chi_M(t)=t^{k}+\sum_{i=1}^{k}(-1)^{i}\sigma_i(M)\,t^{k-i}$，$\sigma_i$ 是 $i$ 阶主子式之和。每个 $i$ 阶子式由 Hadamard 界控制在 $(\sqrt{i}\|M\|_\infty)^{i}$ 以内；求和至多 $\binom{k}{i}$ 项，只增加 $\log_2\binom{k}{i}\le k$ 位。清分母引入 $M$ 各元素分母的乘积，其对数同样是 $\mathrm{poly}(n,\tau)$。计算可用 Faddeev–LeVerrier 或插值法，算术次数 $\mathrm{poly}(n)$。$\square$

**引理 B.4（根的高度与次数）.** 设 $\mu$ 是 $\chi_M$ 的任一复根。则
$$[\mathbb Q(\mu):\mathbb Q]\le k\le n,\qquad h(\mu)\le \beta(\chi_M)+\tfrac12\log_2(k+1)+\log_2 2,$$
其中 $h$ 是对数绝对高度
$$h(\mu)=\frac{1}{[\mathbb Q(\mu):\mathbb Q]}\sum_{\sigma}\log^{+}|\sigma(\mu)|,\qquad \log^{+}x=\max\{0,\log x\},$$
求和跑遍 $\mu$ 的全部共轭。

*证明.* 次数不超过 $\deg\chi_M=k$。高度：$\mu$ 是整系数多项式 $\chi_M$ 的根，系数比特长 $\beta(\chi_M)$；Cauchy 界给出
$$|\mu|\le 1+\max_{i}\frac{|a_i|}{|a_k|}\le 1+2^{\beta(\chi_M)}\le 2^{\beta(\chi_M)+1},$$
于是每个共轭的 $\log^{+}|\sigma(\mu)|\le\beta(\chi_M)+1$；再除以次数，得所述界。$\square$

**推论 B.4.1.** $h(\mu)=\mathrm{poly}(n,\tau)$；实根可用精确实根隔离在 $\mathrm{poly}(n,\tau)$ 位时间内分离为互不相交的有理区间。

**注 B.3.1.** 引理 B.4 的界对**有理**根同样成立（此时 $h(\mu)=\log\max\{1,|\mu|\}$），故下文对有理与无理特征值用同一套估计，不需要分支。

**B.3.2 这些界是不是空的.** 取最坏但常见的量级：$\tau=1$（$0/1$ 输入）、$n=8$、$\rho=4$、$p=2$。则

$$\beta_W\le 1+2\cdot2\cdot8\cdot1=33,\qquad \beta_K\le \tfrac{4}{2}\log_2 4+4\cdot33=4+132=136,\qquad \beta(N)\le 272 .$$

接着 $\beta(N^{\mathsf T}N)\le 2\cdot272+\log_2 8=547$，$\beta(M)$ 是 §B.2 的三项之和，量级在 $4\times10^{3}$ 比特以内。也就是说：对 $n=8$ 的实例，所有中间量都在几千比特的量级，完全可算。这些界的作用不是给出可行规模，而是证明"不随输入规模指数爆炸"。

---

## B.4 特征向量与纤维基

**引理 B.5（$K$ 上的基）.** 设 $\mu$ 是 $\chi_M$ 的实根、$K=\mathbb Q(\mu)$、$d=[K:\mathbb Q]\le n$。则：

1. $E_\mu=\ker(M-\mu I)$ 在 $K$ 上有一个本原向量 $a$，其坐标（$K$ 元素的坐标表示）的比特长 $\le \beta_K':=2\bigl(\tfrac{k}{2}\log_2 k+k(\beta(M)+\beta(\mu))\bigr)$；
2. $E_\mu^0$、$U_v^\perp$、$D_v=K_0\cap U_v^\perp$、$\mathcal Q_v/\overline V_{0,v}$ 的基都可在 $K$ 上算出，比特长同为 $\mathrm{poly}(n,\tau)$；
3. 全部计算的位时间为 $\mathrm{poly}(n,\tau)\cdot\mathrm{poly}(d,\beta_K')=\mathrm{poly}(n,\tau)$。

*证明.* (1) $a$ 是 $(M-\mu I)\in K^{k\times k}$ 的核，用 Cramer 法则：其坐标是 $(k-1)$ 阶子式（在 $K$ 上）与非零 $(k-1)$ 阶主子式之比。$K$ 元素的算术代价是 $\mathrm{poly}(d,\beta(\mu))$ 位（标准事实 (S3)），子式的界由 Hadamard 与 $\beta(M)$、$\beta(\mu)$ 给出，故坐标为 $K$ 元素、其坐标表示的比特长为所述。清分母、除公约数后得到本原向量。

(2) 四者分别是 $K$ 上矩阵的核、像、和与商：$E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)$ 是两个线性条件的交；$U_v^\perp=\{x:\langle x,v\rangle=\langle x,Av\rangle=0\}$；$D_v$ 是 $K_0$ 上两条泛函的公共核；$\mathcal Q_v/\overline V_{0,v}$ 是商空间的一组补基。四者的矩阵规模都 $\le n$，用同一套无分数消元，中间量是子式，故比特长同上。

(3) $K$ 上每次算术 $\mathrm{poly}(d,\beta)$ 位，消元的算术次数是 $n$ 的多项式，$d\le n$。$\square$

**注 B.4.1（必须在 $K$ 上算）.** 当 $\mu\notin\mathbb Q$ 时，$E_\mu$ 是 $K$ 上的一条直线，而不是 $\mathbb Q$ 上的一维空间：它在 $\mathbb Q$ 上的"迹"是 $d$ 个共轭直线的直和，维数 $d$。若在 $\mathbb Q$ 上算核，会把一条方向错误地拆成 $d$ 条共轭方向，随后的纤维构造与铅笔都会变。因此方向枚举与纤维构造必须与 $\mu$ 落在同一个 $K$ 里。

**注 B.4.2（标量积与范数）.** 上述空间都在 $\mathbb R^n$ 里，正交补与投影按标准欧氏内积取；$v$ 是 $K$ 上的向量，但 $\langle\cdot,\cdot\rangle$ 的值落在 $K$ 里（因为 $A$、$C$、$L_0$ 都取有理数，$\mu$ 是 $\chi_M$ 的根）。故 $D_v$、$U_v^\perp$ 的方程系数在 $K$ 里，无需扩域。

**B.4.3 $K$ 上算术的代价，具体写出来.** 设 $K=\mathbb Q[\mu]/(f)$，$f$ 是 $\mu$ 的极小多项式，次数 $d\le n$、系数比特长 $\beta(f)\le\beta(\chi_M)$。元素用坐标 $(c_0,\dots,c_{d-1})$ 表示，$c_i$ 是比特长 $\le\beta_K'$ 的有理数。则：

- 加法：$d$ 次基域加法，代价 $O(d\beta_K')$；
- 乘法：先做 $d^{2}$ 次基域乘法（代价 $O(d^{2}\beta_K'^{2})$），再把 $2d-2$ 次的结果模 $f$ 约化（$d$ 次多项式除法，代价 $O(d^{2}\beta_K'^{2})$）；
- 求逆：扩展欧几里得，代价 $O(d^{2}\beta_K'^{2})$。

三者都是 $\mathrm{poly}(d,\beta_K')$ 位，与引理 B.5 (3) 一致。**关键点**：这些代价里没有"随 $\mu$ 与有理数距离"增长的量——$K$ 的算术是精确的代数运算，不需要把 $\mu$ 数值化。

---

## B.5 图卡的规模

固定一个实特征值 $\mu$、一条方向 $[v]\in\mathbb P(E_\mu^0)$ 与纤维
$$\operatorname{Gr}\bigl(m,\ \mathcal Q_v/\overline V_{0,v}\bigr),\qquad m=s-\delta .$$
记商丛的秩 $\widetilde r:=r(v)-\delta$，其中 $r(v)=\rho$（特征方向）或 $\rho-1$（非特征方向），$\delta=\dim V_0-\dim(V_0\cap K_0)$。

**引理 B.6（图卡规模）.**

1. **参数个数.** $d_{\mathrm{chart}}=m(\widetilde r-m)\le \widetilde r^{2}/4\le p^{2}$。
2. **次数.** 图卡行 $\mathrm{comp}_i+\sum_{j}X_{ij}\mathrm{comp}_{m+j}$ 对 $X$ 仿射；铅笔 $\lambda H-H_A$ 对 $\lambda$ 线性；故 $\omega\times\omega$ 极大子式对 $X$ 与 $\lambda$ 的次数都 $\le\omega$。
3. **子式个数.** $\binom{q}{\omega}\binom{k}{\omega}=k\binom{q}{s}$，且
$$k\binom{q}{s}\le n\sum_{j=0}^{2p+1}\binom{n}{j}=n^{O(p)} .$$
4. **图卡数.** $\mathrm{Gr}(m,\widetilde r)$ 的标准图卡数为 $\binom{\widetilde r}{m}\le 2^{\widetilde r}\le 2^{2p}$。
5. **块数.** 实特征值至多 $k\le n$ 个，每个至多一条方向（几何单谱），故总图卡数 $\le n\cdot 2^{2p}$。
6. **稠密规模.** 每个子式是"$\lambda$ 次数 $\le\omega$、$X$ 次数 $\le\omega$、$d_{\mathrm{chart}}$ 个变量"的多项式，其稠密规模为
$$D=\omega\binom{d_{\mathrm{chart}}+\omega}{d_{\mathrm{chart}}}\le n\binom{n+p^{2}}{p^{2}}=n^{O(p^{2})}.$$

*证明.* (1) $\widetilde r\le r(v)\le\rho\le 2p$；$x\mapsto x(\widetilde r-x)$ 在 $x=\widetilde r/2$ 取最大，故 $d_{\mathrm{chart}}\le\widetilde r^{2}/4\le p^{2}$。

(3) $\omega=k-1$，故 $\binom{k}{\omega}=k$；非空条件 $s\le r(v)\le\rho\le2p$，故 $\binom{q}{s}\le\sum_{j\le2p}\binom{n}{j}$；乘以 $k\le n$ 得所述。

(4) $\binom{\widetilde r}{m}\le\sum_{j}\binom{\widetilde r}{j}=2^{\widetilde r}$。

(6) 把 $D$ 展开：$\binom{d+\omega}{d}\le (e(d+\omega)/d)^{d}$，其中 $d\le p^{2}$ 是常数（$p$ 固定），$\omega\le n$，故 $D\le n\cdot(\text{常数})^{p^{2}}\cdot n^{p^{2}}=n^{O(p^{2})}$。$\square$

**注 B.5.1（$p$ 固定时 $D$ 是多项式）.** $D=n^{O(p^{2})}$ 的指数含 $p^{2}$，但 $p$ 固定，故 $D$ 是 $n$ 的多项式。这正是本文"固定 $p$"的含义；若 $p$ 随 $n$ 增长，$D$ 不再是多项式。

**B.5.2 结式的比特长（供第 4 节的充分判据使用）.** 第 4 节的"结式判据"用一对 $\omega$ 次 $\lambda$-多项式的结式作为"生成好"的**充分**条件。它的比特长也是 $\mathrm{poly}(n,\tau)$：结式是 $2\omega$ 阶 Sylvester 矩阵的行列式，元素是 $X$ 的多项式（次数 $\le\omega$、系数高度 $\le H$）；由 Hadamard 界，
$$\beta(\operatorname{Res})\le 2\omega\bigl(\tfrac12\log_2(2\omega)+\beta_{\min}\bigr),$$
其中 $\beta_{\min}$ 是 Sylvester 元素（作为 $X$ 的多项式系数）的比特长。于是"某个结式不恒为零"这个判据的验证代价与 B.5 (6) 同量级。**注意**：结式判据只是充分的；它的否定不构成"全坏"的证书（见第 4 节的反例）。

---

## B.6 汇总与依赖

| 条目 | 量 | 界 | 依据 |
|---|---|---|---|
| B.1 | $\beta(N)$ | $2\bigl(\tfrac{\rho}{2}\log_2\rho+\rho\beta_W\bigr)$ | Bareiss + Hadamard |
| B.2 | $\beta(M)$ | $\mathrm{poly}(n,\tau)$（推论 B.2.1） | 伴随矩阵 + $\det\ge1$ |
| B.3 | $\beta(\chi_M)$ | $\mathrm{poly}(n,\tau)$ | 主子式之和 |
| B.4 | $h(\mu)$、$[K:\mathbb Q]$ | $\le\beta(\chi_M)+O(\log k)$、$\le n$ | Cauchy 界 |
| B.5 | $\beta(\text{特征向量与基})$ | $\mathrm{poly}(n,\tau)$ | Cramer + (S3) |
| B.6 | $d_{\mathrm{chart}}$、子式数、图卡数、$D$ | $\le p^{2}$、$n^{O(p)}$、$\le2^{2p}$、$n^{O(p^{2})}$ | 组合计数 |

**标准事实（引用，不在本文证明）：**

- **(S1)** 整系数多项式分解（LLL 型），$\mathrm{poly}(N,\beta)$ 位。
- **(S2)** 实根隔离，$\mathrm{poly}(N,\beta)$ 位。
- **(S3)** 代数数域 $K=\mathbb Q[\mu]/(f)$ 的算术：加减乘求逆是 $\mathrm{poly}(d,h)$ 位，零判定精确。
- **(S4)** 子结式：给出分式域上 gcd 的本原部分，中间量是 Sylvester 子矩阵的行列式，比特长受输入次数与高度的多项式控制。

**本附录自己算的：**

- 清分母与 Bareiss 的具体比特长（B.1）；
- $\det(N^{\mathsf T}N)\ge1$ 及其对逆矩阵分子分母的控制（B.2）；
- $\chi_M$ 系数与根高度的显式界（B.3）；
- 特征向量与纤维基在 $K$ 上的比特长（B.4）；
- 图卡规模与稠密规模 $D$ 的计数（B.5）。

**未声称的：** 本附录不给最优常数，也不给"$K$ 上算术"的最优位复杂度；这两者都不影响第 5 节定理的形状。

**B.6.1 与第 5 节的对应表.**

| 第 5 节 | 用到的本附录条目 |
|---|---|
| 引理 5.1（压缩高度） | 引理 B.1、引理 B.2、推论 B.2.1 |
| 引理 5.2（特征多项式高度） | 引理 B.3 |
| 引理 5.3（根高度与次数） | 引理 B.4、推论 B.4.1、注 B.4.2 |
| 引理 5.4（特征向量与纤维基） | 引理 B.5、注 B.4.1、注 B.4.2、B.4.3 |
| 引理 5.5（图卡规模） | 引理 B.6、注 B.5.1 |
| 引理 5.6、5.7（子结式与多多项式 gcd） | 第 5.6 节（标准事实 (S4)）；本附录 B.5.1 补结式的比特长 |
| 定理 5.1 | 以上全部 |

**B.6.2 界之间的关系.** 文中的界按如下顺序逐层建立，后一层用前一层：

$$\beta(\widehat W)\ \longrightarrow\ \beta(N)\ \longrightarrow\ \beta(N^{\mathsf T}N),\ \beta(N^{\mathsf T}AN)\ \longrightarrow\ \beta(M)\ \longrightarrow\ \beta(\chi_M)\ \longrightarrow\ h(\mu),\ [K:\mathbb Q]\ \longrightarrow\ \beta(\text{特征向量与基}).$$

每一层的界都只依赖前一层与输入参数 $(n,p,\tau)$，没有循环。这是本附录可以独立核对的原因。

# 附录 C 子结式与多多项式 gcd 的复杂度

本附录补上第 5 节引理 5.6 与 5.7 的细节：为什么"在 $K(X)[\lambda]$ 上直接做欧几里得"不构成多项式时间算法，子结式链为什么是无分数的，以及多多项式情形为什么仍然只有多项式代价。全篇记号与第 2、4、5 节一致：$K$ 是数域（$\mathbb Q(\mu)$），$X=(X_1,\dots,X_d)$ 是图卡参数，$m_1,\dots,m_\ell\in K[X][\lambda]$ 是极大子式，$\deg_\lambda\le\omega$，$X$-次数 $\le\omega$，系数高度 $\le H$。

本附录只讨论"如何算出 gcd 以及它的代价"，**不**讨论"gcd 的次数为正为什么能判整张图表坏"——后者是第 4 节引理 4.6 的内容，本附录 C.5 只作提醒。

---

## C.1 朴素欧几里得为什么不行

在 $K[X][\lambda]$ 上直接做带余除法是**错误**的做法：除法的商落在 $K(X)[\lambda]$ 中，于是从第二步起，被除的对象就已经是有理函数，而不是多项式。每一步都会把除数的首项系数"乘进分母"，而下一次除法又要对它取倒数——**分母的次数在每一步都可能翻倍**。

### C.1.1 一个具体例子

取 $K=\mathbb Q$、单参数 $X$：

$$f=\lambda^{3}+X,\qquad g=\lambda^{2}+X\lambda+1 .$$

两者在 $\mathbb Q(X)[\lambda]$ 上互素（见下），我们照样把欧几里得跑完。

**第一步**：$\deg f=3>\deg g=2$。商的最高项 $\dfrac{\lambda^{3}}{\lambda^{2}}=\lambda$，于是

$$q_1=\lambda-X,\qquad r_1=f-q_1g=\lambda^{3}+X-(\lambda-X)(\lambda^{2}+X\lambda+1)=(X^{2}-1)\lambda+2X .$$

这一步没有任何分母：$r_1\in\mathbb Q[X][\lambda]$。

**第二步**：用 $r_1$（$\lambda$-次数 1）除 $g$（$\lambda$-次数 2）。商的最高项

$$\frac{\lambda^{2}}{(X^{2}-1)\lambda}=\frac{\lambda}{X^{2}-1},$$

它已经是**有理函数**；除完整个 $g$ 之后，

$$r_2=g-q_2r_1=\frac{-X^{4}+4X^{2}+1}{(X^{2}-1)^{2}},\qquad q_2=\frac{\lambda}{X^{2}-1}+\frac{X^{3}-3X}{(X^{2}-1)^{2}} .$$

$r_2$ 是非零常数（对 $\lambda$ 而言），故 $\gcd(f,g)=1$。

注意两件事：

1. 分母从**没有**（第一步）跳到 $(X^{2}-1)^{2}$（次数 4）——一步之内就出现了；
2. 分子的 $-X^{4}+4X^{2}+1$ 恰好是结式 $\operatorname{Res}_\lambda(f,g)$；这不是巧合，见 C.2。

### C.1.2 观察

| 步 | 商 | 余式 | 分母次数 |
|---|---|---|---|
| 1 | $\lambda-X$ | $(X^{2}-1)\lambda+2X$ | 0 |
| 2 | $\dfrac{\lambda}{X^{2}-1}+\dfrac{X^{3}-3X}{(X^{2}-1)^{2}}$ | $\dfrac{-X^{4}+4X^{2}+1}{(X^{2}-1)^{2}}$ | 4 |

**增长机制.** 第 $i$ 步的商里含 $\dfrac{1}{\operatorname{lc}_\lambda(r_{i-1})}$，而 $\operatorname{lc}_\lambda(r_{i-1})$ 本身是上一步留下的有理函数。于是分母的次数按**乘积**累积：若每步的首项系数都带分母，$\omega$ 步之后分母的次数可达 $2^{\Omega(\omega)}$ 量级。由于 $\omega\le n$，这已经是输入规模的指数，**不是**多项式界。

再给一个更小的例子作对照：$f=\lambda^{2}+1$、$g=X\lambda^{2}+X\lambda+1$ 时，第一步的余式就是 $-\lambda+\dfrac{X-1}{X}$（分母 $X$），第二步得到常数 $\dfrac{2X^{2}-2X+1}{X}$，其分子同样是结式 $2X^{2}-2X+1$。

结论：在 $K(X)[\lambda]$ 上直接做欧几里得，即使 $d$ 与 $\omega$ 都固定，其系数规模也不能被 $\mathrm{poly}(n,\tau)$ 界定。第 5 节的复杂度定理不能建立在它上面。

---

## C.2 子结式链

正确的工具是**子结式**（subresultant）。它的全部优点来自一个事实：子结式是**行列式**，而行列式是多项式环内的运算，不产生分母。

### C.2.1 定义

设 $f,g\in K[X][\lambda]$，$\deg_\lambda f=m$，$\deg_\lambda g=n$，$m,n\ge1$。把 $f$ 的系数写成 $\lambda$ 的降幂：$f=\sum_{i=0}^{m}f_i\lambda^{m-i}$，$g=\sum_{i=0}^{n}g_i\lambda^{n-i}$，其中 $f_i,g_j\in K[X]$。

**Sylvester 矩阵** $\operatorname{Syl}(f,g)$ 是 $(m+n)\times(m+n)$ 的矩阵：上面 $n$ 行是 $f$ 的系数右移 $0,1,\dots,n-1$ 位（左端补零），下面 $m$ 行是 $g$ 的系数右移 $0,1,\dots,m-1$ 位。其行列式就是**结式** $\operatorname{Res}(f,g)$。

对 $0\le j< \min(m,n)$，**第 $j$ 个子结式** $S_j$ 定义为 $\operatorname{Syl}(f,g)$ 删去
- $f$ 块的最后 $j$ 行、
- $g$ 块的最后 $j$ 行、
- 最后 $2j$ 列

之后所剩的 $(m+n-2j)\times(m+n-2j)$ 子矩阵的行列式。于是 $S_0=\operatorname{Res}(f,g)$。

### C.2.2 三条性质

**性质 1（无分母）.** 每个 $S_j$ 是 $K[X][\lambda]$ 的元素：它是 $K[X]$ 中元素的行列式。特别地 $S_j$ 是 $X$ 的**多项式**，不是有理函数。这是子结式相对欧几里得的关键优势。

**性质 2（次数）.** $\deg_\lambda S_j\le j$。

**性质 3（gcd 的次数）.** 设 $j^{*}=\max\{j:\ S_j\ne0\}$，则

$$\deg_\lambda\gcd_{K(X)[\lambda]}(f,g)=j^{*}.$$

等价地："$f,g$ 在 $K(X)[\lambda]$ 上互素" $\iff$ $S_0=\operatorname{Res}(f,g)\ne0$。当 $j^{*}\ge1$ 时，$S_{j^{*}}$ 的 $\lambda$-次数为 $j^{*}$，且在 $K(X)$ 内它与 gcd 只差一个非零因子——即 $S_{j^{*}}$ 与 gcd 相差一个 $K[X]$ 中的元素。对本文的判据（次数是否为零）只需 $\deg_\lambda$ 这一条。

### C.2.3 规模界

在本文的场合 $m,n\le\omega$，故：

1. Sylvester 矩阵至多 $(2\omega)\times(2\omega)$；
2. 其元素是 $f_i,g_j$，即 $X$-次数 $\le\omega$、高度 $\le\beta$ 的多项式；
3. 每个 $S_j$ 是 $(2\omega)\times(2\omega)$ 矩阵的行列式，由 Hadamard 界，其

$$X\text{-次数}\le 2\omega\cdot\omega=2\omega^{2},\qquad\text{系数高度}\le \mathrm{poly}(\omega,H);$$

4. 因此 $S_j$ 的稠密规模至多 $\binom{d+2\omega^{2}}{d}=O(\omega^{2d})$，对固定的 $d\le p^{2}$ 是 $n^{O(p^{2})}$，与第 5 节引理 5.6 的 $D=n^{O(p^{2})}$ 相容（那里用的是较松的 $X$-次数 $\omega$）。

**注 C.1.** 第 3 条里的 $2\omega^{2}$ 是对"单个子结式"的界。整个链只需算到第一个零为止，故链的长度 $\le\min(m,n)\le\omega$，不改变量级。

---

## C.3 多多项式情形

**命题 C.2（迭代）.** 设 $m_1,\dots,m_\ell\in K[X][\lambda]$。则

$$\gcd(m_1,\dots,m_\ell)=\gcd\bigl(\gcd(m_1,\dots,m_{\ell-1}),\,m_\ell\bigr),$$

且按下标顺序迭代，每一步的两个自变量都满足 C.2 的次数与高度界。

*证明.* gcd 的结合律；次数上 $\deg_\lambda\gcd(m_1,\dots,m_{\ell-1})\le\deg_\lambda m_1\le\omega$，$X$-次数与高度同理。$\square$

**命题 C.3（代价）.** 设 $\ell$ 个多项式的 $X$-次数 $\le\omega$、高度 $\le\beta$。则迭代算法在

$$\mathrm{poly}\bigl(\ell,\,D,\,\beta\bigr),\qquad D=\binom{d+2\omega^{2}}{d}$$

内算出 gcd；判据"次数为正"与"全部 $\ell$ 个同时有非常数公因子"一致。

*证明.* 共 $\ell-1$ 步；每步用 C.2 的子结式链，代价由 C.2.3 控制；每步之后 $X$-次数与高度不增。$\square$

**注 C.4（为什么"两两结式非零"不能代替全体 gcd）.** 若只检查两两结式，会漏掉"每一对都有公因子、但全体没有公共公因子"的情形。取

$$f_1=\lambda(\lambda-1),\qquad f_2=\lambda(\lambda-2),\qquad f_3=(\lambda-1)(\lambda-2).$$

两两的结式都为零（任意两个都有非常数公因子），但 $\gcd(f_1,f_2,f_3)=1$。所以**结式只能作单侧（充分）判据**：结式非零 ⟹ 互素；结式为零 ⟹ 不确定。第 4 节命题 4.11 用的是这一侧。

---

## C.4 与本文实现的关系

第 5 节的复杂度定理按**子结式链**计数（C.2、C.3）。本文的实现用的是另一条路径：把系数当作 $\mathbb Q(X)$ 上的有理函数，在 $\mathbb Q(X)[\lambda]$ 上做带余除法。对小规模实例（$\omega\le3$、$d\le4$）这是可行的，且实现里对分母做了规范化，所以不会触发 C.1 的爆炸。

两者算的是**同一个对象**——$K(X)[\lambda]$ 上的 gcd；判据"次数是否为零"是这个对象的不变量（去掉内容不影响它）。因此：**实现的输出可以作为正确性的证据，但复杂度的计数必须以 C.2 的子结式算法为准**。第 5 节引理 5.6、5.7 与定理 5.1 用的正是后者。

**注 C.5.** 若把实现直接用于大规模实例，代价会按 C.1 的方式增长；这不是定理的问题，而是实现选择的限制。

---

## C.5 "次数为正 ⟹ 整张图表坏"需要第 4 节

本附录只解决"怎么算 gcd、代价多少"。**从 gcd 到判定**还差一步：一般族上，"函数域上的 gcd 次数为正"**并不**推出"每个特化点都有公因子"（$m(X,\lambda)=X\lambda+1$ 在 $X=0$ 退化为常数 1）。

使这一步成立的是第 4 节引理 4.6：在**图表上** $\operatorname{rank}H\equiv\omega$ 成立，于是每个点至少有一个极大子式的 $\lambda$-次数恰为 $\omega$，从而去掉内容后的公因子不会在任何点退化为非零常数。因此：

$$\bigl(\text{gcd 次数}>0\bigr)\ \wedge\ \bigl(\operatorname{rank}H\equiv\omega\bigr)\ \Longrightarrow\ \text{该图表的每个点都坏}.$$

两件事——**算 gcd**（本附录）与**用 gcd 判整张图表**（第 4 节）——必须分开陈述。

---

## C.6 状态

| 条目 | 内容 | 状态 |
|---|---|---|
| C.1 | 朴素欧几里得的分母增长；具体例子 | 初等推导（本附录） |
| C.2.1 | Sylvester 矩阵与子结式 $S_j$ 的定义 | 标准（引用） |
| C.2.2 | 三条性质（无分母、$\deg\le j$、$\deg\gcd=\max\{j:S_j\ne0\}$） | 标准（引用） |
| C.2.3 | 规模界 $(2\omega)\times(2\omega)$、$X$-次数 $\le2\omega^{2}$、高度 $\mathrm{poly}(\omega,H)$ | 由 Hadamard 界推得（本附录） |
| C.3 | 多多项式迭代与代价 | 初等（本附录）；注 C.4 的单侧性为标准 |
| C.4 | 实现用有理函数欧几里得、定理按子结式计数 | 说明性 |
| C.5 | 判据需第 4 节引理 4.6 | 引用第 4 节 |

**引用来源.** C.2 的三条性质属于子结式理论的标准内容（Brown 的子结式 PRS、以及任意符号计算教材中"子结式链给出 gcd 的本原部分"一节）；本文不重新证明，只把它们写成与本文记号一致的形式，并补上本文需要的规模界（C.2.3）与多多项式版本（C.3）。

**本附录不声称的.** 具体常数、最优的位复杂度常数、以及"子结式链是实现该 gcd 的最优算法"——本文只需要"存在多项式时间的无分数算法"这一层面。

