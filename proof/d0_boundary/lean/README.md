# lean/ —— $d=0$ 边界的 Lean 归档

> 本目录是归档；源文件由 [tools/lean/check_lean.sh](../../../tools/lean/check_lean.sh) 收集后统一编译。

## 1. 文件

| 文件 | 内容 |
|---|---|
| `MyProof/D0Boundary.lean` | `d0_rank_nullity`（秩-零化度）、`d0_rank_iff`（$\dim T(V)=\dim V\iff V\cap\ker T=\bot$）、`d0_forall`（$\forall\lambda$ 版）|

## 2. 编译

```bash
wsl -e bash tools/lean/check_lean.sh                                   # 全量
wsl -e bash -lc "cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/D0Boundary.lean"
```

## 3. 覆盖范围

| 命题 | Lean 覆盖 |
|---|---|
| $(S)\iff V\cap\ker(\lambda I-A)=0$（逐 $\lambda$）| ✓ `d0_rank_iff` |
| 对**所有** $\lambda$ | ✓ `d0_forall` |
| "$A$ 在 $V$ 里没有特征向量"这个说法 | ✗ 纸面（定义层）|
| 第二个实例无解 | ✗ 精确验证（`check_qmin5.py`），非 Lean |
