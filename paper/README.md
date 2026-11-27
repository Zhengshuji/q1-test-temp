# paper/ —— 本仓库只保留 Paper III 与 Paper IV

> **2026-11-26 起**：Paper I（判定复杂度）与 Paper II（最小阶与构造）只在
> q1-functional-observer 仓库维护（本地 `../q1-functional-observer/`；
> GitHub: <https://github.com/Zhengshuji/q1-functional-observer>），正文、Lean 与精确验证都在那里。
> 本目录不再保留这两篇的副本，也不再维护它们的 Lean 映射。
> 旧版、合并稿与拆分/Lean 计划见 [archive/paper_drafts/](../archive/paper_drafts/)。

## 文件

| 文件 | 内容 | 状态 |
|---|---|---|
| `current/paper_III_hyperplane.tex` / `.pdf` | Paper III：超平面层（$c=1$ 几何、判据、固定 $p$ 复杂度） | 唯一 `.tex` 源 |
| `current/paper_IV_c2.tex` / `.pdf` | Paper IV：$c=2$ 的像约化与多项式判定 | 唯一 `.tex` 源 |

两篇都是 IEEEtran `journal`、两栏；`.tex` 是唯一事实来源，PDF 是派生物。

## 构建

```text
cd paper/current
pdflatex paper_III_hyperplane.tex && pdflatex paper_III_hyperplane.tex
pdflatex paper_IV_c2.tex && pdflatex paper_IV_c2.tex
```

（两遍以解析交叉引用；`.aux/.log/.out` 由 `.gitignore` 覆盖。）

## 与 q1-functional-observer 的分工

| 内容 | 位置 |
|---|---|
| Paper I / II（正文 + Lean + 验证） | `../q1-functional-observer/` |
| Paper III / IV 的正文 | 本目录 `current/` |
| Paper I/II 的历史材料（旧版、合并稿、拆分计划） | 本仓库 `archive/paper_drafts/` |

Paper III/IV 的数学与 Paper I/II 共享压缩链与子空间语言，但**不引用本仓库的旧文档**：
需要共同记号时，直接引 **Paper I** / **Paper II**（约定见仓库根 `README.md` §1.5）。
