# 520 首个 sound 乘法 gadget（单向）：$q=3$、$n=5$，可行 $\Rightarrow z=xy$

> 2026-11-27。在 519 的压缩门上完成落地：找到显式 $n=5$、$p=1$、$q=3$ 的观测器数据。
> **修正（见 [526](526_lean_correction.md)）**：$(5a)$ 恒成立、$(5b)$ 在门上成立当且仅当 $2x+1\ne0$，
> 因此 **可行 $\iff z=xy$ 且 $x\ne-1/2$**——单向 sound，坏超平面 $x=-1/2$ 上完备性失败。
> 状态：**[已证-纸面]** + **[Lean]**（代数核心）+ **[精确验证]**。

## 数据

$n=5$、$C=e_5^{\mathsf T}$、
$$A=\begin{bmatrix}
-2&0&0&0&0\\
0&-2&0&0&0\\
0&0&2&0&0\\
2y&2&-2&0&0\\
0&0&0&1&0
\end{bmatrix},\qquad
L_0=\begin{bmatrix}
z&x&0&-1&0\\
y&1&0&2&0\\
0&0&1&2&0
\end{bmatrix}.$$
（$Ae_5=e_4$ ⇒ $CA=e_4^{\mathsf T}$，$K_0=\ker[C;CA]=\operatorname{span}(e_1,e_2,e_3)$，$k=3$；
$A(K_0)\not\subseteq K_0$，$E$ 的第 4 行为 $(2y,2,-2)$。）

压缩：$N=I_3$、$H_0=L_0N$、$H_{A,0}=L_0AN$，其中
$$H_0=\begin{bmatrix}z&x&0\\y&1&0\\0&0&1\end{bmatrix},\qquad
H_{A,0}=\begin{bmatrix}-2(x+1)y&-2(x+1)&2\\2y&2&-4\\4y&4&-2\end{bmatrix}.$$

## $(5a)$ 恒成立

- $z\ne xy$：$\det H_0=z-xy\ne0$，$\operatorname{row}H_0=\mathbb C^3$，行包含自动成立；
- $z=xy$：$h_1=(xy,x,0)=x h_2$，故 $\operatorname{row}H_0=\operatorname{span}\{h_2,h_3\}$；而
  $$H_{A,0}\ \text{的三行}= -2(x+1)h_2+2h_3,\quad 2h_2-4h_3,\quad 4h_2-2h_3,$$
  都在 $\operatorname{span}\{h_2,h_3\}$ 里。$\square$

## $(5b)\iff z=xy$

**$z\ne xy$**：$\operatorname{rank}H_0=3=\omega$，$(5a)$ 给 $H_{A,0}=ZH_0$（$Z$ 为 $3\times3$），
$$P(\lambda)=(\lambda I_3-Z)H_0,\qquad \operatorname{rank}P(\lambda)=\operatorname{rank}(\lambda I_3-Z).$$
$\det(\lambda I_3-Z)$ 是首一三次多项式，在 $\mathbb C$ 上有根，故某个 $\lambda$ 处 $\operatorname{rank}P<3$，$(5b)$ 失败。

**$z=xy$**：$\omega=2$，精确计算 $\lambda H_0-H_{A,0}$ 的全部 $2\times2$ 子式：
$$M_1=\lambda^2+12,\quad M_2=x\lambda^2+4x\lambda+2\lambda+4x-4,\quad M_3=M_2\cdot(\text{其它因子}),$$
$$\operatorname{Res}_\lambda(M_1,M_2)=64(2x+1)^2 .$$
故 $\gcd=1\iff 2x+1\ne0$；(5b) 在门上成立 $\iff x\ne-1/2$。在 $x=-1/2$、$\lambda=\pm2\sqrt3 i$ 处
$M_1=M_2=0$，$(5b)$ 失败。（[526](526_lean_correction.md) 的 Lean 文件核验了
$M_2-xM_1=2(2x+1)(\lambda-2)$，并给出该退化点。）$\square$

## 原始矩阵核验（$n=5$）

| 点 | $\operatorname{rank}[L;CA;C]$ | $\operatorname{rank}[LA;L;CA;C]$ | $\lambda=0,1,2,3$ 处 $\operatorname{rank}[\lambda L-LA;CA;C]$ | $\det$ |
|---|---|---|---|---|
| $(2,3,6)$（门） | 4 | 4 | 4,4,4,4 | $0$ |
| $(2,3,7)$（门外） | 5 | 5 | 5,5,5,5 | $(\lambda+2)(\lambda^2+12)$ |
| $(0,3,0)$（门） | 4 | 4 | 4,4,4,4 | $0$ |
| $(0,3,5)$（门外） | 5 | 5 | 5,5,5,5 | $5(\lambda+2)(\lambda^2+12)$ |

门外点 $\det$ 有根（$\lambda=-2,\ \pm2\sqrt3 i$）⇒ $(5b)$ 失败；门内 $\det\equiv0$ 但秩恒 4（由压缩 gcd=1）。

脚本：[520b_verify.py](520b_verify.py)（压缩层 gcd）、[520c_original_check.py](520c_original_check.py)（原始矩阵）。

## 意义

- **第一个（单向）sound 乘法 gadget**：$(5a)$ 恒成立、$(5b)$ 在门上等价于 $x\ne-1/2$；
  即“可行 $\Rightarrow z=xy$”，坏超平面 $x=-1/2$ 上完备性失败（见 [526](526_lean_correction.md)）；
- 关键是把门放进 $(5b)$（$\omega=2<q=3$），而不是 $(5a)$——518 的 $\omega=q$ 障碍被绕开；
- 变量 $x,y,z$ 是 $A$ 与 $L_0$ 的条目（输入控制），不存在 $R=0$ 置零问题（$q=r_0$）。

## 下一步

1. 检查这个 gadget 能否与 296 的非零门、303 C 的输入控制门组合（wiring/equality）；
2. 检查 gadget 的“输入”是 $A,L_0$ 的条目——归约里如何把目标变量写进去（编码规模、$x,y,z$ 的取值范围）；
3. 若组合通过，进入 $\exists\mathbb R$-hardness 的归约骨架。

## 状态

- $(5a)$ 恒成立：**[已证-纸面]**；
- $(5b)$ 门上 $\iff x\ne-1/2$：**[已证-纸面]**（resultant $64(2x+1)^2$）+ **[Lean]**（$M_2-xM_1$ 恒等式）+ **[精确验证]**（反例 $(-1/2,2,-1)$）；
- 双向等价/归约：**[未完成]**（须避开坏超平面）。
