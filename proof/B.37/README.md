# B.37 · 谱可行性的统一刻画（统一定理）

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.37` 条目（§0.1 归并表）。
> 本条是**综合**：把 B.1、B.17、B.24、B.8 接到同一条定理上；每一环都是已复核的命题，
> 本条新增的只有两处识别（见 §"证明"的 (A)(B)）与不变量陈述的合并。


## 域修正（专家第五轮 + L5 否证，2026-11-07）

本条的域由 $W=\mathcal LV$ 修正为
$$W_K=\mathcal L\ker[C;CA],\qquad \Phi_K(\mathcal Lv)=\mathcal LAv\ (v\in\ker[C;CA]),\qquad P_K(\lambda)=\lambda\iota_K-\Phi_K .$$
理由：核方程不要求 $v\in V$（专家 §7），且 $\mathcal LK=\mathcal L(V\cap K)$ 已被反例否证
（$\dim K=2,\ \dim(V\cap K)=1,\ \dim\mathcal LK=2$；随机扫描 382/382 不相等，见 B.24 卷宗）。
L5 的否证意味着 $W_0$ **不能**作为等价实现。

## 命题

设 $\mathcal L$ 满足 $(5a)$，记
$$V=\operatorname{row}[\mathcal L;C],\quad S=V\cap\mathcal Z,\quad W=\mathcal LV,\quad \rho=\dim W,$$
并设 $\Phi:W\to\mathbb C^q$ 为题 B.24 的偏映射（$\Phi(x\mathcal L)=x\Lambda$）、$\iota:W\hookrightarrow\mathbb C^q$ 为包含，
$$P_\Phi(\lambda):=\lambda\iota-\Phi\in\mathbb C^{q\times\rho},\qquad
\overline N_{\mathcal Z}(\lambda):V/S\longrightarrow X/\mathcal Z .$$
则以下四条**等价**：

1. $(5b)$ 成立；
2. $\overline N_{\mathcal Z}(\lambda)$ 对每个有限 $\lambda$ **单射**（商铅笔逐点满列秩）；
3. **不存在非零部分特征向量**：$\nexists\,0\ne w\in W_K$ 与 $\lambda\in\mathbb C$ 使 $\Phi_K(w)=\lambda w$
   （$W_K=\mathcal L\ker[C;CA]$，$\Phi_K(\mathcal Lv)=\mathcal LAv$，$v\in K$）；
4. $P_K(\lambda):=\lambda\iota_K-\Phi_K$ 的全部极大子式（阶 $=\dim W_K$）的 $\gcd$ 是**非零常数**。

此外（核结构，来自 B.17）：

* 公共核 $\bigcap_{\lambda\in\mathbb C}\ker\overline N_{\mathcal Z}(\lambda)=S$；
* 多项式零模 $\ker_{\mathbb C[\lambda]}\overline N_{\mathcal Z}(\lambda)=S\otimes_{\mathbb C}\mathbb C[\lambda]$；
* 由 B.6：$(5a)$ 下右最小指标全为 $0$、无穷初等因子全为 $1$ 次，故**有限初等因子承载全部谱障碍**：
$$(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}\mathcal L .$$

## 纸面证明

**(i)⟺(ii).** B.17 给出 $(5b)\iff\ker\overline N_{\mathcal Z}(\lambda)=S$ 对一切 $\lambda$，且 $S\subseteq\ker\overline N_{\mathcal Z}(\lambda)$
对一切 $\lambda$ 成立（B.17 第 1 条）。于是"$\ker=S$"与"$\ker\subseteq S$"等价，而后者正是
$\overline N_{\mathcal Z}(\lambda)$ 在 $V/S$ 上为**单射**。$\square$

**(i)⟺(iii).** 即 B.24：$\Phi=K_1|_W$，且 $(5b)$ 失败 $\iff\exists\,0\ne w\in W:\Phi(w)\in\mathbb C w$。$\square$

**(iii)⟺(iv).** 关键是识别 (B)：$P_\Phi$ 是**单参数矩形铅笔**，其首项系数 $\iota$ 的秩为 $\rho$，
故正规秩 $=\rho$。而
$$\ker P_\Phi(\lambda)\ne0\iff\exists\,0\ne w:\ \lambda w-\Phi(w)=0\iff\Phi(w)\in\mathbb C w,$$
所以"(iii) 成立"$\iff\operatorname{rank}P_\Phi(\lambda)=\rho$ 对一切 $\lambda$。
把 B.8（取 $h=\rho$、域 $F=\mathbb C$）用于 $P_\Phi$：
$$\operatorname{rank}P_\Phi(\lambda)=\rho\ \forall\lambda\iff \gcd\{\text{全部 } \rho\times\rho\text{ 极大子式}\}\in\mathbb C^\times .$$
两条合起来即 (iii)⟺(iv)。$\square$

由 (i)⟺(ii) 与 (i)⟺(iii) 得 (ii)⟺(iii)，四条等价。核结构与有限初等因子结论分别由 B.17、B.6 给出。$\square$

**两处识别（本条新增，其余为引用）**：
* **(A)** "(ii) 的单射"与 B.17 的"$\ker=S$"是同一件事——用到 B.17 第 1 条给出的 $\ker\supseteq S$；
* **(B)** B.8 的 $h$ 取 $\rho$、矩阵取 $P_\Phi$——用到 $\iota$ 满列秩故正规秩 $=\rho$。

## Lean

**无独立内核（F1）**。四条各自的内核已存在：
B.1（`PencilEquivalence.pencil_rank_forall` 等）、B.17（`B21_B13f` 等）、B.24（`B24Phi` 的商泛性质）、
B.8（纸面，无内核）。本条本身是**组装**，两处识别 (A)(B) 是短推理，尚未形式化。

## 精确验证

* 固定候选判据（(iii)⟺(iv)）已在 `tools/verification/spectral_gcd.py` 的极大子式 gcd 路径上被反复使用；
* 统一性本身是逻辑综合，无可独立检验的数值内容。

## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3（四个组分均经独立复核；组装部分为本轮新写） |
| 形式 F | F1 |
| 导出等级 | **L2** |
| 完成判定 | **完成**（标准：M≥3 即可；Lean 为加分项）—— Lean 无独立内核（四条各自有内核或纸面） |

## 状态与历史

* 2026-11-07：按专家第四轮建议（"把 B.17、B.23–B.24、B.8 合成一条四层统一"）新立本条。
* 专家对该形式的评价：四等价"给出同一现象的四重视角（原秩 / 商铅笔 / 部分特征向量 / 行列式因子）"，
  并建议把它作为论文的**中央定理**。
* 未形式化的仅是组装；若将来形式化，应先在 `MyProof` 里定义 $P_\Phi$ 与 $\overline N_{\mathcal Z}$ 两个对象。

## 支撑目录

[proof/B.17/](../B.17/README.md)、[proof/B.24/](../B.24/README.md)、[proof/B.8/](../B.8/README.md)、
[proof/B.1/](../B.1/README.md)、[proof/B.6/](../B.6/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（第四轮：采纳为中央定理形式，待复核组装）

专家在 29 号答复 §6.4、§11 提出该形式，并明确"subject to checking the equivalences and hypotheses in the
complete proofs"。本轮把两处识别写成显式论证（§"证明"的 (A)(B)）；请复核这两处，以及
"(iii)⟺(iv)"是否确实只需 B.8（即 $P_\Phi$ 的正规秩是否确为 $\rho$）。


## Task 1 的部分结果：块因子化 → 行列式因子（Cauchy–Binet 桥）

专家列的 Task 1 是"把 $\Delta_{P_\Phi}$ 与 B.17 的 Kronecker 不变量接起来"。等号情形（$h=q+r_1$）下可以完全做到，
并且这正好是 B.22 行列式论证的一般化。

**引理（块因子化的极大子式）** 设 $Q=P\,H$，其中 $P$ 为 $h\times h$、$H$ 为 $h\times n$ 且**行满秩**。
则对任意行子集 $I$（$|I|=h$）与列子集 $J$（$|J|=h$），
$$\det Q[I,J]=\det P\cdot\det H[I,J],$$
故 $Q$ 的全部 $h\times h$ 极大子式的 $\gcd$ 为
$$\Delta_Q=\det P\cdot\gcd\{\det H[I,J]\}_{I,J}=\det P\ \ \text{（相差非零常数）},$$
因为 $H$ 行满秩 ⟹ 存在 $I,J$ 使 $\det H[I,J]\ne0$（常数多项式），其 $\gcd$ 是非零常数。

*证明*：Cauchy–Binet。$Q[I,J]=(PH)[I,J]=P\cdot H[I,J]$（$P$ 是 $h\times h$，乘积的第 $I$ 行块
$=P\cdot H[I,\cdot]$ 的相应行），故行列式相乘。$\gcd$ 的结论由"常数族的 gcd 是非零常数（只要有一个非零）"得到。$\square$

**推论（等号情形的行列式因子）** 当 $h=q+r_1$ 时，B.22 给出 $Q_{\mathcal L}=P(\lambda)H_0$，
$P(\lambda)=\begin{pmatrix}\lambda I_q-K_1&-K_2\\0&I_{r_1}\end{pmatrix}$、$H_0=[\mathcal L;B]$ 行满秩。于是
$$\Delta_{Q_{\mathcal L}}(\lambda)=\det P(\lambda)=\det(\lambda I_q-K_1).$$
这解释了 B.22 里"方块行列式 $=\det(\lambda I_q-K_1)$"为何就是极大子式的 gcd——
即 B.8 的 $\Delta_h$，也即 $(5b)$ 失败的判别式。

**一般情形（$h<q+r_1$）仍是 Task 1 的未完成部分**：此时 $Q_{\mathcal L}$ 不能写成"方阵 × 行满秩"的形式，
$\Delta_{Q_{\mathcal L}}$ 与 $P(\lambda)$ 的关系需要更细的 Kronecker 分析（专家列的 Task 1 本体）。
本卷宗记录：**等号情形已闭合；一般情形待证**。



## 实例化待办：$\Phi$ 的行/列约定必须先钉死

尝试给 B.37 写"实例探针"（在可容许实例上真算 $W,\Phi,P_\Phi$）时撞到一处**约定不一致**，
必须先解决才能自动化：

* B.24 写 $\Phi(x\mathcal L):=x\Lambda$，其中 $x$ 是 $V$ 的行向量（长 $n$）。但 $x\mathcal L$ 要合法，
  就得把 $\mathcal L$ 读成 $n\times q$；而 B.37 又写 $W=\mathcal LV\le\mathbb C^q$（列约定，$\mathcal L$ 是 $q\times n$）。
  两种读法下 $W$、$\iota$、$P_\Phi$ 的形状不同。
* 这不是笔误问题：$\Lambda$ 满足 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$（$\Lambda$ 为 $q\times q$），
  只有当 $x$ 是**长为 $q$** 的行时 $x\Lambda$ 才有意义；而 $x\mathcal L$ 在 $q\times n$ 约定下是长 $n$ 的行。
  正确的对应应是"$x$ 为 $\mathbb C^q$ 的行、$x\mathcal L\in\mathbb C^n$"（即 $W\subseteq\mathbb C^n$），
  与 B.37 现在写的 $W\le\mathbb C^q$ 相反。

**待办**：把 B.17/B.24/B.37 三处的 $W$、$\iota$、$\Phi$ 统一到同一约定（建议列约定：$\mathcal L:\mathbb C^n\to\mathbb C^q$、
$W=\mathcal LV\le\mathbb C^q$、$\Phi(w)=\Lambda^{\mathsf T}v$ 其中 $w=\mathcal Lv$），并同步改 B.24 的公式。
在此之前的任何"实例计算"都可能算错对象——本轮已中止一次。

## Task 2 的第一步：参数化结构（$R\mapsto\Phi_R$ 的代数依赖）

设 $\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}$。项目里 $(5a)$ 的标准等价形式是存在
$\Lambda\in\mathbb C^{q\times q}$、$G_0,G_1\in\mathbb C^{q\times p}$ 使
$$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA.\qquad(\ast)$$

**引理 1（$(\ast)$ 是双线性的）.** $(\ast)$ 关于 $R$ 与 $(\Lambda,G_0,G_1)$ **分别线性**：
左端含 $RA$（$R$ 的一次项），右端的 $\Lambda\mathcal L=\Lambda\begin{bmatrix}L_0\\R\end{bmatrix}$ 含 $\Lambda R$（双线性项），
其余项各自线性。因此：

* **固定 $R$** 时，$(\ast)$ 是 $(\Lambda,G_0,G_1)$ 的**仿射线性方程组**（系数含 $R$）；
  其解集是仿射子空间，$\Lambda$ 在其中唯一到"零化 $\mathcal L$ 的映射"为止；诱导到 $W=\mathcal LV$ 上的 $\Phi$ 唯一到"零化 $W$ 的映射"为止；
* **固定 $(\Lambda,G_0,G_1)$** 时，$(\ast)$ 是 $R$ 的线性方程组。

**引理 2（可容许集是构造集）.** 设 $R$ 变化。$(\ast)$ 的可解性是增广矩阵的秩条件，故
$$\mathcal A:=\{R:\ (\ast)\ \text{可解}\}$$
是 $\mathbb C^{(q-r)\times n}$ 中的**构造集**（有限个秩条件的并交；秩 $=k$ 是局部闭的）。
由项目已知的等价（B.28(a)/B.10 的 $\Lambda$-分解），$\mathcal A$ 恰是满足 $(5a)$ 的 $R$ 的集合。

**引理 3（$\Phi_R$ 的代数依赖）.** 在 $\mathcal A$ 上，$\Lambda$ 由 $(\ast)$ 解得（取任一广义逆），故 $\Lambda$ 的条目是 $R$ 的**有理函数**；
$\Phi_R=\Lambda|_W$ 亦然。于是 $P_{\Phi_R}(\lambda)=\lambda\iota_R-\Phi_R$ 的条目是 $(\lambda,R)$ 的有理函数，
其极大子式的 $\gcd$ 的系数是 $R$ 的有理函数，"$\deg\Delta=0$"是 $\mathcal A$ 上的**构造条件**。

**推论（与 G.1 一致）.** 上述构造性说明 $\{R:\ (5b)\ \text{成立}\}$ 是构造集，故
$\mathrm{DEC}\in\exists\mathbb R$ 的编码与这里的代数结构相符；但构造性**不等于**可判定性，
选候选的复杂度仍开放（专家第四轮 §5.5、§9.1 优先级 2）。

**由此得到的参数化问题（Task 2 本体，未解）.** 令
$$\Delta_R(\lambda):=\gcd\{\text{全部 }\rho\times\rho\text{ 极大子式 of }P_{\Phi_R}(\lambda)\},$$
把 $\Delta_R$ 的系数看成 $R$ 的有理映射的像，问：
1. 像空间与"常数 gcd 轨迹"能否用一个**显式的代数条件**（而非 $\exists\Theta$）刻画？
2. 若 $\Phi_R$ 只经由某个低维不变量（例如 $\Lambda$ 在 $W$ 上的限制 + 商上的作用）依赖 $R$，
   能否把参数化降到该不变量上（专家 Task 2 的"内蕴参数空间"）？

## 待办（按专家 §9.1 优先级 1）

**证明行列式因子与 B.17 的 Kronecker 不变量的精确关系**：
$$\Delta_{P_\Phi}(\lambda)\ \leftrightarrow\ \bigl(\text{永久核 }S,\ \text{右最小指标},\ \text{有限初等因子}\bigr),$$
使统一定理成为"结构 → 谱 → 几何 → 代数"的闭环。这是专家列的 Task 1。
