# kronecker —— Workstream B：观测器诱导铅笔的 Kronecker 结构

> 专家 2026-11-02 指定的**主结构方向**。目标定理的形式：
> $$\boxed{\text{观测器诱导的最小层铅笔具有受限的 Kronecker 结构}}$$
> 本目录放：问题陈述、实验记录、以及"什么算成功"的判定标准。

## 1. 为什么是这个问题

- $(5b)$ 已经是一个 **Kronecker 型条件**：$Q_{\mathcal V}(\lambda)$ 的 Kronecker 形**没有正则初等因子**
  （左右奇异块都允许；这是专家 2026-10-30 更正后的正确表述，见
  [proof/layer_program/RESTRICTED_COMPLETION_MODEL.md](../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md) §2）；
- 但"**给定实例，$\exists\mathcal V$ 使型落在这个集合里**"没有现成判据：Dodig (LAA 2008) 的
  行/列补全理论解决的是"**独立新增行/列**"，而我们的自由度是**子空间**（一行选定 ⟹ 全部行同时确定），
  且还带 $(5a)$ 与维数型的**等式**约束 ⟹ 可达集是 Grassmannian 上的 constructible 集；
- 所以问题是：**观测器诱导的铅笔能有哪些 Kronecker 型？**

## 2. 工具（2026-11-02 建好）

| 文件 | 作用 |
|---|---|
| [tools/verification/kronecker_pencil.py](../../tools/verification/kronecker_pencil.py) | 铅笔的 Kronecker 数据：normal rank、有限/无穷初等因子、左右最小指标（精确有理算术；标准块自检通过）|
| [tools/verification/observer_pencils.py](../../tools/verification/observer_pencils.py) | 从 $(A,C,L_0)$ 与 $\mathcal V$ **构造真实的观测器铅笔** $Q_L(\lambda)=[\lambda L-LA;CA;C]$，含 $(5a)/(5b)$ 判定与交叉核对 |
| [tools/verification/kron_struct_scan.py](../../tools/verification/kron_struct_scan.py) | 五步实验驱动（专家 §3 的程序），输出 TSV |

数据：[data/scan_2026-11-02.tsv](data/scan_2026-11-02.tsv)（37 个铅笔）。

## 3. 第一次实验的结论（证据，不是证明）

- 4 个真实实例（$n=6$，seed 1002/1003/1015/1019），候选 $\mathcal V$ 来自两族：
  **(i)** 对 $x\mapsto xA$ **不变**的子空间；**(ii)** 只满足"模 $\mathcal J$ 不变"（即 $(5a)$）的子空间
  （先商空间闭包、再提升，最后用**精确 $(5a)$ 检验**过滤）。共 **42 个**观测器铅笔；
- **$(5b)$ 成立的 8 个**，**全部在 $\rho=0$**（即 $L$ 的行落在 $\mathcal J$ 里，形如 $L=C$ 的平凡解）；
  $\rho\ge1$ 的 34 个**全部不可行**；可行铅笔的型都**没有有限初等因子** ✓；
- **一个曾差点被当成结果的现象**：过滤前有 2 个 $\rho=1$ 的铅笔满足 $(5b)$——但它们**不满足 $(5a)$**（是非法候选）。
  加 $(5a)$ 过滤后消失 ⟹ 又一次"先断言再报告"避免了误报。

### 3.1 已知可行实例（$\rho\ge1$）的型（2026-11-02，[kron_known_instances.py](../../tools/verification/kron_known_instances.py)）

用项目里**已知有解**的实例（$n=6$、$(\rho,c)=(3,1)$、$(5a)+(5b)$ 都成立；来源
[proof/rho1_layer/verify_mu1_good_instance.py](../../proof/rho1_layer/verify_mu1_good_instance.py) §55）：

| 候选 | $q$ | $h$ | $(\rho,c)$ | $(5b)$ | Kronecker 型 |
|---|---|---|---|---|---|
| $\mathcal V=\langle e_1,e_2,e_3,e_5\rangle$ | 4 | 5 | $(3,1)$ | **✓** | 5 个零不变因子；**左指标 $\varepsilon=[4]$**；右指标 $\eta=[0]$；无穷因子 $[0,0,0,0,1]$ |
| $L=C$（平凡解）| 1 | 2 | $(0,1)$ | ✓ | 2 个零不变因子；$\varepsilon=[1]$；$\eta=[0,0,0,0]$；无穷因子 $[0,1]$ |

**要点**：可行的（$(5b)$ 成立的）铅笔可以有**很大的左最小指标**（$\varepsilon=[4]$），
再次说明"可行 ⟹ 只有右奇异块"是错的；同时它给出**第一个 $\rho\ge1$ 的可行型**样本。
- **观察到的可行型**：$\varepsilon$（左最小指标）**非空**（如 $[1,0]$），$\eta$（右最小指标）多是 $0$；
  ——即"可行 ⟹ 只有右奇异块"这个**旧说法是错的**（与专家 2026-10-30 的更正一致 ✓）；
- **没有**观察到"只有右奇异块"或"只有左奇异块"的可行铅笔（本样本内）；
- 固定 $\rho$ 下既有可行也有不可行（$\rho=1$：6 个里 2 个可行）⟹ 型**不由** $(\rho,c)$ 决定（与 S1 被反驳一致）。


### 3.2 撒网：12 个实例、59 个合法铅笔、4 个可行（$\rho\ge1$）

脚本 [kron_sweep.py](../../tools/verification/kron_sweep.py)，数据 [data/sweep_12seeds.tsv](data/sweep_12seeds.tsv)。

| seed | $q$ | $(\rho,c)$ | $h$ | 有限因子 | 右指标 $\eta$ | 左指标 $\varepsilon$ |
|---|---|---|---|---|---|---|
| 1001 | 6 | $(4,2)$ | 6 | 全零 | $\varnothing$ | $[5,1]$ |
| 1010 | 4 | $(3,1)$ | 5 | 全零 | $[0]$ | $[4]$ |
| 1010 | 5 | $(3,2)$ | 5 | 全零 | $[0]$ | $[4,1]$ |

（第 3 行出现两次：同一实例上的两个不同 $\mathcal V$。）

**两条观察——第 1 条已于 2026-11-02 撤回（专家指出 + 反例）**：

1. ~~右最小指标全为 $0$~~ **撤回** ✗（[proof/refuted R18](../../proof/refuted/README.md)）。
   我原来的理由"$(5b)$ ⟹ $\ker Q(\lambda)$ 常值 ⟹ 可取常数基"是**错的**：维数恒定不意味着子空间恒定。
   **反例**：$Q(\lambda)=\begin{pmatrix}\lambda&1\end{pmatrix}$，秩恒 1，但右最小指标 $=1$。
   正确表述：常数秩 ⟺ **无有限初等因子**（正则部分的条件），对最小指标的**次数**不给任何约束。
   证据：[kron_identity_probe.py](../../tools/verification/kron_identity_probe.py) 第 1 节。
2. 左最小指标**普遍很大**（$[5,1]$、$[4]$、$[4,1]$）——这一条仍成立（观察，非定理）；
   无穷因子是 $[0,\dots,0,1]$ 型。

**正确的全局恒等式**（专家 2026-11-02 §3）：
$$\sum_i\eta_i+\sum_j\varepsilon_j+\sum_k\deg\gamma_k=r\quad(\gamma_k\ \text{齐次不变因子}),$$
在 $(5b)$ 型下退化为 $\sum\eta+\sum\varepsilon+d_\infty=r$。**已在全部可行样本上核对成立** ✓
（§55：$0+4+1=5$；seed 1001：$0+6+0=6$；seed 1010：$0+4+1=5$）。
注意 $\sum\deg\gamma_k\ne\sum\deg(\text{有限})+\sum\deg(\text{反转})$（反例见同一脚本第 2 节）。
**因此"右指标之和"不能被单独当作不变量**——要研究的是三元组
$(\{\eta_i\},\{\varepsilon_j\},d_\infty)$。

## 4. 边界（必须写清）

1. 样本只有 4 个实例、$n=6$、且 $\mathcal V$ 限定在"A-不变闭包"这一族 ⟹ **不是**全类型普查；
2. 结论是"记录到/没记录到"，**不是**"只能出现这些"；
3. 交叉核对：方阵正则时用 det 次数、奇异时用采样秩（采样只能反驳）；未对全部 37 个做子式枚举级独立核对。

## 4.5 目标形式 T

**[TARGET_FORM_T.md](TARGET_FORM_T.md)**：按专家 §6 的模板写的暂定目标形式——
第 1–3 条是铅笔理论的一般事实（含已核对的恒等式），**第 4 条才是猜想**（右指标是否为 0 / $d_\infty$ 是否有界 / 左侧下界）。


### 4.6 归一化问题的答案（专家 §5）：商铅笔是**压缩**，不是等价

脚本 [kron_layer_relation.py](../../tools/verification/kron_layer_relation.py) 同时构造
**原始** $Q_L(\lambda)=[\lambda L-LA;CA;C]$ 与 **商铅笔** $Q_{\rm quot}(\lambda)=\lambda\Pi-\Pi T$（docs/02 B.1 的对象），
逐点核对秩恒等式并比较 Kronecker 数据。

**秩恒等式成立**（17 个有理 $\lambda$，两个实例）：
$$\operatorname{rank}Q_L(\lambda)=j+\operatorname{rank}Q_{\rm quot}(\lambda),\qquad j=\dim\mathcal J .$$

**但 Kronecker 数据不能被"平移 $j$"解释**：

| 实例 | 铅笔 | shape | rank | $\eta$ | $\varepsilon$ | 有限因子次数 |
|---|---|---|---|---|---|---|
| seed 1002（$(5b)$ ✗）| 原始 | $6\times6$ | 4 | $[0,0]$ | $[1,0]$ | $[0,0,0,3]$ |
| | 商 | $4\times5$ | 3 | $[1,0]$ | $[0]$ | $[0,0,2]$ |
| seed 1010（$(5b)$ ✓）| 原始 | $6\times6$ | 5 | $[0]$ | $[4]$ | 全零 |
| | 商 | $4\times4$ | 3 | $[3]$ | $[0]$ | 全零 |

**观察**：商化把**左指标搬成右指标**并改变次数（$\varepsilon=[4]$ 变成 $\eta=[3]$）。

**结论**：原始 → 商是**行空间的商/压缩**（把 $\mathcal J$ 部分删掉），**不是**严格等价、也不是幺模等价
⟹ 由专家 §5 的三分法，**Kronecker 不变量不能从层坐标搬回原始铅笔**。
所以结构陈述（TARGET_FORM_T 第 4 条）必须以**原始 $Q_L$** 为对象写。


### 4.7 可行样本扩到 101 个（$n=6,7,8$），右指标**全部为 $0$**

按专家 §4 的要求（"20–30 个可行铅笔、至少三个维度"），加了一个**构造性**的可行族：

> **可观性链**：$L_k=[C;CA;\dots;CA^{k-1}]$（$k=1..n$）。它**总是**满足 $(5b)$。
>
> *证明*：$\lambda L-LA$ 的行是 $\lambda CA^i-CA^{i+1}$，故行空间 $\subseteq\operatorname{row}(L;CA;C)$，给了 $\le h$；
> $\lambda\ne0$ 时它们与 $\{CA^i-\lambda^{-1}CA^{i+1}\}$ 同 span，可反解出 $CA^i$（$i<k$）⟹ 秩 $\ge\operatorname{rank}L$，
> 加上 $CA,C$ 得 $h$；$\lambda=0$ 时是 $-CA^{i+1}$ 加上 $CA,C$，span 也是 $h$ ⟹ 秩恒为 $h$ ✓。
> （**已证-纸面**；$n=6,7,8$ 上的 101 个实例是该族的精确验证。）

**统计**（[kron_sweep.py](../../tools/verification/kron_sweep.py)，数据 `data/sweep_n6|n7|n8_8seeds.tsv`）：

| 项 | 数值 |
|---|---|
| 合法铅笔总数 | 262 |
| **可行（$(5b)$ ✓）** | **101**（$n=6$: 45；$n=7$: 33；$n=8$: 23 左右）|
| 可行铅笔的 $(\rho,c)$ 分布 | $(0,1)$:57、$(0,2)$:17、$(1,2)$:10、$(4,2)$:6、$(2,2)$:5、$(3,2)$:2、$(5,2)$:2、$(3,1)$:1、$(4,1)$:1 |
| **可行且右指标含非零者** | **0** |

**结论**：在 101 个可行样本（$\rho$ 覆盖 $0..5$、$n\in\{6,7,8\}$）里，右最小指标**全部为 $0$**。

**这条已升级为定理**：$(5a)$（甚至不需要 $(5b)$）⟹ 右最小指标全为 $0$。
证明见 [proof/kron_null_module](../../proof/kron_null_module/README.md)（docs/02 B.6），**精确验证 150/150**。
证明要点：按 $\lambda$ 的幂展开，最高次系数 $v_d$ 满足 $Lv_d=CAv_d=Cv_d=0$，
由 $(5a')$ 得 $LAv_d=0$，故 $v_d$ 是常值零向量，再对次数归纳。


### 4.8 可行样本的 $d_\infty$ 与左指标（T4-b / T4-c 的现状）

脚本 [kron_dinfty_stats.py](../../tools/verification/kron_dinfty_stats.py)，**103 个**可行铅笔（$n=6,7,8$）：

| 检验 | 结果 |
|---|---|
| 恒等式 $\sum\eta+\sum\varepsilon+d_\infty=h$ | **103/103 ✓** |
| $d_\infty=0\iff\operatorname{rank}L=h$ | **103/103 ✓** |
| B.6（$\sum\eta=0$）| **103/103 ✓**（注：$d_\infty$ 按正确度量重算见 [proof/t4b_infinite_divisors](../../proof/t4b_infinite_divisors/README.md)）|

$d_\infty$ 的分布：$(\rho,c)=(0,1)$ 有 72 个（其中 9 个 $d_\infty=1$），其余组全部 $d_\infty=0$；
$(h,\operatorname{rank}L,d_\infty)$ 的组合只有 $\{(1,1,0),(2,2,0),(2,1,1),(6,6,0),(3,3,0),(4,4,0),(7,7,0)\}$
—— 即**全部满足 $d_\infty=h-\operatorname{rank}L$**。

**一般铅笔的界**：$d_\infty\ge h-\operatorname{rank}Q_1$（每个无穷初等因子至少贡献 1 次），
$Q_1=[L;0;0]$ 故 $\operatorname{rank}Q_1=\operatorname{rank}L$。样本里**取等** ⟹ 观测器铅笔的
**无穷部分全是 1 次因子**（在 $\infty$ 处没有 Jordan 块）。

**更正（专家 2026-11-02 §2）**：不能把 T4-b 写成"等价于 $\ker L=N$"。
由 B.6 有 $\dim N=n-h$，故 $\ker L=N\iff\operatorname{rank}L=h\iff d_\infty=0$——那是**特例**。
正确的是 $\dim(\ker L/N)=h-\operatorname{rank}L$，于是
$d_\infty=h-\operatorname{rank}L\iff d_\infty=\dim(\ker L/N)$。

**已升级为定理**（[proof/t4b_infinite_divisors](../../proof/t4b_infinite_divisors/README.md)，docs/02 B.7）：
$(5a)$（不需要 $(5b)$）⟹ 无穷初等因子全是 1 次。**精确验证 151/151**（$n=6..10$，含 43 个不可行）。
左指标的和在 $(5a)$ 下是 $\operatorname{rank}L-d_{\rm fin}$（**不是** $\operatorname{rank}L$），
只有再加 $(5b)$ 才等于 $\operatorname{rank}L$（[R21](../../proof/refuted/README.md)）。

**注意量**：$d_\infty$ 用反转铅笔不变因子在 $\mu=0$ 处的**阶**（$\mu$-adic 赋值）算，
不能用多项式总次数——后者会产生假的"反例"（[proof/refuted R20](../../proof/refuted/README.md)）。**更好的待证形式**（专家 §7.2）是反转铅笔 $\widehat Q(\mu)=Q_1+\mu Q_0$ 的链方程；
注意逐字的"$LAw\in\operatorname{im}L\Rightarrow LAw=0$"判据**不对**（行满秩 $L$ 时几乎自动成立，
那些链属于奇异部分）——见 [kron_t4b_prime.py](../../tools/verification/kron_t4b_prime.py) 的实测（59 个里 45 个"不成立"）。

## 5. 下一步

- 把 $\mathcal V$ 的族扩大（非 A-不变的、只满足 $(5a)$ 的、$\rho$ 更大的）；
- 用 [proof/layer_program/RESTRICTED_COMPLETION_MODEL.md](../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md) §5 的"目标形式 T"
  把观察到的型写成**关于不变量的不等式猜想**，再找反例或证明。

## 6. 文件

- [attempts/01_kronecker_structure.md](attempts/01_kronecker_structure.md)（§5.3 格式的开发日志）
- [data/](data/)（扫描输出）
