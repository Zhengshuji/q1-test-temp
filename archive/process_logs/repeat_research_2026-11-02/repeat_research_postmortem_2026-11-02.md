# 重复研究事故分析（2026-11-02）

> 用户指出："这已经不是第一次犯重复研究的问题了，仔细检查一下问题到底出在哪里，后续怎么避免。"
> 本文逐条列出**本会话实际发生的重复**、证据位置、根因（组织性 / 个人习惯）、以及**已落地**的防复发措施。

## 1. 本会话实际发生的重复（有证据）

| # | 我做的事 | 早已存在的东西 | 证据 |
|---|---|---|---|
| P1 | 把"$(5a)$ 不是硬度来源"当成新发现写进报告（Workstream A/B 的动机段）| `proof/5a_archive/README.md`（2026-10-21）已写："**$(5a)$ 必要但多项式；$(5b)$ 必要且未证（谱条件）。硬度在 $(5b)$**" | `proof/5a_archive/README.md` 第 1 节 |
| P2 | 推导 $LA=\Lambda L+G_0C+G_1CA$ 并把它当作 B.7 第 1 步的关键 | 同一文件给出**三种等价形式**，且已被 **Lean 证明**：`proof/5a_archive/lean/ABridge.lean`（秩形式 $\iff$ 分解）、`Factor.lean`（分解 $\iff$ 三核包含，含通用引理 `exists_comp_eq_of_ker_le`）| 同上 `lean/` |
| P3 | 写 `KronFactor.kron_block_factor`（Lean）证"分块恒等式第一行" | 与 P2 的 `ABridge`/`Factor` **同内容**，而且旧的更强（线性映射形式、秩形式 $\iff$ 分解）| `tools/lean/MyProof/KronFactor.lean` vs `proof/5a_archive/lean/*.lean` |
| P4 | 把 $Q_L=P(\lambda)H$ 当作 B.7 的新步骤 | `proof/5b_upper_bound/README.md`（2026-10-21）已用**同一个**铅笔因子化 $P=(\lambda I-\Lambda)H$ 证明上界 | `proof/5b_upper_bound/README.md` |
| P5 | 花了整轮论证"$(5b)\iff$ 无正则初等因子 / Kronecker 型条件"是"新框架" | `proof/layer_program/RESTRICTED_COMPLETION_MODEL.md` §2 已写："$(5b)\iff$ 无有限初等因子 $\iff$ 无正则块" | 该文件 §2 |
| P6 | Workstream A 的"$\mathcal A_{\min}$ 不是仿射"当成新发现 | `proof/spectral_locus/README.md` 已记录 O1 的更正："**仿射簇的投影一般不必闭**（例 $\{(\theta,\lambda):\theta\lambda-1=0\}$）"，并说明 $(14b)$ 要按 constructible 处理 | `proof/spectral_locus/README.md` 开头 |
| P7 | 把"Kronecker 结构"当成全新的 Workstream B 开工 | `proof/README.md` 的"命题关系"表已把 `pencil_equivalence` → `5b_upper_bound` → `dec_q_existsR` → `h_bound` 的依赖关系画清；`h_bound` 已给"不能只用整数条件"的结构障碍 | `proof/README.md` |

**净结论**：本会话的**真正新增**只有 B.6、B.7、B.8、descriptor 约化、observability_chain 与对应工具；
其余"发现"至少有 7 处是重复。用户的批评成立。

## 2. 根因

### 2.1 组织性根因（主要）

**C1：读档协议漏了 `proof/` 树。**
`CLAUDE.md` §7 第 17 条写的是"`CLAUDE → README → STATUS → ATTEMPTS → archive/expert_correspondence → workspace/*/attempts/`"——
**完全没有 `proof/README.md` 与 `proof/*/README.md`**。即使严格照做，也读不到 `5a_archive`、`5b_upper_bound`、`h_bound`。

**C2：`proof/README.md` 的目录表本身不全。**
实际有 34 个子目录，表里只列了 19 个；漏掉的包括 `quotient_equivalence`、`layer_31_theorems`、
`base_family`、`incidence_strata`、`global_incidence`、`PCC`、`bivector_r2`、`xw_decomposition`、
`d0_boundary`、`h2_dim_arithmetic`、`cyclic_vector_criterion`、`b4_full_space`、`kron_null_module`、
`t4b_infinite_divisors`、`descriptor_reduction`、`observability_chain`。

**C3：`STATUS.md` 只保留最近 2–3 轮。**
旧的关键结论（2026-10-21 的 `5a_archive` / `5b_upper_bound`）不在 STATUS 里 ⟹
"读了 STATUS"$\ne$"知道现状"。这是**信息架构**问题，不是记忆问题。

**C4：没有"命题级"的可检索索引。**
`ATTEMPTS.md` 是**路线**表（方向｜文件｜状态），`docs/02` 是**命题**表但缺反查链接，
`proof/` 是**证明**树但目录名不总是命题名。三者之间没有机器可查的映射。

### 2.2 个人习惯根因

**C5：我按"自己新造的名字"检索，而不是按"命题的形状"检索。**
我搜的是 `T4-b`、`d_infty`、`descriptor`、`Kronecker`——这些是我**发明**的记号；
而 archive 里存的是 `(5a)`、`row(LA)`、`Λ`、`(λI-Λ)H`、`初等因子`。
**教训与 2026-10-28 那次（漏掉 Löfberg）同型**：按对象名检索会漏，必须按**决策问题的形状**检索。

**C6：把"专家给的新工作流"当成"新地"。**
专家说"Workstream B：Kronecker 结构"，我就当成绿地开工，
没有把它对回 `proof/README.md` 的关系表（那里已经写着"$5b$ 上界/下界/结构障碍"三块）。

**C7：STATUS 的"最新块"给了虚假的完整感。**
我每轮都更新 STATUS 顶部，却没读它的历史部分；于是"我写的 STATUS"取代了"项目的历史"。

## 3. 已落地的防复发措施

| 措施 | 实现 | 状态 |
|---|---|---|
| **V1 命题索引 + 检索** | `tools/hygiene/claim_index.py`：抽 4 类来源（proof/*/README、docs/02、docs/03、ATTEMPTS）成 `workspace/inventory/claims.tsv`（**152 条**），支持 `--grep`、`--check` | ✅ 已实现并跑通 |
| **V2 修读档协议** | `CLAUDE.md` §7.17 增加 `proof/README.md` 与 `python tools/hygiene/claim_index.py`；新增规则 22（见下）| ✅ 本轮改 |
| **V3 补齐 proof/README 目录表** | 34 个目录全部列入（本轮补）| ✅ 本轮改 |
| **V4 STATUS 顶部固定一行** | "完整命题清单见 `workspace/inventory/claims.tsv`（`claim_index.py --grep`）" | ✅ 本轮改 |
| **V5 开工前"按形状检索"** | 新规则 22：每个新命题/新路线开工前跑 2–3 个**形状级**查询，把命中写进 attempt 文档的"先前工作"小节 | ✅ 写进规范 |
| **V6 提交前闸门（可选开启）** | `python tools/hygiene/claim_index.py --check`：索引比任何 `proof/*/README.md` 旧即退出码 1 | ✅ 可用（未接入强制流程） |
| **V7 事故登记** | 本文 + `workspace/inventory/5b_map.md` §8 的"重复研究教训"段 | ✅ 本轮 |

## 4. 自查清单（写新命题前必跑）

```bash
# 1) 按"命题形状"检索（不是按你新造的记号）
python tools/hygiene/claim_index.py --grep "(5a)|row\(LA\)|Lambda|因子化|初等因子"
python tools/hygiene/claim_index.py --grep "Smith|行列式因子|gcd"
python tools/hygiene/claim_index.py --grep "可控性|descriptor|Kronecker"

# 2) 若命中 proof/ 目录，先读它的 README 再决定是否重复
# 3) 把命中与"为什么不是重复"写进 attempt 文档的「先前工作」
```

## 5. 一句话

> **重复研究的根因不是"忘了"，而是"读档协议不覆盖 proof/、且没有命题级索引"。**
> 现在补上了：`claims.tsv`（152 条）+ `proof/README.md` 全目录 + 规范第 22 条。
> 下次开工的正确动作是**先 grep 形状，再读命中目录，最后才写新东西**。
