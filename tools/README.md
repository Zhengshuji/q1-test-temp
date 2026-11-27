# tools/ —— 工具

> **用法（2026-11-26）**：先按**应用场景**查下表；场景里没有，再按类别目录找。
> 别的方向要用同类工具时，**先来这里找**，找不到再去对应方向的 `attempts/` 看有没有可参考的实现，
> 最后才新写；新工具一律进类别目录，并在本文件登记。

## 场景索引

| 你要做什么 | 先去哪 | 入口 |
|---|---|---|
| 判定一个具体实例是否满足 $(5a)/(5b)$ | `verification/` | `c164_trusted_baseline.py`（有理数精确） |
| 查所有已知实例的公式判定 | `ledger/` | `c189_ledger.py` |
| 枚举 $d$ 维商空间里的层、求可达 $(\rho,c)$ | `layer_search/` | `c192_reduced_search.py` |
| 算 $P$ / 要一个可行见证 | `p_algorithm/` | `c195_P_q.py`、`c197_P_witness.py` |
| 生成/核验证书（JSON + 精确复核） | `certificates/` | `c190`、`c191` |
| 需要带维数断言的精确线代 | `exact_linalg/` | `audit_independent.py`、`linalg_q.py` |
| Lean 编译 / 公理审计 / 声明对照 | `lean/` + WSL | `check_lean.sh`、`STATEMENT_MAP.md` |
| 仓库卫生（布局、断链、撤回、声明覆盖） | `hygiene/` | `audit_layout.py` 等四道门 |
| DSH 写作/代理预设 | `presets/` | `academic-writing/` bundle |

## 类别

| 目录 | 内容 |
|---|---|
| `exact_linalg/` | 有理数精确线代层（带维数断言/残差校验；被其他脚本 import） |
| `verification/` | 实例级精确判定（可信基线、旧验证器、谱 gcd 等） |
| `ledger/` | 唯一账本：所有已知实例 + 公式判定 |
| `layer_search/` | 商空间里的层枚举与可达集 |
| `p_algorithm/` | $P$ 的算法、见证、反例 |
| `certificates/` | 证书生成与核验 |
| `lean/` | Lean 驱动脚本与声明映射（**源在 WSL**，见下） |
| `hygiene/` | 布局/断链/撤回/声明覆盖审计 |
| `presets/` | DSH agent preset（学术写作） |

## Lean 4 + Mathlib（共用 WSL 环境）

| 项 | 值 |
|---|---|
| 工程 | WSL `~/WorkSpace/lean4/MyProof` —— **项目共用的 Lean 环境**（Paper I/II 的 `Q1Paper` 是另一个工程） |
| 工具链 | `leanprover/lean4:v4.35.0` |
| Mathlib | 已预构建 |
| 单文件 | `wsl -e bash -lc 'cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MyProof/X.lean'` |
| 整图 | `lake build MyProof`（必须 exit=0） |

**注意**：Lean 源只在 WSL，仓库里**不存 Windows 备份**（旧的 `tools/lean/MyProof/` 已移入
`trash/lean_removed_2026-11-19/`）。

## 维护规则

1. 新脚本进**类别目录**，不放 `tools/` 根；文件名保留 `cNNN_` 编号（若来自某条 attempt）。
2. 登记到上面的**场景索引**（一行场景 + 一行类别），否则别人找不到。
3. 脚本要自包含（纯 Python + `fractions.Fraction`）；用 CAS 的必须在文件头注明可靠性条件。
4. 被别的脚本 `import` 的模块放 `exact_linalg/`，不要放 `verification/`。
