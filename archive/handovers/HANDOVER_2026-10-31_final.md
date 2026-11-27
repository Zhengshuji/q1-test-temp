# HANDOVER —— 接手先读这一份

> 生成日期：2026-10-30。作者：上一任（AI 会话）。
> 本文件是**交接说明**，不是研究记录。研究记录的权威入口是 §「阅读顺序」里的那几份。
> 说明：CLAUDE.md §2 规定根目录只放 5 个 md；本文件是**经用户明确要求**放在根目录的，
> 已在 `tools/hygiene/audit_layout.py` 的 `ROOT_MD` 里登记为例外。

> ⚠️ **后续接手者的复核（2026-10-30）**：[archive/handovers/HANDOVER2_2026-10-30.md](archive/handovers/HANDOVER2_2026-10-30.md)
> —— 含 10 个待确认的疑问，以及一条更正：`STATUS` §12.1b 引用的 §82"可审计证书"脚本**实际有 bug**
> （`lift` 被 `% 1` 清零），**结论仍对**，但证明应换成 λ=0 的一行（见该文件 §3）。读本文件时请一并看那一份。

---

## 0. 一句话现状（**2026-10-30 定位更新**）

$$\boxed{\ q1\ \textbf{仍开放};\qquad \text{但 }q_{\min}\ \text{的\textbf{刻画}已由 Fernando 2026 两篇完成（[P1] 2609.33615、[P2] 2609.37992）};\qquad \text{唯一剩下的靶子 = 复杂度}\ }$$

- 文献的刻画：阶谱 $\Sigma_{FO}\subseteq[q_0,n_0-p]$、每阶充要（P2 Thm 5 的 $\exists Z$ = 本项目的 $\exists(\mathcal U,\mathcal H)$）、
  $\nu_{\min}=\min\Sigma_{FO}$、构造；$q_0=\sum_j\eta_j$ 多项式。对照见
  [literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md](literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md)。
- 本项目的旧结果（$\rho_{ci}$、层分解、格判据、$\tau$ 消除）一律**降级为对接/重新发现**，写作时引用 P1/P2。
- **唯一开放**：$\exists\Theta$（图卡 × 半代数）的判定复杂度 = $q1$。

---

## 1. 这个项目在做什么

**MIN-ROWS / q1**：给定 $(A,C,L_0)$（$A\in\mathbb C^{n\times n}$、$C$ 为 $p\times n$、$L_0$ 为若干固定行），
求最小行数 $q$，使存在 $R$（$q-|L_0|$ 行）令 $\mathcal L=[L_0;R]$ 满足

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \ \forall\lambda.$$

$q1$ 问：计算 $q_{\min}$ 是否 NP-hard？**仍开放。**

记 $\mathcal J=\operatorname{row}[C;CA]$、$j=|\mathcal J|$、$X=\mathbb C^n/\mathcal J$、$B=\pi(\mathcal JA)$、
$d=\dim X$。层号 $q=\rho+c$，其中 $\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$。

---

## 2. 现在到哪了（三张表）

### 2.1 站得住 ✓

| 成果 | 等级 | 位置 |
|---|---|---|
| $P(A,B,S)$ 递归定理 + $O(n^4)$ 算法（算术侧 $\rho_{ci}=P(T,B,U_0)$）| 已证 + Lean | `proof/p_is_polynomial/` |
| 下界 $q\ge\max(r+\varepsilon,\rho+\max(c_0,1))$ | 已证 | `proof/lower_bound/` |
| 顶层判据（$\rho=d$ 时可观测性）| 已证 + 65/65 | `proof/top_layer_observability/` |
| $\rho=0$ 层：$(5b)$ 自动 | 已证 | `proof/rho0_layer/` |
| **格子级五条判据 C.1–C.5**（固定 $(\mathcal U,\mathcal H)$ 时层是否可行）| 已证 + 多重验证 | `proof/layer_31_theorems/theorem.md` |
| **覆盖判据的权威表述**（行/列约定、基无关 30/30）| 已证 | `proof/layer_31_theorems/criterion.md` |
| **$d=4$ 的充要分类**（四条引理 + 定理 6.1）| 已证 + 60/60 + 40/40 | `proof/layer_31_theorems/d4_classification.md` |
| **T11**（$\gcd=1\Rightarrow$ 存在 $D_0\le2d(m-1)$ 行满秩）| 已证 + 195/195 | `proof/rho1_layer/theorem.md` §27 |
| $(N)$ = 经典条件不变性 | 已证 + 28/28 | RCP §36 |
| **秩屏障**：层可行 $\Rightarrow\rho\le\min_\lambda r(\lambda)$；$\min_\lambda r<\rho_{ci}\Rightarrow$ 无解 | 已证-纸面 + 1484+113 | `proof/rank_barrier/`、docs/02 §F |
| Lean：12 个模块，32 条声明，全部 `lean` 退出码 0 | Lean | `tools/lean/` |

### 2.2 已推翻（**有证书，禁止正面引用**）

| 命题 | 说明 |
|---|---|
| 四个 $q_{\min}$ 闭式 | `proof/refuted/`（R1–R4）|
| S1 充要判据 $\dim K\ge\rho$ | `proof/refuted/S1_criterion_iff.md` |
| "可控性"刻画 $(5b)$ | `proof/controllability_equivalence/` §8 |
| 引理 37.1（可对角化 ⟹ 全坏）、定理 37.2 | RCP §44（撤回）|
| **专家 QA6 §5 的"二分猜想"** | **`proof/refuted/README.md` 的 R12** —— 见 §3 |

完整撤回清单：RCP §44。**共约 15 条**，每条都有反例或崩点。

### 2.3 开放 ✗

| 问题 | 说明 |
|---|---|
| **$q1$** | **DEC-$\Theta$**（= P2 的 Thm 5/6，图卡表述）与 **$\mathrm{DEC}(q)$**（chart-free 的 $Z$-表述）是同一判定问题。多项式 ⟹ $q1$ 假；$\exists\mathbb R$-hard ⟹ $q1$ 强 hard。**上界已得**：$\mathrm{DEC}(q)\in\exists\mathbb R$（[proof/dec_q_existsR/](../../trash/README.md)，2026-10-31）；**下界/多项式算法仍未知**。 |
| **$d=4$ 的谱步** | 2026-10-30 已推进：$\dim B=1$ 时可行 $\varphi$ **至多 2 个**（转移映射），批量 12 例全部落定；仅"二次域候选"未实现 ✗ | `proof/layer_program/SPECTRAL_STEP_DESIGN.md` |
| **EDCI**（定维数条件不变子空间存在性）| 只表述清楚，**未解**；见 `proof/layer_31_theorems/edci.md` |
| 层级别判定 | 无定理（只有格子级 + 若干区域）|

---

## 3. 最近一次重大进展（2026-10-30）：二分猜想的反例

专家在 QA6 提议：**每个结构可允许的 $(3,1)$ 层，要么没有 $\mu\ge1$ 的可允许格子，要么存在未被覆盖的格子。**

**这个猜想是假的。** 反例：

$$
n=6,\quad
A=\begin{pmatrix}-1&0&2&1&-1&-1\\0&2&0&0&0&0\\0&0&0&0&0&0\\-2&-1&4&2&-2&-2\\-2&0&4&2&-2&-2\\0&-2&0&0&0&0\end{pmatrix},\quad
C_0=\begin{pmatrix}2&1&-2&2&-1&-1\\2&2&2&1&-1&1\end{pmatrix},\quad
L_0=[1,0,0,0,0,0].
$$

- $j=3$、$d=3$ ⟹ 3 维 $\mathcal U$ **唯一**（$=X$）；
- $\dim B=1$ ⟹ $\mu=1$ ⟹ **P2 = YES**；
- **证书（三行，2026-10-30 修正版）**：$\operatorname{rank}(A)=2$ 且 $\dim\pi(XA)=1$ ⟹ 对**任意** 4 行 $\mathcal L$
  $$\operatorname{rank}[-\mathcal LA;CA;C]\le j+\dim\pi(XA)=4<6=r_0$$
  ⟹ $(5b)$ 在 $\lambda=0$ 处必失败 ⟹ **层不可行** ✓（与 $\mathcal U$、截面、提升全都无关 ✓）。

$$\boxed{\ \text{P2 = YES 且无好格子}\ \Longrightarrow\ \text{二分猜想为假}\ }$$

**证书脚本**：`proof/layer_program/verify_counterexample_certificate_v2.py`（598/598 ✓）。
**注**：更早的 `verify_counterexample_certificate.py`（28 子式）**有 bug** ✗（`% 1` 把 `lift` 打成零向量），
已被 HANDOVER2 查出并由 v2 取代 ✓ —— 结论不变，证书换了。

**为什么这条重要**：它证明 **P2 不能替代层问题** —— 存在"结构上完全允许、$\mu\ge1$、但谱条件被一致违反"的实例。
关键机制：把"整族都坏"从"每个 $\mathcal U$ 含一个坏特征向量"改成"**$A$ 的秩整体小**"（与 $\mathcal U$ 无关）。

---

## 4. 阅读顺序（**严格按此顺序，不要跳**）

1. 本文件（HANDOVER）
2. `CLAUDE.md` —— 规范：验证分级、纪律 20 条、禁区清单。**必读**，尤其 §7 与 §10。
3. `README.md` —— 问题与地图
4. `STATUS.md` —— 一页纸现状（**§12 是 $(3,1)$ 层的权威入口**）
5. `ATTEMPTS.md` —— 约 30 条历史路线 + 状态（避免重复）
6. `proof/layer_31_theorems/README.md` —— 冻结的定理包（C.1–C.5、criterion、d4、edci）
7. `proof/layer_program/RESTRICTED_COMPLETION_MODEL.md` —— **§44 是权威总表**（什么站得住、什么撤回）
8. `archive/expert_correspondence/` —— 与专家的问答（QA6–QA8 是最近的）；**`ROADMAP_STATUS_2026-10-30.md`** 是路线图完成情况

**不要凭记忆或摘要开工** —— 本项目已因此重复劳动两次（CLAUDE.md §7.17）。

---

## 5. 目录地图

```
README.md / STATUS.md / ATTEMPTS.md / CLAUDE.md / HANDOVER.md   ← 五份入口文档（HANDOVER 是用户要求的例外）
docs/           已证/引用的纯理论（不放实验）
proof/<claim>/  按命题组织：README + 证明 + verify.py
  layer_31_theorems/   ← 冻结的 (3,1) 层定理包（C.1–C.5、criterion、d4_classification、edci）
  layer_program/       ← 层程序的工作记录（RCP = RESTRICTED_COMPLETION_MODEL.md）+ 最新脚本
  rho1_layer/          ← (ρ=1) 层的历史工作 + 大量 verify_*.py
  refuted/             ← 被推翻的命题 + 证书（R1–R12）
tools/hygiene/   两道自动闸门（见 §7）
tools/lean/      Lean 源码（WSL 里 ~/WorkSpace/lean4/MyProof 是运行环境）
workspace/       临时文件（草稿、试算）
archive/         归档：handovers/ expert_correspondence/ paper_drafts/ attempts_2026-10/ ...
trash/           回收站（不删除，登记）
```

---

## 6. 怎么跑（三条最常用）

```bash
python tools/hygiene/audit_layout.py          # 布局审计，必须 0 issue
python tools/hygiene/audit_retractions.py     # 撤回标记审计，必须 RC=0
python proof/layer_program/verify_counterexample_certificate.py   # 反例证书（符号计算，约 10 秒）
```

关键脚本（都在 `proof/`、无第三方依赖、用 `fractions.Fraction` 精确算术）：

| 脚本 | 作用 |
|---|---|
| `layer_program/verify_counterexample_certificate.py` | **反例证书**：28 个 6 阶子式恒为零 |
| `layer_program/verify_d4_classification.py` | $d=4$ 三条引理，40/40 × 3 |
| `layer_program/verify_d4_perp_branch.py` | $d=4$ 的 $\phi\perp B$ 分支（构造法），60/60 × 2 |
| `layer_program/verify_criterion_convention.py` | 覆盖判据的基无关性，30/30 |
| `rho1_layer/verify_9_12.py`、`verify_t11.py` | 历史验证（423/423、195/195）|

（**这些是精确验证，不是证明** —— 见 CLAUDE.md §4 的分级。）

---

## 7. 两条铁律（每次提交前）

```bash
python tools/hygiene/audit_layout.py        # 必须 0 issue
python tools/hygiene/audit_retractions.py   # 必须 RC=0
```

第二个闸门保证**已撤回的结论不会被再次正面引用** —— 本会话有 15 次撤回，这是自动防护。

---

## 8. 已知的坑（**都踩过，按踩的次数排序**）

| # | 坑 | 教训 |
|---|---|---|
| 1 | **把"$\perp$"/内积当成不变量** | 判据必须是**秩/包含**形式：被覆盖 $\iff\exists\lambda:\ \operatorname{rank}[\lambda I-T;w^{\mathsf T}]<\rho$。坐标点积换基会变（实测 28/30 变）。$w$ 是**行**（$w\mapsto wP^{-1}$），不是向量 |
| 2 | **行/列取向** | 铅笔是**竖着**增广的 ⟹ 秩不满 $\iff w\in\operatorname{row}(\lambda I-T)$，**不是** $\operatorname{im}$ |
| 3 | **$\mu$ 的算法** | $\mu=\dim B+3-\operatorname{rank}[B;\mathcal U]$，**不能**数"$B$ 的基向量里有多少个落在 $\mathcal U$ 里"（组合可以落在里面而基向量都不在）|
| 4 | **稀有条件不能采样** | 余维 $\ge1$ 的代数条件在 $\mathbb Q$ 上随机命中概率为 0。本会话踩了 5 次。**构造**，不要抽样 |
| 5 | **有限域语义不对** | $\mathbb F_p$ 上"$\gcd=1$"只表示在 $\overline{\mathbb F_p}$ 无公共根，**强于**"在 $\mathbb C$ 无公共根" ⟹ 有限域**系统性多报"被覆盖"**。只能用来找候选 |
| 6 | **supremal ≠ 定维数** | 条件不变子空间的族对 $+$ 封闭、最大元 $=X$ ⟹ 经典算法对"恰好 3 维"毫无信息 |
| 7 | **$\dim B\le p$**（$C$ 的行数）| 因为 $\mathcal JA$ 模 $\mathcal J$ 只由 $\{c_iA^2\}$ 张成。要 $\dim B\ge k$ 必须 $p\ge k$ |
| 8 | **"约束写漏、结论看起来对"** | 每个检查器先打印全部约束；新脚本先跑断言 |

---

## 9. 下一步（按价值排序，来自专家 QA8 §5 的路线图）

| 优先 | 事项 | 为什么 |
|---|---|---|
| 1 | **$d=4$ 的谱步**：$\dim\Phi\ge2$ 的 incidence 判定 | 把"充要"补成真正的"可判"；$\Phi$ 是 A2/A3 给出的射影子空间 |
| 2 | **EDCI**：可行维数集的结构（区间？区间之并？Kronecker 数据？）| 专家的"定维数定理"候选；**不要假设是区间** —— 和封闭不证明中间维数可达 |
| 3 | 正维族的统一覆盖（次要）| 专家已降级；若能找到会更强，但不是必需 |
| 4 | 三份新文件（criterion / d4_classification / edci）的**英文版** | 目前只有中文，而给专家的文档是英文 |

---

## 10. 与专家的往来

全部在 `archive/expert_correspondence/`。最近的：

| 文件 | 内容 |
|---|---|
| `QA6_2026-10-29.md` | 专家给的四步计划（本项目的路线图来源）|
| `REPORT_FOR_EXPERT_2026-10-29_EN.md` | 第一份自包含英文报告 |
| `QA7_2026-10-30.md` | 专家审阅"进展与计划"（三级标签 S/C/L 的来源）|
| `PROGRESS_AND_PLAN_2026-10-30_EN.md` | 第二份英文报告 |
| `QA8_2026-10-30.md` | 专家审阅反例（**两处技术更正**：$\operatorname{row}$ vs $\operatorname{im}$、$w\in\operatorname{im}f$ 类型错）|
| `COUNTEREXAMPLE_2026-10-30_EN.md` | 第三份英文报告（反例）|
| `ROADMAP_STATUS_2026-10-30.md` | 6 条 checklist 的完成情况 + 缺口 |

**给下一位**：如果要再问专家，请把问题写成**自包含的英文单文档**，不要用链接（这是用户的要求 —— 专家只看那一份）。

---

## 11. 2026-10-30 晚间进展（按专家 QA9 的 Phase I–III）

> 详细内容见各文件；这里只记"下次接手先从哪读"。

### 11.1 文献裁决（已定）

[P1] arXiv:2609.33615 与 [P2] arXiv:2609.37992 已完成**刻画**；项目定位改为"只做复杂度"。
对照：[literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md](literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md)。
假设核对（4/5 一致，第 2 条由 [proof/l0_reduction/](../../trash/README.md) 解决）：[literature/notes/P1P2_ASSUMPTIONS_CHECK.md](literature/notes/P1P2_ASSUMPTIONS_CHECK.md)。

### 11.2 Phase I（完成）

[proof/spectral_locus/](../../trash/README.md)：引理 1（$\lambda=\infty$）、引理 2（修正版 O1：分层闭/可构造）、
引理 3（Smith 证书）⟹ **$\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$**（用 $Z$-表述、不枚举图卡、$\forall\lambda$ 消去）。
新工具：[tools/verification/spectral_gcd.py](tools/verification/spectral_gcd.py)（极大子式 gcd，精确）。

### 11.3 Phase II 的结构结果（读 [proof/h_bound/README.md](../../trash/README.md)）

| 结果 | 等级 |
|---|---|
| **互补障碍**：$\ker C=\mathcal V\oplus Z$ ⟹ $(S)$ 必失败（只在 $q=n-r_1$ 可能发生）| [已证-纸面] |
| **顶层定律**：$\operatorname{rank}(CAZ)=d$ 时 $\mathcal V\cap Z=0$、$h=N_c$，故 $(S)$ 失败 $\iff q=n-r_1$ | 定理 + 数据 188/188 |
| **阶谱猜想**：可行阶 $=\{n_0-p\}\cup\{q: d\le p,\ q\ne n-r_1\}$ | 数据 53/53 + 薄层探针未推翻 |
| **公根两型**：结构型（$A$ 在 $\mathcal V$ 内的特征值）/ 耦合型（广义特征值）| 精确例子 |
| 已推翻（登记）：R13（$h<n-p$ 必要）、R14（唯一障碍）、R15（功能可观测版唯一障碍）| [proof/refuted/](../../trash/README.md) |

### 11.4 Phase III（进行中）

[workspace/q1_true/attempts/02_hardness_skeleton.md](workspace/q1_true/attempts/02_hardness_skeleton.md)：两段式骨架，
Stage 1 的双线性基元、Stage 2 的 $Z\subseteq\mathcal V\iff\operatorname{row}[C;CA]\subseteq\operatorname{row}[C;L_0]$（300/300）、
$d>p$ 的薄层是难点。**下一步**：薄层的 $(A)$-点构造 → 若能在 $d>p$ 找到 $(A)\wedge(S)$ 点，阶谱猜想被推翻；否则需要新思路。

### 11.5 已踩过的坑（这十轮的）

- 有限实 $\lambda$ 采样判 $(S)$ 会造假"通过"（CLAUDE §10.1）；
- det 论证必须先确认方阵/宽矩阵（R13）；
- 随机采样找不到薄集（R14/R15 的失败点都是薄集）；
- $q=n-r_1$ 是唯一可能被互补障碍挡住的阶。

### 11.6 阶谱猜想（**已被 R17 推翻**）

**R17 反例**（构造性、方向正确、功能可观测，[c235](proof/layer_program/c235_order_refute_v2.py)、[R17](../../trash/README.md)）：
$n=8$、$p=2$、$r_1=4$、$C=[e_1;e_2]$，
$A\colon e_1\mapsto e_3,\ e_2\mapsto e_4,\ e_3\mapsto e_7,\ e_4\mapsto e_8,\ e_5\mapsto e_5,\ e_6\mapsto e_6,\ e_7\mapsto e_1,\ e_8\mapsto e_2$，$L_0=e_3$。
则 $q=2$（$d=4$）与 $q=3$（$d=3$）上都有 $(A)\wedge(S)$ 的点，而 $q<n_0-p=4$、$d>p$、$Z\not\subseteq\mathcal V$。
**为什么之前找不到**：此前证据都来自 $Z\subseteq\mathcal V$（那时 $(A)\iff$ 不变性 ⟹ $Z\subseteq\ker\mathcal O_C$ ⟹ 终端阶）。
**R16 撤回**：曾报"$q=n-r_1$ 可行"的反例，实为行/列作用方向 bug（[c227](proof/layer_program/c227_order_conj_refute.py)）。

**仍成立**（不受 R17 影响）：
- **Theorem D**：$(S)$ 成立 ⟹ $q>t=\dim\mathcal V-\dim(\mathcal V\cap Z)$；
- **顶层定律**：$\operatorname{rank}(CAZ)=d$ 时 $(S)$ 失败 $\iff q=n-r_1$；
- **互补障碍**；**薄层部分定理**（$Z\subseteq\mathcal V$、$AZ\subseteq Z$、$A\mathcal V\subseteq\mathcal V+Z$ ⟹ 失败）。

**开放**：$A\mathcal V\not\subseteq\mathcal V+Z$ 的一般判据（R17 证明它**可以**发生且 $(S)$ 可成立），
以及 R17 之后的阶谱新刻画。

### 11.6b Lean 验证清单（2026-10-30）

| 命题 | Lean 文件 | 退出码 |
|---|---|---|
| Theorem E（横截 ⟹ 谱条件成立）| tools/lean/MyProof/TheoremE.lean | 0 ✓ |
| Theorem D 两分支（$q<t$ 与 $q=t$ 的维数障碍）| tools/lean/MyProof/TheoremD.lean | 0 ✓ |
| Theorem C 的端同态核心（自同态 ⟹ 存在 $lam$ 使 $lam\cdot\mathrm{id}-B$ 不单射）| tools/lean/MyProof/TheoremC.lean | 0 ✓ |
| 商铅笔恒等式**第一步**（$\operatorname{range}[T\mid Z]=\operatorname{range}T\sqcup Z$）| tools/lean/MyProof/QuotientPencil.lean | 0 ✓ |

复现：把 `tools/lean/MyProof/*.lean` 拷进 WSL 的 `~/WorkSpace/lean4/MyProof/MyProof/`，
再 `lake env lean MyProof/TheoremE.lean`（Mathlib 已预构建；**只**用 `write` 工具写 Lean 文件，避免 PowerShell 破坏 Unicode）。

**仍是纸面的**：商铅笔恒等式 $\operatorname{rank}P=d+\operatorname{rank}T_\lambda$、
Theorem C 的"奇异 ⟹ $\operatorname{rank}P<h$"一步、以及阶谱的全部结构结论。

### 11.7 关键脚本（回归已跑）

```bash
python tools/verification/spectral_gcd.py            # gcd 工具自检
python proof/spectral_locus/verify_smith_check.py    # 点数旁证
python proof/l0_reduction/verify.py                  # row(C) 归约 100/100
python proof/layer_program/c206_paper_example.py     # P1 例子
python proof/layer_program/c209_paper2_example.py    # P2 例子 q0/n0
python proof/layer_program/c212_allbad_exact.py      # q=4 all-bad、q=5 可行
python proof/layer_program/c225_order_conjecture.py  # 阶谱 53/53
```
