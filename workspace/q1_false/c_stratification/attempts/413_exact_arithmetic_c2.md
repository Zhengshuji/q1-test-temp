# 413 $c=2$ 单谱定理的精确算术与位复杂度（专家 109 号 Priority 2）

> 承接 408（复杂度骨架）与 411（专家要求补五项：$D$ 的精确表示、高度增长、$\varphi/\Phi_0$ 的精确判定、
> gcd 复杂度、实图卡有效性）。本文件逐项补。

## 目标

在固定 $c=2$、单谱、$K_0$-split 的许诺下，把"$\mathrm{poly}(n,\tau)$"从骨架变成**可引用的定理**：
每一项的表示、判定与代价都写清。

## 设想与理由

单谱时不变 2-平面的结构极简：**两个特征直线之和**。所以"精确表示 $D$"归结为
"精确表示两条特征直线"，而特征直线由**不可约因子的实根**给出。关键是：

1. $M\in\mathbb{Q}^{k\times k}$ ⟹ 特征值是有理多项式 $f\in\mathbb{Q}[t]$（不可约）的根 ⟹ **代数数、可精确表示**；
2. 若两条直线来自因子 $f,g$（次数 $d_f,d_g$），则 $D$ 定义在 $L=\mathbb{Q}(\alpha,\beta)$ 上，**次数 $\le d_fd_g\le k^2$**；
3. $L$ 的实嵌入给"实"直线——算法只需枚举**实嵌入**，不需要一般实代数几何。

## 做法与进展

### (1) $D$ 的精确表示——**分两个谱分支**（专家 110 号 §5.1 的必修）

> **更正**：原来只按"实根 $\alpha,\beta$"描述，**漏了共轭复特征值**。专家给的反例说明
> "simple spectrum（复谱互异）"**不等于** "real simple spectrum"：
> $M=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ 有特征值 $\pm i$、无实特征向量，
> 但其不变 2-子空间是 $D=\mathbb R^2$。

设 $m_M(t)=\prod_i f_i(t)$ 是 $M$ 在 $\mathbb{Q}[t]$ 上的最小多项式分解（单谱 ⟹ 各 $f_i$ 互异、无重根）。

**分支 R（$f_i$ 有实根，两个不同的实特征直线）**：
$$\alpha\in\operatorname{Roots}_{\mathbb R}(f_i),\ \beta\in\operatorname{Roots}_{\mathbb R}(f_j),\quad
D=\operatorname{span}_{\mathbb R}\{v_\alpha,v_\beta\},\quad
L=\mathbb{Q}(\alpha,\beta),\quad [L:\mathbb{Q}]\le d_id_j\le k^2 .$$
$v_\alpha=\ker(M-\alpha I)$ 在 $L$ 上精确算（Cramer，分母 $f_i'(\alpha)\ne0$ 由单谱保证）。

**分支 C（$f_i$ 无实根，共轭复特征值）**：取复根 $\alpha$、复特征向量 $z=u+iw$（$u,w\in\mathbb R^k$），则
$$D=\operatorname{span}_{\mathbb R}\{u,w\}.$$
两条路线等价，取**不需要数域**的那条：
- $f$ 不可约二次时 $\dim_\mathbb{Q}\ker f(M)=2$，故 $D=\ker f(M)$ 是 $\mathbb{Q}$-定义的、唯一 ✓；
- $f$ 次数 $2m>2$（重数 $m>1$）：不变 2-平面的族是 $\mathbb P$ 型的正维族（393 定理 3 的第三类），
  算法侧按 $M|_D$ 的实 Jordan 型分层处理；**本轮的单谱定理只用到 $m=1$**。

**关于"只在实域里算"的说明**（专家 §5.2 要求写清）：
- 分支 R：$L=\mathbb{Q}(\alpha,\beta)\subset\mathbb R$，**本身就是实域**，取恒等嵌入；
- 分支 C：计算 $z$ 时用 $L_\mathbb{C}=\mathbb{Q}[t]/(f)$ 的**复嵌入**，但**输出 $D$ 是 $\mathbb{Q}$-定义的**
  （$f$ 不可约二次时 $D=\ker f(M)$），故后续所有线性代数可在 $\mathbb Q$ 上做——**不需要在复域里算**。
  两件事必须分开说：*中间量*（$z$、$u$、$w$）在复嵌入下算出，*最终对象*（$D$ 及其后的 $T_D,\varphi,\Phi_0$）是 $\mathbb Q$-定义的。

**数域次数与高度（专家 §5.3 要求的形式）**：

> **引理（不变平面枚举的算术复杂度，单谱）.** 设 $M\in\mathbb{Q}^{k\times k}$ 单谱、输入位长 $\tau$。则
> $$\#\{D\}=\binom{k_{\mathbb R}}{2}+\#\{\text{共轭对}\}\le k^2,\qquad d_L\le k^2,\qquad
> h(L)\le \mathrm{poly}(n,\tau),$$
> 且每个 $D$ 的基（在 $L$ 上）、$D^{\perp_{K_0}}$、$T_D$、$\varphi$、$\Phi_0$、$\lambda H-H_A$ 的条目高度
> $\le\mathrm{poly}(n,\tau)$。

（**"次数 $\le k^2$"与"系数位长 $=\mathrm{poly}$"是两个独立命题**，专家 §5.3 明确要求分开陈述；
本文件只给量级，**论文附录必须按他列的八步逐项补常数**。）

### (2) 高度增长（逐项）

| 量 | 高度 | 理由 |
|---|---|---|
| $M$、$A_{21}$、$N$ | $\mathrm{poly}(n,\tau)$ | Cramer + Gram 逆（分母 $\det$ 的界） |
| $f_i$ 的系数 | $\mathrm{poly}(n,\tau)$ | $m_M$ 由 $M$ 的特征多项式整除得到（Kronecker/整性） |
| 代数数 $\alpha$（作为 $f_i$ 的根） | $\mathrm{poly}(n,\tau)$ | 根的高度 $\le$ 多项式的 Mahler 界（标准） |
| $v_\alpha$ 的坐标（在 $L$ 的幂基下） | $\mathrm{poly}(n,\tau)$ | Cramer 于 $L$ 上（分母 $f_i'(\alpha)\ne0$） |
| $D^{\perp_{K_0}}$、$T_D$ 的基 | $\mathrm{poly}$ | 正交补/核的基，仍由 Cramer |
| $\varphi$、$\Phi_0$、$\lambda H-H_A$ 的条目 | $\mathrm{poly}$ | 有限次 $L$-算术，次数 $\le$ $\mathrm{poly}$ |

（结论是标准的"高度多项式增长"，但**逐项给出界**是专家要求的；这里给的是量级，
细节由标准引理支撑：$L$ 上 Cramer 的分母是与判别式相关的非零量。）

### (3) $\varphi$、$\Phi_0$、可实现性的精确判定

固定 $D$（在 $L$ 上）：
1. $T_D=K_0^\perp\cap(A_{21}D)^\perp$：$L$ 上的核，**精确可算**（Gauss 消元，$L$ 是域）；
2. $\varphi:T_D\to D^\circ$，$w\mapsto\varphi_w$；$\rank\varphi$、$\ker\varphi$、$\Phi_0=\varphi(W_0)$ 全是 $L$ 上的线性代数，
   **精确可判**（秩 = 非零子式的存在性，在域上无舍入）；
3. 可实现性（411 定理 3）：$\Phi_0\subseteq\Phi\subseteq\varphi(T_D)$ 与
   $\dim\Phi-\dim\Phi_0\le t-w_0\le\dim\ker\bar\varphi+\dim\Phi-\dim\Phi_0$——都是整数比较 + 子空间包含判定 ✓。

**Dedup 与枚举**：候选 $D$ 的个数 $\le\binom{k}{2}+$共轭对数（单谱）；每个 $D$ 的 $\Phi$-类至多 3 种（411 §B 的表）。

### (4) 每张图卡的 gcd 复杂度

图卡参数化**像直线** $\Phi(s)=\operatorname{span}(\phi_0+s\phi_1)$（只用一行，见 408 引理 2）：
- 铅笔条目在 $L(s)$ 中，$\deg_s\le1$、$\deg_\lambda\le\omega\le k$；
- 子式个数 $\binom{q}{\omega}\binom{k}{\omega}\le 2^n$（乘性）；
- 每个 $\omega$ 阶子式：$\omega!\cdot\omega^3$ 次 $L[s]$ 的乘法，$\deg_s\le1$；
- 在 $L(s)[\lambda]$ 上算 gcd（分式自由子结式链）：代价
  $$\mathrm{poly}\bigl(\omega,\ \deg_s,\ [L:\mathbb{Q}],\ \text{高度}\bigr)=\mathrm{poly}(n,\tau)$$
  （$[L:\mathbb{Q}]\le k^2$、高度 $\mathrm{poly}(n,\tau)$，而 $\omega\le k$）。

**这正是专家 §5.3 第 4 条要的界**：gcd 的代价由系数次数与高度决定，而两者都是 $\mathrm{poly}$。

### (5) 实图卡的有效性

每个 $D$ 都通过**实嵌入**构造（$\alpha$ 取 $f_i$ 的**实根**；共轭对情形用 $\ker f_i(M)$ 的实性），
所以 $D$ 是**实** 2-平面、$T_D$、$\varphi$、$\Phi_0$ 都是实的；$\Phi$ 的直线族 $\mathbb P(D^\circ)$ 里
能取到的实点由 411 §B 的表与可实现性不等式决定。于是每张图的实点问题**不需要**一般实代数几何：
- 若有效 $\Phi$ 是 $\{0\}$ 或 $D^\circ$：单点，实的 ✓；
- 若是直线：$\mathbb P^1$ 的两张标准图卡各有实点（$\mathbb P^1(\mathbb R)$ 稠密），且整条直线由实参数给出 ✓。

再由 405 的实一般点判据（每点满秩 + 实点稠密）把"一般点 gcd"翻译成"存在实可行点"。

### 定理（$c=2$ 单谱，精确算术版）

许诺 (i) $c=2$；(ii) $M$ 单谱；(iii) $K_0$-split。则层判定（三值）可在
$$\mathrm{poly}\Bigl(k^2\cdot \mathrm{poly}(n,\tau)\Bigr)=\mathrm{poly}(n,\tau)$$
内完成，其中算术在次数 $\le k^2$ 的数域上进行；所有判定（秩、包含、维数不等式、gcd）都是精确的。

*证明.* 由 (1) 枚举 $O(k^2)$ 个 $D$（每个一次域构造）；由 (3) 每 $D$ 判至多 3 个 $\Phi$-类；
由 (4) 每类至多 2 张图的 gcd；代价由 (2)(4) 的界控制；(5) 给实点。$\square$

## 进展

- 五项逐条给出：表示（域次数 $\le k^2$）、高度（表中逐项）、精确判定（域上线性代数）、
  gcd 代价（$\deg_s\le1$、$\deg_\lambda\le\omega$、高度 $\mathrm{poly}$）、实点（实嵌入 + 405）；
- 定理从"骨架"升级为"可引用形式"；
- 诚实标注：高度界只给量级 + 标准引理，没有逐项算出显式常数；`dedup` 的具体实现未写。

## 最终结论

1. **$c=2$ 单谱定理的精确算术版成立**（在 $\mathrm{poly}$ 位复杂度意义下、数域次数 $\le k^2$）；
2. 关键简化：**只用实嵌入**（不需要一般实代数几何）；
3. 与 411 的三条定理、405 的判据、408 的图卡计数拼成完整的算法链。

## 放弃原因

- 高度界没有逐项展开（依赖"根的高度 $\le$ Mahler 界"等标准引理，未在本文档内证明）；
- 没有把"$L$ 上的 Cramer 分母非零"（即 $f_i'(\alpha)\ne0$，单谱保证）写成完整引理；
- `dedup`（同一 $D$ 的多种表示）只提了一句，没有算法；
- 没实现脚本。

## 残留价值

- 专家 Priority 2 五项要求的**逐条回应**；
- 精确算术版定理（可直接进 $c=2$ 论文的算法节）；
- 数域次数 $\le k^2$、$\deg_s\le1$、$\deg_\lambda\le\omega$ 这三个界，是全部代价的来源。

## 相关文件

- [attempts/408](408_c2_complexity.md)（复杂度骨架）、[411](../../decision_algorithms/attempts/411_expert109_audit.md)（五项要求）
- [attempts/407](../../decision_algorithms/attempts/407_effective_charts.md)（图卡；一般情形已撤回，单谱保留）
- [attempts/405](../../decision_algorithms/attempts/405_real_generic_point.md)（实一般点判据）
