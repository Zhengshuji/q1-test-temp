# 629 定理：$A$ 保持 $K_0$ 时 q1 是平凡的（可行 $\iff L_0N=0$）

> 2026-11-27。由 627/628 的审计继续，发现右铅笔（$AN=NZ'$，即 $A K_0\subseteq K_0$）类有一个干净的
> 完整刻画：**只有 $\omega=0$ 可行**；于是可行 $\iff H_0=L_0N=0$。这解释了 557/598/601 的“门”全都不成立。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 设定

$N$ 为 $K_0=\ker[C;CA]$ 的基，$k=\dim K_0$；假设
$$A N=N Z'\quad(\text{即 } A K_0\subseteq K_0).$$
则 $H=LN$、$H_A=LAN=HZ'$。记 $K=\ker H\subseteq\mathbb C^k$，$\omega=\operatorname{rank}H=k-\dim K$。

## $(5a)$ 等价于 $K$ 不变

$H_A v=H Z'v$；$(5a)$：$\forall v\in K$，$H Z'v=0$，即 $Z'v\in K$。所以
$$(5a)\iff Z'(K)\subseteq K .$$

## $(5b)$ 强制 $K=\mathbb C^k$

设 $K$ 不变。$H$ 通过商空间分解：$H=\bar H\circ\pi$，$\pi:\mathbb C^k\to\mathbb C^k/K$。
于是
$$P(\lambda)=H(\lambda I-Z')=\bar H\circ\overline{(\lambda I-Z')}\circ\pi,\qquad
\operatorname{rank}P(\lambda)=\operatorname{rank}\overline{(\lambda I-Z')},$$
（$\bar H$ 在商空间上单射）。而
$$\operatorname{rank}P=\omega=k-\dim K=\dim(\mathbb C^k/K).$$
所以 $(5b)\iff\overline{(\lambda I-Z')}$ 对**所有** $\lambda$ 可逆。

若 $\dim(\mathbb C^k/K)>0$，复线性映射 $\overline{Z'}$ 必有特征值 $\lambda_0$，
则 $\overline{(\lambda_0 I-Z')}$ 不可逆——矛盾。故
$$K=\mathbb C^k,\qquad \omega=0 .$$

## 推论

- $\omega=0$ 即 $H=0$，要求 $H_0=L_0N=0$ 且自由行取零（$RN=0$）；
- 反之若 $L_0N=0$，取 $R=0$ 得 $H=H_A=0$，$(5a)(5b)$ 成立；
- 所以
$$\boxed{A K_0\subseteq K_0\ \Longrightarrow\ \big(\text{可行}\iff L_0N=0\big)}$$
且此时 $q_{\min}=r_0$（$R$ 取空）。

## 精确验证（此前“门”的实例全部不可行）

| 实例 | $A K_0\subseteq K_0$ | $L_0N$ | 判定 |
|---|---|---|---|
| 557 | 是 | $(1,0,0),(0,1,0)$ ≠0 | 不可行（与 557 一致） |
| 598（门 $(2,3,6)$） | 是 | 含常数行 ⇒ ≠0 | 不可行（此前“门上可行”是错的） |
| 598（门外 $(2,3,5)$） | 是 | ≠0 | 不可行 |
| 601（$r_1=0$ 与 $r_1\ne0$） | 是 | $(1,0,0)$ ≠0 | 全部不可行（sympy：$(5a)$ 对所有 $r_1$ 失败） |

sympy 直接检查：601 的 $(5a)$ 对 $r_1=0,1,2$ 均失败；598 的门上 $(5a)$ 失败、门外 $(5a)$ 成立但 $(5b)$ 失败。

## 意义

- 这解释了 596–616 的整条“右铅笔 gadget”路线为何反复出问题：**$(5a)$ 要求 $K$ 不变，$(5b)$ 再强迫 $K$ 为全空间**；
- $A$ 保持 $K_0$ 的实例类是**平凡可判**的（检查 $L_0N=0$），没有任何 hardness 空间；
- q1_true 若要继续，必须研究 $A K_0\not\subseteq K_0$（即 $W\ne0$）的情形——那里 $H_A=HZ'+G$，$(5a)$ 不再强制 $K$ 不变。

## 状态

- 定理：**[已证-纸面]**；
- 实例检查：**[精确验证]**；
- $W\ne0$：**[未分析]**。
