# 722 一般 $Z'$ 的强界：$d=1$ 已证，$d\ge2$ 仍是猜想

> 2026-11-27。按 ChatGPT 的建议检验强界 $\operatorname{rank}((I-XR)G)\le a$；$d=1$ 可证，$d=2$ 有数值支持。
> 状态：**[已证-纸面]**（$d=1$）+ **[猜想]**（$d\ge2$）。

## $d=1$ 的证明

$H=u v^{\mathsf T}$、$X=u$（$q\times1$）、$V=v^{\mathsf T}$、$R$ 为左逆（$Ru=1$）、$\Pi=I-uR$。
$$G=ZH-HZ'=(Zu)v^{\mathsf T}-u\,w^{\mathsf T},\qquad w=v^{\mathsf T}Z' .$$
由 $Ru=1$：
$$\Pi G=G-uRG=(Zu-u\,RZu)\,v^{\mathsf T}=(\Pi Zu)\,v^{\mathsf T},$$
故 $\operatorname{rank}(\Pi G)\le1$。

若 $a=\dim(U\cap T)=0$（即 $v\notin T$），715 的论证给出 $Zu=\mu u$（相容性 + $G$ 行在 $T$ 迫使），故 $\Pi Zu=0$，从而
$$\Pi G=0\ \Rightarrow\ r=0=a .$$
若 $a=1$（$v\in T$），$\operatorname{rank}(\Pi G)\le1=a$ ✓。

故 $d=1$ 时强界成立。

## $d=2$ 的数值检验

$k=q=3$、$T=\operatorname{span}\{e_1\}$、$a=0$（$U\cap T=0$）、随机 $Z'$ 与 $H$（秩 2），检查相容性后解 $Z$，计算 $\operatorname{rank}(\Pi G)$：
33 个相容实例中**全部为 0**（即 $G$ 的列落在 $\operatorname{im}X$）。

支持“$a=0\Rightarrow \Pi G=0$”的猜想，但未证。

## ChatGPT 的判断

- 721 的归约正确，但由 $\operatorname{rank}G\le t$ 降到 $\le a$ 缺少关键条件；
- 它尝试构造反例失败（因为 $G$ 不能独立指定，必须满足 $G=ZH-HZ'$）；
- 结论：强界目前既未证明也未被否定；引理 F 只能作为**条件性**结论。

## 待证猜想

$$\boxed{a=0\ \Longrightarrow\ \Pi G=0\ (\text{即 }G\ \text{的列}\subseteq\operatorname{im}X)}$$
以及一般 $a$：
$$\boxed{\operatorname{rank}(\Pi G)\le a .}$$

## 下一步

1. 用 $G=ZH-HZ'$ 与 $G$ 行在 $T$、$a=0$ 的分解（$T\oplus U$ 直和）证明 $\Pi G=0$；
2. 一般 $a$ 的分解；
3. 若证明成功，引理 F 成为定理。

## 状态

- $d=1$：**[已证-纸面]**；
- $d=2$：**[猜想]**（33/33 数值）；
- ChatGPT 评估：**[M2]**。
