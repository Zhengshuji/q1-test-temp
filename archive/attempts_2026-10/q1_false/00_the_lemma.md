# THE_LEMMA —— 层紧性引理（Q1-FALSE 的承重引理）

## 目标
给出"层紧性"引理：$q(ho)=ho+1$（固定 $ho$ 层的最优解），并刻画 $ho=1$ 层。

## 最终结论
**部分有效**：$ho=1$ 层有完整刻画（可多项式判定）；一般层的"$q(ho)=ho+1$"**不成立**（70 对中 69 紧、1 例外已解释；且 $c$ 可被顶大）。

## 相关文件
- [../tests/rho1/](../tests/rho1/)、[../tests/verify/](../tests/verify/)
- [../../../proof/rho1_layer/](../../../proof/rho1_layer/README.md)
- [../../../tools/layer_search/c192_reduced_search.py](../../../tools/layer_search/c192_reduced_search.py)


## 0. 记号（与 README 一致）

给定 $(A,C,L_0)$，$A\in\mathbb R^{n\times n}$，$C\in\mathbb R^{p\times n}$，$L_0\in\mathbb R^{r\times n}$。

- $K=\ker[C;CA]$（$\dim=d$），基 $N$（$n\times d$），$\mathcal J=\operatorname{row}[C;CA]$（$K^\perp=\mathcal J$）；
- $A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$，$R_0=AN-NA'$，$S=\operatorname{row}(R_0)$，$V=\langle S\rangle_{A'}$；
- 对解 $\mathcal L$：$\rho=\operatorname{rank}(\mathcal L N)=\dim(\operatorname{row}\mathcal L\cdot N)$，$M=\mathcal LN$，$N'=\mathcal L R_0$；
- $\rho_0=\operatorname{rank}(L_0N)$，$\rho^*=\min\{\rho:\ q(\rho)<\infty\}$，$q_{\min}=\min_\rho q(\rho)$。

**目标公式（2026-10-25 已被推翻）**：~~$q_{\min}=\max(r,\rho^*+1)$~~

**反例**（`../../proof/refuted/certificates/counterexample_refute_layer_formula_2026-10-25.json`）：$n{=}5,p{=}2,r{=}2,d{=}1,\dim V{=}1,\rho_0{=}0$，
$L_0$ 不是解，但 $q_{\min}=3>\max(r,\rho^*+1)=2$。机制：$q=r$ 时 $\mathcal V=\operatorname{row}(L_0)$，故 $L_0$ 必须是解。

**修正后的目标公式**：

$$\boxed{\ q_{\min}=\max\big(r+\delta,\ \rho^*+1\big)},\qquad
\delta=\begin{cases}0,& L_0\ \text{本身是解}\\1,& L_0\ \text{不是解}\end{cases}$$

下界已证（$q\ge r+\delta$ 与 $q\ge\rho+1$）；与 66 个实例一致；等号是猜想。

---

## 1. 弱版（修正后，足够推出目标公式）

$$\textbf{L-T（修正）}:\qquad q(\rho^*)=\max\big(r+\delta,\ \rho^*+1\big),\qquad \delta=[L_0\ \text{不是解}].$$

> 原版 $q(\rho^*)=\max(r,\rho^*+1)$ 已被 2026-10-25 的反例否定（见 §0）。
> 反例中 $r{=}2>\rho^*{=}1$，$q(\rho^*)=3=\max(2+1,\,2)$ —— 修正版仍成立。
> 下界 $q\ge\max(r+\delta,\rho+1)$ 已证；等号部分是猜想。

## 2. 强版（更干净，可能更容易陈述）

$$\textbf{L-T$'$}:\qquad \forall\ \text{可达}\ \rho:\quad q(\rho)=\max(r,\ \rho+1).$$

> 强版 ⟹ 弱版 ⟹ 目标公式。反之不必然（弱版只要求最小层紧）。
> 强版若为假，弱版仍可能为真 —— 这正是 D42 的情形（$\rho=1$ 不紧，但 $\rho^*=0$）。

---

## 3. 已证特例

### 3.1 $\rho^*=0$

**命题**：若存在 $\mathcal V\subseteq\mathcal J$ 是解且 $\supseteq\operatorname{row}(L_0)$，则 $L_0$ 本身是解，$q_{\min}=r$。

**证明**：$\operatorname{row}(L_0)\subseteq\mathcal J\Rightarrow L_0A\in\mathcal J$？不完全 —— 用 $\mathcal V$：
$K_0A\subseteq \mathcal VA\subseteq \mathcal V+\mathcal J=\mathcal J$（因 $\mathcal V\subseteq\mathcal J$）。
于是 $(5a)$ 对 $L_0$ 成立；又 $L_0N=0$ 退化 $\Rightarrow(5b)$ 自动（$\lambda L_0-L_0A\in\mathcal J$，$[\cdot;CA;C]$ 行空间 $=\mathcal J$）。∎

### 3.2 $\rho^*=\dim V$

**命题**：$q_{\min}\le\dim V+1$（构造），且 $\rho=\dim V$ 可达。故该层 $q=\dim V+1=\rho+1$。

依据：§21 两步构造 + §29 的 $\dim B\le p$（$\operatorname{row}(\mathcal L N)=V$）。

### 3.3 $\rho^*=\rho_0>0$

只有精确验证（D33 24/24 + D42 审计），**无证明**。已知的必要条件是 $W_0$ 化归（D36）：

$$\rho=\rho_0\ \text{可达}\iff\exists\ \text{解其所有行都在}\ W_0=\{x:xN\in\operatorname{row}(L_0N)\}\ \text{内}.$$

---

## 4. 证明计划

### 4.1 先分情形：$r$ 与 $\rho+1$ 的大小

$$q=\max(r,\rho+1)=\begin{cases}r, & r\ge\rho+1\\ \rho+1, & r\le\rho+1\end{cases}$$

- **$r\ge\rho+1$**：$q=r$ 要求 $\operatorname{row}(\mathcal L)=\operatorname{row}(L_0)$（因 $q=r$ 且 $\supseteq$），
  即 $L_0$ 本身是解。这强制 $\rho=\rho_0$。所以这个分支只可能出现在 $\rho^*=\rho_0$，
  且断言变成"$\rho_0$ 可达 $\Rightarrow L_0$ 是解"，需要**另证**（目前只有验证）。
- **$r\le\rho+1$**：这是主战场，$q=\rho+1$。

### 4.2 主战场：构造 $q=\rho+1$ 的解

给定任意解 $\mathcal V$（$\dim=q_0$，$\operatorname{rank}(\mathcal V N)=\rho$），要造 $\mathcal V'$：

$$\dim\mathcal V'=\rho+1,\quad \mathcal V'\supseteq\operatorname{row}(L_0),\quad
\mathcal V'A\subseteq\mathcal V'+\mathcal J,\quad \operatorname{rank}(\mathcal V'N)=\rho,\quad (5b).$$

**两个抓手**：

1. **$(5b)$ 是开条件**：对 $\mathcal V'$ 一般位置成立（维数计数：坏集的余维 $\ge1$）。
   真正的约束是 $(5a)$。
2. **线性引理**（已证）：$\forall v\in V\ \exists\ell:\ \ell N=v,\ \ell R_0=0$。
   它保证"前 $\dim V$ 行可以做到 $LR_0=0$"，把 $(5b)$ 化成 $\ker(\lambda M-MA')=\ker M$。

### 4.3 压缩：精确判据（2026-10-24 晚，本轮结果）

设 $\mathcal V$ 是解，$\dim=q$，$\rho=\dim(\mathcal V|_K)$，$K_0=\operatorname{row}(L_0)$，$\mathcal W=\mathcal V\cap\mathcal J$。
把 $\mathcal V^*$ 用"在基 $\mathcal V_1,\dots,\mathcal V_q$ 上的取值"表示，定义

$$\boxed{\ F:=\operatorname{span}\big\{(\langle\mathcal V_i,y\rangle)_{i=1}^q:\ y\in K+AK\big\}\subseteq\mathcal V^*\ }$$

（这是所有 $\Phi_\lambda(\xi)=\langle\cdot,(\lambda I-A)N\xi\rangle|_{\mathcal V}$ 的张成。）

**引理 4.3（可压的充分条件）**：若 $K_0^\perp\not\subseteq F$ **且** $\mathcal W\not\subseteq K_0$，则存在 $\mathcal V$ 的超平面 $H\supseteq K_0$、
$H+\mathcal W=\mathcal V$，且 $H$ 是解。

*证明大意*：$(5a)$ 自动（$H+\mathcal W=\mathcal V\Rightarrow\pi(H)=\pi(\mathcal V)$ 不变）；
$(5b)$ 中 $\ker M'=\ker M$；$H$ 坏 $\iff H=\ker\Phi_\lambda(\xi)$，而坏集 $\subseteq P(F\cap K_0^\perp)$，
是 $P(K_0^\perp)$ 的真闭子集；可容许的 $H$ 在 $P(K_0^\perp)$ 中开稠，故存在好 $H$。$\blacksquare$

> ⚠️ **复核时发现的前提**：可容许的 $H$（$H\supseteq K_0$ 且 $H+\mathcal W=\mathcal V$）**可能为空**。
> 若 $\mathcal W\subseteq K_0$，则任何 $H\supseteq K_0$ 都含 $\mathcal W$，于是 $H+\mathcal W=H\ne\mathcal V$ —— 超平面压缩根本不存在。
> 实测：`middle_layer`（$q{=}2$）与 `refute`（$q{=}1$）的 $W\subseteq K_0$ 成立（不过它们都是紧层，不需要压缩）。
> 所以引理必须加 $\mathcal W\not\subseteq K_0$；**下降算法在 $\mathcal W\subseteq K_0$ 时不能压缩**（但它的输出仍经检查，安全）。

**但压缩不一定在 $\mathcal V$ 内。** 反例（`counterexample_refute_dimV1` 的 $q{=}3,\rho{=}1$ 解）：

$$\dim F=2,\quad \dim K_0^\perp=2,\quad F\cap K_0^\perp=K_0^\perp
\ \Longrightarrow\ \text{引理条件不成立}.$$

而该实例确有 $q{=}2$ 的解 —— 但它**不在这个 $\mathcal V$ 里**（$\rho$ 从 1 降到 0，$\mathcal V'\subseteq\mathcal J$）。

$$\boxed{\ \text{"在给定解内下降"不是正确路线；压缩必须写成\textbf{全局}形式。}}$$

工具：[`tests/cp_check.py`](../tests/verify/cp_check.py)（判定 $K_0^\perp\not\subseteq F$ 并显式构造 $H$）。

### 4.4 正确的 CP 形式

$$\textbf{CP（全局）}:\quad \text{若存在解}\ \mathcal V\ (\dim q,\ \operatorname{rank}\rho),\ \text{则存在解}\ \mathcal V'\ (\text{不必}\subseteq\mathcal V)\ \text{使}$$
$$\dim\mathcal V'=\max(r,\rho+1),\qquad \operatorname{rank}(\mathcal V'N)\le\rho.$$

只有全局形式才能推出弱引理（最小解可能不在给定解内）。

**当前状态**：未证。已知：

- 引理 4.3 给出一类可压缩情形（但 refute 实例不满足）；
- refute 实例说明压缩有时必须降低 $\rho$、离开 $\mathcal V$；
- 尚未找到 CP 的反例，也未有证明。

### 4.5 局部下降算法：它恰好只解出顶层

由引理 4.3 可直接写出一个多项式算法：

```
输入：解 V
while K0^⊥ ⊄ F(V):
    f ← K0^⊥ \ F(V);   V ← ker f        # 维数减 1
输出：V（满足 K0^⊥ ⊆ F）
```

每步都是纯线性代数（$O(n^3)$），维数严格下降，所以终止且多项式。

**关键观察**：每步取的是超平面 $H$，而引理 4.3 的构造要求 $H+\mathcal W=\mathcal V$，
即 $\pi(H)=\pi(\mathcal V)$：

$$\boxed{\ \text{下降保持}\ \rho=\dim(\mathcal V|_K)\ \text{不变}\ }$$

$$\Longrightarrow\quad \text{下降停留在\textbf{起始层}}\ \rho_{\mathrm{start}}\ \text{内，只能给出}\ q(\rho_{\mathrm{start}}).$$

**实验**（[`tests/descent_algorithm.py`](../tests/verify/descent_algorithm.py)，5 个证书实例）：

| 实例 | 初始 $(q,\rho)$ | 下降后 | $q(\rho_{\mathrm{start}})$ | $\rho^*$ | 命中 $q_{\min}$ |
|---|---|---|---|---|---|
| `refute_dimV1` | 2, **0** | **1** | 1 | 0 | ✅ |
| `candidate` | 3, 2 | **3** | 3 | 2 | ✅ |
| `d4` | 3, 2 | **3** | 3 | 2 | ✅ |
| `middle_layer` | 3, **2** | 3 | 3 | **1** | ❌ |
| `rhostar_lt_dimV` | 3, **2** | 3 | 3 | **1** | ❌ |

结论：

$$\boxed{\ \text{下降命中}\ q_{\min}\iff \rho_{\mathrm{start}}=\rho^*\ }$$

失败的恰好是那两个初始层 $\rho=2$、而 $\rho^*=1$ 的中间层实例
（注意 refute 能成功，是因为它构造出的初始解恰好落在 $\rho=0$ 层）。

**所以剩余问题被精确地压缩成一个动作**：

$$\boxed{\ \text{如何到达}\ \rho^*\ \text{层（把}\ \rho\ \text{降 1 且保持是解）？}\ }$$

这正是中间层证书做的事（$q{=}3,\rho{=}2\ \to\ q{=}2,\rho{=}1$），但目前没有构造性办法 ——
它需要 $\bar{\mathcal V}$ 的 $A$-不变子空间，而实数域上不一定存在。

### 4.6 拆中间层证书：两个解互不包含

对 `certificate_middle_layer.json`（$n{=}6$）做结构对比：

| | $V_2$（证书） | $V_3$（搜到的顶层解） |
|---|---|---|
| $\dim$ | 2 | 3 |
| $\rho$ | 1 | 2 |
| $\dim(V\cap\mathcal J)$ | 1 | 1 |
| $K_0^\perp\subseteq F$（局部极小判据）| ✅ | ✅ |

$$\dim(V_2+V_3)=4,\qquad \dim(V_2\cap V_3)=1,\qquad V_2\not\subseteq V_3,\ V_3\not\subseteq V_2 .$$

$$\boxed{\ \text{两个解互不包含，且\textbf{都}满足局部极小判据}\ }$$

推论（重要）：

1. **"降 $\rho$"不是子空间操作** —— 它必须另起一个与 $V_3$ 横截的解，不能靠"在 $V_3$ 里找"。
2. **$K_0^\perp\subseteq F$ 只是"层内极小"的判据**，不是全局极小；$V_2$ 与 $V_3$ 都满足它，
   但 $q_{\min}=2<3$。
3. 所以下降算法 + 局部判据**不可能**单独解决 q1；必须有独立的"构造 $\rho-1$ 层解"的方法。

### 4.7 $\rho=1$ 层的完全刻画（$q=2$）

这是目前唯一能完整写出的一层。设 $\operatorname{rank}(LN)=1$，$M=LN=uv^{\mathsf T}$（$u\in\mathbb R^2\setminus0$，$v\in\mathbb R^d\setminus0$）。

$$\boxed{\ \textbf{定理（}\rho=1\textbf{）}:\quad (5b)\iff \exists\, y\in\mathbb R^2\setminus\operatorname{span}\{u\}:\quad
LN=uv^{\mathsf T},\quad LR_0=-u\,(A'^{\mathsf T}v)^{\mathsf T}+y\,v^{\mathsf T}\ }$$

配合 $(5a)$ 即为解。（$q=2$、$\rho=1$ 时 $q=\rho+1$，是紧层。）

*证明*：$\ker M=v^\perp$。取 $z\not\parallel u$，写 $N'\xi=a(\xi)u+b(\xi)z$。
$(5b)$ 要求：
- $\xi\in v^\perp$：$N'\xi=-u\,(w^{\mathsf T}\xi)$，$w=A'^{\mathsf T}v$；
- $\xi\notin v^\perp$：对一切 $\lambda$ 有 $\lambda(v^{\mathsf T}\xi)u-w^{\mathsf T}\xi\,u-N'\xi\ne0$，
  这迫使 $b(\xi)\ne0$，即 $b=c\,v^{\mathsf T}$（$c\ne0$）。

合并即得 $LR_0=-u w^{\mathsf T}+(cu+cz)v^{\mathsf T}$，其中 $y:=cu+cz\notin\operatorname{span}\{u\}$。$\blacksquare$

**验证**（[`tests/rho1_characterization.py`](../tests/rho1/rho1_characterization.py)）：

| 实例 | $M=uv^{\mathsf T}$ | C1: $b\propto v$ | C2: $(N'+uw^{\mathsf T})$ 行 $\propto v$ |
|---|---|---|---|
| `middle_layer`（$v=(1,-2)$）| ✅ | ✅ ($c=-1/3$) | ✅ |
| `rhostar`（$v=(0,1)$）| ✅ | ✅ | ✅ |

**为什么这有用**：固定 $(u,v)$ 后，定理里的方程**对 $L$ 是线性的**（$y$ 自由，只需 $y\notin\operatorname{span}u$ 这个开条件）。
所以 $\rho=1$ 层的存在性化归为：

$$\exists\,(u,v):\quad \text{线性方程组}\ L[N,R_0]=\big[uv^{\mathsf T},\,-u(A'^{\mathsf T}v)^{\mathsf T}+y v^{\mathsf T}\big]\ \text{有解，且}\ y\notin\operatorname{span}u .$$

参数空间是 $P^1\times P^{d-1}$（$d=2$ 时是二维的），这是下一步要压成多项式的地方。

### 4.8 判定器：参数空间其实塌缩成一次线性方程组

关键补充：$L_0$ 自己的数据就定出了 $v$。

$$L_0N=u_1v^{\mathsf T}\ \Longrightarrow\ \begin{cases}
\alpha_0:=L_0N\neq0: & v\propto\alpha_0,\ \text{取}\ u_1=1;\\
\alpha_0=0: & u_1=0,\ u=(0,1);\ \text{此时第一行给}\ L_0R_0=y_1v^{\mathsf T},
\end{cases}$$

所以 $\alpha_0=0$ 时 $v\propto L_0R_0$（若 $L_0R_0=0$ 则**无解**）。于是没有参数搜索：

$$\text{情形 1（}\rho_0=1\text{）}:\quad \ell N=t\,v,\quad \ell R_0=-t\,w^{\mathsf T}+y_2v^{\mathsf T};\qquad
\text{情形 2（}\rho_0=0\text{）}:\quad \ell N=v,\quad \ell R_0=-w^{\mathsf T}+y_2v^{\mathsf T},$$

$w=vA'$，对 $(\ell,t,y_2)$ **线性**；外加开条件 $y=(y_1,y_2)\notin\operatorname{span}\{u\}$。

**验证**（[`tests/rho1_solver.py`](../tests/rho1/rho1_solver.py)）：

| 实例 | 判定 | 与已知真值 |
|---|---|---|
| `middle_layer` | ✅ 构造 $q{=}2,\rho{=}1$ | 一致（真值 2）|
| `rhostar` | ✅ 构造 $q{=}2,\rho{=}1$ | 一致（真值 2）|
| `refute` | 无解（$\alpha_0{=}0,L_0R_0{=}0$）| 一致（真值 $q(1)=3$，已证）|
| `candidate` / `d4` | 无解 | 一致（$q_{\min}=3$）|

定向随机实例（$\rho_0=0$，13 个可行）：判定器 5 次给出构造，**全部经 c164 可信基线独立复核通过**；
其中 3 个是随机搜索漏掉的（搜索 $\ne$ 不存在）。普通随机实例 5/5 一致。

**状态**：sound —— True 必有构造解且经精确复核；False 的完备性依赖 §4.7 的定理，
加上 $(5a)$ 在自由参数上的抽样（唯一缺口）。

$$\boxed{\ q(1)\ \text{的紧判定是多项式的，而且比随机搜索强}\ }$$

于是各层的可判定性：

| 层 | 判定 | 复杂度 |
|---|---|---|
| $\rho^*=0$ | $L_0$ 本身是解 | 多项式 |
| $\rho^*=1$ | §4.8 判定器 | 多项式 |
| $\rho^*=\dim V$ | 构造 | 多项式 |
| $2\le\rho<\dim V$ | ❌ 未解 | — |

### 4.9 一般 $\rho=k$：铅笔化简（$k=1$ 为什么特殊）

对任意解 $L$，令 $M=LN=UV^{\mathsf T}$（$U$ 为 $q\times k$ 满列秩，$V$ 为 $d\times k$ 满列秩），
$W=A'^{\mathsf T}V$。在 $V^\perp$ 上用 $(5b)$ 得 $LR_0=-UW^{\mathsf T}+YV^{\mathsf T}$（$Y$ 唯一），于是

$$\lambda M-MA'-N'=\big(\lambda U-Y\big)V^{\mathsf T}\ \Longrightarrow\
\boxed{\ (5b)\iff \operatorname{rank}(\lambda U-Y)=k\ \ \forall\lambda\ }$$

即 **$k$ 列的铅笔 $(\lambda U-Y)$ 没有实广义特征值**。

$$\boxed{\ k=1:\ \text{条件} = y\notin\operatorname{span}\{u\}\ (\text{线性});\qquad k\ge2:\ \text{真正的广义特征值条件}}$$

这解释了为什么 $\rho=1$ 能被完全解出：**一维的"span"就是整个空间**，所以"线不经过零"退化成
一个线性不等式；$k\ge2$ 时它才是真的谱条件。

**验证**（[`tests/rho_k_structure.py`](../tests/scans/rho_k_structure.py)）：

| 实例 | $q$ | $k$ | $d$ | $LR_0=-UW^{\mathsf T}+YV^{\mathsf T}$ | $\operatorname{rank}(\lambda U-Y)=k$ |
|---|---|---|---|---|---|
| `candidate` | 3 | 2 | 3 | ✅ | ✅ |
| `d4` | 3 | 2 | 4 | ✅ | ✅ |
| `middle_layer` | 2 | 1 | 2 | ✅ | ✅ |
| `rhostar` | 2 | 1 | 2 | ✅ | ✅ |

**意义**：问题从 $n$ 维原数据化简为 **$k$ 列**的铅笔（$k\le\dim V\le d$，通常远小于 $n$）。
这是真正的降维；但 $k\ge2$ 的判定仍需在 $(U,V,Y)$ 上处理，不能像 $k=1$ 那样塌缩成一次线性方程组。

**$k=2$ 的谱是通有的**：在 `candidate` 与 `d4`（$q{=}3,k{=}2$）上算三个 $2\times2$ 子式的 gcd：

$$\gcd\{2\times2\ \text{子式}\}=1\quad\Longrightarrow\quad\text{铅笔无有限广义特征值}.$$

所以 $k=2$ 的谱条件是**余维 1 的坏集**、通有满足；真正卡住的是 $(5a)$ 与线性系统的耦合，
而不是谱条件本身。$k=1$ 的优势在于条件是**线性**的，不在于它稀少。

### 4.10 $k=2$：$V$ 不被线性结构钉住（负结果）

$k=1$ 时 $L_0$ 的数据把 $v$ 定死。$k=2$ 时 $V$ 是含 $\alpha_0$ 的 2-平面（$d\ge3$ 时是连续族）。
实验（[`tests/k2_V_scan.py`](../tests/rho2_middle/k2_V_scan.py)，`candidate`，$d=3$）：

$$V(t)=\operatorname{span}\{\alpha_0,\ \beta(t)\},\quad t\in\{-2,-1,0,1,2,\pm\tfrac12\}.$$

结果：线性系统 $(LU^\top$ 约束$)$ 对**所有** $t$ 都可解。

$$\boxed{\ k=1\ \text{的"由 }L_0\text{ 定死 }v\text{"不推广；}k=2\text{ 的 }V\text{ 有连续族，线性系统不区分它们}\ }$$

所以 $k\ge2$ 的判定必须引入 $(5a)$（或另一个判别式），不能靠线性塌缩。
这与 §4.6 的"两个解互不包含"一致：**跨层的自由度本质上不是线性的**。

> ⚠️ **修正**：下面 §4.11 证明 $(5a)$ 其实是**自动**的。本节的实验结论仍然正确
> （线性系统对连续多个 $V$ 可解），但"必须引入 $(5a)$"是错的 —— 真正钉住 $V$ 的是**谱条件**。

### 4.11 $(5a)$ 是自动的（重要简化）

这个结论要修正上一段：**$(5a)$ 根本不用单独检查**，它由结构方程自动成立。

$$\boxed{\ \text{若}\ LN=UV^{\mathsf T},\ LR_0=-UW^{\mathsf T}+YV^{\mathsf T}\ (U\ \text{列满秩},\ W=A'^{\mathsf T}V),\ \text{则}\ (5a)\ \text{自动成立}\ }$$

*证明*：$(5a)\iff\ker L\cap K\subseteq\ker(LA)$。取 $x=N\xi\in\ker L\cap K$：
$0=Lx=(LN)\xi=UV^{\mathsf T}\xi\Rightarrow V^{\mathsf T}\xi=0$（$U$ 列满秩），于是

$$LAx=L(AN)\xi=L(NA'+R_0)\xi=(LN)A'\xi+(LR_0)\xi
=UW^{\mathsf T}\xi-UW^{\mathsf T}\xi+YV^{\mathsf T}\xi=0 .\ \blacksquare$$

**实验印证**（[`tests/k2_V_scan.py`](../tests/rho2_middle/k2_V_scan.py)，`candidate`，7 个 $t$）：结构方程的解**全部**满足 $(5a)$；
而 $(5b)$ 只在 $t{=}0$ 成立：

| $t$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $\pm\tfrac12$ |
|---|---|---|---|---|---|---|
| $(5a)$ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| $(5b)$ gcd | 2 | 2 | **0** | 2 | 2 | 2 |

$$\boxed{\ \text{所以 }V\text{ 确实被钉住 —— 但钉住它的不是线性方程，而是\textbf{谱条件}}\ }$$

于是 $k\ge2$ 的判定被精确地描述为：

$$\exists\,V:\quad \text{线性系统有解，且解空间含一个"铅笔无实特征值"的点}.$$

不再是"还要满足 $(5a)$"，而是纯粹的"线性系统 + 谱条件"。

### 4.12 与 Z-形式（Q1-TRUE 的交接）的对偶

Q1-TRUE 方向给出的 Z-FORM（见 [`Q1_TRUE_HANDOFF.md`](../../../archive/handovers/Q1_TRUE_HANDOFF.md)）：

$$q_{\min}=n-p-d_{\max},\quad d_{\max}=\max\dim Z:\ Z\subseteq\ker C\cap L_0^\perp,\ A(Z\cap K)\subseteq Z,\ \text{(8c)} .$$

两个形式通过 $Z=\ker[C;L]$ 对应，$\dim Z=n-p-q$，且

$$\boxed{\ \dim(Z\cap K)=d-\rho\ }$$

（4 个证书全部验证）。所以两边说的"中间层"是同一件事。

**修正**：Z-FORM 的 (8c) 原文缺了一个核维数项，正确的是

$$\dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)-\dim\ker\big((\lambda I-A)|_K\big)\quad\forall\lambda .$$

否则在 $\lambda$ 为 $A|_K$ 的特征值时会假失败（`d4` 在 $\lambda=5,3$ 处）。

**结构不对称点**：$(5a)$ 在 V-形式里自动（§4.11），而 $A(Z\cap K)\subseteq Z$ 在 Z-形式里不是自动的
——这是两边"缺口"不同的原因。

### 4.13 实特征值强迫 $Z$ 与 $K$ 相交

用修正后的谱条件（§4.12）：

$$\dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)-\dim\ker\big((\lambda I-A)|_K\big).$$

若 $Z\cap K=0$，左端 $\ge0$、右端 $=-k_\lambda$，故必须有 $k_\lambda=0$ 对所有 $\lambda$ 成立：

$$\boxed{\ Z\cap K=0\ \Longrightarrow\ A|_K\ \text{没有实特征值}\ }$$

$$\text{等价地：}\quad A'\ \text{有实特征值}\ \Longrightarrow\ Z\cap K\ne0 .$$

**验证**：`candidate`/`d4`/`middle_layer`/`refute` 的 $A'$ 都有实特征值（$3,1,-1$ / $5,3,1,-1$ /
$\lambda^2$ 判别式 $>0$ / $10/7$），而它们全部满足 $\dim(Z\cap K)=d-\rho>0$ ✓。

**意义**：这解释了 Z-FORM 里 $(8c)$ 为什么是"真正的约束"——它不是一般位置条件，
而是被 $A'$ 的实谱**强迫**与 $K$ 耦合的条件。$k=1$ 时能解出来，正是因为
"$\dim(Z\cap K)>0$" 只剩一个方向可挑。

### 4.14 $k=1$ 时 $\Sigma$ 由 $L_0$ 唯一确定（定理）

设 $q=2$、$k=1$（即 $M=LN=uv^{\mathsf T}$，$u\in\mathbb R^2$，$v\in\mathbb R^d$ 非零），且存在解。则

$$\boxed{\ \begin{cases}\alpha_0=L_0N\ne0: & v\propto\alpha_0;\\
\alpha_0=0: & L_0R_0\ne0\ \text{且}\ v\propto L_0R_0;\\
\alpha_0=0\ \text{且}\ L_0R_0=0: & \text{无解}.\end{cases}}$$

*证明*：$M=LN=uv^{\mathsf T}$ 的第一行给 $\alpha_0=u_1v$。若 $\alpha_0=0$，则 $u_1=0$；
于是 $LR_0=-uw^{\mathsf T}+yv^{\mathsf T}$ 的第一行给 $L_0R_0=y_1v$。
而 $(5b)$ 要求 $y\notin\operatorname{span}u$，此处 $u=(0,u_2)$，故 $y_1\ne0$，
所以 $v\propto L_0R_0\ne0$。$\blacksquare$

**推论**：$k=1$ 时该层**只有一个候选** $\Sigma=\operatorname{span}\{v\}$。

$$\text{所以 }q(1)=\max(r,2)\iff\text{该唯一候选上的线性系统有解（且 }y\notin\operatorname{span}u\text{）}.$$

这正是 D47 判定器；"$v$ 被 $L_0$ 定死"不是巧合，而是**定理**。

**验证**：`refute`（$\alpha_0{=}0,L_0R_0{=}0$，故无 $k{=}1$ 解 —— 与 $q(1){=}3$ 一致）；
`middle_layer`（$\alpha_0{=}0,L_0R_0{=}(-\tfrac13,\tfrac23)$，$\Sigma$ 唯一）；
`rhostar`（$\alpha_0{=}(0,-\tfrac{11}5)$，$\Sigma$ 唯一）。

### 4.15 行 1 约束的一般形式（含 $k\ge2$）

对任意解 $L$，$M=LN=UV^{\mathsf T}$（$U$ 列满秩，$V$ 为 $d\times k$），记 $\Sigma=\operatorname{row}(V^{\mathsf T})\subseteq\mathbb R^d$（$\dim=k$）。则

$$\boxed{\ \beta:=L_0R_0+A'^{\mathsf T}\alpha_0=\big(y_1\big)^{\mathsf T}V^{\mathsf T}\ \in\ \Sigma\ }$$

其中 $y_1$ 是 $Y$ 的第一行。*证明*：$M$ 的第一行给 $\alpha_0=(u_1)^{\mathsf T}V^{\mathsf T}$；$N'$ 的第一行给
$L_0R_0=-(u_1)^{\mathsf T}W^{\mathsf T}+(y_1)^{\mathsf T}V^{\mathsf T}$，而 $W^{\mathsf T}=V^{\mathsf T}A'$，
故 $(u_1)^{\mathsf T}W^{\mathsf T}=\alpha_0^{\mathsf T}A'=(A'^{\mathsf T}\alpha_0)^{\mathsf T}$。$\blacksquare$

**推论**：

- $k=1$：$\Sigma=\operatorname{span}\{v\}$ 且 $\beta\in\Sigma$，即 $v\propto\beta$（若 $\beta\ne0$）——正是 §4.14；
- $k=2$：若 $\beta\not\propto\alpha_0$，则 $\Sigma=\operatorname{span}\{\alpha_0,\beta\}$ **唯一**，层内无搜索自由度。

**通有性**：随机实例（$\rho_0{=}1,d{=}3$）中 $11/11$ 满足 $\beta\not\propto\alpha_0$；
而实例 C/d4 恰是退化的（$L_0R_0{=}0$ 且 $\alpha_0$ 是 $A'$ 的特征向量，故 $\beta\propto\alpha_0$）。

**但钉住 $\Sigma$ 不等于有解**：对 45 个非退化实例（$\dim V{=}3,d{=}3,\rho_0{=}1$），
用唯一的 $\Sigma$ 解线性系统并抽样（要求 $\operatorname{rank}U{=}2$、$\operatorname{rank}L{=}3$、$\gcd=1$）：

$$\boxed{\ \text{45 个里 }q{=}3,\rho{=}2\ \text{的解：0 个（与随机搜索 45/45 一致）}\ }$$

（注：若漏掉 $\operatorname{rank}U=2$ 的检查，会误报"命中"——退化点 $\operatorname{rank}(LN){=}1$ 也能通过 $\gcd$ 检查，
但那时 $(5a)$ 不再自动、解也不是 $k{=}2$ 层。）

### 4.16 铅笔的显式公式

由 §2.3，$(\lambda U-Y)V^{\mathsf T}=P_\lambda:=\lambda M-MA'-N'$，且 $V^{\mathsf T}$ 行满秩。
取 $V^{\mathsf T}$ 的任一右逆 $(V^{\mathsf T})^{+}$（$V^{\mathsf T}(V^{\mathsf T})^{+}=I_k$），则

$$\boxed{\ \lambda U-Y=P_\lambda\,(V^{\mathsf T})^{+}=L(\lambda N-AN)\,(V^{\mathsf T})^{+}\ }$$

（用了 $P_\lambda=L(\lambda N-AN)$，因 $R_0=AN-NA'$。）

**推论**：铅笔只通过 $P_\lambda=L(\lambda N-AN)$ 依赖 $L$。

**两个经验事实**（$k{=}2$，$d{=}3$，6 个非退化实例）：

1. $\gcd_{\mathbb Q(s)[\lambda]}$ 的**系数不含 $s$**（$6/6$）。所以仿射族里每个点都有相同公共根——
   "全好/全坏"在这些情形下是**证明**，不是抽样；
2. $\gcd$ 的根**不是** $\operatorname{spec}(A')$ 的子集。例如某实例 $\gcd$ 的根为 $\{-1.89,\,1.35\}$，
   而 $\operatorname{spec}(A')=\{0.70,\,-1.35\pm0.27i\}$。所以"—继承 $A'$ 特征值"只在部分实例
   （如实例 C）成立，**不是普遍机制**。

$$\text{待解释：为什么 }\gcd\ \text{与 }s\ \text{无关？}$$

---

## 5. 什么会推翻目标公式

$$\exists\ (A,C,L_0):\quad q(\rho^*)>\max(r,\rho^*+1).$$

已知不可能的情形：$\rho^*=0$（§3.1）。
必须满足：$\rho^*\ge1$，且该层不紧。

**搜索约束**（写脚本时必须显式检查）：

1. $L=[L_0;R]$ 字面前缀；
2. $(5a)$、$(5b)$ 用精确 gcd（$\lambda$ 采样只作拒绝器）；
3. $\operatorname{rank}(\mathcal L N)=\rho^*$ 恰好，不是 $\le$；
4. 必须证明下界（不能只报告"搜索没找到更小的"）。

---

## 6. 状态表

| 项 | 状态 | 位置 |
|---|---|---|
| $\rho^*=0$ 层 | ✅ 已证 | 本文 §3.1 |
| $\rho^*=\dim V$ 层 | ✅ 已证 | §3.2 + LEMMA_LIFT §21/§29 |
| $\rho^*=\rho_0>0$ 层 | 🟡 34/34 | 本文 §3.3 |
| 中间层紧性 | ❌ 开放 | — |
| 引理 4.3（可压充分条件）| 🟡 已推导，未数值正例 | §4.3 |
| CP（全局）| ❌ 未证；refute 实例说明"内部下降"不成立 | §4.4 |
| 公式在 $r\ge2$ 上的检验 | ✅ 20/20（seed 21/22，2026-10-24 晚）| `archive/process_logs/` |
