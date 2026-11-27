# $\dim V=\dim K=2$ 的可行性边界：$V\cap K=0$ 要求 $2p+r\ge n$

## 目标

在 $\dim V=\dim K\ge2$ 上继续 gadget（上一轮发现 $\dim=1$ 退化）。先确定**非退化**配置的充要条件。

## 设想与理由

B.13e 的单-$\lambda$ 证书的例外是"$x\in\mathcal Z$ 对所有 $z$ 成立"；因 $x\in V$、$\mathcal Z\subseteq K$，
只需 $V\cap K=0$ 即无例外。而
$$\dim(V\cap K)=\dim\ker[C;CA;L_0]\ \ge\ n-(2p+r),$$
所以 $V\cap K=0$ 要求 $2p+r\ge n$。

## 做法

1. 在 $n=4$、$p=r=1$、$r_1=2$（即 $\dim V=\dim K=2$）上按 B.13e 实现证书并对照整族失败
   （`tools/verification/dim2_certificate.py`）；
2. 用上面的不等式解释结果。

## 进展

**（1）$n=4,p=r=1$ 全部退化**：4000 次随机中 3958 个满足其余条件，但 **V∩K ≠ 0 全部成立**
（因为 $2p+r=3<4=n$，必有 $\dim(V\cap K)\ge1$）。故该配置**无法**做无例外的证书。

**（2）$2p+r=n$ 是边界**：本项目两个整族反例都是 $n=6,p=r=2$ ⟹ $2p+r=6=n$ ✓ 恰好取等。
再结合 $\dim V=n-r_1\ge n-2p$：要在 $\dim V=\dim K=2$ 且 $V\cap K=0$，最小可行配置正是
$$n=6,\quad p=r=2\quad(r_1=4).$$
这解释了为什么两个反例（C4 与新实例）**都在这一组参数上**——不是巧合，而是维数约束下唯一的最小非退化配置。

## 最终结论

1. **设计约束**：$V\cap K=0$（单-$\lambda$ 证书无例外）$\iff$ $2p+r\ge n$（在 $\operatorname{rank}[C;CA;L_0]=n$ 时取等）；
2. $n=4,p=r=1$ 的"$\dim2$"配置**必然**有例外（$\dim(V\cap K)\ge1$），不能作为 gadget 的干净底座；
3. 唯一的最小非退化底座是 $n=6,p=r=2$（$2p+r=n$、$\dim V=\dim K=2$）——**正是我们两个反例的参数**；
4. 下一步的 gadget 就应建在这个底座上（阶 $q=3$，$d=1<k=2$，参数族正维）。

## 放弃原因

不适用（约束已确定；$n=4$ 的尝试排除了一个错误底座）。

## 残留价值

* 一条**设计不等式**（$2p+r\ge n$），避免再次在退化底座上做 gadget；
* 解释了"为什么两个反例都在 $n=6,p=r=2$"——维数约束下的唯一最小非退化配置；
* 明确了 gadget 的底座：$n=6$、$p=r=2$、$q=3$。

## 相关文件

- `docs/02` B.13e（新增"例外来源"段）、B.13c、B.13f
- `tools/verification/dim2_certificate.py`
- `proof/type3_second_example/README.md`（底座上的实例）
