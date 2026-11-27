# 论文排版与写作规范（q1 论文重写用）

> 依据：amsthm 包的官方约定（`plain` 用于定理类、`definition` 用于定义、`remark` 用于注记；
> 证明一律用 `proof` 环境并以 QED 结束）与 IEEE 期刊的通行排版习惯。
> 目的：消除全文的格式不一致与重复陈述。

## 1. 定理类环境

1. **单一共享计数器**：全文只用一个序列，定理/引理/命题/推论依次编号。
   ```latex
   \newtheorem{thm}{Theorem}
   \newtheorem{lem}[thm]{Lemma}
   \newtheorem{prop}[thm]{Proposition}
   \newtheorem{cor}[thm]{Corollary}
   ```
2. **禁止手写编号**：不得出现 `\begin{lem}[3]`。编号由计数器给出。
3. **每个环境必须有 `\label`**，且正文一律用 `\ref`：
   ```latex
   \begin{lem}\label{lem:rankid} ... \end{lem}
   ... by Lemma~\ref{lem:rankid} ...
   ```
4. **注记**用独立计数器：`\theoremstyle{remark}` + `\newtheorem{remark}{Remark}`。

## 2. 证明

1. **只有一种写法**：`\begin{proof} ... \end{proof}`。
   禁止 `\emph{Proof.}`、禁止手写 QED。
2. 分情形证明用行内小标题：`\emph{(i)}`、`\emph{(ii)}`，或 `\textbf{Step 1.}`；
   同一篇里只用其中一种。
3. QED 符号：`\renewcommand{\qedsymbol}{$\blacksquare$}`（全文唯一）。
4. 证明必须**公式化**：每一步"设—推—得"用行间公式承载，自然语言只做连接；
   禁止"因为……所以……"连续成段而不给式子。
5. 证明中引用的每个事实都要么是已编号的命题（`\ref`），要么当场给出。

## 3. 算法

1. 真正的过程用 `algorithm` 浮动体 + `algorithmic`，**标题在上**、行号自动。
2. 定理证明内部的构造用行内 `\emph{Step 1.}` 段落形式。
3. 同一个定理内部不得混用两种。

## 4. 公式

1. **只在后文引用时编号**；不被引用的用 `equation*`/`\[ \]`。
2. 编号公式一律 `\begin{equation}\label{eq:...}`，引用用 `\eqref{eq:...}`。
3. 多行对齐用 `align`/`aligned`，以 `=` 对齐。
4. 公式作为句子成分时，句末标点放在公式**内部**。

## 5. 交叉引用

- 结构：`Section~\ref{}`、`Appendix~\ref{}`
- 命题：`Lemma~\ref{}`、`Theorem~\ref{}`、`Proposition~\ref{}`、`Corollary~\ref{}`
- 公式：`\eqref{}`
- **禁止**把编号写死成 "Lemma 3"、"Theorem 1"。

## 6. 不重复

1. 每个命题只在它首次出现处**完整陈述**一次；后文只用 `\ref` 指回。
2. 同一记号只定义一次（见 §7）。
3. 同一事实不在引言、预备、结论里各说一遍：引言说"要解决什么"，
   预备说"记号与问题"，结论说"得到了什么"。
4. 算法与定理：定理给保证，算法给步骤；两者的正确性论证只出现一次。

## 7. 记号

1. 首次使用时定义；同一符号不得表示两个对象
   （例：不要同时用 $R$ 表示自由行与某个块矩阵）。
2. 矩阵分块统一用 $[X;Y]$（竖排）与 $[X\ \ Y]$（横排）。
3. 秩、维数、生成空间：`\operatorname{rank}`、`\dim`、`\operatorname{row}`。

## 8. 语言与标点

1. 不用口语化表达（"obviously"、"It's obviously that"、"clearly"）。
2. 名称列表用 en-dash：Fernando--Trinh--Jennings。
3. 缩写首次出现给全称；`\mathrm{DEC}` 这类算子名一律 `\mathrm`。
4. 段落标题用 `\paragraph*{}`（不编号）。

## 9. 与其他部分的衔接

- 引言不写证明，只写问题、动机、贡献；
- 每节开头一句话说明本节要做什么，结尾不重复结论。
