# 493 $q=4$、$k=5$、$L_0=[e_1;e_2]$ 的整族不可行

> 2026-11-27。把 492 的“子族”升级为**整族**：在 $q=4$、$k=5$ 的移位族里，
> 秩退化只剩 $\operatorname{rank}H=3$（$\operatorname{rank}H=4$ 本身不可行），而秩 3 迫使
> $r_2\in\operatorname{span}(e_1,e_2,r_1)$——正是 492 证明恒不可行的类型。故**整族无可行实例**。
> 状态：**[已证-纸面]**（限于 $q=4$、$k=5$、$L_0=[e_1;e_2]$、$A$ 移位）。

## 引理 A：$\operatorname{rank}H=4$ 不可行

$H$ 为 $4\times5$，$\operatorname{rank}H=4$。$(5a)$ 给 $\ker H\subseteq\ker H_A$，故 $H_A=ZH$
（$Z$ 为 $4\times4$；$H$ 行满秩，取右逆）。于是
$$P(\lambda)=\lambda H-H_A=(\lambda I_4-Z)H,\qquad \operatorname{rank}P(\lambda)=\operatorname{rank}(\lambda I_4-Z).$$
$\det(\lambda I-Z)$ 在 $\mathbb C$ 上有 4 个根，故存在 $\lambda$ 使 $\operatorname{rank}P<4$，$(5b)$ 失败。$\square$

（一般地：$q=4$ 的可行实例必有 $\omega\le3$。）

## 引理 B：$\operatorname{rank}H=3$ 的两种情形

$H$ 的行是 $e_1,e_2,r_1,r_2$，其中 $e_1,e_2$ 独立。$\operatorname{rank}H=3$ 分两种：

- **(i) $r_1\notin\operatorname{span}(e_1,e_2)$**：则 $\operatorname{span}\{e_1,e_2,r_1\}$ 已是 3 维，故
  $r_2\in\operatorname{span}\{e_1,e_2,r_1\}$——即 492 的子族；
- **(ii) $r_1\in\operatorname{span}(e_1,e_2)$**：则第三个独立方向必须来自 $r_2$，
  即 $r_2\notin\operatorname{span}(e_1,e_2)$。

**（ChatGPT 2026-11-27 指出的缺口：原表述漏了 (ii)。下面补上。）**

### 情形 (ii) 也不可行

写 $r_1=\beta e_1+\gamma e_2$，则 $r_1M=\gamma e_1$。$\ker H=\{x:x_1=x_2=0\}$（3 维）。
$(5a)$ 要求对一切这样的 $x$，$H_Ax=0$；其中只剩
$$r_2M\cdot x=r_{2,4}x_3+r_{2,5}x_4=0\quad(\forall x_3,x_4,x_5),$$
故 $r_{2,4}=r_{2,5}=0$。于是 $r_2M=(r_{2,2},r_{2,3},0,0,0)$，而 $H_A$ 的四行
$0,\ e_1,\ \gamma e_1,\ r_2M$ 全在 $\operatorname{span}\{e_1,e_2\}$ 里，$\operatorname{rank}H_A\le2$；
$\lambda=0$ 处 $P(0)=-H_A$ 秩 $\le2<3$，$(5b)$ 失败。$\square$

## 定理：整族不可行

情形 (i) 由 492 排除；情形 (ii) 由上一节排除；引理 A 排除 $\operatorname{rank}H=4$。
故 $q=4$、$k=5$、$L_0=[e_1;e_2]$、$A$ 移位的族**没有可行实例**。$\square$

## 意义

- 该族不能承载任何门（可行集为空）；
- 与 490（$k=4$ 有可行点）对照：$k=5$ 的额外坐标改变了 $\ker H$ 的维数与 $(5a)$ 的强度，
  使“秩退化”与“$H_A$ 满秩”不可兼得；
- 下一族必须换 $q$（$q=5$）或换 $H_{A,0}$ 的结构（例如 $L_0$ 取非 $e_1,e_2$ 的行），
  或者放弃 $q=4$ 的秩门。

## 相关

- [492](492_k5_span_subfamily.md)、[490](490_q4_family_probe.md)、[PLAN](../PLAN.md)

## 对照：换 $A$ 后不再恒不可行（493b）

把 $A$ 从“下移位”换成 $K_0$ 上的上移位 $J_5$（$e_i\mapsto e_{i+1}$，$e_5\mapsto0$；$Ae_7=e_6$，仍 $C=e_7$、$k=5$）：
$H_{A,0}=[e_2;e_3]$，$rM=(0,r_1,r_2,r_3,r_4)$。在同一个 $r_2=\alpha r_1+\beta e_1+\gamma e_2$ 子族上取 300 个随机点：

| 量 | 数值 |
|---|---|
| $\operatorname{rank}H=3$ 且满足 $(5a)$ | **4 / 300** |
| 其中 $(5b)$ 成立（可行） | **4 / 4** |

例：$r_1=[2,0,-2,0,0]$、$(\alpha,\beta,\gamma)=(1,1,1)$，$\gcd=1$。

**结论**：493 的整族 no-go 是**下移位 $A$ 的偶然**，不是 $q=4,k=5$ 的普遍现象。
换成上移位后可行点出现，但可行集仍是开集（没有“被 $(5a)$ 强制的门”）——所以这个族**也不是门**，
只是不再是空集。下一步若要找门，需要换 $H_{A,0}$ 的结构或让 $K_0$ 不 $A$-不变。

## 外部复核（ChatGPT，2026-11-27）

第一版漏了 $r_1\in\operatorname{span}(e_1,e_2)$ 的分支；补上后 ChatGPT 复核：
**整族 no-go 已闭合**（三种情形覆盖全部：$\operatorname{rank}H=4$、秩 3 且 $r_1\notin\operatorname{span}$、
秩 3 且 $r_1\in\operatorname{span}$）。但**不自动推广**到其他 $k$、其他移位矩阵或其他 $H_0,H_{A,0}$ 结构。

## 状态

- 引理 A、B 与定理：**[已证-纸面]**（该族；ChatGPT 复核通过）；
- 一般 $q=4$（其他 $L_0$/$A$）：**[未证]**。
