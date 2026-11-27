# 389 Lean 现状盘点：本文、两篇姊妹稿、与 GitHub artifact 仓库

> **2026-11-19 更新（用户指认后核实）**：GitHub artifact 仓库是
> `C:\Users\26074\Desktop\工作 学习（待办）\q1-functional-observer`
> （remote `git@github.com:Zhengshuji/q1-functional-observer.git`）。WSL 的
> `~/WorkSpace/lean4/Q1Paper` 是它的**工作源**，仓库 `Q1Paper/` 是**逐字节镜像**（29 模块，实测一致）。
> 该仓库覆盖**两篇姊妹稿（Paper I / II）**；本文（超平面层）**不在其中**。
> 另：仓库内 `tools/lean/MyProof/` 已清空，253 个文件移入 `trash/lean_removed_2026-11-19/`
> （按 CLAUDE.md §6 的"Lean 只存在 WSL"）。

## 目标

用户问两件事：**（1）** 本文（超平面层论文）的内容有没有 Lean 验证；**（2）** WSL 里那个
`Q1proof`/`Q1Paper` 是不是与本项目/两篇论文配套、更干净、且上传到 GitHub 的库，有什么约定，
能不能在里面找到另外两篇 paper 对应的 Lean。

## 设想与理由

如果 `Q1Paper` 真是"上传版"，那么它应当是**唯一事实来源**，仓库里的 `tools/lean/MyProof` 只是备份；
反之若它是另一条支线的产物，就不能拿它来声称本文有 Lean。所以先做**实测**（能否构建、公理是否干净、
模块名是否对应论文引理），再谈覆盖。

## 做法

1. 在 WSL 里定位候选：`~/WorkSpace/lean4/Q1Paper`（28 模块，2026-11-17 最新）、
   `~/WorkSpace/lean4/MyProof`（老工程，107 文件）、`~/qproof`（只有 `Foundations.lean`）。
2. 实测 `Q1Paper`：`bash scripts/check.sh`（= `lake build Q1Paper` + `lake env lean Q1Paper/Audit.lean`）。
3. 读它的 `lakefile.toml`、`lean-toolchain`、`Audit.lean`、各模块 docstring，抽出命名约定。
4. 与仓库内 `tools/lean/MyProof` 及 `STATEMENT_MAP.md` 对账，判断本文的结果覆盖情况。
5. 用关键词（`Grassmann`、`parameteriz`、`fullRank`、`eigen`）在 `Q1Paper` 里检索本文的核心概念。

### GitHub artifact 仓库（已核实）

`q1-functional-observer` 的 `paper/` 里是 `paper_I_dec.tex/pdf`、`paper_II_minorder.tex/pdf`、
`q1_parametric_algorithms.tex/pdf` 与 `paper/LEAN_MAP.md`（映射 + gap 清单）；`verification/` 是
`c311–c329` 有限精确检查脚本 + 一张"脚本 → 论文位置"表；`.github/workflows/build.yml` 三个 job
（lean: build + axiom audit；paper: 编译 `q1_parametric_algorithms.tex`；verify: 跑三个脚本）；
LICENSE 双许可（代码 MIT / 论文 CC BY 4.0）。

**约定五条**：① Lean 源在 WSL、仓库只做镜像（必须逐字节一致）；② 一模块一条论文引理，
namespace 用 `Q1Paper`/`Q1Subspace`/`KappaObs`；③ `Audit.lean` 做 `#print axioms`（52 条声明，
只有 `propext`/`Classical.choice`/`Quot.sound`）；④ verification 脚本命名 `cNNN_topic.py`，
先打印实例并断言不变量，README 表同步论文编号；⑤ README 的 "What is verified, and how" 表 +
`paper/LEAN_MAP.md` 是"证据 → 论文位置"的登记处。

**本文并入该仓库所需**：`paper/hyperplane_layer.tex` + pdf；`Q1Paper/HyperplaneDirection.lean`
与 `HyperplanePrescribed.lean`（若形式化）；`verification/c330_*.py`（把 c356/c357 的证书搬过去）；
README 表与 `LEAN_MAP.md` 加 Paper III 一节；CI 的 paper job 增加一次编译。

## 进展

### 结论

| 库 | 位置 | 内容 | 与本文的关系 |
|---|---|---|---|
| 论文本体 | `paper/hyperplane/` | **无 Lean** | 全部定理是纸面证明 |
| 仓库内备份 | `tools/lean/MyProof/`（66 文件） | c=1 线做过的 **5 条**声明（PropC 3 + Quad 2） | 只有 attempts/344 支线的**工具内核** |
| **干净库（WSL）** | `~/WorkSpace/lean4/Q1Paper`（28 模块） | 按**论文引理编号**组织：Lemma A/B/C/D/F、G2–G5、阶界 | **不含本文的超平面层结果** |
| 老工程（WSL） | `~/WorkSpace/lean4/MyProof`（107 文件） | 历史混合库；`Q1Paper` 的 Mathlib 走它 | 同上 |
| 空壳 | `~/qproof/QProof` | 只有 `Foundations.lean` | 早期未成形的尝试 |

**`Q1Paper` 确实是干净版，但它对应两篇姊妹稿，不是本文。** 本文的三条核心结果**没有 Lean**。

### `Q1Paper` 实测与约定

- **构建通过**：`scripts/check.sh` **exit=0**；`Audit.lean` 的 `#print axioms` 输出只有
  `propext`、`Classical.choice`、`Quot.sound`，**无 `sorryAx`**。
- **模块名 = 论文引理**：`Compression`=Lemma A、`FreeRows`=Lemma B、`FixedOrder`/`RankConsistency`=Lemma C、
  `SpectralCertificate`=Lemma D、`FPT`=Lemma F、`G2Assembly`/`G3Adjugate`/`G3LeftInverse`/`G3Coeff`=G3 组、
  `G4RankIdentity`、`G5GramRank`、`DegreeBounds`、`HyperplaneAvoid`（**注意：这是"超平面不可覆盖"的线代原语，
  不是本文的超平面层**）、`BezoutDeg`、`BoundLower`/`TightDim`=Paper II 的阶界 $\omega+1\le\dim W\le2\omega$。
- **配置**：`lakefile.toml`（`lean_lib Q1Paper`，Mathlib 走 `../MyProof/.lake/packages/mathlib`）、
  `lean-toolchain`=`leanprover/lean4:v4.35.0`。
- **约定四条**：① 一模块一条论文引理，模块名用引理的字母标号；② 全部 `namespace Q1Paper`；
  ③ `Audit.lean` 汇总 + 公理审计；④ `scripts/check.sh` 一条命令跑"构建 + 审计"。
- **缺**：`.git`（本地无 git 元数据 ⟹ **无法确认远端**）、README、CLAIMS 对照表。

### 本文目前的 Lean 覆盖

`tools/lean/MyProof/` 中、已在 `STATEMENT_MAP.md` 登记的 c=1 线声明共 5 条（均来自 attempts/344）：
`propC_rank_identity`、`propC_consequence`、`rank_drop_of_mem_common`（秩恒等式与零频障碍）、
`exists_sq_eq_of_isAlgClosed`、`quadratic_has_root`（Theorem B 的取根一步）——**都是工具，不是本文定理**。

| 本文结果 | 可形式化 | 难度 | 需要什么 |
|---|---|---|---|
| 方向定理（$Mv=\mu v$ ⟺ 两泛函比例） | **可**，纯线代 | 低 | 正交投影、商、泛函比例性 |
| 引理 4（$V_0\subseteq U_v^\perp$ 自动、$\delta$ 与 $v$ 无关） | **可** | 低 | 维数公式 |
| 引理 6（常秩 + 纤维 = Grassmann） | 部分 | 中 | Mathlib 无"相对丛"，以维数+非空条件代替 |
| 满秩引理 | 部分 | 中高 | 多项式次数与首项系数 |
| 定理 7（参数化） | 不适合 | 高 | 需相对丛的一般概念 |
| 定理 24（位复杂度） | 不适合 | 极高 | 位模型不在 Mathlib 范围 |

## 最终结论

1. 本文**没有核心 Lean**；只有 5 条工具引理。
2. `Q1Paper` 是"干净版"，但覆盖的是**两篇姊妹稿**，且**本地无 git 元数据**，无法证实"已上传 GitHub"。
3. 值得形式化的只有**方向定理**与**引理 4**（各一个模块），加上满秩引理的**代数内核**。

## 放弃原因

- 没有在本轮就动手写本文的 Lean 模块（先要用户确认是否要并入 `Q1Paper`、是否重新 `git init`）；
- 没有确认 GitHub 远端（本地无 `.git`，需要用户给地址或授权 clone）。

## 残留价值

- 一张**三库对照表**与 `Q1Paper` 的**四条约定**（后续新增模块可照抄）；
- 本文结果的**可形式化排序**（先方向定理与引理 4，其余不划算）；
- 明确了 `HyperplaneAvoid` 与本文"超平面层"**同名不同物**，避免后续误引。

## 相关文件

- WSL：`~/WorkSpace/lean4/Q1Paper`（28 模块 + `Audit.lean` + `scripts/check.sh`）
- 仓库：[tools/lean/STATEMENT_MAP.md](../../../../tools/lean/STATEMENT_MAP.md)、[tools/lean/MyProof](../../../../tools/lean/MyProof)
- 论文：[paper/hyperplane](../../../../archive/paper_drafts/paper_III_workspace_2026-11/hyperplane)
- 本轮实测日志：`/mnt/c/Windows/Temp/q1paper_check.log`（WSL 侧）
