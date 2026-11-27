# $P(A,B,S)$：下界与一步递归定理

> 本目录：`theorem.md`（证明）｜`algorithm.md`（算法）｜`verification.md`（验证）｜`scripts/`｜`lean/`

## 1. 问题与文献位置

$$P(A,B,S)=\min\{\dim W:\ W\supseteq S,\ AW\subseteq W+B\}$$

等价形式：
$$P=\min_{\varphi\in\operatorname{Hom}(X,B)}\dim\langle S\rangle_{A+\varphi}\qquad(\text{项目已验 }40/40)$$

**文献**：Warren–Eckberg（SIAM J. Control 13, 1975）§5 明确写"最小维数 c.s. 含任意子空间仍是 open"。
但注意其对象是 **controllability subspace（c.s.）**；本问题的 **$(A,B)$-不变** 版本与之只在 $D\subseteq B$ 时重合
（Wonham–Morse, Automatica 8 (1972) Thm 2.1；见项目 `../../archive/process_logs/REVIEW_LOG.md` 记录 5 Remark 4）。
所以本文的结果与文献的 open 问题**不冲突**：解决的是 $(A,B)$-不变版本。

**与 $q1$ 的关系**：MIN-ROWS 的 $q_{\min}=\min\{\rho+c\}$，其中 $\rho=\dim\pi(V)$ 的下界正是 $P$ 型量
（$U\supseteq U_0$ 的 $(T,B)$-不变最小维数）。所以本文把 $q1$ 的**算术侧**解决了；$(5b)$/层结构仍独立。

---

## 2. 定理 1（下界）

设 $M=S+B$、$r=\dim\frac{AS+M}{M}$。则对任意可行 $W$（$W\supseteq S$、$AW\subseteq W+B$）：

$$P\ \ge\ \dim S+r .$$

**证明.** $AW\subseteq W+B\Rightarrow AS+M\subseteq AW+M\subseteq W+M$，故
$r\le\dim\frac{W+M}{M}$。又 $\frac{W+M}{M}\cong\frac{W}{W\cap M}$，而 $W\cap M\supseteq S$，故
$\dim\frac{W+M}{M}\le\dim\frac{W}{S}=\dim W-\dim S$。$\square$

---

## 3. 定理 2（一步递归）

**类.** 数据 $(Y,\ C\subseteq Y,\ \Phi:Y\to Y/C,\ T\subseteq Y)$；$U$ 可行 $\iff$
$T\subseteq U$ 且 $\Phi U\subseteq (U+C)/C$。记 $\mathcal P$ 为最小维数。

**定理.** 令 $M=T+C$，$\pi:Y\to Y/M$，$\bar\pi:Y/C\to Y/M$，
$$C'=\bar\pi\Phi(M),\qquad T'=\bar\pi\Phi(T),\qquad \Phi'=\Phi\bmod M .$$
则
$$\mathcal P(Y,C,\Phi,T)=\dim T+\mathcal P(Y/M,\,C',\,\Phi').$$

**良定性.** $y'=y+m\Rightarrow\Phi(y')=\Phi(y)+\Phi(m)$ 且 $\Phi(m)\in\Phi(M)$，故
$\bar\pi\Phi(m)\in C'$，$\Phi'$ 在 $(Y/M)/C'$ 里良定义。$\square$

**$({\ge})$.** 取可行 $U$，令 $\bar U=\pi U$。$T\subseteq U\cap M$ 给
$\dim U=\dim(U\cap M)+\dim\bar U\ge\dim T+\dim\bar U$；而 $\bar U$ 在 level 1 可行
（$T'\subseteq\bar U$：由 $\Phi(t)=u'+C,\ u'\in U$；可行性由 $\bar\pi'\Phi(U)\subseteq(\bar U+C')/C'$）。$\square$

**$({\le})$.** 取截面 $s:Y/M\to Y$（$\pi s=\mathrm{id}$），$E_0=s(U')$，一般提升
$E_\sigma=\{s(u)+\sigma(u)\}$，令 $U=T\oplus E_\sigma$。
- $T$ 部分：$\bar\pi\Phi(T)=T'\subseteq U'=\pi(E_\sigma)$，故 $\Phi(T)\subseteq E_\sigma+M=U+C$；
- $E$ 部分：level 1 可行性给 $\pi\Phi(s u)\in U'+C'$，即存在 $m\in M$ 使
  $\pi(\Phi(su)+\Phi(m))\in U'$。映射 $M\to C'$，$m\mapsto\bar\pi\Phi(m)$ **满射**（$C'$ 的定义），
  故 $\to C'/(C'\cap U')$ 仍满射；逐基向量取原像并线性延拓得 $\sigma$。$\square$

---

