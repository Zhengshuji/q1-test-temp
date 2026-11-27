# 753 749 被 695 完全支配（一般 $k,d',t$）

> 2026-11-27。子 agent `indep-749` 的搜索 0 独立例；其给出的两行恒等式给出一般证明：749 触发 ⇒ 695 必失败。
> 状态：**[已证-纸面]**。

## 定理

设 $A=\mu I-Z'$、$T\subseteq\mathbb C^k$、$H$ 任意。则
$$\dim\big(\operatorname{row}A+T\big)=k-\dim\big(\ker A\cap T^\perp\big)\tag{$\star$}$$
且
$$\operatorname{row}(HA)\subseteq\operatorname{row}A.\tag{$\star\star$}$$
因此若 749 触发：
$$\dim(\ker A\cap T^\perp)\ge k-d'+1,$$
则
$$\dim\big(\operatorname{row}(HA)+T\big)\le\dim\big(\operatorname{row}A+T\big)\le d'-1<d',$$
即 **695 必失败**。等价地，695 通过 ⇒ 749 不触发。

## 证明

- $(\star)$：$(U+T)^\perp=U^\perp\cap T^\perp$，取 $U=\operatorname{row}A$，并用 $(\operatorname{row}A)^\perp=\ker A$（$x\perp$ 所有行 $\iff Ax=0$）。两边取维数即得。
- $(\star\star)$：$HA$ 的每一行是 $A$ 的行的线性组合。
- 代入 $A$ 即得。$\square$

## 推论

1. **749 被 695 支配**：$\{749\text{ 触发}\}\subseteq\{695\text{ 失败}\}$；预筛选链保留 695 即可删去 749（749 仍可作“直接给出公共根”的解释性引理）；
2. **751 的 42,768 组全部被 695 收编**现在是必然，不再依赖 $t=1$ 的特殊计算；
3. **752 的猜测被推翻**：其中“$t<d'-1$ 时可能出现独立情形”不成立——$(\star)(\star\star)$ 对任意 $k,d',t,H$ 都成立。

## 子 agent 的验证

- 400 组（构造 200 + 随机 200），749 触发 231 组，**0 个** 695 通过；max $\dim(\operatorname{row}HM+T)=3<4$；
- 300 组任意 $\mu$ 构造、750 组随机 $(Z',\mu)$ 的 $(\star)$ 恒等式检查全部通过；
- 3 个代表见证（$W=\operatorname{span}\{e_3,e_4\}$ 等）显示 $\operatorname{row}(HM)+T\subseteq W^\perp$ 维数 $\le3$。

## 意义

- 预筛选链可简化为
  $$704\to726\to725\to690\to695\to705\to\gcd;$$
- 705（$\rho_{d'}=1$）与 695 是**互不包含**的两类：638 触发 705 但 695 通过；
- 至此“结构性不可行”的两条主线明确为：**Bézout 子式退化（705）** 与 **方向性秩亏（695，含 749 为其特例）**。

## 状态

- 定理：**[已证-纸面]**；
- 子 agent 验证：**[精确验证 400 组]**；
- 752 的猜测：**推翻**。
