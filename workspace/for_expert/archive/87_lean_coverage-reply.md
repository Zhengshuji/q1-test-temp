# 总体判断

这五个缺口的性质并不相同：G1–G3 是主定理证明链中的代数核心，G4 是把代数算法提升为严格 bit-complexity 结论所需的复杂度审计，G5 则是把数学判定条件与标准实代数几何复杂度类连接起来的编码正确性问题。

如果目标是让论文的主定理达到“Lean 内核检查了主要数学推导，只留下少量明确列出的外部复杂度事实”，我建议优先做：

1. G2：多项式 Bézout 的统一有界次数版本。
2. G3：矩形伴随矩阵构造，以及它与有限线性系统的等价。

这两项能直接支撑“谱条件对所有复数 \\(\lambda\\)”到“有限代数证书”的关键桥梁，而且可以复用已有的多项式环、行列式、伴随矩阵和线性代数基础设施。G1 很重要，但它主要支撑你们所强调的 Cauchy–Binet 压缩步骤；若暂时不形式化它，仍可把主定理的正确性证明与“避免枚举所有最大子式”的优化贡献分开处理。G4 不宜一开始就做成完整 Lean 形式化。G5 值得做一个精确的固定分支编码正确性定理，但不要把它误称为已经形式化证明了 \\(\exists\mathbb R\\) 归属。

下面逐项分析，并区分数学判断、形式化建议和需要在你们当前 Mathlib checkout 中进一步核实的 API 细节。

## 1. G1：矩形 Cauchy–Binet

你写的恒等式是正确的。设 \\(A\in K^{\omega\times k}\\)、\\(B\in K^{k\times\omega}\\)，其中 \\(K\\) 是交换环，则

\\[ \det(AB)= \sum\_{\substack{J\subseteq\\{1,\ldots,k\\}\\\\|J|=\omega}} \det(A\_{:,J})\det(B\_{J,:}). \\]

需要留意：这个形式的陈述通常要求 \\(\omega\le k\\)。若 \\(\omega>k\\)，左侧是一个秩不足的方阵乘积的行列式，右侧为空和，二者仍为零；但形式化时最好明确处理这一情形，或者把定理前提写成 \\(\omega\le k\\)。

### 1.1 是否可能在 Mathlib 中以别的名称存在？

你们搜索 `binet` 没有找到，不能据此断定没有相关结果。相关基础可能分散在：

- `Matrix.det_mul`：方阵行列式乘法；
- `Matrix.det_apply` 或行列式的 Leibniz 展开；
- `Finset` 上的子集、等势映射和有限求和；
- `AlternatingMap`、外幂或交替多线性映射。

但必须区分两件事：

- 有方阵行列式乘法定理，不等于已经有矩形 Cauchy–Binet；
- 有外幂或交替映射的基础定义，也不等于已经有你们需要的有限子集求和公式。

我不想在没有核对你们确切的 Mathlib 版本源代码和定理声明前，给出一个可能不存在的定理名。你们使用的是 Lean 4.35 对应的 checkout，API 名称尤其不应凭记忆猜测。就目前能够可靠给出的结论而言：应先按数学结构寻找，而不是继续只搜索 `binet` 这个字符串；但不能把“可能存在相关基础设施”当作“已有可直接复用的矩形定理”。

### 1.2 我建议的形式化路线：先做指标版，再做矩阵版

我不会把外代数作为第一条路线。对你们当前目标，最短、最容易调试的路线通常是：

1. 先证明有限指标集上的矩形 Cauchy–Binet；
2. 再用 `Fin` 索引和 `Matrix` 的子矩阵定义，把它包装成矩阵定理；
3. 最后才考虑把它抽象成外幂上的自然性定理。

设 \\(I,J\\) 是有限类型，\\(|I|=|J|=\omega\\)，中间指标集 \\(K\\) 的大小为 \\(k\\)。可以把矩阵写成有限函数，目标先写成：

\\[ \det\left(\sum\_{t\in K} A\_{it}B\_{tj}\right)\_{i,j\in I} = \sum\_{\substack{S\subseteq K\\\\|S|=\omega}} \det(A\_{i,s})\_{i\in I,s\in S} \det(B\_{s,j})\_{s\in S,j\in J}. \\]

实际证明可从行列式的 Leibniz 展开出发：

\\[ \det(AB) = \sum\_{\sigma\in\operatorname{Perm}(I)} \operatorname{sgn}(\sigma) \prod\_{i\in I} \left(\sum\_{t\in K}A\_{it}B\_{t,\sigma(i)}\right). \\]

展开乘积后，出现所有函数 \\(f:I\to K\\)。按 \\(f\\) 是否单射分类：

- 若 \\(f\\) 非单射，对应项在交替求和中相消；
- 若 \\(f\\) 单射，其像是一个大小为 \\(\omega\\) 的子集 \\(S\subseteq K\\)；
- 对同一个像 \\(S\\)，对所有枚举 \\(S\\) 的双射求和，恰好形成两个子行列式的乘积。

这条路线的难点不是数学，而是 Lean 中的有限求和重排、函数按像集分组，以及符号与排列求和的相消。建议把证明拆成几个独立引理：

- `sum_expand_det_mul`：行列式展开矩阵乘积；
- `noninjective_terms_cancel`：非单射项相消；
- `injective_terms_group_by_range`：单射项按像集分组；
- `rectangular_cauchy_binet`：合并得到最终定理。

### 1.3 什么时候才值得走外代数路线？

外代数路线有更好的概念统一性：

\\[ \bigwedge^\omega(AB) = \big(\bigwedge^\omega A\big) \big(\bigwedge^\omega B\big), \\]

而 Cauchy–Binet 可以看成这一恒等式在标准基下的坐标表达。

但它通常要求你先建立或复用：

- 外幂的基；
- 线性映射在外幂上的提升；
- 外幂标准基上的矩阵系数；
- 这些系数与子式之间的对应。

如果 Mathlib 已经有一套完整的外幂 API，这可能是长期更漂亮的方案；但若没有，为了一条 Cauchy–Binet 恒等式从头构造外代数，往往比直接做有限指标证明更重。

我的建议是：先做指标版 Cauchy–Binet，不要让 G1 阻塞 G2、G3。等你们确认是否需要把 Cauchy–Binet 推广到一般交换环、一般有限指标类型时，再决定是否抽象为外幂理论。

## 2. G2：\\(s\\) 个多项式的有界次数 Bézout

你提出的结论是正确的，但直接对 \\(s\\) 做归纳，并不能自动得到你需要的统一次数界。这里有一个值得明确的细节。

设 \\(K\\) 是代数闭域，且

\\[ f_1,\ldots,f_s\in K[X],\qquad \deg f_i\le\omega, \\]

并且这些多项式没有公共根。因为 \\(K\\) 代数闭，这等价于

\\[ \gcd(f_1,\ldots,f_s)=1. \\]

你们需要的结论是存在 \\(g_i\\)，满足

\\[ \sum\_{i=1}^s g_if_i=1, \qquad \deg g_i<\omega. \\]

这里先假定 \\(\omega\ge1\\)。如果 \\(\omega=0\\)，所有 \\(f_i\\) 都是常数；没有公共根意味着至少有一个 \\(f_i\\) 非零，此时存在常数系数 \\(g_i\\) 使线性组合等于 1。若严格要求 \\(\deg g_i<0\\)，这个表述本身就不合适，必须单独约定零多项式的次数，或把 \\(\omega=0\\) 独立处理。

### 2.1 不建议把“直接归纳”作为主要证明路线

假设你先令

\\[ d_j=\gcd(f_1,\ldots,f_j) \\]

并归纳构造

\\[ d_j=\sum\_{i=1}^j a_i f_i. \\]

再用两多项式 Bézout 得到

\\[ u d_j+v f\_{j+1}=d\_{j+1}. \\]

代入后，

\\[ d\_{j+1} = \sum\_{i=1}^j (u a_i)f_i+v f\_{j+1}. \\]

虽然两多项式 Bézout 可以控制 \\(u,v\\) 的次数，但这并不直接保证 \\(u a_i\\) 的次数仍小于 \\(\omega\\)。因此，你需要额外的次数约化论证。简单地说，“两两 gcd 的 Bézout 系数次数有界”不等于“迭代后的所有原始生成元系数次数仍有界”。

### 2.2 更干净的证明：先取两个一般线性组合

我更推荐下面这个证明，它恰好把 \\(s\\) 多项式问题约化成你们已经形式化的两多项式 Bézout。

因为没有公共根，对任意 \\(\alpha\in K\\)，至少一个 \\(f_i(\alpha)\ne0\\)。

先选择一个线性组合

\\[ F=\sum\_{i=1}^s a_i f_i \\]

使 \\(F\ne0\\)。它的根集是有限的。对每个 \\(F\\) 的根 \\(\alpha\\)，由于 \\(f_i\\) 没有公共根，向量

\\[ (f_1(\alpha),\ldots,f_s(\alpha)) \\]

不是零向量。因此，条件

\\[ \sum\_{i=1}^s b_i f_i(\alpha)=0 \\]

在系数向量 \\(b=(b_1,\ldots,b_s)\in K^s\\) 上定义一个真超平面。

由于 \\(F\\) 只有有限多个根，我们只需要避开有限多个真超平面。因此可以选择 \\(b\\)，使

\\[ G=\sum\_{i=1}^s b_i f_i \\]

在 \\(F\\) 的所有根处都不为零。于是 \\(F,G\\) 互素：

\\[ \gcd(F,G)=1. \\]

由于 \\(K\\) 是无限域，有限多个真超平面不可能覆盖整个 \\(K^s\\)，所以这样的 \\(b\\) 存在。

现在使用两多项式 Bézout：

\\[ UF+VG=1. \\]

对非零的 \\(F,G\\)，标准次数界可以取为

\\[ \deg U<\deg G\le\omega,\qquad \deg V<\deg F\le\omega. \\]

把 \\(F,G\\) 展开：

\\[ 1 = \sum\_{i=1}^s (Ua_i+Vb_i)f_i. \\]

令

\\[ g_i=Ua_i+Vb_i, \\]

由于 \\(a_i,b_i\\) 是常数，

\\[ \deg g_i<\omega. \\]

这就得到你们所需的统一次数界，而且完全避免了归纳过程中次数膨胀的问题。

### 2.3 Lean 形式化建议

可以把证明拆成：

1. `exists_nonzero_linear_combination`：存在非零线性组合；
2. `finite_roots_of_nonzero_polynomial`：非零多项式根集有限；
3. `exists_linear_combination_avoiding_roots`：选择第二个线性组合，避开第一个的全部根；
4. `coprime_of_no_common_root`：由根条件得到互素；
5. 调用已有的两多项式 Bézout；
6. 展开线性组合，构造 \\(g_i\\)，继承次数界。

这里有一个重要的形式化设计选择：不要把“存在一组系数避开有限多个超平面”做成多项式特有的定理。 它本质上是无限域上的有限个非零线性泛函不能同时覆盖整个向量空间。若你们把它抽象成线性代数引理，未来会更容易复用。

此外，如果你们最终的实际系数域是 \\(\mathbb R\\)，但无公共根条件是在 \\(\mathbb C\\) 上判断，最好在论文和 Lean 中都明确分层：

- 在代数闭域 \\(\mathbb C\\) 上证明互素与 Bézout；
- 若多项式原本具有实系数，再证明可以取实系数的 Bézout 证书，或者通过实系数 gcd / 欧几里得算法直接得到实系数证书。

不能在没有说明的情况下，把“在 \\(\mathbb C[X]\\) 中互素”直接替换成“在 \\(\mathbb R[X]\\) 中存在所需系数”。这个替换是可以证明的，但应在形式化依赖链中显式体现。

G2 的核心建议：保留已有两多项式 Bézout，增加“泛线性组合避开有限根集”这一引理，而不是直接迭代 gcd。

## 3. G3：矩形伴随矩阵与 \\(r=0\\) 的线性系统

这里我认为你们的数学路线是正确的，而且 G3 很适合成为下一项正式化工作。不过需要把两个逻辑步骤分开：

1. 对每个最大子式使用方阵伴随矩阵恒等式，构造多项式左逆；
2. 用 Bézout 系数把这些局部恒等式合并为全局左逆，再把多项式恒等式展开成有限个系数方程。

### 3.1 矩形伴随矩阵不需要一个新的“矩形 adjugate”

设

\\[ Q(\lambda)\in K[\lambda]^{q\times\omega}, \qquad q\ge\omega. \\]

对每个大小为 \\(\omega\\) 的行指标集 \\(I\\)，令

\\[ Q_I=E_IQ\in K[\lambda]^{\omega\times\omega}, \qquad f_I=\det Q_I. \\]

Mathlib 中已有的方阵伴随矩阵恒等式是核心基础。矩形表达式

\\[ \operatorname{adj}(Q_I)E_IQ=f_I I\_\omega \\]

并不是一个独立的矩形伴随矩阵定理：它只是先对方阵 \\(Q_I\\) 使用

\\[ \operatorname{adj}(Q_I)Q_I=(\det Q_I)I\_\omega, \\]

再把 \\(Q_I=E_IQ\\) 代入。

所以我建议不要先定义一个抽象的 `RectangularAdjugate`。直接把左侧定义成

\\[ S_I:=\operatorname{adj}(Q_I)E_I \\]

即可。它的尺寸是 \\(\omega\times q\\)，并满足

\\[ S_IQ=f_I I\_\omega. \\]

这样形式化的工作量集中在已有 `Matrix.adjugate` 恒等式、子矩阵索引和矩阵乘法的维度协调上。

### 3.2 “无公共根”到多项式左逆：用 Bézout，不用 resultant

令所有最大子式为 \\(f_I\\)。对每个 \\(\lambda\in K\\)，矩阵 \\(Q(\lambda)\\) 满列秩，当且仅当至少有一个最大子式 \\(f_I(\lambda)\ne0\\)。因此：

\\[ Q(\lambda)\text{ 对每个 }\lambda\in K\text{ 满列秩} \iff \\{f_I\\}\_I\text{ 没有公共根}. \\]

当 \\(K\\) 代数闭时，这等价于这些最大子式的 gcd 为 1。使用 G2 的有界次数 Bézout，存在 \\(g_I\\)，使

\\[ \sum_I g_I f_I=1. \\]

于是令

\\[ S=\sum_I g_I\operatorname{adj}(Q_I)E_I, \\]

就有

\\[ SQ = \sum_I g_I\operatorname{adj}(Q_I)E_IQ = \sum_I g_I f_I I\_\omega = I\_\omega. \\]

这是最直接的构造证明。

我不建议把 resultant 作为主路线。 Resultant 对两个多项式很有用，但你们这里是多个最大子式，而且真正需要的不只是“互素”这一布尔判断，还需要显式的 Bézout 系数及其次数界。Bézout/Sylvester 线性系统直接给出所需的系数证书，与后续构造 \\(S\\) 的步骤自然衔接。

### 3.3 多项式左逆到系数线性系统

如果

\\[ S(\lambda)=\sum\_{j=0}^{2\omega-2}S_j\lambda^j, \\]

那么

\\[ S(\lambda)(\lambda X-G)=I\_\omega \\]

按次数比较系数，得到：

\\[ -S_0G=I\_\omega, \\]

\\[ S\_{j-1}X-S_jG=0 \quad (1\le j\le 2\omega-2), \\]

以及

\\[ S\_{2\omega-2}X=0. \\]

这一方向只是多项式系数外延和 `ext`，预计是 G3 中相对容易的部分。反方向则是把线性系统解重新组装成 \\(S(\lambda)\\)，再用矩阵乘法和多项式系数相等证明左逆恒等式。

需要特别注意次数界的来源：G2 中每个 \\(g_I\\) 的次数小于 \\(\omega\\)，而每个 \\(\operatorname{adj}(Q_I)\\) 的元素是 \\((\omega-1)\\) 阶子式，次数至多 \\(\omega-1\\)。因此

\\[ \deg S\le(\omega-1)+(\omega-1)=2\omega-2. \\]

这也说明 G2 和 G3 的依赖关系非常紧密：如果先完成 G2 的次数界，G3 的多项式左逆次数界就不需要另起一套估计。

一个需要写清楚的边界条件： 当 \\(\omega=1\\) 时，次数上界是 0，系数系统只包含

\\[ -S_0G=I_1,\qquad S_0X=0. \\]

不存在中间的 \\(S\_{j-1}X-S_jG=0\\) 方程。Lean 中最好用独立的 `ω = 1` 化简或统一的 `Fin` 索引方式处理，不要让空区间索引造成证明负担。

还有一个域的问题：若左逆结论是在 \\(\mathbb C[\lambda]\\) 上得到，而输入矩阵 \\(X,G\\) 为实或有理系数，那么要证明系数系统可以在原系数域上求解。可用实系数矩阵的线性方程组可解性在域扩张下保持/下降来处理；这应作为独立引理，不能悄悄省略。

## 4. G4：有理数 bit-size 与 Gaussian elimination

这里我的建议比较明确：把 bit-size 论证留在论文中，做一份可独立审计的严格证明；暂时不要把整个 bit-complexity 体系作为 Lean 正式化目标。

这不是因为它不重要，而是因为它的形式化成本和主定理的数学收益不成比例。你们最值得形式化的是“为什么这个有限证书与原问题等价”；而系数长度界更适合用明确的整数行列式估计和 Hadamard 不等式完成。

### 4.1 Mathlib 有相关的代数基础，但这不等于有 bit-complexity 理论

Mathlib 有有理数的标准表示、矩阵行列式、矩阵伴随矩阵、线性代数等基础。`ℚ` 的表示本身就涉及分子、分母和既约性。Mathlib 也有用于有理矩阵消元的 `Echelon` tactic 基础设施，其中包括通过 Bareiss 消元处理有理数的机制。

[image](https://www.google.com/s2/favicons?domain=https://leanprover-community.github.io\&sz=32)

mathlib3 docs+1



但这些设施主要支持代数运算和可执行消元，不应被理解为已经提供了以下定理：

\\[ \text{输入有理矩阵的 bit-size 为 }L \Longrightarrow \text{消元过程中每个中间数的 bit-size 都是 }\operatorname{poly}(n,L). \\]

我没有找到可以直接复用、并且覆盖你们整个链条的 Mathlib 定理或成熟 Lean 项目。这里应谨慎地说“没有找到现成的完整 bit-size 理论”，而不是断言 Lean 社区完全没有相关工作。

### 4.2 论文中的 Cramer + Hadamard 路线是合理的

你们可以把所有有理矩阵的分母统一清除。若原始输入矩阵有 \\(m\\) 个有理条目，每个条目的分子、分母 bit-size 至多 \\(L\\)，则取所有分母的乘积作为统一分母，其 bit-size 至多为 \\(O(mL)\\)。清分母后，整数矩阵条目的 bit-size 仍是输入维数和 \\(L\\) 的多项式。

对一个 \\(t\times t\\) 的整数子矩阵 \\(D\\)，若所有条目绝对值至多 \\(B\\)，则 Hadamard 给出

\\[ |\det D| \le \prod\_{i=1}^t \\|\operatorname{row}\_i(D)\\|\_2 \le (\sqrt t B)^t. \\]

因此

\\[ \log_2(1+|\det D|) = O\bigl(t(\log B+\log t)\bigr). \\]

这给出所有相关子式的多项式 bit-size。利用 Cramer 公式或 RREF 的子式表示，便能进一步控制：

- \\(\ker[C;CA]\\) 的有理基；
- \\([N\ AN]\\) 的行空间基；
- \\(H=LN\\) 和 \\(H_A=LAN\\) 中固定部分的系数；
- 多项式矩阵的子式系数；
- Gram 矩阵中有限个系数的求和结果。

这里有两个容易被忽略的细节。

第一，不能只说“每个子式 bit-size 多项式”，还要说明有理数的分母如何统一控制。 对基向量的 Cramer 表示，分子和分母都是整数子式或其组合；应明确给出共同分母的选择方式，避免每一步重新约分导致证明叙述不完整。

第二，Gram 矩阵的系数是大量有理数的和。 即使每个被加数的 bit-size 都有多项式界，也要计入项数。若项数至多为 \\(2^{\operatorname{poly}(n)}\\)，其对数仍是多项式，因此累加后的 bit-size 仍为多项式；但论文应把这个“项数的对数”明确写出来。

关于 Gaussian elimination 的多项式 bit complexity，经典证明确实可以通过“消元中间数是原矩阵子式之比”以及 Hadamard 界来完成；这也是标准算法复杂度文献中常见的论证方式。

[image](https://www.google.com/s2/favicons?domain=https://drops.dagstuhl.de\&sz=32)

DROPS+1



### 4.3 我建议的形式化边界

Lean 中可以考虑形式化一个有限的基础引理，例如：

> 对整数矩阵的任意 \\(t\times t\\) 子矩阵，其行列式的绝对值由条目上界和维数给出的显式整数表达式控制。

这类定理能帮助你们检查 Hadamard 推导中的代数和维度细节。但我不建议现在继续形式化：

- bit-length 的编码定义；
- 有理数的规范化与每一步分母增长；
- Gaussian elimination 的所有中间状态；
- 多项式系数矩阵的完整编码长度；
- 参数化算法运行时间的机器级计数。

这些内容需要先确定计算模型、整数编码、分母表示、算法实现和运行步骤。否则很容易做出一个形式上漂亮、却没有覆盖论文所声称 bit-operation 模型的 formalization。

推荐做法： 论文附录给出一个统一的“Rational coefficient growth lemma”，逐个列出矩阵尺寸、统一分母、整数条目上界、子式上界、求和项数和最终 bit-size。Lean 只负责验证其中你们认为有复用价值的纯代数子引理。这样既不削弱论文的复杂度论证，也不会让形式化项目陷入另一个庞大的数值复杂度工程。

## 5. G5：\\(\exists\mathbb R\\) 编码是否值得形式化？

我的判断是：值得形式化编码的数学正确性，但不必形式化实闭域量词消去算法。 不过，你们目前对 G5 的描述有一个需要纠正的复杂度问题。

### 5.1 先区分三个不同命题

这三件事不是同一件事：

1. 存在一个有限的一阶实闭域公式，等价于原问题；
2. 这个公式的编码长度关于输入长度是多项式；
3. 该问题属于 \\(\exists\mathbb R\\)。

第一项是数学正确性。第二项是编码复杂度。前两项合起来，才支持第三项。

\\(\exists\mathbb R\\) 通常指可在多项式时间内 many-one 归约到实数存在性问题的复杂度类；标准的实代数几何决策程序用于说明相应存在性问题可判定，而不是用来代替“构造一个多项式大小的存在性公式”这一归约步骤。

[image](https://www.google.com/s2/favicons?domain=https://mathworld.wolfram.com\&sz=32)

Wolfram MathWorld



因此，你们应当避免写成：

> Membership in \\(\exists\mathbb R\\) follows from the standard quantifier-elimination decision procedure.

更准确的写法是：

> We construct, in polynomial time and with polynomial encoding size, an existential formula over the reals equivalent to the instance of DEC. Hence \\(\mathrm{DEC}\in\exists\mathbb R\\). Decidability of the target existential theory is a separate standard result.

这一区分很重要。一个问题可判定，并不意味着它属于 \\(\exists\mathbb R\\)。

### 5.2 你们的有限析取是否会破坏多项式编码长度？

这是 G5 最需要先审计的地方。

你写到公式是对 \\(\omega\\) 和列集合 \\(J\\) 的有限析取。如果这里确实显式枚举所有

\\[ J\subseteq\\{1,\ldots,k\\},\qquad |J|=\omega, \\]

那么分支数是

\\[ \binom{k}{\omega}, \\]

最坏情况下是指数级的。有限析取本身并不足以证明 \\(\exists\mathbb R\\) 归属；公式必须有关于输入长度的多项式编码长度。

如果列集合 \\(J\\) 只是为了选择一个秩分解的 pivot 子集，那么我建议考虑用存在性矩阵变量代替显式枚举。例如，对实矩阵 \\(H\\)：

\\[ \operatorname{rank}H=\omega \\]

可以尝试通过

\\[ H=UV, \\]

其中 \\(U\\) 有 \\(\omega\\) 列、\\(V\\) 有 \\(\omega\\) 行，再加上存在左逆和右逆的变量来表达：

\\[ WU=I\_\omega,\qquad VT=I\_\omega. \\]

这里 \\(W,T\\) 是额外的实矩阵变量。这样：

- \\(WU=I\_\omega\\) 保证 \\(U\\) 满列秩；
- \\(VT=I\_\omega\\) 保证 \\(V\\) 满行秩；
- \\(H=UV\\) 保证 \\(\operatorname{rank}H\le\omega\\)；
- 两个满秩条件保证 \\(\operatorname{rank}H\ge\omega\\)。

从而用多项式数量的变量和等式表达秩恰为 \\(\omega\\)，而无需枚举 pivot 列集合。

当然，这个替代方案是否与论文中的 \\(X,G,Z\\) 变量设计兼容，需要逐条对照你们已有的编码。我的重点是：如果 \\(J\\) 的枚举只是一个技术性 rank-factorization 选择，就应该尽量消掉它；若它是不可避免的分支，则必须另行证明总编码长度仍是多项式。

\\(\omega\\) 本身只有 \\(O(k)\\) 个可能值，所以对 \\(\omega\\) 的析取通常不是问题；真正需要警惕的是对 \\(J\\) 的组合枚举。

### 5.3 固定 \\(\omega,J\\) 的等价性 formalization 值得做

如果你们把编码组织成固定 \\(\omega,J\\) 的分支，那么 Lean 可以证明一个很有价值的定理：

\\[ \texttt{BranchFormula}(\omega,J) \iff \texttt{OriginalConditions}(\omega,J). \\]

这个定理至少应覆盖：

1. rank factorization 与指定秩的等价性；
2. rank-consistency 公式与线性方程组可解性的等价性；
3. 谱条件的有限多项式证书与原始全称谱条件的等价性；
4. Gram 形式 \\(Z^{\mathsf T}Zx=e_0\\) 与所需行空间包含条件的等价性；
5. 所有变量维度和多项式系数的正确对应。

尤其是第四项，不能仅仅证明一个形式上类似的矩阵方程。需要证明所使用的实 Gram 矩阵确实满足

\\[ \operatorname{im}(Z^{\mathsf T}Z)=\operatorname{im}(Z^{\mathsf T}). \\]

在实数域上，这一结论可由

\\[ \ker(Z^{\mathsf T}Z)=\ker Z \\]

推出，再用有限维线性代数的正交补关系得到像空间相等。你们已有的 `RankConsistency` 抽象定理可以在这一层复用。

### 5.4 但固定分支正确性不等于 \\(\exists\mathbb R\\) 归属已形式化

建议把正式化成果分成三个层次，并在论文或 artifact 中如实标记：

| 层次 | 形式化内容                         | 能支持的结论                                |
| -- | ----------------------------- | ------------------------------------- |
| A  | 固定 \\(\omega,J\\) 的公式与原数学条件等价 | 单个分支的正确性                              |
| B  | 所有分支的析取与 DEC 等价，且变量、约束数量有多项式界 | 存在性公式的数学与编码正确性                        |
| C  | 公式构造是多项式时间的归约，连接到标准 ETR 定义    | \\(\mathrm{DEC}\in\exists\mathbb R\\) |

A 是值得做的。B 是更有价值、也更接近完整论文结论的目标。C 中的归约可以在 Lean 中形式化其编码长度和构造函数，但没有必要把 ETR 的完整决策算法也做进来。

如果你们只完成 A，论文可以诚实地说“formalized the correctness of each algebraic branch”，不能说“formalized the \\(\exists\mathbb R\\)-membership proof”。

## 6. 对五个问题的直接回答

把上面的分析压缩成明确结论：

| 问题                           | 判断                                        | 建议路线                                         | 优先级 |
| ---------------------------- | ----------------------------------------- | -------------------------------------------- | --- |
| G1 Cauchy–Binet              | Mathlib 中未找到可直接调用的矩形定理；已有外部 Lean 形式化成果可参考 | 先移植有限指标版本，再包装成矩阵定理                           | 中   |
| G2 多项式 Bézout                | 结论正确；直接 gcd 归纳不自动保持次数界                    | 两个一般线性组合避开有限根集，再用已有两多项式 Bézout               | 最高  |
| G3 矩形伴随矩阵与线性系统               | 方阵伴随矩阵恒等式已在 Mathlib；矩形版本只需组合已有定理          | 最大子式 + 方阵 adjugate + G2 Bézout；然后比较系数        | 最高  |
| G4 系数 bit-size               | 没有找到覆盖完整链条的现成 Mathlib bit-size 理论         | 论文附录做严格的 Cramer/Hadamard 审计，Lean 只形式化必要代数子引理 | 低   |
| G5 \\(\exists\mathbb R\\) 编码 | 部分形式化有实质价值；但多项式编码长度必须单独证明                 | 先形式化固定分支正确性，再证明整个公式多项式大小                     | 中高  |

### G1 的额外发现：有一个值得参考的 Lean 形式化成果

我查到一个非常相关的外部结果：Prove2Me 的 Formalpedia 页面记录了定理 `ClassicalGaps.cauchy_binet_det`，标注为 Lean 4.30.0、Mathlib commit `c5ea003` 上完成的 Cauchy–Binet 形式化。该页面同时明确说明，这个结果尚未进入 Mathlib 本身。它采用的正是你们需要的有限子集求和形式：对所有大小为 \\(m\\) 的列指标集求和。

[image](https://www.google.com/s2/favicons?domain=https://prove2.me\&sz=32)

Prove2Me



因此，对 G1 的回答可以更精确：

- Mathlib 本体： 我没有找到已经合并的矩形 Cauchy–Binet 定理。
- Mathlib 生态中的 Lean 工作： 已有一个 Lean 4.30 的相关形式化成果，值得先检查其完整证明和许可证，再考虑移植到你们的 Lean 4.35 项目。
- 外代数路线： 是标准的概念解释，但未必是最短的工程路线。
- 你们最实际的路线： 先复用或移植这个有限子集版本，再将系数环推广到你们实际需要的多项式环。

另外，`hex-determinant` 项目也明确列出了 Cauchy–Binet 型的 column-tuple expansion，但它属于独立的 Lean 计算机代数项目，不能直接视为 Mathlib 的矩阵定理。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



### G3 的额外发现：Sylvester 矩阵工具已经存在

Mathlib 的 `Mathlib.RingTheory.Polynomial.Resultant.Basic` 不仅包含 resultant 理论，还定义了 Sylvester map 和 `adjSylvester`，并证明了相应的伴随映射复合恒等式。这说明你们并不需要从零开始形式化 Sylvester 矩阵及其伴随构造。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



但我仍然建议你们优先沿着 G2 的一般线性组合路线走。原因是你们需要的不是一个 resultant 数值，而是明确的多项式 Bézout 系数和次数界。已有的 Sylvester 工具可以作为两多项式 Bézout 的另一种实现或校验途径，不必成为 G3 的主线。

## 7. 一个需要补充的缺口：矩阵级压缩恒等式 \\((\*)\\)

你们在 Part I 中把

\\[ \operatorname{rank} \begin{bmatrix}J\\\M\end{bmatrix} = \operatorname{rank}J+ \operatorname{rank}(MN_J) \tag{\*} \\]

列为 paper-level only，但它其实是整个论文证明链中一个非常适合优先形式化的定理。

它是一个标准的商空间/核空间维数恒等式。令 \\(N_J\\) 的列构成 \\(\ker J\\) 的一组基。考虑线性映射

\\[ T:\ker J\longrightarrow \operatorname{im}M, \qquad x\longmapsto Mx. \\]

那么

\\[ \operatorname{im}T=M(\ker J), \qquad \ker T=\ker J\cap\ker M. \\]

由秩–零度定理，

\\[ \dim M(\ker J) = \dim\ker J-\dim(\ker J\cap\ker M). \\]

另一方面，堆叠矩阵对应的行空间增加量，恰好是 \\(M\\) 在 \\(\ker J\\) 上所诱导的有效秩。由此得到 \\((\*)\\)。

我建议把它作为一个独立的矩阵级定理形式化，而不是把它埋在某个压缩证明里。最好同时提供两个版本：

- `rank_stack_eq_rank_add_rank_restriction`：抽象线性映射或子空间版本；
- `rank_vstack_eq_rank_add_rank_mul_kernelBasis`：矩阵和核基版本。

这样你们现有的 `ker_compressed_iff` 就能与论文实际使用的矩阵表达式建立一个完全显式的连接。

因此，严格说来，我会把工作顺序安排为：先完成 \\((\*)\\)，再完成 G2 和 G3。 如果限定只能从 G1–G5 中挑两项，我的选择仍然是 G2 和 G3；但从整个形式化项目的依赖结构看，\\((\*)\\) 应该是它们之前的一项短而高价值的基础工作。

## 8. 还有两个数学表述需要明确

### 8.1 G3 中的域条件和实系数问题

你们写的是 \\(K[\lambda]\\)，并假设在代数闭域上无公共根。建议定理直接写成：

> Let \\(K\\) be an algebraically closed field, and let \\(Q\in K[\lambda]^{q\times\omega}\\), with \\(q\ge\omega\ge1\\). Then \\(Q(\alpha)\\) has full column rank for every \\(\alpha\in K\\) if and only if there exists a polynomial left inverse \\(S\\) with \\(\deg S\le2\omega-2\\).

如果实际输入 \\(X,G\\) 是实矩阵，但谱条件要求所有 \\(\lambda\in\mathbb C\\)，可以先在 \\(\mathbb C[\lambda]\\) 上构造左逆，再利用线性系统的实系数性质取回实系数解。

具体地，若系数线性系统

\\[ \mathcal A s=b \\]

的矩阵和右端都在 \\(\mathbb R\\) 上，而它有一个复数解

\\[ s=u+iv, \\]

则

\\[ \mathcal A u=b,\qquad \mathcal A v=0. \\]

所以 \\(u\\) 是实数解。这比单独发展一套复杂的实闭域代数论证更直接。

### 8.2 G2 的次数界需要明确处理零多项式和 \\(\omega=0\\)

建议将 G2 的正式定理前提写成：

\\[ \omega\ge1,\quad s\ge1,\quad \deg f_i\le\omega, \quad \gcd(f_1,\ldots,f_s)=1. \\]

然后结论为

\\[ \exists g_1,\ldots,g_s,\qquad \sum_i g_if_i=1,\qquad \deg g_i<\omega. \\]

零多项式的次数在 Mathlib 中通常采用特定约定。形式化时，不要依赖直觉中的“零多项式次数是负无穷”来自动解决所有边界问题。建议把次数约束改写成更适合 Lean 的形式，例如：

\\[ g_i.\operatorname{natDegree}<\omega \\]

并在零多项式情形单独确认这一表达式的行为。

对于 \\(\omega=0\\)，单独给出常数多项式引理，不要把它塞进一般的次数界定理。

## 9. 推荐的实际实施计划

我会把工作拆成三个阶段，而不是同时攻五个缺口。

阶段 I：打通核心代数证明

首先完成

1. 矩阵压缩恒等式 \\((\*)\\)

   将现有抽象 `ker_compressed_iff` 与论文的矩阵堆叠秩公式连接起来。
2. G2：多项式 Bézout 次数界

   完成有限根集、一般线性组合避根、互素、两多项式 Bézout 和系数次数界。
3. G3：矩形伴随构造

   复用 `Matrix.adjugate_mul`，完成最大子式、Bézout 合并和多项式左逆。
4. G3：系数线性系统

   完成多项式恒等式与有限线性方程组的双向等价，并单独处理 \\(\omega=1\\)。

阶段 II：形式化 Cauchy–Binet 与 Gram 证书

第二阶段

1. 先审查外部 Lean 4.30 形式化成果，判断能否直接移植。
2. 把 Cauchy–Binet 推广到你们需要的交换环或多项式系数环。
3. 形式化 Gram 矩阵秩性质及 \\(Z^{\mathsf T}Z\\) 的像空间恒等式。
4. 将 Cauchy–Binet 的压缩结果接入 Bézout 证书。

阶段 III：编码与复杂度边界

最后处理

1. 固定 \\(\omega,J\\) 的 ETR 分支正确性。
2. 检查所有分支的总编码长度，消除不必要的指数级列集枚举。
3. 在 Lean 中证明编码构造和等价性；将 ETR 决策算法作为外部标准结果。
4. 论文附录给出 Cramer/Hadamard bit-size 审计。

## 10. 对论文和 formalization artifact 的建议

我建议在论文中增加一张 formalization coverage 表，避免读者把“抽象定理已形式化”误解成“主定理已被 Lean 验证”。

可以采用如下分类：

| 数学内容                      | 当前状态       | 建议目标状态            |
| ------------------------- | ---------- | ----------------- |
| 抽象核压缩                     | Lean 已完成   | 保持                |
| 可达自由行对空间                  | Lean 已完成   | 补充矩阵实例            |
| 秩一致性                      | Lean 已完成   | 接入矩阵级条件           |
| 两多项式 Bézout               | Lean 已完成   | 增加多项式次数界          |
| 矩阵压缩恒等式                   | Paper only | Lean              |
| 矩形 Cauchy–Binet           | Paper only | Lean              |
| 矩形伴随矩阵构造                  | Paper only | Lean              |
| 谱条件与有限线性系统等价              | Paper only | Lean              |
| Gram 秩与像空间引理              | Paper only | Lean              |
| 有理数 bit-size              | Paper only | Paper-level audit |
| \\(\exists\mathbb R\\) 编码 | Paper only | 分支正确性与编码长度分开      |
| ETR 决策算法                  | 外部标准结果     | 无需形式化             |

这里还建议给 artifact 增加一个依赖图，标出每个正式化定理依赖哪些 Mathlib 定理、哪些自建引理，以及哪些论文级结论仍未进入 Lean。这样读者可以准确知道形式化到底覆盖到哪一层。

## 11. 最终评价

你们目前的 Lean 工作并不是“只形式化了几个无关紧要的基础事实”。四个抽象线性代数和多项式定理都位于论文的真实证明结构中，特别是：

- `ker_compressed_iff` 对应压缩正确性；
- `freePairSpace` 系列对应参数 \\(\kappa\_{\rm obs}\\) 的结构来源；
- `RankConsistency` 对应存在性约束的代数表达；
- 两多项式 Bézout 对应全称谱条件转为有限证书的关键工具。

这些是实质性的 formalization 贡献。

但从你们列出的 coverage 看，目前还不能称为主定理已经 kernel-checked。矩阵压缩、谱条件到多项式左逆、次数界、Gram 证书和编码正确性都仍然是 paper-level proof obligations。

我认为最好的策略不是追求“所有内容都形式化”，而是优先把主证明中最容易发生隐蔽错误的代数桥梁形式化：

1. G2： 因为它保证证书存在，而且保证次数界；
2. G3： 因为它把谱条件转成明确的有限线性系统；
3. 同时补上矩阵压缩恒等式 \\((\*)\\)，作为连接抽象 Lean 结果和论文矩阵表述的必要基础。

G1 值得完成，但可以随后移植现有 Lean 工作。G4 应保留为严格的论文复杂度审计。G5 则值得形式化编码正确性，但必须先解决显式列集析取是否导致指数级公式长度的问题。

最重要的一个提醒： G5 中“对所有列集合 \\(J\\) 做有限析取”与论文希望通过 Cauchy–Binet 避免显式枚举最大子式的思路之间，存在一个需要解释的潜在冲突。若这确实是指数数量的分支，那么即使每个分支都正确，也不能直接推出 \\(\mathrm{DEC}\in\exists\mathbb R\\)。我会把它列为目前最值得优先核查的论文级问题之一。

总体上，我认为你们的形式化方向是合理的，而且不必为了追求形式化覆盖率而把 ETR 决策算法和完整 bit-complexity 理论都纳入 Lean。先完成压缩恒等式、G2 和 G3，你们就能把论文中最核心的数学证书链条变成机器检查的证明；再把编码大小和系数增长作为明确、可审计的外部复杂度论证。这是成本与可信度之间更好的平衡。