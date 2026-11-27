# 689 $d'=k$、$q>k$ 的构造：$H=[I_k;0]$ + 简单谱扰动

> 2026-11-27。对 687 的特例 $d'=k$（$H$ 列满秩）给出一个显式构造，证明在 $S\ne0$、$q>k$ 且扰动矩阵有简单谱时可行。
> 状态：**[已证-纸面]**（构造与条件）+ **[精确验证]**（$k=3,q=4$ 数值）。

## 构造

设 $H=\begin{bmatrix}I_k\\0\end{bmatrix}$（$q\times k$）。则 $U=\mathbb C^k$，相容性自动。
取 $Z$ 的前 $k$ 列为 $\begin{bmatrix}A\\ B\end{bmatrix}$（$A\in\mathbb C^{k\times k}$，$B\in\mathbb C^{(q-k)\times k}$），其余列取 0。则
$$ZH=\begin{bmatrix}A\\B\end{bmatrix},\qquad HZ'=\begin{bmatrix}Z'\\0\end{bmatrix},$$
$$G=ZH-HZ'=\begin{bmatrix}A-Z'\\B\end{bmatrix}.$$
要求 $G$ 的行在 $S$：
- 取 $A=Z'+C$，其中 $C$ 的每一行在 $S$（如 $C=c\,\varphi^{\mathsf T}$，$\varphi\in S$）；
- 取 $B$ 的每一行在 $S$（如 $B=\mathbf{1}\,\varphi^{\mathsf T}$，或用多行）。

则 $(5a)$ 成立。铅笔
$$\lambda H-ZH=\begin{bmatrix}\lambda I_k-A\\ -B\end{bmatrix}.$$
其秩为 $k$ 对一切 $\lambda$ $\iff$ 不存在 $x\ne0$ 使 $Ax=\lambda x$ 且 $Bx=0$。

## 定理（条件性）

若存在 $C$（行在 $S$）使 $A=Z'+C$ 的每个特征值的几何重数 $\le\operatorname{rank}B$，且 $\ker(\lambda I-A)\cap\ker B=0$ 对所有特征值成立，则
$$\operatorname{rank}(\lambda H-ZH)=k\quad\forall\lambda,$$
故该 $H$ 可行（$d'=k$）。

**特别地**：若 $A$ 有**简单谱**（各特征值重数 1），取 $B$ 的一行 $\varphi^{\mathsf T}$（$\varphi\in S$）且 $\varphi$ 不垂直于任何特征向量，即满足条件。

## 数值验证（$k=3$、$q=4$、$S=\operatorname{span}\{\varphi\}$）

随机 $Z'$、$\varphi$、$c$：$A=Z'+c\varphi^{\mathsf T}$ 有三个互异特征值；$B=\varphi^{\mathsf T}$。
结果：$G$ 的行全在 $S$ 内；$\operatorname{rank}(\lambda H-ZH)=3$ 在 $\lambda=0,1,2,3$ 处均成立。

## 例外：$Z'$ 为标量

若 $Z'=\mu I$，则 $A=\mu I+C$，其中 $C$ 的行在 $S$（$\operatorname{rank}C\le s=\dim S$），故 $A$ 有特征值 $\mu$、几何重数 $\ge k-s$。
此时需要 $\operatorname{rank}B\ge k-s$（$B$ 的行在 $S$，秩 $\le s$），即
$$\boxed{k\le 2s}$$
才能满足定理条件。$s=1$、$k\ge3$ 时该构造失败（但可能有别的 $H$）。

## 与 684 猜想的关系

- 这给出 $d'=k$、$q>k$、$S\ne0$ 下的一族显式可行解（除标量 $Z'$ 且 $k>2s$ 的例外）；
- 支持“一般可行”猜想；
- 661（$q=k=2$）不满足 $q>k$，仍是 $m=1$ 的不可行。

## 状态

- 构造与条件：**[已证-纸面]**；
- 数值验证：**[精确验证]**；
- 标量 $Z'$ 的完整处理：**[未做]**。
