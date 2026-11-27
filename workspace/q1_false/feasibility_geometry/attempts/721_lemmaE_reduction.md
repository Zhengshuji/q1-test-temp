# 721 引理 E 的精确归约：$r=\operatorname{rank}((I-XR)GV^+)$

> 2026-11-27。把引理 E 的秩缺陷化为 $G$ 的投影，得到弱界 $r\le t$，并定位强界 $r\le a$ 的缺口。
> 状态：**[已证-纸面]**（弱界与归约）+ **[开放]**（强界）。

## 归约

设 $H=XV$（$X$ 列满秩、$V$ 行满秩）、$R$ 为 $X$ 的左逆（$RX=I$）、$V^+$ 为 $V$ 的右逆（$VV^+=I$）。
由 $ZH-HZ'=G$ 与 $H=XV$：
$$ZXV=G+XVZ'\ \Longrightarrow\ ZX=(G+XVZ')V^+ .$$
于是
$$(I-XR)\,ZX=(I-XR)\,G\,V^+ + \underbrace{(I-XR)X}_{=0}\,VZ'V^+=(I-XR)\,G\,V^+ .$$
因此
$$\boxed{r:=\operatorname{rank}(ZX-XA)=\operatorname{rank}\big((I-XR)GV^+\big)\le\operatorname{rank}G .}$$

## 弱界

$G$ 的行在 $T$ ⇒ $\operatorname{rank}G\le t$，故
$$r\le t .$$
结合 717 的 $k-d+a$ 界，有 $r\le\min(t,\ k-d+a)$。

## 强界 $r\le a$ 的缺口

- $Z'=0$ 时，$HZ'=0$ ⇒ $G=ZH$ 的行在 $U$，又 $G$ 行在 $T$ ⇒ $G$ 行在 $U\cap T$ ⇒ $\operatorname{rank}G\le a$ ⇒ $r\le a$（720）；
- 一般 $Z'\ne0$ 时，$G_i=(ZH)_i-(HZ')_i\in T$，但不一定在 $U$；需要证明 $(I-XR)G$ 的秩 $\le a$，即 $G$ 的 $T$-分量中“落在 $U$ 外”的部分被投影杀死。

## 检验

- 718（$k=3$，44 例）：未找到 $r>a$；
- 本轮补充：$a=0$（$U\cap T=0$）的 31 个相容实例中，$r=0$——与“$a=0$ 时 $r\le0$”一致，但未证。

## 下一步

1. 证明或反驳：$a=0\Rightarrow G$ 的 $T$-分量完全落在 $U$ 的可补方向内 ⇒ $r=0$；
2. 一般 $a$：尝试用 $G$ 的分解（$T$-分量按 $U\cap T$ 与补方向）证明 $r\le a$；
3. 与 ChatGPT 核对。

## 状态

- 归约与弱界：**[已证-纸面]**；
- 强界：**[M2 提案]**。
