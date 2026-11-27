# 回复：对 Report 110 的项目审查意见（转录）

> 说明：专家回复以正文形式给出（非文件），此文件为**机械去转义后的完整转录**，
> 保留其全部裁决、建议与问题；LaTeX 转义已还原为 `$…$`。

## 总体判断

方向正确，取得实质进展：研究已从 $c=1$ 超平面层进入 $c=2$ 二维核层，并开始形成一般 $c$ 的统一结构理论。
最有价值的三项成果：**(1)** 纠正 layer index 与维数关系的混淆；**(2)** $c=2$ 时把高维纤维压缩成至多一维像空间；
**(3)** 建立固定 $c=2$、简单谱、$K_0$-split 下的精确多项式时间算法框架。

但不建议现在把 110 的全部结论视为可投稿状态：

- 结构理论：有明显进展，核心方向正确；
- $c=2$ 复杂度定理：有独立论文潜力，但需完成若干关键证明审计；
- A.1：基本思路正确，但需把映射、空间与行向量约定写得更严格；
- **A.2：存在需重点核查的谱类型问题，不能直接接受目前表述**；
- **三值算法：算法契约与精确可判定性之间存在逻辑张力，需优先解决**；
- 一般 $c$：主要是结构性框架，尚不能视为已取得一般参数化复杂度结果。

并特别肯定：**没有再试图用已被推翻的假设简化问题，而是把 unrestricted layer 与 $K_0$-split layer 明确分开**。

## 一、layer 的定义终于统一（最基础也最重要）

统一采用 $\rho=\rank H=\dim\pi_{K_0}(V)$、$c=k-\rho$、$t=q-\rho$，故 $q=\rho+t$、$c-t=k-q$；
$D=\ker H=K_0\cap V^\perp$、$\dim D=c$、$\dim(V\cap K_0^\perp)=t$。三量必须严格区分
（$D$ 的维数 $c$；$V\cap K_0$ 的维数**不一定**等于 $\rho$；$V\cap K_0^\perp$ 的维数 $t$）。
$\omega=\rank(LN)=\rho$ 而**不是** $\dim(V\cap K_0)$ —— 正确。

**split 条件必须独立保留**：split 下才有 $M(D)\subseteq D$；unrestricted 下不能由 (5a) 推出。
报告给的 $c=2$ 反例证明它**不是无害的归一化**。

**建议**：split 与 unrestricted 作为两个不同研究问题；**今后所有定理都加范围标识**
（U = unrestricted；S = $K_0$-split；U+S = 两者都成立），避免后续论文再次混淆。

## 二、II.2 固定核空间后的纤维结构（$c\ge2$ 的关键）

unrestricted：$\mathcal F_D=\{V\in\Gr(q,U_D^\perp):V_0\subseteq V,\ K_0\cap V^\perp=D\}$，$U_D=D+AD$，
exactness 条件 $K_0\cap(D+AD)=D$ —— 仅 $D\subseteq K_0\cap V^\perp$ 不够。

split：$V=D^{\perp_{K_0}}\oplus W$、$W_0\subseteq W\subseteq T_D$、$T_D=K_0^\perp\cap(A_{21}D)^\perp$，
$\mathcal F_D^{\rm split}\simeq\Gr(t-w_0,T_D/W_0)$，维数 $(t-w_0)((n-k)-r(D)-t)$，
非空 $w_0\le t\le(n-k)-r(D)$。**这个结果非常好**：把 $q\times n$ 自由设计矩阵的问题变成 Grassmannian 上的子空间选择，
且清楚分离"核方向 $D$ 的选择"与"固定 $D$ 后的纤维选择"。

**预设行条件的修正尤其重要**：不能只用 $W_0\subseteq W$，还必须限制底空间
$P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}$（即 $D\perp P_{K_0}(V_0)$），底空间变成
$\mathcal B_{\rm pres}=\{D\in I_c(M):P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}\}$。
遗漏它时，即使在纤维上找到含 $W_0$ 的子空间，也不意味着能与预设行块组合成合法观测器。

**建议**：把 II.2 作为后续论文的核心基础定理；**unrestricted 与 split 纤维分别整理成独立命题，不要混在一个证明里**。

## 三、II.5 Image reduction 是最有潜力的创新点

$\phi_w(u)=\langle w,A_{21}u\rangle$、$\Phi(W)=\{\phi_w:w\in W\}$、$\Phi(W)\subseteq D^\circ$、
$\dim D^\circ=c$ ⟹ $\dim\Phi(W)\le c$。即：位于高维空间的自由子空间 $W$，对谱条件的影响只能通过至多 $c$ 维像空间体现。

### 3.1 对 A.1 的审查

$\Psi_\lambda(V)=\Psi_\lambda(P)+\Phi(W)$，$P=D^{\perp_{K_0}}$，$\Psi_\lambda(v)=\lambda h_v-h^A_v$；
对 $w\in W\subseteq K_0^\perp$ 有 $h_w=0$、$h^A_w=\phi_w$，故 $\Psi_\lambda(w)=-\phi_w$（**负号不能丢**），
再由 $-\Phi(W)=\Phi(W)$ 得恒等式。**核心代数思路正确**，但建议两处形式化修正：

1. **明确 $h_v,h^A_v$ 的定义域**：$h_v:K_0\to\mathbb R,\ h_v(x)=\langle v,x\rangle$；
   $h^A_v:K_0\to\mathbb R,\ h^A_v(x)=\langle v,Ax\rangle$；再用 $N:\mathbb R^k\to K_0$ 的基变换表示成 $\mathbb R^k$ 上的行向量。
   避免 $K_0^*$ 与 $\mathbb R^k$ 之间的识别被隐藏。
2. **明确 $A=M+A_{21}$ 是针对 $K_0$ 上的输入**：$A|_{K_0}=P_{K_0}A|_{K_0}+P_{K_0^\perp}A|_{K_0}$，
   两者值域不同，不能不加说明地当作同一空间上的矩阵相加。

补上这两点，A.1 可作为一个干净的通用引理。

### 3.2 意义远不止降低变量数

它揭示：**谱条件不关心 $W$ 本身，只关心 $\Phi(W)$**——若 $\Phi(W_1)=\Phi(W_2)$，则对谱条件影响完全相同，
故可按 $\Phi$ 的纤维商化设计空间。建议称为
**Image-space reduction of the spectral feasibility condition**，作为 $c=2$ 论文的核心创新之一。

## 四、$c=2$ 的突破：真正可发表的复杂度结果

$\dim D=2$ ⟹ $\dim D^\circ=2$ ⟹ $\Phi$ 只有 $\dim=0,1,2$，即 $\{0\}$、$\mathbb P(D^\circ)$、$D^\circ$；
中间是一维参数。对像直线 $\Phi(s)=\span(\phi_0+s\phi_1)$ 参数化后，铅笔中**只有一行**随 $s$ 变，故
$\deg_s m_I\le1$、$\deg_\lambda m_I\le\omega$——这是复杂度下降的直接原因。

固定 $c=2$ 的多项式时间定理（简单谱 + split）有独立学术价值，但**目前还不能当作已完成结果**，
因为 A.2 与三值算法的逻辑还需审计。

## 五、A.2 是当前最需要认真检查的地方

### 5.1 必须区分 simple spectrum 与 real simple spectrum（最重要）

simple spectrum 只意味着复特征值互异，**不意味着都实**。例：$M=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$，
特征值 $\pm i$，无实特征向量，但实不变 2-子空间是 $D=\mathbb R^2$。
故不能把 simple spectrum 下的所有二维不变子空间都描述成两个实特征向量张成。必须分两支：

- **情况 A**：两个不同实特征值，$D=\span_{\mathbb R}\{v_\alpha,v_\beta\}$；
- **情况 B**：一对共轭复特征值 $\alpha=a+ib$，$z=u+iw$，则 $D=\span_{\mathbb R}\{u,w\}$。

两类的代数表示不同。报告 II.3 提到共轭对，但 A.2 主要用实根 $\alpha,\beta$ 描述——**必须统一**。
建议 A.2 明确拆两支，并对第二种给出实部/虚部构造、所在实代数数域的次数与高度界。
**不能因为最终设计矩阵是实数，就认为整个计算只需实根。**

### 5.2 数域次数界

两实特征值、来自次数 $d_i,d_j$ 的不可约多项式：$[\mathbb Q(\alpha,\beta):\mathbb Q]\le d_id_j$（含 $i=j$ 时 $\le d_i^2$），
故 $\le k^2$ ✓。但涉及共轭复根时必须明确：用哪个数域、实部/虚部是否在该域中、所选嵌入如何表示、
如何确保得到正确的实不变子空间。不要只写 "only real embeddings are used"，要给出具体数域构造——
否则审稿人会问：究竟在复代数数域还是实代数数域中计算？两种表述的复杂度分析需明确衔接。

### 5.3 代数数高度

$\text{heights}=\mathrm{poly}(n,\tau)$ 可能成立，但不能仅由矩阵元素高度多项式直接得出。需完整展示：
$M$ 的系数位长 → 特征多项式系数位长 → 不可约因子系数高度 → 代数根的次数与高度 → 特征向量坐标高度 →
不变子空间基高度 → $A_{21},T_D,\phi,\Phi_0$ 高度 → gcd/subresultant 的系数增长。
**"次数 $\le k^2$"与"系数位长 $=\mathrm{poly}(n,\tau)$"是两个不同命题**，应分别给界再推总复杂度。

建议 A.2 改写为正式技术引理：

> **Lemma (Arithmetic complexity of invariant-plane enumeration).** $d_L\le k^2$、$h(L)\le\mathrm{poly}(n,\tau)$、$\#D=O(k^2)$。

再给：

> **Theorem (Bit complexity of the fixed-$c=2$ algorithm).**

**A.2 暂不建议直接定稿。**

## 六、Q3 三值算法：可作为部分算法，不可直接代替精确判定

**必须明确论文声称的是精确判定算法，还是带证书的部分判定算法**——两者不是同一结论。

### 6.1 一个可进一步利用的关键事实

固定 $D$、split 纤维中 $V=D^{\perp_{K_0}}\oplus W$、$W\subseteq K_0^\perp$，故 $H=LN$ 中来自 $W$ 的行**全为零**，
$D$ 部分秩固定 $k-c=\rho$ ⟹ 对每个真正属于 split 纤维的设计，$\rank H=\rho$ **自动成立**。
这意味着：在每个正确构造的纤维 chart 中，admissibility 条件**可能自动满足**。
结合 II.4 的判据 ⟹ 应检查：**$c=2$ 的 image-line chart 中能否证明所有实参数点都自动 admissible？**
若可以，`undecided` 分支可能完全消失，算法升级为真正的 FEASIBLE / INFEASIBLE 精确判定。

### 6.2 需特别检查的地方（不能只查一般 Grassmannian chart）

$\phi_0+s\phi_1$ 是否可能为零；仿射 chart 的分母是否可能为零；chart 的排除集合是否被其他 chart 覆盖；
$\Phi_0\subseteq\Phi(s)$ 是否对所有参数自动成立；image realizability 的维数不等式是否在整卡上成立；
对应的 $W$ 是否始终存在。若全部通过，每张有效 chart 的参数域是非空实代数开集，实点稠密性可直接使用；
若存在无法排除的特殊参数点，应作为单独 stratum 处理，而不是返回 `undecided`。

### 6.3 建议分层判定，而不是保留模糊的 undecided

$\mathcal X=\mathcal X_{\rm generic}\sqcup\mathcal X_{\rm exceptional}$：generic 用函数域 gcd，exceptional 单独精确计算，
最终仍输出 FEASIBLE 或 INFEASIBLE。若确实存在无法处理的 exceptional locus，可保留三值，但论文必须表述为
**a certified partial decision procedure**，不能称 exact decision algorithm。
**更建议优先尝试消除 undecided 分支**——若固定 $c=2$ 的多项式时间精确判定成立，论文理论价值明显提高。

## 七、II.8 一般 $c$：方向正确，但不要过早声称已建立一般理论

$\Phi\in\Gr(j,D^\circ)$、$\max_j j(c-j)=\lfloor c^2/4\rfloor$ 是好框架，说明 $c=2$ 不是孤立技巧。
但有三个不同困难：**(1)** 底空间枚举复杂度（重数时可能成正维簇，维数可达 $c(d_\lambda-c)$，
不能认为 $\#I_c(M)=O(k^c)$ 就解决一般情形）；**(2)** 像空间的选择（$c$ 增长时 Grassmannian 维数也增长，
不能仅凭 $\dim D^\circ=c$ 就认为可用固定参数算法）；**(3)** image realizability 需转化为可计算的参数化。

**建议把 image-space feasibility 与 image realizability 分成两个命题**，以看清一般 $c$ 的困难来自谱条件还是原像空间维数约束。

## 八、按此顺序处理的三个技术问题

**Priority 1（必须先解决）完成 $c=2$ 定理的严格证明审计**：(1) A.2 中实谱与共轭复谱的统一处理；
(2) 数域次数与代数数高度的严格界；(3) 三值能否升级为二值精确判定；(4) 每张 chart 的 admissibility 与覆盖性；
(5) gcd 算法的完整位复杂度。这是目前最接近形成完整论文的部分。

**Priority 2** 一般 $c$ 的 Q-B：能否消去 $\exists\Phi\subseteq D^\circ$，得到只依赖诱导映射与铅笔的秩条件。

**Priority 3（中长期）** 底空间 $I_c(M)$ 的复杂度：利用 Jordan 结构、几何重数、不变子空间格、代数簇分解、
特征子空间直和结构，避免直接枚举所有 $c$ 维不变子空间。

### 8.1 为什么 Q-B 先于 Q-A

Q-B 直接处理 image reduction 之后剩下的核心谱约束，Q-A 处理底空间枚举。若 Q-B 得到简洁秩判据，
即使暂不解决枚举问题，也能得到"给定 $D$ 的高效判定算法"；反之没有 Q-B，即使枚举更快，每个 $D$ 仍要高维谱可行性。

## 九、建议把 $c=2$ 单独写成一篇新论文

不要等一般 $c$ 全部解决再投稿。已有完整逻辑链：split-layer structure → invariant-plane base →
Grassmannian fiber → image-space reduction → one-dimensional spectral parameter → exact algebraic decision。
标题建议二选一，**倾向第二个**：
*Image-Space Reduction and Polynomial-Time Feasibility for Functional Observers with a
Two-Dimensional Compressed Kernel*。

### 9.1 建议章节

I 引言 · II layer 结构（统一 $c,t,\rho$，区分 split/unrestricted）· III 固定核纤维（两种纤维 + 预设行）·
IV image-space reduction（核心）· V 二维核（$I_2(M)$ 的简单谱分类）· VI 精确算法（image-line charts、gcd、证书）·
VII 位复杂度（数域、系数高度、subresultant）· VIII 例子与局限（反例、复杂度边界、一般 $c$）。
**III、IV、VI、VII 是核心**；**A.1、A.2 不应只作附录技术细节**，它们承担主要定理的证明责任。

### 9.2 与前三篇的关系

不要把新论文简单称作 Paper IV 的延续，而应强调它解决了此前未解决的特殊层复杂度问题。
四篇分工：Paper I 一般阶数存在性与复杂度；Paper II 最小阶与构造；Paper III 一维压缩核几何；
新论文 二维压缩核的像空间降维与精确复杂度。

## 十、需补充的两类证据

### 10.1 系统性精确测试集（不要只留一两个反例）

| 实例类型 | 目的 |
|---|---|
| 简单实谱 | 验证有限底空间枚举 |
| **含共轭复特征值** | **验证 A.2 的复谱处理（目前最值得检验）** |
| 重复实特征值 | 展示底空间变正维 |
| 不同 $\rank A_{21}$ | 验证不同纤维维数 |
| 非平凡预设行块 | 验证底空间筛选 |
| $\Phi_0=0$ / $\Phi_0=D^\circ$ | 检查完整/唯一像空间分支 |
| realizability 取等 | 检查维数不等式边界 |
| 不可行 / 可行谱条件 | 验证 gcd / Bézout 证书 |

### 10.2 Lean 形式化应瞄准真正的结构定理

优先：(1) $c=k-\rho$ 的统一维数关系；(2) unrestricted 与 split 的区别；(3) fixed-$D$ fiber 结构；
(4) $\Phi(W)\subseteq D^\circ$；(5) **A.1 的完整 row-space identity**；(6) realizability 两不等式；
(7) $c=2$ 的三个 image-rank 分支。**特别是 A.1**——它是从高维 $W$ 过渡到低维 $\Phi(W)$ 的核心等式。
不建议为形式化覆盖率把未形式化的代数数复杂度部分包装成已验证结果。

## 十一、对四个问题的直接回答

| 问题 | 判断 | 建议 |
|---|---|---|
| Q1 A.1 是否正确 | 核心推导正确 | 补齐空间定义、投影与行向量约定 |
| Q2 A.2 次数与高度界 | 实特征值分支次数界正确；整体论证需补全 | 单独处理共轭复特征值、实代数表示与高度传播 |
| Q3 三值契约 | 可作为部分算法，不足以支持精确判定定理 | 优先证明 undecided 不发生，或单独处理 exceptional strata |
| Q4 Q-B 还是先写论文 | **先完成并写出 $c=2$ 论文** | Q-B 作为下一阶段主攻 |

**不要现在继续无限制扩大一般 $c$ 的研究范围**；$c=2$ 已出现明确理论突破且可独立成文，应先固定。

## 十二、最终评价与执行顺序

项目已不只是研究某一种设计算法，而在形成一个系统性方向：
**Computational Geometry and Complexity of Functional Observer Design**——
利用压缩子空间、核空间几何与像空间降维，把高维矩阵设计问题转化为低维代数几何上的精确可行性问题。

**建议执行顺序**：
1. 完成 A.1 的严格证明版本，固定所有空间、映射与符号约定；
2. 彻底审计 A.2（共轭复特征值、数域、高度界）；
3. 解决三值算法的 undecided 问题，争取真正的二值精确判定；
4. 完成 $c=2$ 的完整位复杂度证明；
5. 把 $c=2$ 结果独立写成论文；
6. 再回到 Q-B 推进一般 $c$ 的 image-space elimination。

**第 3、4 项是能否把 $c=2$ 提升为有说服力的理论计算论文的关键。**
总体态度积极：110 是实质性进展，$c=2$ 的 image-space reduction 比单纯推广 $c=1$ 的特征向量参数化
更有长期研究价值，可能成为推广到一般 $c$ 的真正理论支点；但在正式宣称固定 $c=2$ 的多项式时间精确判定定理之前，
必须先把上述证明缺口关闭。
