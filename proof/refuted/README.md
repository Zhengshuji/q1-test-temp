# 被推翻的命题（反例库）

> **对应 docs 条目**：—（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 这些命题**曾经**是本项目的主猜想。全部被精确反例推翻，证书保留在此。
> 证书 = 带矩阵数字的 JSON，可用 `tools/verification/c164_trusted_baseline.py` 的有理数判据复核。

---

## R1 · $q_{\min}=\dim V+1$

**陈述**：$q_{\min}=\dim V+1$，其中 $V=\langle S\rangle_{A'}$ 是 $S=\operatorname{row}(R_0)$ 在 $A'$ 下的不变闭包。
**推翻**：$n{=}5$、$p{=}2$、$q{=}1<\dim V+1=2$。
**证书**：`certificates/counterexample_refute_dimV1.json`
**崩点**：$S\not\subseteq\mathcal A$（Gap A）。
**历史**：这是最早的主攻方向，见 [archive/attempts_2026-10/q1_false/01_dimV_plus_1.md](../../archive/attempts_2026-10/q1_false/01_dimV_plus_1.md)。

---

## R2 · $q_{\min}=d+\max(c_0,1)$

**陈述**：$q_{\min}=d+\max(c_0,1)$。
**推翻**：三份证书——`counterexample_candidate.json`、`counterexample_d4.json`、`counterexample_p2.json`。
**典型**：$n{=}6,p{=}1,d{=}4,c_0{=}0$：$\dim V+1$-型的值给出 5，真值 3。

---

## R3 · $q_{\min}=\max(r+\varepsilon,\ \rho^*+1)$

**陈述**：$q_{\min}=\max(r+\varepsilon,\rho^*+1)$。
**推翻**：`counterexample_max_r_eps_rho_star_plus1_n5_2026-10-26.json`、`..._n6_....json`、
`counterexample_refute_layer_formula_2026-10-25.json`。
**反例族**：$\operatorname{row}(L_0)=\mathcal J$ 且 $\langle\mathcal J\rangle_A=\mathbb C^n$ 时 $q_{\min}=n$（[tools/certificates/c190_invariant_family.py](../../tools/certificates/c190_invariant_family.py)），而下界 $\rho^*+1$ 小得多。

---

## R4 · $F_3:\ q_{\min}=\max(r+\varepsilon,\ \rho^*+\max(c_0,1))$

**陈述**：上一条加上 $c_0$ 项（曾被认为是"最后幸存的闭式"）。
**推翻**：$n{=}4$、$d{=}2$、$r{=}2$、$c_0{=}1$、$\varepsilon{=}1$，$q_{\min}=4$ 而 $F_3$ 给 3。
**证书**：`certificates/counterexample_f3_n4_2026-10-27.json`（脚本 `tools/p_algorithm/c196_f3_counterexample.py`）
**机制**：$q{=}3$ 层 $(5a)$ 在整条 1 参数族上成立、$(5b)$ 全部失败 ⟹ 强制 $c=2$（$c_0$ 只是下界）。

---

## 正面证书（不是反例，但用于推翻公式）

| 文件 | 用途 |
|---|---|
| **C1** | $q_{\min}=\mathrm{cl}+1$（闭包 $+1$）| [C1_closure_plus_one.md](C1_closure_plus_one.md) | $n=5$ seed 3001 等 **40/56** 个可观测实例是 $q_{\min}=\mathrm{cl}$ |
| **C2** | "$h<q+r_1$ 充分"| [C2_h_lt_q_r1_not_sufficient.md](C2_h_lt_q_r1_not_sufficient.md) | 912 个铅笔中 **415 个**满足 $h<q+r_1$ 但 $(5b)$ 失败（有显式例）|
| **C3** | "$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$"| [C3_gap_can_be_two.md](C3_gap_can_be_two.md) | Fernando 2026 §VII：$q_0=3$、$\nu_{\min}=5$（间隔 2）；本项目已复现 |
| **C4** | 猜想 T（$q=q_0$ 处 $(5b)\iff h<q_0+r_1$）| [C4_type3_counterexample.md](C4_type3_counterexample.md) | $n=6$、Jordan 块 $A$、$p=r=2$：$L$ 满足 $(5a)$、$h=6<7=q_0+r_1$，但 $d_{\rm fin}=2$（证书 [verify_C4_type3.py](verify_C4_type3.py)）|
| `certificates/certificate_middle_layer.json` | 中间层存在（$q_{\min}=2$，$d{=}2$，$c_0{=}1$，$\varepsilon{=}1$）|
| `certificates/certificate_rho0_lt_dimV.json` | $\rho^*=0<\dim V$ 的解 |
| `certificates/certificate_rhostar_lt_dimV.json` | $\rho^*<\dim V$ |
| `certificates/certificate_wide_bracket.json` | 夹逼可以很宽 |

---

## 复核

```bash
python tools/p_algorithm/c196_f3_counterexample.py     # R4（含 JSON 写出）
python tools/verification/c164_trusted_baseline.py     # (5a)/(5b) 的有理数判据
```
| **S1 判据的充要性**（$\dim K\ge\rho$）| [S1_criterion_iff.md](S1_criterion_iff.md) | `counterexample_s1.json`（$n{=}4,\rho{=}2,c{=}1$：判据假但 $(5a)\wedge(5b)$ 真）| 2026-10-28 |

---

## R12 · 专家 QA6 §5 的**二分猜想**（P2 = NO 或存在未被覆盖的格子）

**陈述**（专家 2026-10-29 提出）：每个结构可允许的 $(3,1)$ 层，要么没有 $\mu\ge1$ 的可允许格子，要么存在**未被覆盖**的可允许格子。

**推翻**：$n=6$ 的实例 $A=\begin{pmatrix}-1&0&2&1&-1&-1\\0&2&0&0&0&0\\0&0&0&0&0&0\\-2&-1&4&2&-2&-2\\-2&0&4&2&-2&-2\\0&-2&0&0&0&0\end{pmatrix}$、$C_0=\begin{pmatrix}2&1&-2&2&-1&-1\\2&2&2&1&-1&1\end{pmatrix}$、$L_0=[1,0,0,0,0,0]$：
$j=3$、$d=3$ ⟹ 3 维 $\mathcal U$ **唯一**（$=X$）、$\dim B=1$ ⟹ $\mu=1$（P2 = YES）；
而对**所有**允许的提升、**所有** $\lambda$，铅笔的 28 个 6 阶子式**恒为零** ⟹ $(5b)$ 恒失败 ⟹ 层不可行。

**证书**：`proof/layer_program/verify_counterexample_certificate_v2.py`（598/598 ✓）：
$\operatorname{rank}(A)=2$ 与 $\dim\pi(XA)=1$ 给 $\operatorname{rank}[-\mathcal LA;CA;C]\le j+1=4<6=r_0$，
故 $(5b)$ 在 $\lambda=0$ 处对**任意** 4 行 $\mathcal L$ 都失败 ✓。
（更早的 `..._certificate.py` 用 28 子式，**有 bug** ✗ —— 已被 HANDOVER2 §3 查出，结论不变、证书已换 ✓。）

**崩点**：P2 只保证"结构上有一个与 $B$ 相交的通道"；谱条件可以被 $A$ 的**低秩**性质**一致地**违反，与 $\mathcal U$ 的选取无关。

**详情**：`proof/layer_program/RESTRICTED_COMPLETION_MODEL.md` §80–§82；专家往来 `archive/expert_correspondence/QA7_2026-10-30.md`、`QA8_2026-10-30.md`。

## R13 · 可行 ⟹ $h<n-p$（**错误**：只在方阵情形成立）

**陈述（被推翻）**：若 $h=\operatorname{rank}[V\mid Z]=n-p$ 则 $(S)$ 必失败，故可行必 $h<n-p$。

**反例**（[../layer_program/c217_wide_counterexample.py](../layer_program/c217_wide_counterexample.py)，固定种子可复现）：
$n=5$、$p=1$、$r=1$、$q=2$：$r_1=2$、$d=2$、$h=4=n-p$、铅笔列数 $N_c=5>h$（**宽矩阵**），
精确极大子式 gcd $=1$ ⟹ $(S)$ 成立。

**原因**：$h=n-p$ 时极大子式只能取 $\ker C$ 基下的前 $h$ 行；但 $N_c>h$ 时它们是 $h\times h$ **子矩阵**（可多个、次数更低），
gcd 可非常数。只有方阵情形（$N_c=h$）才有"唯一极大子式 = 非零次数的行列式"的论证。

**仍成立的部分**：方阵 + 互补情形（$N_c=h=n-p$，即 $\ker C=\mathcal V\oplus Z$）的**互补障碍**定理 —— 见 [../h_bound/README.md](../h_bound/README.md)；
P2 例子 $q=4$ 恰是方阵（$N_c=6=h$），其 all-bad 仍是确定的。

## R14 · 唯一障碍 = 互补（**错误**）

**陈述（被推翻）**：$(S)$ 失败的唯一机制是 $\ker C=\mathcal V\oplus Z$（互补）。

**反例**（[../layer_program/c219_wide_failure.py](../layer_program/c219_wide_failure.py)）：
$n=5$、$p=1$、$C=e_1$、$L_0=e_5$，$A$ 让 $W=\operatorname{span}(e_2,e_3,e_4)$ **不变**，取 $Z=W$（$d=3$）：
$(A)$ 成立（$\operatorname{rank}[Z,AZR]=3=d$），$h=4=n-p$，但列数 $N_c=7>h$（**非互补**），精确 gcd 次数 $=1$ ⟹ $(S)$ 失败。

**重要补充**：这些实例**不是功能可观测的**（$\operatorname{row}L_0\not\subseteq\operatorname{row}\mathcal O_C$，见 c219 的核对），所以它们违反 P2 的前提"Assume $(A,C,L)$ is functionally observable"。因此 R14 推翻的是**无前提**的"唯一障碍"猜想。[R15](#r15--功能可观测版唯一障碍错误) 给出功能可观测版的反例。

**教训**：上一轮的 528 点数据用**随机** $Z$ 采样，没覆盖"$Z\subseteq V$ 且 $A|_Z$ 有结构"这种薄集
（正是 CLAUDE §7.12 的"薄集不许采样"）。互补障碍定理仍成立，但**不是唯一机制**。

## R15 · 功能可观测版"唯一障碍 = 互补"（**错误**）

**陈述（被推翻）**：在功能可观测（$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O_C$）前提下，$(S)$ 失败仅当 $\ker C=\mathcal V\oplus Z$。

**反例**（[../layer_program/c221_funcobs_family.py](../layer_program/c221_funcobs_family.py)）：
$n=5$、$p=1$、$C=e_1$、$L_0=e_5$、$A$：$e_1\mapsto e_2$、$e_2\mapsto e_4$、$e_3\mapsto e_2$、$e_4\mapsto e_3$、$e_5\mapsto e_1$。
则 $n_0=2$、$\operatorname{row}\mathcal O_C=\operatorname{span}(e_1,e_5)$ ⟹ **功能可观测** ✓；$V=W=\operatorname{span}(e_2,e_3,e_4)$（$\dim3$）。
- $q=1$（终端阶 $n_0-p$）：**可行**（$(A)\wedge(S)$ ✓）；
- $q=2$：$(A)$ 成立 24 个，$(A)\wedge(S)$ **0**；失败点 $h=3$、$N_c=5$（**非互补**）；
- $q=3$：$(A)$ 2 个，$(A)\wedge(S)$ **0**；$h=3$、$N_c=4$（非互补）；
- $q=4$：$h=3=N_c$ 但 $V\ne\ker C$ ⟹ 非互补，$(S)$ 失败。

**结论**：功能可观测前提下 $(S)$ 也会在非互补位置失败 ⟹ 该版本猜想被推翻。
**附带现象**：此例 $q_{\min}=n_0-p=1$，而**所有中间阶全部 all-bad**。

## R16 · **撤回**（原"$q=n-r_1$ 可行"的反例是方向 bug 造成的）

**原主张**：阶谱猜想错误，因为 $q=n-r_1$ 也可行。

**撤回理由**：原检查 [c227](../layer_program/c227_order_conj_refute.py) 用 $\operatorname{row}(v)\cdot A$（**行作用**）
判 $Z=\mathcal V$ 的 $A$-不变性，而 $(A)$ 需要**列作用** $AZ$（$Z$ 的列是基向量）。
按列作用重算原实例：$\operatorname{rank}[Z,AZR]=2\ne d=1$ ⟹ **$(A)$ 不成立** ⟹ 反例不成立。

**更正后的搜索**（[c227b](../layer_program/c227b_order_conj_recheck.py)，正确方向）：
同族（$h=d=1$、$Z=\mathcal V$）200 个 $(A)\wedge(S)$ 点，**全部是终端阶**（$q=n_0-p$，此时不构成反例）；
非终端阶 **0 个** ⟹ **没有反例**。

**结论**：该次"推翻"不成立；教训是 CLAUDE §7.2 的"行堆叠 vs 列拼接"（本会话第 4 次方向问题）。
**仍成立**：顶层定律、互补障碍。

## R17 · 阶谱猜想（**错误**：薄层也能可行 —— 方向正确、全部检查通过）

**陈述（被推翻）**：可行阶 $=\{n_0-p\}\cup\{q: d\le p,\ q\ne n-r_1\}$，即**薄层（$d>p$）除终端阶外不可行**。

**反例**（[../layer_program/c235_order_refute_v2.py](../layer_program/c235_order_refute_v2.py)，构造性、无随机）：
$n=8$、$p=2$、$r=1$、$C=[e_1;e_2]$，
$$A:\ e_1\mapsto e_3,\ e_2\mapsto e_4,\ e_3\mapsto e_7,\ e_4\mapsto e_8,\ e_5\mapsto e_5,\ e_6\mapsto e_6,\ e_7\mapsto e_1,\ e_8\mapsto e_2 .$$
则 $CA=[e_7;e_8]$、$r_1=4$、$\mathcal V=\ker[C;CA]=\operatorname{span}(e_3,e_4,e_5,e_6)$、$n_0=6$、$n_0-p=4$。
取 $L_0=e_3$（$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O_C$ ⟹ **功能可观测** ✓）：

| 阶 | $d$ | $Z$ | $s$ | $t$ | $q<n_0-p$ | $d>p$ | $Z\not\subseteq\mathcal V$ | $(A)$ | $(S)$ |
|---|---|---|---|---|---|---|---|---|---|
| $q=2$ | 4 | $\operatorname{span}(e_4,e_5,e_6,e_8)$ | 3 | 1 | ✓ | ✓ | ✓ | ✓ | ✓ |
| $q=3$ | 3 | $\operatorname{span}(e_4-e_7-e_8,\ e_5,\ e_6)$ | 2 | 2 | ✓ | ✓ | ✓ | ✓ | ✓ |

⟹ 薄层（$d>p$）的**非终端阶**也能可行 ⟹ 阶谱猜想的"薄层不可行"部分**错误** ✗。

**与 Theorem D 相容**：两点的 $q>t$（$2>1$、$3>2$）✓ —— Theorem D 是必要条件，不是充分条件。
**与顶层定律相容**：这些点不在顶层（$r=\operatorname{rank}(CAZ)=1<d$）。

**结构教训**：之前所有"薄层全坏"的证据都来自 $Z\subseteq\mathcal V$（那里 $(A)\iff$ 不变性 ⟹ $Z\subseteq\ker\mathcal O_C$
⟹ 终端阶，见 [../h_bound/README.md](../h_bound/README.md) 的引理）。这里的 $Z\not\subseteq\mathcal V$，
$(A)$ 是真正的秩条件，$(S)$ 得以成立。

---

## R18 · "$(5b)$ ⟹ 铅笔的右最小指标全为 $0$"（**错误**）

**陈述（已撤回）**：若铅笔 $Q(\lambda)$ 的秩恒等于其 normal rank（$(5b)$ 型），则它的**右**最小指标全为 $0$。
2026-11-02 我把它作为"已证观察"写进了 [REPORT_2026-11-02_WORKSTREAM_B_EN.md](../../workspace/for_expert/archive/REPORT_2026-11-02_WORKSTREAM_B_EN.md) §5，
理由是"右零空间是常值子空间"。**该理由错误**：维数恒定不意味着子空间恒定。

**反例（专家 2026-11-02 §1）**：$Q(\lambda)=\begin{pmatrix}\lambda&1\end{pmatrix}$（$1\times2$）。

- $\operatorname{rank}Q(\lambda)=1$ 对一切 $\lambda\in\mathbb C$（常数秩 ✓）；
- $Q(\lambda)\begin{pmatrix}1\\-\lambda\end{pmatrix}=0$ ⟹ 右零空间 $=\operatorname{span}\{(1,-\lambda)^{\mathsf T}\}$ **随 $\lambda$ 变**；
- 故右最小指标是 $1$，**不是** $0$。

**证书**：[tools/verification/kron_identity_probe.py](../../tools/verification/kron_identity_probe.py) 第 1 节
（脚本断言 `eta == [1]`）。

**崩点**："秩恒定 ⟹ 零空间恒定"——把**维数**恒定误当**子空间**恒定。

**正确表述**（专家 §1）：常数秩 ⟺ 无**有限**初等因子（正则部分的条件）；
它对**最小指标的次数**不给任何约束。

**正确的全局恒等式**（专家 §3）：$\sum_i\eta_i+\sum_j\varepsilon_j+\sum_k\deg\gamma_k=r$
（$\gamma_k$ 为齐次不变因子）。注意 $\sum\deg\gamma_k$ **不等于**
"(有限不变因子次数和) + (反转铅笔次数和)"（反例见同一脚本第 2 节）；
在 $(5b)$ 型下退化为 $\sum\eta+\sum\varepsilon+d_\infty=r$，这一特例在我们的可行样本上全部成立 ✓。

---

## R19 · "$d_\infty=h-\operatorname{rank}L\iff\ker L=N$"（**错误**的等价）

**陈述（已更正）**：在 T4-b 的表述里我写了"$d_\infty=h-\operatorname{rank}L$，等价地 $\ker L=N$"。
**错**（专家 2026-11-02 §2 指出）。

**为什么不成立**：由 B.6，$\dim N=n-h$，且 $N\subseteq\ker L$，故
$$\ker L=N\iff\dim\ker L=n-h\iff\operatorname{rank}L=h\iff d_\infty=0 .$$
即"$\ker L=N$"只是 $d_\infty=0$ 的**特例**，不是一般等价。

**正确表述**：$\dim(\ker L/N)=(n-\operatorname{rank}L)-(n-h)=h-\operatorname{rank}L$，于是
$$d_\infty=h-\operatorname{rank}L\iff d_\infty=\dim(\ker L/N).$$

**崩点**：把"$d_\infty$ 等于维数差"误读成"两个空间相等"。

**位置**：更正已在 [workspace/kronecker/TARGET_FORM_T.md](../../workspace/kronecker/TARGET_FORM_T.md)
与 [workspace/kronecker/README.md](../../workspace/kronecker/README.md) §4.8 落地。

---

## R20 · "$d_\infty$ = 反转铅笔不变因子的**次数**和"（**错误**的度量）

**陈述（已更正）**：T4-b 的早期统计里我把 $d_\infty$ 算成"反转铅笔 $Q_1+\mu Q_0$ 的不变因子的**多项式次数**之和"。
**错**：无穷初等因子对应的是反转铅笔在 $\mu=0$ 处的**初等因子**，即不变因子的 **$\mu$-adic 赋值**（常数项为零的阶），
不是总次数。

**反例（具体数字）**：$n=6$、seed 1002、$q=4$ 的观测器铅笔，反转铅笔的不变因子是
$$1,\ 1,\ 1,\ \tfrac14-\mu+\mu^2 .$$
* 总次数读法：$0+0+0+2=2$ ⟹ 假的"反例"（$h-\operatorname{rank}L=4-4=0$，看似矛盾）；
* $\mu$-adic 赋值：$0+0+0+0=0$ ⟹ 与 $h-\operatorname{rank}L=0$ 一致 ✓。

**修正**：`tools/verification/kronecker_pencil.py` 现在输出 `d_infinity`（$\mu$-adic 赋值之和），
`infinite_divisors` 每项也带 `mu_valuation` 字段。

**崩点**：把"次数"当成"在 $\mu=0$ 处的阶"——当不变因子有非零常数项时两者不同。

**影响**：早期"103/103""188/188"两个数字是用总次数算的，碰巧在那些样本上一致；
改成正确度量后，结论更强：**151/151**（含 43 个不可行的铅笔）并且已经**证明**（见
[proof/t4b_infinite_divisors](../t4b_infinite_divisors/README.md)）。

---

## R21 · "$(5a)$ ⟹ $\sum_j\varepsilon_j=\operatorname{rank}L$"（**过度声称**，专家 2026-11-02 §2）

**陈述（已更正）**：我在 T4-b 的"推论"里写"由 B.6 + 恒等式得 $\sum\varepsilon=\operatorname{rank}L$"，
并把它当成 $(5a)$ 的推论（FINAL 报告 §1、§6，docs/02 B.7，TARGET_FORM_T）。
**错**：全局恒等式是
$$\sum\eta+\sum\varepsilon+d_{\rm fin}+d_\infty=h,$$
其中 $d_{\rm fin}$ 是**有限**初等因子的总次数。由 B.6（$\sum\eta=0$）与 B.7（$d_\infty=h-\operatorname{rank}L$）得
$$\sum\varepsilon=\operatorname{rank}L-d_{\rm fin}.$$
只有再加 $(5b)$（$d_{\rm fin}=0$）才有 $\sum\varepsilon=\operatorname{rank}L$。

**证据**：`proof/t4b_infinite_divisors/verify.py` 的 151 个满足 $(5a)$ 的铅笔里，**43 个不满足 $(5b)$**，
它们的 $d_{\rm fin}$ 从 $1$ 到 $7$（分布见脚本输出），$\sum\varepsilon$ 因此**小于** $\operatorname{rank}L$。
用旧说法这些全会被误判为"反例"。

**崩点**：把 $d_{\rm fin}$ 当作 0——那是 $(5b)$ 的内容，不是 $(5a)$ 的。

**顺带的两条正确推论**（已写入 [docs/02 B.7](../../docs/02_theorems_proven.md)）：
1. $d_{\rm fin}\le\operatorname{rank}L$；
2. 若 $(5a)+(5b)$ 同时成立，则 $\operatorname{rank}L\le q+2p-h$（左指标个数非负、和 $=\operatorname{rank}L$）——
   一条**谱可行性的必要条件**。

---

---

## R22 · "$\omega=2$、$q=3$、固定 $L_0$ 时变量核不可能"（**错误**）

**陈述**：若 $L_0$ 固定、$\omega=2$、$q=3$，则不存在变量核的可行族（attempt 217）。
**推翻**：专家 68/69 答复给出 $n=10$、$p=3$、$q=3$ 的显式族
$L(t)=[e_1;\ e_2+t e_3+e_8;\ e_1+e_2+t e_3+e_8+e_9+t e_{10}]$，
固定 $A,C,L_0$，核 $V_t=\operatorname{span}\{-t e_2+e_3,\ e_4\}$ 随 $t$ 变，
且对所有 $t$ 满足 $(5a)(5b)$ 与 $\mathsf P_{\rm ind}$。
**证书**：[tools/verification/c228_omega2_family.py](../../tools/verification/c228_omega2_family.py)（精确有理，$t=0,1,2,-1,3$ 全过）。
**崩点**：$h_{A,0}$ 为零行并不使 $3\times k$ 的秩 $2$ 铅笔掉秩——其余两行可以独立。
**历史**：[attempts/217](../../workspace/q1_true/multiplication_gate/attempts/217_single_gate_q_lower_bound.md)、[attempts/228](../../workspace/q1_true/multiplication_gate/attempts/228_68_69_verdict.md)。

---

## R23 · "只用 $lA$ 的 reduced determinant $\det M=ad-bc$ 是观测器门"（**错误**）

**陈述**：$n=5$、$q=2$ 的实例中，$\det[lA;L_0;l;CA;C]=ad-bc$ 给出 $(5a)$ 的充要条件（attempt 234/237）。
**推翻**：$(5a)$ 的 $LA$ 含**两行** $L_0A$ 与 $lA$；漏掉 $L_0A$ 后条件变弱。补上后
$(5a)\iff b=0,\ d=0,\ c\ne0$，而在这条轨迹上 $(5b)$ 的极大子式
$\Delta=c(\lambda^2-\lambda-1)$ 恒有复根 ⇒ 该实例**没有可行 $L$**。
**证书**：[tools/verification/c239_missing_L0A.py](../../tools/verification/c239_missing_L0A.py)（精确有理；$(1,0,1,0,0)$ 满足 $(5a)$ 但 $(5b)$ 失败；$(0,0,1,1,0)$ 等不满足完整 $(5a)$）。
**崩点**：漏行 $L_0A$；reduced determinant 只测 $lA\in\operatorname{row}M_0$。
**历史**：[attempts/234](../../workspace/q1_true/multiplication_gate/attempts/234_explicit_gate.md)、[attempts/239](../../workspace/q1_true/multiplication_gate/attempts/239_72_missing_L0A.md)。
