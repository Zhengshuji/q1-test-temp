# 677 引理 S 的证明：$U=I\cap\mathbb C[\lambda]_{<2d}$

> 2026-11-27。给出 675 的 Sylvester 秩引理的一般证明，从而完成 674 的一般 $d$ 猜想。
> 状态：**[已证-纸面]**。

## 定理（Sylvester 秩引理）

设 $f_1,\dots,f_m\in\mathbb C[\lambda]$，$\deg f_i\le d$，且**某个 $f_j$ 的次数恰为 $d$**。令 $g=\gcd(f_i)$，$e=\deg g$。定义
$$\Phi:\bigoplus_{i=1}^m\mathbb C[\lambda]_{<d}\longrightarrow\mathbb C[\lambda]_{<2d},\qquad
(g_i)\longmapsto\sum_i g_if_i .$$
则
$$\boxed{\operatorname{rank}\Phi=2d-e .}$$

## 证明

记 $I=(f_1,\dots,f_m)=(g)$，$U=\operatorname{im}\Phi$。显然 $U\subseteq I\cap\mathbb C[\lambda]_{<2d}$（每个 $g_if_i$ 次数 $\le(d-1)+d<2d$，且在 $I$ 中）。

**反向包含**：设 $h\in I$，$\deg h<2d$。写 $h=\sum a_if_i$（$a_i\in\mathbb C[\lambda]$）。取 $\deg f_j=d$，做带余除法
$$a_i=q_if_j+r_i,\qquad \deg r_i<d .$$
则
$$h=f_j\,s+\sum_i r_if_i,\qquad s:=\sum_i q_if_i\in I .$$
后一项次数 $<2d$；故 $f_js=h-\sum r_if_i$ 的次数 $<2d$。若 $s\ne0$，则
$$\deg s=\deg(f_js)-d<2d-d=d .$$
于是 $f_js=s\cdot f_j$ 是“系数 $s$（$\deg<d$）乘生成元 $f_j$”，属于 $U$；而 $\sum r_if_i\in U$（$\deg r_i<d$）。故 $h\in U$。

所以 $U=I\cap\mathbb C[\lambda]_{<2d}$，从而
$$\operatorname{rank}\Phi=\dim\big(I\cap\mathbb C[\lambda]_{<2d}\big)=\dim g\cdot\mathbb C[\lambda]_{<2d-e}=2d-e .\qquad\square$$

## 推论（一般 $d$ 的猜想成立）

若 $H$ 的秩为 $d$，则某个 $d$-子式 $f_j$ 的次数恰为 $d$（其首项系数是 $H$ 的非零 $d$-子式），故引理 S 适用：
$$\operatorname{rank}M(H)=2d-\deg\gcd(f_i).$$
于是
$$\boxed{(5b)\iff\gcd(f_i)=1\iff\operatorname{rank}M(H)=2d\iff D_d(H)\ne0 .}$$

特别地，$e_0\in\operatorname{col}M$ $\iff$ $\operatorname{rank}M=2d$（满秩时列空间为全空间；反之由上式）。

## 检验

- $d=1$：$M$ 为 $2\times m$，$2d-e=2$ 当 $e=0$ ✓；
- $d=2$：674 的定理是特例（此前用列分析证明，现由引理 S 统一推出）；
- 638：$\gcd=1$，$\operatorname{rank}M=4$ ✓；
- 641B：$\deg\gcd=2$，$\operatorname{rank}M=4-2=2$ ✓（与 668 一致）；
- 661：$m=1$、$f=\det P$ 次数 2、$e=2$，$\operatorname{rank}M=4-2=2<4$，$e_0\notin\operatorname{col}M$ ✓。

## 意义

1. **完成 674 的一般 $d$ 猜想**（不再需要逐 $d$ 分类）；
2. 可行性的“满秩判据”成立：
   $$\text{可行}\iff\exists H\ (\operatorname{rank}H=d):\ D_d(H)\ne0,$$
   即**开条件**；退化层只在 $\operatorname{rank}H<d$（实际最高次数 $<d$）时出现，递归到更低秩；
3. 665 的模板判据、663 的 $d=1$ 判据都是它的特例；
4. 统一路线的“局部秩判定”部分完成，剩下的正是 $\exists H$ 的代数/复杂度问题。

## 注意

- 引理 S 要求“某个 $f_j$ 次数恰为 $d$”；若 $H$ 秩 $<d$，需按实际最高次数 $d'$ 重设（此时用 $d'$ 代替 $d$）；
- 这与 676 的提醒一致。

## 状态

- 引理 S：**[已证-纸面]**；
- 674 一般 $d$ 猜想：**[已证-纸面]**（由引理 S）；
- 665/663/661 的一致性：**[已证-纸面]** + **[精确验证]**（668）。
