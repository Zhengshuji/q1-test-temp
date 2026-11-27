# 724 $a=0$ 不变性：证明尝试与障碍

> 2026-11-27。尝试证明 723 的猜想 $a=0\Rightarrow Z(\operatorname{im}H)\subseteq\operatorname{im}H$，记录障碍。
> 状态：**[开放]**（证明未完成）。

## 设定

$a=0$（$U\cap T=0$），$H=XV$，$G=ZH-HZ'$ 的行在 $T$。由 723，目标等价于 $\Pi G=0$，即 $Z(\operatorname{im}X)\subseteq\operatorname{im}X$。

## 可用的关系

1. $G$ 行在 $T$ ⇒ 在商空间 $\mathbb C^k/T$ 中
   $$ZX\,\overline V=X\,\overline{VZ'} .$$
   （这里 $\overline{\cdot}$ 表示模 $T$；该式不需要 $Z'$ 诱导作用，只对行向量取商。）
2. $a=0$ ⇒ $V$ 在商空间中的像 $\overline V$ 行满秩 $d$。
3. 兼容性（697）$H_iZ'\in U+T$。

## 障碍

- (1) 只给出 $ZX$ 在 $\overline V$ 上的作用，而 $\overline V$ 是 $V$ 的像（$d$ 维），**不直接约束 $ZX$ 的列**；
- 目标 $Z(\operatorname{im}X)\subseteq\operatorname{im}X$ 是关于 $Z$ 在 $\operatorname{im}X\subset\mathbb C^q$ 上的作用，而 (1) 是关于行空间 $\mathbb C^k$ 的商——两者方向不同（$Z$ 是 $q\times q$，作用在列向量上；$G=ZH-HZ'$ 的方程混合了左右）；
- 需要额外的“列-行”对偶关系（例如 $X$ 与 $V$ 的配对 $XV=H$），才能把 (1) 翻译成对 $ZX$ 的约束。

## 一个失败的构造尝试

取 $k=4$、$T=e_1$、$U=\operatorname{span}\{e_2,e_3\}$（$a=0$，$U+T=\operatorname{span}\{e_1,e_2,e_3\}\subsetneq\mathbb C^4$）。
若 $H$ 的行为 $e_2,e_3$、$Z'=\operatorname{diag}(1,0,0,0)$，则 $HZ'=0$，故 $G=ZH$ 行在 $T$ 且 $ZH$ 行在 $U$ ⇒ $G\in U\cap T=0$ ⇒ $ZH=0$。
此时 $Z$ 必须杀死 $\operatorname{im}H$，故 $ZX=0$、$\Pi G=0$——但这只是特例，不能说明一般情形。

## 结论

- $a=0$ 的不变性在 $d=1$ 与 39 个数值例中成立；
- 但一般证明需要新的“行-列”桥接引理（把 $G$ 的行约束转成 $Z$ 在 $\operatorname{im}X$ 上的约束）；
- 这是当前 $T$-纤维理论的核心缺口。

## 下一步

1. 寻找行-列桥接：利用 $H=XV$、$X$ 列满秩、$V$ 行满秩，把 $G=ZH-HZ'$ 左乘 $V^+$ 得到 $ZX=GV^++XVZ'V^+$（721），再用 $G$ 行在 $T$ 与 $a=0$ 分析 $GV^+$；
2. 若 $GV^+$ 的列落在 $\operatorname{im}X$，则得证——这需要 $G$ 的列结构，而不仅是行；
3. 与 ChatGPT 讨论。

## 状态

- 证明尝试：**[未完成]**；
- $d=1$ 与数值：**[已证/验证]**。
