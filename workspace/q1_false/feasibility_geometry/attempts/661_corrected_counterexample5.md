# 661 修正 ChatGPT 的反例 5：$H_0=e_2^{\mathsf T}$ 的实例级不可行
> **更正（685）**：该实例只是 **$q=2=r_0+1$ 不可行**；$q=3$ 时存在可行点（$H=[[0,1],[-1,0],[-2,1]]$，$G$ 行在 $e_1$，$U=\mathbb C^2$），故 $q_{\min}=3$，**不是实例级不可行**。
> **更正（697/726）**：其数据 $N=I_2$ ⇒ $T=\{lW:lN=0\}=0$，故 $G=0$ 被强制、$H_A=HZ'$，$P=H(\lambda I-Z')$ 在 $\sigma(Z')$ 处降秩 ⇒ **661 对 $d>0$ 不可行**；$q=3$ 的旧构造不满足 $(5a)$（$G$ 不能任意取 $e_1$ 方向）。$\omega>s$ 不能由 661 支持。



> 2026-11-27。ChatGPT 的“反例 5”用 $H_0=e_1^{\mathsf T}$，但该数据下 $T_\infty=\operatorname{span}\{e_1\}$，
> $H_0$ 在 $T_\infty$ 上不为零，**违反 651**。改用 $H_0=e_2^{\mathsf T}$ 后，得到真正的实例级不可行例子（$r_0=1$，有一个自由行）。
> 状态：**[已证-纸面]**。

## 数据

$k=q=2$、$r_0=1$、$N=I_2$、$C=0$、$Z'=\begin{bmatrix}0&1\\0&0\end{bmatrix}$、$W=\begin{bmatrix}1&0\\0&0\end{bmatrix}$，
$$A=Z'+W=\begin{bmatrix}1&1\\0&0\end{bmatrix},\qquad S=\operatorname{row}(W)=\operatorname{span}\{e_1\},\qquad K=S^\perp=\operatorname{span}\{e_2\}.$$
固定行 $H_0=e_2^{\mathsf T}$（$L_0=(0,1)$）。

## $T_\infty$

$Z'e_1=0$，$Z'e_2=e_1$；$K=\operatorname{span}\{e_2\}$，$Z'(K)=\operatorname{span}\{e_1\}$。
$$T_0=K_\infty=K\cap(Z')^{-1}K=\operatorname{span}\{e_2\}\cap\{x:Z'x\in\operatorname{span}\{e_2\}\}=\{0\}\ (\text{因 }Z'e_2=e_1\notin K),$$
$$T_1=T_0+Z'(T_0\cap K)=0,\qquad T_\infty=0,\qquad d=2 .$$

## 651 条件

$H_0|_{T_\infty}=0$（$T_\infty=0$）✓；$\operatorname{rank}H_0=1\le2$ ✓。**条件全满足。**

## 排除所有 $H$

- **$d=0$**：$H=0$ 与 $H_0\ne0$ 矛盾；
- **$d=1$**：$T_\infty=0$ 不给核约束；但 $\operatorname{row}(H_0)=\operatorname{span}\{e_2\}\subseteq\operatorname{row}H$ 且 $\operatorname{rank}H=1$ ⇒ $H=u e_2^{\mathsf T}$（首行 $e_2^{\mathsf T}$ 迫使 $u_1=1$）。
  则 $HZ'=u\,(e_2^{\mathsf T}Z')=u\cdot(0,0)=0$，故 $G=ZH=Z u\,e_2^{\mathsf T}$。$G$ 的行在 $S=\operatorname{span}\{e_1\}$ ⇒ 每行 $\propto e_1^{\mathsf T}$；但 $e_2^{\mathsf T}\notin\operatorname{span}\{e_1^{\mathsf T}\}$ ⇒ $Zu=0$。
  于是 $P(\lambda)=\lambda u e_2^{\mathsf T}-0$，在 $\lambda=0$ 处秩 0 $<1$ ⇒ 失败；
- **$d=2=q$**：秩等于行数的障碍（518/659）：$H$ 可逆 ⇒ $H_A=ZH$ ⇒ $P=(\lambda I_2-Z)H$，$\operatorname{rank}P=\operatorname{rank}(\lambda I_2-Z)$，而 $2\times2$ 复矩阵必有特征值 ⇒ 某 $\lambda$ 掉秩 ⇒ 失败。

三种秩全部排除 ⇒ **实例不可行**。

## 与 ChatGPT 版本的区别

- 它取 $H_0=e_1^{\mathsf T}$：此时 $H_0e_1=1\ne0$，违反 651（$H_0|_{T_\infty}=0$），所以不能作为“满足 651 的反例”；
- 改用 $H_0=e_2^{\mathsf T}$ 后，651 条件全满足，且证明完整。

## 意义

- 这是第一个**满足 651 全部必要条件**、且有自由行（$q-r_0=1$）的实例级不可行例子；
- 不可行性同时来自两层：秩 1 的 $G$ 行约束逼 $Zu=0$；秩 2 的特征值障碍；
- 说明 651 的条件确实不充分，且不可行性可以发生在很小的实例上。

## 状态

- 修正后的反例：**[已证-纸面]**；
- ChatGPT 的原版反例：**不满足 651**（已指出）。
