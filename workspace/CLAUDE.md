# workspace/CLAUDE.md —— 接手须知与避坑清单

> 本文件是**给下一次会话/协作者的操作手册**，不替代根目录的 `CLAUDE.md`（规范）。
> 根 `CLAUDE.md` 讲"项目是什么、怎么组织"；本文件讲"动手时最容易出错的地方"。
> 阅读顺序：根 `CLAUDE.md` → `STATUS.md` → [`ATTEMPTS_INDEX.tsv`](ATTEMPTS_INDEX.tsv) →
> [`q1_true/README.md`](q1_true/README.md) / [`q1_false/README.md`](q1_false/README.md) → 本文件。

---

## 0. 三条铁律（违反任何一条，本轮工作作废）

1. **不把"看起来对"当"已证"**。实验（`[精确验证 n/N]`、随机实例）**永远不计入证明**。
2. **不把"弱于命题的 Lean 内核"记成整条命题的 `[Lean]`**。内核只能记 `[Lean 内核]` 并写明差在哪（根 `CLAUDE.md` §4 硬规则 6）。
3. **不留半成品**。Lean 文件编译不过就删掉，只在卷宗里留"卡在哪、下一步怎么写"；提交信息里写清楚失败原因。

---

## 1. 先查再动手：避免重复劳动

本项目已因"凭记忆/凭摘要开工"重复劳动过 4 次（最严重一次 2026-11-02，见 `archive/process_logs/repeat_research_2026-11-02/`）。

**开工前按顺序查（每项不超过 1 分钟）：**

| # | 查什么 | 命令/位置 |
|---|---|---|
| 1 | 这个命题是否已有卷宗 | `workspace/q1_*/<子方向>/proof/` 与 `attempts/`；总索引 `ATTEMPTS_INDEX.tsv` |
| 2 | 是否已有 Lean 声明 | `tools/lean/STATEMENT_MAP.md`（219 条声明，每条带"对应/差异"）|
| 3 | 是否已有相关工作 | `python tools/hygiene/claim_index.py --grep "<形状词>"`（用**问题的形状**检索，不要用自己新造的记号）|
| 4 | 是否已被推翻 | `proof/refuted/README.md`；`python tools/hygiene/audit_retractions.py` |
| 5 | 是否试过并失败 | `workspace/*/attempts/`；`git log --oneline --all -- <相关文件>` |
| 6 | 是否与文献重复 | `literature/notes/`、`docs/07_literature_review.md`；根 `CLAUDE.md` §3 已把"文献已解决"的部分圈出 |

**判断标准**：如果能把新命题一句话映射到已有序号（如"这就是 B.24 的实例化"），就**不要新开条目**，直接改进已有卷宗。

---

## 2. Lean 4 验证的可靠性：checklist

### 2.1 陈述保真（最容易被忽略，也是本项目踩过的坑）

> **事故**：B.4 的 Lean 内核证的是**对偶写法** $(\dim(M\top+J)=n\iff\ker M^{\mathsf T}\cap J^\perp=0)$，
> 而论文命题是**右特征向量**判据。数学上两条都真，但**不是同一个命题**。
> 机器核验：右特征向量 3962/3962 与铅笔秩降一致，对偶写法 **117 个反例**。

**做法**：
* 写 Lean 前，先把**论文陈述逐字抄到文件头的 docstring 里**，写完再逐词对照一次；
* 对照三点：**量词**（`∀λ` 还是 `∃λ`）、**方向**（$\ker$ / $\operatorname{range}$ / 转置）、**域**（$\mathbb C$ vs $\mathbb R$，代数闭 vs 实）；
* 在 `STATEMENT_MAP` 的"差异"一栏写清：**差哪一步、为什么这一步仍是纸面**；
* 若 Lean 陈述与论文陈述不一致，**改 Lean 或改论文**，不要用"等价"糊过去。

### 2.2 公理与逃逸（escape）

* 每个主要定理都要跑一次
  ```lean
  #print axioms 定理名
  ```
  允许出现的只有 `propext`、`Classical.choice`、`Quot.sound`。出现 **`sorryAx`** 说明有未完成证明。
* **禁用**：`sorry`、`admit`、`axiom` 声明、`unsafe`、`@[implemented_by]`。
* **慎用 `native_decide` / `bv_decide`**：它们把"编译器求值"引入信任基（每次求值对应一条 `Lean.ofReduceBool` 类公理），
  属于"信任编译器"而非"信任内核"。若确要用，必须在卷宗里写明"该步依赖 native 求值"，并尽量改用 `decide` 或显式构造。
* **注意 `#print axioms` 看不到 `simp` 引理里 `@[implemented_by]` 的信任**（Lean 社区的已知盲点）——
  所以**不要给自定义引理加 `@[implemented_by]`**。

### 2.3 环境与版本

* `lean-toolchain` 固定为 `leanprover/lean4:v4.35.0`；Mathlib 由 `lake-manifest.json` 的 commit 固定。
  **不要**在会话中升级 token 链；升级必须单独一轮并重跑全图。
* 编译验证必须用**整图**，不能只 `lake env lean 单文件`：
  单文件编译不检查模块是否在 `MyProof.lean` 的导入图里（本项目的聚合文件是生成的 `MyProof.lean`）。
  ```bash
  # WSL
  cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH"
  lake build MyProof          # 必须 exit=0
  bash scripts/check_rules.sh # 规则门（PASS）
  ```
* **不要用 `module` 系统**：本项目试过，9 个文件因"未标 `public` 不导出"而失败，已回退。
  聚合靠 `MyProof/Blocks/*` + 生成的 `MyProof.lean`，不要改回 `module`。

### 2.4 常见 Lean 4 陷阱（都是本项目实际踩过的）

| 陷阱 | 现象 | 正确做法 |
|---|---|---|
| `ext x j` 复合 | `Function expected at x … type n` | 拆开：`apply LinearMap.ext; intro x; funext j` |
| `rw` 方向错 | `Did not find an occurrence of the pattern` | `set` 引入的缩写，改向用 `← h`，或改用 `simp only [...]` |
| `finrank` 混用 $E$ 与 $E^{**}$ | `omega` 无法关闭、类型不匹配 | 维数计算**全部在同一个空间里做**；跨空间要用显式同构 |
| `Submodule.dualAnnihilator` vs `dualCoannihilator` | 类型落在 $E^{**}$ | $J\le E^*$ 的零化子用 `dualCoannihilator` |
| `by omega` 处理 `finrank (Dual K E)` | 缺 `finrank (Dual K E) = finrank K E` | 先 `have` 这条，再 `omega` |
| 自定义 `gcd` 与 `EuclideanDomain.gcd` | 定义不相等 | 不要依赖定义相等；用整除性 + 代数闭域取根（B.25 的写法）|
| `[DecidableEq K]` 缺失 | `failed to synthesize GCDMonoid K[X]` | 补实例，或改用不依赖可判定性的陈述 |
| 结论里出现 `Finite`/`Fintype` 争议 | 编译过但陈述弱 | 检查是否为 `[Finite m]` 而非 `[Fintype m]`（行数只需有限） |

---

## 3. 命题管理与文档维护

### 3.1 编号

* `docs/02` 的 **29 条主条目**是唯一编号源；`§0.1` 的别名表把 76 个旧编号映射到主条目 + 分部。
  **新增/合并条目必须同时更新 §0.1**，否则 `audit_lean_coverage.py` 的别名对账会失败。
* 卷宗目录名 = 主条目名（旧 `proof/B.9/`）；**2026-11-26 起证明放各子方向的 `proof/`**，
  不再往根 `proof/` 新增。
* 引用旧编号（如 `B.9b`）在正文里仍然合法——别名表保证可检索。

### 3.2 每份卷宗必须有的六节

`## 命题`、`## 纸面证明`、`## Lean`、`## 精确验证`、`## 验证状态`、`## 状态与历史`（`audit_proof_map.py` 会查）。
`## 验证状态` 用 (M, F) 双维 + 完成判定：

```markdown
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准：M≥3 即可；Lean 为加分项）|  —— <Lean 状态> |
```

### 3.3 验收规则（2026-11-07）

> **能用 Lean 就用 Lean；不能或不方便用 Lean 的，接受可信度高的纸面证明**（专家复核 / 论文教材）。
> 纸面可含 Lean 也可不含，**含 Lean 更好**；**Lean 不是硬门槛**；实验不计入证明。

### 3.4 缺口登记

* 任何未闭合的条目必须出现在 `proof/UNFINISHED.md`（当前为空）；
* 写清三件事：**缺什么**（数学 vs 形式化）、**专家给的路**、**工作量预估**；
* 从表里移出时同步改卷宗与 `docs/02` 的等级行。

---

## 4. 提交与卫生

每次有结论就提交；提交前**四道门**全绿：

```bash
python tools/hygiene/audit_layout.py            # 布局/断链 → 0 issue
python tools/hygiene/audit_lean_statements.py   # 声明 ↔ STATEMENT_MAP → 0
python tools/hygiene/audit_lean_coverage.py     # docs 的 [Lean] ↔ 覆盖表 → 0
python tools/hygiene/audit_proof_map.py         # 卷宗 ↔ 索引 ↔ 六节 → 0
```

**踩过的坑（工具层面）**：

| 坑 | 现象 | 做法 |
|---|---|---|
| 文件编码 | `non UTF-8 data` | Python 写文件一律 `encoding='utf-8', newline='\n'` |
| BOM | `invalid literal for int(): '\ufeff28'` | 纯数字/纯 ASCII 文件用 `encoding='ascii'` |
| Python 正则替换串含 `\` | `bad escape \i / \s` | `re.sub(..., lambda _m: repl, ...)`，或先转义 |
| 移动文件后相对链接断 | `audit_layout` 报断链 | 移动后批量重写：把以「右括号 + ../proof/」开头的链接改为「右括号 + ../」；`tools/` 一类前缀改成 `../../tools/`；再跑 `audit_layout` |
| PowerShell 吞 Unicode | 公式变形 | 大段文本用 `write` 工具写文件，别用管道 `Set-Content` |
| 提交信息文件 | 根目录出现非 md | `git commit -F mNNN.txt` 后立刻删除，并单独提交一次"清理" |

**临时文件约定（2026-11-07）**：跨"Windows 仓库 ↔ WSL Lean 工程"的临时文件（探针 `.lean`、驱动 `.sh`、日志 `.log`、一次性脚本）一律放 `workspace/_exchange/`，**不要**用 `C:\Temp`（仓库外、审计看不到、容易积压）。该目录默认不入 git；会话结束清空，仍有价值的结论写进对应卷宗。

**提交信息格式**（根 `CLAUDE.md` §11.3）：`<类型>：<一句话>` + 关键结论（含等级）+ 涉及文件。

---

## 5. 与专家往返的规范

* 每次**只寄一个自包含文件**（`workspace/for_expert/NN_topic.md`），正文**不出现仓库路径、不写日期**；
* 结构：Part I 问题与记号 → Part II 已做的工作（含**更正记录**）→ Part III 请求（具体到"这一行对不对"）；
* 收到答复后：**先归档**（`for_expert/archive/`），再逐条落实，最后在卷宗写 `## 专家复核意见（裁决）`；
* 不要把"专家的客气话"当成"命题已被证明"——只记**明确裁决**（成立 / 有缺口 / 需额外假设）。

---

## 6. 每轮开工/收工的固定动作

**开工（5 分钟）**
1. 读根 `CLAUDE.md` §3（主线定位）与 §4（验收规则）；
2. 读 `workspace/ATTEMPTS_INDEX.tsv` 与 `STATUS.md` 顶部；
3. 选**一个**命题，先在 `claim_index` / `STATEMENT_MAP` / `git log` 里查重；
4. 若涉及 Lean，先确认 WSL 侧 `lake build MyProof` 当前是绿的（改之前先确认基线）。

**收工（10 分钟）**
1. 命题有推进 → 更新所在子方向的 `STATUS.md` / `RESULTS.md` + `docs/02` 等级行；
2. 有失败 → 写进该子方向 `attempts/` 的卷宗"卡在哪"，删掉半成品；
3. 更新 `workspace/ATTEMPTS_INDEX.tsv` 与 `STATUS.md`；
4. 四道门全绿 → 提交（含"清理"提交）；
5. 若与专家往返，把答复归档。

---

## 7. 已知的"不要碰"

| 事项 | 原因 |
|---|---|
| `module` 系统迁移 | 9 个文件失败；需要每个导出声明标 `public`，与生成式聚合冲突 |
| 把 `$(5a)$` 的几何结果写进 `docs/02` 的"结果" | 根 `CLAUDE.md` §3：`$(5a)$` 只作定义域，不作研究对象 |
| 用矩阵层陈述替换抽象陈述（为了省事） | 专家明确：B.4 用抽象求值配对；矩阵化会引入基选择、行/列约定与转置关系四面楚歌 |
| 为了补齐 B.8 而形式化 Smith 形 | Mathlib 无；专家推荐 gcd/Bézout 路线（有限族 gcd 引理 + 子式插值 + 代数闭域取根）|
| 用"线性代数替身"替换 B.13 的射影几何论证 | 那就不是原命题了；宁可停在 F1，也不要改陈述 |
| 删除 `trash/` 与 `archive/` | 它们是证据；git 是历史，trash 是"人肉"回收站（根 `CLAUDE.md` §11.5）|

---

## 8. 可选路线图（不影响当前完成度）

| 事项 | 现状 | 下一步 |
|---|---|---|
| B.4 的 (P) 版内核 | M3/F1，纸面 + 3962/3962 核验 | 四引理 + 自定义 `annihilator`；L1 自写、L2/L3 经 `Module.Dual.evalEquiv` |
| B.8 的 gcd/Bézout | M3/F1 | Layer A 有限族 gcd 引理（$g(\alpha)=0\iff\forall i,p_i(\alpha)=0$）先独立证，再实例化 |
| B.10 / B.14 / B.24 的 Lean | M3/F1 | 各 1 会话；B.24 的商泛性质已完成（`B24Phi`），只差实例化 |
| B.13 的 L3–L5 | M3/F1（纤维代数内核已 Lean 化）| 需射影簇维数与闭像；建议在 `workspace/` 独立立项，勿硬塞进现有卷宗 |
| 旧编号清理 | 76 → 29 已完成 | 若将来再合并，**必须**同步 §0.1 别名表 |
