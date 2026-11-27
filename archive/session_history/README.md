# history — 历史归档

> ⚠️ **本目录下的所有内容都是历史记录，不得作为结论引用。**
> **现行结论一律以 [`../OPEN_PROBLEM.md`](../OPEN_PROBLEM.md) 与 [`../RESULTS.md`](../RESULTS.md) 为准**
> （`../FINAL.md` 也已降级为历史结论库，见其文首横幅）。
> 保留它们的原因是：**记录被推翻的结论及其错误分析**——这对避免重犯同一个错误有价值。

---

## 归档原因与内容

### 1. `proof/`（16 个文件）

原来 `proof/01`–`proof/20` 是按时间顺序累积的推进记录，问题在于：

- **相互冲突**：后面的文件推翻了前面的文件（如 `13_支A证明审查.md` 推翻了 `11`/`12` 中的结论），
  但旧文件仍原样保留在 `proof/` 里 ⟹ 读者无法判断哪个是最新的；
- **大量已作废内容**：引理 4、引理 5、引理 7、猜想 (S0)、旧 `condS` 判据等，
  其错误分析已提炼进 [`../FINAL.md`](../FINAL.md) §7；
- **过程性内容**：试错记录、中间推导、失败的尝试。

**保留在 `proof/` 的**（当前有效）：
`A_分支A的完整证明.md`、`B_地基检查与交付结论.md`、`C_情形II的结构.md`、
`D_支B的精确解数.md`、`E_审查与撤回清单.md`、`00_证明索引.md`

**归档到这里的**：`01`–`12`、`15`、`16`、`18`、`19`

| 归档文件 | 内容 | 为何归档 |
|---|---|---|
| `01_初始审查.md` | 最初的命题审查 | 结论已被 02–13 大量修正 |
| `02_约束影响与q1q2关系.md` | q1/q2 关系 | 已并入 `problems/q2.md` |
| `03_证伪尝试.md` | 早期证伪尝试 | 大部分结论已作废 |
| `04_完整数学证明尝试.md` | 最初的"完整证明" | **依赖已被证伪的引理 4、5** |
| `05_PDF前提假设清单.md` | 论文假设清单 | 内容已并入 `FINAL.md` §1 |
| `06_重新审查.md` | 第二轮审查 | 已并入 `13`（现 `E_`） |
| `07_0-1现象与多项式算法.md` | 早期数值现象 | 方法（`condS`）已证不可靠 |
| `08_S的几何刻画.md` | (S) 的几何直观 | 已被 `T5/T5′` 取代 |
| `09_实现缺陷定位与结论修正.md` | 实现缺陷 | 记录保留 |
| `10_本轮发现与修正.md` | 中间修正 | 已被后续覆盖 |
| `11_P1闭式实现与随机方法失效.md` | P1 闭式实现 | 关键内容已提炼进 `FINAL` §4.2 |
| `12_命题q的数学推导.md` | 早期推导 | 引理 4/5 在此，**已证伪** |
| `15_分支A最终结论.md` | "最终结论"（旧） | 被 `17`（现 `B_`）取代 |
| `16_分支A的确定结论.md` | "确定结论"（旧） | 被 `17`（现 `B_`）取代 |
| `18_情形II的可能性实验.md` | 情形 II 可为 YES | 已合并进 `C_情形II的结构.md` |
| `19_情形II的仿射结构.md` | 定理 D1/D2 | 已合并进 `C_情形II的结构.md` |

### 2. `problems_txt/`（旧命题原文）

| 文件 | 现位置 |
|---|---|
| `q.txt` | → [`../../problems/q1.md`](../problems/q1.md) |
| `q2.txt` | → [`../../problems/q2.md`](../problems/q2.md) |
| `q3.txt` | → [`../../problems/q3.md`](../problems/q3.md) |
| `q4.txt` | → [`../../problems/q4.md`](../problems/q4.md) |
| `q_simp.md` | → [`../../problems/q_now_MFOSP.md`](../problems/q_now_MFOSP.md) |
| `q_now_旧版_292行.md` | → 已重写为 [`../../problems/q_now.md`](../problems/q_now.md) |

**归档原因**：原 `q4.txt` 的"支 A"整段（引理 4/5 + 定理 6 + "满测度或空"）**已被推翻**，
但旧文本仍在文件里 ⟹ 会误导。新 `problems/*.md` 已按统一框架（描述/定位/已完成/下一步/验证）重写。

### 3. `scripts/`（134 个旧脚本）

原 `scripts/core/` 有 **101 个** `.py`、`scripts/archive/` 有 **43 个**。问题：
- 大量是**一次性诊断脚本**（`diag*.py`、`debug*.py`）或**失败的尝试**（多次重跑同一实验的不同版本）；
- **相互覆盖**：许多脚本复制粘贴了同一段库代码，改动历史无法追溯；
- **无法判断哪个是结论依据**。

**保留在 [`../../scripts/core/`](../../scripts/core/) 的只有 13 个**（见其 README），
其余 134 个归档至此。

### 3b. 🆕 本会话新归档的 23 个脚本（任务 ②/①/A/B 的产物）

**归档规则**：脚本的**结论已被撤回或被取代** ⟹ 归档。
（详见 [`../FINAL.md`](../FINAL.md) §7 的第 13–17 处更正。）

| 脚本 | 为何归档 |
|---|---|
| `attack_chart.py`、`attack_chart_eig.py`、`attack_chart_decomp.py`、`attack_chart_grid.py`、`diag_decomp.py`、`diag_rank_pattern.py` | 计算 $\operatorname{rank}(RN_CK)$ 时用了 **`mm(RNC,Kr)` 维数错配** ✗ ⟹ "实例在图卡外"是 artifact（第 13 处）|
| `B_ii_first_step.py`、`recompute_rho_fixed.py` ~~保留~~ | 前者同上 ✗；**后者已修正并保留** ✓ |
| `verify_T5a.py` | 它**错误地支持了核空间版** T5a ✗（第 11/12 处：行空间版才对）|
| `verify_T10.py`、`construct_T5a_A.py`、`construct_and_check_S.py` | T10 撤回、T11 无效（第 12 处）|
| `verify_chart_linear.py` | 判据 A 有维数错配 ✗ ⟹ 结论不可信（已由 `recompute_rho_fixed.py` 取代 ✓）|
| `test_parallel_case.py`、`taskA_conjecture.py`、`settle_Astar.py`、`diag_search_space.py`、`taskA_branch2.py`、`taskA_branch1_rigorous.py`、`taskA_decide.py` | 全部用了**只对 $q_0=2$ 成立的 (I)∧(II) 表述**去处理 $q_0=3$ 的实例 ✗（第 15、17 处）|
| `verify_c5_rigorous.py`、`verify_c5_witness.py`、`diag_c5_values.py` | c5 撤回（第 16 处：判定是**空洞**的——齐次系统 ⟹ 零解恒存在 ✗）|
| `close_lambda12_gap.py` | 其结论（$\lambda_{12}=0$ 分支为空）**只对 $k=2$ 实例成立**，$k=1$ 时该分支**非空** ✗（第 14 处）|

**⭐ 其中最值得记住的两个**：
1. `diag_c5_values.py` —— 它打印出了"解是 $\lambda{=}0,\gamma{=}0,c{=}0$ ⟹ $w=0$"，
   从而**揭穿了 c5 判定是空洞的** ✓（诊断脚本的价值）
2. `taskA_branch1_rigorous.py` —— 它的"子式全 $\equiv0$"结果**引发了那个矛盾**，
   最终定位到 **(I)∧(II) 只对 $q_0=2$ 成立** ✓

---

## 如何使用本目录

- ❌ **不要**从本目录引用任何结论；
- ✅ **可以**在这里查找"某个错误结论当初是怎么来的"（例如 `12_命题q的数学推导.md` 里的引理 4 及其证明）；
- ✅ 若要查"某个结论的现状"，去 [`../FINAL.md`](../FINAL.md)；
- ✅ 若要查"某个命题要做什么"，去 [`../problems/`](../problems/)。

## 其他归档

| 文件 | 内容 |
|---|---|
| `README_旧版_24KB.md` | 旧的总览（含已作废结论，如"支 A ⟹ BPP"、"P1: NP-hard 为假"） |
| `CLAUDE_旧版.md` | 旧的工作记忆 |

---

## 2026-10-20 工作区整理（本次）

| 新位置 | 内容 | 来源 |
|---|---|---|
| `docs/` | 目录说明：[`docs/README.md`](docs/README.md) | 新建 |
| `docs/DIRECTIONS_2026-10-18.md` | 旧的「所有研究方向索引」（86 KB，10-18 版，已被 `52`/`53` 取代） | 原根目录 `DIRECTIONS.md` |
| `docs/ANSWER_2026-10-20.txt` | **外部模型对本项目的审阅意见**（P4b、Φ 收缩等结论的提出者） | 原根目录 `ANSWER.txt` |
| `proof/c6-strategy_2026-10-16.md` | c6 策略文档（c6 已于 10-17 被显式见证证伪） | 原 `proof/c6-strategy.md` |
| `scripts/2026_10_experiments/` | **258 个**被取代的实验脚本（原 `scripts/core/` 的超集），见其 [`README.md`](scripts/2026_10_experiments/README.md) 与 [`FILES.md`](scripts/2026_10_experiments/FILES.md) | 原 `scripts/core/` |
| `scripts/archive_early/` | 最早一批 43 个脚本（原 `scripts_archive/`） | 原 `history/scripts_archive/` |

> 归档脚本**未修改**，它们按 `__file__` 定位库文件 ⟹ **不能就地运行**，要跑请复制回 `scripts/core/`。
> 根目录现在只保留 7 个 md：`README / OPEN_PROBLEM / RESULTS / PAPER / PROOF_AUDIT / FINAL / CLAUDE`。
