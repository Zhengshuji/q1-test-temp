# CLAUDE.md — 项目规范（2026-10-27）

> 本文件是**唯一**的开发规范（也是给后续会话/协作者的"提示词"）。
> 开始工作前：读本文件 → `README.md` → `STATUS.md` → `ATTEMPTS.md`。
> 目标：让"有效的工作"沉淀下来，"无效的尝试"留下可查记录，且**永不把猜想写成定理**。

---

## 0. 这个框架存在的理由（先读这一节）

新框架的全部设计只服务五个目标。**任何改动都要先问：它服务于哪一条？**

| # | 目标 | 靠什么机制保证 |
|---|---|---|
| 1 | **方便接手** | `README`（问题+地图）→ `STATUS`（一页纸现状）→ `CLAUDE`（规范）三件套；`workspace/<方向>/<子方向>/attempts/NN_*.md` 每条路线一篇开发日志 |
| 2 | **建立在坚实基础上** | `docs/` 只放**纸面证明或 Lean** 的命题（§4 验证分级）；`proof/<claim>/` 一命题一目录，附 `verify.py`；`[精确验证]` 与 `[已证]` 严格区分 |
| 3 | **不重复已完成的研究** | `ATTEMPTS.md` 总表（约 30 条路线 + 状态）；`archive/framework_map/`（旧框架结论现状）；§10.3 已死路线；`archive/data/inventory.tsv`（885 文件总清单）|
| 4 | **不重复过去的错误** | §7 纪律 **20 条** + §10 教训速查（**15 条禁区** / 7 条有效做法）；被推翻的命题进 `proof/refuted/` 而不是删掉 |
| 5 | **查找文件方便快捷** | 固定目录语义（§2）；`inventory.tsv` 一行一文件（路径/大小/类型/标题）；`tools/hygiene/audit_layout.py` 保证不断链；`git log` 可回溯任何版本 |

> 一句话：**"有效的东西沉下来，无效的东西留下尸检记录，任何断言都能点到文件。"**

---

## 1. 项目是什么

**MIN-ROWS / q1**：给定 $(A,C,L_0)$，求最小 $q$ 使存在 $R$（$\mathcal L=[L_0;R]$，$q$ 行）满足

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \forall\lambda .$$

$q1$ 问：计算 $q_{\min}$ 是否 NP-hard？——**仍开放**。

---

## 2. 目录结构（按"是否有效"组织，不按新旧）

| 目录 | 放什么 | 判定标准 |
|---|---|---|
| `paper/` | **只放 Paper III / IV**（Paper I / II 在 `q1-functional-observer`，本仓库不留副本、不复述） | 论文只放冻结的算法/结构结果；硬度/gadget 不进论文 |
| `docs/` | 定义、**已证**命题（纸面证明或 Lean）、**引用**定理、结构定理、术语 | 只放**严谨**的：Python 实例复核不算证明，一律放 `workspace/q1_*/<子方向>/proof/` |
| `proof/<claim>/` | 按**要证的命题**组织：`README.md` + 证明 + 可选 `verify.py` | **2026-11-26 起不再维护**；可复用的目录已复制到 `workspace/q1_*/<子方向>/proof/`，原件只作历史 |
| `workspace/` | **核心工作空间**：两个大方向 + `support/`（管理/审计/讨论）+ `_exchange/`（临时） | 见下三行 |
| `workspace/q1_true/` | 硬度侧（证 NP-hard / $\exists\mathbb R$-hard）。子方向：`multiplication_gate`（活跃）、`rank_gates`（历史）、`arm_reduction`（规划） | 每级四件套：`README` / `STATUS` / `RESULTS` / `LESSONS`；`attempts/` 在子方向内 |
| `workspace/q1_false/` | 算法侧（证多项式）。子方向：`c_stratification`（活跃，Paper III/IV）、`decision_algorithms`（冻结，Paper I）、`feasibility_geometry`（历史） | 同上 |
| `workspace/ATTEMPTS_INDEX.tsv` | 501 篇 attempts 的分层索引（方向 / 子方向 / 策略） | 迁移与检索的权威表 |
| `tools/` | 按**类别**：`exact_linalg/ verification/ ledger/ layer_search/ p_algorithm/ certificates/ lean/ hygiene/`（`hygiene/` = `audit_layout.py` 布局审计 + `backup_before_edit.py` 覆盖前备份） | 脚本必须在类别目录里，不放 `tools/` 根 |
| `literature/` | **仅参考文献**：`pdf/ txt/ papers/ notes/` | 不放本项目的结论 |
| `archive/` | 按**内容**归档：`attack_A2V0/ handovers/ expert_correspondence/ framework_map/ gap_analyses/ proof_audits/ proof_notes_dimV_line/ problem_statements/ paper_drafts/ process_logs/ project_reports/ session_history/ old_scripts/ data/ methodology/` | 只归档"对主线已无帮助"的；**归档后只读**——`archive/handovers/` 里的交接文档不再修改（用户 2026-11-01 明确），现状变化写 `STATUS.md` / `workspace/` |
| `trash/` | **回收站**：不用的文件先移到这里，不删除 | 只有 `README.md` + 登记过的文件 |

**根目录只允许 5 个 md**：`README.md`、`STATUS.md`、`HISTORY.md`、`ATTEMPTS.md`、`CLAUDE.md`。
`HISTORY.md` 记录项目脉络（怎么走到 $q1$）；`STATUS.md` 只记现状与尝试方向，二者互补、不重复。别的进上面某个目录。

新方向 → 在 `workspace/` 下新建目录；**不要**建"新/旧"或日期目录。

---

## 3. 当前主线（写文档前先对齐）

> **2026-10-30 定位更新（最重要的一条）**：本项目的"刻画"目标**已被文献完成**。
> [P1] arXiv:2609.33615 与 [P2] arXiv:2609.37992（Fernando, 2026-09）给出**逐阶完整刻画**：
> 阶谱 $\Sigma_{FO}(L)\subseteq[q_0,\,n_0-p]$、每阶充要条件（P2 Thm 5 的 $\exists Z$；Thm 6 的图卡 $Z_I(\Theta)$：
> $q$ 阶观测器存在 $\iff\exists$ 图卡与 $\Theta$ 使 $(14a)(14b)$）、$\nu_{\min}=\min\Sigma_{FO}$、以及构造。
> 其中 $\exists Z$ 判据**就是**本项目的 $\exists(\mathcal U,\mathcal H)$（换坐标）；$q_0=\sum_j\eta_j$ 也是多项式。
> 对照见 [literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md](literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md)。

$$\boxed{\ \textbf{唯一还开放的}：\ \exists\Theta\ \text{（图卡}\times\text{半代数）的判定复杂度}\ \text{——即 }q1\ }$$

- **已由文献解决（不要再"证明"）**：存在性、阶谱、逐阶充要、最小阶 = 最小谱可行阶、构造；
  以及 $q_0=\sum_j\eta_j$（$(A)$ 侧的最小维数，多项式）。
- **$(5a)$ 的定位（2026-11-03 明确）**：$(5a)$ **只作为"定义域/参数化"出现**（$\exists\mathcal L$ 的约束），
  **不作为研究对象**。任何"$(5a)$ 的几何/判据/维数"结果都只能标为**工具**，
  不进 `docs/02`、不写进对外简报的"结果"部分。研究时间必须以 **$(5b)$ / $q_{\min}$ / 阶差** 为主体。
  （教训：2026-11-03 连续几轮在做 $G_{\mathcal Z}$、$\operatorname{rank}\varphi$、Schubert 余维，
  这些是 $(5a)$ 侧的工具，偏离了主线。）
- **本项目的既有结果**（一律**降级**为"对接/重新发现"，写作时必须引用 P1/P2）：
  $\rho_{ci}=P(T,B,U_0)$（弱于 $q_0$）、层分解 $(\rho,c)$、格判据 C.1–C.5（Thm 5 的特例）、$\tau$ 消除（同 Thm 6 的 gcd 检验）。
- **可能独有**（需先查文献再声称）：秩屏障 $\rho\le\min_\lambda r(\lambda)$；$\exists\mathbb R$ 框架；$d=4$ 的有限性观察。
- **已死**：四个闭式（[proof/refuted/](proof/refuted/README.md)）、拟阵/TAP、**"可控性"刻画**（$\beta(\mathcal H)\subseteq B$ 恒为零）。

---

## 4. 验证分级（**强制标注**）

| 等级 | 含义 | 写作 |
|---|---|---|
| **Lean** | 机器检查通过（`lake build` 0 error） | `[Lean]` + 模块名 |
| **已证** | 有完整纸面证明 | `[已证]` + 证明位置 |
| **精确验证** | 有理数/整数算术，有限实例，无舍入 | `[精确验证 n/N]` |
| **数值** | 浮点/随机 | `[数值]`（**不能**当证据）|
| **猜想** | 其余一切都是猜想 | `[猜想]` |

**硬规则**
1. 没有实例的断言等于零：公式/反例必须带**证书文件**或**可复现脚本**。
2. 不许把 `[精确验证]` 写成 `[已证]`；不许把 `[数值]` 写进 `docs/`。
3. 被推翻的命题进 `proof/refuted/`，**保留**陈述 + 反例 + 证书路径（不要删）。
4. 新公式先自查：是不是恒等式？是不是只在 $n\le4$ / $\mathbb F_p$ 上成立？
5. 小素数小规模实验**只能**筛掉假命题，不能确认公式。
6. **`[Lean]` 必须可追溯到声明名；登记只写"框架 + 出处"**（2026-11-07 用户修订）：
   写 `[Lean]` 时必须给出 [`tools/lean/STATEMENT_MAP.md`](tools/lean/STATEMENT_MAP.md) 里登记的**声明名**
   （只写文件名不算）。该表的**目的**是给出**证明框架**——它以命题为节点、以"支撑关系"为边，
   **只关注命题之间的联系，不关注具体证明**。因此：

   * **必填：出处**。要么引用参考文献（作者/年份/arXiv 编号），要么链接到本项目**已证明的命题**
     （`docs/` 或 `proof/` 的链接都行，也可只写命题编号如 `B.9(a)`）。
   * **选填：意义**。该声明在框架中的作用是什么（此前要求的"差异"一节**已取消**：
     它原是研究方向发散时用来强制各命题保持区别的，现按用户指示改为"意义"且不强制登记）。
     历史条目里的"差异"保留不动，但不再是必须项。
   * **粒度：以"命题级声明"为准**。工具/辅助声明可按
     [`tools/lean/EXEMPT_AUXILIARY.md`](tools/lean/EXEMPT_AUXILIARY.md) 做**文件级豁免**；
     豁免文件里的命题级声明仍必须点名并登记。
   * 新增声明未登记 ⟹ `audit_lean_statements.py` 报错。**Lean 证的是"内核"时，只能写 `[Lean 内核]`
     并写明差在哪**，不许把弱于命题的东西标成整条命题的 `[Lean]`。
   * **严谨性不减**：出处必须真实、可点开；宁可少登记，不许登记查不到的东西。

**验收规则（2026-11-07 用户修订）**："完成证明"的标准是——

> **能用 Lean 的就用 Lean 验证；不能或不方便用 Lean 的，接受可信度高、可靠性高的纸面证明**
> （专家复核，或来自论文/经典教材等可信来源）。纸面证明**可以包含 Lean 也可以不包含**，**包含 Lean 更好**。

由此：
* **完成** = 数学 M≥3（可信纸面）且（如 Lean 可行则已形式化）；**Lean 不是硬门槛**；
* **未完成** = M<3（纸面未闭合，或未经任何可信来源确认）；
* **实验**（精确算术/数值/随机实例）仍**不计入证明**（§18）；
* 每条卷宗必须写清：M 值、F 值、"Lean 是否可行/已有"，以及**完成判定**。

**状态双维（2026-11-07 采纳专家建议）**：数学状态与形式化状态**分开记**，L 由 (M,F) 导出——

| 维度 | 取值 |
|---|---|
| 数学 M | M0 未证 · M1 仅有实验 · M2 纸面草稿 · M3 独立复核（专家/文献）· M4 已成文献定理 |
| 形式 F | F0 无 · F1 辅助引理 · F2 非平凡核心已形式化 · F3 字面陈述已形式化 |

**导出的 L**：L4 ⟺ F3（且 M≥3）；L3 ⟺ F2 且 M≥3；L2 ⟺ M≥3 且 F≤1；其余 L1。
卷宗的 `## 验证状态` 必须写 `(M?, F?)` 与导出的 L。

**对外部的三级映射**（专家 2026-11-01 §9.2 要求"说 verified 必须带级别"）：
L1 = 纸面推导自检（≈ `[已证-纸面]` 的门槛）、L2 = 精确算术验证（`[精确验证]`）、L3 = Lean（`[Lean]`）。
写 "verified" 时一律写成 `L1` / `L1+L2` / `L3`，并说明覆盖范围（只验了特例就必须写出来）。

---

## 5. 文档规范

### 5.1 `docs/`（严谨内容）
`00_problem` 问题与等价形式 · `01_notation` 记号 + 术语表 · `02_theorems_proven` 已证命题 · `03_theorems_cited` 引用定理 · `04_structure` 结构 · `05_open_questions` 开放问题 · `07_literature_review` **文献综述** · `08_results` 结果汇总。管理/总览文档在 `workspace/support/project_management/`。
每条命题：**陈述 → 证明（或指针）→ 等级 → 位置**。经验数据、python 复核、未证等价**都不放这里**。

### 5.2 `proof/<claim>/`
- 必须 `README.md`：陈述、状态（已证/部分/推翻）、文件清单、复现命令。
- 长证明拆 `theorem.md`（陈述+证明）/ `algorithm.md` / `verification.md`。
- 精确算术复核写 `verify.py`，**标明"验证不是证明"**。

### 5.3 `attempts/`（每方向每条路线一篇开发日志）

位置：`workspace/<方向>/<子方向>/attempts/`；分层索引在 `workspace/ATTEMPTS_INDEX.tsv`
（列：`num / file / title / direction / subdirection / strategy`）。
固定小节（缺一不可；`tools/hygiene/audit_layout.py` 会检查）：
```
# 路线名
## 目标
## 设想与理由
## 做法
## 进展
## 最终结论
## 放弃原因（若失败：具体到哪一步过不去）
## 残留价值
## 相关文件
```
编号约定：`00_` 放该方向的索引/总结，`01_`… 放具体路线。

### 5.4 总表
`ATTEMPTS.md`：只列 方向 | 文件 | 最后更新 | 状态 | 一句话结论。不放细节。

### 5.5 `workspace/for_expert/`（对外文档）

> 2026-11-02 教训：给专家的文档写了 6 份、按日期命名、正文靠 `proof/…` 路径指路——**专家看不到仓库**，
> 于是"where"一列、"Pointers"一节对他全是空的；同时内容按时间堆叠而不是按实质分类。

1. **一份文件**：每次对外**只提交一个文件**。它必须**自包含**——正文里不出现仓库路径
   （`proof/…`、`docs/…`、"见某处"）；要给出的结论必须把**陈述与关键证明**写进文档本身；
   提到文献时给作者/年份/编号（专家可自行核对），不复述其证明。
2. **结构固定三段**（按**实质内容**分类，不按时间）：
   - **Part I 问题与标准形式**：问题陈述（$q1$、$(5a)/(5b)$）、记号的完整定义、等价形式、
     文献**已解决**的部分（明确划出"这不由本项目承担"）；
   - **Part II 项目已做的工作**：结果（陈述+证明+等级）、方法（如何验证）、**更正记录**（哪些说法被撤回及原因）；
   - **Part III 请求**：缺口（复杂度、编码规模、结构）、具体问题。
   同一件事只出现一次；不要"Equivalences / Settled / Results"再分家。
3. **不写日期**（会话日期对专家无意义）。
4. **命名**：`NN_<topic>.md`（两位序号，按提交顺序）。**待回复的文档可以多份并存**于顶层
   （每个问题一份，互不覆盖）。**收到回复后成对归档**：提问 `<NN>_<topic>.md` 与回复
   `<NN>_<topic>-reply.md` 一起移入 `for_expert/archive/`；顶层只留仍在等待回复或仍需处理的那几份，
   外加 `README.md` 索引。
5. **语气中立**：只写"已证 / 已精确验证 / 未证 / 未知"；不写"这很有希望""我们建议您……"这类
   引导性判断，不替专家下结论；把判断留白。

### 5.6 `paper/`：论文以 `.tex` 为**唯一**事实来源（2026-11-10 起）

> 起因：论文曾以 Markdown 维护、再转 LaTeX 出 PDF，版式与学术论文差距大，且存在两份要同步的源。
> 现改为**直接维护 `.tex`**。

1. **唯一来源**：`paper/current/<name>.tex`（与 PDF 同目录，`pdflatex` 就地编译；`.aux/.log/.out` 已被 `.gitignore` 覆盖）。**不再维护同名 `.md`**；旧 `.md` 只留一个指针桩
   （避免历史链接断掉），内容以 git 历史与 `trash/` 备份为准。
2. **版式**：`\documentclass[journal]{IEEEtran}`（两栏），对齐
   [`literature/papers/2307.08923.pdf`](literature/papers/2307.08923.pdf) 的风格：
   标题 + 作者块 + `abstract` + `IEEEkeywords` + 编号章节 + 编号参考文献。
   **不要**在正文里放开头的 "Status/草稿" 横幅（状态写进 `paper/README.md`）。
3. **定理环境**：`amsthm` + 自定义 `plainn` 风格，`\newtheorem*{lem}{Lemma}` 等；编号**写在可选参数里**
   （`\begin{lem}[3]` → "Lemma 3."），正文一律用数字引用（Lemma 1–6、Theorem 1–3、Proposition 1、
   Corollary 1–2），与式号 (1)(2)(3) 同一套风格。改编号只改可选参数与正文文字，**不要**把环境改成
   带计数器的版本（试过一次，`\end` 错位导致嵌套报错）。
4. **表格**：两栏下用 `table*` + `booktabs`（不用 `longtable`），每张表必须有 `\caption`。
5. **构建**：`cd paper && pdflatex <name>.tex && pdflatex <name>.tex`（两遍，交叉引用与文献号），
   或 `latexmk -pdf`。PDF 入库、作为交付物；`.tex` 是源头，PDF 是派生物。
6. **文献**：正文用 `\cite{key}` + `thebibliography`；arXiv 预印本要在条目里注明 `(preprint)`。
7. 旧的 `md2tex.py` 已移入 `trash/`，**不要**再引入 Markdown 平行源。


---

## 6. 工具与环境

- **Git（Windows 侧）**：**`C:\Program Files\Git\cmd\git.exe`**（v2.49.0.windows.1，已在 PATH 上，
  直接 `git` 即可；2026-11-19 核实）。`git config --global`：`user.name=Zhengshuji`、
  `user.email=2607430020@qq.com`、`core.autocrlf=false`（与 §11.1 一致）。
  **SSH 已配置并验证**：`ssh -T git@github.com` 返回 `Hi Zhengshuji! You've successfully authenticated`
  （密钥在 `%USERPROFILE%\.ssh\`，`id_rsa`/`id_dsa` 与 `known_hosts` 都在），因此
  **artifact 仓库可以推送**：`git@github.com:Zhengshuji/q1-functional-observer.git`；
  该仓库本地副本在 `C:\Users\26074\Desktop\工作 学习（待办）\q1-functional-observer`（WSL 的
  `~/WorkSpace/lean4/Q1Paper` 是其工作源，仓库 `Q1Paper/` 必须与它逐字节一致）。
  推送前先在 WSL 侧跑 `bash scripts/check.sh`（构建 + 公理审计），再把文件同步过去再 commit/push。
- Python：`python <path>`（Windows 侧）。**默认解释器是 conda base**（`C:\ProgramData\anaconda3-updata\python.exe`，3.12.7），
  其中 **sympy 1.13.2 可用**（2026-11-03 核实）。约定：
  * 常规脚本仍用 `fractions.Fraction` 纯 Python（保证可移植）；
  * **CAS 只在 `tools/verification/exact_elimination.py` 这类"精确消元"模块里使用**，并在文件头注明；
  * 用 CAS 得到的结论必须写明**可靠性条件**（例：Rabinowitsch 见证枚举不得截断，否则只能报 `unknown`）。
- **Lean 4 + Mathlib 在 WSL**：**WSL 里就是本项目的 Lean 树**（2026-11-04 核实：`~/WorkSpace/lean4/MyProof/MyProof/` 有 **107 个 `.lean`**，含 `proof/*/lean/` 归来的文件与 `Foundations/`、`Chk*.lean` 等）。
  * **Windows 侧可直接读写它**（UNC 已验证可访问）：
    `\\wsl$\Ubuntu-22.04\home\zsj\WorkSpace\lean4\MyProof\MyProof\` —— 读写都不必先拷进临时目录；
* **Lean 只存在 WSL，不再有 Windows 备份**（2026-11-19 收敛）：论文用 `~/WorkSpace/lean4/Q1Paper/`
  （唯一源），项目推进中的证明检查用 `~/WorkSpace/lean4/MyProof/`。仓库内原有的
  `tools/lean/MyProof/`、`paper/lean/`、`proof/*/lean/` 等副本已移入 `trash/lean_removed_2026-11-19/`；
  `tools/lean/` 下只保留 `check_lean.sh`、`STATEMENT_MAP.md` 一类工具与记录。修改一律直接在 WSL 里进行，不再来回拷贝。
  * 工具链 `leanprover/lean4:v4.35.0`，Mathlib 已预构建。单文件编译（已验证）：
    `wsl -e bash -lc 'cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MyProof/X.lean'`
  * 被 `import` 的模块（如 `MyProof.RowSpace`）必须先 `lake build MyProof.RowSpace` 生成 `.olean`，
    否则报 `object file ... does not exist`；
  * 输出重定向到文件再读（`> /mnt/c/Windows/Temp/x.log 2>&1`），避免 PowerShell 管道吞掉 Unicode；
  * **不要**再用 `C:\Windows\Temp\leanprobe` 一类临时目录中转（这是 2026-11-04 之前反复"重新发现路径"的原因）。
- **Unicode 陷阱**：`⧸`/`⊔`/`⊆` 经 PowerShell 重定向或管道可能被替换；Lean 文件一律用 `write` 工具写，或先写到 `workspace/` 再 `cp` 进 WSL。
- **卫生检查**：`python tools/hygiene/audit_layout.py`（布局、attempts 小节、docs 严谨性、trash、断链；0 issue 才算干净）。

---

## 7. 纪律

1. **不删除、不覆盖**。要"删"的移进 `trash/` 并在 `trash/README.md` 登记；**整体替换任何文件前先跑** `python tools/hygiene/backup_before_edit.py <path>`（自动存到 `trash/*.bak`）。真删除必须先问人。
2. 秩判据写清"行堆叠"还是"列拼接"（踩过 4 次）。
3. 完整堆叠 $\ker[L;CA;C]\neq\ker L\cap\ker C$。
4. "开集非空" ≠ "处处成立"；薄解集用采样必错过。
5. 搜索必须显式检查 $\operatorname{row}(L_0)\subseteq\operatorname{row}(\mathcal L)$。
6. 历史工具 bug 的共同模式：**约束写漏、结论看起来对**——脚本先打印所有约束检查。
7. 反例优先：先花 10 分钟造反例，再造公式。
8. 别用"数据支持"当结论；最多写 `[精确验证 n/N]`。
9. 文档里的每条断言都要能点到一个文件；点不到的删掉（先移 `trash/`）。
10. 一个会话只推进**一个**命题；跨命题的发现先记 `workspace/`，随后归类。
11. **拿不准就问**：目录归类、是否算定理、是否与已有结论冲突——先问再做。
12. **稀有/薄集不许采样**：可行集常是余维 $\ge1$ 的代数集。已知两例：$q_0$ 下界 0/300×8；
    $n{=}4,p{=}1,d{=}2$ 精确 $1/133$ vs 采样 $0/300$。要么精确枚举，要么**构造**。
13. **数值与推导冲突时，用手算最小反例定案**（旧框架第 11/12 处即"数值错、推导对"）。
14. **矩阵乘法前断言维数**（旧 `mm(X,Y)` 不检查、静默算错，第 13 处）。
15. **齐次系统"相容"≠"有解"**（右端为 $0$ 时零解恒在，判定会空洞；第 16 处）。
16. **旧框架只作参考**：引用前查 [`archive/framework_map/`](archive/framework_map/README.md)，
    标 ❌ 的禁止引用；研究工作一律在**新框架** $(\rho,c,(5a),(5b))$ 下开展。
17. **开工先读全档案**：`CLAUDE → README → STATUS → ATTEMPTS → proof/README.md（命题关系表）→
    需要的那几个 proof/*/README.md` → `archive/expert_correspondence/expert_qa_*/REPLY` →
    `workspace/*/attempts/`。**不许凭摘要或记忆动手**（本项目已因此重复劳动三次；
    2026-11-02 那次的复盘见 [archive/process_logs/repeat_research_2026-11-02/repeat_research_postmortem_2026-11-02.md](archive/process_logs/repeat_research_2026-11-02/repeat_research_postmortem_2026-11-02.md)）。
    完整命题清单：`tools/hygiene/claims.tsv`，检索用
    `python tools/hygiene/claim_index.py --grep <关键词>`。
18. **实验永远不能替代证明**。任何 `[精确验证]`/`[数值]` 结论都必须**在同一处写明缺什么证明**；
    对 $q1$ 的最终结论（无论真假）**必须**是纸面证明或 Lean 检查，实验只用于**筛假**和**找方向**。
    这条是对 §4"验证分级"的操作化：分级不是终点，只是标记"证明还差什么"。
19. **每个命题开工前先做一轮文献检索**：按**问题的形状**检索（如"∃ 参数使某条件成立"的术语），
    而不是只按对象名；固定跑一遍"相邻判定问题是否 NP-hard"的查询清单；
    查询式、日期、命中结果记进 [`literature/SEARCH_LOG.md`](literature/SEARCH_LOG.md)。
    **教训**：本项目曾因只引用冻结的文献笔记，漏掉了 2026-09 的 Löfberg（静态输出反馈 NP-hard）——
    而它恰好推翻了我们一条关键启发式。


20. **每个命题必须"证完就验"**：新命题写完立刻至少做一条机器检查 —— 优先 **Lean**（`tools/lean/`，退出码 0），
    其次**精确验证**（`verify_*.py`，有理算术 + 具体见证）。两者都做不到时，**必须**在文档里写明
    "为什么不能"并把该条标为 **【已证-纸面】**，不许默默放过。
    判定"验证是否足够"的标准：**验证的是命题本身，而不是它的特例**；若只验了特例，写明"覆盖范围"。
    （2026-10-29 教训：定理 12 起初只写纸面一行式，改 Lean 后才发现 `det(λ•U − U Tᵀ) = det U · det(λI − Tᵀ)`
    可以三条引理机器验证；而"非零三次必有根"那一步在 Lean 里 API 名不对，就明确标注由精确验证覆盖。）

21. **"证书"脚本必须先打印并 `assert` 被检验对象的基本不变量**（秩、维数、类型），再判断结论。
    每个证书必须能被一条断言在**坏输入**上打挂。
    （2026-10-30 教训：`verify_counterexample_certificate.py` 的 `lift` 被 `% 1` 清零 ⟹ 脚本里的 "V" 秩 1
    ⟹ 28 个 6 阶子式**平凡**为零，脚本还打印 `r0 = 6（应 = 6）` 这种同义反复，照样宣布"证书成立"。
    后来加的 v2 先打印 `rank(A)`、`j`、`d`、`dim B`、`dim π(XA)` 并逐条 assert —— 这才是证书该有的形状。
    **统一实现**：`tools/verification/consistency_checks.py` 的 `check_candidate(A,C,L0,L)` 提供专家 2026-11-03 §8.6
    的七条检查（秩、零空间维数、$CZ=\mathcal LZ=0$、$(5a)$ 与零空间判据一致、目标秩=法秩、
    gcd 与 Toeplitz 一致、系数域为有理）；新增 `verify_*.py` 必须调用它。

22. **开工前"按命题形状"检索，并写进 attempt 文档**：新命题/新路线动手前，先跑
    `python tools/hygiene/claim_index.py --grep "<形状词>"`（例：`row\(LA\)`、`初等因子`、`Smith`、
    `descriptor`、`因子化`），**不许只按自己新造的记号检索**（例：`T4-b`、`d_infty`——archive 里没有这些词）。
    命中列进 attempt 文档的「先前工作」小节，并写明"为什么这不是重复"。
    2026-11-02 的教训：$(5a)$ 不是硬度来源、$LA=\Lambda L+G_0C+G_1CA$、$P=(\lambda I-\Lambda)H$
    三件事早在 `proof/5a_archive` 与 `proof/5b_upper_bound`（2026-10-21）就有，
    而本会话重新推导并重复做了 Lean 形式化。

---

## 8. 会话协议

**开始**：读 `CLAUDE.md` → `README.md` → `STATUS.md` → `ATTEMPTS.md` → [`workspace/CLAUDE.md`](workspace/CLAUDE.md)（接手须知与避坑清单）；不要凭记忆开工。

**结束**（每次有结论的会话）：
1. 有证明的 → `workspace/q1_*/<子方向>/proof/` + `docs/02` 登记（`proof/` 只作历史，不再新增）；
2. 有尝试的 → `workspace/<方向>/<子方向>/attempts/NN_xxx.md`（§5.3 格式）+ `ATTEMPTS.md` 一行 +
   `workspace/ATTEMPTS_INDEX.tsv` 一行；
3. 有反例/证书的 → 对应子方向的 `proof/` 或 `certificates/` + `docs/02` / `proof/refuted/README.md`（历史）；
4. 更新 `STATUS.md` 与该方向/子方向的 `STATUS.md`；
5. 跑 `python tools/hygiene/audit_layout.py`，0 issue 收工。

---

## 9. 常用命令

```bash
python tools/hygiene/audit_layout.py                 # 布局/一致性审计（0 issue 才算干净）
python tools/hygiene/audit_retractions.py             # 已撤回结论不得被正面引用
python tools/hygiene/audit_lean_statements.py         # Lean 声明 ↔ 命题对照表（STATEMENT_MAP）一致
python tools/hygiene/audit_lean_coverage.py          # docs/02 的 [Lean] 标记 ↔ proof/lean_coverage.md 表一致
python tools/hygiene/backup_before_edit.py <path>     # 覆盖前备份到 trash/
python tools/ledger/c189_ledger.py                   # 账本：所有实例的公式判定
python tools/p_algorithm/c195_P_q.py                 # P 的值
python tools/p_algorithm/c197_P_witness.py --n 5      # P 的值 + 见证
python tools/layer_search/c192_reduced_search.py --n 6 --k 3   # 可达集
python proof/lower_bound/verify.py                   # A.1-A.3
python proof/pencil_equivalence/verify.py            # B.1
python proof/rho0_layer/verify.py                    # B.3
python proof/top_layer_observability/verify.py       # B.4
```

---

## 10. 历史教训速查（禁区 / 有效做法）

> 来源：旧框架 20 处自我更正（`archive/process_logs/CLAUDE_旧记忆_2026-10-23前.md` §3/§5）+
> 新框架的尝试记录（`ATTEMPTS.md`）。**读一遍再动手。**

### 10.1 禁区（已证实会出错，不要重复）

| 禁区 | 为什么会错 |
|---|---|
| 用只对 $q_0=2$ 成立的 (I)∧(II) 表述处理 $q_0\ge3$ | 连续 4 处错误的根源 |
| 矩阵乘法不检查维数（旧 `mm`）| 静默算错，看不出 |
| 把齐次系统的"相容"当"有解" | 零解恒存在 ⟹ 判定空洞 |
| 用随机采样找稀有实例 | 薄集必错过（0/300 × 8）|
| 用"随机方向"验证下界 | 可行集是零测代数集 |
| 用优化器"没找到"当"不存在" | 两次误判 |
| 用过时的判据（旧 `condS`）| 只在 $A$ 的特征值处检验，而 $(5b)$ 必须对所有 $\lambda$ |
| 只用 $L_0$ 的第一行做"平行"判据 | 对 $r\ge2$ 太弱，选出的是假平行 |
| 固定 $\ell$（$\Lambda$ 的后 $k$ 列）再扫网格 | $\ell$ 本身自由，固定它是对轨迹取子集 |
| 用"坐标层"结论直接推非坐标层 | 需要 $(T)$，而 $(T)$ 已被 $n{=}6$ 反例推翻 |
| 引用旧框架的"已证"结论 | 多数已被 $n{=}5$ 反例推翻（查 framework_map）|
| **"某对象在采样里恒为零"当成"某结构定理成立"** | 例：$(5b)\iff$ 可控的"输入"$\beta(\mathcal H)\subseteq B$ 恒为零 ⟹ 可控退化；16276/16276 的"验证"只是没碰到非退化情形 |
| 用别的判据的**退化项**做等价 | 先把每个对象在两端都算出来，看它是否恒为 0 / 恒满秩 |
| 写出一个"因为对象恒在子空间里"而**自动成立**的充要/必要条件 | 例：$\beta(h)\in B$ 恒成立 ⟹"$\beta(h)$ 的模 $B$ 闭包 $\le2$"是空话，不能解释任何稀有性（本项目第二次踩到，已更正为"需要模 $B$ 的特征方向"）|
| **层号 $\rho$ 必须由 $\operatorname{rank}[\mathcal L;CA;C]-j$ 算出** | 不能用 $\dim\mathcal L$ 或 $\dim(\mathcal L\cap\mathcal J)$ 推；2026-10-28 曾因此把一个 $(1,1)$ 层实例误当成 $(2,1)$，险些误报"基线有 bug" |
| **用有限个（实）$\lambda$ 采样代替 $\forall\lambda$** | 2026-10-30：P2 例子的 $q=4$ 上用 7 个实 $\lambda$ 判出"(S) 通过 432/486"，精确极大子式 gcd 显示**全部失败**（公根是复根/非整数）⟹ 谱条件必须用 gcd（[tools/verification/spectral_gcd.py](tools/verification/spectral_gcd.py)）|
| **把"唯一极大子式 = 行列式"的论证用在宽矩阵上** | 2026-10-30：证明"$h=n-p\Rightarrow(S)$ 失败"时没检查铅笔列数 $N_c=(n-r_1)+d$ 是否等于 $h$；宽矩阵（$N_c>h$）下极大子式是**子矩阵**、gcd 可非常数 ⟹ 结论假（反例 [R13](proof/refuted/README.md)）。**任何"det 论证"先写清矩阵是方阵还是宽/高** |
| 用**一个**左零向量刻画"秩降" | 一个 $\varphi$ 只给 $\operatorname{rank}\le d-1$；要刻画 $\operatorname{rank}\le\rho-1$ 必须用**全部** $\times$ 子式（本项目在 $(2,1)$ 层踩到，已自我更正）|
| **把 $m$ 行的"截断对象"当成铅笔行列式** | $m=h-s$ 是**参数空间** $H/S$ 的维数，$w_m=w-s$ 是**铅笔底空间** $W/S$ 的维数；只有 $m=w_m$（$H=W$，$L_0\subseteq\operatorname{row}C$）时两者相同。否则 $m$ 行对象只是某个子式，不是 $\det[U\mid P]$（2026-11-01：支 5 的 58 例全部踩中；见 [proof/quotient_equivalence](proof/quotient_equivalence/README.md)）|
| **用会解释转义的方式写 `.md` 里的 LaTeX** | `\text`/`\big`/`\ne`/`\notin` 会被写成 TAB/退格/换行，公式静默变形（2026-11-01 在 A2 §34 查出 9 处、历史提交里已存在）。一律用 `write`/`edit` 工具写 md；改完用 `audit_layout` + 肉眼查一次公式 |

### 10.2 有效做法（已验证可用）

| 做法 | 说明 |
|---|---|
| **最大子式的 gcd 判据** | $(5b)\iff$ 全部 $k\times k$ 子式的 $\gcd$ 为常数（[docs/02](docs/02_theorems_proven.md) B.1）|
| **精确单变量消元 / 子式插值** | 把子式插值成多项式，比较 gcd，判定"恒不相容" |
| **带断言矩阵运算** | 每次调用前断言维数 |
| **地基检查** | 任何"等价性"检验必须含至少一个 **True 点**（否则可能空转）|
| **手算最小反例定案** | 推导 vs 数值冲突时的唯一仲裁 |
| **构造实例，不采样** | 如 $L_0=CA^m$ 造 $k\ge2$；块对角/不可见块造中间层 |
| **用 `apply_col(A,Z)`（带方向断言）算 $A\cdot Z$** | 2026-10-30 R16 撤回后加入：[spectral_gcd.py](tools/verification/spectral_gcd.py) 的 `apply_col` 断言 $Z$ 是 $n\times d$；`spectral_gcd_Z` 断言 $CZ=0$ |
| **每个 claim 配 `verify.py`** | 精确算术复核；标注"验证 ≠ 证明" |
| **新推导先用真实实例跑一遍** | 维数计数只给单向结论；把"$\dim\mathrm{Bad}<\dim\mathcal A$"的**逆否**当充要，会写出假定理（2026-10-28：S1 判据被 $n{=}4$ 的精确反例推翻，见 [proof/refuted/S1_criterion_iff.md](proof/refuted/S1_criterion_iff.md)）|


### 10.3 已死的路线（不要在没新想法时重走）

见 [ATTEMPTS.md](ATTEMPTS.md) 与 [archive/attempts_2026-10/q1_true/00_attempts_and_barriers.md](archive/attempts_2026-10/q1_true/00_attempts_and_barriers.md)（约 30 条，各有死因与出处）。

---

## 11. Git 规范

仓库就在项目根（`.git`），全历史可回溯。

### 11.1 配置

```bash
git config core.autocrlf false      # 全仓库 LF（项目文件都是 LF）
```

`.gitignore` 已排除 `__pycache__/`、`*.pyc`、`*.bak`。**PDF 已入库**，不再增加大二进制。

### 11.2 什么时候提交

- **每完成一个命题、或一次有结论的实验，就提交一次**；不要把半天的工作堆成一个提交。
- 提交前必须 `python tools/hygiene/audit_layout.py` **0 issue**。

### 11.3 提交信息格式

```
<类型>：<一句话做了什么>

- 关键结论 1（含验证等级）
- 关键结论 2
- 涉及的文件/目录
```

| 类型 | 用于 |
|---|---|
| `命题` | 新增/修改证明（`proof/`、`docs/02`）|
| `实验` | 测量、反例、证书（`tools/`、`proof/refuted/`）|
| `整理` | 目录、文档、索引（`archive/`、`workspace/`）|
| `修复` | bug、断链、编号错 |
| `快照` | 大范围重构 |

### 11.4 里程碑

每次 $q1$ 有实质推进，打一个 tag：

```bash
git tag -a milestone-20261027 -m "P∈P 完成（递归定理 + O(n^4)）"
git tag                                  # 列出
git show milestone-20261027 --stat       # 看那次改了什么
```

### 11.5 禁令

- ❌ `push --force`（本项目无远端，但纪律照旧）
- ❌ `reset --hard` 丢未提交内容
- ❌ 删除 `trash/` 里的历史文件（它们也在版本控制里；`trash` 是**证据**）
- ❌ 提交密钥、`.venv`、临时大文件

### 11.6 回溯（比 trash 更完整）

```bash
git log --oneline -20                 # 历史
git show <hash>:<path>                # 看某版本的某个文件
git checkout <hash> -- <path>         # 把某文件恢复到某版本
git diff <hash1> <hash2> -- <path>    # 两次提交之间的差异
```

> 记住：`trash/` 是"人肉"回收站，**git 才是真正的历史**。被覆盖的文件优先用 `git checkout` 恢复。



