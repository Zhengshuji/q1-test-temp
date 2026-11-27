# 744 统一预筛选定理（方向性必要条件）

> 2026-11-27。把 704/725/726/690/695/734/739 包装成一条入口定理；只列必要条件，不做充分性声明。
> 状态：**[已证-纸面]**。

## 定理（可行 ⇒ 全部筛选通过）

设实例可行，$H$ 为秩 $d'>0$ 的可行解，$U=\operatorname{row}H$、$T=\{lW:lN=0\}$、$a=\dim(U\cap T)$、$t=\dim T$、$A=RZX$（$R$ 为 $X$ 的左逆）、$\operatorname{cls}_\mu=\dim\big((U+\operatorname{row}(H(\mu I-Z')))/U\big)$。则：

1. **（704）** $\operatorname{rank}H_A=d'$；
2. **（726）** $a\ge1$；
3. **（725）** 对每个 $\mu\in\sigma(A)$：$g_\mu=\dim\ker(\mu I-A)\le a$；
4. **（690）** 对每个 $\mu$：$\operatorname{rank}(\mu I-Z')\ge d'-t$；
5. **（695）** 对每个 $\mu$：$\dim(\operatorname{row}(H(\mu I-Z'))+T)\ge d'$；
6. **（734 + 739/743）** 对每个 $\mu$：
   $$\boxed{d'\ \le\ \operatorname{rank}\big(H(\mu I-Z')\big)+\dim(U\cap T)+\operatorname{cls}_\mu .}$$
7. **（739）** 若所有 $F_i=T\cap(U-H_iZ')\ne\varnothing$，则
   $$\dim E_H=\dim(U\cap T)+\operatorname{cls}_\mu;$$
   可行性保证 $F_i\ne\varnothing$（$F_i\ne\varnothing\iff H_iZ'\in U+T$，697）。

## 证明指针

- 1：704 的证明（$\lambda=0$）；
- 2、3：725 的引理 F 与复方阵必有特征值；
- 4、5：690/695；
- 6：734（定理 B）+ 739（$E_H$ 的维数）；
- 7：739 + 697。

## 逻辑强度

- 1–6 是**必要条件**；7 是**结构恒等式**（在可行性下）；
- 没有任何一条是充分的：733 通过全部条件且可行，638 也通过（见 745）却不可行；
- 因此预筛选只能**排除**，不能判定可行。

## 与 733 的对照

733：$d'=2$、$\mu=1\pm\sqrt2$ 时 $\operatorname{rank}(HM)=1$、$a=1$、$\operatorname{cls}=0$，第 6 条取等 $2=1+1+0$；它可行（$\gcd=1$）。

## 待办

1. 把 1–7 写成脚本（`verify_prefilter.py`）对候选 $H$ 批量检查；
2. 研究“取等但不可行”的 638（745），找与 733 的代数差异。

## 状态

- 1–7：**[已证-纸面]**；
- 脚本化：**[未做]**。
