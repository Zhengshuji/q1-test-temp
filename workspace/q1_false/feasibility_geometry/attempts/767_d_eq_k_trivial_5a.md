# 767 $d'=k$ 时 $(5a)$ 自动成立；非退化区域是 $d'<k$

> 2026-11-28。由 764 的结构恒等式推出：$U=\mathbb C^k$（$d'=k$）时 $(5a)$ 恒成立，判定退化为纯 $(5b)$；只有 $d'<k$ 时 $(5a)$ 才是真正的约束。
> 状态：**[已证-纸面]**。

## 定理

设标准块形（$N=[I_k;0]$、$CN=0$、$CW=0$、$\operatorname{rank}[C;CA]=n-k$），$L$ 满足 $LN=H$，$U=\operatorname{row}H$，$d'=\dim U$。则
$$\boxed{\dim\operatorname{row}[L;CA;C]=(n-k)+d'.}$$

**证明**：$[C;CA]$ 的行张成 $\{0\}\times\mathbb C^{n-k}$（因 $CN=0$、$CW=0$ 且秩 $n-k$）。故
$$\operatorname{row}[L;CA;C]=\operatorname{row}L+(\{0\}\times\mathbb C^{n-k}).$$
投影 $\pi:\mathbb C^n\to\mathbb C^k$（前 $k$ 坐标）在 $\operatorname{row}L$ 上的像为 $\operatorname{row}(LN)=\operatorname{row}H=U$，核为 $\operatorname{row}L\cap(\{0\}\times\mathbb C^{n-k})$，维数
$$\dim\operatorname{row}L-\dim U .$$
而 $\operatorname{row}L$ 含 $\{0\}\times\mathbb C^{n-k}$ 的部分？$\operatorname{row}L$ 本身投影到 $U$，故其与 $\{0\}\times\mathbb C^{n-k}$ 的交维数 $=\dim\operatorname{row}L-d'$；于是
$$\dim(\operatorname{row}L+\{0\}\times\mathbb C^{n-k})=\dim\operatorname{row}L+(n-k)-(\dim\operatorname{row}L-d')=(n-k)+d'. \qquad\square$$

（$\operatorname{rank}L$ 可以大于 $d'$；上式只用 $\operatorname{row}L\to U$ 的投影。）

## 推论

1. **$d'=k$**（$U=\mathbb C^k$）：$\dim\operatorname{row}[L;CA;C]=n$ ⇒ $(5a)$ 两侧都满秩 $n$，**自动成立**；可行性 $\iff$ $(5b)$（即 $\gcd=1$）。
   - 733、747 正是这种情形，所以它们只检验 $(5b)$；
   - 638 的 $d'=2<k=3$，不在其中。
2. **$d'<k$**：$\dim\operatorname{row}[L;CA;C]=(n-k)+d'<n$，$(5a)$ 是非平凡约束——这是 764 的实例（$n=6,k=2,d'=1$，秩 5<6）。
3. 因此“非退化”与“$d'<k$”等价（在标准块形下）。

## 意义

- 把研究空间分成两块：
  - $d'=k$：问题退化为 $(5b)$ 的 $\exists H$（733/747 的区域）；
  - $d'<k$：$(5a)$ 与 $(5b)$ 耦合（764 的区域），也是 761 的 $(Z'',G')$ 机制真正起作用的地方。
- 此前很多例子（638 除外）落在 $d'=k$，导致 $(5a)$ 的约束被低估；764 修正了这一盲点。

## 待办

1. 在标准块形之外（$CN\ne0$ 或 $CW\ne0$）验证恒等式是否仍成立；
2. 发展 $d'<k$ 的 $(5a)$ 判据（$H$ 行空间的 Grassmann 条件）；
3. 把 $d'<k$ 与 761 的 $F_U$ 维数（$E_H$ 等式）结合。

## 状态

- 定理：**[已证-纸面]**（标准块形）；
- 推论：**[已证-纸面]**；
- 非块形推广：**[待做]**。
