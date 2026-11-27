可以，而且我认为这是一个很有研究价值的方向。不过，我建议不要直接把 Shannon 熵或者互信息作为最小功能观测器阶次的度量，而是考虑建立一种基于信息充分性（Information Sufficiency）、信息维数（Information Dimension）和动态信息压缩（Dynamic Information Compression）的功能观测器阶次理论。

这样做有一个重要优势：我们不仅希望得到一个比现有代数下界更准确的下界，还希望这个下界具有可实现性，即能够严格证明存在相应阶次的功能观测器。

我仔细看了你给出的两篇论文。先说我的核心判断：

1. 第一篇论文将最小阶次问题推广到更一般的增广功能矩阵构造，并通过代数条件和谱条件确定最小可行阶次。
2. 第二篇论文进一步给出了逐阶刻画，将代数可行阶次和真正存在功能观测器的阶次区分开来。
3. 这两篇论文已经说明，单纯考虑代数意义上的最小阶次是不够的。真正的难点在于如何同时满足代数可恢复性和动态谱可行性。

尤其值得注意的是，第二篇论文的例子已经给出了一个很好的反例：

\\[ q_0=3,\qquad n_0-p=6. \\]

但实际情况是：

\\[ q=3:\text{不可行}, \\]

\\[ q=4:\text{不可行}, \\]

\\[ q=5:\text{可行}. \\]

因此：

\\[ \boxed{\nu\_{\min}=5>q_0=3.} \\]

这恰好说明：功能观测器的最小阶次不仅取决于需要估计多少个独立功能量，还取决于系统动态中必须保留多少维信息，才能使这些功能量具有正确的渐近重构性质。

相关依据见第二篇论文的第 VI、VII 节，特别是其 Theorem 5、Theorem 7 和 Theorem 9。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



下面我从信息论的角度，尝试建立一套更加完整的理论框架。

# 一、首先明确：为什么传统的信息论不能直接解决这个问题？

考虑连续时间线性系统：

\\[ \begin{cases} \dot x(t)=Ax(t)+Bu(t),\\\ y(t)=Cx(t),\\\ z(t)=Lx(t). \end{cases} \\]

其中：

- \\(x\in\mathbb R^n\\)：系统状态；
- \\(y\in\mathbb R^p\\)：可测输出；
- \\(z\in\mathbb R^r\\)：需要估计的功能量；
- \\(q\\)：功能观测器的动态阶次。

通常希望构造：

\\[ \begin{cases} \dot w=Fw+Gy+Hu,\\\ \hat z=Mw+Ny. \end{cases} \\]

使得在适当的初始条件和稳定性条件下：

\\[ \lim\_{t\to\infty}\\|\hat z(t)-z(t)\\|=0. \\]

这里有一个容易被忽略的问题。

观测器阶次 \\(q\\) 并不等于系统所包含的信息量。

例如，考虑一个连续随机状态变量 \\(x\\)。

它可能具有无限大的 Shannon 微分熵，也可能包含无限精度的连续信息。但这并不意味着我们需要无限维的观测器。

原因是：

观测器不是要保存状态的全部信息，而是只需要保存足以重构目标功能量的信息。

因此，我们真正应该研究的是：

\boxed{\text{为了重构 }z(t)，最少需要保存多少维动态信息？}}

这与经典信息论中的充分统计量思想非常接近。

但需要作一个重要区分：

- Shannon 信息量衡量的是不确定性；
- 信息维数衡量连续变量在高分辨率下的有效维度；
- 功能观测器阶次衡量的是实现动态充分统计量所需要的内部状态维数。

这三者不能直接画等号。

我认为第三种才是这个问题真正需要研究的对象。

# 二、建立基于信息充分性的理论框架

## 2.1 从状态可区分性出发

考虑两个具有不同初始状态的系统：

\\[ x_1(0)=x\_{10},\qquad x_2(0)=x\_{20}. \\]

假设两者输入相同。

定义初始状态差：

\\[ \delta x_0=x\_{10}-x\_{20}. \\]

相应的输出差为：

\\[ \delta y(t)=Ce^{At}\delta x_0. \\]

如果：

\\[ Ce^{At}\delta x_0=0,\qquad \forall t\geq 0, \\]

那么这两个初始状态对于观测输出而言不可区分。

定义不可观测子空间：

\\[ \mathcal N_C= \bigcap\_{k=0}^{n-1}\ker(CA^k). \\]

那么：

\\[ \delta x_0\in\mathcal N_C \\]

意味着两个状态产生完全相同的输出轨迹。

但是，我们并不需要区分所有状态。

只需要保证它们对应的目标功能量一致：

\\[ L e^{At}\delta x_0=0. \\]

因此，功能可观测的本质是：

\\[ \boxed{ \mathcal N_C\subseteq\mathcal N_L } \\]

其中：

\\[ \mathcal N_L= \bigcap\_{k=0}^{n-1}\ker(LA^k). \\]

等价地：

\\[ \operatorname{row}(\mathcal O_L) \subseteq \operatorname{row}(\mathcal O_C). \\]

这正是功能可观测性的经典条件。

但这里还可以进一步发展。

## 2.2 引入信息等价类

定义两个状态之间的信息等价关系：

\\[ x_1\sim_C x_2 \\]

当且仅当：

\\[ Ce^{At}x_1=Ce^{At}x_2, \quad \forall t\geq0. \\]

这意味着两种状态产生完全相同的可测信息。

所有等价状态构成一个等价类：

\\[ [x]\_C=x+\mathcal N_C. \\]

从信息论角度看，这个等价类表示：仅凭输出历史，无法进一步区分的状态集合。

如果系统功能可观测，那么：

\\[ Lx_1=Lx_2 \\]

对于所有属于同一个等价类的状态均成立。

因此，目标功能量实际上定义在商空间：

\\[ \mathcal X/\mathcal N_C \\]

之上。

这给出一个重要启示：

功能观测器没有必要保留完整状态，只需要保留与目标功能量有关的动态信息。

这也是信息压缩理论能够介入功能观测器阶次研究的原因。

# 三、为什么信息维数可能比现有代数下界更有价值？

第二篇论文给出的代数下界为：

\\[ q_0=\sum\_{j=1}^{r}\eta_j. \\]

其中，\\(\eta_j\\) 是第 \\(j\\) 个功能量对应的功能可观测指数。

这个下界解决的是：

在代数条件下，至少需要多少维增广功能变量？

但它并没有完全解决：

这些变量是否能够形成一个具有所要求谱性质的动态系统？

我认为可以从信息压缩的角度进一步解释这个问题。

假设存在两个增广功能矩阵：

\\[ \mathcal L_1,\qquad \mathcal L_2. \\]

它们可能都能够重构：

\\[ z=Lx. \\]

但它们保留的动态信息不同。

其中一个可能保留了某些对于当前时刻功能量重构并非必需、但对于动态误差收敛非常重要的信息。

另一个则可能丢失了这些信息。

这就造成：

\\[ \text{代数可恢复} \not\Rightarrow \text{动态可实现}. \\]

从信息论角度看，这相当于：

一个统计量虽然是目标变量的充分统计量，但它未必能够通过所要求的有限维、稳定、因果动态系统实现。

因此，我们需要研究的不是静态充分性，而是：

\\[ \boxed{\text{动态充分统计量的最小维数}} \\]

这个概念可以成为一个新的研究切入点。

# 四、一个更严谨的方向：动态信息充分统计量

这是我认为最值得深入研究的部分。

## 4.1 定义动态充分统计量

设：

\\[ \mathscr Y_t=\\{y(\tau):0\leq\tau\leq t\\} \\]

表示截至时刻 \\(t\\) 所获得的全部输出历史。

考虑一个 \\(q\\) 维统计量：

\\[ s(t)=\Phi_q(\mathscr Y_t,u\_{[0,t]}). \\]

这里 \\(\Phi_q\\) 是某种因果信息压缩映射。

如果存在一个映射 \\(\Psi\\)，使得：

\\[ z(t)=\Psi(s(t),y(t)) \\]

能够渐近成立，那么可以说 \\(s(t)\\) 对目标功能量具有充分性。

但这只是静态意义上的充分性。

为了对应功能观测器，还需要要求 \\(s(t)\\) 具有有限维动态实现：

\\[ \dot s(t)=f(s(t),y(t),u(t)). \\]

对于线性功能观测器，我们进一步限制为：

\\[ \dot s(t)=Fs(t)+Gy(t)+Hu(t). \\]

于是可以定义：

定义（动态信息充分阶次）

满足以下三个条件的最小状态维数：

1. 能够保存重构目标功能量所需的信息；
2. 能够通过有限维因果动态系统实现；
3. 其估计误差满足规定的渐近收敛或极点配置要求。

记为：

\\[ q\_{\mathrm{DIS}}. \\]

这里 DIS 表示 Dynamic Information Sufficiency。

如果能够证明：

\\[ \boxed{q\_{\mathrm{DIS}}=\nu\_{\min}} \\]

那么就建立了信息充分性理论与最小功能观测器阶次理论之间的严格联系。

不过，这个定义本身还不是一个新的计算公式。真正的贡献应该是把它转化成可计算的矩阵秩条件。

## 4.2 用信息维数刻画连续状态信息

这里可以引入 Rényi 信息维数。

对于一个随机变量 \\(X\\)，其信息维数可以写成：

\\[ d_I(X)= \lim\_{\epsilon\rightarrow0} \frac{H(\lfloor X/\epsilon\rfloor)} {\log(1/\epsilon)} \\]

其中，在极限存在及适当正则条件下，该定义描述变量在高精度量化下的信息维数。

对于非退化的 \\(q\\) 维连续随机向量：

\\[ d_I(X)=q. \\]

但是，需要注意：

不能简单地写成：

\\[ q\_{\min}=d_I(z\mid y). \\]

因为在功能可观测的情况下，完整输出历史可能已经决定目标功能量，条件信息维数甚至为零，而实际动态观测器仍然可能需要多个内部状态。

真正需要研究的是输出历史的一个有限维、因果、递归充分表示。

例如：

\\[ s(t)=T\mathscr Y_t. \\]

要求其在时间演化过程中能够闭合：

\\[ \dot s=Fs+Gy+Hu. \\]

也就是说，压缩后的信息不仅要足以估计当前目标，还必须足以更新下一时刻的统计量。

这正是动态信息压缩与普通数据压缩的本质区别。

## 4.3 将动态信息压缩转化为矩阵条件

我们可以直接利用第二篇论文中的零空间表示。

设：

\\[ \mathcal N= \ker \begin{pmatrix} C\\\ \mathcal L \end{pmatrix}. \\]

假设：

\\[ \dim\mathcal N=n-p-q. \\]

取矩阵 \\(Z\\)，使：

\\[ \operatorname{im}Z=\mathcal N. \\]

那么：

\\[ CZ=0,\qquad LZ=0. \\]

这两个条件表示：

在被压缩掉的信息方向上，既没有可测输出，也没有目标功能量。

因此，\\(\operatorname{im}Z\\) 可以看作一个候选信息丢弃子空间。

现在问题变成：

哪些信息方向可以丢弃，而不会破坏功能量的动态重构？

这就需要同时满足两个条件。

第一，代数闭合条件：

\\[ \operatorname{im}(AZR_Z) \subseteq\operatorname{im}Z, \\]

其中：

\\[ \operatorname{im}R_Z=\ker(CAZ). \\]

它保证被丢弃的信息在相应不可测方向上不会重新进入保留的信息空间。

第二，谱条件：

\\[ \operatorname{rank} \begin{pmatrix} (\lambda I-A)V&Z \end{pmatrix} = \operatorname{rank} \begin{pmatrix} V&Z \end{pmatrix}, \quad \lambda\in\Omega_S, \\]

其中：

\\[ \operatorname{im}V= \ker \begin{pmatrix} C\\\ CA \end{pmatrix}. \\]

它保证压缩后不会产生违反指定谱要求的动态信息损失。

于是，我们得到：

\\[ \boxed{ q=n-p-\dim\mathcal N } \\]

以及：

\\[ \boxed{ \begin{aligned} CZ&=0,\\\ LZ&=0,\\\ \operatorname{rank}[Z\ AZR_Z]&=\dim\mathcal N,\\\ \operatorname{rank}[(\lambda I-A)V\ Z] &=\operatorname{rank}[V\ Z]. \end{aligned} } \\]

这实际上给出了动态信息压缩的一个具体矩阵化表达。

值得强调的是，这些条件不是我另外假设出来的，而是第二篇论文 Theorem 3 和 Theorem 4 已经证明的等价条件。我们可以在其基础上赋予它们信息压缩的解释。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



# 五、真正有意义的下界应该如何定义？

现在讨论你最关心的问题。

你希望得到一个比 \\(q_0\\) 更准确的下界，而且这个下界一定存在相应的功能观测器。

这里有一个非常重要的数学逻辑：

假设我们找到一个数 \\(q\_\*\\)，满足：

\\[ q\_\*\leq\nu\_{\min}. \\]

这是一个真正的下界。

如果同时证明：

\\[ q\_\*\in\Sigma\_{FO}(L), \\]

即存在一个阶次为 \\(q\_\*\\) 的功能观测器，那么：

\\[ \nu\_{\min}\leq q\_\*. \\]

两者合并：

\\[ \boxed{\nu\_{\min}=q\_\*}. \\]

所以：

一个既是最小阶次下界、又保证可实现的界，实际上就是最小功能观测器阶次的精确刻画。

这也意味着，单纯从信息论推出一个数值下界还不够。我们必须证明它对应的动态信息压缩方案可以实现。

## 5.1 建议建立一个新的信息论阶次指标

可以定义：

\\[ \boxed{ q\_{\mathrm{info}} = n-p- \max\_{Z\in\mathscr Z\_{AS}} \dim\operatorname{im}Z } \\]

其中：

\\[ \mathscr Z\_{AS} \\]

表示所有同时满足代数条件和谱条件的候选信息丢弃子空间的集合。

展开来说：

\\[ \mathscr Z\_{AS} = \left\\{ Z: \begin{array}{l} CZ=0,\quad LZ=0,\\\ \operatorname{rank}[Z\ AZR_Z]=d,\\\ \operatorname{rank}[(\lambda I-A)V\ Z] =\operatorname{rank}[V\ Z],\\\ \forall\lambda\in\Omega_S \end{array} \right\\}. \\]

这里 \\(d=\dim\operatorname{im}Z\\)。

因为：

\\[ q=n-p-d, \\]

所以最小观测器阶次对应于最大可允许的信息丢弃维数。

这个表达式的意义是：

- 尽可能压缩内部状态；
- 但不能丢失目标功能量所需的信息；
- 不能破坏增广动态系统的代数闭合；
- 不能破坏要求的谱性质。

由此得到：

\\[ \boxed{ \nu\_{\min}=q\_{\mathrm{info}}. } \\]

注意，这个等式是建立在 \\(\mathscr Z\_{AS}\\) 非空的前提下的。对于功能可观测系统，这一点可以由后面提到的端点存在性定理保证。

这套表达式与第二篇论文的 Theorem 9 在数学上是等价的，但它提供了一个不同的解释：最小功能观测器阶次等于在动态可恢复性和谱约束下，无法继续压缩掉的信息维数所对应的剩余维度。

## 5.2 为什么这个下界一定可实现？

这里可以利用第二篇论文中一个非常重要、但可能值得进一步强调的结果。

设：

\\[ n_0=\operatorname{rank}\mathcal O_C. \\]

定义：

\\[ \mathcal N_0=\ker\mathcal O_C. \\]

取 \\(Z_0\\) 为 \\(\mathcal N_0\\) 的一组基。

那么：

\\[ \dim\mathcal N_0=n-n_0. \\]

并且：

\\[ CZ_0=0,\qquad LZ_0=0. \\]

由于不可观测子空间具有 \\(A\\)-不变性：

\\[ AZ_0=Z_0F_0 \\]

对某个矩阵 \\(F_0\\) 成立。

因此，在功能可观测的前提下，论文证明了：

\\[ \boxed{q=n_0-p} \\]

一定属于可行阶次集合。

这意味着：

\\[ \Sigma\_{FO}(L)\neq\varnothing. \\]

换句话说：

只要系统满足功能可观测性，就一定存在一个阶次为 \\(n_0-p\\) 的功能观测器。

这是第二篇论文 Theorem 7 的结论。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



因此，我们可以得到一个严格的搜索区间：

\\[ \boxed{ q_0\leq\nu\_{\min}\leq n_0-p. } \\]

但如果你的研究目标是寻找一个比 \\(q_0\\) 更精确且可实现的下界，那么我建议把重点放在：

\\[ \max\_{Z\in\mathscr Z\_{AS}}\dim\operatorname{im}Z \\]

而不是继续寻找一个单纯依赖可观测指数的标量公式。

这也避免了一个理论上的困难：不同系统即使具有相同的功能可观测指数，也可能有不同的谱可行性。

# 六、从信息论角度进一步发展：能否得到更简单的闭式下界？

上面的矩阵优化表达式是严谨的，但还不够简洁。

如果希望进一步形成有理论创新性的结果，我认为可以考虑以下三个方向。

## 方向一：基于条件信息维数的阶次下界

考虑系统状态的随机化：

\\[ x(0)\sim\mathcal N(0,P_0), \qquad P_0>0. \\]

定义输出历史对应的信息空间：

\\[ \mathcal Y_t= \operatorname{span} \\{C,CA,\ldots,CA^{n-1}\\}. \\]

再考虑目标功能量的信息空间：

\\[ \mathcal Z_t= \operatorname{span} \\{L,LA,\ldots,LA^{n-1}\\}. \\]

我们可以研究：

\\[ \dim\left( \mathcal Y_t+\mathcal Z_t \right) - \dim\mathcal Y_t. \\]

这描述了目标功能量在输出信息之外还需要增加多少独立信息方向。

不过，这个量只描述静态信息缺口，尚不能反映动态稳定性。

因此，可以进一步引入时间扩展：

\\[ \mathcal Y_t^{(k)} = \operatorname{span} \\{C,CA,\ldots,CA^k\\}, \\]

\\[ \mathcal Z_t^{(k)} = \operatorname{span} \\{L,LA,\ldots,LA^k\\}. \\]

研究不同 \\(k\\) 下信息空间的增长速度。

我认为，这有机会建立一种新的动态信息增长指标，并与功能可观测指数建立联系。

但要注意：仅仅计算这些秩的增长，并不能保证谱可行性。必须另外建立动态闭合定理。

## 方向二：基于 Hankel 秩的动态信息维数

这是我更加推荐的方向。

在经典系统理论中，Hankel 秩与最小状态空间实现维数具有非常紧密的关系。

对于功能观测器，我们可以研究从输入输出历史到目标功能量的动态映射，并构造相应的功能 Hankel 算子。

例如，考虑：

\\[ \mathcal H_L: \text{过去的输出和输入信息} \longrightarrow \text{未来的目标功能响应}. \\]

如果能够构造一个合适的有限维 Hankel 算子，使其秩等于最小功能观测器的内部状态维数，那么就可以得到：

\\[ \boxed{ \nu\_{\min}=\operatorname{rank}\mathcal H_L } \\]

这样的结果。

不过，这里有一个关键技术问题：

普通 Hankel 算子的秩刻画的是最小输入输出实现维数，而功能观测器涉及未知初始状态、已知输入、直接测量输出以及渐近误差收敛。

所以不能直接套用普通的 Hankel 秩结论。

需要专门构造一个带有初始状态不确定性和功能输出约束的 Hankel 算子。

如果能证明：

1. 该算子的秩给出任何功能观测器阶次的必要下界；
2. 其最小秩分解能够生成一个满足谱条件的观测器；

那么就能够同时解决下界和可实现性问题。

这个方向很适合形成一篇独立的理论研究论文。

## 方向三：基于信息损失的谱约束

我认为这是最有可能取得实质性理论进展的方向。

传统信息论关注：

\\[ I(X;Y) \\]

即随机变量之间的互信息。

但是对于功能观测器，更重要的是：

压缩信息后，系统中哪些动态模态变得不可区分？

设某个信息压缩子空间为：

\\[ \mathcal N=\operatorname{im}Z. \\]

如果某个特征模态：

\\[ Av=\lambda v \\]

在压缩后落入不可区分的信息空间，那么就可能造成目标功能量无法被正确重构。

因此，可以研究如下映射：

\\[ \mathcal T\_\lambda: v\mapsto(\lambda I-A)v \\]

在候选信息丢弃子空间上的作用。

进一步定义：

\\[ \rho(\lambda,Z)= \operatorname{rank} \begin{pmatrix} (\lambda I-A)V&Z \end{pmatrix} - \operatorname{rank} \begin{pmatrix} V&Z \end{pmatrix}. \\]

根据第二篇论文的 Theorem 4：

\\[ \rho(\lambda,Z)=0 \\]

对于所有要求的 \\(\lambda\\)，就是相应的谱可行条件。

因此，可以将谱条件理解为：

信息压缩不能使系统在指定频谱区域内产生额外的动态不可区分性。

这实际上是把信息损失和动态稳定性联系起来。

对于极点任意配置：

\\[ \Omega_S=\mathbb C. \\]

对于检测性：

\\[ \Omega_S= \\{\lambda:\operatorname{Re}\lambda\geq0\\}. \\]

这两种情况对应不同的信息保留要求。

特别值得研究的是：是否能够利用系统特征值分布、广义特征向量以及 Jordan 结构，直接推导谱约束所要求的最小保留信息维数。

这有可能得到比逐阶搜索更加简洁的下界。

# 七、我认为最值得研究的核心定理

如果希望将上述想法发展成一篇有理论深度的论文，我建议最终尝试证明下面这个定理。

定理（动态信息充分性与最小功能观测器阶次）

考虑线性系统：

\\[ \dot x=Ax+Bu,\qquad y=Cx,\qquad z=Lx. \\]

假设系统满足功能可观测性，并且采用给定的谱可行性要求 \\(\Omega_S\\)。

定义：

\\[ d\_{\max}= \max\left\\{ \dim\mathcal N: \mathcal N\subseteq\ker C\cap\ker L, \ \mathcal N\text{ 满足代数闭合条件和谱条件} \right\\}. \\]

那么：

\\[ \boxed{ \nu\_{\min}=n-p-d\_{\max}. } \\]

并且存在一个阶次为：

\\[ q^\*=n-p-d\_{\max} \\]

的功能观测器。

证明思路：

1. 任意阶次为 \\(q\\) 的功能观测器，都对应一个维数为 \\(n-p-q\\) 的信息丢弃子空间。
2. 该子空间必须满足代数闭合条件和谱条件。
3. 因此：

\\[ n-p-q\leq d\_{\max}. \\]

&#x20;  从而：

\\[ q\geq n-p-d\_{\max}. \\]

4. 另一方面，由 \\(d\_{\max}\\) 的定义，存在一个达到最大维数的可行子空间。
5. 根据零空间参数化定理，可以由该子空间构造对应的增广功能矩阵。
6. 根据代数条件和谱条件，可以进一步构造对应的功能观测器。

因此：

\\[ \boxed{\nu\_{\min}=q^\*.} \\]

这个定理的价值在于：把最小阶次问题转换成了最大动态信息压缩问题。

需要说明的是，这个定理在现有第二篇论文的矩阵框架内，本质上是对其固定阶次存在性定理和全阶次刻画定理的最大化重述，并非已经得到一个独立于原论文的新下界。真正需要进一步证明的创新，是能否找到不必逐阶搜索所有 Grassmann 子空间的、更简单的动态信息维数公式。

# 八、如何设计具体的研究工作？

我建议分为四个阶段。

第一阶段：建立信息论描述

理论准备

- 定义状态信息等价类。
- 建立功能信息充分性的数学定义。
- 研究输出历史与目标功能量之间的条件信息关系。
- 区分静态充分统计量与动态充分统计量。

第二阶段：建立动态信息维数

核心理论

- 构造功能 Hankel 算子。
- 研究其秩与功能观测器阶次的关系。
- 引入谱约束，研究哪些信息维度必须保留。
- 寻找可以直接计算的秩下界。

第三阶段：证明可实现性

关键证明

- 证明信息维数给出所有观测器阶次的必要下界。
- 构造达到该维数的增广功能矩阵。
- 证明对应矩阵满足代数和谱条件。
- 建立信息维数与最小功能观测器阶次的等价定理。

第四阶段：算法与数值验证

应用验证

- 与 Darouach 方法比较。
- 与 Luenberger 方法比较。
- 与现有功能可观测指数下界比较。
- 验证不同系统结构下信息维数的变化。
- 研究参数扰动和数值稳定性。

## 具体数值实验建议

可以直接使用第二篇论文第 VII 节的例子作为基准。

它具有：

\\[ n=8,\quad p=2,\quad r=2. \\]

并且：

\\[ q_0=3,\quad \nu\_{\min}=5,\quad n_0-p=6. \\]

这个例子非常适合检验新理论。

如果新提出的信息论下界能够直接给出：

\\[ q\_{\mathrm{info}}=5, \\]

就说明它比传统代数下界：

\\[ q_0=3 \\]

更准确，同时又不需要从 \\(3,4,5,6\\) 逐阶验证。

进一步可以设计不同的 \\(A,C,L\\)，观察在相同 \\(q_0\\) 下，最小功能观测器阶次是否发生变化。

如果发生变化，就能进一步说明：仅依靠功能可观测指数无法完全确定最小阶次，而动态信息结构确实提供了额外信息。

# 九、建议重点阅读的参考文献

我建议从以下几组文献入手。

## 1. 功能观测器理论

这两篇是当前研究的直接基础。

1\. Fernando, T. A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions. arXiv:2609.33615, 2026.

[arXiv 原文](https://arxiv.org/abs/2609.33615?utm_source=chatgpt.com)。

2\. Fernando, T. Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger. arXiv:2609.37992, 2026.

[arXiv HTML 全文](https://arxiv.org/html/2609.37992?utm_source=chatgpt.com)。

重点阅读第二篇的：

- Section II：问题建模；
- Section III：代数可行阶次；
- Section IV–V：零空间和谱条件；
- Section VI：全阶次刻画；
- Section VII：代数下界失效的具体例子。

## 2. 信息论与信息维数

3\. Shannon, C. E. (1948). A Mathematical Theory of Communication. Bell System Technical Journal, 27, 379–423, 623–656.

4\. Rényi, A. (1959). On the Dimension and Entropy of Probability Distributions. Acta Mathematica Academiae Scientiarum Hungaricae, 10, 193–215.

5\. Wu, Y. and Verdú, S. (2010). Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression. IEEE Transactions on Information Theory, 56(8), 3721–3748.

其中，Wu 和 Verdú 的工作尤其值得关注，可以为连续状态变量的信息维数和信息压缩提供理论基础。

## 3. 线性系统实现理论与 Hankel 秩

6\. Ho, B. L. and Kalman, R. E. (1966). Effective Construction of Linear State-Variable Models from Input/Output Functions. Regelungstechnik, 14, 545–548.

7\. Kailath, T. (1980). Linear Systems. Prentice-Hall.

这两项是研究动态信息维数、Hankel 秩和最小实现阶次的重要基础。

# 十、我对这个研究方向的最终建议

我认为需要特别注意一个问题：

不要把研究目标简单设定为利用信息论重新推导一个比 \\(q_0\\) 更大的数。

因为第二篇论文已经证明，最小功能观测器阶次受到谱可行性影响，而且不同阶次之间并不具有简单的单调可行性。

真正有价值的研究应该是：

\\[ \boxed{ \text{信息充分性} \longrightarrow \text{动态信息维数} \longrightarrow \text{谱约束} \longrightarrow \text{最小功能观测器阶次} } \\]

我尤其看好两个可能形成独立创新点的方向：

创新点 A：基于功能 Hankel 算子的最小阶次理论。

试图找到一个新的 Hankel 算子，其秩直接刻画最小功能观测器阶次，而不是仅仅刻画传统意义上的最小状态空间实现维数。

创新点 B：基于谱约束的信息压缩理论。

将最小功能观测器阶次解释为：在保证功能可恢复和动态谱可行的前提下，系统所允许的最大信息丢弃维数。

我更推荐先研究创新点 B。因为它可以直接利用两篇论文已经建立的零空间矩阵参数化和谱条件，不必从头构造整个理论体系。

最后，还有一个非常重要的理论边界：如果不限定观测器类型、因果性、线性性、输入可用性和收敛要求，就不存在一个普遍适用的信息论阶次公式。必须先明确这些条件，才能保证所谓的最小信息维数与实际观测器阶次一致。

我建议下一步直接做一件事：从第二篇论文的 Theorem 5 和 Theorem 9 出发，尝试构造一个真正独立的功能 Hankel 算子，并证明其秩是否能够等于最小功能观测器阶次。 这比仅仅重新解释现有秩条件更有可能形成新的理论成果。





我继续深入后，已经找到一条比直接使用 Shannon 信息量更有希望的数学路线。它把你提出的问题连接到了三个成熟理论：

1. 商空间上的 PBH 可观测性理论；
2. Hankel 秩与最小状态空间实现理论；
3. 递归充分统计量与动态信息压缩理论。

其中，第一个方向已经可以得到一个严格的等价定理；第二个方向可以进一步得到 Hankel 秩刻画；第三个方向则需要谨慎处理，不能把条件熵直接当成观测器阶次。

我先给出目前最重要的推导。

# 一、先纠正一个理论定位：什么样的下界才是你真正需要的？

两篇论文实际上已经把问题分成了两个层次。

第一篇证明了：

\\[ q_0=\sum\_{j=1}^{r}\eta_j \\]

是代数条件允许的最小阶次，但只有当某个阶次为 \\(q_0\\) 的增广矩阵同时满足谱条件时，才有：

\\[ \nu\_{\min}=q_0. \\]

第二篇进一步证明：

\\[ q_0\leq\nu\_{\min}\leq n_0-p. \\]

并且逐阶刻画了所有可能的功能观测器阶次。这里特别重要的是：真正可行的阶次集合不一定是一个连续整数区间。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+2



所以，我们需要先认识一个数学事实。

假设我们构造了一个新的数值指标 \\(q\_\*\\)，同时证明：

\\[ q\_\*\leq\nu\_{\min}, \\]

并且：

\\[ \exists\ \text{一个阶次为 }q\_\*\text{ 的功能观测器}. \\]

那么必然有：

\\[ \nu\_{\min}\leq q\_\*. \\]

因此：

\\[ \boxed{q\_\*=\nu\_{\min}.} \\]

这说明，你所要求的不是普通意义上更强的下界，而是一个具有可实现性保证的精确最小阶次刻画。

我下面尝试利用商空间和 Hankel 秩，将这个问题转化为更容易分析的形式。

# 二、研究方向 A：将谱条件转化为商空间上的 PBH 可观测性

已经得到严格等价推导

这是目前最有实质进展的部分。

## 2.1 首先重新解释论文中的零空间

考虑：

\\[ \dot x=Ax+Bu,\qquad y=Cx,\qquad z=Lx. \\]

设某个候选功能观测器的阶次为 \\(q\\)，对应的增广功能矩阵为 \\(\mathcal L\\)。

定义：

\\[ \mathcal Z=\ker \begin{pmatrix} C\\\ \mathcal L \end{pmatrix}. \\]

记：

\\[ Z\in\mathbb R^{n\times d}, \qquad \operatorname{im}Z=\mathcal Z. \\]

根据论文中的降阶条件：

\\[ d=n-p-q. \\]

由于目标功能量可以从增广功能矩阵和测量输出中恢复，因此：

\\[ CZ=0,\qquad LZ=0. \\]

也就是说：

\\[ \mathcal Z\subseteq\ker C\cap\ker L. \\]

现在定义一个非常重要的子空间：

\\[ \boxed{ \mathcal U=\ker \begin{pmatrix} C\\\CA \end{pmatrix}. } \\]

它有一个很直观的意义：

对于 \\(v\in\mathcal U\\)，有：

\\[ Cv=0,\qquad CAv=0. \\]

也就是说，沿着这个方向改变状态，当前输出和输出的一阶导数都无法区分该状态变化。

我把它理解为系统中的一阶动态不可区分信息空间。

## 2.2 重新解释代数条件

论文 Theorem 3 中的代数条件为：

\\[ \operatorname{im}(AZR_Z) \subseteq\operatorname{im}Z, \\]

其中：

\\[ \operatorname{im}R_Z=\ker(CAZ). \\]

注意：

\\[ ZR_Z \\]

恰好张成：

\\[ \mathcal Z\cap\ker(CA) = \mathcal Z\cap\mathcal U. \\]

因此，代数条件可以完全等价地写成：

\\[ \boxed{ A(\mathcal Z\cap\mathcal U) \subseteq\mathcal Z. } \tag{A'} \\]

这个表达式比原来的矩阵秩条件更容易理解。

它表示：

对于已经被压缩掉、并且当前输出及其一阶导数都无法识别的状态方向，其动态演化仍然必须留在被压缩的信息空间内部。

否则，这些被压缩的信息会重新进入保留的系统动态，破坏观测器的代数闭合。

这个结论直接来自论文 Theorem 3，但这里给出了一个适合进一步建立商空间理论的几何表达。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 2.3 构造两个商空间

现在进入关键步骤。

定义：

\\[ \boxed{ \mathcal Q_Z= \mathcal U/(\mathcal U\cap\mathcal Z). } \\]

同时定义：

\\[ \boxed{ \mathcal W_Z= \ker C/\mathcal Z. } \\]

为什么选择这两个空间？

因为：

- \\(\mathcal Q_Z\\) 表示一阶动态不可区分信息中，尚未被压缩掉的部分；
- \\(\mathcal W_Z\\) 表示全部未被直接测量、并且尚未被压缩掉的状态信息。

二者的维数分别为：

\\[ s=\dim\mathcal Q_Z \\]

和：

\\[ \dim\mathcal W_Z=n-p-d=q. \\]

于是我们得到：

\\[ s\leq q. \\]

显然存在一个自然的嵌入映射：

\\[ J_Z:\mathcal Q_Z\longrightarrow\mathcal W_Z, \\]

定义为：

\\[ J_Z([v])=[v]. \\]

这里的方括号表示相应商空间中的等价类。

这个映射是单射。

接下来定义：

\\[ \overline A_Z:\mathcal Q_Z\longrightarrow\mathcal W_Z \\]

为：

\\[ \overline A_Z([v])=[Av]. \\]

为什么这个映射是良定义的？

假设：

\\[ [v_1]=[v_2]. \\]

那么：

\\[ v_1-v_2\in\mathcal U\cap\mathcal Z. \\]

根据刚才得到的代数条件：

\\[ A(v_1-v_2)\in\mathcal Z. \\]

所以：

\\[ [Av_1]=[Av_2]. \\]

因此：

\\[ \boxed{\overline A_Z\text{ 是良定义的。}} \\]

这一步是整个推导的核心：代数条件保证系统矩阵 \\(A\\) 能够在相应的商空间上定义一个动态映射。

## 2.4 核心定理：谱条件等价于商空间 PBH 条件

现在可以得到一个新的命题。

命题 1：商空间谱可行性定理

设 \\(\mathcal Z\subseteq\ker C\cap\ker L\\) 满足代数闭合条件：

\\[ A(\mathcal Z\cap\mathcal U)\subseteq\mathcal Z. \\]

定义：

\\[ \mathcal Q_Z=\mathcal U/(\mathcal U\cap\mathcal Z), \\]

\\[ \mathcal W_Z=\ker C/\mathcal Z. \\]

令 \\(J_Z\\) 和 \\(\overline A_Z\\) 分别为上述自然嵌入映射和诱导动态映射。

那么，论文中的谱条件等价于：

\\[ \boxed{ \operatorname{rank} (\lambda J_Z-\overline A_Z) =\dim\mathcal Q_Z, \quad \forall\lambda\in\Omega_S. } \\]

即这个商空间矩阵铅笔必须具有满列秩。

证明：

取矩阵 \\(V\\)，满足：

\\[ \operatorname{im}V=\mathcal U. \\]

论文中的谱条件是：

\\[ \operatorname{rank} \begin{pmatrix} (\lambda I-A)V&Z \end{pmatrix} = \operatorname{rank} \begin{pmatrix} V&Z \end{pmatrix}. \\]

注意：

\\[ \operatorname{rank} \begin{pmatrix} V&Z \end{pmatrix} = \dim(\mathcal U+\mathcal Z). \\]

利用商空间映射，可以将左侧写为：

\\[ \begin{aligned} &\operatorname{rank} \begin{pmatrix} (\lambda I-A)V&Z \end{pmatrix}\\\ &=\dim\mathcal Z+ \operatorname{rank}(\lambda J_Z-\overline A_Z). \end{aligned} \\]

另一方面：

\\[ \dim(\mathcal U+\mathcal Z) = \dim\mathcal Z+\dim\mathcal Q_Z. \\]

因此，两边秩相等当且仅当：

\\[ \operatorname{rank}(\lambda J_Z-\overline A_Z) = \dim\mathcal Q_Z. \\]

证毕。

这意味着论文中的谱条件虽然表现为关于 \\(\lambda\\) 的一族矩阵秩等式，但实际上可以转化为一个标准的商空间动态系统的可观测性问题。原论文的 Theorem 4、Theorem 5 给出了前一种矩阵表达。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



## 2.5 一个更重要的结果：转化为标准 PBH 可观测性

设：

\\[ s=\dim\mathcal Q_Z. \\]

因为 \\(J_Z\\) 是单射，我们可以适当选择商空间 \\(\mathcal W_Z\\) 的基，使得：

\\[ J_Z= \begin{pmatrix} I_s\\\ 0 \end{pmatrix}. \\]

在相同坐标系下，将诱导动态映射写成：

\\[ \overline A_Z= \begin{pmatrix} A_1\\\ A_2 \end{pmatrix}, \\]

其中：

\\[ A_1\in\mathbb R^{s\times s}, \\]

\\[ A_2\in\mathbb R^{(q-s)\times s}. \\]

于是：

\\[ \lambda J_Z-\overline A_Z = \begin{pmatrix} \lambda I_s-A_1\\\ -A_2 \end{pmatrix}. \\]

因此：

\\[ \boxed{ \operatorname{rank} \begin{pmatrix} \lambda I_s-A_1\\\ A_2 \end{pmatrix} =s. } \\]

这就是经典的 PBH 可观测性判据。

由此得到：

推论 1

在采用任意观测器极点配置要求时：

\\[ \Omega_S=\mathbb C, \\]

功能观测器的谱条件等价于：

\\[ \boxed{(A_1,A_2)\text{ 完全可观测。}} \\]

在仅要求渐近收敛时：

\\[ \Omega_S=\\{\lambda:\operatorname{Re}\lambda\geq0\\}, \\]

谱条件等价于：

\\[ \boxed{(A_1,A_2)\text{ 可检测。}} \\]

这里得到了一种新的解释：

一个候选功能观测器是否能够实现，取决于压缩信息后剩余的动态不可区分状态，能否通过商空间上的一个虚拟输出矩阵 \\(A_2\\) 完全观测出来。

这比直接讨论所有复数 \\(\lambda\\) 上的秩条件更加直观。

# 三、从上面的定理得到一个新的阶次分解

这是我认为上述命题最值得继续发展的地方。

定义：

\\[ h=\dim(\mathcal U+\mathcal Z). \\]

根据前面的定义：

\\[ s=h-d. \\]

同时：

\\[ q=n-p-d. \\]

因此：

\\[ q-s=n-p-h. \\]

令：

\\[ t=n-p-h. \\]

就有：

\\[ \boxed{q=s+t.} \\]

进一步：

\\[ t=\dim\frac{\ker C}{\mathcal U+\mathcal Z}. \\]

也就是说，功能观测器阶次可以分成两个部分：

\\[ \boxed{ \begin{aligned} q={}& \underbrace{\dim\frac{\mathcal U} {\mathcal U\cap\mathcal Z}}\_{\text{未压缩的一阶动态信息维数}}\\\ &+ \underbrace{\dim\frac{\ker C}{\mathcal U+\mathcal Z}}\_{\text{剩余输出创新维数}}. \end{aligned} } \\]

这两个部分具有不同的含义。

第一部分 \\(s\\)：需要在观测器内部保留的动态信息状态。

第二部分 \\(t\\)：未被直接测量、但又不属于一阶不可区分信息空间的剩余方向。

在商空间坐标下，\\(A_2\\) 恰好有 \\(t\\) 行。

因此，\\(t\\) 可以理解为将隐藏动态信息暴露出来的独立创新通道数。

## 一个立即得到的谱可行性结论

如果：

\\[ t=0,\qquad s>0, \\]

那么：

\\[ A_2=0. \\]

PBH 矩阵变成：

\\[ \lambda I_s-A_1. \\]

对于任意有限维复数域上的方阵 \\(A_1\\)，特征多项式必然存在复根。

因此：

\\[ \boxed{ t=0,\ s>0 \quad\Longrightarrow\quad \text{不可能实现任意极点配置。} } \\]

但对于仅要求渐近稳定的功能观测器，情况不同。如果 \\(A_1\\) 本身是 Hurwitz 矩阵，则即使 \\(A_2=0\\)，仍然可能满足检测性要求。

这一区别非常重要，说明极点任意配置和渐近收敛所要求的动态信息保留量并不相同。

# 四、研究方向 B：构造功能信息 Hankel 矩阵

得到可验证的有限秩条件

有了上面的商空间定理，Hankel 秩就不再是凭空引入的概念，而是自然出现的。

## 4.1 从商空间系统构造传递矩阵

我们已经得到：

\\[ (A_1,A_2), \\]

并且要求它满足可观测性。

构造一个辅助状态空间系统：

\\[ \begin{cases} \dot \xi=A_1\xi+v,\\\ \omega=A_2\xi. \end{cases} \\]

其中：

\\[ \xi\in\mathbb R^s,\qquad v\in\mathbb R^s,\qquad \omega\in\mathbb R^t. \\]

其传递矩阵为：

\\[ \boxed{ G_Z(\zeta)=A_2(\zeta I-A_1)^{-1}. } \\]

这里使用单位矩阵作为输入矩阵，因此 \\((A_1,I_s)\\) 自动完全可控。

于是，辅助系统的最小实现阶次恰好等于：

\\[ \operatorname{rank} \begin{pmatrix} A_2\\\ A_2A_1\\\ \vdots\\\ A_2A_1^{s-1} \end{pmatrix}. \\]

当且仅当 \\((A_1,A_2)\\) 完全可观测时：

\\[ \boxed{\delta_M(G_Z)=s.} \\]

其中 \\(\delta_M\\) 表示 McMillan 阶次。

这将功能观测器的谱条件与经典最小实现理论连接起来。Hankel 秩等于最小实现阶次，是 Ho–Kalman 实现理论中的经典结论。

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

数字对象标识符



## 4.2 构造功能信息 Hankel 矩阵

定义 Markov 参数：

\\[ M_k=A_2A_1^k,\qquad k=0,1,2,\ldots \\]

构造：

\\[ \mathscr H\_\ell(Z)= \begin{pmatrix} M_0&M_1&\cdots&M\_{\ell-1}\\\ M_1&M_2&\cdots&M\_\ell\\\ \vdots&\vdots&\ddots&\vdots\\\ M\_{\ell-1}&M\_\ell&\cdots&M\_{2\ell-2} \end{pmatrix}. \\]

它具有分解：

\\[ \mathscr H\_\ell(Z) = \underbrace{ \begin{pmatrix} A_2\\\ A_2A_1\\\ \vdots\\\ A_2A_1^{\ell-1} \end{pmatrix}}\_{\mathscr O\_\ell} \underbrace{ \begin{pmatrix} I&A_1&\cdots&A_1^{\ell-1} \end{pmatrix}}\_{\mathscr R\_\ell}. \\]

因为 \\(\mathscr R\_\ell\\) 包含单位矩阵块，所以它具有满行秩。

当 \\(\ell=s\\) 时：

\\[ \boxed{ \operatorname{rank}\mathscr H_s(Z)=s \iff (A_1,A_2)\text{ 完全可观测}. } \\]

因此，在任意极点配置意义下，我们已经得到：

\\[ \boxed{ \text{功能观测器谱可行} \iff \operatorname{rank}\mathscr H_s(Z)=s, } \\]

前提是候选子空间满足代数闭合条件。

这就是我建议进一步研究的商空间功能 Hankel 秩。

它有两个优势：

- 不必直接检查连续无穷多个复数 \\(\lambda\\)；
- 可以通过有限维矩阵的秩，判断所有动态信息模式是否可以区分。

对于渐近观测器，可以将完全可观测改为可检测，此时不能再要求 Hankel 矩阵满秩，而应检查其未观测部分是否全部渐近稳定。

## 4.3 一个更有价值的结果：最小阶次的分解公式

对于任意极点配置情形，由于：

\\[ s=\operatorname{rank}\mathscr H_s(Z), \\]

以及：

\\[ t=\dim\frac{\ker C}{\mathcal U+\mathcal Z}, \\]

我们得到：

\\[ \boxed{ q= \operatorname{rank}\mathscr H_s(Z) + \dim\frac{\ker C}{\mathcal U+\mathcal Z}. } \\]

这意味着：

观测器阶次不再只被解释为需要保存的内部状态数量，而可以分解成：

1. 动态信息系统的最小实现阶次；
2. 还没有被当前输出和一阶输出信息解释掉的剩余维数。

进一步，我们可以提出一个候选的精确优化表达式：

\\[ \boxed{ \nu\_{\min} = \min\_{\mathcal Z\in\mathfrak Z_A} \left[ \operatorname{rank}\mathscr H\_{s(\mathcal Z)}(\mathcal Z) + \dim\frac{\ker C}{\mathcal U+\mathcal Z} \right] } \\]

其中 \\(\mathfrak Z_A\\) 表示所有满足：

\\[ \mathcal Z\subseteq\ker C\cap\ker L \\]

以及：

\\[ A(\mathcal Z\cap\mathcal U)\subseteq\mathcal Z \\]

的候选子空间。

这里还要附加：

\\[ \operatorname{rank}\mathscr H\_{s(\mathcal Z)}(\mathcal Z) =s(\mathcal Z). \\]

因此，每一个参与最小化的候选子空间都具有相应的功能观测器。

注意：这个公式是对最小阶次的 Hankel—商空间重表达，不应当冒充一个已经消除了子空间搜索的新闭式下界。 它的下一步价值在于寻找能够直接计算最大可压缩维数的结构性条件。

# 五、利用原论文的数值例子检验新理论

现在我们不只停留在理论推导，而是使用第二篇论文第 VII 节的例子进行一次独立的矩阵计算。

论文给出的系统满足：

\\[ n=8,\qquad p=2,\qquad r=2. \\]

并且：

\\[ q_0=3,\qquad n_0-p=6. \\]

论文证明：

\\[ \Sigma\_{FO}(L)=\\{5,6\\}. \\]

所以：

\\[ \nu\_{\min}=5. \\]

这个例子已经明确分离了代数下界和真实最小阶次。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



## 5.1 考察阶次为 5 的候选观测器

论文给出的可行零空间基向量为：

\\[ Z_5= \begin{pmatrix} 1&1&1&0&-2&1&0&0 \end{pmatrix}^{T}. \\]

它满足：

\\[ CZ_5=0,\qquad LZ_5=0. \\]

同时：

\\[ CAZ_5= \begin{pmatrix} -3\\\\-1 \end{pmatrix}. \\]

因此：

\\[ \ker(CAZ_5)=\\{0\\}. \\]

代数条件自动成立。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



现在：

\\[ d=1,\qquad \dim\mathcal U=4. \\]

因为：

\\[ \mathcal Z_5\cap\mathcal U=\\{0\\}, \\]

所以：

\\[ s=\dim\mathcal Q\_{Z_5}=4. \\]

而：

\\[ q-s=5-4=1. \\]

也就是说，这个五阶观测器的商空间系统具有四维动态状态和一个独立的创新通道。

## 5.2 计算诱导矩阵

选取 \\(\mathcal U\\) 的一组有理数基，并补充一个属于 \\(\ker C\\) 的方向：

\\[ v_0= (-1,1,0,0,0,0,0,0)^T. \\]

在相应的商空间坐标下，可以得到一组诱导矩阵：

\\[ A_1= \begin{pmatrix} 12&-2&-24&-11\\\ -7&-1&13&6\\\ 0&-1&-2&1\\\ 0&0&1&-2 \end{pmatrix}, \\]

\\[ A_2= \begin{pmatrix} -12&-1&21&12 \end{pmatrix}. \\]

这里的矩阵数值依赖所选基，但可观测性不依赖基的选择。

于是：

\\[ \mathscr O_4= \begin{pmatrix} A_2\\\ A_2A_1\\\ A_2A_1^2\\\ A_2A_1^3 \end{pmatrix}. \\]

使用精确有理数计算，得到：

\\[ \boxed{\det\mathscr O_4=4228\neq0.} \\]

因此：

\\[ \operatorname{rank}\mathscr O_4=4. \\]

也就是说：

\\[ (A_1,A_2) \\]

完全可观测。

从而：

\\[ 5\in\Sigma\_{FO}(L). \\]

这与论文中的 gcd 检验结果一致：

\\[ \gcd\_\lambda\\{\Delta_j(\lambda)\\}=1. \\]

但我们现在得到了一个不同的解释：原来复杂的矩阵铅笔条件，在合适的商空间坐标下，就变成了一个普通的四阶可观测性矩阵满秩条件。

这也是本次研究最具体的一个计算结果。

## 5.3 对阶次 3 和 4 的进一步启示

论文已经严格证明：

\\[ 3\notin\Sigma\_{FO}(L), \qquad 4\notin\Sigma\_{FO}(L). \\]

根据刚才的命题，这意味着：

- 所有满足代数条件的三阶候选方案，其诱导商空间对均不能完全可观；
- 所有满足代数条件的四阶候选方案，其诱导商空间对也不能完全可观。

这就为解释原论文的反例提供了新的研究入口。

与其对每个候选增广矩阵反复计算多项式最大子式的 gcd，不如直接寻找：

\\[ \ker\mathscr O_s(Z). \\]

如果能对整个 Grassmann 参数族证明这个核始终非零，并进一步找到对应的不可观测特征模态，就可能得到一个更加简洁的非存在性证明。

这里还没有完成对 \\(q=3,4\\) 所有候选分支的精确消元，因此暂时不能声称已经找到了它们共同的不可观测特征值。这是下一步需要攻克的具体问题。

# 六、研究方向 C：真正的信息论应该研究什么？

需要进一步建立理论

前面两个方向已经有了明确的代数基础。现在回过头来讨论信息论。

我想修正前面一个容易引起误解的地方：

Rényi 信息维数不能直接等于最小功能观测器阶次。

例如，系统满足功能可观测性：

\\[ \operatorname{row}(\mathcal O_L) \subseteq \operatorname{row}(\mathcal O_C). \\]

这意味着从一段有限时间的输出轨迹和已知输入中，能够唯一确定所需功能量。

因此，在无噪声条件下，如果采用适当的随机初始状态模型，那么目标功能量对完整输出历史的条件不确定性已经消失。

但是：

\\[ \text{目标信息能够从完整历史中确定} \\]

并不意味着：

\\[ \text{不需要保存任何内部动态状态}. \\]

例如，上面的例子中：

\\[ r=2,\qquad\nu\_{\min}=5. \\]

虽然只需要估计两个功能量，但还必须保存五维观测器状态。

这五维不是目标变量的静态信息维数，而是实现实时递归重构所需的动态记忆。

所以，我建议将研究重点从 Shannon 熵转向递归充分统计量。

## 6.1 定义递归充分统计量

设：

\\[ \mathscr Y_t= \\{y(\tau):0\leq\tau\leq t\\} \\]

为输出历史。

定义一个信息状态：

\\[ s(t)=\Phi(\mathscr Y_t,u\_{[0,t]}). \\]

要求它具有三个性质：

性质 1：功能充分性

存在一个重构映射，使得：

\\[ z(t)=\Psi(s(t),y(t)) \\]

或者在允许的渐近意义下成立。

性质 2：递归闭合性

未来的信息状态只依赖于当前信息状态以及后续输入和输出，不需要保留全部历史：

\\[ s(t+\Delta) = \Gamma\_\Delta \left( s(t),y\_{[t,t+\Delta]},u\_{[t,t+\Delta]} \right). \\]

性质 3：有限维线性实现性

存在：

\\[ \dot s=Fs+Gy+Hu, \\]

且：

\\[ \dim s=q. \\]

于是定义：

\\[ \boxed{ d\_{\mathrm{rec}} = \min\dim s. } \\]

这才是和最小功能观测器阶次相对应的信息维数。

在上述线性时不变、已知输入、线性观测器和指定谱条件的框架下，若将信息状态限制为有限维线性递归实现，就有：

\\[ \boxed{d\_{\mathrm{rec}}=\nu\_{\min}.} \\]

这一定义本身仍属于观测器实现问题的另一种表述；真正有价值的是利用前面得到的商空间 Hankel 矩阵来计算它。

## 6.2 信息压缩与 Hankel 秩的关系

我们现在可以提出一个比 Shannon 熵更适合的概念：

动态信息复杂度（Dynamic Information Complexity）。

对某个候选压缩空间 \\(\mathcal Z\\)，定义：

\\[ \mathfrak D(\mathcal Z) = \operatorname{rank}\mathscr H_s(\mathcal Z) + \dim\frac{\ker C}{\mathcal U+\mathcal Z}. \\]

在任意极点配置情形：

\\[ \mathfrak D(\mathcal Z)=q \\]

当且仅当：

- 代数闭合条件成立；
- 商空间 Hankel 秩达到 \\(s\\)。

因此：

\\[ \boxed{ \nu\_{\min} = \min\_{\mathcal Z\text{ 满足动态信息充分性}} \mathfrak D(\mathcal Z). } \\]

这才是我认为真正有希望发展成信息论下界理论的表达式。

它至少有三个优点：

1. 不依赖任意选取的状态协方差矩阵。
2. 具有坐标不变性。
3. 每一个满足条件的压缩空间都可以构造对应的功能观测器。

不过，这仍然是一个带子空间约束的优化问题。要称为新的信息论下界，还需要找到它的闭式计算方法，或者证明一组可直接由 \\(A,C,L\\) 计算的充分条件。

# 七、研究方向 D：发展真正可以计算的严格下界

现在把三个方向放在一起，可以进一步形成一个更接近算法的方案。

## 7.1 定义两个新的结构指标

对于每个满足代数条件的候选压缩空间 \\(\mathcal Z\\)，定义：

\\[ \mu(\mathcal Z) = \dim\frac{\mathcal U}{\mathcal U\cap\mathcal Z}, \\]

以及：

\\[ \tau(\mathcal Z) = \dim\frac{\ker C}{\mathcal U+\mathcal Z}. \\]

于是：

\\[ q=\mu(\mathcal Z)+\tau(\mathcal Z). \\]

在任意极点配置要求下：

\\[ \mu(\mathcal Z) = \operatorname{rank}\mathscr H\_{\mu(\mathcal Z)}(\mathcal Z). \\]

因此，问题可以归结为：

\\[ \boxed{ \nu\_{\min} = \min\_{\mathcal Z} \left(\mu(\mathcal Z)+\tau(\mathcal Z)\right) } \\]

其中需要保证：

\\[ \begin{cases} \mathcal Z\subseteq\ker C\cap\ker L,\\\ A(\mathcal Z\cap\mathcal U)\subseteq\mathcal Z,\\\ \operatorname{rank}\mathscr H\_{\mu(\mathcal Z)}(\mathcal Z) =\mu(\mathcal Z). \end{cases} \\]

这是一个同时包含信息压缩、动态实现和谱可行性的优化问题。

## 7.2 得到一个新的必要条件

由于：

\\[ (A_1,A_2) \\]

完全可观测，如果：

\\[ \mu(\mathcal Z)>0, \\]

就必须有：

\\[ \tau(\mathcal Z)>0. \\]

因此：

\\[ \boxed{ \dim(\mathcal U+\mathcal Z) \leq n-p-1. } \\]

这个条件对任意极点配置是必要的。

这给出了一个很简单的计算筛选方法：

假设对于某个阶次 \\(q\\)，所有满足代数条件的候选子空间都满足：

\\[ \mathcal U+\mathcal Z=\ker C. \\]

那么可以直接排除该阶次，无需再计算任何特征值或者多项式最大子式。

对于渐近观测器，如果：

\\[ \mathcal U+\mathcal Z=\ker C, \\]

则需要进一步检查诱导矩阵 \\(A_1\\) 是否 Hurwitz。

这个结果还不是最终的最小阶次下界，但它给出了一个可以直接使用的新型谱筛选条件。

## 7.3 渐近稳定情形的 LMI 算法

对于仅要求误差渐近收敛的情形，有一个额外优势。

根据前面的商空间 PBH 定理：

\\[ (A_1,A_2)\text{ 可检测} \\]

当且仅当存在矩阵 \\(K\\)，使得：

\\[ A_1-KA_2 \\]

为 Hurwitz 矩阵。

这又等价于存在：

\\[ P=P^T>0,\qquad Y \\]

使得：

\\[ \boxed{ A_1^TP+PA_1-A_2^TY^T-YA_2<0. } \\]

其中：

\\[ Y=PK. \\]

因此，对于一个已经确定的候选空间 \\(\mathcal Z\\)，不必进行连续频域上的秩搜索，而可以直接利用 LMI 检验其检测性。

如果把 Grassmann 参数 \\(\Theta\\) 也作为优化变量，那么整体问题仍然是非凸的；但是固定 \\(\Theta\\) 后，稳定性检验是标准凸 LMI 问题。

这提供了一个有实际计算价值的算法框架：

拟议算法：动态信息压缩与商空间可观测性

1. 计算基础空间

   \\[ K=\ker\begin{pmatrix}C\\\L\end{pmatrix}, \qquad U=\ker\begin{pmatrix}C\\\CA\end{pmatrix}. \\]
2. 确定候选信息压缩维数

   对每个：

   \\[ q=q_0,q_0+1,\ldots,n_0-p \\]

   令：

   \\[ d=n-p-q. \\]
3. 参数化压缩子空间

   使用 Grassmann 坐标：

   \\[ Z=K_LW\_{\mathcal I}(\Theta). \\]

   这里沿用第二篇论文的完整参数化方法。
4. 施加动态闭合条件

   \\[ A(U\cap\operatorname{im}Z) \subseteq\operatorname{im}Z. \\]
5. 构造商空间系统

   得到：

   \\[ (A_1(\Theta),A_2(\Theta)). \\]
6. 检验动态信息充分性

   对任意极点配置，检验：

   \\[ \operatorname{rank}\mathscr O_s(\Theta)=s. \\]

   对渐近稳定要求，则检验对应的检测性 LMI。
7. 返回第一个可行阶次

   因为每个被接受的候选空间都有对应的观测器，所以第一个可行阶次就是精确的最小阶次。

与第二篇论文的逐阶 Grassmann 参数化方法相比，这个方案最主要的变化是将谱条件转化成了标准的可观测性或检测性问题。原论文给出的完整阶次刻画仍然是正确性基础，而商空间方法提供了新的计算实现路线。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+2



# 八、还有一个值得深入研究的方向：能否找到不依赖 Grassmann 搜索的闭式下界？

这是目前最没有解决、但也最有研究价值的部分。

我们希望找到一个直接由：

\\[ A,\quad C,\quad L \\]

计算的指标，避免对每一个阶次都搜索所有可能的 \\(\mathcal Z\\)。

我考虑了以下几个可能性。

## 8.1 利用不可观测模态构造强制保留信息空间

考虑：

\\[ Av=\lambda v,\qquad Cv=0. \\]

由于：

\\[ CAv=\lambda Cv=0, \\]

所以：

\\[ v\in\mathcal U. \\]

如果 \\(\mathcal Z\\) 不包含该方向，那么：

\\[ (\lambda I-A)v=0\in\mathcal Z, \\]

对应的 PBH 条件一定失败。

因此，对于任意极点配置：

\\[ \boxed{ \ker(A-\lambda I)\cap\ker C \subseteq\mathcal Z, \qquad \lambda\in\mathbb C. } \\]

不过，功能可观测性意味着这些不可观测特征向量已经满足：

\\[ Lv=0. \\]

所以它们本来就位于：

\\[ \ker C\cap\ker L. \\]

真正有意义的是：除了特征向量之外，是否还需要将某些广义特征向量、Jordan 链方向纳入压缩空间？

我认为可以研究：

\\[ \mathcal E\_\lambda^{(k)} = \ker(A-\lambda I)^k\cap\ker C. \\]

再考察这些广义特征子空间与 \\(\mathcal Z\\) 的交集关系。

这里要注意，单纯包含所有不可观测广义特征子空间并不能直接解决问题，因为 \\(\mathcal Z\\) 已经受到 \\(\ker L\\) 和代数闭合条件约束。需要研究的是这些子空间与动态信息压缩条件之间的耦合。

这条路线可能产生一个基于 Jordan 结构的显式下界。

## 8.2 利用代数可行族的维数

第二篇论文把候选空间参数化为：

\\[ Z=K_LW\_{\mathcal I}(\Theta). \\]

其中：

\\[ \Theta\in\mathbb R^{(m_L-d)\times d}. \\]

但是，不同阶次的代数可行集合具有不同的几何结构。

我们可以定义：

\\[ \mathcal V_d^A = \left\\{ \mathcal Z: \dim\mathcal Z=d,\  \mathcal Z\subseteq K,\  A(\mathcal Z\cap U)\subseteq\mathcal Z \right\\}. \\]

它是 Grassmann 流形中的一个代数约束集合。

再定义：

\\[ \mathcal V_d^{AS} = \left\\{ \mathcal Z\in\mathcal V_d^A: (A_1,A_2)\text{ 满足指定谱条件} \right\\}. \\]

真正的下界问题变成：

\\[ d\_{\max} = \max\left\\{ d:\mathcal V_d^{AS}\neq\varnothing \right\\}. \\]

然后：

\\[ \boxed{ \nu\_{\min}=n-p-d\_{\max}. } \\]

这与第二篇论文 Theorem 9 的核心数学内容等价，但可以进一步利用代数几何工具分析可行集合的维数、分支和非空性。

例如，可以研究：

- 哪些条件导致 \\(\mathcal V_d^A\\) 为空；
- 哪些条件使全部代数可行分支都落在不可观测集合内；
- 哪些参数情况下，存在一个开稠密的谱可行子集；
- 是否可以通过消元得到一个直接关于 \\(d\\) 的判别多项式。

我认为这可能是形成闭式下界的关键。

# 九、目前几个方向的研究成熟度

把目前的结果放在一起，我认为可以这样判断：

| 研究方向        | 当前进展       | 下一步关键问题        |
| ----------- | ---------- | -------------- |
| 商空间 PBH 理论  | 已有严格等价推导   | 研究结构性可行条件      |
| Hankel 秩刻画  | 已建立有限秩条件   | 消除对候选子空间的依赖    |
| 递归信息充分性     | 已建立数学框架    | 与确定性信息维数建立严格关系 |
| Jordan 结构下界 | 已找到切入点     | 证明必要包含关系和维数界   |
| 代数几何优化      | 可沿论文方法推进   | 找出可行集合非空的闭式判据  |
| 渐近检测性       | 已得到 LMI 形式 | 开发全局子空间优化算法    |

我现在最看好的，是前两个方向结合第三个方向：

\\[ \boxed{ \text{商空间动态系统} \longrightarrow \text{功能 Hankel 秩} \longrightarrow \text{递归信息维数} } \\]

这条路线具有明确的数学基础，而且不是简单地把熵、秩和观测器阶次混为一谈。

# 十、我建议形成的论文核心理论

如果以此为基础撰写一篇新论文，我建议将题目暂定为：

Dynamic Information Compression and Hankel-Rank Characterization of Minimum-Order Functional Observers

中文可以叫：

动态信息压缩与最小阶功能观测器的 Hankel 秩刻画。

建议核心定理由三个部分组成。

定理 A：商空间谱可行性等价定理

证明任意候选增广矩阵的谱条件等价于诱导对 \\((A_1,A_2)\\) 的 PBH 可观测性或检测性。

这一部分目前已经有了完整推导。

定理 B：功能 Hankel 秩定理

证明：

\\[ \operatorname{rank}\mathscr H_s(Z)=s \\]

当且仅当对应的商空间动态信息系统完全可观测，并建立：

\\[ q= \operatorname{rank}\mathscr H_s(Z) + \dim\frac{\ker C}{U+Z}. \\]

这一部分也已经具有明确的证明路线。

定理 C：最小动态信息维数定理

尝试证明存在一组只依赖 \\(A,C,L\\) 的结构性指标，使得：

\\[ \boxed{ \nu\_{\min} = \Phi(A,C,L) } \\]

其中 \\(\Phi\\) 不需要搜索所有 Grassmann 子空间。

这是最终最值得攻克的核心难题，也是目前尚未解决的部分。

# 十一、参考文献补充与研究边界

除了你给出的两篇论文，还建议关注以下工作：

1\. Fernando, T. (2010). Functional Observability and the Design of Minimum Order Linear Functional Observers. IEEE Transactions on Automatic Control, 55(5), 1268–1273. DOI: 10.1109/TAC.2010.2042761。[论文信息](https://doi.org/10.1109/TAC.2010.2042761?utm_source=chatgpt.com)。

2\. Darouach, M. and Fernando, T. (2025). On Functional Observability and Functional Observer Design. Automatica, 173, 112115. DOI: 10.1016/j.automatica.2025.112115。[论文信息](https://www.sciencedirect.com/science/article/pii/S0005109825000068?utm_source=chatgpt.com)。

3\. Ho, B. L. and Kalman, R. E. (1966). Effective Construction of Linear State-Variable Models from Input/Output Functions. Regelungstechnik, 14, 545–548。

4\. Kailath, T. (1980). Linear Systems. Prentice-Hall。

5\. Fernando, T. (2026). Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger. arXiv:2609.37992。[论文全文](https://arxiv.org/html/2609.37992?utm_source=chatgpt.com)。

这些文献分别提供功能可观测性、最小功能观测器、PBH 判据及 Hankel 最小实现理论的基础。特别需要注意，商空间 PBH 推导是对现有秩条件的重新组织；是否属于已有文献中未被提出的原创结果，还需要继续进行针对性的文献比对，不能仅凭这次推导就宣称已经解决了相关开放问题。

# 十二、下一步我认为应该集中攻克什么？

我不建议现在就把所有方向平均推进。最有价值的是对原论文的这个反例做一次更深的理论分析。

具体来说，下一步应该完成三个任务：

第一：彻底分析 \\(q=3\\) 的四个 Grassmann 分支。

将每个分支的代数条件化为精确多项式方程，构造对应的商空间矩阵对，寻找其必然存在的不可观测模态。

第二：彻底分析 \\(q=4\\) 的六个 Grassmann 分支。

尝试证明所有代数可行分支都不满足商空间 PBH 条件，并寻找一个不需要逐个计算 gcd 的统一证明。

第三：研究 \\(q=5\\) 的结构性优势。

前面的计算已经给出：

\\[ \det\mathscr O_4=4228. \\]

接下来应该研究这个非零行列式能否表示为系统矩阵和功能矩阵的某个结构性不变量，而不是只针对一个具体数值例子。

如果这三个任务能够完成，我们就有机会从原论文的数值反例中提炼出一个真正的新定理：

代数最小阶次与实际最小阶次之间的差距，究竟由哪些动态不可观测模态决定？

我认为这比单纯再提出一个更大的下界更值得研究。

我建议下一轮直接攻克原例 \\(q=3,4\\) 的全部代数分支，使用精确有理数和 Gröbner 基进行消元，争取给出统一的非存在性证明。这将是检验商空间 PBH 理论是否真正带来新成果的关键一步。

另可定期追踪这个方向的新论文及相关理论进展：

📚每周追踪功能观测器理论新进展轻点设置