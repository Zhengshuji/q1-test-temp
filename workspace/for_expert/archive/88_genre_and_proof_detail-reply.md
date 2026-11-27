# 总体建议：把论文定位为参数化算法论文，以控制论问题为动机，以结构压缩为核心贡献

我不建议把它定位成一篇纯数学论文，也不建议定位成一篇传统控制理论论文。最合适的定位是：

一篇面向控制论中的 functional observer feasibility 问题的参数化算法与复杂度论文（parameterized algorithms and complexity），其主要贡献是揭示并利用问题中特有的结构性参数化。

这会影响论文的写法，但不会降低数学证明标准。恰恰相反，复杂度论文对算法正确性、参数依赖、输入编码长度和 bit complexity 的要求通常更明确。它允许引用成熟的数学定理和复杂度定理，却不允许把真正决定算法是否成立的推导藏在一句“standard argument”里。

我会采用这样的贡献层次：

1. 结构性发现： 两个秩条件不是作用于彼此独立的矩阵变量，而是由同一个自由行块 \\(R\\) 诱导出来的耦合矩阵对。
2. 参数化： 通过 \\(K_0\\) 压缩和自由行对空间，识别有效参数\
   \\[\
   \kappa\_{\rm obs}=r\operatorname{rank}[N\ AN].\
   \\]
3. 算法性实现： 通过多项式证书、Gram 表示及 Cauchy–Binet 压缩，得到固定 \\(q\\) 算法和关于 \\(\kappa\_{\rm obs}\\) 的 FPT 算法。
4. 边界与补充结果： \\(r=0\\) 的精确多项式时间判定，以及 \\(\exists\mathbb R\\) 归属。

这里最重要的判断是：结构性压缩是主要发现，Cauchy–Binet 是使这一发现转化为高效证书和算法的关键技术。 不宜把二者写成相互竞争的贡献。

## 1. Genre：三种论文类型中，哪一种最合适？

### 1.1 为什么不是纯数学论文？

纯数学论文通常以定理、结构刻画和证明本身为主要贡献。你们的工作确实包含这些成分，但最终结果并不只是一个新的线性代数或多项式代数定理，而是：

\\[ \text{输入规模与参数} \quad\longmapsto\quad \text{判定算法及其复杂度界}. \\]

尤其是以下两条：

\\[ T\_{\mathrm{DEC}(q)}(\mathcal L) = \mathcal L^{O(q^2)} \\]

以及

\\[ T\_{\mathrm{DEC}}(\mathcal L) = f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). \\]

它们的意义必须通过算法设计、参数依赖和 bit complexity 来评价。因此，纯数学论文的写法并不是最自然的主框架。

### 1.2 为什么不是传统控制论文？

传统控制论文更可能以 observer 的存在性、结构性质、设计方法、最小阶数或工程意义为中心。你们的核心结果却是：

- 一个明确的决策问题；
- 一个输入相关的结构参数；
- 两个参数化复杂度上界；
- 一个精确的特殊情形算法；
- 一个实代数几何复杂度类归属。

这更接近理论计算机科学中的算法与复杂度论文。

当然，控制理论背景仍然非常重要。它解释为什么这个决策问题值得研究，以及为什么 \\(\kappa\_{\rm obs}\\) 是自然而非人为构造的参数。但不应让控制背景挤压复杂度论证的篇幅。

### 1.3 推荐的定位

我会在引言中明确使用类似这样的定位：

> This paper studies the parameterized computational complexity of functional observer feasibility. Its main contribution is a structural compression of the coupled design constraints, which exposes an effective parameter determined by the common free-row structure and leads to fixed-order and fixed-parameter algorithms.

这句话同时交代了：

- 研究对象：functional observer feasibility；
- 研究性质：parameterized computational complexity；
- 主要发现：structural compression；
- 算法结果：fixed-order 与 fixed-parameter algorithms。

所以，我建议以 complexity / parameterized algorithms 为论文类型，以 control theory 为问题背景，以结构压缩为中心贡献。

## 2. 六个证明步骤：哪些可以引用，哪些必须展开？

你们对六个步骤的风险排序总体正确。我会作一个细微调整：

- 第 6 项是复杂度结论最需要严格审计的地方；
- 第 5 项是算法运行时间推导中最容易被忽略的地方；
- 第 2、4 项虽不难，但它们直接影响参数定义和证书构造，应该写清楚；
- 第 1、3 项是标准线性代数事实，可以简短证明，不必长篇展开。

下面逐项给出我认为适合投稿版本的处理方式。

### 2.1 Lemma 1(iii)：最大子式判据

你们目前的表述：

> A pencil of rank \\(\omega\\) loses rank at exactly those \\(\lambda\\) at which all its \\(\omega\times\omega\\) maximal minors vanish.

数学上正确，但“standard maximal-minor criterion for constant rank”这句话有一点不够精确：你们真正需要的是对每个固定 \\(\lambda\\) 的矩阵秩判据，而不是先假设 pencil 具有 constant rank。

建议直接写成一个两行证明：

设 \\(P(\lambda)\\) 是 \\(m\times k\\) 矩阵，并且在考虑的参数范围内其最大可能秩为 \\(\omega\\)。则

\\[ \operatorname{rank}P(\lambda)<\omega \\]

当且仅当所有 \\(\omega\times\omega\\) 子式均为零。这是矩阵秩的标准子式刻画。若 \\(\omega=0\\)，则矩阵秩不可能低于零，谱条件自动成立，应单独约定空子式的处理方式。

如果你们的 \\(\omega\\) 定义为 \\(\operatorname{rank}H\\)，还需要说明为什么 pencil 的秩不可能超过 \\(\omega\\)。这通常来自

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H, \\]

于是

\\[ \operatorname{row}(\lambda H-H_A) \subseteq\operatorname{row}H, \\]

故

\\[ \operatorname{rank}(\lambda H-H_A)\le\omega. \\]

因此谱条件等价于其秩对每个 \\(\lambda\\) 都恰为 \\(\omega\\)，进而等价于所有最大子式不同时为零。

我的建议： 不需要专门引用一个高级定理。直接给出子式秩判据的一句解释，再补上 \\(\operatorname{rank}(\lambda H-H_A)\le\omega\\) 的原因。这样比只写“constant-rank criterion”更精确。

### 2.2 Lemma 2：维数计算

这一项应当展开，因为它不仅是一个普通的秩–零度计算，而且决定了你们的参数 \\(\kappa\_{\rm obs}\\) 从何而来。

考虑线性映射

\\[ \Phi:\mathbb F^{1\times n} \longrightarrow \mathbb F^{1\times d}\times\mathbb F^{1\times d}, \qquad x\longmapsto(xN,xAN), \\]

其中 \\(N\\) 有 \\(d=\dim K_0\\) 列。其矩阵表示可写成

\\[ \Phi(x)=x[N\ AN], \\]

只要把输出理解为相应的两个块。

因此

\\[ \ker\Phi = \\{x:xN=0,\ xAN=0\\} = \\{x:x[N\ AN]=0\\}. \\]

于是

\\[ \dim\ker\Phi = n-\operatorname{rank}[N\ AN]. \\]

由秩–零度定理，

\\[ \dim\operatorname{im}\Phi = \operatorname{rank}[N\ AN] =:d_0. \\]

若每一行自由变量独立地取值，那么 \\(r\\) 行的联合可达空间是 \\(r\\) 个这样的空间的直积，因此维数为

\\[ r d_0=\kappa\_{\rm obs}. \\]

这里需要注意一个记号上的细节：你们在 Part I 中写“the map \\(x\mapsto(xN,xAN)\\) has image of dimension \\(d_0\\) and kernel \\(K_0\\)”时，若 \\(x\\) 是行向量，那么这个 kernel 并不是直接等于 \\(K_0\\)。正确的 kernel 是

\\[ \\{x:x[N\ AN]=0\\}, \\]

其维数为 \\(n-d_0\\)。\\(K_0\\) 是 \\(N\\) 的列空间，是定义 \\(N\\) 的原状态空间子空间。请检查论文和 Lean 定理的类型，避免把行向量的左零空间与 \\(K_0\\) 混为一谈。

我的建议： 这一项必须写出 kernel 的显式表达式。它既证明维数，也使参数的含义可核查。

### 2.3 Lemma 3：秩一致性

这项不需要长篇证明，但不应只写一条无解释的等价链。

给定矩阵 \\(M\\) 和向量 \\(c\\)，有

\\[ Mb=c \iff c\in\operatorname{im}M. \\]

又因为

\\[ \operatorname{im}[M\ c] = \operatorname{im}M+\operatorname{span}\\{c\\}, \\]

所以

\\[ c\in\operatorname{im}M \iff \operatorname{im}[M\ c]=\operatorname{im}M. \\]

等价地，

\\[ \operatorname{rank}[M\ c]=\operatorname{rank}M. \\]

这里有一个写作上的建议：如果你们的 Lemma 3 后面用于构造代数约束，应当直接采用最后这个 rank 等式，而不是在后续章节中反复切换 image inclusion、span inclusion 和 rank equality 三种语言。

我的建议： 展开成上面三行即可。没有必要引用复杂的线性代数文献。

### 2.4 Lemma 5：系数矩阵 \\(Z\\) 的行空间

这一项应当给出精确的线性映射，不应只靠 prose。

设

\\[ f_i(\lambda)=\sum\_{t=0}^{\omega}a\_{i,t}\lambda^t, \\]

并令

\\[ p\_{i,j}(\lambda)=\lambda^j f_i(\lambda). \\]

若最大次数为 \\(D\\)，定义系数映射

\\[ \operatorname{coef}\_{D}: \\{p\in\mathbb F[\lambda]:\deg p\le D\\} \longrightarrow\mathbb F^{D+1}, \\]

其中

\\[ \operatorname{coef}\_{D}(p) = (p_0,p_1,\ldots,p_D), \qquad p(\lambda)=\sum\_{t=0}^{D}p_t\lambda^t. \\]

然后定义 \\(Z\\) 的第 \\((i,j)\\) 行为

\\[ Z\_{(i,j),t} = \begin{cases} a\_{i,t-j},&0\le t-j\le\omega,\\\ 0,&\text{otherwise}. \end{cases} \\]

于是对任意系数 \\(y\_{i,j}\\)，有

\\[ y^{\mathsf T}Z = \operatorname{coef}\_{D} \left( \sum\_{i,j}y\_{i,j}\lambda^j f_i(\lambda) \right). \\]

这就是你们真正使用的事实。

建议把它写成一个独立的小引理：

> The row space of \\(Z\\) is exactly the coefficient-vector representation of the polynomial ideal combinations generated by the shifted polynomials \\(\lambda^j f_i\\) within the chosen degree window.

不过需要谨慎：如果你们的 \\(Z\\) 只包含 \\(0\le j<\omega\\) 的移位，那么它描述的是受次数窗口限制的线性组合空间，不自动等于整个理想 \\((f_1,\ldots,f_s)\\) 的所有系数向量。你们必须说明为什么 G2 的次数界保证所需的 Bézout 组合落在这个窗口中。

我的建议： 给出显式的矩阵条目公式和一个系数比较证明。这一项不复杂，但它是 Gram 证书正确性的直接基础，不能只写成直观说明。

### 2.5 Theorem 1：复杂度指数的吸收

这项需要展开，尤其是你们的结论同时涉及变量数、分支数和输入 bit-size。

假设每个分支的变量数满足

\\[ N\_{\mathrm{var}}=O(q^2), \\]

而每个分支的多项式约束数量、次数和系数 bit-size 均满足关于输入长度 \\(\mathcal L\\) 的多项式界。使用固定变量数的实代数几何判定算法，若所引用的复杂度定理给出

\\[ \mathcal L^{O(N\_{\mathrm{var}})} = \mathcal L^{O(q^2)}, \\]

则单个分支的时间界为

\\[ \mathcal L^{O(q^2)}. \\]

若分支数满足

\\[ B(q,k)\le(q+1)k^q, \\]

且 \\(k\le n\le\mathcal L\\)（需在文中解释输入编码为何保证最后一个不等式），则

\\[ B(q,k) \le(q+1)\mathcal L^q. \\]

对 \\(q\ge1\\) 且 \\(\mathcal L\ge2\\)，有

\\[ q+1\le 2^q\le\mathcal L^q, \\]

从而

\\[ B(q,k)\le\mathcal L^{2q}. \\]

所以总时间为

\\[ \mathcal L^{O(q^2)}\cdot\mathcal L^{2q} = \mathcal L^{O(q^2)}. \\]

这就是你们所说的“chart factor absorbed”的具体含义。

但要额外核查：

- \\(q=0\\) 或 \\(q=r_0=0\\) 等边界情况；
- \\(k=0\\) 时的分支计数约定；
- 是否真的有 \\(k\le n\le\mathcal L\\)；
- 分支的生成本身是否需要指数时间；
- 所引用 Renegar 型定理中，变量数、约束数、次数和系数 bit-size 分别进入复杂度界的方式。

尤其是最后一点，不能只引用一个“Renegar bound”就跳过参数映射。需要写明你们的公式参数如何对应所引用定理中的参数。

我的建议： 把指数吸收的四行算式写出来，并给出引用定理的精确版本。这一项应该扩展。

### 2.6 Coefficient-size lemma：最重要的复杂度审计

我同意你们把它列为最高风险。它可能不影响数学正确性，却直接影响两条算法复杂度定理是否真的成立。

但要强调：这里不是要求你们给出每一个常数的最佳值。复杂度论文通常只需给出一个明确的多项式 bit-size 上界，并把每一步的依赖关系说明白。

至少应有如下链条：

\\[ \begin{aligned} &\text{input rational entries}\\\ &\Downarrow\quad\text{clear denominators}\\\ &\text{integer matrices with bounded entries}\\\ &\Downarrow\quad\text{Hadamard}\\\ &\text{bounded minors}\\\ &\Downarrow\quad\text{Cramer/RREF}\\\ &\text{bounded rational kernel and row-space bases}\\\ &\Downarrow\quad\text{matrix products and polynomial coefficients}\\\ &\text{bounded coefficients of }H,H_A,\text{ minors, Gram matrices}. \end{aligned} \\]

例如，设原始输入中共有 \\(m\\) 个有理数条目，每个分子、分母的 bit-size 不超过 \\(L\\)。将所有分母相乘，得到共同分母 \\(D\\)，其 bit-size 为

\\[ O(mL). \\]

清除分母后，整数矩阵条目的绝对值可由

\\[ 2^{O(mL)} \\]

控制。对一个 \\(t\times t\\) 子式，Hadamard 给出

\\[ |\det M\_{I,J}| \le (\sqrt t\\,B)^t, \\]

其中 \\(B\\) 是整数矩阵条目的绝对值上界。因此

\\[ \operatorname{bits}(\det M\_{I,J}) = O\bigl(t(\log B+\log t)\bigr). \\]

当 \\(t\le n\\)、\\(m\\) 关于输入维数多项式时，这仍然是输入长度的多项式。

接下来，RREF 或 Cramer 公式给出核基和行空间基的有理系数。你们必须明确指出：这些系数是哪些子式之比，以及分母如何控制。然后再对 \\(AN\\)、\\(LN\\)、\\(LAN\\) 的矩阵乘法给出 bit-size 增长界。最后处理多项式系数和 Gram 系数的有限求和：不仅要控制每个加数的 bit-size，也要控制加数数量的对数。

这里最容易漏掉的不是 Hadamard，而是多次有理矩阵运算之后的分母与求和项数。

我会要求作者在附录中给出一个统一的系数增长引理，至少包含：

1. 输入统一分母的 bit-size；
2. 清分母后整数矩阵条目上界；
3. 子式 bit-size 上界；
4. 核基和行空间基系数的分子、分母上界；
5. \\(H,H_A\\) 系数上界；
6. 最大子式的多项式系数上界；
7. Gram 矩阵系数上界；
8. 所有中间对象的维数和求和项数上界。

我的建议： 第 6 项一定要扩展到可以独立审计。你们不必给出最优常数，但不能只写“Cramer's rule and Hadamard imply polynomial bit-size”。

## 3. 如果只能扩展有限数量的证明，referee 最先检查什么？

我会把顺序安排为：

第一优先级：第 6 项——Coefficient-size lemma

必须扩展

它关系到两条复杂度定理是否真的成立。即使所有代数等价都正确，系数 bit-size 若未控制，调用实代数几何算法得到的运行时间界也可能不成立。

第二优先级：第 5 项——Theorem 1 complexity

必须扩展

必须写出变量数、约束数、次数、系数大小、分支数如何进入最终指数。这里是算法复杂度证明，不是普通的代数背景说明。

第三优先级：第 2 项——Lemma 2 dimension count

应当扩展

这是参数 \\(\kappa\_{\rm obs}\\) 的来源。必须显式识别 kernel，并且说明多行自由变量为什么给出 \\(r d_0\\) 维的联合空间。

第四优先级：第 4 项——Lemma 5 coefficient matrix

应当扩展

这连接多项式证书与有限矩阵秩条件。应给出 \\(Z\\) 的显式条目和系数比较。

第五优先级：第 1 项——Maximal-minor criterion

简短补证

一两句话即可，但必须明确使用的是逐点的矩阵秩—子式判据，并说明 pencil 秩不超过 \\(\omega\\)。

第六优先级：第 3 项——Rank consistency

简短补证

直接写出 \\(\operatorname{im}[M\ c]=\operatorname{im}M+\operatorname{span}\\{c\\}\\)，不需要专门引用。

如果只能做一轮修改，我会先扩展 6、5、2、4，然后用简短补证完成 1、3。你们自己给出的风险排序基本正确；我唯一的补充是：第 2 项虽然容易，但因为它定义了参数化结构，不能仅仅因为证明简单就放到最后。

### Referee 实际上会怎样检查？

一个熟悉参数化复杂度的审稿人，通常会沿着如下路径审查：

1. 你们的压缩是否与原始两个秩条件严格等价？
2. \\(\kappa\_{\rm obs}\\) 是否确实控制了自由变量的有效维数？
3. 全称谱条件是否真的被有限个多项式约束等价刻画？
4. 这个有限约束系统的变量数、次数、系数大小是多少？
5. 调用的实代数几何复杂度定理是否适用于这个系统？
6. 所有分支的总运行时间是否满足所声称的参数依赖？

所以 referee 不一定先从 Lemma 1 开始逐行读，而很可能先看 Theorem 1 和 Theorem 2 的证明，再回头检查这些引理是否支撑复杂度结论。

## 4. Genre 会不会改变 Lean formalization 的优先级？

会改变论文如何呈现 formalization，但不改变数学上最值得形式化的内容。

参数化复杂度论文并不要求所有 bit-complexity 推导都经过 Lean 内核检查。它要求的是复杂度论证完整、可审计、没有隐藏的参数依赖。

因此，我认为以下安排是完全合理的：

- Lean 形式化抽象压缩、可达空间、秩一致性和 Bézout；
- 继续形式化矩阵级压缩恒等式、G2、G3 及关键 Gram 引理；
- 论文中完整证明算法正确性；
- 在附录中独立审计 bit-size；
- 引用标准的实代数几何决策复杂度定理，并明确映射参数；
- 不形式化标准量词消去算法本身。

### 4.1 但要准确描述形式化覆盖率

目前四个 Lean 结果不能直接支持“the main theorems are formally verified”。它们支持的是：

> Several key abstract algebraic components underlying the proofs have been formalized in Lean 4 with Mathlib, without additional axioms.

建议再加一句：

> The matrix-level reductions, degree bounds, coefficient-size estimates, and complexity encodings are proved in the paper but are not yet part of the Lean formalization.

这比笼统地说“Lean formalization of the main results”准确得多。

### 4.2 我建议的形式化目标

| 内容                | 是否应 formalize | 原因                   |
| ----------------- | ------------- | -------------------- |
| 矩阵压缩恒等式           | 是             | 连接抽象压缩定理与实际输入        |
| G2 多项式 Bézout 次数界 | 是             | 关键证书存在性和次数控制         |
| G3 矩形伴随与左逆        | 是             | 全称谱条件转为有限代数证书        |
| Gram 秩与像空间性质      | 是             | 证书的线性代数基础            |
| Cauchy–Binet      | 值得做           | 核心算法优化，但可稍后          |
| 完整 bit-size 估计    | 暂不建议          | 成本高，形式化收益相对有限        |
| ETR 分支正确性         | 值得做           | 编码数学正确性              |
| ETR 编码长度与多项式时间归约  | 可部分形式化        | 复杂度论证的关键，但需先消除指数分支问题 |
| 实闭域量词消去算法         | 不必            | 属于成熟外部工具             |

需要特别指出：如果论文声称的是严格的 bit-operation 复杂度，那么 Lean 没有形式化 bit-size 并不会使论文不合格；但论文自身必须给出足够完整的 bit-size 证明。形式化不是复杂度正确性的替代品。

## 5. 论文真正应该强调什么贡献？

这是我认为最值得重新斟酌的部分。

你们现在强调：

> The key algorithmic step is a Cauchy–Binet compression of the Gram certificate.

这句话本身没有错，但它可能让读者误以为整篇论文的核心贡献是一个行列式恒等式的算法应用。

实际上，你们的结构性发现更有辨识度。

### 5.1 真正的结构来自同一自由行块

原始条件涉及

\\[ L,\quad LA,\quad CA,\quad C. \\]

而 \\(L\\) 不是任意的矩阵变量。它由固定部分 \\(L_0\\) 和同一个自由块 \\(R\\) 组成：

\\[ L= \begin{bmatrix} L_0\\\R \end{bmatrix}, \qquad LA= \begin{bmatrix} L_0A\\\RA \end{bmatrix}. \\]

所以 \\(L\\) 和 \\(LA\\) 中的自由部分不是独立的。它们必须同时来自同一组行向量：

\\[ r_i\longmapsto(r_iN,\ r_iAN). \\]

因此所有可能的压缩矩阵对 \\((H,H_A)\\) 都落在一个受约束的线性空间中，而不是填满两个任意矩阵空间。

这个空间的维数由

\\[ d_0=\operatorname{rank}[N\ AN] \\]

控制。对 \\(r\\) 行自由变量，总有效维数为

\\[ \kappa\_{\rm obs}=r d_0. \\]

这才是你们的参数化算法能够成立的结构性原因。

如果忽略这一点，把 \\(H,H_A\\) 当成两个独立的矩阵变量，那么会得到一个明显更大的问题，也无法充分利用自由变量之间的耦合关系。

### 5.2 Cauchy–Binet 的作用是什么？

Cauchy–Binet 并不是孤立的主要发现。它解决的是另一个关键问题：

> 如何在不显式枚举所有最大子式的情况下，保留它们共同无根这一性质，并将其压缩为可供算法处理的 Gram 证书？

因此我会把两个贡献分层：

主要结构性贡献

Coupled free-row compression

两个矩阵由同一自由行块产生，导致可达矩阵对位于低维线性空间中，并自然诱导有效参数 \\(\kappa\_{\rm obs}\\)。

关键算法性贡献

Cauchy–Binet compression of the Gram certificate

将大量最大子式的共同无根条件压缩成一个有限的代数证书，避免直接枚举所有最大子式。

算法结果

Parameterized complexity bounds

基于上述结构和证书，得到固定 \\(q\\) 的算法及关于 \\(\kappa\_{\rm obs}\\) 的 FPT 算法。

### 5.3 如果我来写论文，会怎样组织贡献陈述？

我会用类似下面的三点：

1. Structural reduction. We identify the effective space of attainable compressed matrix pairs induced by the common free-row block, and derive the parameter \\(\kappa\_{\rm obs}\\).
2. Finite algebraic certification. We convert the spectral rank condition into a finite polynomial certificate and use a Cauchy–Binet Gram construction to avoid explicit enumeration of all maximal minors.
3. Parameterized algorithms. We obtain a fixed-order algorithm with running time \\(\mathcal L^{O(q^2)}\\), together with an FPT algorithm parameterized by \\(\kappa\_{\rm obs}\\).

这样读者能理解：结构发现是为什么算法可能存在，Cauchy–Binet 是怎样实现算法，复杂度定理是最终产出。

我的建议：把 structural compression 放在 headline，把 Cauchy–Binet 放在第二层贡献。

## 6. 当前标题和摘要是否匹配？

### 6.1 标题

当前标题：

Parameterized Algorithms for Functional Observer Feasibility

我认为是合适的，可以保留。

它有三个优点：

- 明确点出算法贡献；
- 明确点出参数化视角；
- 保留 functional observer 这一控制理论问题的身份。

我不建议为了突出 Cauchy–Binet 而把它放进标题。Cauchy–Binet 是重要技术，但不是最适合面向广泛读者的标题关键词。

可以考虑两个备选：

- Parameterized Complexity of Functional Observer Feasibility
- Structural Compression and Parameterized Algorithms for Functional Observer Feasibility

第一个更偏理论复杂度，第二个更强调结构性发现。若目标期刊或会议面向理论计算机科学，我会倾向第一个；若希望兼顾控制理论与算法读者，当前标题或第二个备选更好。

### 6.2 摘要应该怎样调整？

摘要需要让读者在很短的篇幅内得到四个信息：

1. 研究什么决策问题；
2. 结构性参数是什么；
3. 得到了什么算法复杂度；
4. Cauchy–Binet 在其中起什么作用。

尤其应避免摘要只强调“我们构造了一个 Gram certificate”，而没有解释为什么它与参数 \\(\kappa\_{\rm obs}\\) 有关。

我建议的摘要结构是：

- 第一至二句：定义问题背景及计算目标；
- 第三句：说明共同自由行块带来的结构压缩；
- 第四句：给出固定 \\(q\\) 的复杂度；
- 第五句：给出 \\(\kappa\_{\rm obs}\\) 参数化的 FPT 结果；
- 第六句：说明 Cauchy–Binet Gram 证书的作用；
- 最后一句：交代 \\(r=0\\) 的特殊情形和 \\(\exists\mathbb R\\) 归属。

下面是一版可供修改的英文摘要草案。它有意不声称一般输入规模下存在多项式时间算法，也不声称 \\(\exists\mathbb R\\)-hardness。

# Abstract

We study the parameterized computational complexity of functional observer feasibility, where a prescribed block of observer rows is fixed and the remaining rows are free design variables. The feasibility constraints couple the observer matrix and its product with the system matrix through the same free-row block. Exploiting this coupling, we compress the design variables to a space of attainable matrix pairs whose dimension is governed by the parameter (\kappa\_{\mathrm{obs}}=r,\operatorname{rank}[N\ AN]), where (N) is a basis of (\ker[C;CA]). We construct a finite algebraic certificate for the spectral rank condition and use a Cauchy–Binet Gram representation to avoid explicit enumeration of all maximal minors. These structural and algebraic reductions yield a decision algorithm with running time (\mathcal L^{O(q^2)}) for fixed observer order (q), as well as a fixed-parameter algorithm with running time (f(\kappa\_{\mathrm{obs}})\operatorname{poly}(\mathcal L)). We also give an exact polynomial-time procedure for the case with no free rows and establish membership in the existential theory of the reals.

这版摘要的主要优点是结构贡献、算法工具和复杂度结果各有位置。但它仍有一个前提：你们必须确认所有 bit-size 论证完整成立，特别是 FPT 算法中函数 \\(f\\) 与参数的依赖确实没有把输入长度隐藏进去。

另外，摘要中“the same free-row block”是你们应当强调的结构。它比单独说“we use Cauchy–Binet”更能说明论文的原创性。

## 7. 我会怎样修改整篇论文的结构？

如果按参数化算法论文重组，我建议：

| 部分                                                  | 建议内容                                | 主要任务                                                         |
| --------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------ |
| I. Introduction                                     | 问题、动机、贡献、复杂度结果                      | 明确定位为参数化算法论文                                                 |
| II. Problem formulation                             | 原始秩条件、输入模型、参数定义                     | 消除符号和域的歧义                                                    |
| III. Structural compression                         | \\(K_0,N,H,H_A\\)，可达矩阵对空间           | 证明结构性参数来源                                                    |
| IV. Algebraic certification                         | 最大子式、Bézout、Gram 证书、Cauchy–Binet    | 建立有限判定条件                                                     |
| V. Fixed-order algorithm                            | 分支、变量、约束、正确性和复杂度                    | 证明 \\(\mathcal L^{O(q^2)}\\)                                 |
| VI. FPT algorithm                                   | 参数化表示、Gram 秩、正确性和复杂度                | 证明 \\(f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L)\\) |
| VII. Special case and real-algebraic classification | \\(r=0\\)，\\(\exists\mathbb R\\) 归属 | 补充结果                                                         |
| Appendix A                                          | 有界次数 Bézout、伴随构造等技术证明               | 让正文保持流畅                                                      |
| Appendix B                                          | 系数 bit-size 审计                      | 支撑 bit complexity                                            |
| Appendix C                                          | Lean formalization coverage         | 透明说明机器检查范围                                                   |

其中最重要的结构性调整是：不要把复杂度证明与代数正确性证明混在同一个段落中。

每个算法定理都应该有清晰的四段：

1. 算法描述；
2. 正确性；
3. 运行时间；
4. 参数依赖和边界情况。

## 8. 最终结论：我建议的投稿定位和修改优先级

### 投稿定位



推荐

&#x20;Parameterized algorithms / computational complexity for a control-theoretic decision problem.



不是纯数学论文，也不是传统控制设计论文。

### 六项证明修改

- 第 6 项：完整展开系数 bit-size 审计；
- 第 5 项：展开 Renegar 型复杂度界的参数映射和分支数吸收；
- 第 2 项：明确 kernel 和维数计算；
- 第 4 项：给出系数矩阵 \\(Z\\) 的显式定义和等价证明；
- 第 1、3 项：各补充简短、精确的线性代数证明。

### Formalization

不要求把 bit-size 和量词消去算法都纳入 Lean。优先形式化：

1. 矩阵压缩恒等式；
2. G2 多项式 Bézout 次数界；
3. G3 矩形伴随与多项式左逆；
4. Gram 矩阵的核心像空间和秩性质。

之后再考虑 Cauchy–Binet 和 ETR 分支正确性。

### 核心贡献

以同一自由行块诱导的耦合结构和有效参数作为 headline；以Cauchy–Binet Gram 压缩作为关键算法技术；以两条参数化复杂度上界作为主要定理。

### 最后一个需要立即检查的问题

你们的 G5 编码如果仍然显式枚举所有大小为 \\(\omega\\) 的列集合 \\(J\\)，必须确认这些分支的总数是否会指数增长。如果是，就不能仅凭每个分支正确推出 \\(\exists\mathbb R\\) 归属。应当考虑用存在性 rank factorization 变量替代显式 pivot 集合枚举，或者给出其他多项式规模的编码。

这点与论文类型无关，是一个直接影响定理正确性的复杂度问题。

我的总体判断： 这篇论文有一个值得强调的结构性算法贡献，当前最需要的不是把每条基础代数引理都写成很长的证明，而是把复杂度链条中真正承重的步骤——有效参数、证书次数、系数 bit-size、分支数量和实代数算法参数映射——写到审稿人可以逐项核验的程度。只要完成这一轮重组和审计，论文的定位就会清楚得多，证明也会从“看起来详细”变成“复杂度论证真正闭合”。