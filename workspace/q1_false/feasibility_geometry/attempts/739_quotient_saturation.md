# 739 商空间饱和引理：$\dim E_H=\dim(U\cap T)+\operatorname{cls}$

> 2026-11-27。证明 737 的等式猜想（数值 342/342），从而 $E_H$ 的维数有精确公式。
> 状态：**[已证-纸面]**。

## 定理

设 $T\subseteq\mathbb C^k$、$U=\operatorname{row}H$、$M=\mu I-Z'$、$H_i$ 为 $H$ 的第 $i$ 行，
$$F_i=T\cap(U-H_iZ'),\qquad E_H=\operatorname{span}\Big(\bigcup_i F_i\Big),$$
$$\operatorname{cls}=\dim\frac{U+\operatorname{row}(HM)}{U}.$$
若所有 $F_i\ne\varnothing$，则
$$\boxed{\dim E_H=\dim(U\cap T)+\operatorname{cls}.}$$

**证明**：

1. 如 737：$F_i=t_i+(U\cap T)$（取 $t_i\in F_i$），故
   $$E_H=(U\cap T)+\operatorname{span}\{t_i\},$$
   $$\dim E_H=\dim(U\cap T)+\dim\operatorname{span}\{[t_i]\},$$
   其中 $[t_i]\in T/(U\cap T)$。
2. $F_i\ne\varnothing$ ⇒ $t_i+H_iZ'\in U$，即 $H_iZ'\in U+T$；由 $H_iZ'=\mu H_i-H_iM$、$H_i\in U$，得 $H_iM\in U+T$。于是 $\operatorname{row}(HM)\subseteq U+T$，且
   $$\operatorname{cls}=\dim\frac{U+\operatorname{row}(HM)}{U}=\dim\frac{\operatorname{row}(HM)}{\operatorname{row}(HM)\cap U}.$$
3. 考虑线性映射
   $$\psi:\ T/(U\cap T)\longrightarrow(U+T)/U,\qquad t+(U\cap T)\longmapsto t+U .$$
   核为 $T\cap U=U\cap T$，像是 $(U+T)/U$，故 $\psi$ 是**同构**。
4. 由 $t_i\equiv-H_iM\pmod U$，有 $\psi([t_i])=[-H_iM]$；这些类张成 $\operatorname{row}(HM)$ 在 $(U+T)/U$ 中的像，维数恰为
   $$\dim\frac{\operatorname{row}(HM)}{\operatorname{row}(HM)\cap U}=\operatorname{cls}.$$
5. 于是 $\dim\operatorname{span}\{[t_i]\}=\operatorname{cls}$，代回第 1 步即得。$\square$

## 推论

$$d'\ \le\ \operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls}$$
（734 + 739，取等时精确）；且
$$\dim E_H=\dim(U\cap T)+\operatorname{cls}
\ \le\ \dim(U\cap T)+\min\big(\operatorname{rank}(HM),\ t-\dim(U\cap T)\big).$$

## 与数值

子 agent 的 342 例（$k=3,4$、$T$ 维 2–3、$\mu\in\{0,\pm1\}$ 或特征值）中该等式 **342/342** 成立，与本证明一致；此前的 737 只有 $\le$，现升级为等式。

## 意义

- $E_H$ 的维数完全由 $U\cap T$ 与 $\operatorname{cls}$ 决定；
- 方向性必要条件达到“精确但依赖 $H$”的形式；
- 若进一步能给出 $\operatorname{cls}$ 的数据级上界，则可去掉对 $H$ 的依赖。

## 状态

- 定理：**[已证-纸面]**；
- 数值：**[精确验证 342/342]**；
- 数据级 $\operatorname{cls}$ 界：**[未做]**。
