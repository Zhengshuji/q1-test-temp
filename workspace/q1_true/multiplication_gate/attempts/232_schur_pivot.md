# (5b) 门（四）：秩单调性障碍与 Schur 枢轴的出路

> 2026-11-09。231 提出“门放 $(5b)$，用 guard+gate 块”。进一步检查发现：
> 直接的块秩设计仍偏向“满秩/独立”，而 $z=xy$ 是**秩一（掉秩）**条件，方向相反。
> 出路是专家建议的**固定枢轴 + Schur 补**：先把总秩钉在一个低值，再让残差秩一。
> 状态：**M2（结构性论证）**。

## 目标

解释为什么“直接块”不能强制 $z=xy$，并给出正确的 Schur 形式。

## 设想与理由

## 做法

### 1. 秩单调性

$(5a)$：$\operatorname{row}(LA)\subseteq\operatorname{row}M$（$M=[L;CA;C]$）。“加行不增秩”。
若 $M$ 含门块 $G=\begin{bmatrix}1&x\\y&z\end{bmatrix}$：
- $G$ 满秩（$z\ne xy$）：$G$ 的行空间是整个二维空间，任何附加行都依赖 ⇒ 条件**自动成立**；
- $G$ 秩一（$z=xy$）：行空间小，附加行**可能**独立 ⇒ 条件可能失败。

所以“依赖”在满秩时自动、在秩一时才可能失败：$(5a)$ 只能**排除**秩一，不能强制秩一。

$(5b)$：$\operatorname{rank}P=\omega$，而 $P=(\lambda I-D)H$ 的秩 $\le\omega$。
掉秩（秩一 $G$）只会让 $\operatorname{rank}P<\omega$，违反 $(5b)$；所以 $(5b)$ 也**排除**秩一。

两个条件都偏向“满秩/独立”，而乘法门 $z=xy$ 是秩一（掉秩）——方向相反。

### 2. Schur 枢轴的出路

专家建议的固定枢轴块确实能改变方向：
$$M=\begin{bmatrix}I_s&U\\ V&G\end{bmatrix}
\ \Longrightarrow\ \operatorname{rank}M=s+\operatorname{rank}(G-VU).$$
如果**总秩被钉在 $s$**（枢轴 $I_s$ 使其余行必须被消掉），则
$$\operatorname{rank}M=s\iff G-VU=0.$$
若取 $G=\begin{bmatrix}1&x\\y&z\end{bmatrix}$、$VU=\begin{bmatrix}0&0\\0&xy\end{bmatrix}$（示意），
则 $G-VU=0$ 给出 $1=0$，不对；应取 $G-VU=\begin{bmatrix}0&?\\?&z-xy\end{bmatrix}$ 之类的残差，
再要求“残差秩一”或“残差为零”。

更实际的形式：
$$\operatorname{rank}\begin{bmatrix}I_s&U\\V&G\end{bmatrix}=s+1
\iff \operatorname{rank}(G-VU)=1
\iff \det(G-VU)=0\ \text{且}\ G-VU\ne0.$$
若 $G-VU=\begin{bmatrix}1&x\\y&z\end{bmatrix}$，则 $\det=0\iff z=xy$，且非零自动。
所以需要：
1. 一个固定枢轴 $I_s$；
2. 一个把总秩钉在 $s+1$ 的观测器秩等式（而不是自由的 $\operatorname{rank}M$）；
3. 门的残差恰为 $\begin{bmatrix}1&x\\y&z\end{bmatrix}$。

## 进展

* 证明直接块的秩单调性（两个通道都偏向满秩）；
* 明确 Schur 枢轴是改变方向的必要机制；
* 给出目标形式：秩 $s+1$ 的等式 + 残差 $\det=0$。

## 最终结论

* 直接把门放进 $(5a)$ 或 $(5b)$ 的块秩都因单调性失败；
* 必须先用固定枢轴把总秩**钉低**，再让残差的秩一条件出现；
* 下一步：构造 $s=1$ 或 $s=2$ 的枢轴，并把 $(5a)/(5b)$ 的秩等式写成 Schur 形式。

## 放弃原因

* 未构造具体枢轴；
* 未证 soundness；
* 未接观察者数据。

## 残留价值

* 秩单调性障碍的清晰陈述；
* Schur 目标形式的精确描述；
* 与专家建议的对齐（固定枢轴）。

## 相关文件

* [attempts/229](229_gate_seed.md)–[231](231_gate_channel_5b.md)
* [for_expert 68/69 answer](../../../for_expert/archive/68_69-answer.md)

## 状态

* 障碍/方向：**[M2]**。
* Schur 构造：**[未做]**。
