# 746 预筛选证书脚本：638 vs 733 的精确对照

> 2026-11-27。把 744/745 的对照写成可复现的精确脚本，并记录输出。
> 状态：**[精确验证]**。

## 脚本

`workspace/q1_false/feasibility_geometry/certificates/verify_prefilter_733_638.py`
（sympy，有理数/根式，无浮点；文件头有用法说明）。

功能：对给定 $(H,Z',Z,T,\mu)$ 计算
- $\operatorname{rank}(H(\mu I-Z'))$、$\dim(U\cap T)$、$\operatorname{cls}$ 与 $R+\dim V+\operatorname{cls}$；
- $P(\lambda)=\lambda H-ZH$ 的全部非零 $d$-子式、$\gcd$、Bézout 矩阵秩。

## 运行输出

```
== 638 ==
  d'= 2  rank(HM)= 1  dim(U∩T)= 0  cls= 1  R+dV+cls= 2
  #minors= 1  rank M= 2  bound(2d)= 4
  gcd(minors)= lam*(lam - 1)

== 733 ==
  d'= 2  rank(HM)= 1  dim(U∩T)= 1  cls= 0  R+dV+cls= 2
  #minors= 3  rank M= 4  bound(2d)= 4
  gcd(minors)= 1
```

## 解读

- 两者都满足 $d'=\operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls}=2$（744 第 6 条取等）；
- **638**：$P$ 秩 1 ⇒ 只有一个非零 2-子式（$\rho_2=1$），$\gcd=\lambda(\lambda-1)\ne1$，$\operatorname{rank}M=2<4$ ⇒ **不可行**（与 709 一致）；
- **733**：3 个非零 2-子式、$\gcd=1$、$\operatorname{rank}M=4$ ⇒ **可行**（与 733 一致）。

这直接复现了 745 的结论：取等本身不决定可行性，$\rho_{d'}$/$\gcd$ 才是区分量。

## 脚本的可靠性

- 638 的 $Z$ 由脚本按 $Z_iH=H_iZ'+g_ie_1$ 逐行解出（自由参数取 0），故只验证“存在某个 $Z$”的量；$P$ 的秩、子式数与 $\gcd$ 对所有可行 $Z$ 一致（687）；
- 733 的 $Z$ 用 733 的显式矩阵；
- 非零子式数 638 为 1，说明 $\rho_2=1$（705 的退化条件）。

## 待办

1. 把脚本扩展到任意输入（从 JSON/命令行读数据），作为 744 的批量筛选器；
2. 用 744 的七条 + $\rho_{d'}$ 对一批随机 $H$ 筛选，统计“取等但不可行”的比例。

## 状态

- 脚本：**[精确验证]**；
- 638/733 输出：**[精确验证]**。
