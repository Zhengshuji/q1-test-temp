# lean/ —— B.5 的 Lean 归档

> 归档目录；源文件由 [tools/lean/check_lean.sh](../../../tools/lean/check_lean.sh) 收集后编译。

| 文件 | 内容 |
|---|---|
| `MyProof/CyclicVector.lean` | `cyclicSpan`、`mem_cyclicSpan_self`、`map_cyclicSpan_le`、`isCyclic_iff`、`ker_invariant_of_left_eigen`、`ker_ne_top_of_left_eigen`、`not_cyclic_of_left_eigen` |

```bash
wsl -e bash tools/lean/check_lean.sh
wsl -e bash -lc "cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/CyclicVector.lean"
```
