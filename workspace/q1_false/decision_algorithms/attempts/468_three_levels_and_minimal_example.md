# 468 采纳专家的框架：$D_I(X)$、A1/A2 拆分、最小反例（$k=2,\omega=1,U=0$）

> 承接 467。专家给出三层区分与显式构造，并指定一个符号化最小模型。本文件落实它。

## 目标

1. 记录他给的 $D_I(X)$ 构造与三层区分；
2. 按他要求做**符号化最小模型**（$k=2$、$\omega=1$、$U=0$、$N=I_2$、$A=\operatorname{diag}(1,2)$）；
3. 把命题 A 拆成 A1（泛型层）与 A2（特殊层）。

## 设想与理由

**三层区分（他的）**：

| 对象 | 参数空间性质 |
|---|---|
| Grassmannian 标准 chart $W_X/U=\operatorname{row}[I_a\ X]$，$X\in\mathbb A^{a(b-a)}$ | **有理仿射空间** ⟹ $\mathbb Q$/$\mathbb R$ 点都稠密 ✓ |
| 泛型秩层 $r=r_{\max}$ | chart 中的**非空 Zariski 开集** ⟹ 可用泛型秩 ✓ |
| 特殊秩层 $r<r_{\max}$ | **局部闭**代数集，可能多个分支 ⟹ 必须做实点判定 ✗ |

$D_I(X)=C(X)B_0$，$C(X)=\begin{pmatrix}-X&I_{b-a}&0&0\\0&0&-X&I_{b-a}\end{pmatrix}$，
$\mathcal T_{W_X}\cong\ker D_I(X)$（消去固定核部分后）✓。

## 做法：最小模型

$k=2$、$\omega=1$、$U=0$（故 $d=0$、$b=2$、$a=1$）、$N=I_2$、$A=\operatorname{diag}(1,2)$。
$K_0=\mathbb Q^2$，$\mathcal S=\operatorname{row}[N\ AN]=\operatorname{row}\begin{pmatrix}1&0&1&0\\0&1&0&2\end{pmatrix}$
⟹ $\mathcal S=\{(x,Ax):x\in\mathbb Q^2\}$（$A$ 的**图**）✓。

$\operatorname{Gr}(1,2)=\mathbb P^1$ 有两个标准卡：
- **卡 1**：$W_X=\operatorname{span}\{(1,X)\}$，$X\in\mathbb A^1$；
- **卡 2**：$W_\infty=\operatorname{span}\{(0,1)\}$（无穷远点，单点）。

**卡 1**：$x=t(1,X)$，$Ax=t(1,2X)$。$Ax\in W_X$ 需 $t(1,2X)=\lambda(1,X)$ ⟹ $\lambda=t$ 且 $2tX=tX$ ⟹ $tX=0$ ⟹

$$\mathcal T_{W_X}=\begin{cases}\{0\},& X\ne0\\ \mathcal S\cap(W\oplus W)=\text{1 维},& X=0\end{cases}$$

所以**卡 1 只有 $X=0$ 可行**（此时 $W=\operatorname{span}\{(1,0)\}$）✓；泛型点 $X\ne0$ **不可行** ✗。

**卡 2**：$Ax=t(1,2X)$ 换成 $x=t(0,1)$ ⟹ $Ax=(0,2t)\in W_\infty$ ✓ 恒成立 ⟹ $\mathcal T_{W_\infty}$ 1 维，
$\pi_1=\pi_2=W_\infty$ ⟹ **处处可行** ✓。

## 进展（结果与结论）

1. **最小反例成立**：卡 1 的泛型点不可行、**特殊点 $X=0$ 可行** ⟹ **泛型秩判定不能替代全部秩层** ✗；
2. **"$\operatorname{rank}M(q)<2\Rightarrow\neg(R)\vee\neg(E)$"被否** ✓（$X=0$ 时 $\operatorname{rank}M=1$ 且 (R)(E) 都成立）⟹ 这条路线**正式关闭**；
3. **命题 A 拆成两条**：
   - **A1（泛型层）**：$X$ 不可约、$\overline{X(\mathbb R)}=X$（实点稠密）⟹ 泛型秩判据成立（用 $\mathbb R(X)$；对 $\mathbb Q$-定义者，$\mathbb Q(X)$ 与 $\mathbb R(X)$ 上泛型秩一致 ✓）；标准 Grassmannian chart 满足，**特殊秩层不自动满足** ✗；
   - **A2（特殊层）**：必须直接判定 $X(\mathbb R)\cap\{\operatorname{rank}F_1\ge r_1\}\cap\{\operatorname{rank}F_2\ge r_2\}\ne\varnothing$——**半代数可行性**，不能用函数域计算代替 ✓；
4. **XP**：只有 chart 数 $\binom{b}{a}$ 有 $n^{O(\ell)}$ 的组合上界；**端到端 XP 未建立**（还要乘秩层数 × 子图数 × 核空间计算 × 实可行性 × 位长）✗。

## 最终结论

1. **专家的框架采纳**：Grassmannian chart 本身没问题（有理仿射）；**困难在秩跳变层上的实点可行性**；
2. **命题 A 必须拆成 A1 + A2**，A2 是实代数几何问题；
3. **最小反例**（卡 1 的 $X=0$）已给出，可直接作为"为什么必须保留秩分层"的标准例；
4. **不转硬度**：先把"Grassmannian 参数化 → 核空间秩分层 → 实点可行性"做成无漏洞的定理链 ✓。

## 放弃原因

- 没有写出**一般**的 $D_I(X)$ 显式公式并证明 $\mathcal T_{W_X}\cong\ker D_I(X)$（只在小模型上验证了结构）；
- 没有枚举特殊秩层的分支并做 A2 的实可行性判定；
- 没有端到端复杂度。

## 残留价值

- **完整的三层区分**与 $D_I(X)$ 构造（可直接用于写算法）；
- **最小反例**（$k=2,\omega=1,U=0$）——这是本线最有说服力的"必须分层"证据；
- A1/A2 的拆分，避免了再把"泛型秩"当成万能判据。

## 下一步

1. 写出一般 $D_I(X)$（从 $\mathcal S$、$U$、图空间约束出发），并证 $\mathcal T_{W_X}\cong\ker D_I(X)$；
2. 枚举特殊秩层分支，做 A2 的实可行性；
3. 估端到端复杂度（明确 XP/FPT 归属）。

## 相关文件

- [467](../../c_stratification/attempts/467_two_more_retractions.md)（两处撤回）
- [463](463_expert108_audit.md)（上一轮裁决）
- [452](../../c_stratification/attempts/452_E_simplified.md)（(R)(E) 判据）

## 状态

- 三层区分：**[已采纳]**。
- 最小反例：**[已算]**。
- 一般 $D_I(X)$：**[未写]**。
- 端到端 XP：**[未建立]**。
