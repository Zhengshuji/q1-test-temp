# paper/hyperplane —— 超平面层论文（单文件版）

**标题**：*Functional-Observer Feasibility in the Hyperplane Layer*

**成品**：`hyperplane_layer.tex`（自包含，1822 行）→ PDF（**15 页**，IEEEtran 两栏）。
（`hyperplane_layer.pdf` 若被查看器锁定，最新构建在 `hl_new.pdf`，关闭查看器后用 `Copy-Item hl_new.pdf hyperplane_layer.pdf -Force` 替换。）

## 结构

```
I     Introduction（与姊妹稿划界 / 五条新结果 / 三条主张的分层）
II    Preliminaries and the compressed formulation（判据引自姊妹稿）
III   Geometry and parameterization（方向定理、E_μ^0、纤维、相对丛、对偶）
IV    Exact algebraic decision procedure（继承工具 + 图卡 + 满秩引理 + 证书 + 算法）
V     Fixed-p bit complexity（引理陈述在此，证明在附录）
VI    A repeated-eigenspace counterexample
A     Complete data and exact certificates
B     Proofs of the height and subresultant bounds
```

## 构建

```bash
cd paper/hyperplane
python build_single.py      # 由 src/ 的分节源拼成单一 hyperplane_layer.tex
pdflatex hyperplane_layer.tex
pdflatex hyperplane_layer.tex
```

`hyperplane_layer.tex` 是**唯一事实来源**（自包含：前言、摘要、正文、附录、参考文献都在里面）。
`src/` 只是分节构建素材（`sec1s, sec2, sec3t, sec4s, sec5s, sec6t, appAs, appBCt`），改内容时二者择一：
直接改单文件，或改 `src/` 后重跑 `build_single.py`。

## 版式约定

- 定理环境共享计数器（`thm`/`lem`/`prop`/`cor`/`defn`/`exmp`/`algo`）；`remark` 独立计数。
- 交叉引用一律 `\label`/`\ref`，不手写编号。
- 表格 `booktabs`；两栏宽表 `table*`。
- 引用键：`companion1`（决策篇）、`companion2`（最小阶篇）、`fer26a/fer26b`、`fer10`、`dar25`、`hj13`、`bpr06`、`lan02`、`vzgg03`。

## 三条主张的分层（审稿要点）

1. **整层精确判定**：任意输入、精确算术、不承诺多项式时间（第 IV 节）。
2. **几何单谱子类的多项式时间**：promise-class，超出范围时报告"超出范围"而非"不可行"（第 V 节）。
3. **反例**：只否定"每个特征值取一个特征向量"的约化（第 VI 节），不声称重复谱困难。
