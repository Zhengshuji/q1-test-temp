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
