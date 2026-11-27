# lean/ —— 投影与压缩工具的 Lean 归档

| 文件 | 内容 |
|---|---|
| `MyProof/ProjW.lean` | `projW`、`projJ`、`projW_add_projJ`、`dualAnnihilator_apply_eq_projW`、`compression`、`compression_sub_mem`、`dualAnnihilator_compression` |

```bash
wsl -e bash tools/lean/check_lean.sh
wsl -e bash -lc "cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/ProjW.lean"
```
