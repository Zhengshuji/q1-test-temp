# 论文 referee report 落实：两处硬错误与结构性修订

> 2026-11-10。86 号（referee report）结论：major revision；核心数学（Lemma A/B/C/D、
> Proposition 3c、编码）被逐条核对并认可，但**发现两处硬错误**（Kronecker 例子、
> $(GU)_iB$ 的维度）与若干记账/定位问题。本轮全部落实。
> 状态：**M3（专家复核）**。

## 目标

按 referee report 修订论文，使"定稿"名副其实：先修数学错误，再补他明确要求的结构。

## 设想与理由

report 自己把问题分成四层（数学正确 / 算法正确 / 复杂度正确 / 新颖性），并明确：

* **Part I 的第一项反对意见他自己撤回了**——他先认为 "(5a) ⟹ (5b) 自动"，随后核对
  Fernando 2026 的原始表述与 Theorem 4，承认缺的是**秩等式**而不是行包含，
  并写出 $\operatorname{rank}[M;B_0]=\operatorname{rank}B_0+\operatorname{rank}(MN)$。
  这条等于**独立复核了 Lemma A(iii)**；
* 其余是两处**硬错误** + 一串"要写清楚"的要求。

所以本轮不是重做数学，而是修错 + 补表述 + 存档。

## 做法

### 1. 两处硬错误

**(a) Kronecker 例子写错。** 原文举 $Q(\lambda)=\operatorname{diag}(1,1+\lambda)$ 作为
"有无穷初等因子但处处满列秩"的二维例子。这是错的：$\det Q=1+\lambda$ 在 $\lambda=-1$ 为零。
改为 $Q(\lambda)=I_2$ 与 $Q(\lambda)=\begin{bmatrix}1&\lambda\\0&1\end{bmatrix}$
（$\det\equiv1$），并明写"早前版本列的 $\operatorname{diag}(1,1+\lambda)$ 是错的，其行列式在 $-1$ 消失"。

**(b) $(GU)_iB$ 维度错。** §7 的自由行方程写成
$D[(X_iB)^{\mathsf T};((GU)_iB)^{\mathsf T}]=0$。但 $G$ 是 $q\times\omega$、$U$ 是
$\omega\times q$，故 $GU$ 是 $q\times q$，其第 $i$ 行是 $1\times q$，乘 $B$（$\omega\times k$）
无定义。改为 $(G_iB)$，并采用 report 的 **Repair A**：公式里不量化 $U$（只用
$e_\omega(X^{\mathsf T}X)>0$），$U$ 只在正确性证明中作为任意左逆出现。
于是变量数 $N=2q\omega+2\omega$ 与公式一致（原来公式用 $U$ 却没计入）。

### 2. 术语：$q1$ 与 $\mathrm{DEC}$ 分开

report 指出 "OPT 是函数问题，不是语言"，$q1\in\exists\mathbb R$ 不严谨。§2.1 新增
$\mathrm{MINDEC}(Q)=\bigvee_{q=r_0}^{Q}\mathrm{DEC}(q)$，并声明
"所有复杂度断言都指判定问题；'$q1\in\exists\mathbb R$' 一律读作 $\mathrm{DEC}(q)\in\exists\mathbb R$"。
Theorem 3 改成"对每个固定 $q$，$\mathrm{DEC}(q)\in\exists\mathbb R$；故 $\mathrm{MINDEC}(Q)\in\exists\mathbb R$"，
摘要、§1.2、Appendix B 同步。

### 3. 他明确要求的结构性补充

| report 要求 | 落实 |
|---|---|
| 把秩恒等式写进 A.1 | §3 Lemma A 的证明里显式给出，并加"$\lambda H-H_A=(\lambda I-F)H$"解释 |
| $\omega=0$ 在 §8 单独指出 | §8 Case 2 末尾加指引（$\omega=0$ 走 §7.1，不用 Lemma D） |
| Cauchy–Binet 的**构造**步骤 | §6.3 新增"Algorithmic reading"四步 + 文献对照表 + 明确"恒等式古典、贡献是压缩" |
| 固定 $q$ 的记账表 | §7 新增数量表（$N$、charts、branches、$s$、$D$、$B$、构造规模），并写明 $t$ 计入 $s$ 不折进 $D$ |
| 矩形 $d$ 次推广 | Lemma 8.1 后加注：$\deg S\le2d\omega-d-1$ |
| 编码拆成 soundness / completeness | Appendix B 拆成两段独立论证，并强调 $UX=I$、$BV=I$ 非冗余 |
| 参数三层次（核商 / 行变换 / 谱不可见） | §10.2 写成三条，并采纳他的建议：**先做固定行约束后的有效秩**（不需谱商） |

## 进展

* 两处硬错误已修；术语已分；七项结构性补充已写入；
* 论文结构：Theorem 1（固定 $q$）、Theorem 2（固定 $\kappa_{\rm obs}$，Cor 2a）、
  Theorem 3（$\mathrm{DEC}(q)\in\exists\mathbb R$）、Corollary 4（组合上界），
  Proposition 3c（$r=0$）；
* 报告本身归档为 [86](../../../for_expert/archive/86_referee_report_paper.md)；
* **注意**：归档文本在 Part V（原创性）处**截断**，最后一句是 "This means the present
  manuscript must not …"。该段之后的要求（若有）未落实，需补发；
* 新增 / 改动的验证：本轮无新数学，c318/c319 仍然 PASS（公式改动只涉及 $U$ 的记账，
  与脚本无关）。

## 最终结论

* **Lemma A(iii) 获得独立复核**（report §2 撤回反对意见并给出同一秩恒等式）；
* 论文的两处硬错误已修，其余修订是表述与记账；
* report 的总体裁决是 **major revision**，其列出的大项（fixed-order 公式、编码、
  位长、参数最优性）中，前三项本轮已闭合，**参数最优性仍是开放研究问题**（不是论文缺陷）。

## 补充：完整版报告（Part V–IX）新增部分的落实

报告后来补全（2072 行），新增 Part V（原创性）、VI（18 条修订清单）、VII（五条研究路线）、
VIII（文献）、IX（总结）。其中属"修订"而非"研究"的部分本轮一并落实：

| 报告条目 | 落实 |
|---|---|
| 16.4 与 Fernando 的分工表 | §1.4 新增对照表（并注明"只针对所引两篇，不是穷尽声明"） |
| §17 清单 8：$e_j$ 的表示 | §7 新增"三项表示细节"第 3 条（用 $\det(zI+G)$ 的系数，分数自由消元） |
| §17 清单 9：严格不等式 | 同节第 1 条（$f>0$ 写成 $\exists u:fu^2=1$，每分支 $O(1)$ 个） |
| §17 清单 10：析取的处理 | 同节第 2 条（逐分支求解、时间相加；$t$ 不入 $D$） |
| §17 清单 16：参数不变性 | §4 Lemma B 加"基变换 $N\to NQ$ 不改变 $d_0$" |
| §17 清单 17：一个构造性例子 | §4 加循环移位例子（$n=4$，$k=2$，$d_0=3$，$\kappa_{\rm obs}=3$，公式 $3+2\omega$ 个变量） |
| §17 清单 18：$f(\kappa)$ 的大小 | §10.2 末段（$f\approx\kappa^{O(\kappa)}$，定理是结构性的，不是可运行算法） |
| §24：文献 | 新增 Fabiano–Struppa 1990（左逆次数界）、Emiris–Mourrain 1999、Darouach–Fernando 2025；2026 两篇标为 **preprint** |
| §24：$\S8.1$ 的次数界归属 | §8.1 注明左逆次数界有经典文献 [Fabiano–Struppa 1990]，本文用的是初等伴随–Bézout 界 |

未做（有意）：§18 要求把全文重排成"压缩 → 证书 → FPT → 固定 $q$ → $r=0$ → $\exists\mathbb R$"的顺序。
现在是 §7 固定 $q$、§8 FPT、§8.1 $r=0$、§9 $\exists\mathbb R$；§1.2 已写明"第二个算法是主要贡献"。
重排会再次打乱全部编号，收益是叙事顺序，风险是引入引用错误，故留给下一稿统一处理。

## 放弃原因

不适用（本轮无失败路线）。明确**不做**的是 report §10.3/§19 的参数最优性研究：
那是一条新的研究线（谱商 / 有效秩），不属于本次修订范围，已写进 §10.2 作为下一步。

## 最终结论（补）

* 报告的最终裁决是 **major revision**，但明确"不要放弃这个项目"：五条结果（压缩、固定 $q$、
  FPT、$r=0$、$\exists\mathbb R$）都被认可，前提是修掉编码与术语、补足记账；
* 它给出的**投稿前唯一建议补做**的理论结果，是"参数能否被观测器行对称性商小"（§28）；
  这正是 §10.2 的第 2、3 层，也是下一步研究线的入口；
* 报告同时给出五条研究路线（A 改进参数、B 绕开实代数几何、C 是否 $q1\in\mathrm P$、
  D 受限硬度、E 一般 $d$ 次左逆界），本轮只把 E 的 $d$ 次界写进论文，其余记为路线。

## 残留价值

* 一份逐条对应的裁决表，可再送同一 refereee 复查；
* 修正后的 $U$ 记账让 Theorem 1 的变量数与公式真正一致；
* "秩恒等式 + $(\lambda I-F)H$" 的解释让 Lemma A 独立可读。

## 相关文件

* [86 报告](../../../for_expert/archive/86_referee_report_paper.md)
* [论文](../../../../trash/paper_root_2026-11-21/q1_parametric_algorithms.md) §2.1、§3、§6.3、§7、§8、§8.1、§10.2、Appendix B
* [REVIEW_NOTES](../../../../trash/paper_root_2026-11-21/REVIEW_NOTES.md)
* [STATUS](../../../../STATUS.md)

## 专家复核意见（裁决）

| 86 号（referee）结论 | 落实 |
|---|---|
| Part I 的反对意见**撤回**：$(5b)$ 经秩恒等式化到常秩铅笔，Lemma A(iii) 正确 | 论文 §3 已显式给出该恒等式与解释；无需改数学 |
| 硬错误 1：$\operatorname{diag}(1,1+\lambda)$ 不是处处满列秩 | 已改为 $I_2$ 与 $\begin{bmatrix}1&\lambda\\0&1\end{bmatrix}$，并注明旧例错误 |
| 硬错误 2：$(GU)_iB$ 维度无定义、$U$ 未计入变量 | 改为 $(G_iB)$，$U$ 只在证明中出现；变量数一致 |
| 术语：$q1$ vs $\mathrm{DEC}$/$\mathrm{OPT}$ | 新增 $\mathrm{MINDEC}(Q)$，全部断言改为判定问题 |
| Lemma D1 正确；矩形次数界正确（$2\omega-2$） | 保留，并加 $d$ 次推广注 |
| Proposition 3c 正确，且是"存在性 → 有限证书 → 小线性系统"的好例子 | 保留，§8.2 见证说明保留 |
| 编码：两方向都对，数据约束必需 | 拆成 soundness/completeness，并强调 $UX=I$、$BV=I$ |
| Cauchy–Binet 恒等式古典；贡献是压缩 | §6.3 改写 + 算法四步 + 文献表 |
| 固定 $q$：$t$ 不计入 $D$，要写构造规模 | §7 数量表 + "construction size $k^{O(q^2)}$" |
| 参数 $\kappa_{\rm obs}$：自然但未证最优；建议先做有效秩 | §10.2 三层写清，并注明先做固定行约束后的有效秩 |
| major revision，不建议按当前版本投 | 本轮修订后可再送；剩余开放项是参数最优性（研究线，非缺陷） |
