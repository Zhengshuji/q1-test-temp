# lean/ —— B.2 的 Lean 归档

| 文件 | 内容 |
|---|---|
| `MyProof/PBH.lean` | `Observable`、`pbh_iff`（PBH）、`pbh_exists_eigenvector` |

```bash
wsl -e bash tools/lean/check_lean.sh
wsl -e bash -lc "cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/PBH.lean"
```
