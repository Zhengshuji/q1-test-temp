# 专家 66 号裁决落实：模板成立，$LAN$ 的行/列作用混淆已更正

> 2026-11-09。专家 66 号指出：模板没有错，是我们对 $H_A=LAN$ 的计算把**列作用** $Ae_i$ 与
> **行作用** $e_i^*A$ 混淆了。用正确的 $A$ 重算，模板通过全部检查。状态：**精确验证（模板成立）**。

## 目标

更正 213/66 中对 6 维模板的错误否定，确认模板并记录正确的矩阵与验证。

## 设想与理由

专家给的 $A$（列作用）：
$$A=\begin{bmatrix}
0&1&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
1&0&0&0&0&0\\
0&0&0&0&1&0
\end{bmatrix},$$
即 $Ae_1=e_5$、$Ae_2=e_1$、$Ae_3=Ae_4=0$、$Ae_5=e_6$、$Ae_6=0$。
**行作用**是转置关系：
$$e_1^*A=e_2^*,\quad e_2^*A=0,\quad e_5^*A=e_1^*.$$
我们此前把 $A$ 的列作用写成了行（例如把 $Ae_1=e_5$ 写成第 1 行第 5 列），
于是 $e_1^*A$ 被误读成 $e_5^*$，$H_A$ 算错。

## 做法：精确验证

取 $C=e_6^*$、$L_0=e_1^*$、$L=[e_1^*;e_2^*;e_1^*+e_2^*+e_5^*]$、$N=[e_1,e_2,e_3,e_4]$。
用 `check_candidate`（有理精确）：
```
rank[C;L]=4 ✓ · dim ker=2 ✓ · CZ=LZ=0 ✓ · (5a)=True ✓ · h=4=法秩 ✓
gcd/Toeplitz 一致（(5b) 成立）✓ · 域=有理 ✓
```
压缩矩阵：
$$H=\begin{bmatrix}1&0&0&0\\0&1&0&0\\1&1&0&0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0&1&0&0\\0&0&0&0\\1&1&0&0\end{bmatrix},$$
与专家一致。铅笔
$$P(\lambda)=\begin{bmatrix}\lambda&-1&0&0\\0&\lambda&0&0\\ \lambda-1&\lambda-1&0&0\end{bmatrix},$$
首两列子式 $\lambda^2,\ \lambda^2-1,\ -\lambda(\lambda-1)$，$\gcd=1$，故 $\operatorname{rank}P(\lambda)=2$ 对所有 $\lambda$。

结构：$K_0=\operatorname{span}\{e_1,\dots,e_4\}$、$A(K_0)\not\subseteq K_0$（$Ae_1=e_5$）、$V=\operatorname{span}\{e_3,e_4\}$、
$A(V)=0\subseteq V$、$\omega=2$、$q=3>\omega$（与 65 号的 $q>\omega$ 必要条件一致）、$\operatorname{rank}[C;L]=4=p+q$（$\mathsf P_{\rm ind}$）。

## 进展

* 模板成立，已精确复核；
* 更正了我们此前的 $LAN$ 计算错误（列/行作用）；
* 模板可作为“移位链 + 泄漏”的已验证谱基座。

## 最终结论

* 专家 66 号正确；213/66 的否定撤回；
* 模板满足 $(5a)(5b)$，是 $A(V)\subseteq V$、$A(K_0)\not\subseteq K_0$ 的可行例；
* 但专家提醒：这是**固定配置**的谱可行，尚不能保证在编码算术的变参扰动下谱一致；这一点需单独证明。

## 放弃原因

* 未把模板嵌入算术 gadget；
* 未证明变参下的谱一致性（uniformity）；
* 未 Lean 化。

## 残留价值

* 一个经过精确验证的谱基座；
* 行/列作用的教训（后续所有 $LAN$ 计算）；
* 下一步的 uniform 谱问题。

## 相关文件

* [attempts/213](213_65_verdict_implementation.md)（被更正）
* [attempts/65 答复](../../../for_expert/archive/65_local_rigidity_counterexample-answer.md)
* [attempts/201](201_pair_lift_theorem.md)

## 状态

* 模板：**[精确验证，L1+L2]**。
* 算术 gadget / uniformity：**[未做]**。
