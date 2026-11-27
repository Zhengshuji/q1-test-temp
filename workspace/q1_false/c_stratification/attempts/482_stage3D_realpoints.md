> **已修正（483）**：3D 的正确目标是 $V(\mathbb R)\ne\varnothing$（原始设计允许实矩阵），
> $V(\mathbb Q)\ne\varnothing$ 只是**构造性证书**（更强但非必需）。
> 故本文末尾的二选一问题应改为 "$V(\mathbb C)\ne\varnothing$ 而 $V(\mathbb R)=\varnothing$"。见 [483](483_realpoint_certificate.md)。

# 482 阶段 3D：$V=\{D\ne0\}$ 是否含**实点/有理点**——可证书化的一半与不可得的另一半

> 承接 [481](481_pencil_gcd_and_specialization.md)（引理 B 是**开集级**结论）。本文件处理 3D：
> 从"开集"走到"实点"。结论是**一半可做、一半不可得**，并说明各自的原因。

## 目标

1. 精确写出 3D 问题；
2. 给出**可证书化**的正面路线（逐实例展示 $\mathbb Q$-点）；
3. 说明为什么**一般稠密性定理不可得**（两类障碍）；
4. 明确 3D 目前的状态，以及它对整条链的影响。

## 做法

把 3D 写成"开集是否含实/有理点"的存在性问题；然后分别给出可证书化的正面路线与两类不可得的一般障碍。

## 进展

（见下文两条路线与最终结论。）

## 设想与理由

3D 问题：给定不可约参数分支 $\mathcal B$、开集 $\mathcal B_R=\{\operatorname{rank}X_1=\omega\}\cap\mathcal B$、
以及清分母得到的 $D\in R\setminus\{0\}$，
$$V=\{D\ne0\}\cap\mathcal B_R\ \text{是否含 }\mathbb Q\text{-点（或 }\mathbb R\text{-点）？}$$

引理 B 只给"$V$ 上每点可行/不可行"，**不**保证 $V\ne\emptyset$ 含实点 ✗。

## 做法：两条路线

### 路线一（可行）：**逐实例证书**

**命题 (3D-cert).** 若在 $V$ 中能**显式给出**一个 $\mathbb Q$-点 $p$（即一组有理坐标使
$D(p)\ne0$、$\operatorname{rank}X_1(p)=\omega$、且 $\deg_\lambda\gcd_J f_J(p)=0$），则层可行，且**见证可构造**。

*理由.* 481 的单点判据 + (FW) 的充分性 ⟹ 该点给出显式 $\mathcal U$，进而显式自由行 ✓。

**这类证书已有先例**：最小模型（$k=2$、$\omega=1$、$U=0$、$N=I_2$、$A=\operatorname{diag}(1,2)$）里
$X=0$ 是有理点、$D\ne0$、且层可行（[468](../../decision_algorithms/attempts/468_three_levels_and_minimal_example.md) 精确验证）✓
——即 3D 在该实例上**成立且可证**（靠展示点，不靠稠密性）。

### 路线二（不可得）：**一般稠密性定理**

两类障碍，都说明"不能靠一般定理"：

1. **一般 $\mathbb Q$-簇的障碍**：不可约 $\mathbb Q$-簇即使在光滑 $\mathbb Q$-点上，$\mathbb Q$-点也**未必稠密**
   （例：秩为 $0$ 的椭圆曲线只有有限个 $\mathbb Q$-点）✗；
2. **线性原像的障碍**（本项目已踩过）：即使底簇是确定性簇（其 $\mathbb R$-点稠密 ✓），
   **线性原像也不保稠密**：$\Phi(x,y)=\begin{pmatrix}x&-y\\y&x\end{pmatrix}$ 线性、$\det\Phi=x^2+y^2$，
   原像 $V(x^2+y^2)$ 的实点只有原点（[472](../../decision_algorithms/attempts/472_linear_preimage_fails.md)）✗。

而我们的 $\mathcal B$ 恰是**线性截面**（Grassmannian 卡坐标 $X,Y$ 上的线性/秩条件），
所以在"一般定理"层面**没有可用的稠密性** ✗。

### 唯一还有希望的缝：$D_I$ 的**特殊**结构

可用的不是"确定性子簇 + 线性原像"这一层，而是更细的结构：$D_I(X)=C(X)B_0$，其两行是**同一泛函** $\ell$
作用在 $N$ 与 $AN$ 上（[473](../../decision_algorithms/attempts/473_three_steps.md) 第一步），子式是 $\ell$ 的二次型（[474](474_minors_identities.md)）。
**这条缝是否足够——目前没有任何结论** ✗。

## 最终结论

1. **3D 的可行性一半在"证书"**：只要能展示一个 $\mathbb Q$-点，层可行即可**构造性**确认（路线一）；
2. **3D 的普适性一半不可得**：一般 $\mathbb Q$-簇 + 线性原像都破坏稠密性，故"每层都含实点"**无一般定理** ✗；
3. 因此中间层算法的**正确表述**是：
   $$\text{给定 }W\ \text{与 }t:\ \text{在 }V\ \text{中找到有理点} \Longrightarrow \text{可行（可构造）};\qquad
   V\ne\emptyset\ \text{但有理解缺失时——未定}$$
4. 这也把 481 的"开集级"结论的意义钉死：它是**充分条件**（开集非空且含点 ⟹ 可行），
   **不是**"整个分支可行"的判定 ✗；
5. **对 $q1$ 的影响**：中间层路线目前为止给出的是**精确的有限维子空间刻画 + 构造性充分条件**，
   还**不是**完整判定算法，更不是复杂度结论 ✗。

## 放弃原因

- 没有判定"$V$ 是否有理点为空"（这本身就是一个实/有理点存在性问题，没有一般算法）；
- 没有利用 $D_I$ 的特殊结构去证稠密性（只指出了这条缝存在）；
- 没有把"$V$ 空"与"层不可行"分开处理（前者是充分条件的失效，不是不可行的证明）。

## 残留价值

- **3D 的精确形态**与两条路线的分界（证书 vs 一般定理）；
- **两类障碍的明确记录**（一般 $\mathbb Q$-簇；线性原像，附本项目反例）；
- 整条中间层链的**诚实终点**：精确刻画 + 构造性充分条件，判定算法与复杂度均未闭合。

## 下一步（若继续）

把 $D_I$ 的特殊结构（同一泛函 $\ell$、子式为 $\ell$ 的二次型）与 3D 结合：问"是否存在实例使
$V(\mathbb Q)=\emptyset$ 而 $V(\mathbb C)\ne\emptyset$"。若有，它是 A2 不可消的最终证据；
若搜不到且能证"$V(\mathbb Q)\ne\emptyset$ 在结构上必然"，则 3D 也能闭合。

## 相关文件

- [481](481_pencil_gcd_and_specialization.md)（开集级结论）
- [480](480_grassmann_parameterization_of_FW.md)（3A/3B）
- [479](479_fixed_W_with_row_budget.md)（(FW)）
- [472](../../decision_algorithms/attempts/472_linear_preimage_fails.md)（线性原像反例）
- [468](../../decision_algorithms/attempts/468_three_levels_and_minimal_example.md)（最小模型的有理点见证）

## 状态

- 3D 证书路线：**[已写]**，且最小模型上有先例 ✓。
- 3D 一般稠密性：**[不可得]**（两类障碍）。
- 3D 整体：**[开放]**。
- 阶段 3 整体：3A/3B/3C 已证；3D 开放；3E（复杂度）未做。
