# 720 $Z'=0$ 时引理 E 的证明

> 2026-11-27。对 $Z'=0$ 的情形给出引理 E 的完整证明（此时不需要商空间）。
> 状态：**[已证-纸面]**。

## 定理

设 $Z'=0$、$H=XV$（$X$ 列满秩、$V$ 行满秩，$\operatorname{rank}H=d$）、$U=\operatorname{row}V$、$a=\dim(U\cap T)$，且 $ZH=G$、$\operatorname{row}(G)\subseteq T$。则
$$\boxed{\operatorname{rank}(ZX-XA)\le a}$$
对 $A=RZX$（$R$ 为 $X$ 的任意左逆）成立。

**证明**：

1. $Z'=0$ 时 $ZH=G$；又 $H=XV$，故 $ZXV=G$。
2. $V$ 行满秩（$d\times k$），取右逆 $V^{+}$（$VV^{+}=I_d$），则
   $$ZX=GV^{+},\qquad \operatorname{rank}(ZX)\le\operatorname{rank}G\le a .$$
   （$G$ 的每一行在 $T$，且 $Z_iH\in U$，故 $G_i=Z_iH\in U$；所以 $G_i\in U\cap T$，$\operatorname{rank}G\le a$。）
3. $A=RZX$，$X R$ 是到 $\operatorname{im}X$ 的投影，故
   $$ZX-XA=(I-XR)\,ZX,$$
   $$\operatorname{rank}(ZX-XA)\le\operatorname{rank}(ZX)\le a .\qquad\square$$

## 意义

- 引理 E 在 $Z'=0$ 时**成立**（且证明简单）；
- 关键步骤 $\operatorname{rank}G\le a$ 用到了 $G_i\in U\cap T$，这需要 $Z_iH\in U$（即 $(5a)$）；
- 对 $Z'\ne0$，$ZX=GV^+$ 不再成立（$ZXV=G+XVZ'$），需要新的论证。

## 与 718 的关系

718 的随机搜索（$k=3$）未找到反例；本定理给出 $Z'=0$ 子族的严格证明。一般 $Z'$ 仍是 **[M2 提案]**。

## 待办

1. 一般 $Z'$：尝试 $ZX = (G+XVZ')V^+$，得到 $\operatorname{rank}(ZX)\le a+\operatorname{rank}(XVZ'V^+)$，再控制第二项；
2. 若第二项可被 $a$ 吸收，则引理 E 得证。

## 状态

- $Z'=0$：**[已证-纸面]**；
- 一般 $Z'$：**[M2 提案]**。
