# Löfberg 2026 的 gadget 清单（可迁移的归约技术）

> 论文：J. Löfberg, *Static output-feedback stabilization is NP-hard*, arXiv:2609.16886 (2026-09)。
> 本文档只提取**可迁移的技术**，不复制论文内容。全文抽取：[`txt/lofberg2026_static_output_feedback.txt`](../txt/lofberg2026_static_output_feedback.txt)。

## 目标问题与结论

$$\textbf{SOF1}(A,B,C):\ \exists K\in\mathbb R^{1\times n}:\ A+BKC\ \text{Hurwitz}\qquad\textbf{NP-hard}$$

归约自 **Betweenness**（NP-完全）。$D=6(m+n)$、整数数据、位长对数。

## 六个 gadget

### G1 消去型源多项式（cancelling source polynomial）

取 $N=2(n+1)$，通用**首一三次**多项式
$$q(s;u,v)=s^3+(N+u)s^2+N(N+v)s+N^2(N+u+v)+1 .$$

Routh–Hurwitz 判据（首一三次 $s^3+as^2+bs+c$）：$a,b,c>0$ 且 $\Delta=ab-c>0$。对 $q$：
$$\Delta=Nuv-1 .$$

**为什么关键**：设计使所有"杂项"在 $\Delta$ 中**完全抵消**，只剩一个**双线性型** $Nuv-1$。
于是"$\Delta>0$" $\iff$ "$uv>1/N$"——一个**乘积符号条件**，天然编码**序关系**（Betweenness ✓）。

> 对应我们：我们需要"某族多项式无公根"，而 $m=2$ 时它等价于 $\operatorname{Res}\ne0$，即**符号非零** ✓。
> 所以"符号条件"这一层是可对接的；缺的是把 $\operatorname{Res}$ 变成"双线性型 + 常数"这种**可设计**的形状。

### G2 锚点（anchors）

固定参数值 $0$ 与 $N$ 的"锚点"三次式：只要某个 $x_i\notin(0,N)$，某个锚点的 $\Delta\le-1$ 立刻失败。

**作用**：把参数向量**限制在一个盒子里**（否则一票否决），从而后续的定量估计（G3、G4）可以在紧集上做。

### G3 定量裕度（quantitative margin）

用的是 $Nuv>1$ 而不是 $uv>0$：因为整数/有界性给出 $|Nuv|\ge N$（当 $uv\ne0$ 且整），
所以在满足侧 $\Delta\ge N-1\gg0$，在失败侧 $\Delta\le-1$——**两侧被常数间隔分开** ✓。

**作用**：这个间隔在 G5 的聚合扰动下不会消失（保证"聚合后仍能判定"）。

### G4 频率分离（frequency separation）

把 $J=m+n$ 个三次式各取**两个共轭移位**，移位量 $\Omega_j=jH$、$H=2R_0+1024JC^\ast$（整数、足够大），
使各因子的根落在**互不相交的圆盘**里。

**作用**：$\prod$ 的根 = 各因子根的并 ⟹ **"乘积 Hurwitz" $\iff$ "每个因子 Hurwitz"** ✓。
这把"多个条件取 AND"变成**一个**多项式的条件 ✓（对我们：需要"全组无公根"，是 AND ✓）。

### G5 一阶截断（first-order truncation）

$$\text{聚合：}P(s,x)=P_0(s)+\sum_a \Delta_a(s,x)\,\frac{P_0(s)}{Q^0_a(s)}$$

即 $\prod_a(Q^0_a+\Delta_a)$ 的**一阶截断**。因为每个 $\Delta_a$ 对 $x$ **仿射**、系数 $P_0/Q^0_a$ 与 $x$ 无关，
所以 $P$ 对 $x$ **仿射** ✓。再用 G4 的分离 + Rouché 型论证证明：$P$ 的根数 = 各因子根数之和 ✓。

**作用**：**仿射**是硬要求——只有仿射的多项式族才能实现为 $A+BKC$ 的特征多项式（单列 $B$：$\det(sI-A-BKC)=\det(sI-A)-w^{\mathsf T}\mathrm{adj}(sI-A)B$ 对 $w$ 仿射）。

### G6 全局缺陷引理（global no-instance defect）

> **Lemma 2.2**：若 Betweenness 不可满足，则**对每个** $x\in\mathbb R^n$ 都存在一个源三次式使 $\Delta\le-1$（且常数项 $c\ge1$）。

**作用**：这是"$\forall$ 侧"的引擎——不可满足 ⟹ **所有**参数都被抓 ⟹ 聚合后必然不 Hurwitz ✓。
没有它，$K$ 可以"逃跑"（跑到某个让所有条件都满足的地方）✓。

> 我们的问题需要**完全一样**的东西：不可满足 ⟹ **所有** $\tau\in\mathcal A$ 都在 $\mathrm{Bad}$ 里 ✓。
> 这正是 §12（猜想 11.4 反例）之后我们已知"$\dim$ 比较是真判据"的那种"坏集覆盖"现象 ✓。

## 映射到本项目：能对接什么、缺什么

| gadget | 我们的对应物 | 状态 |
|---|---|---|
| G1 消去型 + 双线性 | $(5b)$ 的 $m{=}2$ 情形 $\iff\operatorname{Res}\ne0$（符号条件）| **可对接**（形状同）|
| G2 锚点 | 用 $L_0$ / $\mathcal J$ 侧的数据把 $\tau$ 限制在盒子里 | 需设计（$L_0$ 可自由选 ✓）|
| G3 定量裕度 | 整数实例的"两侧常数间隔" | 需设计 |
| G4 频率分离 | 需要"全组 $k\times k$ 子式无公根" = AND | **可对接**（我们用 gcd）|
| G5 仿射截断 | 我们的 $\tau$ **本来**就仿射进入 ✓ | ✓ 天然满足 |
| G6 全局缺陷 | 需要"不可满足 ⟹ $\mathrm{Bad}=\mathcal A$" | **最难**：我们的 $\mathrm{Bad}$ 由铅笔子式决定，不是自由设计 |

## 真正的障碍（诚实）

我们的族 $p_j$ 是**铅笔的子式**，由实例 $(A,C,L_0)$ 决定，**不是自由可设计的** ✓；
而 Löfberg 的源多项式是**逐条构造**的 ✓。所以：

$$\text{要么}\ \text{(i) 找到一种实例族使子式"长得像"源三次式（困难但非显然不可能）};\quad
\text{(ii) 要么用自由行 } R \text{ 的自由度去逼出所需的子式}.$$

(ii) 的希望在于：$R$ 有 $(k-1)\times n$ 个自由参数（远多于 gadget 需要的 $n$ 个），
但 $(5a)$ 的"行空间"约束会把这些自由度**绑在一起** ✗ —— 这是下一步要算清的事。

## 用途

- 若 (i)/(ii) 成功 ⟹ $(k,1)$ 层 NP-hard ⟹ **$q1$ = 真**（路线 T9）；
- 若都不成 ⟹ 硬度路线仍缺证据，$q1$ 更可能"假"（路线 F12：铅笔完成理论）。