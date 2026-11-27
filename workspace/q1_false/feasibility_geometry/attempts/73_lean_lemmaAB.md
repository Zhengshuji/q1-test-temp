# Lemma A / Lemma B 的 Lean 内核（两个文件，0 error 0 warning）

## 目标

用户问：Lemma A（下界可加）与 Lemma B（上界可加）是否经过 Lean 验证？此前只有 L1（纸面）+ L2（精确计算）。
本轮补 Lean 内核。

## 设想与理由

两条引理各自有一个**抽象线性代数核**，它们才是承重的部分：

* **Lemma A 的核（避免性）**：若 $V\cap K'=0$、$Z\le K'$ 非零、$\varphi:V\to K'$ 满射，则存在 $x\in V$
  使 $\varphi x\in Z$ 而 $x\notin Z$。这正是"每个 $\mathcal Z$ 都被打到"的机制（取 $z\in Z\setminus0$，
  原像 $x$；若 $x\in Z$ 则 $x\in V\cap K'=0$，矛盾）。
* **Lemma B 的核（秩可加）**：直和映射 $\varphi\oplus\psi$ 的像的维数 $=$ 两者之和。
  这是"块对角增广的 $(5a)/(5b)$ 按块相加"的全部内容。

## 做法

1. `tools/lean/MyProof/LemmaA.lean`：`LemmaA.exists_witness_not_mem`（及加强版 `exists_witness_not_mem'`，
   含 $x\ne0$）；
2. `tools/lean/MyProof/LemmaB.lean`：`LemmaB.finrank_range_prodMap`（及 $\le$ 形式
   `finrank_range_prodMap_le`），用 `LinearMap.range_prodMap` + `Submodule.prodEquiv` + `Module.finrank_prod`；
3. 在 WSL 树（`~/WorkSpace/lean4/MyProof/MyProof/`）用 `lake env lean` 逐文件编译，日志重定向到文件再读；
4. 登记 `tools/lean/STATEMENT_MAP.md`（含"差异"）与 `proof/lean_coverage.md`；docs/02 B.15 的等级加
   `[Lean 内核]`。

## 进展

| 文件 | 声明 | 编译结果 |
|---|---|---|
| `LemmaA.lean` | `exists_witness_not_mem`、`exists_witness_not_mem'` | **exit=0，0 error 0 warning** |
| `LemmaB.lean` | `finrank_range_prodMap`、`finrank_range_prodMap_le` | **exit=0，0 error 0 warning** |

闸门：`audit_lean_statements` **163 声明 / 61 文件 / 152 条目 / 0 问题**；
`audit_lean_coverage` **48/48 / 0 不一致**。

踩过的坑（记录备查）：

* `write` 工具**不能**直接写 `\\wsl$\...`（9P 上 rename 失败，ENOTSUP）⟹ 先写 Windows 的
  `tools/lean/MyProof/`，经 `C:\Temp`（ASCII 路径）`cp` 进 WSL；
* `import Mathlib.LinearAlgebra.Basic` 之类的**子模块**在本树的 `.olean` 不存在 ⟹ 一律 `import Mathlib`；
* Mathlib 里**没有** `Matrix.rank_fromBlocks` / `Submodule.finrank_prod` / `LinearMap.finrank_range_prodMap`
  （探测确认）⟹ 秩可加要用 `Submodule.prodEquiv` + `Module.finrank_prod` 组合；
* `Submodule.prodEquiv` 的第一个显式参数是**子空间**不是域。

## 最终结论

1. **Lemma A、Lemma B 都有了 Lean 内核**（各 2 条声明，均 0 error 0 warning）；
2. **差异必须一起读**：Lean 证的是抽象核——"满射 + 交集为零 ⟹ 见证"与"直和映射秩可加"；
   $(\lambda_0I-A)|_V$ 的实例化、$k$ 重直和的矩阵记账、矩阵 `fromBlocks` 的桥仍是纸面（L1）；
3. 因此 B.15 的等级写法是 **[已证-纸面] + [Lean 内核] + [精确验证]**，与项目纪律一致。

## 放弃原因

不适用。

## 残留价值

* 两个可复用的 Lean 内核（含"差异"登记），后续任何"直和/避免性"论证可直接引用；
* 一条 WSL 写入与 Mathlib 命名的实操记录，避免重复踩坑；
* 使 B.15 成为本项目**第 25 条**带 Lean 内容的命题。

## 相关文件

- `tools/lean/MyProof/LemmaA.lean`、`tools/lean/MyProof/LemmaB.lean`（与 WSL 树一致）
- `tools/lean/STATEMENT_MAP.md`（两条新条目 + 差异）
- `proof/lean_coverage.md`（B.15 行改为 ✓）
- `docs/02` B.15 等级
