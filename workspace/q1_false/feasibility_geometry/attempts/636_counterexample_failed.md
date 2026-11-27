# 636 反例尝试失败：$G=0$ 时回到 629（$\omega=0$）

> 2026-11-27。尝试构造 $\omega>s$ 的反例（$s=1$、$\omega=2$）：取旋转型 $Z$ 使 $V=\operatorname{im}H$ 无特征向量。
> **结果：该构造中 $G=0$，铅笔回到 $H(\lambda I-Z')$，在 $\lambda=0$ 掉秩——反例失败。**
> 状态：**[已证-纸面]**。

## 构造

$k=q=3$、$H=\operatorname{diag}(1,1,0)$（$V=\operatorname{span}\{e_1,e_2\}$，$\omega=2$）、
$Z=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}$（循环，$V$ 中无特征向量）、$Z'=Z P$（$P=\operatorname{diag}(1,1,0)$）、
$H_A=Z'=HZ'$（$Z'$ 第三列为零）。

## 检查

- $(5a)$：$\ker H=\operatorname{span}\{e_3\}$，$H_A e_3=Z'e_3=0$ ✓；
- $(5b)$：$P(\lambda)=H(\lambda I-Z')$（**注意是 $H(\lambda I-Z')$，不是 $(\lambda I-Z)H$**）。

$\ker\big(H(\lambda I-Z')\big)=\{x:(\lambda I-Z')x\in\ker H=\operatorname{span}\{e_3\}\}$。
在 $\lambda=0$：$Z'x\in\operatorname{span}\{e_3\}$；$Z'$ 的像为 $\operatorname{span}\{e_2,e_3\}$（$Z'=[[0,0,0],[1,0,0],[0,1,0]]$），
$Z'x\in\operatorname{span}\{e_3\}$ ⇒ $x\in\ker Z'=\operatorname{span}\{e_1,e_3\}$，核维数 2 ⇒ $\operatorname{rank}P(0)=1<2$ ⇒ 失败。

## 教训

- $(5b)$ 的铅笔是 $H(\lambda I-Z')$，**$Z'$ 是数据**，不是自由构造的 $Z$；
- $G=0$（即 $L_YW=0$，自由行在 $Y$ 方向取零）时，问题回到 629：$H_A=HZ'$，只有 $\omega=0$ 可行；
- 要得到 $\omega>0$，必须 $G\ne0$，且 $G$ 的行在 $S=\operatorname{row}(W)$ 内；
- 因此 632 的猜想 $\omega\le s$ 仍然成立（反例失败）。

## 状态

- 反例失败：**[已证-纸面]**；
- $\omega\le s$：**[M2 猜想]**（634 穷举支持）。
