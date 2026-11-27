# 723 $a=0$ 的强界等价于“$Z$ 保持 $\operatorname{im}H$ 不变”

> 2026-11-27。把 722 的猜想 $\Pi G=0$ 改写为不变子空间陈述，并与 715（$d=1$）统一。
> 状态：**[已证-纸面]**（等价改写）+ **[猜想]**（不变性）。

## 等价改写

$H=XV$、$\Pi=I-XR$、$U=\operatorname{row}V$。
因 $\Pi X=0$，有 $\Pi H=\Pi XV=0$，故
$$G=ZH-HZ'\ \Longrightarrow\ \Pi G=\Pi ZH-\Pi HZ'=\Pi ZH .$$
于是
$$\Pi G=0\iff \Pi ZH=0\iff (\Pi Z)H=0\iff (\Pi Z)X V=0 .$$
$V$ 行满秩（右乘 $V$ 不改变零性）⇒
$$\boxed{\Pi G=0\iff (\Pi Z)X=0\iff Z(\operatorname{im}X)\subseteq\operatorname{im}X .}$$

即：$G$ 的列落在 $\operatorname{im}X$ $\iff$ $Z$ 保持 $\operatorname{im}H=\operatorname{im}X$ 不变。

## 猜想（$a=0$ 的不变性）

$$\boxed{a=\dim(U\cap T)=0\ \Longrightarrow\ Z(\operatorname{im}H)\subseteq\operatorname{im}H .}$$

**支持**：
- $d=1$：715 已证（$v\notin T$ ⇒ $Zu=\mu u$，即 $\operatorname{im}X=\operatorname{span}\{u\}$ 不变）——正是本猜想的最低维情形；
- $d=2$、$k=3$、$a=0$：33 个相容实例 $\Pi G=0$；
- $q=4$、$k=3$、$a=0$：6 个相容实例 $\Pi G=0$。

## 意义

- 把 722 的“强界”化为经典的不变子空间问题；
- 715（一维方向 $U\subseteq T$）与本猜想（$a=0$ 时 $\operatorname{im}H$ 不变）是同一现象的两个侧面；
- 若猜想成立，则引理 E 在 $a=0$ 时成立（$r=0$），且 $P$ 的行结构受 $Z$ 不变性约束。

## 一般 $a$ 的版本（猜想）

$$a>0\ \Longrightarrow\ \operatorname{rank}(\Pi G)\le a,$$
即 $Z$ 在 $\operatorname{im}H$ 上的作用“破坏不变性的程度”不超过 $a=\dim(U\cap T)$。

## 下一步

1. 用 $U\cap T=0$ 时的直和分解 $C^k=U\oplus T$ 证明猜想（$a=0$）；
2. 一般 $a$ 用 $U\cap T$ 的补方向分解；
3. 与 ChatGPT 核对。

## 状态

- 等价改写：**[已证-纸面]**；
- $a=0$ 不变性：**[猜想]**（$d=1$ 已证 + 39 例数值）；
- 一般 $a$：**[猜想]**。
