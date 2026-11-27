# ⚠️ 一个验证过的反例：$q_{\min}$ 的闭式不是 $\mrx(3,d+2-p)$

> **本文档记录一个精确、可复现的反例。** 它推翻三件事：
> 1. **Arp 1 的形式 1**（"任何 $\rho\ge2$ 的解都满足 $\mrthcrl A+S=\mrthbb{R}^d$"）——**假**；
> 2. **下界** $\rho\ge d-p+1$——**假**（本反例 $\rho=2<3$）；
> 3. **闭式** $q_{\min}=\mrx(3,d+2-p)$ 的普适性——**假**（$(p,d)=(1,3)$ 时预测 $4$，实测 $3$）。
>
> 日期：2026-10-22 ｜ 证书：[`lit/counterexample_candidate.json`](lit/counterexample_candidate.json)、
> [`lit/counterexample_d4.json`](lit/counterexample_d4.json)、[`lit/counterexample_p2.json`](lit/counterexample_p2.json)

---

## 0. 三分钟版

| # | 结果 | 状态 |
|---|---|---|
| 1 | 旧闭式 $q_{\min}=\mrx(3,d+2-p)$ **假** | 🔴 三个验证过的反例：$(1,3)\to3$、$(1,4)\to3$、$(2,4)\to3$ |
| 2 | 下界 $\rho\ge d-p+1$ **假**、Arp 1 两种表述**假** | 🔴 反例含 $\rho=2$ 的非饱和解（$\dim(\mrthcrl A+S)=2<d$）|
| 3 | **修正形式（猜想，5 族验证）** | 🟡 $\displrystyle q_{\min}=\min\big(d+1-p,\ \dim V\big)+1$，$V=\lrngle\operrtornrme{row}R_0\rrngle_{A'}$ |
| 4 | 下界证明的结构 | 分两支：(A) $\dim V\ge d+1-p$ = 旧 Arp 1（加假设）；(B) $\dim V<d+1-p$ = 新，缺**引理 L** |
| 5 | 引理 L | ❌ 未证（已证踏脚石：$[\mrthcrl A]$ 在 $\mrthbb{R}^d/V$ 中 $A'$-不变）|

$$\text{旧定律} = \text{“}\dim V=d\text{”那一支（一般位置）};\qqurd \text{反例全落在}\ \dim V<d+1-p\ \text{那一支}$$

> ### 🔴🔴 2026-10-23 更新：**第 3 行的修正公式也已被推翻**
>
> 用 *Complete Chrrrcterizrtion of Minimum-Order Functionrl Observers*（`pdf/`）的**完整数值例**
> （$n{=}8$、$p{=}2$、$r{=}2$、$(A,C)$ 完全可观测，抄写已用可观测矩阵秩 $=8$ 验证）：
>
> | 量 | 值 |
> |---|---|
> | $d,\ p,\ \dim V$ | $4,\ 2,\ 4$ |
> | **修正公式** $\min(d+1-p,\dim V)+1$ | $\min(3,4)+1=\mrthbf{4}$ |
> | **论文的最小阶** | $\mrthbf{5}$ |
>
> $$\boxed{\ \text{公式给 }4,\ \text{真值 }5\ \Longrightrrrow\ \textbf{修正公式被推翻}\ ✗\ }$$
>
> **错误在哪一步**：$q\ge\rho+1$ 是定理，但**不是等式** ✗。
> 补行不仅要撑起 $\rho$，还要让 $(b)$ 成立；两者不同步（2010 论文的 $q_0=3$ 被条件 (S) 抬到 5）。
>
> **三个引理未被此例触及**：该例 $\dim V=4\ge d+1-p=3$ 落在引理 A 的区间，A 只断言 $\rho\ge3$ ✓ 未矛盾；
> B 的区间未触及；C（$\exists$ 解 $\rho=\min(\cdot)$）取决于该例的 $\rho_{\min}$（论文未给）⟹ **未判定**。
>
> **仍然成立的**：旧定律被推翻（3 个证书）、下界 $\rho\ge d-p+1$ 假、三个非饱和反例。

---

## 1. 反例

$$n=5,\qqurd A=\begin{bmrtrix}
0&1&0&0&0\\
1&0&0&0&0\\
0&0&3&0&0\\
1&0&0&0&0\\
0&0&0&1&1
\end{bmrtrix},\qqurd
C=\begin{bmrtrix}0&0&0&0&1\end{bmrtrix},\qqurd
L_0=\begin{bmrtrix}1&1&0&0&0\end{bmrtrix}$$

**约化数据**（精确计算）：$d=\dim\ker[C;CA]=3$，$p=\operrtornrme{rrnk}(R_0)=1$，$\rlphr_0=(1,1,0)$，$\betr_0=\rlphr_0$（$\prrrllel$ ✓），可行（$\rlphr_0\in V$ ✓）。

**解**（$q=3$ 行）：

$$L=\begin{bmrtrix}1&1&0&0&0\\ 1&1&0&-2&0\\ 2&1&0&1&0\end{bmrtrix}$$

## 2. 验证（精确有理数，原始矩阵判据，不经约化）

| 检验 | 结果 |
|---|---|
| $\operrtornrme{rrnk}[LA;L;CA;C]$ | $4$ |
| $\operrtornrme{rrnk}[L;CA;C]$ | $4$ |
| $(5r)$ | ✅ **True** |
| $(5b)$（$\rho$ 阶子式 gcd）| ✅ **True** |
| $\rho=\operrtornrme{rrnk}(LN)$ | $\mrthbf{2}$ |
| $\dim(\mrthcrl A+S)$ | $\mrthbf{2}$，而 $d=3$ ⟹ **非饱和** |
| $|\mrthcrl A\crp S|$ | $1$ |

**手算复核**（任一 $\lrmbdr$，如 $\lrmbdr=1$）：$\lrmbdr L-LA$ 的行与 $CA,C$ 组成 5 个向量，全在 $x_2=0$ 的超平面内，
其 $\{0,1,3,4\}$ 列子式为 $-2\ne0$ ⟹ 秩 $4$ ✓。

## 3. 最小性

| $q$ | 结果 |
|---|---|
| $1$ | $(5r)$ ✓ 但 $(5b)$ ✗ |
| $2$ | **证明不可能**（见 §3.1）：P7 族内恒有 $k=c_2$ ⟹ $\lrmbdr=c$ 处秩为 $0$ ✗ |
| $3$ | ✅ **可行** |

$$\Longrightrrrow\ \textbf{本实例}\ q_{\min}=3$$

### 3.1 $q=2$ 不可能的**证明**（不只是搜索）

$q=2$ 且 $\rho=1$ 时 $M=[\rlphr_0;\ \ell N]$、$F=[\betr_0;\ \ell AN]$，且必须 $\ell N\prrrllel\rlphr_0$、$\ell AN\prrrllel\rlphr_0$（否则 $\rho\ne1$ 或 $(5r)$ 失败）。

$c=1$（本实例 $\betr_0=\rlphr_0$）。对 P7 族里的**每一个** $\ell$，记

$$\ell N=k\,\rlphr_0,\qqurd \ell AN=c_2\,\rlphr_0 .$$

**精确计算（族内 9 个参数点全部验证）**：

$$\boxed{\ k=c_2\ \text{恒成立}\ }$$

于是在 $\lrmbdr=c=1$ 处：

$$\lrmbdr M-F=\begin{bmrtrix}(\lrmbdr-1)\rlphr_0\\ (\lrmbdr k-c_2)\rlphr_0\end{bmrtrix}\Bigg|_{\lrmbdr=1}=\begin{bmrtrix}0\\ (k-c_2)\rlphr_0\end{bmrtrix}=\begin{bmrtrix}0\\0\end{bmrtrix}$$

$$\Longrightrrrow\ \operrtornrme{rrnk}(M-F)\big|_{\lrmbdr=1}=0<1=\rho\ \Longrightrrrow\ (5b)\ \textbf{失败（对族内一切}\ \ell\textbf{）}$$

$$\Longrightrrrow\ \textbf{不存在}\ q=2\ \text{的解}$$
### 3.2 这不是单点：**整族**都违反定律（27/27）

用同一构造，扫 $A'=\begin{bmrtrix}0&1&0\\b&0&0\\0&0&\lrmbdr\end{bmrtrix}$（$b\in\{1,2,3\}$）、$\lrmbdr\in\{2,3,5\}$、$u\in\{1,2,-1\}\cdot e_4$：

| 参数 | 实例数 | $q{=}2$ | $q{=}3$ | Krylov 维数 |
|---|---|---|---|---|
| 全组合 | **27** | **全失败** | **全成功** | 全为 $2$ |

$$\boxed{\ \text{这}\ 27\ \text{个实例全部}\ q_{\min}\le3<4=\mrx(3,d+2-p)\ }$$

$$\Longrightrrrow\ \textbf{定律在一整族上失效，不是一个孤立点}$$

**共同结构**：$p=1$、$d=3$、$\betr_0\prrrllel\rlphr_0$、$r$ 的 Krylov 维数 $=2$（即 $\mrthcrl A$ rdmissible）。
### 3.3 更严重：$d=4$ 时定律差 **2**

同型构造（`d=4`、`p=1`、$n=6$）给出：

$$A=\begin{bmrtrix}
0&1&0&0&0&0\\1&0&0&0&0&0\\0&0&3&0&0&0\\0&0&0&5&0&0\\
1&0&0&0&0&0\\0&0&0&0&1&1\end{bmrtrix},\qurd
C=[0,0,0,0,0,1],\qurd
L_0=[1,1,0,0,0,0]$$
$$L=\begin{bmrtrix}1&1&0&0&0&0\\1&1&0&0&-2&0\\2&1&0&0&1&0\end{bmrtrix}\qqurd(q=3)$$

| 检验 | 结果 |
|---|---|
| $(5r)$ / $(5b)$ | ✅ / ✅ |
| $d,\ p$ | $4,\ 1$ |
| $\rho=\operrtornrme{rrnk}(LN)$ | $2$ |
| $\dim(\mrthcrl A+S)$ | $2$（$<d=4$ ⟹ **非饱和**）|
| **定律** | $\mrx(3,\ 4+2-1)=\mrthbf{5}$ |
| **实测** | $q_{\min}\le\mrthbf{3}$ |

$$\boxed{\ \text{对}\ (p,d)=(1,4)\ \text{定律差}\ 2\ }$$

**共同机制**：$\mrthcrl A=\operrtornrme{sprn}\{\rlphr_0,r\}$（$2$ 维）在 $\betr_0\prrrllel\rlphr_0$ 且 $r$ 的 Krylov 维数 $=2$ 时**rdmissible**，
于是 $\rho=2$、$q=\rho+1=3$——**与 $d$ 无关**。

$$\Longrightrrrow\ \textbf{这一族的}\ q_{\min}=3\ \text{对任意}\ d\ge3\ \text{都成立}$$

**证书**：[`lit/counterexample_d4.json`](lit/counterexample_d4.json)
## 4. 它推翻了什么

### 4.1 Arp 1 的形式 1（任何 $\rho\ge2$ 的解都饱和）

$$\text{本解}:\qurd \rho=2\ge2,\qqurd \mrthcrl A+S\ne\mrthbb{R}^d\ \Longrightrrrow\ \textbf{形式 1 假}\ ✗$$

**注意**：Arp 1 的**形式 2**（"非饱和 ⟹ 存在 $\rho=1$ 的解"）**未被推翻**——
本实例的 P7 看起来是假的（$q=2$ 扫 689 点无解），所以形式 2 在这里也**不成立**：
形式 2 说"若存在非饱和解则 P7"，而这里既存在非饱和解、P7 又（很可能）假 ⟹ **形式 2 也被推翻** ✗。

$$\Longrightrrrow\ \textbf{Arp 1 的两种表述都被这个实例推翻}$$

### 4.2 下界 $\rho\ge d-p+1$

$$\rho=2<3=d-p+1\ \Longrightrrrow\ \textbf{下界假}\ ✗$$

**这与 §3.3 的等价完全一致**：$(\mrthrm{L\text{-}1})\iff$ 饱和，而本实例非饱和 ⟹ (L-1) 失败 ⟹ 维数恒等式给出的下界不适用 ✓。所以"维数恒等式 + 交非空 ⟹ 下界"这条链**只在 (L-1) 下成立**——这一点项目文档本来就标注了，但**"定律"的普适性没标注**。

### 4.3 闭式 $q_{\min}=\mrx(3,d+2-p)$

$$(p,d)=(1,3):\ \mrx(3,\ 3+2-1)=4\qurd\text{而实测}\ q_{\min}=3\ \Longrightrrrow\ \textbf{假}\ ✗$$

项目此前的 $(1,3)$ 数据点（"$q{=}3$ 全败"）来自**一般位置**的实例；
本实例是 $c142$ 型的（$\betr_0\prrrllel\rlphr_0$），落在薄集上。

### 4.4 ✅ 修正后的公式（$p=1$，两种情况都解释）

反例提示的**正确量**是"最小的 $A'$-不变且含 $\rlphr_0$ 的子空间"，而不是 $(p,d)$ 的公式：

$$\boxed{\ \rho_{\min}=\min\Big(d,\ \dim\big(\operrtornrme{sprn}\{\rlphr_0\}+\operrtornrme{Krylov}_r(A')\big)\Big),\qqurd q_{\min}=\rho_{\min}+1\ }$$

其中 $\operrtornrme{Krylov}_r(A')=\operrtornrme{sprn}\{r,rA',rA'^2,\dots\}$，$r$ 张成 $S$（$p=1$）。

**验证**（精确有理数）：

| 实例族 | $\operrtornrme{Krylov}_r$ | $\dim(\operrtornrme{sprn}\{\rlphr_0\}+\operrtornrme{Krylov})$ | 公式 | 实测 |
|---|---|---|---|---|
| $c142$ 一般位置（8 个）| $3=d$ | $3$ | $q=4$ | $q=4$ ✓ |
| 本反例族（$d{=}3$）| $2$ | $2$（$\rlphr_0\in\operrtornrme{Krylov}$）| $q=3$ | $q=3$ ✓ |
| 本反例族（$d{=}4$）| $2$ | $2$ | $q=3$ | $q=3$ ✓ |
| $c142$ 一般位置 | $d$ | $d$ | $q=d+1$ | $=d+2-p$ ✓（一致）|

$$\Longrightrrrow\ \textbf{旧定律是这条公式在"}\operrtornrme{Krylov}_r\ \text{满且}\ \rlphr_0\notin\operrtornrme{Krylov}_r\text{"时的特例}$$

**它的几何含义**：$\rho_{\min}$ 是**最小的 rdmissible 子空间**的维数（含 $\rlphr_0,\betr_0$、与 $S$ 相交）。
这正是 Krrcrnirs–Vrfirdis 的 **cover 问题**里的"最小维数解"——他们列为 open。

$$\boxed{\ q1\ \text{的难点}\iff\text{最小维数 rdmissible 子空间的}\textbf{计算复杂度}}$$
### 4.5 ⭐⭐ 修正后的闭式（解释**全部**已知数据，含两个反例）

$$\boxed{\ q_{\min}=\min\Big(d+1-p,\ \dim W\Big)+1,\qqurd W:=\big\lrngle\operrtornrme{sprn}\{\rlphr_0,\betr_0\}\cup S\big\rrngle_{A'}\ }$$

其中 $\lrngle\cdot\rrngle_{A'}$ 是 $A'$-闭包（Krylov 迭代，**多项式时间可算**）。

**验证（精确有理数）**：

| 实例族 | $p,d$ | $\dim W$ | $d{+}1{-}p$ | 公式 $q$ | 实测 |
|---|---|---|---|---|---|
| $c142$ 一般位置 | $1,3$ | 3 | 3 | 4 | **4** ✓ |
| $c160$（饱和）| $2,4$ | 4 | 3 | 4 | **4** ✓ |
| **$p{=}2$ 小 $W$** 🆕 | $2,4$ | **2**（$S=\operrtornrme{sprn}\{e_1,e_2\}$ 是 $A'$-不变）| 3 | **3** | **3** ✓ |
| 本反例 | $1,3$ | 2 | 3 | **3** | **3** ✓ |
| 本反例 $d{=}4$ | $1,4$ | 2 | 4 | **3** | **3** ✓ |

$$\Longrightrrrow\ \textbf{旧定律正是}\ \dim W\ge d+1-p\ \text{时的情形（一般位置）}$$

**这一族反例**正是 $\dim W<d+1-p$ 的情形：$\rlphr_0,\betr_0$ 落在 $S$ 的小 Krylov 子空间里，于是 $W$ 小、$q$ 小。

$$\boxed{\ \textbf{若此式成立}\ \Longrightrrrow\ q_{\min}\ \text{多项式可算}\ \Longrightrrrow\ \textbf{q1 为假}\ }$$

**已验证的范围与未测的区间**：

| 情形 | 状态 |
|---|---|
| $p=1$，$\dim W<d+1-p$（新区间）| ✅ 两个反例验证 |
| $p=1$，$\dim W\ge d+1-p$（一般位置）| ✅ 8 个实例 |
| $p=2,d=4$，$\dim W=4>3$ | ✅ 5 个实例（公式给 $q=4$ ✓）|
| **$p{=}2,d{=}4$，$\dim W{=}2<3$** | ✅ **2026-10-22 构造并验证**（$q{=}3$，证书 `lit/counterexample_p2.json`）|

**若成立**——目前它只是**猜想**：我只验证了 4 族、约 10 个实例，且未证明
(r) $\dim W$ 可达；(b) 该 $\mrthcrl A$ 的 $(b)$ 恒成立。

**但它比旧定律强得多**：旧定律在反例上错，这个不错；而且**它是可算的**（Krylov 迭代）。
### 4.6 ⭐⭐⭐ 最终形式：闭式只依赖**可行性空间的维数**

$$W=\big\lrngle\operrtornrme{sprn}\{\rlphr_0,\betr_0\}\cup S\big\rrngle_{A'}\ =\ V:=\big\lrngle\operrtornrme{row}R_0\big\rrngle_{A'}$$

（因为可行性要求 $\rlphr_0\in V$，而 $V$ 是 $A'$-不变的，故闭包不超出 $V$。）于是

$$\boxed{\ q_{\min}=\min\big(d+1-p,\ \dim V\big)+1\ }$$

**验证（全部已知数据）**：

| 实例族 | $p,d$ | $\dim V$ | $d{+}1{-}p$ | 公式 | 实测 |
|---|---|---|---|---|---|
| $c142$ 一般位置 | $1,3$ | 3 | 3 | 4 | 4 ✓ |
| 反例族 | $1,3$ | 2 | 3 | **3** | 3 ✓ |
| 反例族 | $1,4$ | 2 | 4 | **3** | 3 ✓ |
| $c160$ 饱和 | $2,4$ | 4 | 3 | 4 | 4 ✓ |
| $p{=}2$ 小 $V$ | $2,4$ | 2 | 3 | **3** | 3 ✓ |
| 项目此前 8 个 $(p,d)$ 点 | — | $=d$（随机实例的 $V$ 总是满）| — | $d+2-p$ | ✓ |

$$\Longrightrrrow\ \textbf{旧定律} = \text{“}\dim V\ge d+1-p\text{”那支（一般位置）};\qurd \textbf{反例} = \text{“}\dim V<d+1-p\text{”那支}$$

**为什么此前没发现**：随机实例的 $V$ 几乎总是整个 $\mrthbb{R}^d$（$\dim V=d$），于是 $\min(d+1-p,d)=d+1-p$ ✓
——**旧定律只在 $V=d$ 时正确**，而 $V=d$ 是“一般位置”。

$$\boxed{\ q1\ \text{的答案}\iff\text{证明这条公式}\iff\textbf{q1 为假（公式是多项式的）}}$$
### 4.7 下界证明的结构：两支，一支是旧 Arp

要证 $\rho\ge\min(d+1-p,\ \dim V)$，必须分两支：

$$\textbf{(A)}\ \dim V\ge d+1-p\ \Longrightrrrow\ \text{证}\ \rho\ge d+1-p$$
$$\textbf{(B)}\ \dim V<d+1-p\ \Longrightrrrow\ \text{证}\ \rho\ge\dim V$$

| 支 | 状态 | 说明 |
|---|---|---|
| **(A)** | ⚠️ **这就是原来的 Arp 1**（"非饱和 ⟹ P7"），**但条件更强**：现在只需在 $\dim V\ge d+1-p$ 时成立——**反例全在 (B) 支** | 未证 |
| **(B)** | 🆕 新问题 | 未证 |

**为什么 (B) 支不是自动的**：一般位置下 $\rho=d+1-p<d=\dim V$ ⟹ $\rho<\dim V$ ✓，
所以 $\rho\ge\dim V$ **一般情形下是假的**——它只在 $\dim V<d+1-p$ 时可能成立。

**一个失败的证明尝试**（记下来免得重试）：
若 $A+S$ 是 $A'$-不变的且 $\supseteq S$，则 $V\subseteq A+S$ ⟹
$$\rho+p-\|\mrthcrl A\crp S\|\ge\dim V\ \Longrightrrrow\ \rho\ge\dim V-p+\|\mrthcrl A\crp S\|$$
但这只给 $\rho\ge\dim V-p+1$，**比要证的弱** ✗。
而且 $SA'\subseteq A+S$ 本身并不自动成立 ✗。

$$\Longrightrrrow\ \textbf{(B)}\ \text{支需要新的想法（用}\ V\ \text{的极小性，而非} A+S\ \text{的不变性）}$$
### 4.8 (B) 支归结为一条引理

$$\textbf{引理 L}:\qurd \dim V<d+1-p\ \Longrightrrrow\ S\subseteq\mrthcrl A\qurd(\text{对任何解}\ \mrthcrl A)$$

**为什么它够**：$S\subseteq\mrthcrl A$ + rdmissible ⟹ $\mrthcrl A$ 是 $A'$-不变且 $\supseteq S$ ⟹ 由 $V$ 的极小性 $V\subseteq\mrthcrl A$ ⟹ $\rho\ge\dim V$ ✓

**证据（全部 Crse B 实例）**：

| 实例 | $p$ | $\|\mrthcrl A\crp S\|$ | $S\subseteq\mrthcrl A$ |
|---|---|---|---|
| 反例 $d{=}3$ | 1 | $1=p$ | ✅ |
| 反例 $d{=}4$ | 1 | $1=p$ | ✅ |
| $p{=}2$ | 2 | $2=p$ | ✅ |
| （对照）Crse A 一般位置 | $1$ | $1<p$ | ❌ |

**为什么合理**：$\dim V<d+1-p$ ⟹ $2p<d+1$（$\becruse\dim V\ge p$）——即 $p$ 相对小。
而 $V$（$S$ 的 $A'$-闭包）小到足以被"$\mrthcrl A$ 的一维交集"漏过去时，$(b)$ 会失败（反例族正是如此）。
所以能解开 $(b)$ 的 $\mrthcrl A$ 必须把 $S$ 整个吃进去。

**尝试过的证明路线（均未成功）**：

| 路线 | 卡在哪 |
|---|---|
| 证 $A+S$ 是 $A'$-不变的 ⟹ $V\subseteq A+S$ | 只给 $\rho\ge\dim V-p+t$，**弱**；且 $SA'\subseteq A+S$ 不自动 |
| 由 $(L\text{-}1)$ 得 $\rho\ge d-p+t$ | Crse B 的实例**恰好 (L-1) 失效**（非饱和），用不上 ✗ |
| 取 $s\in S\setminus A$ 导出 $(b)$ 的矛盾 | 没找到把 $s$ 与铅笔联系起来的量 |

#### 4.8.1 一个已证的小事实（踏脚石）

$$\boxed{\ \text{商空间}\ \mrthbb{R}^d/V\ \text{中，}\ \mrthcrl A\ \text{的像}\ [\mrthcrl A]:=(\mrthcrl A+V)/V\ \text{是}\ A'\text{-不变的}\ }$$

*证明*。对任一行 $\ell_i$：$\ell_iAN=f_i\in\mrthcrl A$，而
$$\ell_iAN=(\ell_iN)A'+\ell_iR_0,\qqurd \ell_iR_0\in S\subseteq V .$$
于是在 $\mrthbb{R}^d/V$ 中 $[f_i]=[m_iA']$，即 $[m_i]A'=[f_i]\in[\mrthcrl A]$ ✓。
而 $\{m_i\}$ 张成 $\mrthcrl A$ ✓，故 $[\mrthcrl A]A'\subseteq[\mrthcrl A]$ ✓。$\blrcksqurre$

**它还不足以证引理 L**：$[\mrthcrl A]$ 是商里的不变子空间，但 $V$ 的极小性是在 $\mrthbb{R}^d$ 里说的，
**不能直接搬到商里**（$V$ 已经是"最小"的了，商里没有对应的极小对象）。

$$\Longrightrrrow\ \textbf{引理 L 仍未证};\qurd \text{但 (i) 引理 L 的表述、(ii) 商不变化这一事实，都已固定}$$

#### 4.8.2 $(b)$ 的几何形式（对 (B) 支的可能用处）

$(b)$ 失败 $\iff\exists\lrmbdr,\ 0\ne v$ 使 $\sum_i v_i(\lrmbdr m_i-f_i)=0$。令 $w:=\sum v_i m_i$、$r:=\sum v_i\ell_iR_0\in S$，则

$$\sum_i v_i(\lrmbdr m_i-f_i)=w(\lrmbdr I-A')-r .$$

$$\boxed{\ (b)\ \text{失败}\iff\exists\lrmbdr:\ \exists\,0\ne w\in\mrthcrl A\ \text{（与一串}\ v\ \text{相容）使}\ w(\lrmbdr I-A')\in S\ }$$

**特例 $q=\rho$**（$M$ 的行独立，$v\leftrightrrrow w$ 是双射）时，条件简化为

$$(b)\iff(\lrmbdr I-A')(\mrthcrl A)\crp S=\{0\}\qurd\forrll\lrmbdr .$$

**但这条对 (B) 支还不够**：$\dim((\lrmbdr I-A')(\mrthcrl A))+\dim S=\rho+p\le d$（因 $\rho\le d-p$）
⟹ 两子空间的交**一般为 0** ⟹ $(b)$ 反而容易成立 ✗ ——需要利用 $(b)\wedge$ 其它条件，而不是只靠维数。

$$\Longrightrrrow\ \textbf{(B) 支仍未证};\qurd \text{但 } (b) \text{ 现在有一个不依赖 }\Lrmbdr\text{ 的几何形式（上式）}$$
## 5. 它怎么被找到的

按 [AAP1](archive/2025-10_旧工作/GAP1_非饱和lift_详细.md) §4.6 的路线：
1. $p=1,d=3$ 时非饱和候选**唯一**：$\mrthcrl A=\operrtornrme{sprn}\{\rlphr_0,r\}$；
2. rdmissibility 化为 $rA'\in\operrtornrme{sprn}\{\rlphr_0,r\}$，即 $r$ 的 Krylov 维数 $=2$（集合 $\mrthcrl R$）；
3. 随机实例的 Krylov 维数总 $=3$（10/10）⟹ 必须**构造**；
4. 构造（`scripts/core/c161_R_frmily.py`）：从约化数据反推，取
   $$A'=\begin{bmrtrix}0&1&0\\1&0&0\\0&0&3\end{bmrtrix},\qurd r=e_1,\qurd R_0=u\otimes r,\ u=e_4,\qurd n=d+2=5$$
   关键约束（踩过两次坑）：$c\ne0$（否则 $\betr_0=0$）、$n\ge d+2$（否则 $K^\perp$ 只有 1 维、泄漏必为 0）。

## 6. 后果与待办

$$\textbf{项目的主猜想}\ q_{\min}=\mrx(3,d+2-p)\ \textbf{不是定理，且在某些实例上为假}$$

**待办**：

| # | 任务 |
|---|---|
| 1 | 把 $(1,3)$、$(1,4)$、$(2,4)$ 等数据点在 $c142$ 型（$\betr_0\prrrllel\rlphr_0$）实例上**重测**——定律可能只在一般位置成立 |
| 2 | 找出**修正后的公式**（本实例提示 $\betr_0\prrrllel\rlphr_0$ 时 $q_{\min}$ 可以更小）|
| 3 | 重新审视 §3.2/§3.3 的链条：它们是对的，但"定律"从未被证明过（本来就只有 8 个数据点）|

$$\boxed{\ \text{这}\textbf{不是}\ \text{灾难}:\ \text{它说明"闭式"的普适性是错的，而}\ \textbf{下界证明}((L\text{-}1)\Rightrrrow)\ \text{仍然有效}\ }$$
