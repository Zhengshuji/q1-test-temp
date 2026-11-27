# 339 富余档实验：没有造出合格层点（失败记录 + 一处被数值否掉的猜想）

> 承接 338（维度图：$n-2-p>k-1$ 只在 $r>p+1$ 时可能出现，故 $p\ge2$）。
> 目标是造 $p=2$ 的富余档实例，看非特征层是否"生成好"。**没成功**，记录在此。

## 目标

构造 $p\ge2$、$r>p+1$ 的实例（$r=\operatorname{rank}[C;CA]$），在非特征层上找一个
$\operatorname{rank}H=\omega$、$(5a)$ 成立、$\gcd=1$ 的层点。

## 设想与理由

取 $n=8$、$p=2$、$q=4$，$C$ 随机 $2\times8$、$A$ 随机 $8\times8$；若 $\operatorname{rank}[C;CA]=4$ 则
$k=4$、$\omega=3$，而 $n-2-p=4>k-1=3$ ⟹ 富余档。
非特征 $v$ 时行空间取 $U^\perp$（6 维）里的随机 4 行，筛 $\operatorname{rank}H=3$、$(5a)$，再算 $\gcd$。

## 做法

照上述直接随机采样（6 个 $(A,C)$、每个 6 组行）。

## 进展

**样本 0 个通过筛选**：$\operatorname{rank}H=\omega$ 或 $(5a)$ 没有一个满足。

诊断时我试了一个"几何解释"：**它是错的**。
我猜 $V\subseteq U^\perp$ 加上 $\omega=\dim(V\cap K_0)\le\dim(K_0\cap U^\perp)=k-\operatorname{rank}(U^{\mathsf T}N)$；
但在 $p=1$ 的已知成功实例上数值核对：

- $\dim(K_0\cap U^\perp)=3-2=1$（按上式），
- 而实测 $\operatorname{rank}H=2=\omega$，且**直接算** $\dim(K_0\cap V^\perp)=1$。

若套用恒等式 $\dim(K_0\cap V)+\dim(K_0\cap V^\perp)=k$，会得到 $\dim(K_0\cap V)=2$，与
$K_0\cap V\subseteq K_0\cap U^\perp$（1 维）矛盾。**所以那个恒等式在这里不成立**——
标准双线性型在 $K_0$ 上可能是**退化**的（$K_0\cap K_0^\perp\ne0$），
"正交补"与"零化子"不能混用。**该猜想作废，未写入任何命题**。

## 最终结论

1. 富余档的**随机采样构造失败**：随机 $(A,C)$ 下几乎不会有 $\operatorname{rank}H=\omega$ 的行空间
   （$\omega=3$ 要求 $V$ 与 $K_0$ 交 3 维，而 $V\subseteq U^\perp$ 把可用的 $K_0$ 方向限制死了）。
2. 正确的做法应是**先指定 $K_0$、$V$、再反解 $A,C$**（该项目已有"实现定理"可用于此），
   而不是随机采样。见 [attempts/04_realization](../../../q1_true/attempts/04_realization.md)（旧框架的 realization 结论）。
3. 顺带记一条**工具级教训**：在 $K_0$ 上做维数账时，**不能**用 $V^\perp$ 代替"$K_0$ 内的正交补"；
   $K_0$ 可能退化，$V^\perp\cap K_0$ 与 $(K_0\cap V)^\perp$ 不是一回事。

## 放弃原因

- 直接随机采样造不出合格层点；
- 诊断用的维数论证被数值否掉（$K_0$ 退化），没有现成的正确版本；
- 没有走"先定 $K_0,V$ 再反解"的路线（工作量更大）。

## 残留价值

- 一条**失败记录**，防止后续会话再"随机采样富余档"；
- 一条正确但容易踩的**工具提醒**：$K_0$ 退化时正交补≠零化子；
- 指明了可行路线：反解（realization）。

## 相关文件

- [attempts/338](338_dimension_map_p1.md)（维度图；富余档需 $r>p+1$）
- [attempts/04_realization](../../../q1_true/attempts/04_realization.md)（实现定理，旧框架）
- [attempts/328](../../decision_algorithms/attempts/328_quotient_pencil_theorem.md)（商铅笔）

## 状态

- 富余档实例：**[未构造成功]**。
- 相关猜想：**[已被数值否定]**，未进入任何命题。
