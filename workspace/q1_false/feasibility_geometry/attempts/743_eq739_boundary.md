# 743 739 的边界：空 $F_i$ 与 $\operatorname{cls}<\operatorname{rank}$ 的两个例子

> 2026-11-27。子 agent（eq-search）在 $k=5,6$ 上做了 664 例精确检验：等式 664/664、0 反例；并给出两个边界例子。
> 状态：**[精确验证]** + **[已证-纸面]**（推论）。

## eq-search 的检验

- 设置：$k\in\{5,6\}$、$q=k$、$r=\operatorname{rank}H\in\{2,3\}$、$t\in\{2,3\}$、$T=\operatorname{span}\{e_1,e_2\}$（或三维）；
- 664 组满足“所有 $F_i$ 非空”；$\operatorname{cls}\ge2$ 有 469 组、$\operatorname{cls}=3$ 有 43 组、$U+T\subsetneq V$ 有 429 组、$d=\dim(U\cap T)>0$ 有 349 组、$\mu$ 取特征值 48 组；
- **violations $=0$，等式 664/664**（两个 seed 一致）。

结论：与 739 的纸面证明一致；在“所有 $F_i$ 非空”下**不可能**失败（子 agent 也复核了证明）。

## 候选 B：空 $F_i$ 会让等式失败（且本身不可行）

$k=5$、$T=\operatorname{span}\{e_1,e_2\}$、$U=\operatorname{span}\{e_1+e_3,e_4\}$，
$$H=\begin{bmatrix}1&0&1&0&0\\0&0&0&1&0\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\end{bmatrix},\qquad
Z'=\begin{bmatrix}0&0&1&0&0\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&1\\0&0&0&0&0\end{bmatrix},\quad\mu=0 .$$
$h_1Z'=e_3\in U+T$ ⇒ $F_1$ 非空；$h_2Z'=e_5\notin U+T$ ⇒ $F_2=\varnothing$。
于是 $(\dim E_H,\ \dim(U\cap T),\ \operatorname{cls})=(1,0,2)$，**严格不等式** $1<0+2$。

**但空 $F_i$ 与 $(5a)$ 矛盾**：$F_i\ne\varnothing\iff H_iZ'\in U+T$（因为 $t+H_iZ'\in U$、$t\in T$），所以可行性要求所有 $F_i$ 非空。故候选 B 本身不可行，不是 739 的反例。

## 候选 A：$\operatorname{cls}<\operatorname{rank}(HM)$ 的实例

$k=5$、$T=\operatorname{span}\{e_1,e_2\}$、$U=\operatorname{span}\{e_1+e_3,e_4\}$，
$$H=\begin{bmatrix}1&0&1&0&0\\0&0&0&1&0\\1&0&1&0&0\\0&0&0&0&0\\0&0&0&0&0\end{bmatrix},\qquad
Z'=\begin{bmatrix}-1&0&0&0&0\\0&0&0&0&0\\-1&0&-1&0&0\\-1&0&0&-1&0\\0&0&0&0&0\end{bmatrix},\quad\mu=0 .$$
$h_1M=(2,0,1,0,0)$、$h_2M=(1,0,0,1,0)$，二者之差 $e_1+e_3-e_4\in U$，故两类相同；
$(\dim E_H,\dim(U\cap T),\operatorname{cls})=(1,0,1)$，而 $\operatorname{rank}(HM)=2$。

这正说明 739 用 $\operatorname{cls}$ 而非 $\operatorname{rank}(HM)$ 是正确的：$\operatorname{cls}$ 只计“模 $U$ 的新方向”。

## 推论（可行性 ⇒ 等式）

若可行，则（$H_iZ'\in U+T$，见 697）所有 $F_i\ne\varnothing$，故 739 的等式成立：
$$\boxed{\text{可行}\ \Longrightarrow\ \dim E_H=\dim(U\cap T)+\operatorname{cls}.}$$

## 状态

- 664 例检验：**[精确验证]**；
- 候选 B：**[精确验证]**（空 $F_i$ ⇒ 不可行）；
- 候选 A：**[精确验证]**（$\operatorname{cls}<\operatorname{rank}$）；
- 推论：**[已证-纸面]**。
