# 736 ChatGPT 的商空间方向性猜想 (D)
> **已证（737）**：$\dim E_H\le\dim(U\cap T)+\operatorname{cls}\le\dim(U\cap T)+\operatorname{rank}(HM)$；见 737。


> 2026-11-27。ChatGPT 建议在定理 B（734）基础上证明 $E_H/(U\cap T)$ 被 $\operatorname{rank}(H(\mu I-Z'))$ 控制。
> 状态：**[猜想]**（未证）。

## 猜想 (D)

设 $T$、$U=\operatorname{row}H$、$V=U\cap T$、
$$E_H=\operatorname{span}\Big(\bigcup_i\big(T\cap(U-H_iZ')\big)\Big),\qquad M=\mu I-Z' .$$
则
$$\boxed{\dim E_H\ \le\ \dim(U\cap T)+\operatorname{rank}(HM).}$$

等价形式：$\dim\big(E_H/(U\cap T)\big)\le\operatorname{rank}(HM)$。

若成立，代入 734（$d'\le\operatorname{rank}(HM)+\dim E_H$）得
$$d'\ \le\ \dim(U\cap T)+2\operatorname{rank}(HM).$$

## 观察

- 关键恒等式：$H_iZ'=H_i(\mu I-M)=\mu H_i-H_iM$，且 $H_i\in U$，故
  $$U-H_iZ'=U+H_iM\quad(\text{平移意义}),$$
  所以 $F_i:=T\cap(U-H_iZ')=T\cap(U+H_iM)$。
- 因此 $E_H=\sum_i F_i$，其“超出 $U\cap T$ 的部分”应受 $H_iM$（即 $HM$ 的行）约束——这正是 (D) 的直觉。
- 难点：$E_H$ 是各行 $F_i$ 的**和**，跨行的线性组合可能产生额外维数；不能逐行相加。

## 验证

- **733**：$U=\mathbb C^2$、$T=\operatorname{span}\{e_1\}$，故 $V=U\cap T=T$，$\dim(E_H/V)=0\le\operatorname{rank}(HM)=1$ ✓（平凡）；
- **638**：$T=\operatorname{span}\{e_1\}$、$U\cap T=0$（707），$E_H$ 需要具体计算；若 (D) 成立可给更强筛选。

## 证明策略（ChatGPT 建议）

构造线性映射
$$\Phi:E_H\longrightarrow\operatorname{row}(HM),\qquad \ker\Phi=U\cap T,$$
再用秩-零化度定理。关键是保证 $\Phi$ 在不同 $F_i$ 之间定义一致。

## 与 734/695 的关系

- 734（B）：$d'\le\operatorname{rank}(HM)+\dim E_H$（已证）；
- 695：$d'\le\dim(\operatorname{row}(HM)+T)$（已证，通常更强，除非 $E_H$ 远小于 $T$）；
- (D) 若成立，可把 734 的 $E_H$ 换成 $U\cap T$ 与 $\operatorname{rank}(HM)$ 的更细组合。

## 下一步

1. 先做 $t=2$ 或 $t=3$ 的数值检验：随机相容 $H$，比较 $\dim E_H$ 与 $\dim(U\cap T)+\operatorname{rank}(HM)$；
2. 若找到反例，记录跨行组合产生额外维数的具体机制；
3. 若无数值反例，尝试构造 $\Phi$ 并证明一致性。

## 状态

- (D)：**[猜想]**；
- 733 检验：**[平凡成立]**；
- 数值检验（$t\ge2$）：**[未做]**。
