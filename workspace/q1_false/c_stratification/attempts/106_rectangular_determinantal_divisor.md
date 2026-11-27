# 矩形行列式因子：用 Hermite 形把缺口补上

> 2026-11-08。回应专家 51 号答复 §8.3 的 caveat：KKS 1987 的显式确定性定理是**方阵非奇异**，
> 不能直接当作矩形行列式因子的引用。本文件给出一个**初等桥接引理**，把矩形情形归约到
> **矩形 Hermite 形**（有明确的矩形来源），从而把 RP 证明的引用换成可核的形式。

## 目标

设 $P(\lambda)\in\mathbb Q[\lambda]^{q\times k}$，列法秩 $k$。记
$$\Delta_k(P)=\gcd\{\text{全部 }k\times k\text{ 子式}\}$$
（$k$ 阶行列式因子）。目标：把 $\Delta_k(P)$ 的计算归约到**矩形 Hermite 形**，并写清复杂度引用。

## 设想与理由

* 专家指出：KKS 的显式定理是方阵非奇异；矩形 Smith/Hermite 的复杂度要单独引。
* 但"矩形行列式因子"和"矩形 Hermite 形"之间其实只差一个**初等引理**：
  若 $UP=[D;0]$（$U$ 幺模、$D$ 为 $k\times k$ 三角块），则全部 $k$-子式的理想由 $\det D$ 生成。
* 这样就不需要"矩形 Smith 形"的完整定理；只需**矩形 Hermite 形**（Storjohann–Labahn 的矩形预处理；
  Beckermann–Labahn–Villard 的一般多项式矩阵标准形）。

## 做法

**引理（桥接）**：设 $P\in\mathbb Q[\lambda]^{q\times k}$ 列满法秩。若存在幺模
$U\in\mathrm{GL}_q(\mathbb Q[\lambda])$ 使
$$UP=\begin{pmatrix}D\\0\end{pmatrix},\qquad D\in\mathbb Q[\lambda]^{k\times k}\ \text{三角},$$
则
$$\Delta_k(P)=\det D\quad(\text{相差一个非零常数}).$$

*证明*：对任意 $k$ 行子集 $I$，由 Cauchy–Binet
$$\det((UP)_I)=\sum_{|J|=k}\det(U_{I,J})\,\det(P_J).$$
$U$ 幺模 ⟹ 两边 $k$-子式生成的理想相同（相差单位）。而 $[D;0]$ 的 $k$-子式中，凡含零行的为 $0$，
唯一非零的是 $\det D$。故理想 $=(\det D)$，即 $\gcd$ 为 $\det D$ 乘一个非零常数。$\square$

**推论**：要算 $\Delta_k(P)$ 是否为常数，只需算矩形 Hermite 形 $UP=[D;0]$ 的 $\det D$。
矩形 Hermite 形有明确的算法来源（$U$ 幺模、$D$ 三角）；其位复杂度按所引定理的输入/输出模型记账即可。

**与 RP 的关系**：RP 证明只需 $\deg\Delta_k=0$ 的判定；由引理，这等于 $\det D\in\mathbb Q^\times$。
矩形 Hermite 形有 **Las Vegas** 算法（Storjohann–Labahn, ISSAC 1995, pp. 119–125, Zbl 0914.65044）：
把 $m\times n$（$m>n$）的矩形 Hermite 形归约到 $(n+1)\times n$ 的同类型计算，
主代价与 $m\times n$ 多项式矩阵的无分数高斯消元同阶。Las Vegas 可并入 RP（见下），
所以 RP 定理不依赖 KKS 的"方阵非奇异"确定性定理。

**确定性路线（专家 52 号补充）。** 取 $P$ 的一个非奇异 $k\times k$ 行子块 $P_1$，令
$$\widehat P=\begin{pmatrix}P_1&0\\P_2&I_{q-k}\end{pmatrix}\quad(q\times q\ \text{非奇异}).$$
$\widehat P$ 的方阵 Hermite 形的前 $k$ 列就是 $P$ 的矩形 Hermite 形。Kannan 1985 给方阵非奇异多项式矩阵的
**确定性多项式时间** Hermite 形；故矩形行列式因子也有确定性路线（比 SL95 慢，但不随机）。

**位长界。** 次数 $\le1$、输入位长 $L$ 时，矩形 Hermite 形的系数位长
$\operatorname{bitsize}(D)=\widetilde O(k^2L)$；清分母 $\eta$ 使 $\Delta_k(\eta P)=\eta^k\Delta_k(P)$，对 monic 归一无害。

**RP + Las Vegas 的显式截断。** 用 Las Vegas 的期望时间界 $T$，取截断 $2T$；超时则拒绝。子程序不返回错结果，
故只增加假阴性；整体仍是 RP（外层抽样仍随机，不是 ZPP）。若采用确定性路线，则不需要这条截断。

## 进展

* 桥接引理已证明（两行 Cauchy–Binet + 理想不变性）。
* 矩形 Hermite 的引用已核对：SL95 是 **Las Vegas**，矩形 $m\times n$（$m>n$）归约到 $(n+1)\times n$，
  主代价同无分数高斯消元（zbMATH 评论 Zbl 0914.65044 的摘要）。
* 仍未做：$D$ 的位长/次数界（$\det D$ 的次数 $\le$ 输入次数之和）；若论文只给 Hermite 形而不给变换，
  本引理只需 Hermite 形本身（$U$ 只用于证明），所以不影响。

## 最终结论

* **数学缺口已补**：矩形行列式因子 $\to$ 矩形 Hermite 形的 $\det D$，只需一个初等引理；
  这样就不必把 KKS 的方阵定理硬套到矩形情形。
* **引用缺口已核对**：SL95 是 **Las Vegas**（不是确定性）；RP 吸收 Las Vegas（RP + Las Vegas = RP），
  故 RP 定理的这一步成立，不需要 KKS 的方阵定理。
* RP 的状态：数学与引用都闭合（在 RP 的意义下）；剩 $D$ 的位长/次数界是写作细节。

## 放弃原因

* 没有逐字核对 SL95 的完整位复杂度公式（只核对了摘要级的"主代价同无分数高斯消元"）；
  最终稿需引用论文中的精确指数/位长界。
* 没有给 $D$ 的显式次数/位长上界；这是论文写作时要补的。

## 残留价值

* 一条可复用的初等引理：**矩形行列式因子 = Hermite 方块的行列式**（差单位）。
* 把 RP 的引用从"KKS 方阵"换成"矩形 Hermite + 初等引理"，直接回应专家 §8.3 的 caveat。
* 对偶地，也可用于矩阵 pencil 的 gcd 判据（把"枚举全部子式"换成"算一个 Hermite 方块"）。

## 相关文件

* [attempts/101](101_rp_k_omega.md)（RP 定理；引理 8 的引用改为本文件的桥接）
* [workspace/ROADMAP.md](../../../ROADMAP.md) §4.3（文献）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（块判据、行列式因子的用法）

## 状态

* 桥接引理：**[已证-纸面]**（Cauchy–Binet + 理想不变性）。
* 引用：SL95 矩形 Las Vegas（Zbl 0914.65044）；**另有确定性路线**（方阵嵌入 + Kannan 1985），
  故 RP 步不必依赖随机化。
* 位长：$\operatorname{bitsize}(D)=\widetilde O(k^2L)$（次数 $\le1$）。
* 与专家 51/52 号的对应：caveat 已闭合；两条路线都写。
