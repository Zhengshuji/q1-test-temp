# 85 号裁决落实：$r=0$ 的精确铅笔测试（有限线性系统）

> 2026-11-10。85 号对 $r=0$ 送审件的裁决：报告指出的缺口**成立**，但缺口可以**直接补上**——
> 次数界 $\deg S\le2\omega-2$ 已把"$\forall\lambda$ 的秩条件"变成有限个线性方程。
> 状态：**M3（专家裁决）+ 精确验证 c318**。

## 目标

把 85 号的裁决落实到论文、台账与 STATUS：证明 $r=0$ 的判定是**确定性多项式时间**，
而不是"未审计比特代价的 Kronecker 算法"；同时修正报告里关于 Kronecker 型的过强表述。

## 设想与理由

85 号把三件事分开：

1. 代数刻画：$Q(\lambda)=\lambda X-G$ 在 $\mathbb C$ 上处处满列秩；
2. 多项式尺寸证书：条件成立时存在 $\deg S\le2\omega-2$ 的多项式左逆；
3. 高效精确判定：以 $q,\omega$ 为输入、确定性多项式比特时间。

报告只做到 (1)(2)，把 (3) 寄托在"标准 Kronecker/阶梯算法"上。85 号指出：
数值线性代数的 Kronecker 算法**不自动**给出有理比特界；(3) 需要单独算法。

关键观察（85 号 §1.2）：若 $S(\lambda)=\sum_{j=0}^{2\omega-2}S_j\lambda^j$ 且
$S(\lambda)(\lambda X-G)=I_\omega$，按 $\lambda$ 的幂比较系数得

$$
-S_0G=I_\omega,\qquad S_{j-1}X-S_jG=0\ (1\le j\le2\omega-2),\qquad S_{2\omega-2}X=0 .
$$

未知量是 $S_j$ 的**条目**，$X,G$ 是固定输入 ⟹ 这是普通的有理线性系统，相容性可精确判定。
极大子式枚举（$\binom q\omega$ 个）只用于**证明存在性**，不进算法。

另一条更正（85 号 §4）：报告写"Kronecker 型既无右奇异块也无正则块"是**过强**的。
$Q(\lambda)=1$ 是正则铅笔、带一个无穷初等因子，但它在每个有限 $\lambda$ 秩为 1。
正确表述是：**右奇异块**与**有限正则初等因子块**必须缺席；左奇异块与**无穷**初等因子允许。

## 做法

### 1. 先机器核验，再改文档（纪律 §20 / §21）

新建 [c318](../../../../tools/verification/c318_r0_linear_system.py)，用两套**独立**精确判据互相对照：

* (a) 全部 $\omega\times\omega$ 极大子式的 gcd 是否为非零常数（参考判据，枚举 $\binom q\omega$）；
* (b) 线性系统 (R0) 的相容性（先通分，再用 sympy 有理消元比较 $\operatorname{rank}M$ 与 $\operatorname{rank}[M\mid b]$）。

覆盖：

* 135 个随机满列秩铅笔（$(q,\omega)=(3,1),(4,2),(5,2),(6,3),(8,3)$）；
* 共根反例 $G=\lambda_0X$（$\lambda_0=0,2,-3$）——两判据都必须拒绝；
* $Q=1$（85 号的无穷初等因子例子）、常值满列秩、零铅笔；
* **薄集构造**（纪律 §12：稀有集不许采样）：奇异 $X$、$\det(\lambda X-G)$ 为常数，
  最小证书次数为 $1>0$ ⟹ $d=0$ 会误拒，$d=2\omega-2$ 正确；
* 端到端：随机 $(A,C,L_0)$、$r=0$，取 $N$ 为 $\ker[C;CA]$ 的基，
  $H=L_0N$、$H_A=L_0AN$，在 $(5a)$ 成立时秩分解 $H=XB$、$H_A=GB$，压成 $(X,G)$，
  与项目参考实现 `spectral_gcd`（在 $(A,C,L_0)$ 层算全铅笔极大子式 gcd）对照。

同时断言 85 号的计数：未知量 $(2\omega-1)q\omega$、方程 $2\omega^3$。

### 2. 脚本自身暴露的一个 bug（保留为教训）

端到端第 26 例误报不一致。原因：`int()` 把有理条目**截断**成整数，系统被静默改写成别的实例。
修法：先把 $(X,G)$ 通分到整数（整体乘非零有理数不改变 $\operatorname{rank}(\lambda X-G)$，
也不改变 (R0) 的相容性），再构造整数系统。
——这正是"证书必须先断言不变量"的价值：整数实例段全部通过，反而只有有理段暴露问题。

### 3. 论文改动

| 位置 | 改动 |
|---|---|
| 摘要 | FPT 对所有 $r\ge0$；$r=0$ 另有确定性多项式判定 |
| §1.2 | 新增贡献 4（zero-free-row），原 4 改为 5 |
| §8 | Theorem 3 改为所有 $r\ge0$，证明分 Case 1 ($r=0$) / Case 2 ($r\ge1$) |
| §8.1（新）| Lemma 8.1（五条等价）+ 尺寸/比特复杂度 + "存在性 vs 算法"备注 + Proposition 3c（算法与正确性）+ 更正后的 Kronecker 读法 + 见证 + Lean 状态 |
| §9 | Theorem 4 改为所有 $r\ge0$ |
| §10.1 | $r=0$ 由"开放义务"改为"已解决，仅剩常数审计" |
| A.5 | $r=0$ 不再由该计数覆盖，改指 Prop 3c |
| A.5.1 | 重写：矩形伴随构造的细节（$E_I$、$\operatorname{adj}(Q_I)E_IQ=f_II_\omega$）+ $(5a)$ 先行 + 不用 Kronecker |
| 附录 C | 增加 c318 的记录 |

### 4. 台账同步

* [CLAIMS](../../../../trash/paper_root_2026-11-21/CLAIMS.md)：新增 Lemma G（铅笔测试），F/3/4 改为全 $r\ge0$；
* [FREEZE_CHECKLIST](../../../../trash/paper_root_2026-11-21/FREEZE_CHECKLIST.md)：新增 Prop 3c 与 Lemma G，勾选项与开放项 5 改写，参考文献加 Beelen–Van Dooren；
* [LEAN_MAP](../../../../archive/paper_drafts/LEAN_MAP_2026-11-25.md)：Lemma G 记为 paper-only 缺口（Mathlib 无多项式矩阵 Bézout）；
* [verification_log](../../../../trash/paper_root_2026-11-21/verification_log.md)、[STATUS](../../../../STATUS.md)、[ATTEMPTS](../../../../ATTEMPTS.md) 同步。

## 进展

`c318` PASS，输出：

```
[1] gcd test vs linear system: 135 random pencils agree
[2] omega=1, q=3: 2 equations (=2 omega^3), 3 unknowns (=(2 omega-1) q omega)
[2] omega=2, q=4: 16 equations, 24 unknowns
[2] omega=3, q=6: 54 equations, 90 unknowns
[3a] common-root controls (lam0 = 0, 2, -3): both tests reject
[3b] Q(lam) = 1 (q = omega = 1) accepted by both tests
[3c] constant full-column-rank pencil accepted
[3d] zero pencil rejected (rank 0 < omega)
[4] minimal certificate degree on 24 random feasible pencils: max=0
[4b] thin constructed pencils: minimal degree 1 > 0
[5] end to end: 51 r=0 compressions, 29 satisfy (5a), 29 agree with spectral_gcd
```

论文、台账、STATUS 已按上表改完；四道门与提交见下。

## 最终结论

* **$r=0$ 分支已解决**：$M3$（专家 85 号）+ 精确验证 c318。
  Theorem 3 现在对所有 $r\ge0$ 成立；参数取 $0$ 时退化为 $\operatorname{poly}(\mathcal L)$。
* 算法不需要精确 Kronecker/Smith，也不枚举极大子式；返回显式见证 $S(\lambda)$。
* Kronecker 表述已更正（只排除右奇异块与**有限**正则初等因子块）。
* 剩余义务（不阻塞）：$r\ge1$ 的系数尺寸界常数；§8.1 比特界的逐行审计
  （标准 Hadamard/消元界，未逐项复核）；固定 $q$ 的常数与图卡记账。

## 放弃原因

不适用（本轮无失败路线）。被放弃的只是**旧路线**"用精确 Kronecker 算法判定 $r=0$"：
85 号指出它既不必要，也不足以给出比特复杂度。

## 残留价值

* 一个可复用的精确判据实现（c318），含反例对照与薄集构造；
* 论文 §8.1 自包含：证明、计数、比特界、见证、Kronecker 更正；
* 一条工程教训：`int()` 截断有理条目会把实例静默换掉——证书必须先用有理实例自检。

## 相关文件

* [85 答复](../../../for_expert/archive/85_r0_exact_kronecker-answer.md)（已归档）
* [85 送审件](../../../for_expert/archive/85_r0_exact_kronecker.md)（已归档）
* [论文](../../../../trash/paper_root_2026-11-21/q1_parametric_algorithms.md) §8、§8.1、§9、§10.1、A.5、A.5.1、附录 C
* [c318](../../../../tools/verification/c318_r0_linear_system.py)
* [CLAIMS](../../../../trash/paper_root_2026-11-21/CLAIMS.md) · [FREEZE_CHECKLIST](../../../../trash/paper_root_2026-11-21/FREEZE_CHECKLIST.md) · [LEAN_MAP](../../../../archive/paper_drafts/LEAN_MAP_2026-11-25.md)
* [STATUS](../../../../STATUS.md)

## 专家复核意见（裁决）

| 85 号结论 | 落实位置 |
|---|---|
| (1) $r=0$ 有确定性多项式算法：系数线性系统，$O(q\omega^2)$ 未知量、$2\omega^3$ 方程 | 论文 §8.1 Lemma 8.1 + Prop 3c；c318 |
| (2) 不需要精确 Kronecker 算法；数值算法不足以给出比特界 | 论文删去 Kronecker 路线，仅在读法处引用 [Beelen–Van Dooren 1988] 作背景 |
| (3) "无右奇异块且**无正则块**"过强；应只排除有限正则初等因子 | 论文 §8.1 "Kronecker reading (corrected)" 与 A.5.1，含 $Q(\lambda)=1$ 反例 |
| (4) Theorem 3 去掉 $r\ge1$，证明分两情形 | 论文 §8 Theorem 3 + Case 1/2；§9 Theorem 4 |
| (5) 更新状态报告：$r=0$ 不再是开放点 | STATUS §0/1.1/3/6/7、CLAIMS、FREEZE_CHECKLIST |
| (6) 仍缺：$r\ge1$ 的系数尺寸界与全局比特审计 | FREEZE_CHECKLIST "Main open checks" 5；本轮未改变 |
| (7) 建议把关键方程放进正文而不是附录 | 论文 §8.1 正文给出 (R0)；A.5.1 只放证明细节 |

裁决记 **M3**（专家明确：缺口成立但可补，且给出补法）。
