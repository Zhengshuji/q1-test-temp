# lean/ —— B.4 的 Lean 归档

> 归档目录；源文件由 [tools/lean/check_lean.sh](../../../tools/lean/check_lean.sh) 收集后统一编译。

## 1. 文件

| 文件 | 内容 |
|---|---|
| `MyProof/B4FullSpace.lean` | `b4_finrank_iff`（对偶维数判据）、`b4_iff_no_eigenvector`（陈述本身）|

依赖 `MyProof.Prelude`。

## 2. 编译

```bash
wsl -e bash tools/lean/check_lean.sh
# 或单文件：
wsl -e bash -lc "cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/B4FullSpace.lean"
```

## 3. 覆盖范围

| 命题 | Lean |
|---|---|
| $\dim(ME+J)=n\iff\ker M^{\mathsf T}\cap J^{\perp}=0$ | ✓ `b4_finrank_iff` |
| "无 $K$ 里的左特征向量" | ✓ `b4_iff_no_eigenvector`（写成 $\varphi\circ(\lambda I-A)=0$）|
| $\forall\lambda$ | ✗ 纸面（逐点取交）|
