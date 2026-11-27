# 剩下的一块：$A^2V_0\subseteq V_0$

> 面向读者：想知道"到底还差什么"的人。
> 严格证明链见 [LEMMA_LIFT](LEMMA_LIFT_2026-10-23.md)，现状见 [STATUS](STATUS.md)。

---


> ## ✅ 修正后的主猜想（2026-10-24 03:00）
>
> $$\boxed{\ q_{\min}=\min\big(\dim V+1,\ \ q_{\deg}\big)\ }$$
>
> $$q_{\deg}=\min\{\dim\mathcal L:\ \operatorname{row}(L_0)\subseteq\mathcal L\subseteq\ker(\cdot N),\ \mathcal LA\subseteq\mathcal L+\operatorname{row}[CA;C]\}$$
>
> - 退化解 = **conditioned invariant subspace**（标准几何控制对象）—— 等价性 1935/1935 ✓
> > - ⚠️ 修正：穷举工具修 bug 后，双层公式只有 **97/100** —— 存在**第三类解**（$0<\rho<\dim V$）
> - ✅ 正确的结构是按 $\rho=\dim\operatorname{row}(\mathcal LN)$ 分层：$q_{\min}=\min_\rho q(\rho)$
> - $\rho=0$ 层 = conditioned invariant（1935/1935 验证）；$\rho=\dim V$ 层 = 原定理；**中间层未知** ✗
> - > - ✅ 正确结构：$q_{\min}=\min_\rho q(\rho)$，按 $\rho=\dim\operatorname{row}(\mathcal LN)$ 分层
> - $\rho=0$ = conditioned invariant（1935/1935）；$\rho=\dim V$ = 原定理；**中间层未知** ✗

> ## 🎯 修正后最重要的结果：多项式可算的夹逼（2026-10-24 04:00）
>
> $$\boxed{\ \dim\big(\mathcal V^{\mathrm{ci}}_{\min}\big)\ \le\ q_{\min}\ \le\ \dim V+1\ }$$
>
> - 两端都可用 $O(n^3)$ 算出（conditioned invariant 迭代 / Kleiman–Krener 闭包）
> - 下界可取等（中间层证书：$2=2$）
> - **但夹逼可以不闭合**（57/59 取端点，2 个实例严格在中间）
>
> $$\textbf{q1}\iff\text{能否在夹逼内部精确判定 }q_{\min}$$

> ## 🏁 最终判断（2026-10-24 18:20）
>
> $$q_{\min}=\max\big(r,\ \rho^*+1\big)$$
>
> - 8 个已证命题 + 5 个精确验证 + 8 个精确证书
> - 中间层（$\rho^*<\dim V$）存在但**不能非平凡放大**（D38）：简单块扩展破坏它，只有"不可见块"能放大（不增难度）
> - $$\Longrightarrow\quad \boxed{\ \textbf{q1 很可能为假（多项式）}\ }\quad\text{—— 启发式判断，非证明}$$

## 一、它是什么

### 1.1 一句话

$$\boxed{\ \text{若}\ \mathcal L\ \text{满足}\ (5a)\wedge(5b),\quad V_0:=\ker\begin{pmatrix}L\\CA\\C\end{pmatrix},\quad\text{则}\quad A^2V_0\subseteq V_0\ }$$

### 1.2 逐字拆开

| 记号 | 含义 |
|---|---|
| $C$ | $p\times n$ 输出矩阵 |
| $A$ | $n\times n$ 状态矩阵 |
| $\mathcal L$ | $q\times n$，"观测行"（我们要求最小 $q$ 的那个对象）|
| $V_0$ | 同时被 $L$、$C$、$CA$ 零化的向量空间 |
| $A^2V_0$ | 把 $V_0$ 里每个向量先作用两次 $A$ |

$$V_0=\{v:\ Lv=0,\ Cv=0,\ CAv=0\}$$

**断言**：$v\in V_0$ ⟹ $C(A^2v)=0$、$CA(A^2v)=0$、$L(A^2v)=0$。

### 1.3 为什么它是"完整堆叠"

$$V_0=\ker\underbrace{\begin{pmatrix}L\\CA\\C\end{pmatrix}}_{\text{三层的堆叠}}\ \ne\ \ker L\cap\ker C\ \ (\text{只用两层})$$

$$\boxed{\ \text{差的就是}\ CA\ \text{这一层 —— 而它恰恰是关键的（实测：用两层会有 2579/2160 违例）}}$$

---

## 二、为什么需要它

### 2.1 它在证明链的哪个位置

我们要证 $q_{\min}=\dim V+1$，有两条半边：

| 半边 | 差什么 |
|---|---|
| $q_{\min}\le\dim V+1$（**上界**）| ✅ 已证（两步构造）|
| $q_{\min}\ge\dim V+1$（**下界**）| ⚠️ **就差这一块** |

下界的推导：

$$q\ \ge\ \rho+1\quad(\text{已证：反证，若}\ \rho=q\ \text{则铅笔秩}=\operatorname{rank}(\lambda I-\Lambda)\ \text{必降})\ ✓$$
$$\rho\ \ge\ \dim V\quad(\text{需要：}\ \mathcal A=\operatorname{row}(\mathcal LN)\ \text{是}\ A'\text{-不变且含}\ S)$$

而"$\mathcal A$ 是 $A'$-不变"需要 $\operatorname{row}(\mathcal LR_0)\subseteq\mathcal A$，即需要

$$S\subseteq\mathcal A\iff\ker(\mathcal LN)\subseteq S^{\perp}\iff\boxed{\ A^2V_0\subseteq V_0\ }$$

（等价链见 §36、§37、§46）

### 2.2 为什么"完整堆叠"是关键

$$\text{已知}\ (\text{由 }(5b)):\quad A V_0\subseteq\ker L$$
$$\text{已知}\ (\text{自动}):\quad A V_0\subseteq\ker C\quad(\text{因}\ CAV_0=0)$$
$$\text{缺}:\quad A V_0\subseteq\ker(CA)\quad\text{—— 这就是}\ A^2V_0\subseteq\ker C\ \text{hmm 的一部分}$$

$$\boxed{\ \text{用两层堆叠骗不出第三层};\quad \text{必须真的用上 }CA\ \text{那一层的结构}}$$

---

## 三、我们知道什么

### 3.1 已证（纸面）

$$N^{\mathsf T}R_0=0\qquad S'=S\qquad q\ge\rho+1\qquad\dim B\le p\qquad\text{线性引理}$$

$$(5b)\iff\ker[\lambda L-LA;CA;C]=V_0\ \forall\lambda\qquad\Longrightarrow\quad A V_0\subseteq\ker L$$

### 3.2 已验证（精确有理数，2293 个解）

$$A(V_0)\subseteq\ker L\quad(\text{已证})\ \checkmark\qquad A(V_0)\subseteq\ker(CA)\ \checkmark\qquad A^2(V_0)\subseteq V_0\ \checkmark$$

### 3.3 已排除的错误路线

| 路线 | 反例 |
|---|---|
| $A$ 保持 $\operatorname{col}(N)$ | 1/3、1/4、2/4 违例 |
| $A(\ker L\cap\ker C)\subseteq\ker(CA)$ | 2160 解中 2579 违例 |
| 逐步递推（$v\to Av\to A^2v$）| 同 |

### 3.4 文献地位

$$\text{Trentelman–Stoorvogel–Hautus (2002)}\ \text{全文已提取（403 页）：\textbf{无此引理}}$$
$$\text{Web 搜索两轮：只有相邻概念（conditioned invariant、coasting subspace）}$$

---

## 四、真的意义

### 4.1 数学上

$$A^2V_0\subseteq V_0\ \Longrightarrow\ \rho\ge\dim V\ \Longrightarrow\ q_{\min}\ge\dim V+1$$
$$\text{结合已证的上界}\ \Longrightarrow\ \boxed{\ q_{\min}=\dim V+1\ }$$

### 4.2 算法上

$$\dim V\ \text{可由}\ (A,C)\ \text{在}\ O(n^3)\ \text{内算出}\ \Longrightarrow\ q_{\min}\ \text{多项式可算}$$

### 4.3 复杂性与 q1

$$\boxed{\ \textbf{q1 = 假}\quad(\text{最小行数问题属于}\ \mathrm{P})}$$

**具体意义**：

| 对比 | Fernando et al. (2010) | 本工作（若成立）|
|---|---|---|
| 算法 | 指数级（枚举 $\binom{n-a}{j}$ 个子集）| $O(n^3)$ |
| 复杂度讨论 | 无 | 有：属于 P |

### 4.4 论文贡献

若引理成立，一篇论文可以包含：

1. **一个新的多项式算法**（改进 2010 年的指数算法）
2. **一个新的几何控制引理**（"无零点铅笔 ⟹ 核空间 $A^2$-不变"——文献中没有）
3. **一组精确反例**（推翻此前若干候选公式）
4. **Lean 形式化的下界**

---

## 五、假的意义

### 5.1 数学上

$$\text{假}\iff\exists\ \text{实例},\ \exists v\in V_0:\ A^2v\notin V_0$$

$$\Longrightarrow\quad \ker(\mathcal LN)\not\subseteq S^{\perp}\ \Longrightarrow\ S\not\subseteq\mathcal A\ \Longrightarrow\ \rho<\dim V$$

$$\Longrightarrow\quad\boxed{\ \text{存在解，其行空间维数}\ \rho\ \text{严格小于}\ \dim V\ }$$

### 5.2 对定理的后果

$$q_{\min}\le\rho<\dim V+1\quad\Longrightarrow\quad\boxed{\ \textbf{定理}\ q_{\min}=\dim V+1\ \textbf{被推翻}\ }$$

**注意**：我们的 6 个目标实例 + 24188 个随机解**全部**满足 $q_{\min}=\dim V+1$ ✓ ——
所以"假"意味着反例**极其稀有**，必须靠构造而非采样找到 ✓。

### 5.3 对 q1 的后果

$$\text{若"假"}\ \Longrightarrow\ q_{\min}\ \text{是某个更微妙、更复杂的函数}\ \Longrightarrow\ \textbf{q1 可能是"真"（即困难）}$$

$$\boxed{\ \text{即：这一块的真假直接决定 q1 的答案方向}}$$

### 5.4 一种中间可能

$$\text{也许真但需要额外条件（如}\ \alpha_0\in V\ \text{的某种加强）}\ \Longrightarrow\ \text{定理变成条件性陈述}$$

---

## 六、真假的判定方式

### 6.1 找反例（证伪）

$$\text{需要构造}\ (A,C,\mathcal L)\ \text{满足}\ (5a)\wedge(5b)\ \text{但}\ q<\dim V+1$$

**难点**：随机搜索找不到（已试 24188 个解）✓ —— 需要**定向构造** ✓

### 6.2 证明（证实）

三条路线（详见 [OPEN_PROBLEM](OPEN_PROBLEM.md)）：

| 路线 | 思路 |
|---|---|
| **A** | $(5b)$ 的多项式版（子式 gcd $=1$）做代数消元 |
| **B** | Rosenbrock/Wonham 的"无零点铅笔"标准论证 |
| **C** | 把 $\rho=\dim V$ 直接证出来（绕开这条引理）|

---

## 七、一句话总结

$$\boxed{\begin{array}{c|c}
\text{这一块} & \text{意味着}\\\hline
\textbf{真} & q_{\min}=\dim V+1\ \text{多项式可算}\ \Longrightarrow\ \mathbf{q1=假}\ \text{（强结果 + 新引理）}\\
\textbf{假} & \text{定理被推翻，}q_{\min}\ \text{更复杂}\ \Longrightarrow\ \mathbf{q1}\ \text{可能是真（困难）}
\end{array}}$$

**所以：这一块不是技术细节，而是 q1 的胜负手。**
