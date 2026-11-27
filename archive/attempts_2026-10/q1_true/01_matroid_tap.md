> **开发日志摘要**（2026-10-27 整理）
> - **目标**：利用"坐标层 $(5b)$ = 拟阵无 coloop"把 Tree Augmentation Problem 的 NP-hardness 传进 MIN-ROWS。
> - **结果**：**死**。两个独立原因：①§7.9 的显式反例证明 $(T)$（坐标不劣于非坐标）为假；②§7.6–7.7 的可实现性：$\mathcal J=\operatorname{row}[C;CA]$ 只能是 Krylov 补丁之和，图拟阵（圈空间）不在其中。
> - **残留价值**：拟阵刻画本身（并环集）与"可实现 $\mathcal J$ 很薄"这两个结论仍然有效。
# 新引理：坐标 $\mathcal V$ + 对角 $A$ 时，$(5b)$ 是一个拟阵条件

## 目标
利用"坐标层 $(5b)$ = 拟阵无 coloop"把 Tree Augmentation Problem 的 NP-hardness 传进 MIN-ROWS。

## 最终结论
**死**。两个独立原因：①§7.9 的显式反例证明 $(T)$（坐标不劣于非坐标）为假；②§7.6–7.7 的可实现性：$\mathcal J=\operatorname{row}[C;CA]$ 只能是 Krylov 补丁之和，图拟阵（圈空间）不在其中。

## 相关文件
- [../tests/](../../q1_false/tests/) 不相关；相关工具在 `archive/old_scripts/q1_true_routes/`（c170–c175）
- [05_graph_reduction.md](05_graph_reduction.md)（同源的图论表述）


> 2026-10-24。本引理是本会话在 $(5b)$ 上找到的**第一个离散结构**。

---

## 1. 陈述

设 $A=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$，$\lambda_i$ 为**互异实数**；$\mathcal J\subseteq\mathbb R^n$ 任意；
$\mathcal V=\operatorname{span}\{e_i:\ i\in S\}$（坐标子空间）。

则 $(5a)$ 自动成立，且

$$\boxed{\ (5b)\iff \forall i\in S:\ r(S\setminus\{i\})=r(S)\ }$$

其中

$$r(S):=\dim\operatorname{span}\{\pi(e_j):\ j\in S\},\qquad \pi:\mathbb R^n\to\mathbb R^n/\mathcal J\ \text{为商映射}.$$

**等价说法**：在由 $\pi(e_1),\dots,\pi(e_n)$ 表示的线性拟阵 $M$ 上，$S$ 中**没有 coloop**（coloop = 删去后秩下降的元素）——即 $S$ 是一个**并环集**（union of circuits）。

---

## 2. 证明

$(5a)$：$\mathcal VA=\mathcal V\subseteq\mathcal V+\mathcal J$ ✓（对角 $A$ 保持坐标子空间）。

$(5b)$：对 $\lambda=\lambda_i$（$i\in S$），
$$(\lambda_i I-A)\mathcal V=\operatorname{span}\{e_j:\ j\in S,\ j\ne i\},\qquad
\dim(\mathcal V\cap E_{\lambda_i}^{\mathrm L})=1 .$$
代入交维数恒等式
$$\dim\big((\lambda_i I-A)\mathcal V\cap\mathcal J\big)=\dim(\mathcal V\cap\mathcal J)-1 .$$
而 $\dim(\operatorname{span}_S\cap\mathcal J)=|S|-r(S)$，故
$$|S|-1-r(S\setminus\{i\})=|S|-r(S)-1\iff r(S\setminus\{i\})=r(S). \qquad\square$$

$\lambda$ 取其它值时条件自动成立（$\mathcal V\cap E_\lambda^{\mathrm L}=0$，且交维数由上式同一恒等式给出）。

---

## 3. 数值验证

脚本 [`scripts/c170_matroid_check.py`](../../../archive/old_scripts/q1_true_routes/c170_matroid_check.py)：$n=4$、$A=\operatorname{diag}(1,2,3,4)$、
$\mathcal J$ 随机 2 维；枚举全部 15 个非空 $S$，逐个用**精确子式 gcd** 判 $(5b)$，与拟阵条件比较：

$$\boxed{\ 15/15\ \text{一致，0 不一致}\ }$$

（例：$S=\{0,3\}$：$(5b)$ ✓、拟阵 ✓；$S=\{0,1,3\}$：都 ✗。）

---

## 4. 由此得到的子问题

$$\textbf{CYCLIC-COVER}:\quad \min|S|\quad\text{s.t.}\quad \operatorname{supp}(K_0)\subseteq S\subseteq[n],\ \ S\ \text{是并环集}.$$

（$q_{\min}=|S|$ 在该子族上。）

**结构**：并环集族对并封闭；非并环集时，需不断添加"含某 coloop 的环"直到无 coloop。
每一步选哪个环会影响总大小 —— 这是**选择型**结构，可能承载硬度。

**注意**：$S$ 是并环集 $\iff M|S$ 无 coloop $\iff$ 每个 $e\in S$ 都落在 $M|S$ 的某个环里。

---

## 5. 缺口（为什么这还不是 q1 = 真的证明）

$\mathcal V$ 坐标是一个**限制**，所以

$$q_{\min}\ \le\ \min_{\text{坐标 }\mathcal V}|S| .$$

即：即使 CYCLIC-COVER 是 NP-hard，也只说明"坐标层"难；全问题可能有更好的非坐标解。

$$\text{要把它变成归约，需要一个把最优解\textbf{逼成坐标子空间}的 gadget（例如让 }\mathcal J\ \text{与 }A\ \text{的结构排除非坐标解）。}$$

---

## 6. 下一步

1. 定 CYCLIC-COVER 的复杂度：它是"最小环覆盖/并环集"型问题，可能多项式（拟阵并、拟阵交），也可能 NP-hard（选择型）；
2. 若 NP-hard，再找"逼成坐标"的 gadget；
3. 若多项式，则这是 q1 = 假的又一证据（至少在坐标层）。

---

## 7. CYCLIC-COVER 的硬度：图拟阵特化 = 一个已知 NP-hard 问题

### 7.1 特化

取 $M$ 为图 $G$ 的**图拟阵**（元素 = 边，电路 = 圈）。取 $S_0$ = $G$ 的一棵**生成树** $T$。则

$$S\supseteq T\ \text{且}\ G[S]\ \text{无桥}\iff S\supseteq T\ \text{且}\ G[S]\ \text{2-边连通}\qquad(\text{因 }S\supseteq T\ \text{已连通}).$$

于是

$$\text{CYCLIC-COVER}\big|_{\text{graphic},\ S_0=T}\ \equiv\ \text{「含指定生成树的最小 2-边连通生成子图」}.$$

### 7.2 这个特化问题是文献里的标准问题

- **H. Nagamochi, "An approximation for finding a smallest 2-edge-connected subgraph containing a specified spanning tree", Discrete Applied Mathematics 129 (2003)** —— 标题与我们的特化**逐字相同**，给的是近似算法；
- 同一问题即 **Tree Augmentation Problem**（TAP）：给定树 $T$ 与可选边集，求最小加边使 $T\cup J$ 2-边连通；近期文献（如 Nutov, *On the Tree Augmentation Problem*, arXiv:1703.07247）仍在做近似比与 LP 整性间隙。

$$\boxed{\ \text{TAP 系公认 NP-hard（近似算法文献的前提）；因此 CYCLIC-COVER 在 }\mathbb Q\text{ 上的线性拟阵里已是 NP-hard}\ }$$

（图拟阵都在 $\mathbb Q$ 上可表示，所以这是我们的拟阵族的一个子族。）

> 保留意见：我没有从原文里摘到一句"NP-hard"的原话；上述判断依据"存在近似算法文献 + 该问题长期无精确多项式算法"。

### 7.3 仍然差的最后一步

MIN-ROWS 在"坐标 $\mathcal V$"上**等于** CYCLIC-COVER，但全问题允许非坐标 $\mathcal V$，所以

$$q_{\min}\ \le\ \min_{\text{坐标}}\text{CYCLIC-COVER}.$$

即 MIN-ROWS 是 CYCLIC-COVER 的**松弛**。松弛可以变简单，所以 CYCLIC-COVER 的 NP-hardness **不能**直接推出 q1 = 真。

$$\text{还差：证明在这些实例上非坐标解不会更小（"逼成坐标"），或构造一个使非坐标解必然失效的 gadget。}$$

### 7.4 数值：非坐标解**没有**更好（3 组）

脚本 [`scripts/c172_coordinate_vs_full.py`](../../../archive/old_scripts/q1_true_routes/c172_coordinate_vs_full.py)：$A=\operatorname{diag}(1,2,3,4)$、$\mathcal J$ 随机 2 维、
$K_0=\operatorname{span}\{e_0\}$；比较坐标最优 $q_{\text{coord}}$ 与"$V=\operatorname{span}\{e_0,u\}$ 上的随机搜索"。

| seed | $q_{\text{coord}}$ | dim-2 非坐标可行解数 | $q_{\text{full}}$ |
|---|---|---|---|
| 1 | 3 | 0 | 3 |
| 2 | 2 | 126 | 2 |
| 3 | 3 | 0 | 3 |

$$\boxed{\ \text{非坐标解要么不存在，要么与坐标解同维——没有出现严格更优}}$$

这是"松弛可能是紧的"的初步证据（不是证明）。若紧，则 MIN-ROWS 在这些实例上**等于** CYCLIC-COVER，归约成立。

### 7.5 修正与更强的数值证据

**一次自我纠错**：早先 seed 6 曾出现 $q_{\text{full}}=2<q_{\text{coord}}=3$，但那个 $\mathcal J$ **不可实现**
（$\mathcal J$ 必须是 $\operatorname{row}[C;CA]$；该 $\mathcal J$ 没有任何 $C$ 能生成）。改用**可实现**的 $\mathcal J$（随机 $C$，$\mathcal J=\operatorname{row}[C;CA]$）后：

| 规模 | 实例数（$q_{\text{coord}}\ge3$）| 找到反例 |
|---|---|---|
| $n=4$（[c173](../../../archive/old_scripts/q1_true_routes/c173_search_counterexample.py)）| 81 | **0** |
| $n=5$（[c174](../../../archive/old_scripts/q1_true_routes/c174_n5_counterexample.py)）| 13 | **0** |

$$\boxed{\ \text{(T) 在 94 个可实现实例上无一败例}}$$

### 7.6 第二个缺口：拟阵族的可实现性

即使 (T) 成立，归约还差一步。坐标构造给出的拟阵是

$$M=M\big(\pi(e_1),\dots,\pi(e_n)\big),\qquad \pi:\mathbb R^n\to\mathbb R^n/\mathcal J,\quad \mathcal J=\operatorname{row}[C;CA],$$

即 $\mathcal J$ 必须是"由 $\le 2p$ 个向量及其 $A$-像生成"。而 TAP 用的图拟阵由**关联矩阵**表示，
其 $\mathcal J=\ker(\text{关联矩阵})=$ **圈空间**。于是需要：

$$\text{圈空间}=\operatorname{row}[C;CA]\quad(\text{对某个 }C\ \text{与对角互异 }A).$$

对角 $A$ 的 $\operatorname{row}[C;CA]=\operatorname{span}\{c_i,\ c_iA\}$ 是很窄的一类子空间；圈空间一般不在此列。

$$\boxed{\ \text{所以："CYCLIC-COVER NP-hard" + "(T)" 仍不直接给出 q1 = 真——还差"拟阵族可实现性"}\ }$$

### 7.7 缺口 B 有多严重：可实现 $\mathcal J$ 很稀少

**一个小引理**：$\dim\mathcal J=1$ 时，$\mathcal J$ 可实现 $\iff$ $\mathcal J$ 是坐标直线。

*证明*：$\mathcal J=\operatorname{span}\{u\}$ 可实现 $\Rightarrow$ 存在 $C$ 使所有 $c_i,\ c_iA\in\mathcal J$，故 $c_i\propto u$、$c_i\circ\lambda\propto u$，于是 $u\circ\lambda\propto u$，$u$ 是 $A$ 的特征向量；$A$ 对角互异 $\Rightarrow u$ 单支撑。$\square$

**推论**：单圈图的圈空间（由 0/1 圈向量张成、非坐标）**不可实现**。

**数值**（[c175](../../../archive/old_scripts/q1_true_routes/c175_realizable_J.py)，$n=4$，$A=\operatorname{diag}(1,2,3,4)$，$p=1$ 搜 $\{-2..2\}^4$、$p=2$ 搜 $\{-1..1\}^4$）：

| 对象 | 可实现 |
|---|---|
| 随机 2 维 $\mathcal J$（40 个）| **0** |
| 坐标 2-平面 | ✓ |
| 3-支撑的 Krylov 平面 $\operatorname{span}\{u,uA\}$（$\#\mathrm{supp}\,u=3$）| ✓ |

$$\boxed{\ \text{可实现的 }\mathcal J\ \text{是}\textbf{很薄}的一类（坐标、Krylov 型）；随机子空间几乎都不可实现}\ }$$

**这意味着**：TAP 的图拟阵（圈空间）大概率落在可实现族之外，缺口 B 对 TAP 路线**可能是致命的**。

### 7.8 $p=1$ 的拟阵是什么：均匀拟阵 ⊕ 自由元（已验证）

$p=1$ 时 $\mathcal J=\operatorname{span}\{c,\ c\circ\lambda\}$（$\dim\le2$）。设 $c$ 的支撑为 $S_c$（$|S_c|=m$），则

$$M=\underbrace{U_{m-2,\,m}}_{\text{在 }S_c\text{ 上}}\ \oplus\ \underbrace{\text{自由元}}_{[n]\setminus S_c}.$$

*理由*：$\operatorname{span}\{e_j:j\in S\}\cap\mathcal J\ne0$ 当且仅当 $\alpha c+\beta(c\circ\lambda)$ 在 $S$ 外为零，即对每个 $j\in S_c\setminus S$ 有 $\lambda_j=-\alpha/\beta$；因 $\lambda_j$ 互异，$S_c\setminus S$ 至多一个元素。故秩函数为 $r(S)=|S|$（$|S_c\setminus S|\ge2$）、$|S|-1$（$|S_c\setminus S|\le1$）。

**验证**（$n=4$，$c=(1,1,1,0)$）：秩表给出 $S_c=\{0,1,2\}$ 上所有对都是秩 1（全部平行），$3$ 是自由元 ✓。

$$\Longrightarrow\ p=1\ \text{的拟阵是均匀拟阵}\ \oplus\ \text{自由元 —— 多项式可解}$$

$$\boxed{\ \text{所以"薄"的那一族不仅薄，而且}\textbf{简单}；TAP 路线基本可以判定为死路}\ }$$

### 7.9 (T) 为假：显式反例（2026-10-24 22:40）

$n=6$、$A=\operatorname{diag}(1,\dots,6)$、$L_0=e_0$、

$$C=\begin{pmatrix}1&2&1&1&0&1\\-1&0&0&2&-2&-2\end{pmatrix},\qquad
\mathcal L=\begin{pmatrix}e_0\\ u\end{pmatrix},\quad u=(0,-1,-1,0,1,1).$$

| 检查（可信基线 `c162.cond5a/cond5b`）| 结果 |
|---|---|
| $\operatorname{rank}\mathcal L$ | 2 |
| $(5a)$ | ✅ True |
| $(5b)$ 子式 gcd 次数 | **0**（成立）|
| $d,\ \dim V,\ \rho=\operatorname{rank}(\mathcal LN)$ | $2,\ 2,\ 1$ |

而**坐标最优**：不存在维数 $\le2$ 的可行坐标 $\mathcal V$（$q_{\text{coord}}=3$）。

$$\boxed{\ q_{\min}\le 2\ <\ 3=q_{\text{coord}}\ \Longrightarrow\ \textbf{(T) 为假}}$$

$$\Longrightarrow\ \text{MIN-ROWS 严格松于 CYCLIC-COVER；拟阵/TAP 路线\textbf{死}}$$

（该实例还是"中间层"：$\rho=1<\dim V=2$，与 $q_{\min}=\rho^*+1=2$ 一致。）

---

## 8. 补充：$K_4$ 圈空间的显式检验（2026-10-27）

> **⚠️ 说明**：本节是 §7.6–7.7（缺口 B：拟阵族可实现性）的一个**具体实例检验**，不是新结论。
> 写完后才发现 §7.9 已经用显式反例证明 $(T)$ 为假、并判定 TAP 路线死亡——
> 也就是说，本节的结论（"圈空间不可实现"）只是给已死的路线再加一条独立理由。

### 8.1 结构性约束（$\S7.6$ 的同一句话）

$A$ 对角时 $\mathcal J=\operatorname{row}[C;CA]=\sum_{c\in C}\operatorname{span}\{c,\ cA\}$，
即 $\mathcal J$ 必是若干 **Krylov 补丁** $\operatorname{span}\{u,Au\}$ 之和。

### 8.2 具体检验（`scripts/c198_graphic_matroid.py`）

$n=6$、$A=\operatorname{diag}(1,\dots,6)$、$\mathcal J=\ker(\text{incidence of }K_4)$（$K_4$ 的圈空间，$\dim3$）：

| 量 | 值 |
|---|---|
| $\max_C\dim(\operatorname{row}[C;CA])$，$C\subseteq\mathcal J,\ \dim C=2$ | **$4$**（要 $=3$ 才可能 $=\mathcal J$）|
| 同上，$\dim C=3$ | $\ge 5$ |
| $200$ 组随机对角 $A$ 找 $C$ | **$0/200$** |

$$\boxed{\ K_4\ \text{的圈空间在对角 }A\ \text{下不可实现（与 §7.7 的"可实现 }\mathcal J\ \text{很薄"一致）}\ }$$

### 8.3 结论

与 §7.9 相同：**TAP 路线死**（§7.9 的反例已足够，本节只是第二重理由）。
$(5b)$ 侧的下一步不是这个方向，而是层判定的可判定性。
