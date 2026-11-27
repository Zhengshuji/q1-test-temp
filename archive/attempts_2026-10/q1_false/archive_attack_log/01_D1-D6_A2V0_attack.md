> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 攻击日志 · D1–D6（拆分自 ATTACK_LOG.md）

> 原文：`archive/attack_A2V0/ATTACK_LOG.md`。

## D1：定向构造反例

### D1.1 设想

$V_0$ 的大小由 $\dim[L;CA;C]$ 决定：

$$\dim V_0\ \ge\ n-(q+2p)$$

要 $V_0\ne0$，需要 $q+2p<n$。所以**小 $q$、大 $n$** 是反例最可能出现的地方。

之前搜过 $q\in[r,\min(n,r+2)]$（§42、§44），但那偏向**大** $q$ ✓。现在专门搜**小** $q$。

### D1.2 做法

- $n\in\{5,6,7\}$，$p=1$
- $q$ 从 $r$ 开始（$L_0$ 的行数）到 $r+1$
- 要求 $(5a)\wedge(5b)$
- 检查 $A^2V_0\subseteq V_0$

### D1.3 结果（2026-10-23 22:05）

```
随机实例 400 个（n∈{5,6,7}, p=1, q∈{r, r+1}）
其中满足 (5a)∧(5b) 的解：5 个
A²V₀ ⊄ V₀ 的：0
```

**结论**：✗ **没找到反例**，但样本太少（5 个）。

**原因**：小 $q$ 几乎总让 $(5a)$ 失败 —— 因为 $(5a)$ 需要 $\operatorname{row}(\mathcal LN)\supseteq V$，
即 $q\ge
ho\ge\dim V$。所以"小 $q$"与"可行"基本互斥。

**教训**：反例若要存在，必须是"$q$ 足够大（满足 $(5a)$）但 $\dim V_0$ 仍非零"的**夹缝实例**。

### D1.4 改进的搜索策略

$$	ext{需要}:\quad q+2p<n\quad	ext{（使 }V_0
e0	ext{）}\quad	extbf{且}\quad q\ge\dim V\quad	ext{（使 }(5a)	ext{ 可能）}$$

$$\Longrightarrow\quad \dim V+2p<n$$

所以反例必须满足：**$V$ 小（小 $
ho$）但 $n$ 大** ✓ —— 也就是说 $A$ 的"闭包"很小 ✓。

**这是下一步要定向构造的结构** ⏭

### D1.5 🚨 假阳性事件（重要教训）

用**采样 $\lambda\in\{0,\pm1\}$** 的快检，我找到一个"反例"：
$$n=6,\ p=1,\ q=1,\ \dim V=2,\ \dim V_0=3,\ A^2V_0
ot\subseteq V_0$$

**但用精确的 `cond5b`（子式 gcd）验证**：
```
cond5a = True
cond5b = 1        # 1 = gcd 的次数 1 ≠ 0 ⟹ (5b) 失败!
```

$$\boxed{\ 	ext{这不是反例 —— }(5b)\ 	ext{不成立};\ 	ext{采样 3 个 }\lambda\ 	ext{会漏掉非}\lambda\in\{0,\pm1\}	ext{ 的零点}\ }$$

**教训（加入纪律）**：

> **验证 $(5b)$ 必须用精确的 gcd，绝不能用有限个 $\lambda$ 采样。**

（此前 §42、§44 的"快检"都有这个隐患 ⚠️ —— 它们的结论需要用精确算法重验。）

### D1.6 精确搜索（用 cond5b）

```
候选实例（dimV+2p<n）：8 个
其中满足 (5a)∧(5b) 的解：0 个
```

**结论**：夹缝实例极少同时满足两个条件 ✓ —— 无法在此判定引理真假 ✗

**新认识**：$(5b)$ 是**极强**的条件 ✓，它几乎"锁死"了 $\mathcal L$ 的结构 ✓。这反而支持引理为**真** ✓。

---

## D2：多项式版

### D2.1 设想

$$(5b)\iff\gcd\{\rho\text{ 阶子式}(\lambda L-LA;CA;C)\}=1$$

子式都是 $\lambda$ 的多项式，次数 $\le\rank L$。可以**显式展开**，然后利用 gcd 条件做多项式消元。

### D2.2 做法

（待填）

---

## D3–D6

（待填）


---

## D1.7 精确重验（关键完整性检查）

用**精确 gcd** 重验真实解：

| 实例 | $(5a)$ | $(5b)$ | $\dim V_0$ | $A^2V_0
ot\subseteq V_0$ |
|---|---|---|---|---|
| `cand` | ✓ | ✓ | 1 | **0** ✓ |
| `d4` | ✓ | ✓ | 2 | **0** ✓ |
| `p2` | ✓ | ✓ | 2 | **0** ✓ |
| `2010` | ✗（$L_0$ 只有 2 行，$(5a)$ 不成立）| ✓ | — | 跳过 |
| c163-0/1/2 | ✓ | ✓ | 0 | **0** ✓ |

$$\boxed{\ \text{全部真解满足 }A^2V_0\subseteq V_0\ ✓\ }$$

### ⚠️ 完整性警告

§42（5749 个解）、§44（2197/2293 个解）用的是**采样 $\lambda\in\{0,\pm1\}$ 的快检** ✗ ——
那些"解"里可能混有**非解**（如 D1.5 的假阳性）✓

$$\boxed{\ \text{所以那些计数是\textbf{上界}，不是精确值；需要重做才能作为论文证据}}$$

**已用精确算法确认的**：
- 3 个反例证书 ✓
- 3 个 c163 构造 ✓
- 6 个目标实例 ✓

$$\Longrightarrow\ \text{核心结论（}A^2V_0\subseteq V_0\text{）在\textbf{全部精确验证的实例}上成立}\ ✓$$


---

## D2/D5 联合尝试（2026-10-23 22:45）

### 尝试：对"堆叠深度"归纳 + 精确随机验证

想用 $V_0^{(k)}:=\ker[L;CA;\ldots;CA^{k-1};C]$ 做归纳，先要一个**精确**的随机基线。

### 结果

```
精确随机验证（n∈{4,5}, p=1, q∈{dimV, dimV+1}）：
  试了 476 个 L
  精确满足 (5a)∧(5b) 的：224 个
  其中 V₀=0 的：全部 224 个      ← 平凡
  A²V₀ ⊄ V₀ 的：0 个
```

$$\boxed{\ \text{小 }n\text{ 时 }V_0\ \text{恒为 }0\text{ —— 断言平凡成立，无信息量}}$$

### 关键结构性观察 ⭐

$$V_0\ne0\ \text{需要}\ q+2p<n;\qquad (5a)\ \text{需要}\ q\ge\rho$$

$$\Longrightarrow\quad\boxed{\ \rho+2p\ <\ n\ }$$

**这就是"夹缝"的精确条件** ✓ —— 而三个反例证书恰好满足：

| 实例 | $n$ | $\rho$ | $p$ | $\rho+2p$ | $V_0\ne0$? |
|---|---|---|---|---|---|
| `cand` | 6 | 2 | 1 | 4 | ✓（dim 1）|
| `d4` | 6 | 2 | 1 | 4 | ✓（dim 2）|
| `p2` | 8 | 2 | 2 | 6 | ✓（dim 2）|

$$\Longrightarrow\ \text{真正需要检验的实例	extbf{必然}\"n\text{ 大、}\rho\text{ 小}"} \;\Longrightarrow\ \text{随机搜索几乎打不中} \;✗$$

### 教训

$$\text{"}\rho+2p<n\text{" 是采样极难命中的余维条件 —— 与本项目此前的教训（第 2 条纪律）一致}$$

**所以 D1（构造反例）应当改成"定向构造 \rho 小、n 大的实例"，而不是随机搜索。**


---

## D1.8 ✅ 定向构造成功：$\rho=0$、$\dim V_0=5$ 的非平凡验证

### 构造方法

取 $A$ 使 $A(K)\subseteq K$（$K=\ker[C;CA]$）—— 最简单的做法是 $A=NBN^{\mathsf T}$（像在 $K$ 内）。

$$\Longrightarrow\quad R_0=AN-NA'=0\ \Longrightarrow\ S=0\ \Longrightarrow\ \rho=0$$

$$\text{定理预测}:\quad q_{\min}=0+1=1$$

### 结果（精确 gcd 验证）

| 实例 | $\rho$ | $q$ | $\dim V_0$ | $A^2V_0\not\subseteq V_0$ |
|---|---|---|---|---|
| 构造 1 | 0 | 1 | **5** | **0** ✓ |
| 构造 2 | 0 | 1 | **5** | **0** ✓ |
| 构造 3 | 0 | 1 | **5** | **0** ✓ |

$$\boxed{\ \dim V_0=5\ \text{的非平凡情形下，}A^2V_0\subseteq V_0\ \text{仍成立}\ ✓\ }$$

### 为什么这重要

之前所有非平凡验证都受限于 $\dim V_0\le2$（三个证书）。现在有了 $\dim V_0=5$ 的族 ✓ ——
**断言的证据强度显著提高** ✓

### 这类实例为什么"显然"成立（不是证明，但给出直觉）

$$A(K)\subseteq K\ \Longrightarrow\ A^2(V_0)\subseteq A^2(K)\subseteq K$$

$$\text{而}\ A^2V_0\subseteq V_0\ \text{还需要}\ L(A^2v)=0,\ CA(A^2v)=0,\ C(A^2v)=0$$

$$\text{后三者由}\ (5b)\ \text{的迭代使用推出（此处未证，但数值全对）}$$


---

## D1.9 ✅ 部分证明：$\rho=0$ 族里 $A^2V_0\subseteq\ker[CA;C]$ 已证

### 命题

$$\text{若}\ A(K)\subseteq K\ (K=\ker[C;CA])\ \text{且}\ v\in V_0=\ker[L;CA;C],\ \text{则}\ A^2v\in\ker[CA;C]$$

### 证明

$$V_0\subseteq K\ \text{且}\ A(K)\subseteq K\ \Longrightarrow\ A^2v\in K\subseteq\ker C$$

$$\Longrightarrow\ C(A^2v)=0\ ✓$$

$$\text{又}\ A(A^2v)\in A(K)\subseteq K\subseteq\ker(CA)\ \Longrightarrow\ CA(A^2v)=0\ ✓$$

$$\Longrightarrow\ \boxed{\ A^2V_0\subseteq\ker[CA;C]\ }\qquad\blacksquare$$

### 剩余

$$\text{还差}\ L(A^2v)=0\ ✗$$

**这是唯一需要 $(5b)$ 的地方** —— 因为 $L$ 是"观测行"，$(5b)$ 是它的唯一约束 ✓

### 价值

| 项 | 状态 |
|---|---|
| $C(A^2v)=0$ | ✅ **已证**（$\rho=0$ 族）|
| $CA(A^2v)=0$ | ✅ **已证**（$\rho=0$ 族）|
| $L(A^2v)=0$ | ✗ 待证 |

$$\Longrightarrow\ \text{三分之二已证};\ \text{剩下的纯粹是 }L\ \text{与 }(5b)\ \text{的关系}$$


---

## D1.10 ✅ 更强：$\rho=0$ 族里 $V_0$ 是 $A$-不变

### 精确检验（$\rho=0$ 族，$A=NBN^{\mathsf T}$）

| 检验 | 精确解数 | 违例 |
|---|---|---|
| $A(V_0)\not\subseteq V_0$ | 6 | **0** ✓ |
| $A^2(V_0)\not\subseteq V_0$ | 6 | **0** ✓ |

$$\boxed{\ A(V_0)\subseteq V_0\ }\qquad(\text{比 }A^2\text{-不变更强})$$

### 推论

$$A(V_0)\subseteq V_0\ \Longrightarrow\ A^2V_0\subseteq V_0\ \Longrightarrow\ L(A^2v)=0\ ✓\ (V_0\subseteq\ker L)$$

$$\boxed{\ \rho=0\ \text{族的断言数值上完全成立}\ ✓\ }$$

### 证明仍差的一步

$$A(V_0)\subseteq\ker L\ ✓\quad(\text{由 }(5b))\qquad A(V_0)\subseteq\ker C\ ✓\quad(\text{自动})$$
$$\text{还差}\quad A(V_0)\subseteq\ker(CA)\ ✗$$

**这又是一次"循环"**：$A(V_0)\subseteq\ker(CA)\iff CA^2V_0=0$ —— 正是要证的 ✓

### 现状总结（本方向 D1）

| 子目标 | 状态 |
|---|---|
| 找反例 | ❌ 未找到（精确验证 + 定向构造）|
| $\rho=0$ 族：$C(A^2v)=0$ | ✅ 已证 |
| $\rho=0$ 族：$CA(A^2v)=0$ | ✅ 已证 |
| $\rho=0$ 族：$L(A^2v)=0$ | ✅ **数值 6/6**（$A$-不变性）；✗ 未证 |
| 一般 $\rho$ | ✗ 未处理 |


---

## D6：Rosenbrock system matrix / 弱不可观子空间（2026-10-23 23:10）

### 6.1 从 Trentelman 书 Ch. 7 提取到的

$$P_\Sigma(s)=\begin{pmatrix}sI-A&-B\\ C&D\end{pmatrix}\quad\text{（system matrix）}$$

$$\text{"weakly unobservable subspace" 与 "strongly reachable subspace" 是 conditioned invariant 的推广}$$
$$\text{"system transmission polynomials and zeros 可由 weakly unobservable subspace 解释"}$$

### 6.2 标准事实（$B=0$，无输入）

$$\mathcal W:=\bigcap_{k\ge0}\ker(CA^k)\ \text{（不可观子空间）}$$

$$\boxed{\ A\mathcal W\subseteq\mathcal W\ }\quad\text{（标准，直接验证：}CA^k(Ax)=CA^{k+1}x=0\text{）}$$

### 6.3 为什么不能直接用

$$V_0=\ker[L;CA;C]\ \ne\ \mathcal W=\ker[C;CA;CA^2;\ldots]$$

$$\text{差别：}V_0\ \text{只用 }CA\ \text{一层；}\mathcal W\ \text{用所有层}$$

$$\Longrightarrow\ A\text{-不变性不能直接搬（}V_0\not\subseteq A^{-1}V_0\ \text{一般）}$$

$$\Longrightarrow\ \textbf{这正是断言 }A^2\text{-不变（而非 }A\text{-不变）的原因}\ ✓$$

### 6.4 新的思路（本节产出）

$$\text{若把 }V_0\ \text{"加厚"成 }\mathcal W:\text{ hmm——但 }\mathcal W\ \text{依赖所有层，不是有限对象}$$

$$\text{替代：}\ V_0^{(k)}:=\ker[L;CA;C;CA^2;\ldots;CA^k]\ \text{（有限层）}$$

$$\text{则 }V_0^{(k)}\ \text{随 }k\ \text{递减，且 }\mathcal W=\bigcap_k V_0^{(k)}$$

**观察**：$V_0^{(1)}=\ker[L;CA;C]=V_0$ ✓；$V_0^{(2)}=\ker[L;CA;C;CA^2]$ hmm

$$\text{断言 }A^2V_0\subseteq V_0\ \text{等价于}\ A^2V_0\subseteq\ker[L;CA;C]\ \text{—— 不是"加厚"能直接给的}$$

### 6.5 D6 结论

$$\boxed{\ \text{D6 给出的是\textbf{标准的 }A\text{-不变性}，但我们的 }V_0\ \text{是截断版，}\"加厚"路线不通}\ ✗}$$

**新收获**：确认了 $V_0$ 与标准对象（$\mathcal W$）的**本质差别**就是在"层数"上 ✓ ——
而断言说：**只差一层时，$A^2$-不变性仍然成立** ✓ —— 这更像一个"两层补偿一层"的现象 ✓


---

## D6.6 🎯 一般形式成立：层数补偿的定量版本

### 命题（一般形式）

$$\boxed{\ A^{k+1}V_0^{(k)}\subseteq V_0^{(k)},\qquad V_0^{(k)}:=\ker[L;CA;\ldots;CA^k]\ }$$

### 验证（三个精确证书）

| 实例 | $k=1$ | $k=2$ | $k=3$ |
|---|---|---|---|
| `cand` | ✓（dim 1）| ✓ | ✓ |
| `d4` | ✓（dim 2）| ✓ | ✓ |
| `p2` | ✓（dim 2）| ✓ | ✓ |

$$\boxed{\ \text{全部通过}\ ✓\ }$$

### 意义

$$k=1:\quad A^2V_0\subseteq V_0\quad(\textbf{我们的断言})$$
$$k\to\infty:\quad A\mathcal W\subseteq\mathcal W\quad(\textbf{标准事实})$$

$$\Longrightarrow\ \text{它\textbf{插值}于两者之间 —— 是一个定量的"未观测深度加倍"定理}$$

### 等价改写（"深度加倍"）

$$v\in V_0^{(k)}\ \text{即}\ CA^mv=0\ (m=0..k)\ \Longrightarrow\ CA^mv=0\ \text{对}\ m=k+1..2k+1$$

$$\boxed{\ \textbf{若前 }k+1\ \text{层不可观测，则接下来 }k+1\ \text{层也不可观测}}$$

### 为什么这是好形式

| 优点 | 说明 |
|---|---|
| **可归纳** | $k\to k+1$ 可能有干净递推 |
| **包含已知** | $k\to\infty$ 退化为标准结论 |
| **定量** | 给出"深度加倍"的精确倍数 |
| **可证伪** | 每个 $k$ 都是有限检查 |

### 证明待做

$$\text{需要}:\quad CA^{k+1+j}v=0\ (j=0..k)\ \text{从}\ CA^mv=0\ (m=0..k)\ \text{推出}$$

**关键难点**：需要跨越 $k+1$ 到 $2k+1$ 的"空档" ✓ —— 而 $(5b)$ 只直接给 $A^mv$ 的 $L$-部分 ✓


---

## D6.7 一般形式的扩大验证（14 个实例）

| 族 | 测试 | 通过 | 违例 |
|---|---|---|---|
| 三个精确证书 | 3 | 3 ✓ | 0 |
| c163 构造的解 | 10 | 10 ✓ | 0 |
| $\rho=0$ 族 | 1 | 1 ✓ | 0 |
| **合计** | **14** | **14** ✓ | **0** |

$$\boxed{\ A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}\quad(k=1,2,3)\ \text{全部成立}\ ✓\ }$$

### 归纳证明的尝试（失败）

$$\text{想从}\ A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}\ \text{推}\ A^{k+2}V_0^{(k+1)}\subseteq V_0^{(k+1)}$$

$$V_0^{(k+1)}\subseteq V_0^{(k)}\ \Longrightarrow\ A^{k+1}V_0^{(k+1)}\subseteq A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}\ ✓$$

$$\text{但需要}\ \subseteq V_0^{(k+1)}\ \text{—— 还差一层 } \ker(CA^{k+1})\ ✗$$

$$\boxed{\ \text{普通的归纳不通：每一步都需要"再加一层"，而}\ (5b)\ \text{只提供一层}}$$

### 可能的正确路线

$$\text{也许应当反过来}:\quad \text{固定 } k,\ \text{直接算 } A^{k+1}\ \text{在 } V_0^{(k)}\ \text{上的作用}$$

$$\text{或用 }(5b)\ \text{的} \lambda\text{-族：对每个 }\lambda,\ (\lambda L-LA)\ \text{在 } V_0^{(k)}\ \text{上的作用都有约束}$$


---

## D6.8 🚨 关键负面结果：纯 $(A,C)$ 版本是**假**的

### 检验

$$A^{k+1}\ker[C;CA;\ldots;CA^k]\subseteq\ker[C;CA;\ldots;CA^k]\ ?$$

| 测试 | 违例 |
|---|---|
| 68 个（实例, $k$）组合 | **68** ✗ |

$$\boxed{\ \text{纯 }(A,C)\ \text{版本\textbf{完全不成立}（68/68 违例）}}$$

### 为什么这很重要

$$\text{它说明}:\quad \text{"层数加倍"}\ \textbf{不是}\ (A,C)\ \text{的性质，而是}\ (5b)\ \text{的推论}\ ✓$$

$$\Longrightarrow\ \text{断言 }A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}\ \text{是\textbf{真正关于 }}\mathcal L\ \text{的定理}$$

而 $L$ 的唯一约束就是 $(5b)$ ✓ ——
$$\boxed{\ \text{所以证明必须、也只能从 }(5b)\ \text{出发（不能用 }A,C\ \text{的通用性质）}}$$

### 这把搜索空间大幅缩小

| 之前试过的（都不可能行）| 现在知道为什么 |
|---|---|
| $A$ 保持 $\operatorname{col}(N)$ | 与 $(5b)$ 无关 |
| $A(\ker L\cap\ker C)\subseteq\ker(CA)$ | 同上 |
| 纯 $(A,C)$ 的层数论证 | **本节：68/68 违例** |
| 标准不可观子空间的 $A$-不变性 | 那是 $\mathcal W$（无限层），我们只有有限层 |

$$\Longrightarrow\ \text{唯一可用的工具是 }(5b)\ \text{本身}$$


---

## D6.9 ✅✅ 两个真定理（已证）

### 定理 A：$(5b)$ 的行空间等价

$$(5b)\iff\ker[\lambda L-LA;CA;C]=\ker[L;CA;C]\ \forall\lambda$$
$$\iff\boxed{\ \operatorname{row}[\lambda L-LA;CA;C]=\operatorname{row}[L;CA;C]\ \ \forall\lambda\ }$$

*证明*：$\ker X=\ker Y\iff(\operatorname{row}X)^\perp=(\operatorname{row}Y)^\perp\iff\operatorname{row}X=\operatorname{row}Y$ ∎

$$\text{等价地}:\quad \lambda L-LA\ \in\ \operatorname{row}[L;CA;C]\qquad\forall\lambda$$

$$\text{取 }\lambda=0:\quad \boxed{\ LA\ \in\ \operatorname{row}[L;CA;C]\ }$$

### 定理 B：迭代行空间关系（归纳证明）

$$\boxed{\ LA^k\in\operatorname{row}[L;CA;\ldots;CA^k]\qquad\forall k\ge1\ }$$

*证明*（归纳）：

- **基** $k=1$：定理 A 在 $\lambda=0$ 给出 ✓
- **步**：设 $LA^k=\sum_i c_i r_i$，$r_i\in\{L,CA,\ldots,CA^k\}$。则
$$LA^{k+1}=\sum_i c_i\,(r_iA)$$
而 $r_iA\in\{LA,CA^2,\ldots,CA^{k+1}\}$，且 $LA\in\operatorname{row}[L;CA;C]$ ✓
$$\Longrightarrow\ LA^{k+1}\in\operatorname{row}[L;CA;\ldots;CA^{k+1}]\qquad\blacksquare$$

**数值验证**：`cand`、`d4`、`p2` 的 $k=1,2,3$ 全部 ✓

### 与目标的关系（差一层）

目标：$A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}$，需要
$$LA^{k+1}\in\operatorname{row}[L;CA;\ldots;CA^{\mathbf{k}}]\quad(\text{注意：}k\text{ 层，不是 }k+1)$$

而定理 B 只给 $LA^{k+1}\in\operatorname{row}[L;CA;\ldots;CA^{k+1}]$ —— **多了一层** ✗

$$\boxed{\ \text{定理 B 与目标之间\textbf{恰好差一层} —— 这就是全部困难所在}}$$

$$\text{若能把定理 B 加强为}\ LA^k\in\operatorname{row}[L;CA;\ldots;CA^{k-1}]\ (k\ge1)，\text{则目标立即成立}$$


---

## D6.10 🎯 目标的精确等价形式（加强版）

### 等价

$$A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}\iff LA^{k+1}\ \text{annihilates}\ V_0^{(k)}\iff LA^{k+1}\in\operatorname{row}[L;CA;\ldots;CA^k]$$

$$\text{令 }j:=k+1:\quad\boxed{\ LA^j\in\operatorname{row}[L;CA;\ldots;CA^{j-1}]\qquad(j\ge2)\ }$$

### 数值验证

| 实例 | $j=1$ | $j=2$ | $j=3$ |
|---|---|---|---|
| `cand` | ✓ | ✓ | ✓ |
| `d4` | ✓ | ✓ | ✓ |
| `p2` | **✗** | ✓ | ✓ |

$$\boxed{\ j\ge2\ \text{全部成立}\ ✓;\quad j=1\ \text{可能失败}}$$

$$\text{这正好对应：目标从 }k=1\ \text{开始（即 }j=2\text{），所以 }j=1\ \text{的失败不影响}\ ✓$$

### 与定理 B 的对照（差一层）

| 断言 | 状态 |
|---|---|
| $LA^j\in\operatorname{row}[L;CA;\ldots;CA^{j}]$（定理 B）| ✅ **已证** |
| $LA^j\in\operatorname{row}[L;CA;\ldots;CA^{j-1}]$（目标所需）| 🟡 **$j\ge2$ 数值 3/3；未证** |

$$\boxed{\ \text{全部困难 = 从定理 B 去掉最上面那一层 }CA^j}$$

### 为什么那一层可能是"多余"的

$$CA^j\ \text{的系数在迭代中来自 }LA\ \text{被 }A\ \text{作用 }j-1\ \text{次}$$

$$\text{而 }LA\in\operatorname{row}[L;CA;C]\ \text{（定理 A）—— 其中 }C\ \text{那一项被 }A\ \text{作用后变成 }CA，\text{不是 }CA^j$$

$$\Longrightarrow\ \text{系数的"层数"可能不会累加到 }j\ \text{层，而是更低}$$

**这是下一步要精确化的：迭代时记录系数的"层数"。**


---

## D6.11 本方向收束（2026-10-23 23:30）

### 已证（两个）

$$\textbf{定理 A}:\ (5b)\iff\operatorname{row}[\lambda L-LA;CA;C]=\operatorname{row}[L;CA;C]\ \forall\lambda\iff LA\in\operatorname{row}[L;CA;C]$$

$$\textbf{定理 B}:\ LA^k\in\operatorname{row}[L;CA;\ldots;CA^k]\quad\forall k\ge1$$

### 目标的精确等价

$$A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}\iff LA^{k+1}\in\operatorname{row}[L;CA;\ldots;CA^k]$$

$$\text{数值}:\ j=2,3\ \text{在 3 个证书上全部成立}\ ✓$$

### 全部困难 = 去掉最上一层

$$\text{定理 B 给}\ \operatorname{row}[L;CA;\ldots;CA^{j}]；\text{需要}\ \operatorname{row}[L;CA;\ldots;CA^{j-1}]$$

### 显式迭代（说明 $CA^j$ 系数从哪来）

$$LA=XL+YCA+ZC\quad(\text{定理 A 的矩阵版})$$

$$LA^2=X(LA)+Y(CA^2)+Z(CA)=(X^2)L+(XY+Z)CA+(XZ)C+Y\,CA^2$$

$$\text{所以}:\ LA^2\in\operatorname{row}[L;CA;C]\iff Y\,CA^2\in\operatorname{row}[L;CA;C]$$

$$\boxed{\ \text{核心问题}：\textbf{$Y\,CA^2$ 的像是否被 }\operatorname{row}[L;CA;C]\ \text{吸收}}$$

（$Y$ 是 $LA$ 在 $CA$ 方向上的系数，来自 $(5b)$ 的行关系）

### 本方向的净收获

| 项 | 状态 |
|---|---|
| 定理 A（行空间等价）| ✅ **已证** |
| 定理 B（迭代关系）| ✅ **已证** |
| 目标 ⟺ 去掉一层 | ✅ 已精确化 |
| 去掉一层 | 🟡 数值 3/3，**未证** |
| 显式迭代结构 | ✅ 已写出（$Y\,CA^2$ 项）|

$$\boxed{\ \text{下一步唯一目标}：\text{证明 }Y\,CA^2\in\operatorname{row}[L;CA;C]\ \text{（或等价的 }LA^2\in\operatorname{row}[L;CA;C]）}$$


---

## D6.12 显式系数计算（2026-10-24 00:20）

### 结果

| 实例 | $LA=XL+YCA+ZC$ 重构 | $Y\cdot CA^2\in\operatorname{row}[L;CA;C]$ | $LA^2\in\operatorname{row}[L;CA;C]$ |
|---|---|---|---|
| `cand` | ✓ | ✓ | ✓ |
| `d4` | ✓ | ✓ | ✓ |
| `p2` | ✓ | ✓ | ✓ |

$$\boxed{\ \text{显式系数 }X,Y,Z\ \text{可解，且 }YCA^2\ \text{的归属成立}\ }$$

### 结构

$$LA^2=X(LA)+Y(CA^2)+Z(CA)=(X^2)L+(XY+Z)CA+(XZ)C+Y\,CA^2$$

$$\text{所以}\ LA^2\in\operatorname{row}[L;CA;C]\iff Y\,CA^2\in\operatorname{row}[L;CA;C]\ \checkmark\ (\text{数值 3/3})$$

### 未使用的资源

$$(5b)\ \text{给的是 }\lambda\text{-族}:\quad \lambda L-LA\in\operatorname{row}[L;CA;C]\quad\forall\lambda$$

$$\text{我只用了 }\lambda=0\ (\text{得 }LA=XL+YCA+ZC)\ ✗$$

$$\boxed{\ \text{下一步}:\text{用上整个 }\lambda\text{-族（尤其是 }\lambda\to\infty\ \text{或两个 }\lambda\ \text{的比较）}}$$

### 可能的用法

$$\lambda L-LA\in R:=\operatorname{row}[L;CA;C]\quad\forall\lambda$$
$$\Longrightarrow\ L\in R\ (\text{除 }\lambda);\quad LA\in R$$
$$\Longrightarrow\ \text{对 }\lambda_1\ne\lambda_2:\ (\lambda_1L-LA)-(\lambda_2L-LA)=(\lambda_1-\lambda_2)L\in R\ (\text{平凡})$$

$$\text{—— 一阶信息已用尽；需要 }\textbf{二阶}\text{信息（如 }LA^2\text{）}$$

$$\text{而 }LA^2\ \text{并不直接出现在 }(5b)\ \text{中}\ ✗$$

$$\boxed{\ \text{所以必须"从 }(5b)\ \text{推出" }LA^2\ \text{的信息 —— 这正是未解决的核心}}$$


---

## 附录：诚实定位 —— 这两个结果到底"新"在哪

### 定理 A 的实质

$$(5b)\iff\operatorname{row}[\lambda L-LA;CA;C]=\operatorname{row}[L;CA;C]\ \forall\lambda$$

**"新"的程度**：⚠️ **这是初等引理，不是新定理**

- 依据是标准事实 $\ker X=\ker Y\iff\operatorname{row}X=\operatorname{row}Y$（任何线性代数教材）
- 真正有用的是**推论**：$LA\in\operatorname{row}[L;CA;C]$

$$\boxed{\ \text{应当称它为"引理"而非"定理"，且不主张原创性}}$$

### 定理 B 的实质

$$LA^k\in\operatorname{row}[L;CA;\ldots;CA^k]$$

**"新"的程度**：⚠️ **由引理 A 归纳即得，是推论**

- 归纳只用 $LA\in\operatorname{row}[L;CA;C]$
- 无技术难度

$$\boxed{\ \text{同样是"引理"，不是"定理"}}$$

### 真正的贡献 vs 不是贡献的

| 项 | 是否贡献 |
|---|---|
| $q_{\min}=\dim V+1$ 的**下界**（Lean）| ✅ 是（若最终成立）|
| 6 个结构性引理（$N^{\mathsf T}R_0=0$、$S'=S$、$\dim B\le p$、$q\ge\rho+1$、线性引理）| ✅ 大多是真正需要的中间步骤 |
| **引理 A、引理 B**（本节）| ⚠️ **初等整理，不是新数学** |
| $A^2V_0\subseteq V_0$ / $Y\,CA^2\in\operatorname{row}[L;CA;C]$ | ✅ **这才是唯一可能的新数学**（若证出）|

$$\boxed{\ \text{所以：不要声称 A、B 是"新定理"；它们是\textbf{把问题化简的工具}}}$$


---

