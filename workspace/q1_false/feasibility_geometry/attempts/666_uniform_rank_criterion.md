# 666 统一恒秩判据（Theorem U）与放弃逐 $d$ 分类

> 2026-11-27。针对“$d=2$ 做完 $d=3$ 又要补、最终像 $c$-分层一样没有统一方法”的担心，向 ChatGPT 咨询；
> 结论：逐 $d$ 分类**可以避免**，统一判据是最大子式理想；665 应作为它的特例。
> 状态：**[已证-纸面]**（Theorem U 的 1–3 等价）+ **[M2 战略判断]**。

## Theorem U（仿射铅笔的统一恒秩判据）

设 $P(\lambda)=\lambda H-H_A\in\mathbb C[\lambda]^{m\times n}$，$1\le d\le\min(m,n)$。则等价：

1. $\operatorname{rank}P(\lambda)=d$ 对所有 $\lambda\in\mathbb C$；
2. 所有 $(d+1)$ 阶子式恒为零，且所有 $d$ 阶子式的 $\gcd$ 为 1；
3. 所有 $(d+1)$ 阶子式恒为零，且存在多项式 $g_I$ 使
   $$\sum_{I}g_I(\lambda)\Delta_I(\lambda)=1;$$
4. normal rank 为 $d$，且非零 Smith 不变因子全为 1。

**证明**：$1\iff2$：秩 $\le d$ ⇔ $(d+1)$-子式全零；秩 $\ge d$ 处处 ⇔ $d$-子式无公共复根 ⇔ gcd=1（$\mathbb C[\lambda]$ 是 PID + 代数基本定理）。
$2\iff3$：Bézout。$2\iff4$：最大子式 gcd = 不变因子之积。

## 关键：它同时覆盖模板与非模板

$I_{d+1}(P)=0$ 与 $I_d(P)=\mathbb C[\lambda]$ 只依赖铅笔本身，不依赖 $VZ'=0$ 与否。

## 665 是 Theorem U 的推论（验证）

模板 $VZ'=0$、$\operatorname{row}(V)\subseteq S$、$H=UV$、$B=ZU$：
$$P(\lambda)=(\lambda U-B)V .$$
由 Cauchy–Binet（$V$ 为 $d\times k$，$(\lambda U-B)$ 为 $q\times d$）：$P$ 的每个 $d$ 阶子式
$$\Delta_{I,K}(P)=\det\big((\lambda U-B)_{I,[d]}\big)\cdot\det\big(V_{[d],K}\big).$$
于是：
- 所有 $(d+1)$ 阶子式恒零（因 $P$ 分解过 $d$ 维）；
- $\gcd$ 为 1 $\iff$ $\gcd_I\det((\lambda U-B)_{I})\cdot(\text{常数因子})=1$ $\iff$ $\operatorname{rank}(\lambda U-B)=d\ \forall\lambda$（Theorem U）。

后者：$q=d$ 时 $\det(\lambda U-B)$ 是首一 $d$ 次多项式，必有根 ⇒ 失败；$q\ge d+1$ 时可构造（665 的 $U=[I;0]$、$B=[N;e^{\mathsf T}]$、$e$ 避开 $N$ 的特征向量）。
再加大 $E=S\cap\ker(Z'^{\mathsf T})$ 的维数条件（存在 $V$）即得 665。

## 661 在统一判据下的解释

661 的 $d=2=q$：$P=(\lambda I_2-Z)H$，$\det P=\det(\lambda I_2-Z)\det H$；$2\times2$ 子式只有 $\det P$，$\gcd=\det P$ 非常数 ⇒ Theorem U 直接判不可行（无需逐层列论证）。

## 战略判断（ChatGPT）

- **逐 $d$ 分类不是必然的**：统一对象是最大子式理想 $I_d(P)$ 与 Bézout 证书；
- **665 不废弃**：它是统一判据在模板设计空间上的强化结果，不是一般理论的基础；
- **统一恒秩判据 ≠ 统一 q1 算法**：真正困难转移到“设计变量 $U$ 的存在性”——Bézout 辅助变量与 $U$ 的乘积使系统非线性，实可行性与消元复杂度仍是障碍；
- 与 $c$-分层的区别：这里有一元多项式环 PID 这个强工具，但设计空间的一般秩层几何仍可能重现 S3 式障碍。

## 建议的短周期任务（不做 $d=2$/$d=3$ 分类）

1. 写出 Theorem U 的完整纸面证明（含 Smith 版本）；
2. 用 Theorem U 重推 663（$d=1$）与 665（模板），确认无额外假设；
3. 对 661 计算最大子式 gcd，验证统一判据捕捉其真实障碍；
4. 建立“$U$ + Bézout 辅助变量”的统一代数系统，研究其可行性与复杂度；
5. 之后再决定 $d=2$ 是否需要独立分类。

## 状态

- Theorem U：**[已证-纸面]**；
- 665 由 Theorem U 推出：**[已证-纸面]**（Cauchy–Binet 推导）；
- 661 的统一解释：**[已证-纸面]**；
- 设计变量统一系统：**[未做]**。
