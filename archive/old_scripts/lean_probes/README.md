# lean/ —— Lean 草稿与 API 探针

> **用途**：放**尚未定型**的 Lean 草稿与 Mathlib API 探针（`#check` 批量）。
> **定型后**移入 `tools/lean/MyProof/`（正式模块，需通过回归）。

## 1. 现有文件

| 文件 | 内容 | 状态 |
|---|---|---|
| `A3quot.lean` | 商之商 $(M/S)/(G/S)\cong M/G$ 的 **LinearEquiv** 草稿（`liftQ` 两次）| 未完成（API 名未对上）|
| `p3_probe.lean` | `Submodule.comap_subtype_self` 等 API 探针 | 一次性探针 |

## 2. 正式模块在哪

`tools/lean/MyProof/`（**15 个文件，全绿**，回归脚本 `tools/lean/check_lean.sh`）：

| 文件 | 内容 |
|---|---|
| `TheoremC/D/E` | 结构定理 |
| `QuotientPencil` | 商铅笔恒等式第一步 |
| `CoreLemma` | $\ker(CAZ)=Z\cap\mathcal V$ |
| `ExistsRLemmas` | 左逆 ⟹ 单射 |
| `A2`／`A2dim`／`A2root`／`A2prop3` | 核障碍、维数核心、根存在、$p_u$ 的二分 |
| `A3`／`A3id`／`A3sem` | $k\le r$、$(k,\ell)$ 恒等式、模律 + 加性/减法形式 + **商之商维数** |
| `R17Cert` | 显式左逆证书 |
| `G4` | 实点反例（平方和）|

## 3. 待办

| 编号 | 任务 | 卡点 |
|---|---|---|
| L-1 | 语义同构的**显式类型组装**（把 $A(S)+S+G$ 写成 Lean 项，套 `finrank_quotQuot`）| 机械工作，非数学 |
| L-2 | 系数空间判据的 Lean 化 | 需要 Grassmannian/Plücker 的形式化，成本高 |

## 4. 环境

- WSL：`~/WorkSpace/lean4/MyProof`；工具链 `leanprover/lean4:v4.35.0`（Mathlib 已预构建）
- 单文件：`wsl -e bash -lc 'cd ~/WorkSpace/lean4/MyProof && /home/zsj/.elan/bin/lake env lean MyProof/X.lean'`
- 回归：`wsl -e bash tools/lean/check_lean.sh`（必须 LF 换行）
- **Unicode 陷阱**：Lean 文件用 `write` 工具写，或先写 `workspace/` 再 `cp` 进 WSL

## 5. 进展（分支 3，2026-11-01）

**D-5 完成一半**（`A3sem.lean` 新增）：

```lean
theorem finrank_map_mkQ_add (A : W →ₗ[K] W) (S G : Submodule K W) :
    finrank (map (mkQ G) (map A S)) + finrank G = finrank (map A S ⊔ G)
```

即 **$\ell$ 的语义形式**：$\dim\phi(S)=\dim(A(S)+G)-\dim G$。
把纸面的"第二同构"落成**维数恒等式**，不需要构造 `LinearEquiv`。**回归 16 文件全绿** ✓

**未完成**：完整的 $\dim(T_S\cap B_S)=k-\ell$（一次尝试因三处类型不匹配失败，已回滚；
下一步按"两处 `finrank_map_mkQ_add` + 秩-零化度"重写）。

