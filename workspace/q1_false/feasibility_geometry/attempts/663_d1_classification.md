# 663 仿射铅笔 $d=1$ 的完整分类

> 2026-11-27。按 662 的优先级，完成 $d=1$（秩一）的仿射铅笔 gcd 分类：给出充要条件并解释 629/631/638/657/661。
> 状态：**[已证-纸面]**。

## 设定

$H=u v^{\mathsf T}$（$u\in\mathbb C^q\setminus0$、$v\in\mathbb C^k\setminus0$），$H_A=ZH$，$G=ZH-HZ'$。
$K=S^\perp$。条件：
$$(i)\ Gx=0\ \forall x\in K;\qquad (ii)\ \operatorname{rank}P(\lambda)=1\ \forall\lambda,\quad P(\lambda)=(\lambda u-Zu)v^{\mathsf T}.$$

## 情形 A：$v|_K\ne0$（不可行）

取 $x_0\in K$ 使 $v\cdot x_0=1$。$(i)$ 对 $x\in K$：
$$(v\cdot x)\,Zu=(Z'^{\mathsf T}v\cdot x)\,u .$$
取 $x=x_0$ 得 $Zu=(Z'^{\mathsf T}v\cdot x_0)u$，即 $Zu=\mu u$；对 $x\in\ker(v|_K)$ 得 $Z'^{\mathsf T}v$ 在该子空间上为零，故 $Z'^{\mathsf T}v|_K=\mu v|_K$。
于是
$$P(\lambda)=(\lambda-\mu)\,u v^{\mathsf T},$$
在 $\lambda=\mu$ 处 $P=0$，$\operatorname{rank}0<1$ ⇒ 失败。

## 情形 B：$v|_K=0$（可行条件）

$v|_K=0\iff v\in K^{\perp}=S$。$(i)$ 化为 $Z'^{\mathsf T}v\cdot x=0\ \forall x\in K\iff Z'^{\mathsf T}v\in S$。
所以需要
$$\boxed{v\in E:=S\cap(Z'^{\mathsf T})^{-1}S,\quad v\ne0 .}$$
此时 $G=Zu\,v^{\mathsf T}-u(Z'^{\mathsf T}v)^{\mathsf T}$ 满足 $(i)$，且
$$P(\lambda)=(\lambda u-Zu)v^{\mathsf T},\qquad
\operatorname{rank}P(\lambda)=1\ \forall\lambda\iff \lambda u-Zu\ne0\ \forall\lambda .$$
后者 $\iff$ $u$ 不是 $Z$ 的特征向量（若 $Zu=0$ 则 $\lambda=0$ 为零；若 $Zu=\mu u$ 则 $\lambda=\mu$ 为零）。

**存在性**：$q\ge2$ 时可取 $w\notin\operatorname{span}\{u\}$、令 $Zu=w$ 并线性延拓，得 $u$ 非特征向量。
$q=1$ 时 $Z$ 是标量，必有特征值 ⇒ 不可行。

## 定理（$r_0=0$ 的完整版）

$q\ge2$ 时，秩一可行 $\iff$ $E\ne0$；且可行解可显式构造。

## $r_0\ge1$ 的附加约束

$H$ 的前 $r_0$ 行必须等于 $H_0$：$H$ 的第 $i$ 行 $=u_i v^{\mathsf T}$，故
$$\operatorname{row}(H_0)\subseteq\operatorname{span}\{v\};$$
且 $ZH$ 的前 $r_0$ 行必须等于固定的 $H_{A,0}=L_0AN$，即
$$(Zu)_i\,v^{\mathsf T}=H_{A,0}\ \text{的第 }i\text{ 行}\quad(i\le r_0).$$
这两条把 $u_{1..r_0}$ 与 $Z$ 的部分行钉住；最后仍需 $\lambda u-Zu\ne0\ \forall\lambda$。

## 检验

| 实例 | $S$ | $E$ | 结论 |
|---|---|---|---|
| 629（$W=0$） | 0 | 0 | 无秩一 ⇒ 只有 $\omega=0$ ✓ |
| 631（$W$ 满行秩） | $\mathbb C^k$ | $\mathbb C^k$ | 秩一可行 ✓ |
| 638 | $\operatorname{span}\{e_2\}$ | 0 | 秩一不可行；但 $d=2$ 可行（$\omega>s$ 反例）✓ |
| 657（$k=2$，$Z'$ 使 $Z'^{\mathsf T}v\in S$） | $\operatorname{span}\{e_1\}$ | $\operatorname{span}\{e_1\}$ | 秩一可行（$u=(1,0,1)$，$Z=e_3e_1^{\mathsf T}$）✓ |
| 661（$k=q=2$） | $\operatorname{span}\{e_1\}$ | 0（$Z'^{\mathsf T}v=(0,v_1)\in S\Rightarrow v_1=0$，与 $v\in S$ 矛盾） | 秩一不可行；$d=2=q$ 触发 518 障碍 ⇒ 实例不可行 ✓ |

## 意义

- $d=1$ 的仿射铅笔问题**完全解决**：$E=S\cap(Z'^{\mathsf T})^{-1}S$ 是唯一判据（外加 $H_0/H_{A,0}$ 的匹配）；
- 661 的不可行性被统一解释为“$E=0$ + 秩 $=q$ 障碍”，不再依赖逐层列约束技巧；
- 下一步：$d=2$ 的类似分类（$2\times2$ 子式族的 gcd 条件）。

## 状态

- $d=1$（$r_0=0$）：**[已证-纸面]**；
- $r_0\ge1$ 的附加约束：**[已证-纸面]**（写出，未逐例验证）；
- $d=2$：**[未做]**。
