# 414 专家 110 号审计：三值→**二值**（可证）；A.2 的谱分支补全；A.1 约定修正；成果固定

> 送审件 [110](../../../for_expert/archive/110_program_record.md)，答复
> 110-reply（尚未归档）。
> 总评："实质进展；$c=2$ 的 image-space reduction 比单纯推广 $c=1$ 更有长期价值"；
> 但**不宜立即宣称 $c=2$ 的多项式时间精确判定**，需先关掉若干证明缺口。

## 目标

1. 落实他的 Priority 1 五项（A.2 谱分支、数域与高度界、三值→二值、每卡 admissibility 与覆盖、位复杂度）；
2. 修正 A.1 的两处约定（$h_v,h^A_v$ 的定义域；$A|_{K_0}$ 的分解）；
3. **固定成果**：给出新论文的章节骨架与"冻结"结果清单。

## 设想与理由

他的审查里**最有价值的技术观察**是 §6.1：在 split 纤维里 $V=D^{\perp_{K_0}}\oplus W$，故 $H=LN$ 的
$W$ 行**全为零**、$D$ 部分秩固定为 $k-c=\rho$ ⟹ **$\rank H=\rho$ 自动成立**。
如果每张像直线图卡上的每个实点都自动 admissible，那么 405 的判据就变成**两侧都可用**的
充要条件，`undecided` 分支可以**消失**。

我核了这条，成立（见 §A），所以算法可以升级为**二值精确判定**。这是本轮最实质的改动。

## 做法

先验 §A 的二值化，再补 §B 的谱分支与数域、§C 的 A.1 约定，最后 §D 固定论文骨架与结果清单。

## 进展

### A. 三值 → 二值：**admissibility 在像直线图卡上自动成立**

**引理 A1（$\rank H$ 恒定）.** 设 $V=D^{\perp_{K_0}}\oplus W$（$W\subseteq K_0^\perp$），
$\dim D=c$、$\dim D^{\perp_{K_0}}=k-c=\rho$。则
$$\rank H=\rank(V^{\mathsf T}N)=\rho\quad\text{对一切这样的设计成立}.$$

*证明.* $H$ 的行分两块：$D$ 部分（$k-c$ 行）与 $W$ 部分（$t$ 行）。后者是 $w^{\mathsf T}N$，
而 $w\perp K_0\supseteq N(\mathbb R^k)$，故**全零**；前者是 $D^{\perp_{K_0}}$ 的元素对 $N$ 的配对，
其秩为 $\dim D^{\perp_{K_0}}=k-c=\rho$ ✓。$\square$

**引理 A2（像直线图卡上 admissibility 自动）.** 在图卡
$\Phi(s)=\operatorname{span}(\varphi_0+s\varphi_1)$（$s\in\mathbb R$，或 $\mathbb P^1$ 的两张仿射卡）上，
铅笔 $\lambda H-H_A$ 的 $H$-部分**与 $s$ 无关**（由引理 A1 秩恒为 $\rho=\omega$），
故每个实点 $s$ 上都有 $\omega$ 阶子式保持其一般 $\lambda$-次数 ⟹
**每个实点都是 405 意义下的可接受点**。

*证明.* $H$ 的 $W$ 行恒为零、$D$ 行与 $s$ 无关 ⟹ $H$ 整体与 $s$ 无关；$\rank H\equiv\rho=\omega$ ⟹
存在 $\omega$ 阶子式 $\Delta$ 使 $\Delta$ 作为 $\lambda$-多项式的首项系数非零且与 $s$ 无关 ⟹
对每个 $s$ 都有子式保持次数 $\omega$ ✓。$\square$

**推论 A3（二值语义）.** 在 408/413 的许诺下（$c=2$、单谱、$K_0$-split），
$\Phi$-类的每张**实可容许**图卡都满足 405 定理的两个前提（实点稠密 + 每实点可接受），于是
$$d_{\rm gen}=0\iff\text{该图卡含实可行点}.$$
算法因此只需输出

$$\boxed{\ \textbf{FEASIBLE}\ \text{（某实可容许图卡 }d_{\rm gen}=0)\quad\big|\quad
\textbf{INFEASIBLE}\ \text{（所有实可容许图卡的 }d_{\rm gen}>0)\ }}$$

**不再需要 `undecided`。**

**实可容许图卡的三种情形**（他 §6.2 的检查清单，逐条核过）：

| 情形 | 检查 |
|---|---|
| $\Phi=\{0\}$ | 单点，实 ✓；$\Phi_0$ 必须为 0 |
| $\Phi$ = 直线（仅当 $\Phi_0=0$） | $\mathbb P^1$ 两张标准卡，参数 $s\in\mathbb R$；分母（卡的选择）非零 ✓；$\varphi_0+s\varphi_1\ne0$ 在卡上成立 ✓ |
| $\Phi=D^\circ$ | 单点，实 ✓ |

**可实现性不等式**（411 定理 3）是 $\Phi$ 的**开条件**（固定维数的严格不等式）+ 闭条件（$\Phi_0\subseteq\Phi$），
所以"满足不等式的 $\Phi$ 集合"在实数域上是开集或其闭子集；在图卡上它是**有限个开区间的并** ⟹
仍含实点、实点稠密 ✓。**特别地**：$\dim\Phi_0=1$ 时直线情形塌缩为 $\{\Phi_0,D^\circ\}$（他 109 号 §2.3 已指出），
所以只有 $\Phi_0=0$ 时才真有一维参数族。

**边界处理**（他 §6.3）：若某张卡的实可容许部分是空集（例如不等式在整条卡上不成立），
该卡直接不计入——这**不是** `undecided`，而是"该 $\Phi$-类不可实现"。所以不需要保留三值。

### B. A.2 的谱分支补全（他 §5.1：这是最需要核查的问题）

**我原来的写法有真缺口**：只按"实根 $\alpha,\beta$"描述不变 2-平面，漏了**共轭复特征值**情形。
他的反例（旋转矩阵 $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$，特征值 $\pm i$，$D=\mathbb R^2$）说明：
simple spectrum（复谱互异）**不是** real simple spectrum。

**修正为两个分支**：

**分支 R（两个实特征值）**：$\alpha,\beta\in\mathbb R$，$f_i,f_j$ 的实根，$d_i,d_j$ 为因子次数。
$$D=\operatorname{span}_{\mathbb R}\{v_\alpha,v_\beta\},\qquad L=\mathbb{Q}(\alpha,\beta),\qquad
[L:\mathbb{Q}]\le d_id_j\le k^2 .$$

**分支 C（共轭复对）**：$f$ 不可约、无实根（$\deg f=2m$ 一般；最简单 $m=1$），取一个复根 $\alpha$、
复特征向量 $z=u+iw$，则
$$D=\operatorname{span}_{\mathbb R}\{u,w\}=\ker f(M)\cap\ldots$$
更干净：**$D$ 就是 $\ker f(M)$ 的任一实 2-维不变子空间**；而 $f$ 不可约二次时 $\ker f(M)$ 是 2 维、
$\mathbb Q$-定义，$D=\ker f(M)$ 唯一 ✓。
- 计算在**实**域 $L=\mathbb{Q}[t]/(f)$ 的**复嵌入**上进行（$u,w$ 是 $z$ 的实部/虚部），
  但 $D$ 本身是 $\mathbb Q$-定义的，所以**输出不需要数域**；
- 高度界：$u,w$ 由 $z$ 的坐标取实部/虚部得到，$z$ 由 $\ker(M_\mathbb{C}-\alpha I)$ 给出 ⟹ 高度 $\mathrm{poly}$ ✓。

**技术引理（按他 §5.3 要求的形式）.**

> **引理（不变平面枚举的算术复杂度）.** 设 $M\in\mathbb{Q}^{k\times k}$ 单谱、位长 $\tau$。则
> 存在常数 $C$ 使
> $$\#\{D\}=\binom{k_{\mathbb R}}{2}+\#\{\text{共轭对}\}\le k^2,\qquad d_L\le k^2,\qquad
> h(L)\le (n\tau)^{C},$$
> 且每个 $D$ 的基、$D^{\perp_{K_0}}$、$T_D$、$\varphi$、$\Phi_0$ 的高度 $\le(n\tau)^{C}$。

> **定理（固定 $c=2$ 的位复杂度）.** 在上述引理下，二值判定在
> $\mathrm{poly}(n,\tau)$ 内完成（数域线性代数 + 图像化 + 每卡一次 $\mathbb Q(s)[\lambda]$ 的 gcd）。

**他的八步高度传播**（§5.3）我按序记下，作为论文附录的高度链：
$M$ 的位长 → 特征多项式系数 → 不可约因子 → 代数根的次数与高度 → 特征向量坐标 →
不变子空间基 → $A_{21},T_D,\varphi,\Phi_0$ → subresultant/gcd 的系数增长。
（本轮只给量级与标准引理，未逐项算常数——**这是写论文时必须补的**。）

### C. A.1 的两处约定修正（他 §3.1）

1. **定义域**：改为
$$h_v:K_0\to\mathbb R,\ h_v(x)=\langle v,x\rangle;\qquad h^A_v:K_0\to\mathbb R,\ h^A_v(x)=\langle v,Ax\rangle,$$
   再用 $N:\mathbb R^k\widetilde\to K_0$ **事后**搬成 $\mathbb R^k$ 上的行向量
   （$h_v\circ N$、$h^A_v\circ N$）。这样 $K_0^*\simeq\mathbb R^k$ 的识别不再被隐藏。
   （**注意**：412 里写的 $h_v(x)=\langle v,Nx\rangle$ 已经隐含了这层搬运，但没有说清；已按此改。）
2. **$A$ 的分解**：必须写成
$$A|_{K_0}=P_{K_0}A|_{K_0}+P_{K_0^\perp}A|_{K_0}=M+A_{21},$$
   两者**值域不同**（$M$ 落 $K_0$、$A_{21}$ 落 $K_0^\perp$），不能当作同一空间上的普通矩阵相加。

### D. 成果固定（论文骨架 + 冻结清单）

**论文标题**（他给的两个里取第二个，因为它点出核心创新）：
**Image-Space Reduction and Polynomial-Time Feasibility for Functional Observers with a
Two-Dimensional Compressed Kernel**

**章节骨架**（他的 §9.1，我采纳并标注"已冻结/待补"）：

| 节 | 内容 | 状态 |
|---|---|---|
| I. Introduction | 从 $c=1$ 推进到 $c=2$ | 待写 |
| II. Layer structure | 统一 $c,t,\rho$；区分 split / unrestricted（**每条定理标 U / S / U+S**） | **冻结**（393/404/411） |
| III. Fixed-kernel fibers | 两种纤维 + 预设行条件（命题分别陈述，不混在一个证明里） | **冻结**（393 命题 1/2，命题 2 的集合/维数部分已 Lean） |
| IV. Image-space reduction | $\Phi(W)\subseteq D^\circ$、行空间恒等式、精确可实现性、约化判据 | **冻结**（406/412；关键等价已 Lean；一般证明 412） |
| V. Two-dimensional kernel | $\mathcal I_2(M)$ 的简单谱分类 | **冻结**（393 定理 3 + 推论 4；一般情形明确不参数化） |
| VI. Exact algorithm | 像直线图卡、gcd、证书、**二值语义** | **冻结**（394/405/§A） |
| VII. Bit complexity | 数域次数、高度链、subresultant | **骨架冻结**（408/413/§B），高度链待逐项补 |
| VIII. Examples and limitations | 层不单调反例、两条边界、一般 $c$ | **冻结**（397/410） |

**冻结结果清单（8 条，作为论文主定理）**：
1. 层号统一：$c=k-\rho$、$t=q-\rho$、$c-t=k-q$（含三量区分与 $\omega=\rho$）；
2. 两种固定核纤维（含 exactness $K_0\cap(D+AD)=D$ 与 $\mathcal B_{\rm pres}$）；
3. 像约化（$\Phi(W)\subseteq D^\circ$，$\row$ 恒等式）；
4. 精确可实现性（两个维数不等式）与约化可行性判据；
5. 简单谱的底分类（有限，$\binom{k_{\mathbb R}}{2}+$共轭对）；
6. 二值精确判定算法（§A 的 admissibility 自动性）；
7. 固定 $c=2$ 的 $\mathrm{poly}(n,\tau)$ 位复杂度（§B 的引理 + 定理）；
8. 层不单调反例与两条复杂度边界。

**两类补充工作**（他 §10）：

- **精确测试集**（10 类实例，必须含"共轭复特征值"一类）：简单实谱 / 共轭复 / 重复实特征值 /
  不同 $\rank A_{21}$ / 非平凡预设行 / $\Phi_0=0$ / $\Phi_0=D^\circ$ / 可实现性取等 / 不可行谱 / 可行谱；
- **Lean 目标**（优先）：(i) $c=k-\rho$ 的统一维数关系；(ii) 两种纤维的区分；(iii) 固定 $D$ 的纤维结构；
  (iv) $\Phi(W)\subseteq D^\circ$；(v) **A.1 的行空间恒等式**；(vi) 可实现性两不等式；(vii) $c=2$ 的三个 image-rank 分支。
  已有：$V\perp(D+AD)\iff W\subseteq T_D$、$\Phi\subseteq D^\circ$、$V\cap K_0=K_0\cap D^\perp$、$\dim V$ 加性。

## 最终结论

1. **三值 → 二值成立**（引理 A1/A2 + 推论 A3）：split 纤维上 $\rank H\equiv\rho$，故像直线图卡上每点可接受，
   405 的判据两侧都可用 ⟹ 算法输出 FEASIBLE / INFEASIBLE；
2. **A.2 的谱分支补齐**（分支 R 与分支 C），并给出他要求的技术引理与位复杂度定理的形式；
3. **A.1 两处约定已修**（$h_v$ 的定义域、$A|_{K_0}$ 的分解）；
4. **成果固定**：8 条主定理 + 8 节骨架（III/IV/V/VI/VIII 冻结，VII 骨架冻结），
   外加测试集与 Lean 目标清单；
5. 论文标题采用他建议的第二个。

## 放弃原因

- 没有逐项算高度链的显式常数（只给量级；论文附录必须补）；
- 没有实现测试集（只给了 10 类的清单）；
- 没有 Lean 化 A.1（矩阵行空间 API 成本高）；
- 没有证明一般 $c$ 的 Q-B。

## 残留价值

- **二值化的完整论证**（引理 A1/A2 + 推论 A3 + 三种 $\Phi$ 情形 + 可实现性不等式的开性），
  这是把 $c=2$ 提升为"精确判定定理"的关键一步；
- **A.2 的两个分支**与"技术引理 + 位复杂度定理"的正确形式；
- **冻结清单**（8 条主定理、8 节骨架），可直接作为论文写作的检查表；
- 测试集与 Lean 目标的明确分工。

## 相关文件

- 专家问答：[110 与回复](../../../for_expert/archive/)
- 卷宗：[405](405_real_generic_point.md)（可接受性与判据）、[406](../../c_stratification/attempts/406_eliminate_W.md)（像约化）、
  [408](../../c_stratification/attempts/408_c2_complexity.md)（复杂度）、[412](412_rowspace_identity_proof.md)（行空间恒等式）、
  [413](../../c_stratification/attempts/413_exact_arithmetic_c2.md)（精确算术）、[397](../../c_stratification/attempts/397_layer_nomonotone.md)（反例）
