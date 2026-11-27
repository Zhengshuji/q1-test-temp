# 589 $q=3$ 的分类：可行 $\Rightarrow \omega\le1$，rank-1 铅笔

> **已被 590 推翻**：$q=3$、$\omega=2$ 存在可行实例
> （$H=\operatorname{diag}(1,1,0)$、$H_A=ZH$、$Z$ 为三阶循环置换矩阵）。
> 本文件的错误是断言“$\lambda I-Z$ 的 2 维限制必有特征值”——当 $Z$ 的特征向量都在 $\operatorname{im}H$ 之外时并不成立。
> 以下内容保留作记录。

> 2026-11-27。ChatGPT 要求对 $q=3$、$\omega=2$ 的 3×3 铅笔做代数分类。
> **结论：$q=3$ 时可行实例必有 $\omega\le1$；$\omega=2$ 不可能。**
> 状态：**[已证-纸面]**。

## 分类

$P(\lambda)=\lambda H-H_A\in M_3(\mathbb C[\lambda])$。

- $\omega=3$：586 已排除（$\det H\ne0$ ⇒ $\det P$ 非常数 ⇒ 有根）；
- $\omega=2$：$H$ 的秩 2。$\operatorname{row}H$ 是 2 维；$P=(λI-Z)H$ 在 2 维商空间上。
  该 2 维铅笔 $\lambda I_2-Z_2$ 的行列式是二次多项式，在 $\mathbb C$ 上有根 ⇒ 某 $\lambda$ 掉秩 ⇒ $(5b)$ 失败；
- $\omega\le1$：唯一可能。此时 $\operatorname{rank}P=1$ 对所有 $\lambda$（若存在），
  铅笔是 rank-1 的：$P(\lambda)=(\lambda u-v)\,w^{\mathsf T}$（$u,v,w$ 固定向量）。

## 证明细节（$\omega=2$）

$H$ 秩 2 ⇒ 存在 2 维子空间 $W$ 与同构 $W\cong\mathbb C^2$，$H|_W$ 可逆；
$P(\lambda)|_W=H|_W(\lambda I-Z)$，$Z$ 为 $2\times2$。
若 $\operatorname{rank}P(\lambda)=2$ 对所有 $\lambda$，则 $\lambda I-Z$ 对所有 $\lambda$ 可逆——
但 $\det(\lambda I-Z)$ 是二次多项式，在 $\mathbb C$ 上有根。矛盾。$\square$

## 推论

- $q=3$ 的可行实例只能是 rank-1 铅笔 $P=(\lambda u-v)w^T$；
- rank-1 铅笔的极大子式（$1\times1$）互相成比例，无法编码 $r_1r_2=z$ 这类二次关系；
- **$q=3$ 的 3×3 路线到此关闭**：不存在编码乘法的 3×3 构造。

## 与 586 的关系

586 排除了 $\omega=3$；本文件排除 $\omega=2$；只剩 $\omega\le1$，且 rank-1 铅笔没有足够自由度。

## 下一步

转 $q\ge4$ 或非方阵铅笔：此时 $\omega$ 可以严格小于 $q-1$，rank-2 铅笔在更高维空间里可能避开特征值障碍
（正如 520/530 的 $\omega=2<q=3$）。

## 状态

- 分类：**[已证-纸面]**；
- $q=3$ 路线：**关闭**；
- $q\ge4$：**[未做]**。
