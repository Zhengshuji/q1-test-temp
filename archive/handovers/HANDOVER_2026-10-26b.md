# MIN-ROWS 移交文档（2026-10-26，修正版 b）

> 本文取代 [`HANDOVER_2026-10-26.md`](HANDOVER_2026-10-26.md)（下称 a 版）的**框架部分**。
> a 版的问题陈述、定理 1–8、工具 bug 记录、8 条陷阱**仍然有效**，本文不重抄；
> 本文只写：a 版错在哪、补了什么、以及现在唯一活着的闭式。
>
> **一句话**：闭式只剩一个——$q_{\min}=\max(r+\varepsilon,\ \rho^*+\max(c_0,1))$；
> 它的下界是定理，上界未证。$q_{\min}=d+\max(c_0,1)$ 与 $\max(r+\varepsilon,\rho^*+1)$
> 各被一族**严格反例**杀掉，后者的反例是本文新证的定理 11。

---

## 1. 相对 a 版的改动

| # | a 版的写法 | 现在的写法 | 依据 |
|---|---|---|---|
| 1 | 定理 9：$(5b)\iff(T_W,D_W)$ **可控** | 应为**可观测**（见定理 9′）| `c191_pbh.py`：铅笔 65/65、可观测 65/65、可控 **63/65** |
| 2 | 层表：$q=d+1$ **全部观察实例非空** | **假**。$c_0\ge2$ 时可为空 | 定理 11 + `c190`（8/8 实例 $q_{\min}=n>d+1$）|
| 3 | 「$q=n$ 恒非空」「$\mathcal V=\mathbb R^n$ 必可行」 | **假**。$\mathcal V=\mathbb C^n$ 可行 $\iff A^{\mathsf T}$ 在 $K$ 内无特征向量 | 定理 12；a 版自己的对角例就是反例 |
| 4 | 「无解 1 例 = 采样故障」 | 那例很可能**真的无解**（$q_{\min}=\infty$ 是合法答案）| 1/59 抽样中 $\mathbb C^n$ 不可行且 $q<n$ 全搜不到 |
| 5 | §5(A) 主攻「证 $q=d+1$ 层非空」 | 只在 $c_0\le1$ 分支有意义；一般情形已被定理 11 否 | 同上 |
| 6 | 六个闭式全死，只剩「分层非空性」框架 | 有第七个闭式**没死**（F3），且下界已证 | `c189_ledger.py` 18 行无一反例 |

$$\boxed{\ \text{分层框架只是定义（}q_{\min}=\min\{q:\ \text{第 }q\text{ 层非空}\}\text{），不含信息；有信息的是 F3 与它的下界}}$$

---

## 2. 记号（同 a 版，补三个）

$$S=\operatorname{row}(L_0),\quad \mathcal J=\operatorname{row}[C;CA],\quad j=\dim\mathcal J,\quad d=n-j,$$
$$c_0=\dim(S\cap\mathcal J),\quad \varepsilon=\mathbf 1[L_0\ \text{不是解}],\quad \rho=\operatorname{rank}(\mathcal VN),\quad \rho^*=\min_{\mathcal V\ \text{可行}}\rho .$$

$$q_{\min}=q:=\operatorname{rank}L\ \text{最小};\qquad F_1=d+\max(c_0,1),\quad F_2=\max(r+\varepsilon,\rho^*+1),$$
$$\boxed{F_3=\max\big(r+\varepsilon,\ \rho^*+\max(c_0,1)\big)}$$

---

## 3. 已证（a 版定理 1–8 照旧，此处只列新增与修正）

**定理 5（照旧，且是本文地基）.** 可行 $\mathcal V$ 满足 $q\ge\rho+\max(c_0,1)$。

*证明*：$\operatorname{rank}(L_0N)=r-c_0$，秩次可加得 $q\ge\rho+c_0$；与定理 4（$q\ge\rho+1$）合并。$\square$

**定理 5′（合并形式，本文的地基）.** 每个可行 $\mathcal V$ 满足

$$q\ \ge\ \max\big(r+\varepsilon,\ \rho+\max(c_0,1)\big)\ \ge\ F_3\ \text{（用}\ \rho\ge\rho^*\text{）}.$$

*证明*：第二项由定理 5；第一项因 $q=r$ 时唯一候选是 $\mathcal V=S$，而 $\varepsilon=1$ 说它不是解。$\square$

**定理 9′（修正 a 版定理 9：可观测，不是可控）.** 设 $\mathcal V=H\oplus W$、$H=\mathcal V\cap\mathcal J$（$\dim c$）、$W\cap\mathcal J=0$、$\dim W=d$，令 $T_W=\pi_WA|_W$、$D_W=[\pi_W(h_1A)\cdots\pi_W(h_cA)]$（$d\times c$）。则

$$Q_{\mathcal V}(\lambda)=\begin{pmatrix}-(D_W)^{\mathsf T}\\ \lambda I_d-T_W\end{pmatrix}_{(c+d)\times d},\qquad
(5b)\iff\operatorname{rank}\begin{pmatrix}(D_W)^{\mathsf T}\\ (D_W)^{\mathsf T}T_W\\ \vdots\\ (D_W)^{\mathsf T}T_W^{d-1}\end{pmatrix}=d$$

即 $(D_W^{\mathsf T},T_W)$ **可观测**（等价于 $(T_W^{\mathsf T},D_W^{\mathsf T})$ 可控）。$c=1$ 时就是「$v_W$ 对 $T_W$ 的行作用循环」。

*证明*：$\ker Q_{\mathcal V}(\lambda)=\{x:\pi(\lambda x-xA)=0\}=\mathcal V\cap F_\lambda$；把 $D_W$ 换成可控版只换了转置位置，$T_W$ 非对称时两者不同。$\square$

$$\text{实测：铅笔 }65/65\ =\ \text{可观测 }65/65\ \ne\ \text{可控 }63/65 .$$

$$\boxed{\ \text{好处：顶层（}\rho=d\text{）的 }(5b)\text{ 变成一次 }O(d^3)\text{ 的秩判定，}\lambda\text{ 与子式 gcd 都被消掉}}$$

**定理 10（照旧）.** $d=0\Rightarrow q_{\min}=r$。

**定理 11（新：$S=\mathcal J$ 的闭包定理）.** 设 $\operatorname{row}(L_0)=\mathcal J$（即 $r=c_0=j$）。则任何可行 $\mathcal V$ 满足

$$\mathcal V\supseteq\mathcal J,\quad \dim(\mathcal V\cap\mathcal J)=j,\quad
(5a)\iff\mathcal VA\subseteq\mathcal V+\mathcal J=\mathcal V\iff\mathcal V\ \text{是}\ A\text{-不变的},$$

于是

$$\boxed{\ q_{\min}=\min\{\dim\mathcal V:\ \mathcal V\ A\text{-不变},\ \mathcal V\supseteq\mathcal J,\ (5b)\}\ }$$

特别地，若 $\langle\mathcal J\rangle_A=\mathbb C^n$ 且 $\mathbb C^n$ 满足 $(5b)$，则**唯一的可行解是 $\mathbb C^n$**，

$$\boxed{\ q_{\min}=n,\qquad \rho^*=d\ }$$

*证明*：$S\subseteq\mathcal V$ 与 $S=\mathcal J$ 给 $\mathcal J\subseteq\mathcal V$，故 $\mathcal V+\mathcal J=\mathcal V$；$c=\dim(\mathcal V\cap\mathcal J)$ 满足 $j\ge c\ge c_0=j$，故 $c=j$。$(5a)$ 于是等价于 $A$-不变。$A$-不变且含 $\mathcal J$ 的子空间必含 $\langle\mathcal J\rangle_A$。若后者是全空间，则 $\mathcal V=\mathbb C^n$。$\square$

$$\Longrightarrow\quad F_2=\max(j+1,\ d+1)<n=q_{\min}\quad(j\ge2)$$

$$\boxed{\ \textbf{推论：}\ q_{\min}=\max(r+\varepsilon,\rho^*+1)\ \text{与}\ q_{\min}=\dim V+1\ \text{都被推翻（严格，非采样）}}$$

**定理 12（新：顶层可行性判据）.** $\mathcal V=\mathbb C^n$ 自动满足 $(5a)$；它满足 $(5b)$ 当且仅当

$$\operatorname{rank}[\lambda I-A;CA;C]=n\quad\forall\lambda\iff K=\ker[C;CA]\ \text{内没有}\ A^{\mathsf T}\ \text{的特征向量}$$

$$\iff\ \text{每个左特征向量}\ v\ \text{都满足}\ vC\ne0\ \text{或}\ vCA\ne0 .$$

*证明*：$\operatorname{rank}[I;CA;C]=n$，故 $(5b)$ 说 $[\lambda I-A;CA;C]$ 行满秩 $\forall\lambda$，其零空间是 $\{v:v(\lambda I-A)=0,\ vCA=vC=0\}$。$\square$

> **a 版的对角例就是反例**：$A=\operatorname{diag}(0,1,2,3)$、$C=(1,1,1,0)$ 取 $\lambda=3$，$e_4^{\mathsf T}$ 是左特征向量且 $e_4^{\mathsf T}C=e_4^{\mathsf T}CA=0$，故 $\mathcal V=\mathbb C^n$ 不可行（`c189` 中名为 `handover_diag_CA` 的行复现）。

$$\text{猜想（数据 1/59，未证）：}\ \mathcal V=\mathbb C^n\ \text{不可行}\ \Longrightarrow\ \text{问题无解}\ (q_{\min}=\infty).$$

---

## 4. 已否定（每条给实例与文件）

| 断言 | 反例 | 严格性 |
|---|---|---|
| $q_{\min}=\max(r,\rho^*+1)$ | `lit/counterexample_refute_layer_formula_2026-10-25.json`（$q_{\min}=3>2$）| 严格 |
| $q_{\min}=d+\max(c_0,1)$ | `lit/certificate_middle_layer.json`（$2<3$）、`counterexample_d4`（$3<5$）、`counterexample_p2`（$3<5$）| 严格（$q_{\min}$ 已证）|
| $q_{\min}=d+\max(c_0,1)$（一般位置）| 同上 + `lit/counterexample_rho0_lt_dimV.json` | 严格 |
| $\max(r+\varepsilon,\rho^*+1)$ | `q1_true/evidence/counterexample_max_r_eps_rho_star_plus1_n5_2026-10-26.json`（$q_{\min}=5>4$）、`…_n6_…`（$6>5$）| **严格（定理 11）** |
| $q_{\min}=\dim V+1$ | `certificate_middle_layer`（$2<3$）、`counterexample_refute_dimV1`（$1<2$）、定理 11 族（$5>4$，双向都有）| 严格 |
| 「每个补空间 $W$ 都使 $v_W$ 循环」 | a 版对角例，$W=\operatorname{span}\{CA^2,e_4\}$，$T_W=3I$ | 严格 |
| 「$\rho=d$ 普遍成立」 | `lit/counterexample_refute_dimV1.json`（$\rho=0<d=1$）| 严格 |
| 「$q=d+1$ 层恒非空」 | 定理 11 族（$d+1$ 层空）| **严格** |
| 「$q=n$ 恒非空」 | a 版对角例（$\mathbb C^n$ 不可行）| **严格** |

$$\text{证书总量：}lit/\ 9\ \text{个} + q1\_true/evidence/\ 3\ \text{个；全部经 }c189\ \text{的 }\mathbb Q\ \text{判据复核}.$$

---

## 5. 层表（修正）

| 层 | 状态 | 依据 |
|---|---|---|
| $q=r$ | 直接判定 $L_0$；可行则 $q_{\min}=r$ | 定义 |
| $r<q\le d$ | **未知**；对角 $A$ 的实例可在 $q=r+1$ 非空 | 数据 |
| $q=d+1$ | $c_0\le1$ 时经验非空（$39/39$、$46/46$）；**$c_0\ge2$ 可为空** | 定理 11 |
| $d+1<q<n$ | **未知**；可以全空 | 定理 11 族只有 $q=n$ |
| $q=n$ | 层非空 $\iff$ 定理 12 的条件成立；**可以失败** | 定理 12 |
| 全层 | 可以**全空** $\Rightarrow q_{\min}=\infty$ | 猜想（1/59）|

$$\text{a 版的「}q_{\min}\in[\rho+\max(c_0,1),\ d+1]\text{」只在 }c_0\le1\ \text{成立；}c_0\ge2\ \text{时上界要抬到 }n.$$

---

## 6. 公式清算（`c189_ledger.py` 的输出，可复现）

18 行（12 个证书 + 3 个定向实例 + 3 个定理 11 实例）；加 `--random 12` 是 30 行，4.5 秒。

| 公式 | 判决 | 被谁推翻 / 备注 |
|---|---|---|
| $F_1=d+\max(c_0,1)$ | **死** | 10 个实例（中间层、$\rho^*=0$ 层、对角例）|
| $\dim V+1$（旧定理）| **死** | 5 个实例，且定理 11 族里是**反向超**（5 vs 4）|
| $F_2=\max(r+\varepsilon,\rho^*+1)$ | **死** | 5 个实例（定理 11 族 3 个 + 证书 2 个）；30 行版里其余 9 行 $\rho^*$ 未证，记 undet |
| $F_3=\max(r+\varepsilon,\rho^*+\max(c_0,1))$ | **活** | 无反例；30/30 行**恰好取等** |

$$\boxed{\ F_3\ \text{的下界是定理（定理 5′），上界是唯一未证的部分}}$$

**为什么 $F_3$ 能同时装下两个死掉的公式**：$c_0\le1$ 时 $\max(c_0,1)=1$，故 $F_3=F_2$；$\rho^*=d$ 时 $F_3=\max(r+\varepsilon,\ d+\max(c_0,1))$，去掉 $r+\varepsilon$ 这一项就是 $F_1$。两个特例各被一族反例杀掉，合起来反而都没死。

$$\text{所以 }q1\ \text{的复杂度问题现在完全等价于：计算 }\rho^*\ \text{有多难}.$$

---

## 7. 工具状态

| 文件 | 作用 | 用法 |
|---|---|---|
| [`../scripts/core/audit_independent.py`](../scripts/core/audit_independent.py) | $\mathbb Q$ 精确线代 + 原始 $(5a)/(5b)$ | 被下面全部 import |
| [`scripts/c189_ledger.py`](scripts/c189_ledger.py) | **唯一账本**：实例库 + 三个公式的严格判决 | `python q1_true/scripts/c189_ledger.py [--random 12]` |
| [`scripts/c190_invariant_family.py`](scripts/c190_invariant_family.py) | 定理 11 族：生成 + 机器核验 + 导出证书 | `python … --n 6 --k 5` |
| [`scripts/c191_pbh.py`](scripts/c191_pbh.py) | 定理 9′：顶层 $O(d^3)$ 判据 + 与可控版对拍 | `python q1_true/scripts/c191_pbh.py` |
| [`scripts/c188_fp.py`](scripts/c188_fp.py) | $\mathbb F_p$ 筛选（两个 bug 已修，见 a 版 §6.1）| 只筛，结论必须 $\mathbb Q$ 复核 |
| [`../scripts/core/c162_dimV_formula.py`](../scripts/core/c162_dimV_formula.py)、`c166_layer_audit.py` | 历史验证器 | 保留，注意 `c162` 的构造算法在 `d4`/`p2` 上会失败但解存在 |

**账本的三条硬规矩**（写进代码）：只在 $\mathbb Q$ 上判；`q_status` 只有 `EXACT` / `UB` 两种；公式只有在**能严格推翻的方向**才标 `REFUTED`（$F_1$ 无未知量，其余需要 $\rho^*$ 已证）。

---

## 8. 已知陷阱（a 版 8 条全保留，新增 3 条）

1. 小素数给伪秩——统计用 $\mathbb Q$ 或大素数。
2. 采样系统性高估 $q_{\min}$；可行集常是薄集。
3. $\mathcal J\cap A^{-1}\mathcal J$ **不是**基向量的子集。可靠写法：$\dim(\mathcal J\cap A^{-1}\mathcal J)=j+\dim(A^{-1}\mathcal J)-\dim(\mathcal J+A^{-1}\mathcal J)$，其中 $\dim(A^{-1}\mathcal J)=n-\operatorname{rank}A+\dim(\operatorname{im}A\cap\mathcal J)$；a 版给的 $2j-\operatorname{rank}[\mathcal JA;\mathcal J]$ 只在特殊情形成立，不可默认使用。
4. $(5b)$ 的失败条件是 $\dim(\mathcal V\cap F_\lambda)\ge2$，不是 $\ne0$。
5. 「开集非空」不能由「开性」推出。
6. $\exists R$ 与 $\exists\mathcal V$ 等价（子空间层面工作）。
7. 显式族 $\operatorname{span}\{j_0\}\oplus W$ 只装得下 $c_0\le1$。
8. PowerShell 跑 `python -c` 要引号，`sys.path` 两个目录都要加。
9. **（新）任何候选公式先查 $c_0$ 项**：本轮的 $d+m$、$\max(r+\varepsilon,\rho^*+1)$、$q=d+1$ 非空、$q=n$ 恒非空，四个错误全是「忘了 $q\ge\rho+c_0$」或「忘了 $\mathcal V$ 可能被 $\mathcal J$ 绑成 $A$-不变」。
10. **（新）只写"某个公式为假"而不给实例，等于没写**。a 版 §3 第五行说 $\max(r+\varepsilon,\rho^*+1)$ 被 $8/40$ 否掉，但没有任何实例；本文用它换成了定理 11（8+2 个可复现实例）。
11. **（新）不要用「层表」当框架**。$q_{\min}=\min\{q:\text{层 }q\text{ 非空}\}$ 是定义，不含信息；真正含信息的是层的**判据**（定理 9′ / 定理 11 / 定理 12）。

---

## 9. 下一步（按性价比）

1. **判 $\rho^*$**。这是唯一的硬核：$F_3$ 成立时 $q1\iff\rho^*$ 的复杂度。已知：$\rho^*=0$ 有判据（定理 7）；`q1_false` 那边有 $\rho^*=1$ 的多项式判定器（D47，True 侧 sound、False 侧未完全证）；$\rho^*=d$ 是一般位置；中间层 $2\le\rho^*<d$ 只能搜索。**先做**：$\rho^*\le k$ 的判定能否写成定理 9′ 那样的「一次可观测性秩条件」？
2. **$F_3$ 的上界**。要证 $\exists\mathcal V$ 使 $q=\max(r+\varepsilon,\rho^*+\max(c_0,1))$。$c_0\le1$ 分支走定理 9′（要证「存在 $W$ 使 $(D_W^{\mathsf T},T_W)$ 可观测」，比 a 版的可控版更弱）；$c_0\ge2$ 分支完全空白，定理 11 给了 $c_0=j$ 的极端情形，中间情形需要新想法。
3. **可行性**：把猜想「$\mathbb C^n$ 不可行 $\Rightarrow$ 无解」证掉或否掉。这决定判定问题的输入域（现在的文档都默认有解）。
4. **$\exists\mathbb R$ 归约**。每层判定形如「Grassmannian 上是否存在满足谱条件的点」，是 $\exists\mathbb R$ 型；若能归约到已知 $\exists\mathbb R$-complete 问题（如 copositivity），至少能给出条件性硬度。
5. **定理 11 族能不能承载硬度**。它现在是多项式可判（算 $\langle\mathcal J\rangle_A$），所以只否公式、不给硬度；但它把「$q_{\min}=n$」变成可实现的目标，值得看它的变体（例如 $S$ 只占 $\mathcal J$ 的一半）是否变成组合问题。

---

## 10. 文件地图

| 文件 | 内容 |
|---|---|
| **本文** | 修正版交接（唯一入口）|
| [`HANDOVER_2026-10-26.md`](HANDOVER_2026-10-26.md) | a 版：问题、定理 1–8、bug 记录、8 条陷阱（框架部分已被本文取代）|
| [`STATUS_2026-10-26.md`](STATUS_2026-10-26.md)、[`STATUS_2026-10-25.md`](STATUS_2026-10-25.md) | 历史状态（含已撤回的 $d+m$ 候选与「核心命题 $\rho=d$」）|
| [`Q1_FOR_EXPERT_6.md`](Q1_FOR_EXPERT_6.md) … [`Q1_FOR_EXPERT_9.md`](Q1_FOR_EXPERT_9.md) | 历次给专家的材料（**互相矛盾，只作历史**）|
| [`README.md`](../../trash/README.md) | 方向入口（§1 等价形式、§2 20 条死路线）|
| [`MATROID_LEMMA.md`](MATROID_LEMMA.md)、[`Z_FORMULATION.md`](Z_FORMULATION.md)、[`REDUCTION_TARGETS.md`](REDUCTION_TARGETS.md)、[`ATTEMPTS_AND_BARRIERS.md`](ATTEMPTS_AND_BARRIERS.md) | 各条路线与死因 |
| [`LITERATURE_2026.md`](LITERATURE_2026.md) / [`LITERATURE_COMPLEXITY.md`](LITERATURE_COMPLEXITY.md) / [`LITERATURE_COVER.md`](LITERATURE_COVER.md) | 文献定位（复杂度无结果；相邻问题 NP-hard）|
| `scripts/c189`–`c191` | 本文新增工具 |
| `scripts/c169`–`c188` | 历史实验代码 |
| [`evidence/`](../../trash/README.md) | 间接证据登记 |

---

## 11. 诚实总结

**已建立**：$(5a)/(5b)$ 的可靠 $\mathbb Q$ 判据；定理 1、2（交维数、商铅笔）；定理 5′（无条件下界，$F_3\le q_{\min}$）；定理 9′（顶层 $O(d^3)$ 判据）；定理 11（$S=\mathcal J$ 的闭包定理，$q_{\min}$ 可达 $n$）；定理 12（顶层可行性判据）；唯一账本。

**已排除**：所有给过实例的闭式（见 §4，含 $F_1$、$\dim V+1$、$F_2$）、$q=d+1$ 层恒非空、$q=n$ 恒非空、$\rho=d$ 普遍成立、「每个 $W$ 都可」。

**未解决**：$F_3$ 的上界；$\rho^*$ 的可算性/复杂度。**q1（MIN-ROWS 是否 NP-hard）仍然开放**，且现在可以说得更精确：

$$\boxed{\ q1\ \text{的硬度只能来自 }\rho^*\ \text{（若 }F_3\text{ 成立），或来自 }F_3\ \text{本身为假}}$$

**最重要的教训（承 a 版）**：本项目每一次"看起来对"的结论都来自工具或推理的漏洞；新结论写进文档前必须（i）$\mathbb Q$ 复核，（ii）与定理 5′、定理 9′、定理 11、定理 12 对撞，（iii）给出失败方向与实例文件。

---

## 附录 A：定理 11 的显式证书（$n=5$，整数，[`evidence/counterexample_max_r_eps_rho_star_plus1_n5_2026-10-26.json`](evidence/counterexample_max_r_eps_rho_star_plus1_n5_2026-10-26.json)）

$$A=\begin{pmatrix}1&-1&-2&2&1\\1&0&0&-1&2\\1&-2&1&-1&-1\\2&1&-2&-2&-1\\2&-1&-1&0&-2\end{pmatrix},\quad
C=\begin{pmatrix}-1&-1&2&-1&1\end{pmatrix},\quad
L_0=\begin{pmatrix}5&0&-5&4&-11\\0&5&-5&1&6\end{pmatrix}.$$

逐项核验（全部 $\mathbb Q$ 精确；`c189` 中名为 `counterexample_max_r_eps_rho_star_plus1_n5_2026-10-26` 的那一行，`c190` 输出的第 1 行）：

| 量 | 值 |
|---|---|
| $n,p,r$ | $5,1,2$ |
| $j=\dim\mathcal J$，$d=n-j$ | $2$，$3$ |
| $c_0=\dim(S\cap\mathcal J)$ | $2$（故 $\operatorname{row}(L_0)=\mathcal J$）|
| $\varepsilon$ | $1$（$L_0$ 不是解）|
| $\mathcal J A\subseteq\mathcal J$？ | 否 |
| $\dim\langle\mathcal J\rangle_A$ | $5$ |
| $\mathbb C^n$ 满足 $(5a)\wedge(5b)$？ | 是 |
| $\rho^*$ | $3=d$（唯一可行解是 $\mathbb C^n$）|
| $q_{\min}$ | $5=n$ |

$$\Longrightarrow\quad F_1=5\ \checkmark,\quad F_2=\max(3,4)=4\ \ne5\ (\text{F}_2\ \text{被否}),\quad \dim V+1=4\ \ne5\ (\text{旧定理被否}),\quad F_3=5\ \checkmark .$$

同一构造在 $n=6$ 上给 $q_{\min}=6$、$F_2=5$（[`…_n6_…json`](evidence/counterexample_max_r_eps_rho_star_plus1_n6_2026-10-26.json)）；`c190` 默认给出 8/8 个 $n=5$ 实例，全部 $q_{\min}=n$。
