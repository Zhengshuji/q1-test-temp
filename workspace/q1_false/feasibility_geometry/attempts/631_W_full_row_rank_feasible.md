# 631 定理：$W$ 满行秩时 q1 可行（无 hardness 入口）

> 2026-11-27。由 630 的分解，证明 $W$ 满行秩时可行性几乎总是成立——这一支不承载 hardness。
> 状态：**[已证-纸面]**。

## 定理

设 $\operatorname{row}(W)=\mathbb C^k$（$W$ 满行秩），$q>r_0$（有自由行），$q-1\le k$，且
$\operatorname{rank}H_0\le q-1$。则存在 $L$（$q$ 行）满足 $(5a)(5b)$；即该实例可行。

## 证明

1. **选 $H$**：取 $q\times k$ 矩阵 $H$，前 $r_0$ 行等于 $H_0$，且 $\operatorname{rank}H=q-1$。
   存在性：$\operatorname{rank}H_0\le q-1\le k$，把 $H_0$ 的 $r_0$ 行补到 $q-1$ 个线性无关行即可。
   记 $\omega=q-1$，$V=\operatorname{im}H\subseteq\mathbb C^q$，$\dim V=q-1<q$。
2. **选 $Z$**：取 $q\times q$ 矩阵 $Z$，使其所有特征向量**都不在** $V$ 内。
   存在性：$V$ 是超平面；取 $Z$ 有 $q$ 个互异特征值、特征向量为一般位置的向量
   （避开 $V$ 是开条件，非空）。
3. **取 $H_A=ZH$**。则：
   - $(5a)$：$Hv=0\Rightarrow H_Av=Z(Hv)=0$ ✓；
   - $(5b)$：$\lambda H-H_A=(\lambda I-Z)H$，秩 $=\operatorname{rank}\big((\lambda I-Z)|_V\big)=q-1=\omega$（$V$ 不含 $Z$ 的特征向量）✓。
4. **实现 $H_A$**：需要 $H_A=HZ'+G$ 且 $G$ 可由自由行实现（$\operatorname{row}(G)\subseteq\operatorname{row}(W)$）。
   由 630，$G=H_A-HZ'=ZH-HZ'$，其行属于 $\mathbb C^k=\operatorname{row}(W)$；
   因 $W$ 满行秩，存在 $L_Y$（自由行的 $Y$ 部分）使 $L_YW=G$（W 有右逆）✓。
   $H$ 的自由部分由 $R_N N=H_{\rm free}$ 实现 ✓。
5. 于是 $L=[L_0;R]$ 可行。$\square$

## 推论

- $W$ 满行秩 + 有自由行 + $q-1\le k$ ⇒ 可行；
- 结合 629（$W=0$ 平凡），**hardness 入口只剩** $\operatorname{row}(W)$ 是真子空间且 $W\ne0$ 的情形；
- 若进一步能证明小秩 $W$ 也总是可行，则 q1_true 完全关闭。

## 备注

- 条件 $q-1\le k$：$q$ 是行数，$k=\dim K_0$；在典型 q1 实例（$q\le k$）中成立；
- 证明只用了 $W$ 的行空间等于全空间；$W$ 的其它结构（如与 $Z'$ 的关系）无关。

## 下一步

1. 研究 $\operatorname{row}(W)$ 真子空间的情形：$G$ 受限，是否仍总能完成铅笔？
2. 若不能，构造数据依赖的不可行例子——那才是 q1_true 的最后入口；
3. 把 629/631 合并为 q1 的分情形定理。

## 状态

- 定理：**[已证-纸面]**；
- $W$ 不满行秩：**[开放]**。
