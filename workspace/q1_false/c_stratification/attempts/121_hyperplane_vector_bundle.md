# 超平面情形的向量丛分解定理（$k=\omega+1$）

> 2026-11-08。按专家 54 号的新结果：$k=\omega+1$ 时，$R$ 的约束是**线性**的
> $Rv=0,\ RAv=0$，$v=N\sigma^\top$；纤维是向量丛，分量由**特征向量**决定。
> 定理：lifted incidence 的非空不可约分量 $\le\delta+1$（$\delta=\dim\ker T$），$\delta=2$ 时至多 3 个。
> 状态：**M2（纸面）**；对 11 个例子的分量数核对。

## 目标

设 $k=\omega+1$（**超平面情形**），$S=\ker\sigma$，$N=N_K$，$v=N\sigma^\top\in K$。
证明：

> **定理（超平面向量丛分解）**：设 $K_0=\{N\sigma^\top:\sigma E^\top=0,\ \sigma F_0^\top=0\}$，
> $D_A=K\cap A^{-1}K$，$\delta=\dim D_A=\dim\ker T$。则 lifted incidence 空间的非空不可约分量
> $$\le\delta+1.$$
> 分量落在：
> * 非特征向量的开集 $\mathcal B_2=\mathbb P(K_0)\setminus\mathcal B_1$（若非空）；
> * 特征向量 locus 的各个射影线性子空间
>   $\mathbb P(K_0\cap\ker(A-\lambda I))$（$\lambda\in\operatorname{spec}(A)$）。
> 每个非空分量是其底分量上某个向量丛的开子集。

## 设想与理由

* 对固定 $S$，$\operatorname{row}(RN)\subseteq S$ 与 $\operatorname{row}(RAN)\subseteq S$ 等价于
  $$Rv=0,\qquad RAv=0,$$
  这是 $R$ 的**线性**方程。
* 对一行 $r$，$r\mapsto(rv,rAv)$ 的秩是 $\operatorname{rank}[v,Av]=:\rho(v)\in\{1,2\}$；
  核维数 $n-\rho(v)$。
* $\rho(v)=1\iff Av\in\mathbb Cv\iff v$ 是 $A$ 的特征向量；这给出**射影特征子空间**的并。
* 在常 $\rho$ 的底片上，核构成向量丛；$\operatorname{rank}H=\omega$ 与 $\operatorname{rank}[L_0;R]=q$ 都是开条件。
  所以 lifted incidence 的每一片是**不可约向量丛的开子集**，若非空即不可约。

## 做法

**1. 线性约束。** 对一行 $r$：$rN\sigma^\top=rv$，$rAN\sigma^\top=rAv$。故
$$\operatorname{row}(RN)\subseteq S\iff Rv=0,\qquad \operatorname{row}(RAN)\subseteq S\iff RAv=0.$$

**2. 约束的秩。** 两个线性泛函 $r\mapsto rv$、$r\mapsto rAv$ 独立 $\iff$ $v,Av$ 独立；故秩
$$\rho(v)=\operatorname{rank}[v,Av]\in\{1,2\}.$$
单行核维数 $n-\rho(v)$；$m$ 行共 $m(n-\rho(v))$ 维。

**3. 底空间。** $E+F_0\subseteq S\iff\sigma e^\top=0,\ \sigma f^\top=0$（$e\in E,f\in F_0$）。
在 $N$ 下即 $v\in K_0$，故底空间是 $\mathbb P(K_0)$，不可约（$K_0\ne0$ 时）。

**4. 特征向量 locus。** $\rho(v)=1\iff Av\in\mathbb Cv$，故
$$\mathcal B_1=\bigcup_{\lambda\in\operatorname{spec}(A)}\mathbb P\big(K_0\cap\ker(A-\lambda I)\big).$$
每个非空项是射影线性子空间，故不可约；不同 $\lambda$ 的特征子空间交为零，故这些项**两两不交**。
$\mathcal B_2=\mathbb P(K_0)\setminus\mathcal B_1$ 是非空开集，故不可约。

**5. 分量数。** 每个特征向量 $v$ 属于 $D_A=K\cap A^{-1}K$（因为 $Av\in\mathbb Cv\subseteq K$）。
不同特征值的特征子空间线性独立，故非空特征子空间的个数 $\le\dim D_A=\delta$。
加上 $\mathcal B_2$（若非空），总数 $\le\delta+1$。

**6. 向量丛与不可约性。** 在每片（常 $\rho$）上，$R$ 的解空间是秩 $m(n-\rho)$ 的向量丛；
$\operatorname{rank}H=\omega$（$H$ 的行都在 $S$，这是最大秩开条件）与 $\operatorname{rank}[L_0;R]=q$
都是开条件。故 lifted incidence 在该片上是不可约向量丛的开子集；非空即不可约。

**7. 秩恒等式（专家 54 号）**：
$$\operatorname{rank}\begin{bmatrix}P\\Q\end{bmatrix}=\delta-2+\operatorname{rank}[v,Av],\qquad
\operatorname{rank}Q=\begin{cases}\delta-1,&v\in D_A,\\ \delta,&v\notin D_A.\end{cases}$$
证明：堆叠映射的核 $\cong\ker[v,Av]$（$Z_1u=a\sigma^\top$、$Z_2u=b\sigma^\top$，$av+bAv=0$），
秩-零化度给出第一式；第二式由 $\operatorname{rank}Z_2=\delta$ 与 $\operatorname{rank}Q=\delta-\dim(\operatorname{im}Z_2\cap\operatorname{span}\sigma)$ 给出。

## 进展

* 定理的七步已写；核心是“约束线性 + 特征向量 locus + 向量丛开集”。
* 对 11 个例子（5 个 $e=0$ + 6 个 $e=1$）的分量数核对：
  * $d=1$（$\delta=1$）：$\le2$；104 的 $\mathbb P^1$ 正好是“开集 + 一个特征点”；
  * $d=2$（$\delta=2$）：$\le3$；138 的两个可容许点都是特征点（无开分量）；261 有“线 + 开集”（2 个）；
  * 753/1081/1327/1491/1163/302 的分量数都不超过 $\delta+1$。
* 定理只给分量数；每个分量上的**好坏**仍由 generic gcd 判定（104 的 $\lambda t$、例外点的 $1$ 等）。

## 最终结论

* $k=\omega+1$ 时，lifted incidence 的分量数 $\le\delta+1$，$\delta=2$ 时至多 3 个——**不是 16**，也不是“不可约分解难题”。
* 分量由 $A$ 的特征向量决定：非特征开集 + 各特征子空间。
* 这把 Q9 在超平面情形**基本解决**（分量与纤维都是线性的/向量丛）；剩下的只是每分量的 gcd 与实点。
* 一般 $c=k-\omega>1$ 才是真正的新几何：$\{V\in\operatorname{Gr}(c,K_0):\dim(V+AV)\le s\}$。

## 放弃原因

* 只处理 $k=\omega+1$；$c>1$ 未做。
* 每分量的 generic gcd 未算（只给了分量数）。
* 实点未处理。

## 残留价值

* 一个干净的结构定理，直接取代了 120 的 16 分量粗界。
* 把“分量分解”从代数几何难题降成“特征向量 + 向量丛”。
* 为论文的“超平面”一节提供主定理；为 $c=2$ 的一般化提供对照。

## 相关文件

* [attempts/120](120_base_component_bound.md)（旧的 16 分量界）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（一般定理）
* [attempts/114](114_lifting_lemma.md)（lift）
* [attempts/104](104_p2_constrained_locus.md)（$d=1$ 例子）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（分量复杂度）

## 状态

* 定理：**[已证-纸面，M2]**（按专家 54 号的论证）。
* 例子核对：**[精确验证 11 实例]**（分量数）。
* 未做：每分量 gcd、$c>1$、实点。
