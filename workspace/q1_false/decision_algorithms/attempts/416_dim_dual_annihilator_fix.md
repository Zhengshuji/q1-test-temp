# 416 **更正**：$\dim D^\circ=\omega$（不是 $c$）；铅笔整体落在 $D^\circ$ 里；有效参数受 $n-k\le2p$ 控制

> 本轮"继续推进"时发现一个从 406 起就存在的错误：我把 $\dim D^\circ$ 写成了 $c$。
> 正确的值是 $\omega=k-c$。在 $k=4,c=2$（即 $\omega=2$）的实例上两者**巧合相等**，
> 所以所有数值核对都没暴露它；但它使"$c=2$ 的纤维坍缩到至多一条射影直线"这个结论**只在 $\omega=2$ 时成立**。
> 本文件记录更正，并给出**更强的正确结论**（铅笔整体落在 $D^\circ$ 里 + 有效参数受 $n-k\le2p$ 控制）。

## 目标

1. 更正 $\dim D^\circ$ 与"至多一条 $\mathbb P^1$"的适用范围；
2. 给出两条**新的正确结论**：铅笔的行空间整体落在 $D^\circ$（故 $(5b)\iff R_\lambda+\Phi=D^\circ$），
   以及有效像参数空间维数 $\le n-k\le 2p$；
3. 据此修正确切复杂度定理的假设（需要**固定 $p$**，不只是固定 $c$）。

## 设想与理由

$D^\circ=\{f\in K_0^*:f|_D=0\}$，所以
$$\dim D^\circ=k-\dim D=k-c=\omega .$$
我此前写 $\dim D^\circ=c$；只有在 $k=2c$（即 $\omega=c$）时才对。$c=2$ 的样例 $k=4$ 恰好是这种巧合，
所以 406 的 10 例采样、411 的讨论、甚至专家 109 号 §2.3（"$\dim D^\circ=2$"）都沿用了这个错误。

**新的观察（更关键）**：$P=D^{\perp_{K_0}}$ 的每个 $v$ 满足 $v\perp D$，故对 $d\in D$：
$$\langle v,Ad\rangle=\langle v,Md\rangle+\langle v,A_{21}d\rangle=0+0,$$
因为 $Md\in D$ 且 $A_{21}d\in K_0^\perp$。所以**铅笔的每一行（对任何 $\lambda$）都在 $D$ 上为零**，即
$$\operatorname{row}\bigl(\lambda H-H_A\bigr)\subseteq D^\circ,\qquad\dim D^\circ=\omega .$$

于是 $(5b)$ 不是"秩 $\ge\omega$"，而是"**把 $D^\circ$ 填满**"：

$$\boxed{(5b)\iff R_\lambda+\Phi=D^\circ\ \ \forall\lambda,\qquad R_\lambda:=\operatorname{row}P_D(\lambda).}$$

## 做法

先在两个实例上精确核对（`c410`），再把 $v\in P$ 的配对算清楚，最后改各文档。

## 进展

### A. 精确核对（`c410`）

两个实例（$M=\operatorname{diag}(1,1,2,3)$ 与 $\operatorname{diag}(1,1,1,2)$，$n=8,k=4$）上：

| 检查 | 结果 |
|---|---|
| $k-c$ 与 $\omega=\rank H$ | 都是 $2$ ✓（**注意这是巧合**：$k=2c$） |
| $H$ 的行是否全在 $D^\circ$（即在 $D$ 上为零） | **是** ✓ |
| $\lambda H-H_A$ 的行（$\lambda=0,1,2,5$）是否全在 $D^\circ$ | **是** ✓，且 $\rank\le k-c$ ✓ |

### B. 更正后的结论

**结论 1（铅笔受限于 $D^\circ$）.** 对一切 $\lambda$，$\operatorname{row}(\lambda H-H_A)\subseteq D^\circ$，
$\dim D^\circ=\omega$；因此 $\rank(\lambda H-H_A)\le\omega$ 自动成立，而 $(5b)$ 等价于
$$\operatorname{row}(\lambda H-H_A)=D^\circ\quad\forall\lambda,\qquad\text{即}\qquad R_\lambda+\Phi=D^\circ\ \forall\lambda .$$

**结论 2（$\Phi$ 是移动族的"一致补空间"）.** $\Phi\subseteq D^\circ$ 必须与每个 $R_\lambda$ 一起张成 $D^\circ$；
等价地
$$\dim\Phi-\dim(\Phi\cap R_\lambda)=\omega-r_D(\lambda)\quad\forall\lambda .$$
这正是专家 110 号 §6.1 说的"移动行空间与 $\Phi$ 的交互"，而且现在两边都在同一个 $\omega$ 维空间 $D^\circ$ 里。

**结论 3（必要条件）.** 由 $\dim(R_\lambda+\Phi)\le r_D(\lambda)+\dim\Phi$ 得
$$\max_\lambda\bigl(\omega-r_D(\lambda)\bigr)\ \le\ \dim\Phi\ \le\ \min\bigl(t,\ \rank\varphi\bigr)\ \le\ \min(t,\ n-k)\le 2p .$$
即：**只有当场"秩亏"至多 $n-k$（$\le2p$）时，该层才可能可行**。这是一条新的、可算的必要条件。

**结论 4（有效参数空间）.** $\Phi=\varphi(W)$ 落在 $\varphi(T_D)$ 里，而
$$\dim\varphi(T_D)\le\dim T_D=(n-k)-r(D)\le n-k\le 2p .$$
所以有效像参数空间是 $\operatorname{Gr}(\le\min(t,2p),\ \varphi(T_D))$，其维数
$$\le\Bigl\lfloor\frac{\min(t,2p)^2}{4}\Bigr\rfloor\le p^2 .$$

### C. 必须更正的旧说法

| 旧说法（406/410/411/414/论文稿） | 更正 |
|---|---|
| $\dim D^\circ=c$ | $\dim D^\circ=\omega=k-c$ |
| "$c=2$ 时有效 $\Phi$ 至多一条 $\mathbb P^1$/至多一个射影直线分量" | 只在 $\omega\le2$（即 $k=2c=4$）时如此；一般 $c=2$ 时 $\Phi$ 是 $\operatorname{Gr}(\le\min(t,2p),\varphi(T_D))$ 的点，维数 $\le p^2$ |
| 一般 $c$ 的有效纤维维数 $\lfloor c^2/4\rfloor$ | $\le\lfloor\min(t,2p)^2/4\rfloor\le p^2$（**与 $c$ 无关**，只与 $p$ 有关） |
| 复杂度定理假设"固定 $c$ + 单谱" | 还要**固定 $p$**（或等价地 $n-k$ 有界），否则像参数空间的维数随 $k$ 增长 |

**注**：$c=1$ 论文的复杂度定理里出现的是 $n^{O(p^2)}$——正是这里的 $p^2$，说明两边是同一个量；
此前 406/410 把它误记成 $c^2$ 的来源，是同一个错误的另一面。

### D. 修正后的复杂度定理（陈述）

> **定理（$c=2$，修正版）.** 假设 (i) $c=2$；(ii) $M$ 单谱；(iii) $K_0$-split；(iv) **$p$ 固定**（故 $n-k\le2p$）。
> 则二值判定在 $\mathrm{poly}(n,\tau)$ 内完成。

*要点*：底有限 $O(k^2)$ 点；每点的有效像参数在 $\varphi(T_D)$（维 $\le2p$，**常数**）里，
故图卡数与每卡变量数都是常数（关于 $k$）；$\deg_s\le1$、$\deg_\lambda\le\omega$、高度 $\mathrm{poly}$ ⟹
$O(k^2)\cdot\mathrm{poly}(n,\tau)$。

*（原版只写"固定 $c$"是不够的：$k$ 增大时 $\omega=k-2$ 与 $\dim D^\circ$ 都增大，
虽然 $\Phi$ 仍受 $\varphi(T_D)$ 限制，但"至多一条 $\mathbb P^1$"的论证不成立，需改用结论 4。）*

## 最终结论

1. **错误确认**：$\dim D^\circ=\omega$，不是 $c$；"至多一条 $\mathbb P^1$"只在 $\omega\le2$ 时成立；
2. **两条新结论**（更强、更干净）：铅笔整体落在 $D^\circ$ 里（$(5b)\iff R_\lambda+\Phi=D^\circ$），
   且有效参数空间受 $n-k\le2p$ 控制、维数 $\le p^2$；
3. **复杂度定理的假设要加"固定 $p$"**；错误修正后结论仍成立，且与 $c=1$ 论文的 $n^{O(p^2)}$ 同源；
4. 论文稿的 Remark 5、Definition 2、Theorem 15 的假设与 Section VII 的表述必须按此改。

## 放弃原因

- 没有在 $k>4$（即 $\omega>2$）的实例上重新验证一遍"至多 $\mathbb P^1$ 失效"的具体形态
  （`c410` 只用了 $k=4$ 的两个实例；构造 $k=6$ 的实例需要重写底座）；
- 没有把"$\max_\lambda(\omega-r_D(\lambda))\le\dim\Phi$"这条必要条件写成算法步骤
  （它需要枚举 $P_D(\lambda)$ 的秩降点，属实现细节）；
- 没有重算 §D 定理的显式常数。

## 残留价值

- **一个必须记录的更正**（$\dim D^\circ=\omega$），以及它在文献链上的传染范围
  （406 的采样、411、以及专家 109 号 §2.3 都沿用了它）；
- **两条更强的正确结论**：铅笔受限于 $D^\circ$、$\Phi$ 是移动族的一致补空间；有效参数 $\le p^2$；
- **新的必要条件**：$\max_\lambda(\omega-r_D(\lambda))\le n-k$；
- 与 $c=1$ 论文的 $p^2$ 对上，解释了此前"$c^2$"的来历。

## 相关文件

- [attempts/406](../../c_stratification/attempts/406_eliminate_W.md)（像约化；$\dim D^\circ$ 处需改）
- [attempts/410](../../c_stratification/attempts/410_general_c.md)（一般 $c$ 的 $\lfloor c^2/4\rfloor$ 需改为 $\le p^2$）
- [attempts/411](411_expert109_audit.md)（§2.3 的"至多一个射影直线分量"需限定）
- [attempts/414](414_expert110_audit.md)（二值化的论证不依赖 $\dim D^\circ$，**不受影响**）
- 论文稿：[paper_drafts/paper_IV_c2.md](../../../../archive/paper_drafts/workspace_2026-11/paper_drafts/paper_IV_c2.md)（Remark 5、Def 2、Thm 15、§VII）
- 脚本：[c410](../../../../tools/verification/c410_dual_annihilator_dim.py)
