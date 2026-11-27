# 765 B 的精确接口：Bézout 形式（不是直接 PIT）

> 2026-11-28。按 ChatGPT 的建议，把 B 的定义层与算法层分开：先固定“$\exists G'$ 使 $\gcd=1$”的 Bézout 等价形式，再谈 PIT。
> 状态：**[整理]** + **[已证-纸面]**（Bézout 等价，引用标准事实）。

## B 的问题

固定 $U$（761），
$$\mathcal F_U=\prod_{i}\big(T\cap(U-H_iZ'')\big),$$
需要判定
$$(\mathrm B)\qquad \exists G'\in\mathcal F_U:\ \gcd\big(f_1(\lambda,G'),\dots,f_m(\lambda,G')\big)=1,$$
其中 $f_j$ 是 $P_{G'}(\lambda)=\lambda H-HZ''-G'$ 的全部 $d'$-子式。

## Bézout 等价（定义层）

对域 $K$ 上的一元多项式 $f_1,\dots,f_m$：
$$\gcd(f_1,\dots,f_m)=1\iff \exists u_1,\dots,u_m\in K[\lambda]:\ \sum_{j=1}^m u_jf_j=1 .$$
（理想 $(f_1,\dots,f_m)=K[\lambda]$ 的标准等价；Mathlib 侧对应 `Ideal.span` 与 `IsCoprime` 的多项式版本。）

**次数界**：若 $\deg f_j\le D$ 且 $\gcd=1$，可取 $\deg u_j\le (m-1)D$（粗略标准界；边界情形单独处理）。于是 $u_j$ 只有有限个标量未知量。

## 参数化后的精确陈述

设 $\mathcal F_U$ 由仿射坐标 $x\in K^N$ 参数化（$G'=G'_0+\sum x_\ell V_\ell$）。则 $f_j(\lambda,x)$ 是 $(\lambda,x)$ 的多项式。$(\mathrm B)$ 等价于
$$\boxed{\exists x\in K^N,\ \exists u_j(\lambda)\ (\deg u_j\le (m-1)D):\ \sum_j u_j(\lambda)\,f_j(\lambda,x)\equiv 1 .}$$
这是**有限个系数方程**（比较 $\lambda$ 的各次幂），变量为 $x$ 与 $u$ 的系数。

## 必须避免的陷阱（ChatGPT 指出）

不能把“$\exists x$ 使 $\gcd=1$”等同于“在 $K(x)$ 上泛型 $\gcd=1$”。反例：
$$f_1=(x\lambda+1)(\lambda+1),\qquad f_2=(x\lambda+1)(\lambda+2).$$
一般 $x$ 有公因子 $x\lambda+1$；但 $x=0$ 时 $f_1=\lambda+1$、$f_2=\lambda+2$，$\gcd=1$。

因此：
- 泛型 gcd 只能给**否定**信息（泛型 gcd=1 ⇒ 存在开集可行），不能替代逐点存在性；
- 参数点处次数下降可使公因子退化，必须用 Bézout 形式逐点判定。

## 算法层（未解决）

- 上面得到的是**多项式方程组可解性**，一般不是 PIT；需要该方程组的特殊结构（仿射线性参数、子式为 $d'$-次）才能谈 PIT/Rabinowitsch；
- 目前没有多项式时间算法，也没有 NP-hard 归约；
- 下一步：先证明 Bézout 系统的结构性质（变量数、次数、是否存在消元），再决定算法路线。

## 与 761 的关系

761 把可行性化为 $(\mathrm B)$；765 把 $(\mathrm B)$ 化为**有限 Bézout 方程组**。两者合起来是：
$$\text{可行}\iff \exists U\ \exists x\ \exists u:\ \sum u_jf_j(\lambda,x)\equiv1,$$
即“Grassmann 参数 $U$ + 仿射参数 $x$ + Bézout 系数 $u$”的三层存在性。

## 待办

1. 用 Mathlib 的多项式 API 形式化小规模版本（例如 $m=2$ 的 Bézout 等价）；
2. 写 $(m,D)$ 次数界的精确陈述与证明（或引用）；
3. 在 764 的非退化实例上验证 Bézout 系统确有解（数值/精确）。

## 状态

- Bézout 等价：**[已证-纸面]**（标准事实）；
- 泛型陷阱：**[已记录]**；
- 算法层：**[开放]**。
