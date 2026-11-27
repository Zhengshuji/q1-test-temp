# 51 — ⭐⭐⭐ **可手算的反例**：c6′ 在 $k\ge1$ 范围也假

> 承接 [history/50](50_boundary_is_invariance.md)。本文给出**最简单、可手算**的见证。

---

## 0. 一句话

$$\boxed{\
\begin{array}{l}
n{=}6,\ p{=}1,\ r{=}1,\ \mathbf{q_0{=}2,\ k{=}1},\ d_{CA}{=}4\ (\textbf{情形 II})\\
C=e_1^{\mathsf T},\quad A\ \text{的前三行}\ =e_2^{\mathsf T},e_3^{\mathsf T},0\ (\text{其余任意})\\
L_0=CA=e_2^{\mathsf T}\ (\textbf{退化}),\quad R=e_3^{\mathsf T},\quad \mathcal L=[e_2^{\mathsf T};e_3^{\mathsf T}]
\end{array}}$$

$$\Longrightarrow\ \textbf{H1–H4}\ \wedge\ \textbf{(5a)}\ \wedge\ \textbf{(5b)}\ \text{全部成立}\qquad(\textbf{14/14 独立验证}\ ✓)$$

$$\Longrightarrow\ \textbf{c6 / c6′}\ \text{在}\ \textbf{退化 + 非不变 + }k{=}1\ \text{时}\ \textbf{假}\ \Longrightarrow\ \textbf{情形 II 可以 YES}$$

---

## 1. ⭐ 手算验证（全部可笔算）

### 1.1 数据

$$A=\begin{pmatrix}
0&1&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&0&0&0\\
1&0&0&1&0&0\\
0&1&0&0&1&0\\
0&0&1&0&0&1
\end{pmatrix},\qquad
C=\begin{pmatrix}1&0&0&0&0&0\end{pmatrix}$$

$$L_0=\begin{pmatrix}0&1&0&0&0&0\end{pmatrix},\qquad
R=\begin{pmatrix}0&0&1&0&0&0\end{pmatrix},\qquad
\mathcal L=\begin{pmatrix}0&1&0&0&0&0\\0&0&1&0&0&0\end{pmatrix}$$

### 1.2 逐步手算

$$\textbf{(1)}\ CA=e_2^{\mathsf T},\ CA^2=e_3^{\mathsf T},\ CA^3=0$$

$$\textbf{(2)}\ K=\ker[C;CA]=\ker[e_1^{\mathsf T};e_2^{\mathsf T}]=\operatorname{span}\{e_3,e_4,e_5,e_6\}\ \Longrightarrow\ \mathbf{d_{CA}=4}$$

$$\textbf{(3)}\ CA^2|_K=e_3^{\mathsf T}|_K=(1,0,0,0)\ne0\ \Longrightarrow\ \textbf{非}\ A\text{-不变}\ ✓$$

$$\textbf{(4)}\ \textbf{退化}：\pi(L_0)=L_0N=e_2^{\mathsf T}N=(0,0,0,0)=0\ ✓$$

$$\textbf{(5)}\ H=\mathcal LN=\begin{pmatrix}0&0&0&0\\1&0&0&0\end{pmatrix}\ \Longrightarrow\ \operatorname{rank}H=1<q_0=2\ \Longrightarrow\ \textbf{T5a}\ ✓$$

$$\textbf{(6)}\ \mathcal LA=\begin{pmatrix}e_2^{\mathsf T}A\\ e_3^{\mathsf T}A\end{pmatrix}=\begin{pmatrix}e_3^{\mathsf T}\\0\end{pmatrix}
\ \Longrightarrow\ F=\mathcal LAN=\begin{pmatrix}1&0&0&0\\0&0&0&0\end{pmatrix}$$

$$\textbf{(7)}\ \operatorname{im}H=\operatorname{span}\{(0,1)\},\quad \operatorname{im}F=\operatorname{span}\{(1,0)\}\ \Longrightarrow\ \textbf{不同直线}\ \Longrightarrow\ \Lambda\ \text{不保持}\ \operatorname{im}H$$
$$\Longrightarrow\ \textbf{(S) 成立}\ \Longrightarrow\ \textbf{(5b) 可成立}\ ✓$$

$$\textbf{(8)}\ \textbf{(5a)}：[\mathcal LA;\mathcal L;CA;C]\ \text{的行}\ =\ e_3^{\mathsf T},0,e_2^{\mathsf T},e_3^{\mathsf T},e_2^{\mathsf T},e_1^{\mathsf T}\ \text{张成}\ \operatorname{span}\{e_1,e_2,e_3\}\ \text{rank}\ 3$$
$$[\mathcal L;CA;C]\ \text{的行}\ =\ e_2^{\mathsf T},e_3^{\mathsf T},e_2^{\mathsf T},e_1^{\mathsf T}\ \text{rank}\ 3\ \Longrightarrow\ \textbf{相等}\ ✓$$

$$\textbf{(9)}\ \textbf{(5b)}：[\lambda\mathcal L-\mathcal LA;CA;C]\ \text{的行}\ =\ \lambda e_2^{\mathsf T}-e_3^{\mathsf T},\ \lambda e_3^{\mathsf T},\ e_2^{\mathsf T},\ e_1^{\mathsf T}$$
$$\text{对任意}\ \lambda：\text{含}\ e_1^{\mathsf T},e_2^{\mathsf T},\ \text{且}\ \lambda e_2^{\mathsf T}-e_3^{\mathsf T}\ \text{恒与它们独立}\ \Longrightarrow\ \operatorname{rank}\equiv3=r_0\ ✓$$

### 1.3 $k=1$ 是**最小**的

$$L_0\ \text{本身}\ (A)：[\mathcal L_0A;\mathcal L_0;CA;C]\ \text{rank} = 3\ne 2 = [\mathcal L_0;CA;C]\ \text{rank}\ \Longrightarrow\ \textbf{失败}$$
$$\text{而}\ \mathcal L=[L_0;R]\ \text{成功}\ \Longrightarrow\ \mathbf{q_0=2,\ k=1}\ ✓\ \text{（**最小增广**）}$$

---

## 2. ⭐ 完全独立验证（`verify_witness2_independent.py`，**14/14**）

| 检验 | 结果 |
|---|---|
| H1 $\operatorname{rank}C=p=1$ | ✅ |
| H2 $\operatorname{rank}L_0=r=1$ | ✅ |
| H3 $\operatorname{rank}[L_0;C]=r+p=2$ | ✅ |
| H4 $\operatorname{row}(O_{L_0})\subseteq\operatorname{row}(O_C)$ | ✅ |
| **(5a)** | ✅ $3=3$ |
| **(5b) 全部 3 个 3 阶子式的 gcd** | ✅ $=\mathbf{1}$（非零常数）|
| (5b) 逐 $\lambda$（8 个有理值）| ✅ 全部 $=3$ |
| 情形 II（$d_{CA}=4\ge q_0=2$）| ✅ |
| T5a（$\operatorname{rank}H=1<2$）| ✅ |
| **退化**（$\pi(L_0)=0$）| ✅ |
| **非 $A$-不变** | ✅ |
| $\operatorname{im}F\not\subseteq\operatorname{im}H$（**机制失效**）| ✅ |

$$\textbf{实现}：\text{不 import 项目任何库（自带 Gauss 消元 / 矩阵乘 / 多项式算术 / 零空间基）} ✓$$

---

## 3. ⭐⭐⭐ 最终结论：**c6′ 全面为假**

$$\begin{array}{c|c|c}
& k=0 & k\ge1\\
\hline
\pi(L_0)\ne0\ (\text{非退化}) & \textbf{假}\ (\text{history/47}) & \text{不可能（定理}\ k{=}0\text{）}\\
\pi(L_0)=0\ (\text{退化}) & \text{可能} & \textbf{假}\ (\textbf{本文}\ !)
\end{array}$$

$$\boxed{\ \textbf{"情形 II 平行}\Longrightarrow\text{NO"}\ \text{在}\ k{=}0\ \text{与}\ k\ge1\ \text{两种情形下}\ \textbf{都有反例}\ }$$

$$\Longrightarrow\ \textbf{情形 II 可以 YES}\ \Longrightarrow\ \textbf{分支 A }\textbf{未被排除}\textbf{为硬度所在}\ ⚠️$$

---

## 4. ⭐ 为什么机制在此失效（清楚）

$$\text{机制（history/45）需要}\ \operatorname{im}F\subseteq\operatorname{im}H\ \Longleftarrow\ CA^2=0\ (\text{使}\ F=H\circ A')$$
$$\text{而本文：}\ CA^2|_K\ne0\ (\textbf{非不变})\ \Longrightarrow\ F\ \text{不是}\ H\circ A'\ \Longrightarrow\ \operatorname{im}F\not\subseteq\operatorname{im}H\ \Longrightarrow\ \text{机制失效}\ ✓$$

$$\textbf{所以}\ \text{c6}'\ \text{的}\ \textbf{全部}（已知）\ \text{证明都依赖}\ A\text{-不变性，而这}\ \textbf{不是问题的假设}\ ⚠️$$

---

## 5. 保留（诚实）

| # | 保留 |
|---|---|
| **1** | 该见证 $k=1$（**最小**非零增广）—— 但仍是**常数** $k$，不建立 NP-hardness |
| **2** | $\operatorname{rank}H=1$，$q_0=2$ —— 最小的情形 |
| **3** | 需**常数** $k$ 的实例族**不**产生 NP-hardness ⟹ **主线的硬度问题仍开放** |
| **4** | 但 **c6′ 作为"情形 II 恒 NO"的依据已被彻底排除** |

$$\Longrightarrow\ \text{正确表述}：\textbf{情形 II 的判定既非恒 NO、亦未建立硬度}\ ——\ \textbf{真正开放}$$

---

## 6. 本会话对 c6′ 的完整轨迹

$$\text{c6（平行}\Rightarrow\text{NO）}\ \xrightarrow{\text{第 20 处}}\ \text{撤回}\ \xrightarrow{\text{c6}'}\ \text{14/14 支持}\ \xrightarrow{\text{history/45–46}}\ \text{只有}\ A\text{-不变时能证}$$
$$\xrightarrow{\text{history/47}}\ k{=}0\ \text{反例}\ \xrightarrow{\text{history/48–49}}\ \text{范围缩到退化}\ \xrightarrow{\text{history/50}}\ \text{分界}=\ A\text{-不变（定理）}$$
$$\xrightarrow{\textbf{本文}}\ \textbf{退化}\ +\ k{=}1\ \textbf{反例}\ \Longrightarrow\ \boxed{\ \textbf{c6}'\ \textbf{全面为假}\ }$$

---

## 7. 教训

$$\boxed{\ \textbf{"14/14 支持"可能是}\ \textbf{14/14 都在一个特殊族}\ \text{—— 必须问"我的实例族有多宽？"}\ ⚠️}$$
$$\text{项目 14/14 全在}\ CA^2=0\ (\text{不变})\ \text{族；一超出该族即见反例}\ ⚠️⚠️$$
$$\boxed{\ \text{而}\ \textbf{机制}（\operatorname{im}F\subseteq\operatorname{im}H）\ \text{暴露了}\ \text{族的}\ \textbf{必要结构}\ ——\ \text{这比数值更有价值}\ ✓}$$

---

## 8. 本轮产出

| 文件 | 内容 |
|---|---|
| **`scripts/core/verify_witness2_independent.py`** ★⭐⭐ | $k{=}1$ 见证的**完全独立验证**（14/14）|
| `scripts/core/c6_open_region.py` | 开放区域的构造与测试（16/16 YES）|
| **`scripts/core/verify_family.py`** ★⭐⭐ | **无穷族**验证（$n=4..10$ 全部 ✓）|
| **本文** | 可手算的反例 + 最终结论 |

---

## 9. ⭐⭐⭐ **无穷族**（$n\ge4$ 全部 YES）

### 9.1 族

$$\forall\, n\ge4:\quad C=e_1^{\mathsf T},\quad A\ \text{前三行}=e_2^{\mathsf T},e_3^{\mathsf T},0\ (\text{其余任取})$$
$$L_0=CA=e_2^{\mathsf T}\ (\text{退化}),\quad R=CA^2=e_3^{\mathsf T},\quad \mathcal L=[e_2^{\mathsf T};e_3^{\mathsf T}]$$

### 9.2 对一般 $n$ 的手算（与 $n$ 无关！）

$$K=\operatorname{span}\{e_3,\dots,e_n\},\quad d_{CA}=n-2$$
$$H=\begin{pmatrix}0&0&\cdots&0\\1&0&\cdots&0\end{pmatrix},\quad F=\begin{pmatrix}1&0&\cdots&0\\0&0&\cdots&0\end{pmatrix}$$
$$\operatorname{im}H=\operatorname{span}\{(0,1)\}\perp\!\!\!\perp\operatorname{im}F=\operatorname{span}\{(1,0)\}$$
$$(5a):\ \operatorname{rank}=3=3\ ;\qquad (5b):\ \operatorname{rank}\equiv3\ \forall\lambda$$
$$q_0=2,\quad k=1\quad(\textbf{最小增广}\ \textbf{恰 1 行})$$

$$\text{情形 II}\iff d_{CA}=n-2\ge2=q_0\iff n\ge4\ \checkmark$$

### 9.3 验证（`verify_family.py`，独立实现）

| $n$ | $d_{CA}$ | (5a) | (5b) | 逐 λ | $\operatorname{rank}H$ | 非不变 | $\operatorname{im}F\not\subseteq\operatorname{im}H$ | H4 |
|---|---|---|---|---|---|---|---|---|
| 4 | 2 | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ |
| 5 | 3 | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ |
| 6 | 4 | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ |
| 7 | 5 | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ |
| 8 | 6 | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ |
| 9 | 7 | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ |
| 10 | 8 | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ |

$$\Longrightarrow\ \textbf{情形 II 的 YES 实例是}\ \textbf{无穷族}\ \text{（不是孤例）}\ ⭐⭐⭐$$

$$\text{并且对每个}\ n：\ |R|_{\min}=1\ \text{（常数）}\ \Longrightarrow\ \textbf{不给出 NP-hardness}\ ;$$
$$\text{但}\ \textbf{彻底排除了"情形 II 恒 NO"}\ \checkmark$$

### 9.4 族的本质（为什么这么简单）

$$\text{族的结构}：A\ \text{在}\ e_1\to e_2\to e_3\to0\ \text{上是"链"},\quad L_0=CA,\ R=CA^2$$
$$\Longrightarrow\ \pi(L_0)=0,\ \pi(L_0A)=e_3^{\mathsf T}|_K\ne0\ \Longrightarrow\ L_0\ \text{单行失败，需}\ 1\ \text{行补足}$$
$$\text{而补足后}\ H\ \text{的第一行仍为}\ 0,\ F\ \text{的两行分居两条不同直线}\ \Longrightarrow\ \Lambda\ \text{无法保持}\ \operatorname{im}H$$
$$\Longrightarrow\ (S)\ \text{必可成立}\ \Longrightarrow\ (5b)\ \text{可满足}\ \checkmark$$

$$\textbf{这就是 c6′ 的}\ \textbf{结构性漏洞}\ ：\text{它默认}\ \operatorname{im}F\subseteq\operatorname{im}H\ \text{（只在}\ A\text{-不变时成立）} ⚠️$$

---

## 10. 最终结论（本会话对 c6′ 的完整答案）

$$\boxed{\ \textbf{c6 / c6′（情形 II 平行 ⟹ NO）在}\ n\ge4\ \text{的}\ \textbf{无穷族}\ \text{上为假}\ }$$

$$\boxed{\ \textbf{情形 II 可以 YES}\ \Longrightarrow\ \textbf{分支 A }\textbf{未被排除}\textbf{为硬度所在}\ }$$

$$\text{而}\ \textbf{主线的硬度问题}\ \text{仍}\ \textbf{开放}\ ：\text{需要"最小}\ |R|\ \text{大且难判定"的实例族}$$
$$\text{—— 上述族的}\ |R|_{\min}=1\ \text{（常数），}\textbf{不足以}\ \text{建立 NP-hardness}\ ⚠️$$
