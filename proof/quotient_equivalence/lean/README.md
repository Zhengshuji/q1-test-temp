# lean/ —— 商等价定理的 Lean 归档

> **本目录是归档**：源文件与 `~/WorkSpace/lean4/MyProof/MyProof/` 的副本一致，
> 由 [tools/lean/check_lean.sh](../../../tools/lean/check_lean.sh) 收集后统一编译。

## 1. 文件

| 文件 | 内容 |
|---|---|
| `MyProof/QuotientEquivalence.lean` | Theorem Q 的四条：`qe_colspace`、`qe_finrank`、`qe_well_defined`、`qe_full` |

依赖共享引理 `MyProof.Prelude`（`finrank_inter_add_finrank_map_mkQ`），见 [tools/lean/MyProof/Prelude.lean](../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/Prelude.lean)。

## 2. 编译

```bash
# 从仓库根
wsl -e bash tools/lean/check_lean.sh          # 全量（40 文件）
```

单文件（把源文件拷进 WSL 工程后）：

```bash
wsl -e bash -lc "cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/QuotientEquivalence.lean"
```

## 3. 覆盖范围（诚实）

| 命题 | Lean 覆盖 |
|---|---|
| H.1 陈述本身 | ✓ `qe_full` |
| 证明第 2 步（列空间模 $S$）| ✓ `qe_colspace` + `qe_well_defined` |
| 证明第 4 步（维数记账）| ✓ `qe_finrank` |
| "$r+t$" 与 "$\dim((V+Z)/S)$" 的相等 | ✗ 纸面（[02_证明.md](../02_证明.md) §1 第三步）|

逐条对照见 [tools/lean/STATEMENT_MAP.md](../../../tools/lean/STATEMENT_MAP.md)。
