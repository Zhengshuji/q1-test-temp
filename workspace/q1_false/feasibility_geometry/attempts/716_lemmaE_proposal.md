# 716 ChatGPT 的引理 E（交叠—低秩不变性缺陷）与待核点

> 2026-11-27。记录 ChatGPT 对 714/715 的回应：引理 E/F 与商空间诱导算子的陷阱。
> 状态：**[M2 提案]**（证明待核）。

## 引理 E（它提出）

设 $H=XV$（$X$ 列满秩、$V$ 行满秩，$\operatorname{rank}H=d$），$U=\operatorname{row}(V)$，$T\subseteq\mathbb C^{1\times k}$，且
$$ZH-HZ'=G,\qquad \operatorname{row}(G)\subseteq T .$$
记 $a=\dim(U\cap T)$。则存在 $A\in\mathbb F^{d\times d}$ 使
$$\operatorname{rank}(ZX-XA)\le a .$$

**它的证明思路**：把 $V$ 投影到 $\mathbb C^k/T$；$a=\dim(U\cap T)$ ⇒ $\operatorname{rank}\overline V=d-a$。由 $ZXV-XVZ'=G$ 投影得 $ZX\overline V=X\overline{VZ'}$；取 $A=RZX$（$R$ 为 $X$ 的左逆），得 $(ZX-XA)\overline V=0$，故 $\operatorname{rank}(ZX-XA)\le\dim\ker\overline V^T=a$。

## 需要核验的点（我的疑问）

1. $A=RZX$ 需要 $R$ 是 $X$ 的左逆（$RX=I_d$），但 $X$ 是 $q\times d$ 列满秩，左逆存在当且仅当 $X$ 行满秩？$X$ 列满秩时存在左逆 $R$（$d\times q$）使 $RX=I_d$ ✓（任何列满秩矩阵都有左逆）。
2. 关键等式 $ZX\overline V=X\overline{VZ'}$ 中，$\overline{VZ'}$ 与 $\overline V Z'$ 的关系需要 $Z'$ 在商空间上良定义——**这正是它自己指出的陷阱**：需要 $(U\cap T)Z'\subseteq T$ 才能有诱导作用。
3. $A=RZX$ 后 $(ZX-XA)\overline V=0$ 推出秩 $\le\dim\ker\overline V^T$，但 $\ker\overline V^T$ 的维数是 $k-\operatorname{rank}\overline V=a$？需 $\overline V$ 的行空间维数 $d-a$，其左零空间维数 $k-(d-a)$，不是 $a$。**这里可能有误**：应核对 $\dim\ker(\overline V^T)$ 与 $a$ 的关系（若 $\overline V$ 为 $d\times k$ 行满秩 $d-a$，则左零空间维数 $k-d+a$）。

因此引理 E 的陈述本身可能需修正（$a$ 应出现在不同位置，或需额外假设）。

## 它明确指出的陷阱（有价值）

商空间诱导算子 $\overline{Z_U}:U/(U\cap T)\to U/(U\cap T)$ **不一定存在**；需要
$$(U\cap T)Z'\subseteq T .$$
反例：$U=\mathbb F^2$、$T=\operatorname{span}\{e_1\}$、$Z'=\begin{bmatrix}0&1\\0&0\end{bmatrix}$：$UZ'\subseteq U+T$ 成立，但 $e_1Z'=e_2\notin T$，故诱导作用不良定义。

## 引理 F（它提出）

在引理 E 条件下，$E=ZX-XA$（$\operatorname{rank}E\le a$），对 $\mu\in\sigma(A)$，$g_\mu=\dim\ker(\mu I-A)$：
$$\operatorname{rank}P(\mu)\le d-g_\mu+a,$$
故 $g_\mu>a$ ⇒ 不可行。

## 我们的判断

- 引理 E 的**动机**（$a=\dim(T\cap U)$ 控制不变性缺陷）与 715/714 一致；
- 但证明中的两个步骤（商空间良定义、左零空间维数）需要修正；先作为**[M2 提案]**，不写成定理；
- 它指出的“商空间诱导算子需要 $(U\cap T)Z'\subseteq T$”是重要的负面结论，应记录。

## 下一步

1. 用具体例子（$d=2$、$a=0,1$）数值检验 $\operatorname{rank}(ZX-XA)\le a$ 是否正确；
2. 若陈述有误，找出正确的秩界（可能是 $\le k-d+a$ 或类似）；
3. 再考虑引理 F。

## 状态

- 引理 E：**[M2 提案，证明待核]**；
- 商空间陷阱：**[已记录]**；
- 引理 F：**[未核]**。
