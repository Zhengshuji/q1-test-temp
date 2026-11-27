# 512 改 $A$ 的第三行不能打破 gcd：$(5b)$ 的公共因子是结构性的

> 2026-11-27。511 的门 $(5a)\iff z=xy$ 精确成立，但 $(5b)$ 因公共因子 $q$ 全门失败。
> 本文件检验“只改 $A$ 的第三行”能否打破 gcd：**不能**——只要 $l_2=(1,0,1)$ 且 $D_2=z-xy$，
> 三个子式仍共享同一个二次因子。状态：**[已证-纸面]** + **[精确验证]**。

## 计算

固定 $l_1=(z,x,0)$、$l_2=(1,0,1)$，令 $l_2A=a_2=(\alpha,-1,\alpha+y)$（这正是 $D_2=z-xy$ 的通解：
$D_2=-z\beta-x(\gamma-\alpha)$，要求 $\beta=-1,\ \gamma-\alpha=y$）。

门上 $z=xy$：
$$P(\lambda)=\begin{bmatrix}\lambda xy-x&\lambda x&-x\\\lambda-\alpha&1&\lambda-\alpha-y\end{bmatrix}.$$
三个 $2\times2$ 子式：
$$M_{12}=-x\,Q,\qquad M_{23}=x\,Q,\qquad M_{13}=xy\,Q,\qquad Q(\lambda)=\lambda^2-\lambda(y+\alpha)+1 .$$
所以 $\gcd=xQ$，**与 $\alpha$ 无关**；$Q$ 在 $\mathbb C$ 上必有根 ⟹ $(5b)$ 仍全门失败。

精确核验：[512_verify.py](512_verify.py)（$\alpha=-1$ 的特例给出 $\gcd=x(\lambda^2-\lambda y+\lambda+1)$）。

## 结论

- 改 $A$ 的第三行（等价地改 $a_2$ 的常数部分）**不能**打破 gcd；
- 根因是 $D_2=z-xy$ 把 $a_2$ 的形状锁死为 $(\alpha,-1,\alpha+y)$，而 $M_{12},M_{23},M_{13}$ 都由 $Q$ 整除；
- 要打破 gcd，必须改 $l_2$（或 $l_1$）本身，使 $D_2$ 的通解不再强制这个形状。

## 下一步

取一般的 $l_2=(a,b,c)$（常数，$a,b,c\in\{0,\pm1\}$），重算 $D_1,D_2$ 与门上三个子式，
搜索使 $\gcd_\lambda(M_{12},M_{13},M_{23})=1$ 且 $D_2=c_0(z-xy)$ 的组合。

## 状态

- “改第三行无效”：**[已证-纸面]** + **[精确验证]**；
- 一般 $l_2$ 的搜索：**[未做]**。
