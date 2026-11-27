> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 提升引理 §45–§47（拆分自 LEMMA_LIFT_2026-10-23.md）

> 原文：`archive/attack_A2V0/LEMMA_LIFT_2026-10-23.md`。整条链对应已推翻的 $q_{\min}=\dim V+1$。

## 45. 系统论重述与文献连接（2026-10-23 晚）

### 45.1 用系统语言重写最后一步

$$V_0=\ker\begin{pmatrix}L\\CA\\C\end{pmatrix}=\text{系统}\ (A,[C;CA],L)\ \text{的"核空间"}$$

$$(5b)\iff\begin{pmatrix}\lambda L-LA\\CA\\C\end{pmatrix}\ \text{秩恒定}\iff\textbf{铅笔无零点（minimal / no zeros）}$$

**已证**（$(5b)$ 一阶）：$A(V_0)\subseteq\ker L$

$$\boxed{\ \text{要证}:\quad A(V_0)\subseteq\ker[CA;C]=V_0\cap\ker(CA)\ \text{hmm}\ \Longrightarrow\ \text{即}\ CA^2v=0\ }$$

### 45.2 文献中的对应

| 概念 | 我们的对象 |
|---|---|
| conditioned invariant subspace | $V_0$（$A V_0\subseteq V_0+\ker[C;CA]$）|
| pencil with no zeros（Rosenbrock）| $(5b)$ |
| "无零点 ⟹ 核空间被 $A$ 保持" | **正是要证的引理** |

**参考**：
- Basile–Marro, *Controlled and Conditioned Invariants in Linear System Theory*
- Wonham, *Linear Multivariable Control*（pencil 与 invariant subspace 的桥）
- Camlibel–Heemels 的笔记（input-containing conditioned invariant）

### 45.3 下一步（文献路线）

$$\text{在 Wonham 的书中找}:\quad \text{"}\begin{pmatrix}\lambda I-A & -B\\ C & D\end{pmatrix}\ \text{无零点"与核空间的关系}$$

**具体猜测**：命题会是
$$v\in\ker\begin{pmatrix}L\\CA\\C\end{pmatrix}\ \wedge\ \text{铅笔无零点}\ \Longrightarrow\ A^2v\in\ker\begin{pmatrix}L\\CA\\C\end{pmatrix}$$

—— 即 $V_0$ 是 $A^2$-不变的 ✓（这比 $A$-不变弱，但足够我们 ✓）

---

## 46. ✅ 更清晰的形式：$V_0$ 是 $A^2$-不变

### 46.1 检验

| 检验 | 规模 | 违例 |
|---|---|---|
| $A(V_0)\subseteq\ker(CA)$ | 2293 | **0** ✓ |
| **$A^2(V_0)\subseteq V_0$** | 2293 | **0** ✓ |
| $A(V_0)\subseteq\ker L$（已证）| 2293 | 0 ✓ |

$$\boxed{\ A^2(V_0)\subseteq V_0\quad(2293/2293)\ \checkmark\ }$$

### 46.2 于是 $CA^2v=0$ 成立

$$CA^2v=C(A^2v)\qquad A^2v\in V_0=\ker[L;CA;C]\ \Longrightarrow\ C(A^2v)=0\ \checkmark$$

$$\boxed{\ CA^2v=0\ \text{由}\ A^2\text{-不变性直接得到}\ }$$

### 46.3 为什么这更好

| 旧形式 | 新形式 |
|---|---|
| $CA^2v=0$（逐个 $v$）| **$A^2(V_0)\subseteq V_0$**（子空间不变性）|
| 不便于归纳 | **可以尝试归纳/不变子空间论证** ✓ |

### 46.4 证明路线（新）

$$V_0=\ker\begin{pmatrix}L\\CA\\C\end{pmatrix}\qquad\text{要证}\quad A^2V_0\subseteq V_0$$

**已知**（$(5b)$ 一阶）：$A V_0\subseteq\ker L$ ✓

$$\text{若还能证}\ A V_0\subseteq\ker(CA)\ \text{（2293/2293 ✓）}\ \Longrightarrow\ A V_0\subseteq V_0\cap\ker(CA)$$
$$\Longrightarrow\quad A V_0\subseteq\ker\begin{pmatrix}L\\CA\\C\end{pmatrix}=V_0\ \text{hmm（需要}\ A V_0\subseteq\ker C\ \text{too）}$$

**注意**：$A V_0\subseteq\ker L$ ✓ 且 $A V_0\subseteq\ker(CA)$ ✓ ⟹ $A V_0\subseteq\ker[L;CA]$ hmm — 但 $V_0$ 还要求 $\ker C$ ✗

**所以要证 $A V_0\subseteq\ker C$ hmm** —— 但 $v\in V_0\Rightarrow Cv=0$ ✓，而 $C(Av)=CAv=0$ ✓（因 $v\in\ker(CA)$ ✓）✓！

$$\boxed{\ Av\in\ker C\ \text{自动}\ ✓;\quad Av\in\ker L\ ✓;\quad Av\in\ker(CA)\ \text{需证}\ \Longrightarrow\ Av\in V_0\ \Longrightarrow\ A^2V_0\subseteq V_0\ }$$

---

## 47. 文献查阅报告（Trentelman–Stoorvogel–Hautus 2002）

### 47.1 书的信息

$$\text{Trentelman, Stoorvogel, Hautus, \textit{Control Theory for Linear Systems}, 2002（403 页）}$$
（`pdf/Control Theory of Linear System.pdf`，已提取全文到 `lit/trentelman2002.txt`，822K 字符）

### 47.2 关键词命中

| 关键词 | 次数 |
|---|---|
| no zeros | 20（**全部**指传递矩阵零点 ✗）|
| conditioned invariant | 36 ✓ |
| A-invariant | 44 ✓ |
| unobservable | 106 ✓ |
| **almost invariant** | **0** ✗ |

### 47.3 最相关的定理

**Corollary 7.5**（Ch. 7，多项式矩阵）：
$$P(\lambda)\ \text{可逆}\ \forall\lambda\iff\det P(\lambda)\ \text{是非零常数}$$

**但这是方阵情形** ✗ —— 我们的铅笔是长方阵 ✓，需要"所有 $\rho$ 阶子式的 gcd 为 1"✓（书中未直接给 ✓）

### 47.4 结论

$$\boxed{\ \text{文献中\textbf{没有}直接可用的引理};\quad \text{我们的最后一步（}A^2V_0\subseteq V_0\text{）可能是\textbf{新的}} }$$

$$\Longrightarrow\quad \text{若确实新，它本身就是论文的一个贡献（一个"无零点铅笔 ⟹ 核空间 }A^2\text{-不变"的引理）}$$

### 47.5 下一步

$$\text{要么（a）自己证它（值得，因为是新的）};\quad\text{要么（b）把它作为论文的独立小结果陈述（2293+ 验证）}$$