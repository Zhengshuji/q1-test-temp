# 638 反例：$\omega=2>s=1$ 的可行 q1 实例（推翻 $\omega\le s$）

> 2026-11-27。按 ChatGPT 的建议直接问它能否证明 $\omega\le s$；它给出反例。本文件把反例落成**具体 q1 实例**
> 并逐条验证。
> 状态：**[精确验证]**（sympy 检查 $(5a)(5b)$）。

## 实例

$n=6$、$k=3$、$q=3$；$N$ 为前 3 个坐标的嵌入。
$$A e_1=e_2,\quad A e_2=e_4,\quad A e_4=e_5,\quad A e_5=e_6,\quad \text{其余 }0,$$
$$C=e_5^{\mathsf T}+e_6^{\mathsf T}.$$
$L$ 的三行（全为自由行，$r_0=0$）：
$$L=\begin{bmatrix}1&0&0&0&0&0\\0&1&0&0&0&0\\0&0&0&1&0&0\end{bmatrix}.$$

## 数据

- $K_0=\ker[C;CA]=\operatorname{span}\{e_1,e_2,e_3\}$ ✓（$C$ 杀 $e_1..e_4$，$CA$ 杀 $e_1,e_2,e_3,e_6$，$C e_5,C e_6\ne0$）；
- $A K_0\not\subseteq K_0$（$A e_2=e_4$），故 $W\ne0$：
  $$A N=N Z'+W,\qquad Z'=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix},\qquad W=e_4\,(0,1,0),$$
  $S=\operatorname{row}(W)=\operatorname{span}\{(0,1,0)\}$，$s=1$。

## 压缩数据

$$H=LN=\begin{bmatrix}1&0&0\\0&1&0\\0&0&0\end{bmatrix},\qquad
H_A=LAN=\begin{bmatrix}0&0&0\\1&0&0\\0&1&0\end{bmatrix}=ZH,$$
$$Z=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix},\qquad
G=ZH-HZ'=\begin{bmatrix}0&0&0\\0&0&0\\0&1&0\end{bmatrix},$$
$G$ 的行都在 $S$ 内 ✓。

## 验证

- $(5a)$：$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]=5$ ✓（sympy）；
- $(5b)$：$P(\lambda)=\lambda H-ZH=\begin{bmatrix}\lambda&0&0\\-1&\lambda&0\\0&-1&0\end{bmatrix}$，
  $\det P\equiv0$，非零 2×2 子式的 gcd $=1$（degree 0）⇒ $\operatorname{rank}P=2=\omega$ 对所有 $\lambda$ ✓；
  采样 $\lambda=0,1,2$ 秩均为 2。

## 结论

$$\boxed{\omega=2\ >\ s=1\ \text{可以可行}}$$
——**632 的猜想 $\omega\le s$ 被推翻**。

## 与穷举的关系

634/637 的穷举固定了 $S=\operatorname{span}\{e_1\}$ 与三种 $Z'$；本反例的 $S=\operatorname{span}\{e_2\}$、
$Z'=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix}$ 不在穷举范围内，故不矛盾——穷举的“0 命中”只是覆盖不足。

## 教训

- “$G$ 行在 $S$ 内”不能给出 $\omega$ 的上界；
- 关键在于 $Z$ 的特征向量可以避开 $\operatorname{im}H$（ChatGPT 指出的逃逸机制），而 $G$ 只需落在 $S$ 内；
- 需要新的不变量（如 $\operatorname{im}H\cap\ker(Z-\lambda I)$ 与 $G$ 的联合约束），而不是维数计数。

## 状态

- 反例：**[精确验证]**；
- $\omega\le s$：**推翻**。
