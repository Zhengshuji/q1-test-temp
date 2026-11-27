# 347 富余档：从"18/27 采样"到**该实例的定理**（Bézout 证书 + 两条一般定理）

> 承接 341（富余档可以好，18/27）。本轮把其中一个好点做成**显式有理点 + Bézout 证书**，
> 再用"坏集闭 + 参数族不可约"把它升级为**定理**；同时更正 340/341 里一处措辞错误。

## 目标

1. 拿到一个**有理好点的精确证书**（Bézout 恒等式，不是采样）。
2. 用两条一般定理把它升级为"该实例的富余档生成可行"。
3. 更正 340/341 的"$A K_0\subseteq K_0$"措辞。

## 设想与理由

两条一般事实：

**Theorem 1（无约束高铅笔的生成性）.** 设 $U$ 为 $\omega$ 维，$W\subseteq U\oplus U$ 是 $d=\omega+s$ 维（$s\ge1$）、
两个坐标投影都满射。则满足 $\operatorname{rank}(\lambda\pi_1-\pi_2)|_W=\omega\ \forall\lambda$ 的 $W$ 构成
$\mathfrak G$ 的**非空 Zariski 开稠密集**。

*证明.* 入射簇 $\mathcal I=\{(W,[a:b]):\operatorname{rank}((a\pi_1-b\pi_2)|_W)<\omega\}$；
对固定 $[a:b]$，$(a\pi_1-b\pi_2)$ 满射，限制到一般 $d$ 维子空间的秩降条件余维为 $d-\omega+1=s+1$；
$\mathbb P^1$ 一维 ⟹ $\dim\mathcal I\le\dim\mathfrak G-s<\dim\mathfrak G$；投影紧合 ⟹ 坏集真闭。$\square$

**Theorem 2（一个好点 ⟹ 生成好）.** 设 $X$ 不可约、坏集 $\mathcal B$ 在 $X$ 中闭（97 号 §4 的证明），
且 $X$ 上 $\operatorname{rank}H\equiv\omega$。若存在**一个**点 $x_*\in X$ 使 $(5b)$ 成立，则
$X\setminus\mathcal B$ 是**非空开稠密**子集。

*证明.* $\mathcal B$ 真闭 ⟹ 补非空；$X$ 不可约 ⟹ 非空开集稠密。$\square$

## 做法

对 341 的实例（$n=8,p=2$、$C=[e_1;e_2]$、$A$ 前两行 $=e_3,e_4$）：

- $\operatorname{rank}[C;CA]=4$、$k=4$、$\omega=3$、$n-2-p=4>3$（富余档 ✓）；
- $v=N e_1$ 非特征（$\dim U=2$ ✓）；
- 在 $U^\perp$ 里取超平面，法向坐标 $(-2,-2,-1,-1,-1,-1)$；
- 铅笔 $4\times4$，四条 $3\times3$ 极大子式，$\gcd=1$；
- **Bézout 证书**：找到 $g_i$（$\deg g_i\le2<3$）使 $\sum_i g_i f_i=1$，**精确核对通过**。

见 [c347](../../../../tools/verification/c347_bezout_certificate.py)（输出：证书成立、$H$、$H_A$ 全为有理数）。

## 进展

1. **该实例现在是定理**：由一个精确好点 + Theorem 2 + 层的参数族
   （$\{V\subseteq U^\perp:\dim V=q,\ \dim(V\cap K_0)=\omega\}$ 是 Schubert 型不可约簇的开集）⟹
   **好点构成非空 Zariski 开稠密集**，即"富余档**生成**可行"。
2. **Theorem 1 说明了为什么富余档该好**：多出的一行（$s=d-\omega\ge1$）正是让坏入射簇降维的原因。
3. **仍开放**：$\rho>p+1\Rightarrow$ 生成好——需要"结构族不落在坏铅笔簇内"的非包含论证
   （97 号 §7 的表格里也是这一格）。

## 更正：340/341 的措辞

原文说 340 的退化族"$A K_0\subseteq K_0$"。**这是错的**：该构造里 $A e_5=(0,0,\alpha,\beta,\mu,0,0,0)\notin K_0$
（当 $\alpha,\beta\ne0$）。正确的说法是
$$\operatorname{proj}_{K_0}\circ A|_{K_0}=B ,$$
即**$A$ 在 $K_0$ 上的压缩是 $B$**——这才使 $K_0\cap v^\perp$ 里的行满足 $H_A=HB$，从而带出 $(\lambda I-B)$ 因子。

**但这条也不足以解释 340 与 341 的差别**：两种构造的压缩**都是 $B$**（第 3、4 行只改 $K_0^\perp$ 分量），
而结论是 0/23 与 18/27。差别的真实来源（$B$ 的取法？$x$ 的取法？）**未查明**，这里如实记录。

**另一点（专家指出，正确）**：若 $Av\in K_0$ 且 $v,Av$ 独立，则 $U_v\subseteq K_0$，
于是 $\dim(U_v^\perp\cap K_0)=k-2$，**不能**给出 $\operatorname{rank}H=k-1$ 的可容许点（在满行空间档）。
所以"$Av\in K_0$ 的非特征 $v$"本身就不是可容许的核方向——这与我们的实例一致（$Av\notin K_0$）。

## 最终结论

1. **富余档"生成可行"对一个具体实例成立**（证书 + Theorem 2），不再是 18/27 的采样。
2. **一般情形（$\rho>p+1\Rightarrow$ 生成好）仍开放**；Theorem 1 只解决"无约束"那一半。
3. 340/341 的退化机制措辞已更正为"压缩 $=B$"，并附上专家的相容性观察。

## 放弃原因

- 没有证明一般 $\rho>p+1$ 的非包含；
- 只有**一个**实例的证书（可复制到其它实例，但不是定理）；
- 没有把 Bézout 证书接进 345 的网格判定流程（应当可以：证书就是第二级的见证）。

## 残留价值

- 一个可复跑的证书生成器（[c347](../../../../tools/verification/c347_bezout_certificate.py)）；
- 两条一般定理（Theorem 1 无约束、Theorem 2 结构化）与它们的适用范围；
- 一处措辞错误的更正，以及"$Av\in K_0$ 不可容许"这条一致性检查。

## 相关文件

- [attempts/341](../../decision_algorithms/attempts/341_excess_regime_correction.md)（18/27）
- [attempts/340](340_excess_realization_result.md)（被更正的措辞）
- [attempts/342](../../decision_algorithms/attempts/342_expert97_audit.md)（97 号：缺非包含）
- [attempts/346](346_left_factor_incidence.md)（左因子形式）
- [c347](../../../../tools/verification/c347_bezout_certificate.py)

## 状态

- 实例的"生成可行"：**[已证-纸面]**（Theorem 2 + 精确证书）。
- Theorem 1（无约束）：**[已证-纸面]**（专家证明）。
- Theorem 2（一个好点 ⟹ 生成好）：**[已证-纸面]**。
- 一般 $\rho>p+1$：**[未证]**。
