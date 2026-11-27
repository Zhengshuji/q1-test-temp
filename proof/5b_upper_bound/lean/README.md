# Lean 4 归档：上界相关的最小文件集

这里复制了 `UpperBound.lean` **及其自写依赖**，不是整个 `MyProof` 工程。
`Mathlib` 是外部依赖，未复制。

## 文件

| 文件 | 作用 |
|---|---|
| `MyProof/Theorems/UpperBound.lean` | 本次新增的 5 条上界定理 |
| `MyProof/Theorems/Pencil.lean` | T5′ 恒等式；`T2_pencil_rank` 只是恒等式辅助引理 |
| `MyProof/Theorems/Factor.lean` | `tuple`（**加了 `@[expose]`**）、`tuple_apply`、`decomp_iff_ker` |
| `MyProof/Theorems/ABridge.lean` | $(A)$ 的秩形式 $\iff$ 分解（`decomp_iff_rank`） |
| `MyProof/Theorems.lean` | **归档用的最小根文件**：只 import 上面四个模块 |

## 依赖链

```
Mathlib
  └─ Pencil.lean      （T5′；T2 辅助）
  └─ Factor.lean      （tuple / tuple_apply / decomp_iff_ker）
       └─ ABridge.lean（(A) 秩形式 ⟺ 分解）
            └─ UpperBound.lean
                 ├─ pencil_upper_bound
                 ├─ pencil_upper_bound_mul
                 ├─ pencil_upper_bound_linear
                 ├─ upper_bound_of_decomp
                 └─ upper_bound_of_rank_eq   （端到端：抽象 (5a) ⟹ 上界）
```

## 如何编译

在已有 Lean 4 + Mathlib 工程中：

1. 把 `MyProof/Theorems/{Pencil,Factor,ABridge,UpperBound}.lean` 复制到工程的
   `MyProof/Theorems/` 下（覆盖同名文件）；
2. 确保 `MyProof/Theorems.lean` 里有
   `public import MyProof.Theorems.UpperBound`；
3. 运行：

```bash
export PATH="$HOME/.elan/bin:$PATH"
cd <工程根目录>
lake build
```

本次在 `~/WorkSpace/lean4/MyProof` 上实测：
`Build completed successfully (18136 jobs)`。

## 注意

- `Factor.lean` 里 `tuple` 的 `@[expose]` 和 `tuple_apply` 是 `upper_bound_of_decomp`
  能展开 `tuple` 的前提；只复制 `UpperBound.lean` 会编译失败。
- `Theorems.lean` 是**最小**根文件；实际项目的同名文件还 import 了
  `CaseII`、`Spectral`、`C6` 等许多模块，这里刻意省略。
- `T2_pencil_rank` 只证明“两边是同一个矩阵”，**不是**完整 T2，也不是上界；
  真正的上界是 `UpperBound.lean` 里的定理。
- 本归档是 2026-10-21 的快照；以 `scripts/lean/` 与 WSL 工程为准。
