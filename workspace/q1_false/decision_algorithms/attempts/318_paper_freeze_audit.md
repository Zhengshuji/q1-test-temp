# 论文冻结审计：剩余检查项逐条收口

> 2026-11-10。目标不是继续做数学，而是回答"论文还差什么、能不能现在冻结"。
> 结论：**数学上已无已知缺口（M2）**；冻结只剩机械通读 + 一次专家独立复核（M3）。
> 审计中新发现一个**真缺口**（Appendix B 的 $\exists\mathbb R$ 编码漏了输入数据约束）并已补上。

## 目标

把 [FREEZE_CHECKLIST](../../../../trash/paper_root_2026-11-21/FREEZE_CHECKLIST.md) 的 "Main open checks" 逐条落实，
并判断"论文是否已经可以完成/冻结"。

## 设想与理由

清单上剩下的条目分两类：

* **只是没写出来**（计数、行空间识别、Cauchy–Binet 推导）——写清楚即可，不需要新数学；
* **可能真缺**（$\exists\mathbb R$ 编码、边界情形）——需要逐句核对逻辑。

先按"每一条都当作可能真缺"的态度读，再决定哪些能当场关闭。事实上一半的"缺口"是
遗漏的句子，而不是错的数学；但确实有一条是错的结构（见下）。

## 做法

### 1. 逐条核对（结果见 §进展）

读了论文 §6（Lemma D）、§7（Theorem 2 的计数）、A.5（系数位长引理）、Appendix B（$\exists\mathbb R$ 编码），
对照清单：

* **固定 $q$ 的计数**：原文只写"monomial count $\le k^{O(q^2)}$"，没有把 Renegar 的
  $(sD)^{O(N)}$ 里的 $N,s,D$ 对应上来。补成显式：$N=2q\omega+2\omega\le2q^2+2q$、
  $s=O(k^2)$、$D=O(k)$，于是 $(sD)^{O(N)}=\operatorname{poly}(n)^{O(q^2)}=\mathcal L^{O(q^2)}$（$q$ 固定），
  图卡因子 $(q+1)k^q\le\mathcal L^{O(q)}$ 被吸收。
* **Gram 行空间**：原文一句带过"row space is exactly …"。补成 **Lemma D2** 并证明（含截断约定
  $c_{i,a}=0$ 在 $0\le a\le\omega$ 之外）。
* **Cauchy–Binet**：原文直接断言 $K=\sum_i f_if_i$。补成两步：对每个列集 $J$ 用一次 Cauchy–Binet，
  再对 $J$ 求和；并说明**计算代价**是 $\binom k\omega$ 个 $\omega\times\omega$ 行列式，
  而不是 $\binom q\omega\binom k\omega$ 个子式。随后 $(B^{\mathsf T}B)_{t,t'}=\sum_jS_{t-j,t'-j}$ 一行算出。
* **边界情形**：新增 §7.1（$k=0$、$\omega=0$、$q<r_0$、$r=0$）。
* **$\exists\mathbb R$ 编码**：**发现真缺口**。Appendix B 的编码只有
  $H=XB,\ H_A=GB,\ UX=I,\ BV=I,\ S(\lambda)(\lambda X-G)=I_\omega$——
  $H,H_A$ 完全由 $X,B,G$ 决定，**没有任何约束把它们和输入 $(A,C,L_0)$ 绑定**。
  按原稿，任意可行铅笔都能让公式为真，于是 $\mathrm{DEC}$ 被解成"存在某个可行对"，
  与输入无关。补上数据约束：
  \[
  X_iB=h_i^0,\quad G_iB=g_i^0\ (i\le r_0),\qquad
  D[(X_iB)^{\mathsf T};(G_iB)^{\mathsf T}]=0\ (i>r_0),
  \]
  其中 $h_i^0=(L_0N)_i$、$g_i^0=(L_0AN)_i$、$\ker D=\operatorname{row}[N\ AN]$；
  并补写两方向的正确性论证。变量数不变（$O(n^3)$）。

### 2. 机器核验（纪律 §20）

新建 [c319](../../../../tools/verification/c319_encoding_and_rowspace.py)：

1. Lemma D2 的实例：40 组随机多项式族，逐一核对"$B$ 的行组合 = $\sum g_if_i$ 的系数向量"；
2. 编码的**见证方向**：构造一个真可行实例——$(C,A)$ 可观测、$L_0=e_1^{\mathsf T}$、$L=I_n$
   （(5a)(5b) 都成立，$q=n$）——构造 $X,B,G,U,V,S$ 并逐条验证约束（含 (B.1)(B.2)、$S(\lambda)(\lambda X-G)=I$）；
3. **(B.1)(B.2) 的必要性**：把 $L_0$ 扰动一格，同一个见证仍满足所有"不含数据"的约束，
   但 $H\neq L_0'N$ ⟹ 数据约束不能省。

### 3. 过程中发现的第二个问题（项目记录层面）

原先 [consistency_checks.py](../../../../tools/verification/consistency_checks.py) 的测试数据里，
"公开例子 $q_0$ 的显式可行增广"那一行 $v$ **其实不可行**：
极大子式 gcd 是三次多项式（`spectral_gcd`），Toeplitz 判据也给 `five_b = False`，
新的左逆测试同样找不到证书。`check_candidate` 只断言"两个判据一致"，不断言可行，
所以它一直"通过"——这正是 §21 警告的"证书只查一致性、不查被检对象"。

已把 $v$ 作为 c319 的**负对照**记录下来（脚本里注明它被 gcd 判据拒绝），
但不改 `check_candidate` 的行为（它本来就只做一致性）。

## 进展

c319 PASS：

```
[1] Lemma D2: 40 random families: rows of B = coefficient vectors of sum g_i f_i with deg g_i < omega
[i] constructed instance: n=4, p=1, r0=1, q=4, (C,A) observable, L=I
[2] witness: omega=2, deg S<=2; H=XB, H_A=GB, UX=I, BV=I, S(lam)(lam X-G)=I verified
[2] data constraints: (B.1) on 1 fixed rows, (B.2) on 3 free rows (1 equations per row) verified
[3] with L0 perturbed, rows [0] of (B.1) fail while every other constraint still holds
[4] negative control: consistency_checks' 'feasible' L for the two-gap example is rejected by the gcd criterion
```

论文改动：§6.2（Lemma D2）、§6.3（Cauchy–Binet 两步推导 + 代价说明）、§7（显式计数）、
§7.1（边界情形）、Appendix B（数据约束 + 正确性）、附录 C（c319）。
清单改动：Main open checks 八条全部关闭；新增 "Remaining before freeze" 表。

## 最终结论

* **数学上已无已知缺口**：清单八条全部闭合，其中两条是本轮才真正补的（$\exists\mathbb R$ 编码、
  固定 $q$ 计数），一条是上轮 85 号补的（$r=0$），其余是写法问题。
* 论文处于 **M2**（纸面完整、无已知缺口）；到 **M3** 只差**一次独立复核**（专家读 Theorems 2–3 与 Appendix B）。
* **冻结（去掉 draft 横幅）不需要新数学**：一次机械通读（勾选 cross-reference 清单、重跑 Lean 与五道门）
  加一次专家读，即可。

## 放弃原因

不适用。本轮没有失败路线；唯一"放弃"的是"把 $\exists\mathbb R$ 编码当成已完整"的旧稿状态。

## 残留价值

* 一个只做一致性、不做可行性断言的测试脚本被识别出来（`consistency_checks` 的测试数据），
  并且它的"可行 L" 现在是 c319 的负对照；
* Lemma D2 与 Cauchy–Binet 的显式证明让 §6 可以独立阅读；
* 冻结清单从"五条模糊的开放项"变成"两条机械动作 + 一次专家读"。

## 剩余（冻结前）

1. cross-reference 清单逐项打勾（纯阅读）；
2. 重跑 `lake build` 与五道门（无 Lean 改动则不必重跑）；
3. 把论文（或至少 Theorems 2–3 + Appendix B）送专家读一次——这是 M2→M3 的唯一一步。

## 相关文件

* [论文](../../../../trash/paper_root_2026-11-21/q1_parametric_algorithms.md) §6、§7、§7.1、Appendix B、附录 C
* [FREEZE_CHECKLIST](../../../../trash/paper_root_2026-11-21/FREEZE_CHECKLIST.md) · [CLAIMS](../../../../trash/paper_root_2026-11-21/CLAIMS.md)
* [c319](../../../../tools/verification/c319_encoding_and_rowspace.py) · [c317](../../../../tools/verification/c317_cauchy_binet_random.py) · [c318](../../../../tools/verification/c318_r0_linear_system.py)
* [consistency_checks](../../../../tools/verification/consistency_checks.py)
