# q=ω+1, ω=2：可达块分类与"同一 S 一好一坏"

> 2026-11-08。回应专家 48 号答复的实验 B/C（`workspace/for_expert/archive/48_block_criterion_and_status-answer.md`）。
> 工具：`tools/verification/q_omega_plus_1_w2.py`（纯 `Fraction`）。验证 ≠ 证明；定理陈述见文末"状态"。

## 目标

在 $q=\omega+1=3$、$\omega=2$ 这一格上做两件事：

1. **实验 B**：找"**同一个 Grassmann 点 $S$** 上既有好点又有坏点"的显式例子——专家称这是最有信息量的判决实验；
2. **下一交付物**：把可达的块对 $(A,B)$（等价地 $(A,w)$，$w$ 张成 $\ker B$）用 Grassmann 纤维表出来，
   判定 $\det[w,Aw]\ne0$ 能否达到，即给出 $q=\omega+1,\omega=2$ 的分类。

## 设想与理由

* 由块判据（B.24）：$\text{坏}\iff\exists0\ne y\in\ker B,\ Ay\parallel y$。$q=\omega+1$ 时 $B$ 是一行，
  $\ker B$ 是 $W$ 中的超平面；$\omega=2$ 时它是一条线 $\operatorname{span}\{w\}$，于是
  $$\text{好}\iff\det[w,Aw]\ne0.$$
* 谱行为只依赖 $(H,H_A)$；而 $(H,H_A)$ 由 $S$ 与兼容对 $(x_i,y_i)\in\mathcal C_S$ 决定。
  因此"同一 $S$ 一好一坏"等价于：**同一个 $S$ 的兼容纤维里，不同的 $y$ 给出不同的 $\det$**。
* 自由区（$\ker T=0$，即 $K\cap A^{-1}K=0$）有 $\mathcal C_S=S\times S$，$y$ 完全自由 ⟹ 最可能出现混合；
  约束区（$0<\dim\ker T\le k$）的 $y$ 被线性约束，可能整族全坏。
* 选两个实例：$n=9,p=3$（自由区，$K\cap AK=0$）与 $n=5,p=1$（约束区，$d=2$）。

## 做法

**实例 A（自由区）**：$n=9$、$p=3$、$q=3$、$r=1$。
$C=[I_3\ 0]$；$A$ 的列 $4,5,6=e_1,e_2,e_3$、列 $7,8,9=e_4,e_5,e_6$；$L_0=e_7^{\mathsf T}$。
则 $K=\langle e_7,e_8,e_9\rangle$、$k=3$、$K\cap AK=0$、$\ker T=0$、$U_0=L_0N_K=(1,0,0)$、$V_0=0$、$E=\langle e_1\rangle$。

取 $S=\langle e_1,e_2\rangle$（$K$-坐标），固定
$$H=\begin{pmatrix}1&0&0\\0&1&0\\0&1&0\end{pmatrix}\quad(\text{行 }E,\ w,\ w),\qquad w=e_2,$$
再取两个不同的 $H_A$：
$$H_A^{\rm good}=\begin{pmatrix}0&0&0\\1&1&0\\1&0&0\end{pmatrix}\ (y_1=e_1+w,\ y_2=e_1),\qquad
H_A^{\rm bad}=\begin{pmatrix}0&0&0\\0&1&0\\0&0&0\end{pmatrix}\ (y_1=w,\ y_2=0).$$
两者都满足 $\operatorname{rank}H=2$、$\ker H\subseteq\ker H_A$；回代
$R N_K=H_{2:3}$、$R A N_K=(H_A)_{2:3}$ 得显式 $L=[L_0;R]$，再跑 `consistency_checks` 的七条检查。

**实例 B（约束区）**：$n=5$、$p=1$、$q=3$、$r=1$。
$C=e_1^{\mathsf T}$；$A$ 的行 $1=e_5^{\mathsf T}$、列 $2=e_3$、列 $3=e_2$、列 $4=e_5$；$L_0=e_4^{\mathsf T}$。
则 $K=\langle e_2,e_3,e_4\rangle$、$k=3$，$\ker T$ 由 $(-e_3,e_2),(-e_2,e_3)$ 生成（$d=2$），$E=\langle e_4\rangle$。
Grassmann 判据给出两个 $S$（$\sigma=(1,\pm1,0)$）；兼容对由 $(x,y)$ 的线性关系参数化，扫 200 个可容许点。

## 进展

1. **实验 B 成功**（实例 A）：同一个 $H$（因而同一个 $S$、同一个 $\omega=2$ 层）上
   * good：2-子式 gcd 次数 $0$，$(5b)$ **成立**；回代 $L$ 的秩 $=3$，七条检查全过；
   * bad：gcd 次数 $1$（根 $\lambda=0$），$(5b)$ **失败**；回代 $L$ 的秩 $=3$，七条检查全过。
   $$\boxed{\text{谱行为不是 }S\text{ 的函数（甚至不是 }H\text{ 的函数，只差 }H_A\text{）}}$$
2. **约束区：测试点全坏**（实例 B）：两个 $S$ 上共 200 个可容许点（每个 100），gcd 次数全部 $\ge1$。
   这是**猜想**（整族全坏未证）；专家 49 号答复明确要求按不可约分量做函数域/坐标环证明，不能由采样推出。
   与 48 号报告的 scaling 论证一致（后者只覆盖 $k=2$ 的刚性情形）。
3. **点态判据的补空间无关性**：$\det[w,Aw]$ 本身依赖补空间 $W'$，但它的**零点性**不依赖——
   因为 $w\in\ker B$ 时 $Aw=Zw$，而 $\text{坏}\iff\exists w:Zw\parallel w$ 是内蕴的。
   这条澄清应写进论文（否则读者会误以为 $A$ 是典范矩阵）。
4. **$B=0$ 必须单列**（专家 49 号答复 §5.1）：$B=0$ 时 $\ker B=W$，坏自动成立
   （复 $2\times2$ 矩阵必有特征向量）；$\det[w,Aw]$ 只在 $B\ne0$ 时有效。
5. **分类表（机制层面）**：

| 机制 | 条件 | $q=3$ 判定 |
|---|---|---|
| 自由 | $\ker T=0$（如 $K\cap AK=0$）| 由 $\det[w,Aw]$ 决定；同一 $S$ 可混合（实例 A）|
| 中间/刚性 | $0<\dim\ker T\le k$ | 同一 $\det$ 检验；测试点全坏（实例 B，$d=2$；整族全坏为猜想）|
| 点态（任意可容许点）| $B\ne0$ 且 $w$ 张成 $\ker B$ | 坏 $\iff\det[w,Aw]=0$；$B=0$ 恒坏 |

## 最终结论

* 实验 B：**完成**——给出第一个显式"同一 $S$、同一 $H$、一好一坏"的例子（$n=9$ 自由区）。
* $q=\omega+1,\omega=2$ 的判定：化归为"逐 $S$ 解兼容纤维 + 点态 $\det[w,Aw]$ 检验"的**结构归约 + 判定策略**；
  自由区可混合、约束区测试点全坏（猜想）。**在"机制 + 判定策略"层面完成**；逐实例的闭式分类未给，
  且"逐分量取一点"不是算法（需函数域/坐标环检验——专家 49 号答复 §5.2）。
* 这不是 $q1$ 的答案：只是把专家指定的下一交付物做成了一个可执行判定 + 一个正例/反例对。

## 放弃原因

* **未做到**"所有实例的闭式判据"：一般 $k$、一般 $S$ 的纤维参数化仍依赖图卡枚举；
  本轮的完全性只到两个机制 + 一个判定程序。
* 中间区（$0<d<k$）只验证了 $n=5$ 的 200 个测试点全坏（整族全坏未证），**没有找到混合例子**（不排除存在）；

## 残留价值

* 显式同 $S$ 反例，可直接回答专家的 Experiment B；
* 可复用工具 `tools/verification/q_omega_plus_1_w2.py`（回代 + 七条检查 + gcd）；
* 补空间无关性说明、分类表，给 $k-\omega=1$ / 一般 $k$ 的下一步一个明确起点；
* 与 `proof/B.24/check_block_criterion.py`（738 例）互补：后者验判据，前者验"可达性"与混合性。

## 相关文件

* [tools/verification/q_omega_plus_1_w2.py](../../../../tools/verification/q_omega_plus_1_w2.py)
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（块判据、$q=\omega+1$ 判据、专家第二十二轮）
* [workspace/for_expert/archive/48_block_criterion_and_status-answer.md](../../../for_expert/archive/48_block_criterion_and_status-answer.md)
* [workspace/for_expert/archive/49_same_S_and_q_omega_plus_1-answer.md](../../../for_expert/archive/49_same_S_and_q_omega_plus_1-answer.md)
* [proof/B.24/check_block_criterion.py](../../../../proof/B.24/check_block_criterion.py)

## 状态

* 实验 A：**[精确验证]**（两条 $L$ 过七条一致性检查；good/bad 与 Toeplitz 一致）；
* 实验 B：**[精确验证：200 个测试点全坏]**（约束区；整族全坏是**猜想**，不构成证明）；
* 点态判据：**[已证]**（块判据一行，见 B.24）；
* 分类表：**兼容机制的归纳 + 判定策略**，不是所有实例的闭式可行性分类。

## 专家复核（49 号答复，2026-11-08）

* **实验 B：决定性**（"Experiment B is decisively answered"）。不需要再找"不同分量"的例子：
  自由区 $\mathcal C_S=S\times S$ 是线性的，施加满秩开条件后不可约，因此本例子已经是**同一个不可约纤维内**的混合，
  比"不同分量"版本更强。
* **II.3 降级**：点态代数正确，但"逐 $S$ 枚举 + 每个不可约分量取一点"**不是精确算法**——
  任意点可能落在零集里；正确做法是函数域/坐标环（或构造集）检验。专家建议把 II.3 称为
  **结构归约 + 判定策略**（structural reduction and proposed decision strategy）。
* **$B=0$ 单列**（见上 §5.1）；**约束例是猜想**：200 个测试点不能排除开稠密好集，需按分量做函数域证明。
* **RP 路线**：原则上成立，正确目标是 **RP，不是 ZPP**；需补：有理输入模型、例外集次数界
  （两个常系数组合的结式，总次数 $\le2k^2$）、有限网格采样与拒绝重采、Smith 形的位复杂度。
  fixed-$(q,\omega)$ 的措辞已够；变量维数的 RP 是单独的更强结果。
* **优先级**：A 完成 $k=\omega$ 的 RP 定理；B 自由区 $q=3,\omega=2$ 的充要判据
  （允许依赖 $(S,U_0,V_0,m)$，不要先假定只依赖 $U_0,V_0$）；C 证明/否定约束例的"整族全坏"。
