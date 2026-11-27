# paper_rewrite — 论文 v2 重组的脚本与快照

> 2026-11-10。这里是 Phase 2（结构重排）的**一次性迁移工具**与当时的产物快照。
> 正式论文仍是 [paper/current/others/q1_parametric_algorithms.tex](../../paper/current/others/q1_parametric_algorithms.tex)，
> 本目录的 `v2_snapshot.tex` **不是**事实来源，只在 v2 尚未转正时用于回退与对比。

## 文件

| 文件 | 作用 |
|---|---|
| `assemble_v2.py` | 按 `\section` 切块重排：9 节 + 1 附录；Literature Review 插为 §II；旧附录 A 的 A.1–A.5 拆开并回 III/IV/V/VII；旧附录 C 删除；参考文献移到末尾；修正 `Appendix A.1/A.5/B` 的悬空引用 |
| `equations_v2.py` | 给 (5a)、(5b)、(R0)、(B.1)、(B.2) 加真正的 `\tag` + `\label`；正文 76 处手打引用改 `\eqref` |
| `v2_snapshot.tex` | 上述两步之后的产物（12 页、0 error、0 overfull、0 undefined、0 重复标签） |

## 复现

```text
python workspace/paper_rewrite/assemble_v2.py     # 需要 paper/lit_review_draft.tex
python workspace/paper_rewrite/equations_v2.py    # 就地修改 paper/v2_test.tex
cd paper && pdflatex v2_test.tex && pdflatex v2_test.tex
```

（脚本里的路径是相对仓库根写的；`paper/v2_test.tex` 在 `.gitignore` 里。）

## 转正前还差

1. 54 个行间公式改嵌入（[paper/display_math_audit.md](../../trash/paper_root_2026-11-21/display_math_audit.md) 的 list 3）；
2. 12 处"被引用但无编号"补号或去重；
3. 引理改数字编号（Lemma A/B/C/D1/D2/8.1 → 1–6，Prop 3c → 1，约 70 处引用）；
4. 并入两个算法框（[paper/algorithms_draft.tex](../../trash/paper_root_2026-11-21/algorithms_draft.tex)）；
5. 记号 $B\to R$、证书矩阵 $\to Z$；
6. §IX 加 Reproducibility 段 + 证据表（替代被删的附录 C）；
7. 编译 + 逐页目视 + 页数 ≤ 11；
8. 把 `v2_test.tex` 覆盖到 `paper/current/others/q1_parametric_algorithms.tex`，删掉本目录的快照。
