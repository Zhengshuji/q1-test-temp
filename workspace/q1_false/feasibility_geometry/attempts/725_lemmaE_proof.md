# 725 引理 E 的完整证明：$\operatorname{rank}(ZX-XA)\le a$

> 2026-11-27。按 ChatGPT 的桥接引理，完成引理 E 与引理 F 的证明；$a=0$ 的不变性成为定理。
> 状态：**[已证-纸面]**。

## 定理（引理 E）

设 $H=XV$（$X$ 列满秩、$V$ 行满秩，$\operatorname{rank}H=d$），$U=\operatorname{row}V$，$T\subseteq\mathbb C^{1\times k}$，$a=\dim(U\cap T)$，且
$$G=ZH-HZ',\qquad \operatorname{row}(G)\subseteq T .$$
取 $R$ 为 $X$ 的左逆（$RX=I_d$）、$A=RZX$、$\Pi=I-XR$。则
$$\boxed{\operatorname{rank}(ZX-XA)=\operatorname{rank}(\Pi G V^+)\le a .}$$

## 证明

1. **商空间桥接**：令 $\pi:\mathbb C^{1\times k}\to\mathbb C^{1\times k}/T$ 为商映射，$\overline V=\pi(V)$（逐行取商）。
2. **$\operatorname{rank}\overline V=d-a$**：$c\mapsto cV$ 单射（$V$ 行满秩），其复合 $\pi(cV)$ 的核为 $\{c:cV\in U\cap T\}$，维数 $a$；由秩-零度定理得 $\operatorname{rank}\overline V=d-a$。
3. **模 $T$ 的相容方程**：$G$ 行在 $T$ ⇒
   $$ZX\,\overline V=X\,\overline{VZ'} .$$
4. 左乘 $R$：$\overline{VZ'}=RZX\,\overline V$；代回得
   $$ZX\,\overline V=XRZX\,\overline V\ \Longrightarrow\ \Pi ZX\,\overline V=0 .$$
5. **秩界**：$\Pi ZX$ 为 $q\times d$、$\overline V$ 为 $d\times k$、乘积为零 ⇒
   $$\operatorname{rank}(\Pi ZX)\le d-\operatorname{rank}\overline V=a .$$
6. **回到 $G$**：由 $\Pi X=0$，
   $$\Pi G=\Pi(ZXV-XVZ')=\Pi ZX\,V\ \Longrightarrow\ \operatorname{rank}(\Pi G)\le\operatorname{rank}(\Pi ZX)\le a .$$
7. **$r$ 的界**：$ZX-XA=\Pi ZX=\Pi G V^+$（721）⇒
   $$\operatorname{rank}(ZX-XA)\le a .\qquad\square$$

## 推论 1（$a=0$ 的不变性，723）

$a=0$ ⇒ $\operatorname{rank}(\Pi ZX)=0$ ⇒ $\Pi ZX=0$ ⇒
$$\boxed{Z(\operatorname{im}X)\subseteq\operatorname{im}X\ (\text{即 }Z(\operatorname{im}H)\subseteq\operatorname{im}H).}$$

## 推论 2（引理 F）

记 $E=ZX-XA$（$\operatorname{rank}E\le a$）。由 $ZH=ZXV=XAV+EV$：
$$P(\lambda)=\lambda H-ZH=X(\lambda I-A)V-EV .$$
对 $\mu\in\sigma(A)$，$g_\mu=\dim\ker(\mu I-A)$：
$$\operatorname{rank}P(\mu)\le\operatorname{rank}\big(X(\mu I-A)V\big)+\operatorname{rank}(EV)\le(d-g_\mu)+a .$$
故 $g_\mu>a$ ⇒ $\operatorname{rank}P(\mu)<d$ ⇒ 不可行。

**新的必要条件**：
$$\boxed{\text{可行}\ \Longrightarrow\ \text{每个 }\mu\in\sigma(A)\text{ 的几何重数 }g_\mu\le a=\dim(U\cap T).}$$

## 与旧结果的关系

- 720（$Z'=0$）是特例；
- 722 的 $d=1$ 证明是 $a\le1$ 的直接情形；
- 723/724 的猜想与障碍**解决**：不变性由商空间桥接推出，不需要“行-列直接桥接”。

## 检验

- 638：$a=0$（707）⇒ $Z(\operatorname{im}H)\subseteq\operatorname{im}H$，与 709 的 $P$ 行在 $U$ 内一致；
- 693（$d'=1$、$U\subseteq T$）：$a=1$，$g_\mu\le1$ 自动成立。

## 状态

- 引理 E：**[已证-纸面]**；
- 引理 F：**[已证-纸面]**；
- $a=0$ 不变性：**[已证-纸面]**；
- 新必要条件 $g_\mu\le a$：**[已证-纸面]**。
