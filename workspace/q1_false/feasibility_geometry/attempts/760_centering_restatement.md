# 760 中心化重述：$(Z'',G')$ 框架下的 697/726/749/753 与 693 证书

> 2026-11-27。按 757/758 的裁决，把核心结论统一到 $Z''=Z'+W_{\mathrm{top}}$、$G'=G-HW_{\mathrm{top}}\in T^q$；并给出 693 的不可行证书。
> 状态：**[已证-纸面]**（重述）+ **[精确验证]**（693）。

## 1. 记号（固定）

$N=\begin{bmatrix}I_k\\0\end{bmatrix}$（若不在此坐标，先做可逆行变换）、$W=\begin{bmatrix}W_{\mathrm{top}}\\W_{\mathrm{bot}}\end{bmatrix}$、$T=\operatorname{row}(W_{\mathrm{bot}})$，
$$Z''=Z'+W_{\mathrm{top}},\qquad G'=G-HW_{\mathrm{top}}\in T^q,$$
$$P(\lambda)=\lambda H-HZ''-G',\qquad ZH=HZ''+G'.$$
$W_{\mathrm{top}}=0$ 时 $Z''=Z'$、$G'=G$，757 之前的结论原样成立。

## 2. 重述的结论

### 2.1 相容性与 $F_i$（697 的中心化）

$(5a)$ 可解 $\iff$ 对每行
$$\boxed{H_iZ''\in U+T,}$$
且此时 $G'_i\in T\cap(U-H_iZ'')$；$F_i:=T\cap(U-H_iZ'')\ne\varnothing\iff H_iZ''\in U+T$。

证明同 697/755，只把 $Z',G$ 换成 $Z'',G'$。

### 2.2 $a\ge1$（726 的中心化）

设可行、$d'>0$。则
$$\boxed{a=\dim(U\cap T)\ \ge\ 1.}$$
证明：725 的引理 F 以 $(Z'',G')$ 重写后给出 $g_\mu=\dim\ker(\mu I-A)\le a$（$A=RZX$），复方阵必有特征值、$g_\mu\ge1$。$\square$

### 2.3 749 的中心化

设 $A=\mu I-Z''$。若
$$\dim\big(\ker A\cap T^\perp\big)\ \ge\ k-d'+1,$$
则不可行。
证明：与 753 相同（用 $G'$ 行在 $T$），只需要把 $Z'$ 换成 $Z''$。

### 2.4 753 的中心化

$$(\star)\ \dim(\operatorname{row}A+T)=k-\dim(\ker A\cap T^\perp),\qquad
(\star\star)\ \operatorname{row}(HA)\subseteq\operatorname{row}A,$$
其中 $A=\mu I-Z''$。于是 749 触发 ⇒ 695（用 $Z''$）失败。证明不变。

### 2.5 695/725/734/739 的替换

- 695：$\dim(\operatorname{row}(H(\mu I-Z''))+T)\ge d'$；
- 725：$g_\mu\le a$，$\mu\in\sigma(A)$；
- 734：$d'\le\operatorname{rank}(H(\mu I-Z''))+\dim E_H$，$E_H$ 用 $Z''$；
- 739：$\dim E_H=\dim(U\cap T)+\operatorname{cls}_\mu$，$\operatorname{cls}_\mu=\dim((U+\operatorname{row}(H(\mu I-Z'')))/U)$。

这些证明只依赖“$G'$ 行在 $T$”与 $P=H(\mu I-Z'')-G'$，故逐字替换成立。

## 3. 693 的不可行证书

693 数据：$N$ 前 2 坐标、$W=\begin{bmatrix}0&1\\0&0\\1&0\\0&0\end{bmatrix}$、$W_{\mathrm{top}}=\begin{bmatrix}0&1\\0&0\end{bmatrix}$、$T=\operatorname{span}\{e_1\}$、$Z'=\begin{bmatrix}0&0\\1&0\end{bmatrix}$、$H=u e_1^{\mathsf T}$（$u=(1,0,1)$，$U=\operatorname{span}\{e_1\}$，$d'=1$）。

$$Z''=Z'+W_{\mathrm{top}}=\begin{bmatrix}0&1\\1&0\end{bmatrix},\qquad
HZ''=\begin{bmatrix}0&1\\0&0\\0&1\end{bmatrix}.$$
第一行 $H_1Z''=e_2$，而
$$U+T=\operatorname{span}\{e_1\}\not\ni e_2 .$$
故相容性失败，$(5a)$ 无解 ⇒ **693 不可行**（与 757 的结论一致，且无需构造 $Z$ 或 $G$）。

## 4. 文档处理

| 文件 | 处理 |
|---|---|
| 692 | 已加 757 横幅；正文的 $G\in T^q$ 应读作 $G'\in T^q$（$Z''$ 框架） |
| 693 | 已加撤回横幅；本文给出不可行证书 |
| 697 | 以本文 2.1 为准 |
| 726/749/753 | 以本文 2.2–2.4 为准（证明不变） |
| 638/733/747 | $W_{\mathrm{top}}=0$，无需改动 |
| 661 | $Z''=A$，结论不变 |

## 状态

- 重述：**[已证-纸面]**；
- 693 证书：**[精确验证]**；
- 下一步：把 744 的预筛选链整体改写为 $Z''$ 版本，然后回到 A（固定 $U$ 的存在性定理）。
