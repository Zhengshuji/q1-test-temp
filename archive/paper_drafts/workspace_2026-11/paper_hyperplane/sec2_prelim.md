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
