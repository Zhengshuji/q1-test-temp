# lean/ —— H.2 的 Lean 归档

| 文件 | 内容 |
|---|---|
| `MyProof/DimArithmetic.lean` | `no_truncation`、`r_add_t`、`square_iff`、`m_iff_h` |

```bash
wsl -e bash tools/lean/check_lean.sh
wsl -e bash -lc "cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/DimArithmetic.lean"
```
