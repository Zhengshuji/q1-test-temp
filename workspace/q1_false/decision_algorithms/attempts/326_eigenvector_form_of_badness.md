# 326 坏性的谱形式（**已更正**）：充分条件、行张成假设、以及"λ 随 v 移动"的三分

> 承接 325（Theorem C 归约到一个 PIT）与 94 号 Q2 的提示（"用不可观测特征向量入射簇重述"）。
> **更正**：初版把 $\mathbb C^n$ 与 $\mathbb C^k$（$K_0$ 的坐标）混用，写出了
> $(\lambda I-A)u\in\ker L_0\cap\operatorname{span}(v,Av)$ 的形式，并在证明里用了 $\ker L=\ker L_0\cap U$——
> **那是错的**（$Av$ 未必在 $K_0$ 内，$L_0$ 只是 $q$ 行中的一行）。下面是正确的形式与条件。

## 目标

把"$\operatorname{rank}P(\lambda)<\omega$"改写成关于 $A$ 与 $v$ 的**谱**条件，并说清需要什么假设才等价。

## 设想与理由

沿用 121 的记号：$S=\ker\sigma\subset K_0$ 是超平面，$v=N\sigma^{\mathsf T}$，自由行满足 $r_iN\in S$，即
$$r_iv=0,\qquad r_iAv=0 .$$
固定行满足同类条件（这正是 $v\in B$ 的定义）。于是

$$\text{所有行}\ r\ \text{都同时消去}\ v\ \text{与}\ Av\quad\Longrightarrow\quad \operatorname{row}L\subseteq U^\perp,\qquad U:=\operatorname{span}(v,Av).$$

其中 $U^\perp$ 是 $\mathbb C^n$ 里关于标准配对的**标准正交补**（行 $r$ 就是 $\mathbb C^n$ 的向量）。

而 $P(\lambda)=(\lambda L-LA)N$，故对 $w\in\mathbb C^k$、$u=Nw\in K_0$：
$$P(\lambda)w=0\iff L(\lambda I-A)u=0\iff(\lambda I-A)u\in\ker L,\qquad \ker L=(\operatorname{row}L)^\perp .$$

## 做法

### 引理（坏性的谱形式）

> **引理.** 设 $v\in B$、$U=\operatorname{span}(v,Av)$，并设**行空间张满** $U^\perp$（即 $\operatorname{row}L=U^\perp$；
> 若 $L$ 的行数 $q\ge n-\dim U$ 且取一般的行，这成立）。则对任意 $\lambda$：
> $$\operatorname{rank}P(\lambda)<\omega\iff\exists u\in K_0:\ u\notin\operatorname{span}(v)\ \text{且}\ (\lambda I-A)u\in U .$$

*证明.* $\operatorname{row}L=U^\perp\Rightarrow\ker L=U$。又 $\operatorname{rank}P(\lambda)<\omega=k-1\iff\dim\ker P(\lambda)\ge2\iff$
存在 $w\notin\ker H$ 使 $P(\lambda)w=0$；而 $\ker H=\operatorname{span}(v)$（$121$ 的超平面层），
$w\mapsto u=Nw$ 是 $K_0$ 上的同构。代入上式即得。$\square$

**只有一半时（$\operatorname{row}L\subsetneq U^\perp$）**：仍有 $\ker L\supseteq U$，引理给的是**充分**条件
（$(5a)$ 的两个约束保证所有行消去 $v,Av$，这一步不依赖张成）。

（更正说明：初版写作"$\ker L=\ker L_0\cap U$"，隐含了 $Av\in K_0$ 且 $L_0$ 决定 $\ker L$，两者都不成立。）

### 它给出什么

1. **坏性的 $(\lambda,u)$ 证书**：一个坏点由两条线性条件 + "$u\notin\operatorname{span}(v)$" 当场验。
2. **固定 $v$ 时是纯数值问题**：$\psi_\lambda:K_0\to\mathbb C^n/U$、$u\mapsto(\lambda I-A)u$ 是仿射铅笔
   $\psi_0+\lambda\psi_1$，$\ker\psi_\lambda\ni$ 至少 $\operatorname{span}(v)$，故
   $$\text{bad}\iff\exists\lambda:\ \operatorname{rank}(\psi_0+\lambda\psi_1)\le k-2 .$$
   数值矩阵、无符号参数 ⟹ 多项式时间（Kronecker/子式 gcd）。
3. **坏集 $\Lambda(v)$ 的显式描述**：记
   $$\Lambda(v)=\{\lambda\in\mathbb C:\ \dim\{u\in K_0:(\lambda I-A)u\in U\}\ge2\},$$
   它是 $(k-1)$-子式的 gcd 的零点集，**有限**（除非 $\psi_\lambda$ 恒降秩）。

### 遗留：$\lambda$ 随 $v$ 的三分

判定要回答"$\exists v\in B$：$\Lambda(v)=\varnothing$"。按 $\Lambda(v)$ 随 $v$ 的行为分三类：

| 类 | 定义 | 现状 |
|---|---|---|
| **1 固定根** | $\exists\lambda_0$ 使 $\lambda_0\in\Lambda(v)$ 对**所有** $v$ 成立 | 104 的 $Z^\circ$ 属此类（$\lambda_0=0$）；**已可判**（325 的 S2，精确除法） |
| **2 覆盖型** | $\lambda$ 随 $v$ 变但 $\Lambda(v)$ 由一个与 $v$ 无关的有限集覆盖 | 未见实例 |
| **3 真移动** | 否则（公共根真正随 $v$ 移动） | **已确认存在**（[327](../../c_stratification/attempts/327_lambda_movement_experiment.md)：10 个 $v$、8 个不同 gcd、零点各不相同） |

> **重要更正（327）**：初版写"若所有分量都落在 1/2 类，则 S3 可用有限检查代替 ⟹ 定理 C 有望"——
> 现在第 3 类已被实测确认，**S2 不能闭合定理 C**，S3 的 PIT 必须正面处理。
> 新的靶子是"gcd 次数在分量上恒定"（见 327）。

## 进展

- 引理已更正（假设改为"行张满 $U^\perp$"，证明改为 $\ker L=U$）；初版的错误与该错误为何不成立已写明。
- 三个后果（证书 / 固定 $v$ 数值可判 / $\Lambda(v)$ 的显式描述）成立。
- 三分表已写出，作为 S3 的判定转接点。

## 最终结论

1. 坏性有**谱形式**（在行张成假设下双向；否则充分）。
2. 逐点判定便宜（数值铅笔的秩跌落）；昂贵的仍是"$\exists v$"，即 325 的 S3。
3. **下一步的靶子被精确化**：证明"类 2 覆盖"或给出"类 3"的实例。若所有超平面分量都落在 1/2 类，则 S3 可用有限检查代替 ⟹ 定理 C 有望。

## 放弃原因

- 没有证明三分中"类 2/类 3"的判别准则，也没有构造类 3 的实例。
- 行张成假设在 $q<n-\dim U$ 时不成立，此时只有充分方向（未处理）。

## 残留价值

- 一个更正后的、可写进论文的谱形式引理（含正确假设）；
- $\Lambda(v)$ 的显式描述与三分表——把 S3 从"一个 PIT"进一步收窄成"类 2 vs 类 3"的结构判断；
- 记录了初版坐标混淆的错误，避免后续会话沿用。

## 相关文件

- [attempts/325](../../c_stratification/attempts/325_theorem_c_cost_model.md)（S3：唯一的 PIT）
- [attempts/324](../../c_stratification/attempts/324_hyperplane_component_theorem.md)（分量结构）
- [attempts/121](../../c_stratification/attempts/121_hyperplane_vector_bundle.md)（$S=\ker\sigma$、$U=\operatorname{span}(v,Av)$、$\rho$）
- [docs/05 Q9](../../../../docs/05_open_questions.md)

## 实例核对（c334：$n=5,p=1,r_0=1,q=3$，$k=3$）

三件都核了（[c334](../../../../tools/verification/c334_spectral_form_check.py)）：

| 检查 | 情形 A（非特征 $v$，$\dim U=2$） | 情形 B（特征 $v$，$\dim U=1$） |
|---|---|---|
| $\operatorname{rank}H=\omega$ | $2=k-1$ ✓ | $2=k-1$ ✓ |
| $\dim\ker H$ | $1$ ✓ | $1$ ✓ |
| $(5a)$（$\ker H\subseteq\ker H_A$） | ✓ | ✓ |
| $\dim\operatorname{row}L$ vs $\dim U^\perp$ | $3=3$，**$V=U^\perp$** | $3<4$，**$V\subsetneq U^\perp$** |
| $\gcd$（$\lambda H-H_A$ 的 $2$-子式） | $\lambda^2$ ⟹ 坏 | $1$ ⟹ 好 |
| 引理侧 $\gcd$（$M(\lambda)$ 的 $(k-1)$-子式） | $\lambda^2$ ⟹ 条件成立 | $1$ ⟹ 条件不成立 |
| 一致性 | **两侧同进同出，连多项式都相同** | 只充分方向可用，无矛盾 |

补充：3 个随机 $R$（仍 $V=U^\perp$）全部一致；一个退化 $R$（$V\subsetneq U^\perp$）上，引理条件成立 $\Rightarrow$ 坏成立（**充分方向**✓）。

**由此得到两个结论**：

1. **适用性已解决**：非特征层（$\dim U=2$，行数够且一般）**自动** $V=U^\perp$，引理双向；
   特征层（$\dim U=1$）$V\subsetneq U^\perp$，只有充分方向。这与 104 的观察吻合——特征点那支（$Z_1$）是**好**的。
   （顺带澄清：两种情形都满足 $\omega=k-1$，所以**特征与非特征都在超平面层内**，只是行空间张成不同。）
2. **一个可用的算法事实**：在 $Z^\circ$ 上，坏性可以用**更小的铅笔** $M(\lambda)$（$(n-2)\times k$，而非 $q\times k$）来测，
   且两者的 gcd **相同**（本例都是 $\lambda^2$）。这把 S3 的被测矩阵降了一个量级。

## 状态

- 引理：**[已证-纸面]**（作为**条件命题**：若 $\operatorname{row}L=U^\perp$，则双向；否则只充分）。
  初版的坐标混淆已更正。
- **适用性：已核**（c334）：非特征层（$\dim U=2$）自动 $V=U^\perp$，双向；特征层（$\dim U=1$）只充分。
- 三分：**已测**（c335）：第 1 类（104）与第 3 类（c335）都存在，第 2 类未见。**S2 不能闭合定理 C**。
